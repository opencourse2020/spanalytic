# System Design

## 1. What the system has to do

For each client, on a monthly cycle:

1. Build a geo-specific prompt set a real patient would type.
2. Run it across every tracked AI assistant, several times, through official APIs.
3. Detect which clinics were named, in what order, with what sentiment, and which
   sources the assistant cited.
4. Crawl the client's site and diagnose why they are absent.
5. Produce remediation artefacts — copy, schema, GBP values, submission packages.
6. Render a PDF and email it.

Everything else is supporting infrastructure.

**Scale it must handle:** 48 prompts × 4 engines × 3 repetitions = 576 responses per
run, per client, per month. At 100 clients that is 57,600 paid API calls a month.
This number drives every design decision below.

## 2. Data model

### clinics

```
Client            name, slug, status, metro, timezone, stripe_customer_id
Location          client → address, lat/lng, gbp_place_id
Provider          client → name, credential, is_medical_director
Service           client → name, price_low_cents, price_high_cents, unit, publishable
Competitor        client → name, aliases[], website
ClaimsGuardrail   client → phrase, reason        # things this clinic may never say
```

`Service.publishable` matters commercially: engines will not recommend a clinic whose
price they cannot state, and some clients refuse to publish. The flag makes that
visible in the report rather than silently degrading results.

### prompts

```
PromptSet         client → version, generated_at, is_active
Prompt            prompt_set → text, intent, service (nullable), neighborhood (nullable)
```

Prompt sets are **versioned and immutable**. Editing a prompt creates a new set
version. Comparing month 3 against month 1 is only meaningful if the instrument did
not change, and the delta report is the thing that renews the retainer.

### measurement

```
Engine            key, display_name, provider, is_active
Run               client, prompt_set, started_at, finished_at, status,
                  budget_cap_cents, spend_cents, completion_rate
Response          run, prompt, engine, repetition,
                  model_id, model_version, grounding_enabled, temperature,
                  raw JSONB, text, status, error, cost_cents, created_at
Mention           response, subject_type (client|competitor|other),
                  competitor (nullable), matched_name, position, sentiment,
                  price_stated (bool)
Source            domain (unique), display_name, category
Citation          response, source, url, rank
```

Notes that matter:

- `Response.raw` is JSONB. Postgres compresses it well and it is the audit trail
  behind every number we print. Never discard it.
- `Mention.position` is the ordinal in the assistant's answer. "Named third" and
  "named first" are different products commercially.
- `Source` is global, not per-client. Yelp is Yelp for everyone, and cross-client
  source frequency is a genuine data asset — it tells us which directories matter in
  a metro before we have a client there.

### diagnosis / remediation

```
Crawl             client, started_at, pages_found, robots_respected
Page              crawl → url, title, h1, word_count, has_schema,
                  schema_types[], answer_block_score, price_mentioned
Gap               client, kind, severity, source (nullable), detail JSONB, resolved_at
AnswerBlock       client, prompt (nullable), heading, body, claims_status, approved_by
SchemaPackage     client, jsonld JSONB, validated_at, installed_at
CitationTarget    client, source, priority, status, submitted_at, accepted_at
Submission        citation_target → payload JSONB, submitted_at, outcome
```

`Gap.kind` is an enum, not free text: `MISSING_SCHEMA`, `NO_PUBLISHED_PRICE`,
`NON_EXTRACTABLE_PAGE`, `ABSENT_FROM_SOURCE`, `NAP_INCONSISTENT`,
`CREDENTIALS_NOT_MACHINE_READABLE`. Ranked gap lists are only comparable across
months if the taxonomy is fixed.

### reports

```
Report            client, run, kind (baseline|delta|monthly), period_start, period_end,
                  metrics JSONB, pdf_file, sent_at
```

`metrics` is a frozen snapshot. Reports must render identically a year later even if
aggregation logic changes. Never compute report figures at render time.

## 3. The mention-detection problem

This is the hardest correctness problem in the system and the easiest to get quietly
wrong. Clinic names are messy: "Lumen Aesthetics & Wellness" appears as "Lumen
Aesthetics", "Lumen Med Spa", or "Lumen".

Approach, in order:

1. Normalise: casefold, strip punctuation, drop stopword suffixes (`med spa`,
   `aesthetics`, `wellness`, `skin`, `clinic`).
2. Exact match against `Competitor.aliases[]` and the client's alias list.
3. Trigram similarity via `pg_trgm` above a tuned threshold for the remainder.
4. Anything scoring in the uncertain band is written to a review queue, not guessed.

Never let fuzzy matching silently inflate a client's mention rate. An
over-reported baseline produces a delta report that shows a decline, which is worse
than a low starting number.

## 4. Pipeline execution

```
run_measurement(client_id)
  └── chord(
        group(query_engine.s(response_id) for each prompt × engine × repetition),
        finalise_run.s(run_id)
      )
```

- A `Response` row is created with `status=PENDING` **before** the API call. Retries
  look up the existing row rather than creating a second one. This is the primary
  defence against duplicate spend.
- `MeteredClient` checks `run.spend_cents` against `run.budget_cap_cents` before every
  call and aborts the run if exceeded. A runaway loop is the single most plausible way
  this business loses money.
- Per-engine rate limits are enforced with a Redis token bucket. Celery task retries
  use exponential backoff with jitter.
- Individual failures do not fail the run. `finalise_run` computes `completion_rate`,
  and any report generated from a run below 95% completion prints that fact.

Long-lived fan-out is why Celery is the right choice here over a simpler queue —
`chord` gives correct completion semantics with retries.

## 5. Engine adapters

```python
class EngineAdapter(Protocol):
    key: str
    def query(self, prompt: str) -> EngineResult: ...
```

`EngineResult` carries `text`, `citations`, `model_id`, `model_version`,
`grounding_enabled`, `cost_cents`, `raw`.

Provider quirks are normalised inside the adapter. `Response` never grows a
provider-specific column. Adding an engine must not require a schema change.

Adapters are tested against recorded fixtures. **No test may make a live paid call.**

## 6. Report rendering

HTML template → WeasyPrint → PDF. The same design tokens as the marketing site
(`frontend-rules.md`), so a report looks like it came from the same company.

Every report includes a method section printing: engines queried, model versions,
grounding configuration, prompt set version, repetition count, run date, completion
rate. This is a contractual promise, not a nicety — it is our stated differentiator
against vendors who scrape.

White-labelling swaps a logo and an accent colour. It never removes the method
section.

## 7. Security and data posture

- No PHI. Enforced by convention, code review, and a CI check that greps migrations
  for prohibited field names (`patient`, `mrn`, `dob`, `diagnosis`, `chart`).
- Client credentials (GBP access, CMS logins) are the sensitive assets here. Store
  encrypted at rest with a KMS-backed key; never in plain columns, never in logs.
- Stripe: webhook signature verification mandatory. Subscription state is derived
  from Stripe, never set by application code.
- Crawler respects `robots.txt` and identifies itself honestly with a contact URL.

## 8. Deliberate non-goals

- **No client login.** Deliverables go out as PDFs by email. A portal is the obvious
  next feature and the wrong one — it converts a service into a dashboard product
  competing with well-funded incumbents.
- **No real-time measurement.** Runs are monthly. Nothing here needs to be live, and
  live querying multiplies cost by orders of magnitude for no client value.
- **No multi-region.** One VPS, one Postgres, one Redis until it hurts.
- **No attribution modelling.** AI answers produce no referral traffic. We measure
  visibility and say so plainly. Building a bookings-attribution feature would mean
  shipping a number we cannot defend.

## 9. What will break first

At roughly 100 active clients the constraint is not infrastructure — 57,600 monthly
API calls on one VPS is unremarkable. It is the human review step: claims-safety
sign-off on everything published under a clinic's name, at about 45 minutes per
client per month. Design accordingly: the review queue UI is the interface that most
deserves engineering attention, because it is the only thing that does not scale.

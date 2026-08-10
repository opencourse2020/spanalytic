# Spa Analytic — Engagement Specification

**Worked example client:** Lumen Aesthetics & Wellness, Austin TX *(fictional — used throughout to show exactly what changes hands)*
**Engagement:** AI Visibility Audit & Remediation — $995 setup, then $499/month
**Duration to first delivered result:** 14 days. Measurable delta at day 30.

---

## Part 1 — What the client provides

The single biggest reason med spa engagements stall is intake friction. A clinic owner injecting patients all day will not fill in a 40-field form. Everything below is split into what blocks the work and what merely improves it.

### 1a. Required before we start — 15 minutes, one form

| Item | Why it's needed | Example (Lumen) |
|---|---|---|
| Website URL | Crawl target for the extractability audit | lumenaesthetics.com |
| Google Business Profile — manager access | GBP fields feed the local pack, which several engines cite directly | Invite sent to ops@spanalytic.com |
| Primary metro + up to 3 neighborhoods | Prompts are geo-specific or they measure nothing | Austin; South Congress, Westlake, Domain |
| Up to 5 competitors you care about | Share-of-voice baseline | Bluebonnet Aesthetics, Zilker Skin & Laser, Violet Crown Aesthetics, Hill Country Med Spa, Congress Ave Skin Studio |
| Service list, with price ranges you are willing to publish | The hard one. Engines will not recommend a clinic whose price they cannot state | Neurotoxin $12/unit; filler $650–850/syringe; microneedling $350; semaglutide program $299/mo |
| Provider names, credentials, medical director | Trust signals; also a compliance requirement in Texas | Dr. Priya Raman, MD (medical director); 2 NPs, 1 RN injector |
| Claims guardrails | Anything counsel or your medical director has told you never to say | No "permanent"; no outcome guarantees; no before/after without written consent on file |

### 1b. Needed before remediation ships — week 2

| Item | Why | If unavailable |
|---|---|---|
| CMS access (WordPress editor role or equivalent) | To install copy blocks and schema | We hand over a paste-ready implementation packet; your web person does it in ~45 min |
| Directory logins, or permission to claim | Yelp, RealSelf, Healthgrades profiles | We prepare submissions; you approve and submit |
| Logo, brand fonts, 3–5 approved photos | Report white-labelling and any new pages | We deliver unbranded |
| Written consent status for any before/after imagery | Texas claims exposure sits here | We exclude imagery entirely from remediation |

### 1c. What we never ask for, and never touch

No patient records. No EHR or PM system access. No appointment data, no chart data, no patient names, no PHI of any kind. Nothing we do requires it, and asking for it would drag a marketing engagement into HIPAA scope for no benefit. This is stated in the MSA, not just here.

### 1d. Client time commitment, total

- Week 1: 15 minutes (intake form) + 5 minutes (GBP invite)
- Week 2: ~30 minutes reviewing the remediation package before it goes live
- Monthly thereafter: ~10 minutes reviewing the report

If it exceeds this, the productisation has failed and the retainer will churn.

---

## Part 2 — What gets delivered

### Timeline

| Day | Event | Client effort |
|---|---|---|
| 0 | Contract signed, intake submitted, deposit charged | 20 min |
| 1–4 | Baseline measurement runs. Silent. | None |
| **5** | **Deliverable 1 — Baseline Visibility Report** | 15 min to read |
| 6–12 | Remediation build | None |
| **14** | **Deliverable 2 — Remediation Package + implementation** | 30 min approval |
| 15–29 | Citation-source submissions land, re-crawl period | None |
| **30** | **Deliverable 3 — Delta Report.** Retainer begins | 10 min |
| Monthly | **Deliverable 4 — Monthly Visibility Report + 2 new assets** | 10 min |

---

### Deliverable 1 — Baseline Visibility Report (day 5)

A 9-page PDF. The client's logo if white-labelled, ours if not.

**Method disclosed on page 2, not buried.** 48 buyer-intent prompts, run across 4 engines, 3 repetitions each = 576 responses. Queried through official APIs with search grounding enabled. Stated plainly: this is a calibrated proxy for consumer assistant behaviour, not a capture of it. Any vendor claiming otherwise is scraping, which breaks and violates terms.

**Sample of the prompt set (48 total, 12 shown):**

```
best med spa in Austin for Botox
where to get lip filler south Austin
who does the best microneedling near me Austin TX
how much does Botox cost in Austin
med spa Austin that does semaglutide weight loss
is there a nurse injector in Westlake I can trust
best place for laser hair removal Austin
med spa near the Domain with good reviews
what should I look for in a med spa medical director
Botox vs Dysport which clinic in Austin offers both
affordable filler Austin without looking overdone
med spa Austin open Saturday
```

**Headline findings for Lumen:**

| Metric | Lumen | Category leader (Bluebonnet) |
|---|---|---|
| Mention rate across 576 responses | 11% | 43% |
| Appears in top-3 named recommendations | 4% | 31% |
| Recommended with a price stated | 0% | 18% |
| Sentiment when mentioned | Neutral | Positive |

**Where the recommendations actually came from.** The 14 sources cited most often across Austin med spa prompts, with Lumen's status on each:

| Source | Citation frequency | Lumen present? |
|---|---|---|
| Yelp | 31% of responses | Yes — unclaimed, 11 reviews |
| Google Business Profile / local pack | 28% | Yes — incomplete (no services, no hours exceptions) |
| RealSelf | 19% | **No profile** |
| Reddit r/Austin | 14% | Mentioned twice, both 2023 |
| Austin Monthly "Best of" | 11% | No |
| Healthgrades | 9% | Provider listed, clinic not linked |
| Expertise.com "Best Med Spas Austin" | 8% | No |
| Do512 | 6% | No |
| *(6 further sources listed in full report)* | | |

**The finding that matters, stated in one line:** Lumen loses on the 82% of citations that come from third-party sources, not on its own website. That reframes the entire engagement, and it is why the remediation package below is weighted toward off-site work.

---

### Deliverable 2 — Remediation Package (day 14)

Six components. Each is a file, not a recommendation.

**2.1 — Answer blocks (12 pieces of copy, ~150 words each)**
Written to be extractable: a direct answer in the first sentence, a specific number, then context. Mapped one-to-one against prompts Lumen currently loses.

> *Sample — mapped to "how much does Botox cost in Austin":*
> **What does Botox cost at Lumen Aesthetics?** Neurotoxin treatment at Lumen is priced at $12 per unit. A typical forehead and glabellar treatment uses 20–40 units, placing most first appointments between $240 and $480. Pricing is per unit rather than per area, so you pay only for what is administered. All injections are performed by a licensed RN or NP injector under the supervision of medical director Dr. Priya Raman, MD, following a good faith exam as required in Texas. Consultations are complimentary and no treatment is administered on the same visit unless the good faith exam is complete.

Note what that paragraph does: answers the literal question in sentence one, contains a citable number, names the credentialed provider, and states Texas GFE compliance — which is simultaneously a trust signal and a legal accuracy requirement.

**2.2 — Schema package (`lumen-schema.jsonld`)**
`MedicalBusiness` + `MedicalProcedure` entries per service, `Person` entries with credentials for each injector, `offers` with the published price ranges, `openingHoursSpecification`, consistent NAP. Paste-ready, validated.

**2.3 — Google Business Profile field sheet**
Exact values to enter, field by field: 14 service entries with descriptions and prices, category primary/secondary, attributes, 8 Q&A pairs seeded, hours exceptions. Not "optimise your GBP" — the literal strings.

**2.4 — Citation-source targeting plan** *(the highest-leverage component)*
The 14 cited sources, ranked by frequency × difficulty, with:
- RealSelf: full profile submission drafted, 6 procedure pages, provider bios — ready to submit
- Yelp: claim instructions, category corrections, 12 seeded Q&A
- Expertise.com and Do512: submission copy drafted, deadlines noted
- Austin Monthly: editorial pitch drafted for the next "Best of" cycle, with dates
- Healthgrades: clinic-to-provider linkage fix
- Tracked in a shared sheet with status per source, updated monthly

**2.5 — Claims-safety pass**
Every line of delivered copy run against a Texas med spa filter: no outcome guarantees, no "permanent", no comparative superiority claims without substantiation, correct GFE and medical-director language, no imagery implied without documented consent. Flagged items returned to the client's medical director, never quietly softened. Two items were flagged in Lumen's existing site copy and reported even though they were outside our scope.

**2.6 — Implementation**
We install where we have CMS access. Where we don't, a paste-ready packet with screenshots. Either way, verified live before day 14 closes.

---

### Deliverable 3 — Delta Report (day 30)

Same 48 prompts, same engines, same repetitions. The only thing that changed is the client.

| Metric | Day 0 | Day 30 |
|---|---|---|
| Mention rate | 11% | 24% |
| Top-3 named recommendation | 4% | 13% |
| Recommended with a price stated | 0% | 21% |
| Sources where Lumen is present | 2 of 14 | 6 of 14 |

**And a section titled "what has not moved yet," because it protects the renewal.** RealSelf and Expertise submissions were accepted on day 19 and 22 but engine re-crawl typically lags 30–90 days. The Austin Monthly pitch targets a cycle that closes in November. On-site changes register fastest; earned media is where the compounding happens, and it is slow by nature. A client who is told this at day 30 renews. A client who is shown a hockey stick and then a flat month two does not.

---

### Deliverable 4 — Monthly retainer, $499

| Every month | |
|---|---|
| Re-run | Full 48-prompt set, 4 engines, tracked over time |
| Report | 4-page PDF: movement, competitor share-of-voice shifts, new sources appearing in citations |
| New assets | 2 new answer blocks targeting prompts still being lost |
| Off-site | 2 new citation-source submissions or refreshes |
| Alerts | Email if a competitor gains >10 points of share of voice, or a new engine/source enters the citation mix |
| Prompt set maintenance | Add prompts for new services; retire dead ones. GLP-1 prompts didn't exist in 2022 |

**Why this recurs rather than completing.** Competitors move, engines change how they ground answers, new sources enter the citation pool, and the clinic adds services. The month-one job is a fix; the month-twelve job is defence and expansion. If a client ever asks "am I done?", the honest answer is that they can stop and watch it decay — and some should, which is why we don't lock people into annual terms they'll resent.

---

## Part 3 — What we do not promise

Put in the proposal, not the fine print. It costs a small number of deals and prevents every bad one.

- **No ranking guarantee.** No one controls what a language model says. We move measurable inputs and report what happened.
- **No patient-volume claim.** <a>Zero-click AI answers generate no referral session</a>, so attributing bookings to AI visibility is not currently possible with integrity. We measure visibility. If someone sells you attribution here, ask to see the method.
- **No medical claims, ever.** We will not write outcome language, and we will refuse a request to.
- **No scraped consumer interfaces.** Official APIs only. Stated in the method section of every report.
- **Cancel any time on the retainer.** Setup fee non-refundable once the baseline report is delivered.

---

## Part 4 — Internal notes (not client-facing)

**Delivery cost for this engagement:** ~$14 in API and data for the baseline, ~$9/month ongoing. Gross margin above 95%.

**Where the time actually goes:** stages 1–4 of the agent pipeline run unattended. The human hours are the claims-safety review and the sign-off on anything published under the clinic's name — roughly 2 hours for setup, 45 minutes monthly. That 45 minutes is the number that sets the ceiling described in the run book.

**The intake form is the conversion bottleneck, not the price.** Pricing is the field clinics hesitate on. If a prospect refuses to publish prices, the honest response is that the engagement will underperform — engines will not recommend what they cannot quantify — and to say so before taking the money rather than after.

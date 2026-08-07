# CLAUDE.md

Instructions for working in this repository.

## What this is

Spa Analytic measures whether AI assistants recommend a given medical spa when a
patient asks where to go, then produces and installs the fixes that change the
answer. Two revenue lines: a $995 setup engagement and a $499/month retainer.

The product is a **delivery pipeline that produces PDFs and copy**, not a customer-facing
dashboard. Clients receive reports by email. Resist any change that turns this into a
SaaS dashboard — that market is saturated and it is not what we sell.

## Stack

| Layer | Choice |
|---|---|
| Backend | Django 5.x, Python 3.12 |
| Database | PostgreSQL 16 |
| Async | Celery + Redis |
| Frontend | Django templates, vanilla CSS and JS. No SPA framework |
| PDF | WeasyPrint (HTML/CSS → PDF, reuses the design tokens) |
| Payments | Stripe (Checkout + Billing) |
| Hosting | Single VPS, Docker Compose |

## Layout

```
config/            settings/{base,dev,prod}.py, celery.py, urls.py
apps/
  core/            shared models, mixins, the metered API client
  clinics/         Client, Location, Provider, Service, Competitor
  prompts/         PromptSet, Prompt, generation logic
  measurement/     Engine adapters, Run, Response, Mention, Citation, Source
  diagnosis/       Crawl, Page, Gap
  remediation/     AnswerBlock, SchemaPackage, CitationTarget, Submission
  reports/         Report generation and rendering
  billing/         Stripe webhooks and subscription state
static/            css/, js/  — see frontend-rules.md
templates/         Django templates and PDF templates
docs/              system-design.md, frontend-rules.md
```

One app per bounded concept. If you are adding a model and cannot name which app it
belongs to, the design is wrong — stop and ask.

## Commands

```bash
make up              # docker compose up (postgres, redis, web, worker)
make migrate         # python manage.py migrate
make test            # pytest
make lint            # ruff check . && ruff format --check .
make shell           # python manage.py shell_plus
make worker          # celery -A config worker -l info
```

Always run `make lint` and `make test` before considering a task done.

## Hard rules

These are not style preferences. Breaking any of them creates legal or financial
exposure.

1. **Official APIs only.** Never scrape or automate a consumer chat interface. It
   violates provider terms, breaks without warning, and every client report states
   in writing that we do not do it.
2. **No PHI, ever.** No model may store patient names, appointment data, chart data,
   or anything from a clinic's EHR. Nothing in the product needs it. A migration that
   adds such a field should be rejected outright.
3. **Every paid API call goes through `apps.core.metering.MeteredClient`.** Direct
   calls to provider SDKs are forbidden. The client enforces per-run budget caps,
   records spend, and prevents duplicate charges on retry.
4. **Record method metadata before using a result.** Every `Response` row stores
   engine, model id, model version, grounding configuration, temperature, and
   timestamp. Reports print this. A response missing metadata is unusable and must
   not be aggregated.
5. **No client-facing copy ships without the claims filter.** See `SKILL.md`. Med spa
   marketing is regulated; unreviewed outcome language is a real liability for the
   clinic and for us.
6. **Never fabricate measurement data.** No placeholder mention rates, no sample
   numbers in anything that could reach a client. If data is missing, the report
   fails loudly.

## Conventions

- **Migrations:** one logical change per migration, always reviewed. Never edit an
  applied migration; add a new one.
- **Money:** integer cents, never float. `DecimalField` for anything displayed.
- **Time:** `USE_TZ = True`, store UTC, render in the clinic's local timezone.
- **Settings:** `django-environ`. Never commit a secret. `.env.example` stays current.
- **Tasks:** Celery tasks are thin — they load, call a service function, and save.
  Business logic lives in `services.py`, not in tasks or views.
- **Fan-out:** a measurement run is a Celery `group` of per-prompt-per-engine tasks
  collected by a `chord`. Individual failures must not fail the run; they mark the
  response as errored and the report reports the completion rate.
- **Tests:** pytest with `pytest-django`. Engine adapters are always tested against
  recorded fixtures, never live APIs. Any test that would spend money is a bug.
- **Naming:** `Client` is the paying med spa. `Competitor` is a tracked rival.
  `Engine` is an AI assistant we query. Never use "customer" or "brand" in code.

## When adding an engine

New assistants enter the citation mix regularly. Adding one means: subclass
`EngineAdapter`, implement `query()`, register in `ENGINE_REGISTRY`, add recorded
fixtures, and add a migration seeding the `Engine` row. Do not change the shape of
`Response` to accommodate a provider quirk — normalise in the adapter.

## Style

Follow `ruff` defaults. Type hints on service functions and adapters; not required
on views or tasks. Docstrings only where the *why* is non-obvious — do not restate
the function name.

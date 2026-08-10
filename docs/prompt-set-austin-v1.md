# Prompt Set — Austin Metro, v1

**Status:** frozen on first run. Editing any line creates v2.
**Composition:** 48 prompts × 4 engines × 3 repetitions = 576 responses per run.
**Estimated cost:** ~$14 per full run.

Columns map to the `Prompt` model: `text`, `intent`, `service`, `neighborhood`.
`intent` is a fixed enum — `discovery`, `service`, `price`, `geo`, `trust`,
`comparison`, `practical`, `firsttimer`. Do not add values without versioning.

---

## Why these 48 and not others

Three rules governed selection, and all three are worth defending if a client asks:

1. **Every prompt is something a patient would actually type**, not a keyword. "how
   much does botox cost in austin" is real; "austin botox med spa services" is a
   search query nobody has ever spoken to an assistant.
2. **Price prompts are over-weighted (8 of 48).** Price is the most requested figure
   and the one engines most often cannot state, which makes it the highest-signal
   diagnostic in the set.
3. **No prompt a clinic could only win by lying.** If a clinic has no Saturday hours,
   losing prompt 41 is a fact about the clinic, not a content gap. Those prompts stay
   in because the honest finding is worth reporting.

---

## The set

### Discovery — 6

| # | Prompt | Service | Neighborhood |
|---|---|---|---|
| 1 | best med spa in Austin | — | — |
| 2 | who are the top rated med spas in Austin Texas | — | — |
| 3 | med spa near me Austin | — | — |
| 4 | what's the best medical spa in Austin for someone in their 30s | — | — |
| 5 | recommend a med spa in Austin with good reviews | — | — |
| 6 | best aesthetics clinic Austin TX | — | — |

### Service-specific — 12

| # | Prompt | Service | Neighborhood |
|---|---|---|---|
| 7 | best med spa in Austin for Botox | neurotoxin | — |
| 8 | where to get lip filler in Austin | filler | — |
| 9 | who does the best microneedling in Austin | microneedling | — |
| 10 | best place for laser hair removal Austin | laser hair removal | — |
| 11 | med spa Austin that does semaglutide weight loss | GLP-1 | — |
| 12 | where can I get Morpheus8 in Austin | RF microneedling | — |
| 13 | best chemical peel Austin TX | chemical peel | — |
| 14 | who does Sculptra in Austin | biostimulator | — |
| 15 | best hydrafacial in Austin | hydrafacial | — |
| 16 | where to get IPL or BBL in Austin | IPL/BBL | — |
| 17 | med spa Austin that offers PRP for hair loss | PRP | — |
| 18 | liquid rhinoplasty Austin who does it | filler | — |

### Price — 8

| # | Prompt | Service | Neighborhood |
|---|---|---|---|
| 19 | how much does Botox cost in Austin | neurotoxin | — |
| 20 | average price per unit of Botox Austin TX | neurotoxin | — |
| 21 | how much is lip filler in Austin | filler | — |
| 22 | cost of laser hair removal Austin full body | laser hair removal | — |
| 23 | affordable med spa Austin that isn't cheap quality | — | — |
| 24 | how much does microneedling cost in Austin | microneedling | — |
| 25 | med spa membership Austin worth it cost | — | — |
| 26 | cheapest place for Botox in Austin that's still safe | neurotoxin | — |

### Neighborhood — 8

| # | Prompt | Service | Neighborhood |
|---|---|---|---|
| 27 | med spa South Congress Austin | — | South Congress |
| 28 | where to get Botox in Westlake Austin | neurotoxin | Westlake |
| 29 | med spa near the Domain Austin | — | Domain |
| 30 | best injector north Austin | neurotoxin | North Austin |
| 31 | med spa 78704 | — | South Austin |
| 32 | aesthetics clinic downtown Austin | — | Downtown |
| 33 | med spa Bee Caves Road | — | Westlake |
| 34 | Botox near Round Rock or north Austin | neurotoxin | Round Rock |

### Trust and credentials — 6

| # | Prompt | Service | Neighborhood |
|---|---|---|---|
| 35 | is there a nurse injector in Austin I can trust | — | — |
| 36 | what should I look for in a med spa medical director | — | — |
| 37 | how do I know if a med spa in Austin is legitimate | — | — |
| 38 | med spa Austin with a physician on site | — | — |
| 39 | is Botox at a med spa safe compared to a dermatologist | neurotoxin | — |
| 40 | do med spas in Texas require a good faith exam | — | — |

### Comparison — 4

| # | Prompt | Service | Neighborhood |
|---|---|---|---|
| 41 | Botox vs Dysport which Austin clinic offers both | neurotoxin | — |
| 42 | med spa or dermatologist for filler in Austin | filler | — |
| 43 | compare med spas in Austin for laser treatments | laser | — |
| 44 | which Austin med spa is best for natural looking results | — | — |

### Practical and first-timer — 4

| # | Prompt | Service | Neighborhood |
|---|---|---|---|
| 45 | med spa Austin open Saturday | — | — |
| 46 | med spa Austin free consultation | — | — |
| 47 | first time getting Botox in Austin where should I go | neurotoxin | — |
| 48 | med spa in Austin that won't make me look overdone | — | — |

---

## Execution notes

- **Repetitions run in separate sessions.** Three calls in one context produces
  three correlated answers, not three samples.
- **Temperature fixed at the provider default and recorded.** Do not tune it to make
  results look stable; the variance is a finding, not noise to suppress.
- **Grounding enabled on every engine that supports it**, and the configuration is
  recorded per response. An ungrounded run measures the model's training data, not
  what a patient sees.
- **Run all 48 against all engines before analysing any of it.** Partial analysis
  invites the temptation to adjust the instrument mid-run.

## What the run produces

For each of the 576 responses: the raw payload, the extracted answer text, every
clinic named with its ordinal position and sentiment, whether a price was stated, and
every source cited with its URL.

Aggregated, that yields per clinic: mention rate, top-3 rate, price-stated rate,
sentiment split, and the ranked list of sources that were cited instead.

**One dataset, 20 client slices.** The prompt set is a property of the metro, not of
any clinic. Every clinic in Austin is measured by the same instrument at the same
moment, which is also what makes the competitor share-of-voice numbers legitimate.

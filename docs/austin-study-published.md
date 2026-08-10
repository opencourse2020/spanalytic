# We asked AI assistants 573 questions patients type before booking Botox in Austin. Here's who gets named — and who doesn't.

*Spa Analytic — August 2026*

---

## The method, up front

We built 48 prompts a real Austin patient would actually type into an AI assistant — not keywords, sentences. Things like *"best med spa in Austin for Botox"*, *"how much does Botox cost in Austin"*, *"is there a nurse injector in Westlake I can trust."* We ran every prompt three times against four assistants — Claude, ChatGPT, Gemini, and Perplexity — with web search or grounding forced on for every call. That's 576 attempted responses; 573 completed and returned a genuinely grounded answer, a 99.5% completion rate. The other three came back without a search having run and were discarded rather than counted.

We queried through official APIs, not scraped consumer interfaces. That's a calibrated proxy for what a patient sees, not a recording of it — API grounding and consumer-app grounding aren't guaranteed identical, and any report that claims otherwise is describing something it can't actually measure.

We then tracked, across all 573 responses: which of 20 independent Austin med spas got named, in what position, with a price attached or not; which chains and dermatology practices got named instead; and which third-party sources — Yelp, Reddit, directories — the assistants cited as the basis for their answer.

---

## The finding that matters

**One clinic was named in 52% of all responses. It's a four-location chain — Viva Day Spa + Med Spa.** No independent clinic in the cohort broke 27%. Two chains together — Viva and Westlake Dermatology — outpolled all twenty independents in the study combined on several prompt categories.

That's not a story about any one clinic doing something wrong. It's a story about scale: a business with four locations and a marketing team accumulates review volume, directory presence, and press mentions faster than a single-location practice ever will organically. AI assistants are reading that accumulated signal, not evaluating injector skill.

**The second finding is where the leverage is.** Every clinic in this cohort was checked against 14 sources the assistants cited most often. The clinics that appeared in the fewest of them had the lowest mention rates — almost without exception. Visibility here isn't mainly a website problem. It's a presence problem, spread across a small, identifiable set of third-party sources.

---

## Where the 20 independent clinics stand

| Clinic | Mentioned | Top-3 | Named with a price |
|---|---:|---:|---:|
| Austin Med Spa* | 26.2% | 21.1% | 0.2% |
| Beaux MedSpa | 23.0% | 18.7% | 0.5% |
| Rejuvenate Austin | 15.0% | 8.7% | 0.0% |
| Refine Aesthetics | 14.0% | 9.6% | 0.2% |
| The Injection Room | 12.4% | 9.9% | 1.9% |
| Wild and Beautiful Natural Aesthetics | 9.2% | 7.5% | 0.3% |
| Texas Laser and Aesthetics Medspa | 5.1% | 3.0% | 0.0% |
| Westlake Aesthetics & Wellness | 5.4% | 2.8% | 0.0% |
| Victory MedSpa | 4.7% | 4.4% | 0.0% |
| Muse Medspa | 4.5% | 2.8% | 0.0% |
| W Aesthetics | 3.1% | 1.7% | 0.2% |
| Body Tonic RX Westlake | 2.4% | 1.0% | 0.0% |
| Austin Aesthetic Atelier | 2.3% | 0.9% | 0.0% |
| Auveau | 2.1% | 2.1% | 0.0% |
| Austin Luxury Medspa | 1.9% | 1.9% | 0.0% |
| NakedMD Med Spa Austin | 1.9% | 1.4% | 0.7% |
| Fresh Aesthetics | 1.4% | 1.0% | 0.0% |
| ATX Aesthetics | 0.5% | 0.0% | 0.0% |
| Austin Aesthetics Club | 0.2% | 0.2% | 0.0% |
| Lake Travis Laser Skincare & Aesthetics | 0.2% | 0.2% | 0.0% |

*\*Austin Med Spa's name is also the generic phrase assistants use to describe the category ("there are several Austin med spa options..."). We only counted occurrences that read as the specific business — capitalised, in context — and routed 38 ambiguous cases to manual review rather than guessing. This number is the conservative one.*

**The number every clinic above should sit with: at most 1.9% of responses named any clinic alongside an actual price.** Nineteen of twenty never appeared with a price at all. Assistants consistently could not tell a patient what treatment costs at almost any independent clinic in Austin — which means on the single most-asked question category in this study ("how much does Botox cost in Austin"), the answer these tools give is almost never a specific Austin clinic. It's a national average, or nothing.

---

## Where the recommendations actually come from

| Source cited | Share of responses |
|---|---:|
| Yelp | 54.8% |
| Reddit | 45.4% |
| MedSpaScout.com | 43.5% |
| InjectCo.com | 41.4% |
| MedicalSpaLocator.com | 29.8% |
| BanyanAndBamboo.com | 25.5% |
| Westlake Dermatology (own site) | 21.5% |
| TheMedSpaAustin.com | 17.3% |

*(Own-site citations for individual clinics — e.g. austinmedspa.com, beauxmedspa.com — sit in this range too; full table available on request.)*

Two of these are worth naming specifically because they're actionable, not just informative. **MedSpaScout.com** is a national directory — 9,000+ providers, real Google review data pulled in, free to claim — cited in 43.5% of responses and covering all 50 states, including a dedicated Austin page. **A claimed, complete listing there is a same-week fix**, not a months-long content project. If your clinic isn't on it, or is unclaimed, that's diagnosable today.

Yelp and Reddit together account for the majority of citations across the entire study. Neither is optimized by adding schema markup to a clinic's website. They're won by review volume, review recency, and — on Reddit specifically — organic mentions in threads a clinic has no direct control over. That's a different kind of work than SEO, and it's most of the actual leverage sitting in this dataset.

---

## What this study can't tell you

We don't know how many bookings any of this produces. AI-assisted answers generate no referral click a clinic's analytics can see, so honest attribution from a mention to a patient in the chair isn't currently possible with integrity — anyone selling you that number should be asked how they got it.

We also don't know if API-measured grounding matches what a patient sees in the consumer apps exactly. It's the closest calibrated proxy available without scraping consumer interfaces, which breaks and violates terms — but it's a proxy, stated plainly, not a claim of certainty.

---

## If you run one of these clinics

You already know your number. If you'd like the fuller picture — every prompt you were and weren't named on, every source you're absent from, and a specific first-fix — reply and we'll send it. No account, no call, no cost.

**hello@spanalytic.com**

---

*Spa Analytic measures whether AI assistants recommend a business, and fixes the specific reasons they don't, starting with medical spas in the US. Methodology, model versions, and full per-clinic data available on request.*

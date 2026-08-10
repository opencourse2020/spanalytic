# Operating Run Book — Agentic AI Answer Remediation

**Brand:** Spa Analytic (spanalytic.com)
**Vertical:** US medical spas — direct to clinic
**Target:** $12,000 collected revenue in 12 months
**Capital:** $1,000
**Operator:** agent-run, human on ~30 min/week
**Rails:** US entity + US bank + Stripe + domain — all in place. Gate G0 is cleared.

---

## 1. What changed when you told me you were US-based

My previous answer spent half its reasoning routing around a payment problem that no longer exists. With a US bank account, Stripe, Shopify Partner payouts, Paddle and every marketplace payout rail open at once. That kills the constraint — and with it, the reason I'd shaped the plan the way I had.

So I re-ran the thesis check. It failed.

## 2. The thesis I killed

I proposed selling a cheap AI-visibility monitoring dashboard into the SMB/agency long tail, on the assumption that incumbents were priced for enterprise and the low end was empty.

**The low end is not empty.** Verified pricing as of July 2026: Rankscale ~$20/mo, Otterly Lite $29/mo, LLMrefs $79/mo flat for 500 prompts, Peec from ~$85-95/mo. The category absorbed $300m+ in funding between summer 2025 and spring 2026, with the leader at roughly a $1bn valuation. Entering that with $1,000 is entering a knife fight with a spoon.

**But the same research handed me the replacement.** The most consistent complaint across independent 2026 round-ups is that every one of these products is a dashboard: it tells you ChatGPT recommends your competitor, and stops. Nobody fixes it. Fixing it means restructuring pages into extractable answers, cleaning entity data, adding the statistics and citations that lift extraction rates, and earning off-site mentions.

That is not a dashboard. That is repetitive knowledge work — which is exactly what an agent pipeline is for.

**The call: sell the fix, not the measurement. White-label it to agencies.**

## 3. The number that reframes everything

I built the model to find out what actually has to be true. The answer is narrower than expected:

| Paying customers acquired in 12 months | Cumulative revenue |
|---|---|
| 3 | $9,506 |
| **4** | **$12,105** |
| 6 | $16,479 |
| 10 | $26,832 |

At $750 setup + $349/brand/month, **four customers clears the target.** And the sensitivities are almost flat:

- Cut the retainer from $349 to **$149** — 10 customers still yields $14,580.
- Raise churn from 5%/mo to a catastrophic **20%/mo** — 10 customers still yields $18,719.
- Cash never dips below **$856**. The $1,000 is never actually at risk.

**Conclusion: this business is not capital-constrained, not price-constrained, and not retention-constrained. It is constrained on exactly one variable — whether you can reach and close 4-6 businesses.** Every hour spent on product polish, pricing theory, or churn engineering in the first six months is misallocated. The plan below optimises for reach and nothing else.

## 4. The agentic delivery pipeline

Five agents, run as a chain per client brand. Human reviews the last stage only.

| Stage | Agent | Input | Output |
|---|---|---|---|
| 1 | **Prompt-set builder** | Brand, category, competitors, geography | 40-60 buyer-intent prompts a real customer would type into an AI assistant |
| 2 | **Measurement** | Prompt set | Multi-engine runs via official APIs with search grounding on. Mention rate, share of voice, sentiment, which sources got cited instead |
| 3 | **Diagnosis** | Measurement + crawl of client site | Ranked gap list: missing entity data, non-extractable page structures, absent third-party corroboration |
| 4 | **Remediation** | Gap list | The actual deliverables — rewritten answer-blocks, schema markup, comparison pages, FAQ blocks, a source-targeting list |
| 5 | **Reporting** | Before/after runs | White-label PDF with the agency's logo. This is the artefact that renews the retainer |

**Methodology honesty, which is also the moat:** measurement runs through official APIs, not scraped consumer interfaces. Scraping ChatGPT's web UI violates terms and breaks without warning. API results with grounding enabled are a proxy, not the consumer product — state that in the report. Incumbents are vague about this; being explicit is a trust asset when selling to agencies who will be asked by their own clients.

**Unit cost:** ~$8.50 per brand per month all-in. Gross margin holds above 90% at every price tested.

## 4b. The vertical, and why the domain decided it

`spanalytic.com` is not a neutral asset. Read aloud it says *spa analytic*, and any generic positioning fights that reading forever. Rather than pay a permanent naming tax, use it: medical spas were already on the shortlist, and the domain makes the vertical free.

**The vertical checks out on every criterion that matters:**

| Criterion | Med spas | Why it matters |
|---|---|---|
| Revenue per location | ~$1.4M average, +7% YoY | A $499/mo service is 0.4% of revenue. Trivially justifiable |
| Fragmentation | ~10,000-12,000 US locations, ~1,000 new per year | No national brand owns the AI answer. It is genuinely up for grabs |
| Query shape | "best med spa near me", "where to get botox in Austin" | High-intent, local, exactly what people now ask assistants instead of Google |
| Marketing sophistication | Already buy SEO, ads, and agency services | The budget line exists; you are competing for allocation, not creating demand |
| Enumerability | Public directories, state licensing, Google Maps | The prospect list is buildable, not guessed at. Florida and California are densest |
| Citation sources | RealSelf, Yelp, local roundups, directories | Finite and submittable — which is how you attack the earned-media problem in §7 |

**Revised offer — direct to clinic, not white-label to agencies.** White-label hides your brand, which wastes the domain. Direct pricing at **$995 setup + $499/month** puts the whole thing below what a clinic pays for one week of ads.

| Clinics acquired in 12 months | Cumulative revenue | Exit MRR |
|---|---|---|
| 2 | $9,378 | $590 |
| **3** | **$13,621** | **$914** |
| 5 | $21,113 | $1,624 |
| 8 | $29,544 | $2,869 |

**Three clinics clears the target.** And the downside case holds: if nobody renews and it becomes a project-only business, 12 one-off engagements at $995 still gets you to $11,940.

**The name tension, and how it resolves.** "Analytic" signals a dashboard — the exact thing §2 argues against selling. That is fine, because it describes the *lead magnet* precisely. The free AI visibility report is the analytic; the remediation is the sale. Positioning line: *"Spa Analytic — see what AI tells patients about your clinic. Then fix it."*

Two cheap housekeeping items: buy `spa-analytic.com` as a redirect (~$12, kills the "span-alytic" misread), and set the wordmark as **Spa Analytic** with a visible word break, never lowercase-run-together.

**One constraint specific to this vertical.** Med spa regulation is tightening — Good Faith Exam requirements, medical director oversight, and state Corporate Practice of Medicine rules. Everything you publish on a clinic's behalf must avoid medical claims, outcome promises, and before/after implications you cannot substantiate. Add a claims filter as a mandatory stage between remediation and sign-off. This is a genuine liability, not a formality, and it is also a selling point: an agency that does not know this will write copy that gets the clinic in trouble.

## 5. Twelve months

**Weeks 1-3 — Prove the pain, build nothing.**
Build a list of 60 med spas across three metros (start with Florida and California by density, plus one mid-size market for contrast). Run the pipeline manually against 20 of them. Publish one report: *"We asked AI assistants 2,000 questions patients actually ask about med spas. Here's which clinics get recommended — and why."* Send each named clinic its individual slice.
This is simultaneously the market research, the lead magnet, the proof of competence, and the product demo. Cost: API credits only.

**Weeks 4-6 — Sell before you build.**
Convert one recipient into a paid engagement at $995. Deliver it by hand. If nobody buys, the problem is not felt — test one adjacent vertical (dermatology or dental aesthetics, both reachable under the same brand), then abandon the thesis. *(Gate G2.)*

**Weeks 6-14 — Productise the path you actually walked.**
Automate only the stages that hurt during manual delivery. Convert project buyers to retainers by making the monthly before/after report the thing they can't reproduce themselves.

**Months 4-12 — One report per month, one new vertical per quarter.**
Each published report seeds the next vertical's pipeline. Agencies compound: one account that adds a second and third brand is worth more than two new logos and costs nothing to acquire.

## 6. Division of labour

**Agent (me), continuously:** vertical screening, prompt-set design, all measurement runs, diagnosis, drafting every deliverable, writing the monthly research report, drafting outbound sequences, maintaining the model, flagging gate breaches.

**You, ~30 min/week — irreducible because it requires identity or authority:**
1. *Week 1:* register the LLC (or use a sole prop + EIN), open Stripe, buy the domain. **Nothing else can start until this is done.**
2. *Ongoing:* send the outbound from your name, and reply to anyone who replies. Agencies buy from people.
3. *Ongoing:* final sign-off on client deliverables before they ship under an agency's logo.
4. *At each gate:* make the call. The rule is pre-committed in the workbook precisely so it isn't re-argued under sunk-cost pressure.

## 7. The four risks that actually matter

| Risk | Why it's real | Pre-committed response |
|---|---|---|
| **Incumbents add remediation** | Well-funded, obvious next feature | Compete on vertical depth and white-label service, not features. If a funded player ships vertical remediation for your niche, move niche — don't defend |
| **API grounding drifts from consumer behaviour** | Your measurement stops predicting reality | Publish methodology openly; re-baseline quarterly; never claim more precision than the method supports |
| **Nobody converts from free audit** | The single most fragile assumption in the model — no benchmark exists | Gate G1 at week 3. If no unprompted "what would it cost to fix this?", stop before building |
| **The work doesn't recur** | One-time fix, then they leave | Falls back to project-only economics. The model then needs ~16 projects instead of 10 customers — still reachable, but re-forecast at Gate G3 |

## 8. What I need from you to start

One decision and one action.

Rails, domain and vertical are settled. What remains:

**Decision:** confirm med spas as the beachhead, or name the adjacent vertical you'd rather test first.
**Action, ~20 minutes:** point spanalytic.com at a one-page site, create the Stripe product ($995 one-time, $499 recurring), and set up a single inbox on the domain. Deliverability on cold outbound depends on the domain having sending history, so this wants doing in week one even though nothing sends until week three.

Then I build the 60-clinic list and run the first 20 audits. The first thing you'll see is the report draft and the outbound sequence, for your sign-off.

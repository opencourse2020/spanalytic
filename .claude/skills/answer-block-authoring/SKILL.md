---
name: answer-block-authoring
description: Write and claims-check extractable answer blocks for medical spa clients. Use whenever producing copy that will be published under a clinic's name — answer blocks, GBP field values, directory submission text, FAQ entries, schema descriptions — or when reviewing existing clinic copy for regulatory exposure. Also use when a client asks for outcome or superiority language, to determine what may be written instead.
---

# Answer-block authoring and claims safety

This is the highest-risk repeatable work in the product. Copy produced here is
published under a licensed medical practice's name, in a regulated advertising
context. A block that reads well and violates state medical advertising rules is a
worse outcome than no block at all.

Two things happen here, in order: write for extraction, then filter for claims.
Never reverse them — filtering first produces timid copy that gets extracted by
nobody.

## Part 1 — Writing for extraction

An answer block exists to be quoted by an AI assistant answering a specific patient
question. It is not a page, a paragraph of marketing, or an SEO snippet.

**Structure, in this order:**

1. **A heading that restates the patient's literal question.** Match the phrasing in
   the mapped prompt. "What does Botox cost in Austin?" not "Our Neurotoxin Pricing".
2. **A direct answer in the first sentence.** No preamble, no "At Lumen, we believe".
   The first sentence must be independently quotable and still true.
3. **A specific, citable number.** A price, a unit range, a duration, a count. Blocks
   without a number are dramatically less likely to be extracted, and price is the
   single most requested figure.
4. **Named credentialed provider.** Who performs the treatment and what license they
   hold.
5. **One piece of qualifying context** that a patient would actually want — hours,
   consultation policy, what the price includes.

Target 120–170 words. Longer blocks get truncated mid-claim, which is how a
compliant sentence becomes a non-compliant fragment.

**Worked example, mapped to "how much does Botox cost in Austin":**

> **What does Botox cost at Lumen Aesthetics?**
> Neurotoxin treatment at Lumen is priced at $12 per unit. A typical forehead and
> glabellar treatment uses 20–40 units, placing most first appointments between $240
> and $480. Pricing is per unit rather than per area, so you pay only for what is
> administered. All injections are performed by a licensed RN or NP injector under
> the supervision of medical director Dr. Priya Raman, MD, following a good faith
> exam as required in Texas. Consultations are complimentary, and no treatment is
> administered on the same visit unless the good faith exam is complete.

Every sentence there does a job: literal answer, citable number, pricing model,
credential and supervision, policy. Nothing is decorative.

**Never do these:**

- Open with the clinic name as the subject ("Lumen offers...") — it reads as
  advertising and extracts poorly.
- Use ranges so wide they answer nothing ("$200–$2,000").
- Write a block for a prompt the client actually loses on for a structural reason —
  if they have no Saturday hours, the fix is not copy.
- Reuse one block across several prompts. One block, one prompt, or the mapping in
  the report is a lie.

## Part 2 — The claims filter

Run every block, every GBP value, every directory submission through all seven checks.
A block failing any check does not get softened quietly — it is rewritten, and if the
underlying request was for prohibited language, it is escalated to the client's
medical director with the reason.

| # | Check | Prohibited | Permitted instead |
|---|---|---|---|
| 1 | **Outcome guarantees** | "You will look years younger", "guaranteed results", "eliminates wrinkles" | Describe the procedure and typical parameters. "Most patients return every 3–4 months to maintain results." |
| 2 | **Permanence** | "permanent", "forever", "never comes back" | "long-lasting", or state the actual duration with a number |
| 3 | **Comparative superiority** | "the best injector in Austin", "safer than", "better results than" | Verifiable, attributable facts: years of practice, credential, procedure volume |
| 4 | **Supervision and GFE language** | Implying treatment without a good faith exam, or omitting the medical director where the state requires disclosure | Name the medical director and their credential; state the GFE requirement plainly |
| 5 | **Scope of practice** | Attributing physician-level acts to an RN or aesthetician; vague "our experts" | Name the role and license for each act described |
| 6 | **Before/after implication** | Any described or implied result imagery without documented written consent on file | Omit entirely. Do not describe a result in place of showing one |
| 7 | **Off-label and unapproved use** | Presenting an off-label use as approved; disease-treatment claims for cosmetic products | State the indication accurately, or omit the service from the block |

**Escalate, do not soften, when:**

- The client asks directly for outcome or superiority language.
- The service described may exceed the stated provider's scope of practice.
- A claim would need substantiation the clinic has not provided.
- Existing site copy fails a check, even though it is outside our engagement scope —
  report it anyway, in writing, and note that remediation was not included.

**Refuse outright:** any request to write copy that guarantees a medical outcome,
claims superiority without substantiation, or implies results the clinic cannot
document. This is stated in the proposal before the engagement begins, so a refusal
is never a surprise. Say what may be written instead.

## Part 3 — Recording the result

Every block gets a `claims_status` of `PASS`, `REWRITTEN`, or `ESCALATED`, with the
failed check number and the reason. Two consequences depend on this record:

- Nothing with status `ESCALATED` may be installed or submitted anywhere.
- The remediation report lists escalations to the client's medical director by name.
  This is the point of the exercise. A clinic that discovers a compliance problem in
  our report and fixes it is a clinic that renews.

## Jurisdiction note

The checks above are the general filter. State rules differ — Texas good faith exam
and medical director requirements, and Corporate Practice of Medicine rules that vary
by state, are the ones that bite most often. When a client operates somewhere the
current filter has not been validated against, flag it before writing rather than
after. We are not their lawyers, and the report should say so.
# Frontend Rules

Applies to Django templates, the internal review queue, and PDF report templates.
All three share one visual system — a client's report and our marketing site must
look like the same company made them.

## Stack rules

- Django templates, vanilla CSS, vanilla JS. **No React, no Vue, no build step.**
- One optional dependency is permitted: **HTMX**, and only for partial updates in the
  internal review queue. It never appears in a client-facing or PDF template.
- No CSS framework. No Tailwind. The token system below is the whole design system.
- No `localStorage` or `sessionStorage` in report templates — WeasyPrint has no
  browser storage and will fail silently.
- JavaScript is progressive enhancement only. Every page must work with JS disabled.
  The review queue may degrade to full page reloads; it may not become unusable.

## Tokens

Defined once in `static/css/tokens.css` and imported everywhere, including PDF
templates. Never hardcode a hex value in a component.

```css
:root{
  --ink:        #161B26;  /* primary text, dark surfaces */
  --ink-soft:   #3A4152;  /* secondary text */
  --paper:      #F2F1EE;  /* page background */
  --paper-deep: #E4E2DC;  /* inset surfaces, empty track */
  --rule:       #C9C6BE;  /* hairlines, borders */
  --white:      #FBFAF8;  /* raised surfaces */
  --brass:      #B4791F;  /* a competitor named — the problem */
  --clinical:   #1F6F73;  /* our client, our fix — the resolution */
}
```

**Colour carries meaning here; it is not decoration.** Brass marks a competitor
being named or a gap being reported. Clinical teal marks the client's own presence,
a resolved gap, or a completed action. Do not use either colour to decorate a heading
or a button that has nothing to do with that distinction. A designer who swaps them
has changed what a report says.

Focus rings are always `--clinical`. Error states use `--brass`, never red — this is
a measurement product, and red implies clinical alarm we have no basis for.

## Type

```
Display   Newsreader        400/500   headings, report figures
Body      Instrument Sans   400/500/600
Data      IBM Plex Mono     400/500   prompt strings, percentages, labels, eyebrows
```

Monospace is reserved for things that are literally machine data: the prompt text we
sent, a percentage, a source name in a citation table, a field label. It is not a
decorative choice. If a piece of text is prose, it is not mono.

Headings use `letter-spacing: -.015em` and `line-height: 1.12`. Body sits at
`17px/1.6`. Never set body below 15px, including in PDFs — the reader is often a
clinic owner on a phone between patients.

## Layout

- Content max width 1080px; prose max width 720px; measure caps at ~56ch.
- Spacing scale, in px: `7 10 14 18 26 34 46 60 76`. Nothing outside it.
- Border radius: 2–3px only. This system is closer to a lab report than a consumer
  app; rounded cards read wrong.
- Section rhythm is a hairline rule in `--rule`, not a background colour change.

## Components

Structure encodes information or it does not exist:

- **Numbered or dated markers** only where order is real. Report stages are `Day 5 /
  Day 14 / Day 30` because those are actual dates, not `01 / 02 / 03`.
- **Bars** are always normalised against the largest value in the set, computed at
  render time — never a magic multiplier. The numeric label always shows the true
  value, not the scaled one.
- **Empty states** say what to do next, in the interface's voice. "No runs yet — the
  baseline starts when intake is complete," not "No data available."
- **Errors** state what happened and how to fix it. They do not apologise and they are
  never vague.

## Accessibility floor

Non-negotiable, checked before any template is considered done:

- Visible keyboard focus on every interactive element. Never `outline: none` without
  a replacement.
- `prefers-reduced-motion` respected — all animation disabled, no content hidden
  behind an animation that no longer runs.
- Real semantic elements. A clickable `div` is a bug.
- Form inputs always have a associated `<label>`. Placeholders are not labels.
- Colour is never the only signal. A brass bar also carries a numeric label.
- Contrast: 4.5:1 for body text, 3:1 for large text and UI boundaries.

## PDF templates

- Live in `templates/reports/pdf/`, import the same `tokens.css`.
- Page size A4, 18mm margins. Set explicit `@page` rules; do not rely on defaults.
- WeasyPrint has no JavaScript. Anything dynamic must be resolved server-side and
  passed into the context.
- Web fonts must be embedded locally, not fetched from Google Fonts at render time —
  a network failure during rendering must not silently change a client deliverable.
- Test every report template against the longest realistic content, not the sample.
  Clinic names and Austin neighborhood names overflow more than you expect.

## Writing in the interface

Copy is design material. Name things by what the user controls, never by how the
system works. A user reviews *answer blocks*, not `AnswerBlock` records; they see
*sources that cite competitors*, not `Citation` rows.

Buttons say what happens: "Send report", not "Submit". The action keeps its name
through the whole flow — a button that says "Approve" produces a state that says
"Approved". Sentence case throughout. No filler, no exclamation marks.

## Before a template is done

1. Keyboard-navigate it start to finish.
2. Check it at 380px wide.
3. Turn off JavaScript.
4. Turn on reduced motion.
5. Remove one thing. There is almost always one element carrying no information.

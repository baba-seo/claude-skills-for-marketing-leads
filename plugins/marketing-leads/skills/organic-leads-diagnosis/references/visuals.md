# Answer first, then show it

The reader is a CMO or head of marketing with five minutes. Write everything, in chat and in the diagnosis, as an inverted pyramid: the answer first, then what to do, then what's unknown, then the evidence, then the detail. Someone who reads only the top of the page must know the answer and the first move. Someone who reads to the end gets the proof.

## In chat, after each step

Lead with a one-line verdict in bold, then one small visual, then at most two lines of explanation. Never a paragraph of numbers.

> **Most of your organic clicks come from people who already know you.**
> [bar: brand 82% / non-brand 18%]
> Non-brand clicks are what organic brings on its own. At 18%, the site is mostly found by people who already searched your name.

A short table counts as a visual when a chart would be overkill (three rows or fewer).

## The diagnosis, top to bottom

1. **The answer**: one sentence a CEO can repeat. What is costing leads, and what happens first. If the data can't tell yet, that's the sentence.
2. **The six causes at a glance**: one strip, one tile per cause, each with an icon and a word, never colour alone:
   - ✓ Confirmed
   - ✕ Ruled out
   - ? Can't tell from this data
   - ○ Not checked
3. **What to fix first**: up to three cards, numbered. Each card: the fix in a bold line, then the first step, the owner, and "you'll know it worked when…".
4. **What I couldn't tell**: one line each, with what would answer it and who has it.
5. **The evidence**: the charts below, one per finding that matters, most important first. Each chart sits under the cause it proves.
6. **The detail**: the ten checks table, the "Not now" lists, the source line.

## Charts

Draw a chart only from figures in their data: the script's chart data (run it with `--chart-data`), their CRM export, or numbers they gave you. Copy figures from the chart data; don't retype them. Never chart a benchmark, an average from other companies, or a number you estimated yourself.

**Which chart for which finding**

| Finding | Chart |
|---|---|
| Brand and non-brand split (check 2) | One horizontal bar split in two, per period |
| Buyer share of the top 50 searches (check 1) | One horizontal bar split in buyer, maybe, not a buyer, after they corrected the marking |
| Clicks from their markets (check 3) | One horizontal bar split in their markets and elsewhere, plus the top countries as short bars |
| Impressions up, clicks flat (rule 2) | Paired bars per period: impressions and clicks for non-brand, with CTR as a label |
| Brand searches losing clicks (rule 4) | Paired bars per brand group: CTR now and before |
| Leads by source and how many became deals (checks 8 and 9) | Horizontal bars per source, deals shown inside each bar |
| Reply time (check 7) | One number, large, with the 5-minute target written next to it and labelled as a target |
| What closing the gaps is worth (check 10) | The sum written out: leads × share that becomes a deal × deal value = total, each input labelled fact, estimate or assumption |

**Every chart**

- The title is the takeaway, as a sentence: "Most clicks come from people who already know you", not "Brand vs non-brand clicks".
- Horizontal bars, values written on the bars, axis starting at zero. No pies, no 3D, no gauges, no dual axes.
- One accent colour for what matters, grey for the rest. Never colour as the only way to tell things apart: label the segments.
- Period labels on everything that compares periods.
- Say how many it rests on when it's small ("based on 6 leads").
- Estimates and assumptions look different from facts (a dashed outline and the word "estimate").
- Every chart has a text alternative with the same numbers: an `aria-label` on the SVG and the figures in a short line or table under it.

## Format

Build the diagnosis as one HTML artifact (or a document, if artifacts are off) with the charts as inline SVG. No external scripts, fonts or images, so it opens anywhere, prints cleanly and works with a keyboard and a screen reader. Real headings in order, enough contrast, text never inside images.

A minimal pattern for a split bar. A label goes inside its segment only when it fits; otherwise it goes on a line under the bar, right-aligned if it would run off the edge. Text at 13px, the chart capped at its natural width so it never blows up on a wide screen.

```html
<figure>
  <figcaption><strong>82% of organic clicks come from people who already searched your name</strong></figcaption>
  <svg role="img" aria-label="Organic clicks, last 3 months: brand 740 (82%), non-brand 160 (18%)"
       viewBox="0 0 600 74" width="100%" style="max-width:600px; font-size:13px">
    <rect x="0" y="4" width="493" height="36" fill="#c9ced6"/>
    <rect x="493" y="4" width="107" height="36" fill="#1c35b8"/>
    <text x="8" y="27" fill="#111">Brand 740 (82%)</text>
    <text x="600" y="62" fill="#111" text-anchor="end">Non-brand 160 (18%)</text>
  </svg>
  <p>Last 3 months. Brand 740 clicks, non-brand 160 clicks. Fact, from your Search Console export.</p>
</figure>
```

Work the widths and label positions out in code from the figures (share × width, label length against segment width), not by eye.

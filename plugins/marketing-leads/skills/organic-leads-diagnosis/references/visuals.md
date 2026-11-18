# Answer first, then show it

The reader is a CMO or head of marketing with five minutes. Write everything, in chat and in the diagnosis, as an inverted pyramid: the answer first, then what to do, then what's unknown, then the evidence, then the detail. Someone who reads only the top of the page must know the answer and the first move. Someone who reads to the end gets the proof.

## In chat, while you work

The chat is work in progress; the diagnosis is the report. Never let a message mid-way look or sound like the finished diagnosis.

- **Label every update as a first read.** Start with a short line such as "First read of your data, not the diagnosis yet", so nobody forwards it as the answer.
- **Say "so far" until the checks are done.** Findings in chat are provisional: what the data suggests, and what would confirm or overturn it. No causes named as confirmed, no fixes, no answer sentence before step 5.
- **Small visuals only.** At most one compact table (three or four rows: the figure now, before, and the change) per message. No titled charts in chat: charts with takeaway titles belong in the diagnosis.
- **One headline, not two.** Don't repeat the same point as a bold line and again as a title.
- **End with what happens next**, so they know the work isn't finished.

> First read of your data, not the diagnosis yet.
> So far: **search visibility looks unchanged, and only demo requests fell.**
>
> | | Now | Before |
> |---|---|---|
> | Organic clicks | 4,440 | 4,597 |
> | Organic demo requests | 19 | 38 |
> | Organic downloads | 121 | 115 |
>
> If that holds, the drop happens after the click, on the site. I'll test it with the checks on your phone before calling it.

The last message, once the diagnosis exists, can give the answer sentence and point to the diagnosis.

## The diagnosis, top to bottom

1. **The answer**: one sentence a CEO can repeat. What is costing leads, and what happens first. If the data can't tell yet, that's the sentence.
2. **The six causes at a glance**: one strip, one tile per cause, each with an icon and a word, never colour alone:
   - ✓ Confirmed
   - ✕ Ruled out
   - ? Can't tell from this data
   - ○ Not checked
   Under it, one plain line on scope: a diagnosis of the coverage they have today, from N months of their data; a direction, not a forecast or a growth strategy.
3. **What to fix first**: up to three cards, numbered, all on existing pages and content. Each card: the fix in a bold line, then the first step, the owner, and "you'll know it worked when…". Then an **Outside organic search** box: findings for sales or the CRM owner, one line each with who gets it.
4. **What I couldn't tell**: one line each, with what would answer it and who has it.
5. **The evidence**: the charts below, one per finding that matters, most important first. Each chart sits under the cause it proves.
6. **The detail**: the ten checks table, the "Not now" lists, the source line.
7. **What comes next**: one short paragraph: growing beyond the pages they have takes a revenue-first SEO strategy and someone to own it.

## Order by reader

Ask in step 1 who the diagnosis is for. The facts and numbers are the same in every version; only the order, the emphasis and the words change. If they want it for a second reader, make a second version from the same findings.

| Reader | Opens with | Then | Evidence leads with | Words |
|---|---|---|---|---|
| **CMO or head of marketing** | The answer: what is costing leads, and what happens first | The six causes strip, the fixes with owners and first steps, what I couldn't tell | Leads, the path to sales, the search data | Marketing terms, each explained once |
| **CFO** | What the gap is worth a year, as a range, each input labelled fact, estimate or assumption | What each fix costs (time, people, money where known) and how soon it should show, cheapest first; then how sure the numbers are | Leads, deals and revenue; search data only as support | Money, ranges and confidence. No SEO terms |
| **CEO or founder** | The answer, and the one decision needed from them | The fixes with owners, what it's worth, the main risk | Leads and deals | Plain business words |

- **Never stretch the money for a CFO.** If deal value or the share of leads that become deals is missing, the CFO version opens by saying the value can't be put in money yet, and what would let you.
- A range beats a single number when any input is an estimate. Work the range from their own low and high estimates, not from benchmarks.
- The same chart can serve two readers with a different title: "Organic demo requests halved since the new navigation" for the CMO, "About €100k to €210k a year of pipeline at stake" for the CFO.

## The asker's briefing

When the person asking isn't the one who'll read the report (a CMO preparing something for the CFO, a head of marketing for the board), they get two things, as two separate artifacts or documents:

1. **The report**, written for the reader. This is the one they forward.
2. **A briefing**, for the asker only, never meant to be forwarded. One screen:
   - **The point in one line**, as they'd say it out loud.
   - **How to open**: the first two sentences to say when they present it.
   - **The questions the reader is likely to ask**, three at most, each with the answer from the data and its label (fact, estimate, assumption). For a CFO: what it's worth, what it costs, how sure we are. For a CEO: what we decide, who owns it, what's the risk.
   - **What's still unknown, and how to say it** without losing the room: what's missing, and when they'll know.
   - **The decision they need** from the reader, in one line.
   - **The marketing detail they'll want for themselves** but the reader won't: which pages, which searches, which rule, in a few lines.

When the asker is the reader, there's one report and no briefing. Refer to the reader by role ("the CFO"), not by he or she, unless the asker has told you.

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
| Trend over 12 to 16 months | Monthly clicks as a line, with a second small chart under it for leads if they have them (never one chart with two axes). Their changes, Google updates and Search Console data errors marked as labelled vertical lines; partial months marked |
| What closing the gaps is worth (check 10) | The sum written out: leads × share that becomes a deal × deal value = total, each input labelled fact, estimate or assumption |

**Every chart**

- The title is the takeaway, as a sentence: "Most clicks come from people who already know you", not "Brand vs non-brand clicks".
- Horizontal bars, values written on the bars, axis starting at zero. No pies, no 3D, no gauges, no dual axes.
- Never put different units on one scale (clicks next to a position or a percentage). When each row compares its own before and after, scale each row on its own and say so under the chart.
- One accent colour for what matters, grey for the rest. Never colour as the only way to tell things apart: label the segments.
- Period labels on everything that compares periods.
- Say how many it rests on when it's small ("based on 6 leads").
- Estimates and assumptions look different from facts (a dashed outline and the word "estimate").
- Every chart has a text alternative with the same numbers: an `aria-label` on the SVG and the figures in a short line or table under it.

## Format

Build the diagnosis as one HTML artifact (or a document, if artifacts are off) with the charts as inline SVG. No external scripts, fonts or images, so it opens anywhere, prints cleanly and works with a keyboard and a screen reader. Real headings in order, text never inside images.

**Light and dark.** People open it in either. Never rely on the viewer's default background: set the page's own background and every colour through the variables below, with the dark override, and colour SVG shapes and text through classes, never `fill="#..."` attributes. These values pass WCAG 2.2 AA in both modes: text 4.5:1 or more, bars 3:1 or more against the page.

```css
:root{color-scheme:light dark;--bg:#ffffff;--fg:#111111;--muted:#444b55;--line:#d5d9e0;
  --accent:#1c35b8;--on-accent:#ffffff;--bar:#858d99;--soft:#f4f6fa}
@media (prefers-color-scheme:dark){:root{--bg:#16181d;--fg:#e8eaee;--muted:#b4bac4;--line:#3a3f48;
  --accent:#8aa2ff;--on-accent:#0b1020;--bar:#60676f;--soft:#1f232b}}
html,body{background:var(--bg);color:var(--fg)} a{color:var(--accent)}
svg text{fill:var(--fg);font-size:13px} svg text.on{fill:var(--on-accent)}
svg rect.acc{fill:var(--accent)} svg rect.base{fill:var(--bar)}
```

A minimal split bar. A label goes inside its segment only when it fits; otherwise on a line under the bar, right-aligned if it would run off the edge. The chart is capped at its natural width so it never blows up on a wide screen.

```html
<figure>
  <figcaption><strong>82% of organic clicks come from people who already searched your name</strong></figcaption>
  <svg role="img" aria-label="Organic clicks, last 3 months: brand 740 (82%), non-brand 160 (18%)"
       viewBox="0 0 600 74" width="100%" style="max-width:600px">
    <rect class="base" x="0" y="4" width="493" height="36"/>
    <rect class="acc" x="493" y="4" width="107" height="36"/>
    <text x="8" y="27">Brand 740 (82%)</text>
    <text x="600" y="62" text-anchor="end">Non-brand 160 (18%)</text>
  </svg>
  <p>Last 3 months. Brand 740 clicks, non-brand 160 clicks. Fact, from your Search Console export.</p>
</figure>
```

Work the widths and label positions out in code from the figures (share × width, label length against segment width), not by eye.

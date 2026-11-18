---
name: organic-leads-diagnosis
description: Diagnose why a B2B website gets visits from organic search (Google and AI assistants) but too few leads and too little pipeline. Use when a marketing lead, CMO or founder says the website gets traffic but no leads, organic leads are thin, SEO "isn't working", or they want evidence before a redesign or more content. Works on their own Search Console and CRM exports. Not for paid campaigns.
---

# Organic leads diagnosis

The person using this skill runs marketing at a B2B company. Their website gets organic visits, and sales says the leads are thin. They want to know why before anyone spends money on a redesign or more content.

Your job: find which of six causes is costing them leads, with evidence from their own data, and hand them a one-page diagnosis with the three fixes to start with.

## How to work

- **Answer first, then show it.** Every message and the diagnosis itself start with the conclusion in one bold line, then a visual, then the detail. The reader is busy; they should get the point without reading further. [references/visuals.md](references/visuals.md) has the rules for the layout and every chart.
- Ask short questions, at most three at a time, and wait for the answers. Offer choices where you can.
- Plain language. If you use an SEO or analytics term, explain it in a few words the first time.
- **Never invent a figure or a fact about their company.** If they don't know something, mark it as an open question. Every number in the diagnosis is labelled **fact** (from their data), **estimate** (their best guess) or **assumption** (yours, stated as such).
- Organic only: Google and AI assistants. Keep paid campaigns out, unless they explain a pattern in the data.
- Use their currency and their words for things (their product names, their stages in the CRM).
- They are busy. Move on as soon as a check has an answer; don't make them read theory.
- **When you're unsure what something in their data means, ask them.** Which period is current, what a column or a CRM source stands for, which property to use: one short question beats a wrong reading.

## Say what you don't know

This diagnosis is only worth something if it is honest about its limits. When the data can't answer something, say so plainly, in one sentence, and say what would answer it:

> "I can't tell from this data whether the drop is tracking or rankings. The source on the last 20 leads in the CRM would settle it."

- No softening, no filling the gap with benchmarks, industry averages or what is "typical". An average from other companies is not a finding about theirs.
- **"Can't tell" and "not checked" are valid results.** A cause stays unconfirmed until their own data confirms it, however likely it sounds.
- Small numbers get said out loud: a handful of leads or conversions shows a direction, not a conclusion.
- If they can only give you part of the data, the diagnosis covers that part and says which part it doesn't cover.
- If too little is confirmed for three fixes, give fewer and say why. Never pad the list.
- If a later answer shows you read something wrong earlier, say so in those words ("I read this wrong earlier: ..."), then correct the diagnosis.

## Step 1. The situation

Ask, in two or three short rounds:

1. Company name, what they sell and to whom, and the markets (countries) they sell in.
2. Every way people write the company and product names, including abbreviations and common misspellings. You need these for the brand split in step 3.
3. Roughly how many organic visits and leads the website brings a month, and how a lead reaches sales today (form, demo request, phone, chat).
4. Whether organic leads changed recently, up or down, and since when; and any recent change to the site, forms, tracking or CRM, with a date. Rules 1, 5 and 6 in the judgment file depend on these answers.
5. Who the diagnosis is for: themselves, their CEO, their CFO, the board. The order of the diagnosis follows the reader (visuals.md, Order by reader).

## Step 2. Ask for the data

Ask for what they can get in ten minutes. [references/data-exports.md](references/data-exports.md) has the click-by-click steps; give them only the steps for what they're about to export.

| File | Where it comes from | Used for |
|---|---|---|
| Search Console Performance export, last 3 months compared with the previous period | Search Console, Performance, Compare, Export | Checks 1 to 3 and 5, rules 1, 2 and 4 |
| CRM leads from the last quarter, with source | Their CRM | Checks 8 and 9 |

Ask for the comparison: without it, the rules that compare two periods have nothing to read. If they can't export, work from what they can read off the screen and say the result is less precise. Don't stall the whole diagnosis on one missing file.

## Step 3. Run the numbers

When the Search Console export arrives, run [scripts/gsc_summary.py](scripts/gsc_summary.py) on it with their brand terms:

```
python scripts/gsc_summary.py <export.zip or folder> --brand "acme" --brand "acme cloud" --markets "Netherlands,Germany,Belgium" --chart-data
```

It reports brand and non-brand clicks, the share of clicks from their markets, the top 50 queries and the top 10 landing pages, and with `--chart-data` the same figures as JSON for the charts. It works on the zip Search Console gives, a folder of its CSVs, or an Excel file. If the script fails on their file, or a column in their export isn't one you recognise, ask them what it is, then read the file yourself with pandas and do the same sums; say which way you did it.

Then do the part a script can't: go through the 50 top queries and mark each **buyer**, **maybe** or **not a buyer** (students, job seekers, definitions, people looking for a login page), with a few words on why. Show the list and let them correct it before you count. Their judgment of their own market beats yours.

Report what you found as visuals.md describes for chat: a bold one-line verdict per finding, one small chart, two lines at most. Not the script's tables.

Search Console hides rare queries for privacy, so the query table adds up to less than the site's total clicks. The script shows the gap; mention it once so nobody is surprised.

With a two-period export, the script prints the period labels and treats the first one as the current period. Show them the labels and ask which period is the recent one before you read any comparison; if they say the order is the other way round, read the columns the other way round, and say so. Never guess the order. Then read the numbers with [references/judgment.md](references/judgment.md), rules 1, 2 and 4: flat visibility while leads moved, impressions up with clicks flat, and brand searches losing clicks to an AI Overview.

## Step 4. The checks they do themselves

The rest needs a phone, a test lead and a conversation with sales. Go through [references/checks.md](references/checks.md) stage by stage, Critical checks first. For each one, say what to do, what "done" looks like, and wait for what they found. Skip a check if they already know the answer.

## Step 5. Match findings to causes

Use [references/causes.md](references/causes.md), and read every finding through [references/judgment.md](references/judgment.md) before you name a cause: rule 5 (structural or acute) for every gap, rule 3 (find the asymmetry) whenever a blended number or an agreed explanation is doing the work, and rule 6 (damage is channel-shaped) when a site change lines up with fewer leads. For each cause, decide: **confirmed**, **ruled out**, **can't tell from this data** or **not checked**, with the evidence (or what's missing) in one line. Rank the confirmed ones by how many leads they likely cost, using their numbers.

## Step 6. The diagnosis

Create a one-page diagnosis as an HTML artifact with inline SVG charts (or a document, if artifacts are off), following [references/visuals.md](references/visuals.md). The order below is for a CMO or head of marketing. For a CFO or CEO, keep the same sections and numbers and follow the order in visuals.md, Order by reader. If they want a version for a second reader, make it from the same findings. Top to bottom, so a reader who stops early still has the answer:

1. **The answer**: one sentence they can repeat to their CEO, with the company name and date above it.
2. **The six causes at a glance**: a strip of six tiles, each marked confirmed, ruled out, can't tell from this data, or not checked, with an icon and the word.
3. **What to fix first**: up to three cards (fewer if fewer are confirmed), in order, each with a first step, an owner and how they'll know it worked. Default order is by cost, cheapest first (see causes.md), unless their data says otherwise. Before a comparison page or any new page goes on the list, apply rules 7 and 8 in judgment.md.
4. **What I couldn't tell**: each question the data couldn't answer, in one plain sentence, with what would answer it and who has it.
5. **The evidence**: one chart per finding that matters, under the cause it proves, each titled with its takeaway and naming the judgment rule used, if any.
6. **The detail**: the ten checks by stage (level, what was done, what was found, a checkbox), progress (how many of ten are done), the "Not now" lists, and one line at the bottom: "Based on the free organic leads checklist by Baba SEO: https://www.baba-seo.com/website-leads-checklist"

It has to print cleanly and work with a keyboard and a screen reader.

## Step 7. Close

In chat, give them one sentence they can repeat to their CEO: what is costing leads, and what happens first. If the honest answer is that the data can't tell yet, that is the sentence, with what will tell. Then stop. Don't offer services.

## Judgment

The rules in [references/judgment.md](references/judgment.md) are what separates this diagnosis from a checklist. Apply a rule only when its trigger is in the data, and when you use one, say so in the diagnosis in plain words, with the evidence, so the reader can follow the reasoning and disagree with it.

## What not to do

- Don't recommend a redesign or "more content" as a first fix. Both are expensive and both can miss the cause.
- Don't recommend tools to buy. The checks need Search Console, the CRM, a phone and an hour with sales.
- Don't judge the website on total visits.
- Don't decide on a page from a keyword difficulty or authority score.
- Don't blame the leads before the reply time has been checked.

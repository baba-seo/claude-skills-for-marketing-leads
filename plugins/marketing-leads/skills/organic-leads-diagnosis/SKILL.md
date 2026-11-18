---
name: organic-leads-diagnosis
description: Diagnose why a B2B website gets visits from organic search (Google and AI assistants) but too few leads and too little pipeline. Use when a marketing lead, CMO or founder says the website gets traffic but no leads, organic leads are thin, SEO "isn't working", or they want evidence before a redesign or more content. Works on their own Search Console and CRM exports. Not for paid campaigns.
---

# Organic leads diagnosis

The person using this skill runs marketing at a B2B company. Their website gets organic visits, and sales says the leads are thin. They want to know why before anyone spends money on a redesign or more content.

Your job: find which of six causes is costing them leads, with evidence from their own data, and hand them a one-page diagnosis with the fixes to start with on the pages and content they already have.

**Scope.** This diagnoses the organic coverage they have today, from a few months of their own data. It is a direction, not a forecast and not a growth strategy. Say so in the diagnosis. Fixes stay on their existing pages and content; anything outside organic search (sales follow-up, CRM set-up) is handed over, not put on the fix list.

## How to work

- **Answer first, then show it.** The diagnosis starts with the conclusion in one line, then the visuals, then the detail. While you work, messages lead with what you found so far, clearly labelled as a first read, never dressed up as the diagnosis. The reader is busy; they should get the point without reading further. [references/visuals.md](references/visuals.md) has the rules for the layout and every chart.
- **Four exchanges before the report, not ten.** Confirm what you read about them, ask for all the data at once, share a first read with one bundle of quick checks, then build the report. Anything they skip becomes "not checked" in the report; it never holds the report up.
- **Show you understand them, then ask them to confirm.** Read what you can before you ask: their website, and anything they said. Propose, don't interview: "From your site, you sell X to Y in these countries. Right?"
- **Questions as choices.** Where your interface offers tappable choices, use them. Otherwise give lettered options they can answer with one letter, and always leave room for their own answer. At most three questions at a time.
- Plain language. If you use an SEO or analytics term, explain it in a few words the first time.
- **Never invent a figure or a fact about their company.** If they don't know something, mark it as an open question. Every number in the diagnosis is labelled **fact** (from their data), **estimate** (their best guess) or **assumption** (yours, stated as such).
- Organic only: Google and AI assistants. Keep paid campaigns out, unless they explain a pattern in the data.
- Use their currency and their words for things (their product names, their stages in the CRM).
- They are busy. Move on as soon as a check has an answer; don't make them read theory.
- **Work out what you can; ask only what you can't.** The script decides which period is the recent one from the export's own labels or dates, and you state that in the report. Ask only when the data gives no way to tell: what a CRM source stands for, which of two properties to use. One short question beats a wrong reading.

## Say what you don't know

This diagnosis is only worth something if it is honest about its limits. When the data can't answer something, say so plainly, in one sentence, and say what would answer it:

> "I can't tell from this data whether the drop is tracking or rankings. The source on the last 20 leads in the CRM would settle it."

- No softening, no filling the gap with benchmarks, industry averages or what is "typical". An average from other companies is not a finding about theirs.
- **"Can't tell" and "not checked" are valid results.** A cause stays unconfirmed until their own data confirms it, however likely it sounds.
- Small numbers get said out loud: a handful of leads or conversions shows a direction, not a conclusion.
- If they can only give you part of the data, the diagnosis covers that part and says which part it doesn't cover.
- If too little is confirmed for three fixes, give fewer and say why. Never pad the list.
- If a later answer shows you read something wrong earlier, say so in those words ("I read this wrong earlier: ..."), then correct the diagnosis.

## Step 1. Who they are, who's asking, and for whom

**Before the first question**, if you can open web pages, read their website: the homepage, the product or solution pages, pricing, about, and a customer story if there is one. Work out what they sell, to whom (industry, company size, the role that buys), in which countries and languages, how the brand is written, and who they compare themselves with. If you can't open pages, or don't know the site yet, ask for the website address first.

Then send **one message** that shows what you understood and asks them to confirm, with choices:

> From your site: you sell fleet software to transport companies with 10 to 200 vehicles, in the Netherlands, Germany and Belgium, and people write you as "Acme Fleet" or "AcmeFleet". Is that right, or what would you change?
>
> Two quick ones:
> 1. What's your role? A) CMO or head of marketing B) Founder or CEO C) Something else
> 2. Who will read the report? A) Me B) My CEO C) My CFO D) The board

In the same message, ask what's going on in their own words, if they haven't said it yet: roughly how many organic visits and leads a month, whether that changed and since when, and any change to the site, forms, tracking or CRM, with a date. Rules 1, 5 and 6 in the judgment file depend on those dates.

**The asker and the reader can be different people.** Keep both in mind for the rest of the work:
- The report is written for the reader, in the order visuals.md gives for that reader.
- When the reader isn't the asker, the asker also gets a short briefing for themselves (visuals.md, The asker's briefing).
- Pitch your questions and the chat to the asker: a CMO gets marketing terms, a founder gets plain business words.

## Step 2. Ask for the data, all at once

Ask for everything in one message, with the steps for each, so they can do it in one sitting. Ask for what they can get in ten minutes. [references/data-exports.md](references/data-exports.md) has the click-by-click steps; give them only the steps for what they're about to export.

| File | Where it comes from | Used for |
|---|---|---|
| Search Console Performance export, last 3 months compared with the previous period | Search Console, Performance, Compare, Export | Checks 1 to 3 and 5, rules 1, 2 and 4 |
| Optional, worth asking for: a second export, the last 16 months without comparison (or at least 12) | Search Console, Performance, Export | The trend: when things moved, and what else happened then |
| CRM leads from the last quarter, with source | Their CRM | Checks 8 and 9 |

If a Search Console connector is available in their Claude, use it for the same data instead of asking for exports, and say which you used. Make the 16 months an easy yes: one line on why (it shows when things moved). Ask for the comparison: without it, the rules that compare two periods have nothing to read. If they can't export, work from what they can read off the screen and say the result is less precise. Don't stall the whole diagnosis on one missing file.

## Step 3. Run the numbers

When the Search Console export arrives, run [scripts/gsc_summary.py](scripts/gsc_summary.py) on it with their brand terms:

```
python scripts/gsc_summary.py <export.zip or folder> --brand "acme" --brand "acme cloud" --markets "Netherlands,Germany,Belgium" --chart-data
```

It reports brand and non-brand clicks, the share of clicks from their markets, the top 50 queries and the top 10 landing pages, and with `--chart-data` the same figures as JSON for the charts. It works on the zip Search Console gives, a folder of its CSVs, or an Excel file. If the script fails on their file, or a column in their export isn't one you recognise, ask them what it is, then read the file yourself with pandas and do the same sums; say which way you did it.

Then do the part a script can't: go through the 50 top queries and mark each **buyer**, **maybe** or **not a buyer** (students, job seekers, definitions, people looking for a login page), with a few words on why, using what you learned about their buyers in step 1. Don't make them review all 50: put the few you're least sure of in the next message as quick choices, and count once they've answered. Their judgment of their own market beats yours.

Report what you found as visuals.md describes for chat: labelled as a first read, findings as "so far", one compact table, and what happens next. Not the script's full tables, and nothing that looks like the finished diagnosis.

With a 12 to 16-month export, the script adds the trend: clicks and impressions per month, and the weeks that moved most. For each of those weeks, look for what else happened then, before you read anything into it:

1. **Their own changes**: ask about relaunches, migrations, navigation or template changes, new or removed pages, tracking or CRM changes, with dates.
2. **Google's confirmed updates**: check the dates on Google's Search Status Dashboard (status.search.google.com) if you can search the web; otherwise ask them, or mark it "not checked".
3. **Search Console's own data errors**: the script flags known ones in the range. Google lists them on its Data anomalies page in Search Console help. Impressions were over-reported from 13 May 2025 to 27 April 2026, so never compare impressions or CTR across that period; clicks are fine.
4. **The calendar**: holidays, August, the end of a quarter in their market.

Timing is a lead, not proof. A dip that lines up with a core update and with Christmas is not explained by either until something else rules the other out. Say which explanation the data supports, and how sure you are.

Search Console hides rare queries for privacy, so the query table adds up to less than the site's total clicks. The script shows the gap; mention it once so nobody is surprised.

With a two-period export, the script works out which period is the recent one from the labels or the dates in them, and prints how it decided. Don't ask about it; write it in the report's detail ("'Last 3 months' read as the recent period, from the export's labels"). Only if the script says it couldn't tell, ask, as one choice. Then read the numbers with [references/judgment.md](references/judgment.md), rules 1, 2 and 4: flat visibility while leads moved, impressions up with clicks flat, and brand searches losing clicks to an AI Overview.

## Step 4. One message: the first read and the quick checks

Send the first read (step 3) and everything you still need from them in **one message**, so they can answer it in one go:

- the few searches you're unsure are buyers, as choices
- for each week the trend flags, "did anything change on your side around [date]?", as choices
- the checks only they can do, from [references/checks.md](references/checks.md): Critical first, each with what to do and what "done" looks like, skipping any they've already answered

Say plainly that they can skip any of it and get the report now: a skipped check becomes "not checked", and they can come back and add it. If they skip the lot, build the report from what you have and say how much that leaves open.

## Step 5. Match findings to causes

Use [references/causes.md](references/causes.md), and read every finding through [references/judgment.md](references/judgment.md) before you name a cause: rule 5 (structural or acute) for every gap, rule 3 (find the asymmetry) whenever a blended number or an agreed explanation is doing the work, and rule 6 (damage is channel-shaped) when a site change lines up with fewer leads. For each cause, decide: **confirmed**, **ruled out**, **can't tell from this data** or **not checked**, with the evidence (or what's missing) in one line. Rank the confirmed ones by how many leads they likely cost, using their numbers.

## Step 6. The diagnosis

Create a one-page diagnosis as an HTML artifact with inline SVG charts (or a document, if artifacts are off), following [references/visuals.md](references/visuals.md). The order below is for a CMO or head of marketing. For a CFO or CEO, keep the same sections and numbers and follow the order in visuals.md, Order by reader. If they want a version for a second reader, make it from the same findings. Top to bottom, so a reader who stops early still has the answer:

1. **The answer**: one sentence they can repeat to their CEO, with the company name and date above it.
2. **The six causes at a glance**: a strip of six tiles, each marked confirmed, ruled out, can't tell from this data, or not checked, with an icon and the word.
   Under it, one line on scope: "A diagnosis of the organic coverage you have today, from [N] months of your own data. A direction, not a forecast or a growth strategy."
3. **What to fix first**: up to three cards (fewer if fewer are confirmed), all on pages and content they already have, in order, each with a first step, an owner and how they'll know it worked. Then a short **Outside organic search** box: findings that cost leads but belong to someone else (reply time, lead routing, CRM sources), each with who should get it. Default order is by cost, cheapest first (see causes.md), unless their data says otherwise. Before a comparison page or any new page goes on the list, apply rules 7 and 8 in judgment.md.
4. **What I couldn't tell**: each question the data couldn't answer, in one plain sentence, with what would answer it and who has it.
5. **The evidence**: one chart per finding that matters, under the cause it proves, each titled with its takeaway and naming the judgment rule used, if any.
6. **The detail**: the ten checks by stage (level, what was done, what was found, a checkbox), progress (how many of ten are done), the "Not now" lists, and one line at the bottom: "Based on the free organic leads checklist by Baba SEO: https://www.baba-seo.com/website-leads-checklist"

7. **What comes next**: one short paragraph. This shows what holds back the pages they have. Growing beyond them takes a revenue-first SEO strategy: which buyers to reach, with which pages, in which order, and someone to own it. No sales pitch, no names.

It has to print cleanly, work in light and dark mode, and work with a keyboard and a screen reader.

If the reader isn't the asker, also make the asker's briefing as a separate artifact or document (visuals.md, The asker's briefing). The report is the one they forward; the briefing stays with them.

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

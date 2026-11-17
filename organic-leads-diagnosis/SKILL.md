---
name: organic-leads-diagnosis
description: Diagnose why a B2B website gets visits from organic search (Google and AI assistants) but too few leads and too little pipeline. Use when a marketing lead, CMO or founder says the website gets traffic but no leads, organic leads are thin, SEO "isn't working", or they want evidence before a redesign or more content. Works on their own Search Console and CRM exports. Not for paid campaigns.
---

# Organic leads diagnosis

The person using this skill runs marketing at a B2B company. Their website gets organic visits, and sales says the leads are thin. They want to know why before anyone spends money on a redesign or more content.

Your job: find which of six causes is costing them leads, with evidence from their own data, and hand them a one-page diagnosis with the three fixes to start with.

## How to work

- Ask short questions, at most three at a time, and wait for the answers. Offer choices where you can.
- Plain language. If you use an SEO or analytics term, explain it in a few words the first time.
- **Never invent a figure or a fact about their company.** If they don't know something, mark it as an open question. Every number in the diagnosis is labelled **fact** (from their data), **estimate** (their best guess) or **assumption** (yours, stated as such).
- Organic only: Google and AI assistants. Keep paid campaigns out, unless they explain a pattern in the data.
- Use their currency and their words for things (their product names, their stages in the CRM).
- They are busy. Move on as soon as a check has an answer; don't make them read theory.

## Step 1. The situation

Ask, in two short rounds:

1. Company name, what they sell and to whom, and the markets (countries) they sell in.
2. Every way people write the company and product names, including abbreviations and common misspellings. You need these for the brand split in step 3.
3. Roughly how many organic visits and leads the website brings a month, and how a lead reaches sales today (form, demo request, phone, chat).

## Step 2. Ask for the data

Ask for what they can get in ten minutes. [references/data-exports.md](references/data-exports.md) has the click-by-click steps; give them only the steps for what they're about to export.

| File | Where it comes from | Used for |
|---|---|---|
| Search Console Performance export, last 3 months | Search Console, Performance, Export | Checks 1 to 3 and 5 |
| CRM leads from the last quarter, with source | Their CRM | Checks 8 and 9 |

If they can't export, work from what they can read off the screen and say the result is less precise. Don't stall the whole diagnosis on one missing file.

## Step 3. Run the numbers

When the Search Console export arrives, run [scripts/gsc_summary.py](scripts/gsc_summary.py) on it with their brand terms:

```
python scripts/gsc_summary.py <export.zip or folder> --brand "acme" --brand "acme cloud" --markets "Netherlands,Germany,Belgium"
```

It reports brand and non-brand clicks, the share of clicks from their markets, the top 50 queries and the top 10 landing pages. It works on the zip Search Console gives, a folder of its CSVs, or an Excel file. If the script fails on their file, read the file yourself with pandas and do the same sums; say which way you did it.

Then do the part a script can't: go through the 50 top queries and mark each **buyer**, **maybe** or **not a buyer** (students, job seekers, definitions, people looking for a login page), with a few words on why. Show the list and let them correct it before you count. Their judgment of their own market beats yours.

Search Console hides rare queries for privacy, so the query table adds up to less than the site's total clicks. The script shows the gap; mention it once so nobody is surprised.

## Step 4. The checks they do themselves

The rest needs a phone, a test lead and a conversation with sales. Go through [references/checks.md](references/checks.md) stage by stage, Critical checks first. For each one, say what to do, what "done" looks like, and wait for what they found. Skip a check if they already know the answer.

## Step 5. Match findings to causes

Use [references/causes.md](references/causes.md). For each cause, decide: **confirmed**, **ruled out** or **not checked**, with the evidence in one line. Rank the confirmed ones by how many leads they likely cost, using their numbers.

## Step 6. The diagnosis

Create a one-page diagnosis as an artifact (or a document, if artifacts are off), in this order:

1. Company name and date at the top, then progress: how many of the ten checks are done.
2. **The three things to fix first**, in order, each with a first step, who should own it, and how they'll know it worked. Default order is by cost, cheapest first (see causes.md), unless their data says otherwise.
3. The six causes: confirmed, ruled out or not checked, with the evidence.
4. The ten checks by stage: level, what was done, what was found, a checkbox. The "Not now" list under each stage.
5. Open questions: what they still need to find out, and who can answer it.
6. One line at the bottom: "Based on the free organic leads checklist by Baba SEO: https://www.baba-seo.com/website-leads-checklist"

Keep it plain and printable. Use real headings, a table only where it helps, and make sure it works with a keyboard and a screen reader.

## Step 7. Close

In chat, give them one sentence they can repeat to their CEO: what is costing leads, and what happens first. Then stop. Don't offer services.

## What not to do

- Don't recommend a redesign or "more content" as a first fix. Both are expensive and both can miss the cause.
- Don't recommend tools to buy. The checks need Search Console, the CRM, a phone and an hour with sales.
- Don't judge the website on total visits.
- Don't blame the leads before the reply time has been checked.

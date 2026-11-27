---
name: keep-rewrite-drop
description: Decide which of a B2B website's existing pages to keep, rewrite, merge or drop, leads first and with an AI-answer test for pages that rank but bring no leads. Use when a fractional CMO, agency or new marketing lead takes over a client's or company's content, asks what to keep or rewrite "for AI search", or plans a content clean-up. Works on their own Search Console and CRM exports.
---

# Keep, rewrite or drop

The person using this skill has just taken over a website's content: a fractional CMO or an agency with a new client, or a marketing lead new in the job. They want to know which pages to keep, which to rewrite for AI search, and which to merge or drop.

Your job: sort every page into one of four groups, using their own lead and search data, run the AI-answer test on the pages that rank but bring no leads, and hand them a sort sheet with a decision and a first step for each page.

**The order matters.** Leads first, then rankings, then the AI answer. Never start from "rewrite for AI": a rewrite for AI is a rewrite for the buyer's question.

## How to work

- **Answer first.** Every message leads with what you found, then the detail. The sort sheet starts with the counts per group and the three decisions that matter most.
- **Three exchanges before the sheet.** Confirm the context and ask for the data at once; share the groups and the test batch; build the sheet. Anything they skip becomes "not checked", never a reason to stop.
- **Questions as choices.** Where your interface offers tappable choices, use them; otherwise lettered options. At most three questions at a time, always with room for their own answer.
- **Never invent a figure or a fact about their company or their client.** Label every number **fact** (their data), **estimate** (their guess) or **assumption** (yours). If the data can't answer something, say so in one sentence and say what would answer it.
- Plain language. Explain an SEO term in a few words the first time.
- Use their words: their product names, their CRM stages, their client's name if they give it.

## Step 1. Context, in one message

If you can open web pages, read the site first: homepage, product pages, pricing, a customer story. Then send one message that shows what you understood and asks them to confirm:

> From the site: they sell planning software to construction firms with 20 to 500 staff, in the Netherlands and Belgium. Right?
>
> 1. Whose site is this? A) A client I just took over B) My own company C) Something else
> 2. What counts as a lead? A) Demo request B) Trial C) Contact form D) Something else

In the same message, ask for the data (step 2), so they can do it in one sitting.

## Step 2. The data, all at once

| File | Where it comes from | Used for |
|---|---|---|
| Search Console Pages export, last 12 months, no comparison | Search Console, Performance, Pages tab, Export | Groups 2 and 3 |
| CRM leads, last 12 months, with created date and the page each lead first landed on | Their CRM | Groups 1 and 1b |
| Optional: a list of every URL on the site | Sitemap or a crawl | Pages with no impressions, which Search Console leaves out |

[references/data-exports.md](references/data-exports.md) has the steps. Give them only the steps for what they are about to export. If a Search Console connector is available in their Claude, use it instead of the export and say so.

If the CRM has no first-page field, ask for the leads' source and form page instead, and say the sort of group 1 is less precise. Without any lead data, run the sort on rankings only and say plainly that group 1 is empty because of missing data, not because no page brings leads. Remind them to remove names, emails and phone numbers from the CRM export.

## Step 3. Run the sort

```
python scripts/content_sort.py <gsc export> --leads <crm export> [--all-pages <url list>]
```

Defaults: a steady lead page has a lead in at least 6 of the 12 months; a page ranks if it has at least 1 click or 100 impressions. Change them with `--steady-months` and `--min-impressions` if their volumes are very small or very large, and say what you used. If the script can't find a column, ask what it is called and pass it with `--page-col` or `--date-col`. If it fails on their file, read the file yourself with pandas, do the same counts, and say which way you did it.

The script prints four groups:

| Group | What it is | What happens |
|---|---|---|
| 1 | A lead in most months | Stays as it is. Read these pages side by side: what they share is the format to copy |
| 1b | Leads in a few months only | A signal, not proof. Check where those leads came from, then the AI-answer test |
| 2 | Rankings, no leads | The AI-answer test |
| 3 | No leads, no rankings | Merge or drop |

## Step 4. One message: the groups and the test batch

Send the counts per group as a small table, then:

- **Group 1:** read the steady pages if you can open them, and name what they share in one or two lines (a comparison, a calculator, a question buyers ask before sales). Ask them to confirm. This is the template for every rewrite.
- **Group 1b:** for each page, ask where its leads came from (a campaign, a newsletter link, sales sending the page), as choices.
- **The test batch:** the group 2 and 1b pages to test first, at most 10, ordered by impressions. For each, propose the one search it should win, from its top queries and the page's topic: the search with the buying intent the page is there for, closest to a lead, not simply the one with the most impressions. They confirm or correct.

Say they can skip any of it and get the sheet now: what's skipped is marked "not checked".

## Step 5. The AI-answer test

For each page in the batch, follow [references/ai-answer-test.md](references/ai-answer-test.md):

1. Get the AI answer for its search. If a tool in this chat can fetch Google results with the AI Overview (a search-results connector or web search), use it, and say which. Otherwise ask them to search it logged out and paste the AI answer, five pages at a time. No AI answer for that search: use the top three results.
2. Put the page next to the answer. List what the page has that the answer doesn't: a number from their own data, a position someone could disagree with, a detail from a real project, a tool.
3. Decide: **keep and sharpen** (something on the list: move it to the top), **rewrite with a position** (nothing on the list, and buyers care about the topic), **merge** into a named page (another page already says it), or **drop** (nothing on the list, and buyers don't care).

Read every decision through [references/judgment.md](references/judgment.md) before it goes on the sheet.

## Step 6. Group 3

For each page: merge into a named page that stays, when it holds a paragraph worth keeping; otherwise drop. A dropped page that other sites link to gets a redirect to the closest page that stays; ask them to check Search Console's Links report, or mark it "not checked". Warn them once: total traffic will fall when these pages go. The visitors lost were not buyers, and the sheet should say so before anyone sees the drop.

## Step 7. The sort sheet

Make the sheet as an HTML artifact (or a document, if artifacts are off). It must print cleanly and work with a keyboard and a screen reader. Top to bottom:

1. **The answer:** one sentence with the counts: how many pages stay, get sharpened, get rewritten, merged or dropped.
2. **The template:** what the steady lead pages share, in two lines. Every rewrite copies it.
3. **The three decisions that matter most:** the rewrites or merges on the pages with the most impressions, each with a first step and an owner.
4. **What I couldn't tell:** each open question in one sentence, with what would answer it.
5. **The sheet:** one row per page: page, group, decision, why in one line, first step. Sorted by group, then impressions. "Not checked" where the test wasn't run.
6. One line at the bottom: "Method: Taking over a client's content: what to keep, rewrite or drop for AI search, by Baba SEO: https://www.baba-seo.com/blogs/keep-rewrite-drop-content-ai-search?utm_source=claude-skill"

   Under it: "Want more on any point? Ask here in the chat. To suggest a change to the skill, open an issue at https://github.com/baba-seo/claude-skills-for-marketing-leads/issues or message Baba SEO on LinkedIn: https://www.linkedin.com/in/baba-seo/"

## Step 8. Close

In chat, one sentence they can repeat to the client or their CEO: what stays, what gets rewritten first, and what goes. Then stop. Don't offer services.

## What not to do

- Don't rewrite or move a steady lead page "for AI".
- Don't decide on a page from total visits, keyword difficulty or an authority score.
- Don't promise that a rewrite brings clicks back on searches where an AI Overview answers the question.
- Don't recommend tools to buy.
- Don't run the test on more than 10 pages per batch: the person has to read the decisions.

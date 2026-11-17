# Claude skills for marketing leads

Free Claude skills for the person who has to explain what organic search brings in: the CMO, the head of marketing, the founder who still owns marketing. Each skill does one job with your own data and ends with something you can show upstairs.

These are built for you to run on your own. They aren't the skills I use for client work.

## The skills

| Skill | What it does | You need |
|---|---|---|
| [organic-leads-diagnosis](organic-leads-diagnosis/SKILL.md) | Finds why your B2B website gets organic visits (Google and AI assistants) but too few leads, and gives you a one-page diagnosis with the three fixes to start with | A Search Console export (last 3 months against the previous period), your CRM, a phone and an hour with sales |

**Download:** [organic-leads-diagnosis.zip](https://github.com/baba-seo/claude-skills-for-marketing-leads/raw/main/organic-leads-diagnosis.zip)

## More than a checklist

The ten checks are public on my site. What the skill adds is how I read what they turn up: eight rules from my own diagnosis work, each with the trigger, the decision, why, and when it doesn't apply. A few of them:

- When organic leads move but Search Console visibility doesn't, it's a tracking question first, whichever way the number went. An unexplained rise is riskier than a drop, because a rise gets budgeted against.
- When impressions grow and clicks don't, the fix is content only your company could write, not more of it.
- A site change hits organic leads harder than paid, so "paid is fine" doesn't clear the website.

Claude applies a rule only when its trigger is in your data, and says in the diagnosis which one it used, so you can follow the reasoning and disagree with it. All eight are in [judgment.md](organic-leads-diagnosis/references/judgment.md).

## Install it in Claude

1. In Claude, go to **Settings**, then **Capabilities**, and turn on **Code execution and file creation** (called **Create and edit files** in the newer settings layout). Skills need it.
2. Download the zip above. Don't unzip it.
3. Go to **Customize**, then **Skills**. Click **+**, then **+ Create skill**, then **Upload a skill**, and choose the zip.
4. Check the skill is switched on in your skills list.

On a Team or Enterprise plan, an owner may have to allow skills first. Skills you turn on in your Claude settings also load in Claude Code when you sign in with the same account.

These steps follow Anthropic's help article on [using skills in Claude](https://support.claude.com/en/articles/12512180-use-skills), checked in November 2026. If the menus have moved, that page has the current ones.

## Use it

Start a new chat and say what's going on, for example:

> Our website gets organic traffic but sales says the leads are thin. Use the organic leads diagnosis.

Claude asks a few short questions about your company, then asks for your Search Console export and tells you exactly where to click. It does the sums on the export, marks your top searches as buyer or not (you correct it), walks you through the checks that need a phone and a test lead, and builds the diagnosis.

It never makes up a figure about your company. Anything you don't know becomes an open question in the diagnosis, and every number is labelled as a fact, an estimate or an assumption.

## Before you install

A skill can run code, so read what you upload. This one has a single script, [`gsc_summary.py`](organic-leads-diagnosis/scripts/gsc_summary.py), which reads your Search Console export and prints a summary. It runs in Claude's own sandbox and sends nothing anywhere.

Remove names, emails and phone numbers from any CRM export before you upload it. The diagnosis doesn't need them.

## Without the skill

The same ten checks are on a free page you can tick off in your browser, with a prompt you can paste into any chat: the [organic leads checklist](https://www.baba-seo.com/website-leads-checklist). The article behind it explains the six causes: [why a B2B website gets organic visits but no pipeline](https://www.baba-seo.com/blogs/website-traffic-no-leads).

## Licence

[CC BY 4.0](LICENSE). Use it, change it and share it, also commercially, as long as you credit Baba SEO with a link to https://www.baba-seo.com.

## About

I'm Baba, a revenue-first SEO consultant in Amsterdam. I work with B2B companies on organic search that shows up in pipeline, not just in traffic reports. More at [baba-seo.com](https://www.baba-seo.com).

Found a mistake or a step that no longer matches Claude's menus? [Open an issue](https://github.com/baba-seo/claude-skills-for-marketing-leads/issues).

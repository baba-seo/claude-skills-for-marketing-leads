# Claude skills for marketing leads

Free Claude skills for the person who has to explain what organic search brings in: the CMO, the head of marketing, the founder who still owns marketing. Each skill does one job with your own data and ends with something you can show upstairs.

These are built for you to run on your own. They aren't the skills I use for client work.

## The skills

| Skill | What it does | You need |
|---|---|---|
| [organic-leads-diagnosis](plugins/marketing-leads/skills/organic-leads-diagnosis/SKILL.md) | Finds why your B2B website gets organic visits (Google and AI assistants) but too few leads, and gives you a one-page diagnosis with the fixes to start with, and what your data can't tell | A Search Console export (last 3 months against the previous period), your CRM, a phone and an hour with sales |
| [keep-rewrite-drop](plugins/marketing-leads/skills/keep-rewrite-drop/SKILL.md) | Sorts every page of a website you just took over into keep, rewrite, merge or drop: leads first, then an AI-answer test for the pages that rank but bring no leads. Ends with a sort sheet, one decision and first step per page | A Search Console Pages export (last 12 months) and your CRM leads with the page each lead first landed on |

## More than a checklist

The ten checks are public on my site. What the skill adds is how I read what they turn up: eight rules from my own diagnosis work, each with the trigger, the decision, why, and when it doesn't apply. A few of them:

- When organic leads move but Search Console visibility doesn't, it's a tracking question first, whichever way the number went. An unexplained rise is riskier than a drop, because a rise gets budgeted against.
- When impressions grow and clicks don't, the fix is content only your company could write, not more of it.
- A site change hits organic leads harder than paid, so "paid is fine" doesn't clear the website.

Claude applies a rule only when its trigger is in your data, and says in the diagnosis which one it used, so you can follow the reasoning and disagree with it. All eight are in [judgment.md](plugins/marketing-leads/skills/organic-leads-diagnosis/references/judgment.md).

## Install it in Claude

The skills come as a plugin, `marketing-leads`, from this repo. Add the repo once and you get every update I make, without downloading anything again.

**On a paid plan (Pro, Max, Team, Enterprise)**

1. In Claude, go to **Customize**, then **Plugins**.
2. Choose **Add**, then **Add marketplace**, and enter `baba-seo/claude-skills-for-marketing-leads`.
3. Add the **marketing-leads** plugin from it.
4. To get updates without thinking about it, turn on **Sync automatically** for the marketplace. Otherwise use **Check for updates** now and then.

On Team and Enterprise plans, an owner decides whether members can add their own marketplaces.

**On the Free plan**

Plugins are for paid plans, but a single skill works on Free too:

1. In **Settings**, then **Capabilities**, turn on **Code execution and file creation** (called **Create and edit files** in the newer layout).
2. Download the skill you want: [organic-leads-diagnosis.zip](https://github.com/baba-seo/claude-skills-for-marketing-leads/raw/main/organic-leads-diagnosis.zip) or [keep-rewrite-drop.zip](https://github.com/baba-seo/claude-skills-for-marketing-leads/raw/main/keep-rewrite-drop.zip). Don't unzip it.
3. Go to **Customize**, then **Skills**, click **+**, then **+ Create skill**, then **Upload a skill**, and choose the zip.

An uploaded zip doesn't update itself. Watch this repo on GitHub, or check back, and upload the new zip when the skill changes.

**In Claude Code**

```
/plugin marketplace add baba-seo/claude-skills-for-marketing-leads
/plugin install marketing-leads@baba-seo
```

These steps follow Anthropic's pages on [using plugins](https://claude.com/docs/plugins/overview) and [using skills](https://support.claude.com/en/articles/12512180-use-skills), checked in November 2026. If the menus have moved, those pages have the current ones.

## For IT and plugin owners

If your company reviews plugins before allowing them, [SECURITY.md](SECURITY.md) lists everything in this one and what it can't do: no connectors, no hooks or agents, no network, no file writes, checked automatically on every change. It also covers three ways to roll it out: add the marketplace and take updates, review once and upload a frozen copy ([marketing-leads-plugin.zip](https://github.com/baba-seo/claude-skills-for-marketing-leads/raw/main/marketing-leads-plugin.zip)), or skip installing and use the [free checklist page](https://www.baba-seo.com/website-leads-checklist) with its prompt.

## Use it

Start a new chat and say what's going on, for example:

> Our website gets organic traffic but sales says the leads are thin. Use the organic leads diagnosis.

or

> I just took over a client's website. Which pages do I keep, rewrite or drop? Use keep-rewrite-drop.

Claude asks a few short questions about your company, then asks for your Search Console export and tells you exactly where to click. It does the sums on the export, marks your top searches as buyer or not (you correct it), walks you through the checks that need a phone and a test lead, and builds the diagnosis.

It never makes up a figure about your company. When your data can't answer something, it says so in one plain sentence, with what would answer it, and the diagnosis keeps a "What I couldn't tell" section near the top. When it isn't sure what something in your data means, it asks you. Every number is labelled as a fact, an estimate or an assumption.

## Before you install

A skill can run code, so read what you upload ([SECURITY.md](SECURITY.md) has the five-minute version). This plugin has two scripts, [`gsc_summary.py`](plugins/marketing-leads/skills/organic-leads-diagnosis/scripts/gsc_summary.py) and [`content_sort.py`](plugins/marketing-leads/skills/keep-rewrite-drop/scripts/content_sort.py). Each reads the files you upload and prints a summary. It runs in Claude's own sandbox and sends nothing anywhere.

Remove names, emails and phone numbers from any CRM export before you upload it. Neither skill needs them.

## Without the skill

The same ten checks are on a free page you can tick off in your browser, with a prompt you can paste into any chat: the [organic leads checklist](https://www.baba-seo.com/website-leads-checklist). The article behind it explains the six causes: [why a B2B website gets organic visits but no pipeline](https://www.baba-seo.com/blogs/website-traffic-no-leads).

## Licence

[CC BY 4.0](LICENSE). Use it, change it and share it, also commercially, as long as you credit Baba SEO with a link to https://www.baba-seo.com.

## About

I'm Baba, a revenue-first SEO consultant in Amsterdam. I work with B2B companies on organic search that shows up in pipeline, not just in traffic reports. More at [baba-seo.com](https://www.baba-seo.com).

Found a mistake or a step that no longer matches Claude's menus? [Open an issue](https://github.com/baba-seo/claude-skills-for-marketing-leads/issues).

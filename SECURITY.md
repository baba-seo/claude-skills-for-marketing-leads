# What this plugin can and can't do

For IT, security and plugin owners who need to decide whether to allow it. Reviewing it takes about five minutes.

**In one line:** instructions written in Markdown, plus one Python script that reads the Search Console file a person uploads and prints a summary. Nothing else.

## What's in it

| File | What it is |
|---|---|
| `plugins/marketing-leads/.claude-plugin/plugin.json` | The plugin's name, description, author and licence. No connectors, hooks, agents or commands |
| `.../organic-leads-diagnosis/SKILL.md` | The instructions Claude follows |
| `.../references/*.md` | The checks, the causes, the export steps and the rules for reading the findings. Text only |
| `.../scripts/gsc_summary.py` | Reads the uploaded Search Console export and prints tables to the conversation |
| `.claude-plugin/marketplace.json` | The catalog that lets Claude add this repo as a marketplace |

The zips at the root of the repo are built from the same folder by a GitHub workflow, after the safety check passes.

## What it can't do

- **No connectors.** It can't reach any app, account or service.
- **No hooks, agents or commands.** Nothing runs on anyone's computer, and nothing runs on its own.
- **No network.** The script imports only `argparse`, `io`, `json`, `re`, `sys`, `zipfile`, `pathlib` and `pandas`.
- **No writes.** The script doesn't create, change or delete files. It reads the uploaded file and prints a summary.
- **Markdown, JSON and Python only.** No binaries, no other file types.

These aren't promises on a page. [`safety_check.py`](.github/scripts/safety_check.py) runs on every change to the repo and fails if any of them stops being true; the result is on the [Actions tab](https://github.com/baba-seo/claude-skills-for-marketing-leads/actions/workflows/safety-check.yml). The zips are only rebuilt after it passes.

## Where the data goes

The skill sends nothing anywhere. The files a person uploads go to Claude, like any other upload, under your Claude plan's terms. In Claude, the script runs in Claude's own code sandbox.

The skill asks people to take names, emails and phone numbers out of a CRM export before uploading it. The diagnosis doesn't need them.

## Three ways to roll it out

| Option | How | What changes later |
|---|---|---|
| **Add the marketplace** | Customize, Plugins, Add, Add marketplace: `baba-seo/claude-skills-for-marketing-leads` | Updates arrive from this repo, each one through the safety check |
| **Review once, upload a copy** | Download [marketing-leads-plugin.zip](https://github.com/baba-seo/claude-skills-for-marketing-leads/raw/main/marketing-leads-plugin.zip), review it, and upload it: Customize, Plugins, Add, Upload plugin, or as an owner in your organization's plugin settings | Nothing, until you upload a newer copy |
| **No install at all** | The same checks as a free page with a prompt to paste into any chat: [organic leads checklist](https://www.baba-seo.com/website-leads-checklist) | Nothing to update |

On Team and Enterprise plans, an owner decides which plugin sources members see and whether they can add their own. Anthropic's own review covers plugins listed in its directory; this one is not listed there, which is why this page exists.

## Review it in five minutes

1. Read `SKILL.md`. It's the full set of instructions, in plain English.
2. Open `gsc_summary.py` and check the imports at the top.
3. Open `plugin.json` and check that it only names the plugin.
4. Check the [safety check](https://github.com/baba-seo/claude-skills-for-marketing-leads/actions/workflows/safety-check.yml) passed on the latest commit.

## Report a problem

Open an [issue](https://github.com/baba-seo/claude-skills-for-marketing-leads/issues). For anything you'd rather not post in public, send me a direct message on [LinkedIn](https://www.linkedin.com/in/baba-seo/).

Built and maintained by [Baba SEO](https://www.baba-seo.com). Licence: [CC BY 4.0](LICENSE).

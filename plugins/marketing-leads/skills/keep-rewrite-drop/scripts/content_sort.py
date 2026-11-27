"""Sort a website's pages into keep, test, and merge-or-drop groups.

Reads a Search Console Pages export (12 months, no comparison) and, if given,
a CRM leads export with the page each lead first landed on. Prints the groups
to the conversation. Reads files only; writes nothing and connects to nothing.

Usage:
  python content_sort.py <gsc export: zip, folder, CSV or Excel>
      [--leads crm.csv] [--page-col "Landing page"] [--date-col "Created"]
      [--all-pages urls.csv] [--steady-months 6] [--min-impressions 100]
      [--top 25] [--json]

Groups:
  1  Steady lead pages: a lead in at least --steady-months different months. Keep.
  1b Occasional lead pages: leads in fewer months. A signal, not proof: check
     where the lead came from, then they go through the AI-answer test.
  2  Rankings, no leads: at least one click or --min-impressions impressions.
     These go through the AI-answer test.
  3  Neither: no leads, and below the impressions bar. Merge or drop.
"""

import argparse
import io
import json
import re
import sys
import zipfile
from pathlib import Path

import pandas as pd


def norm_url(u):
    """Compare URLs without protocol, www, query, fragment or trailing slash."""
    if not isinstance(u, str) or not u.strip():
        return None
    u = u.strip().lower()
    u = re.sub(r"^[a-z]+://", "", u)
    u = re.sub(r"^www\.", "", u)
    u = re.split(r"[?#]", u)[0]
    return u.rstrip("/")


def read_any(path):
    """Return a list of DataFrames from a zip, folder, Excel or CSV file."""
    path = Path(path)
    frames = []
    if path.is_dir():
        for f in sorted(path.glob("*.csv")):
            frames.append(pd.read_csv(f))
    elif path.suffix.lower() in (".xlsx", ".xls"):
        frames.extend(pd.read_excel(path, sheet_name=None).values())
    elif zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as z:
            for name in z.namelist():
                if name.lower().endswith(".csv"):
                    frames.append(pd.read_csv(io.BytesIO(z.read(name))))
    elif path.suffix.lower() == ".csv":
        frames.append(pd.read_csv(path))
    else:
        sys.exit(f"Can't read {path}: expected a zip, a folder, a CSV or an Excel file.")
    return frames


def col(df, *words):
    for c in df.columns:
        if any(w in str(c).lower() for w in words):
            return c
    return None


def load_pages(path):
    for df in read_any(path):
        if df is None or df.empty:
            continue
        first = str(df.columns[0]).lower()
        if "page" in first and col(df, "clicks"):
            out = pd.DataFrame({
                "page": df[df.columns[0]].astype(str),
                "clicks": pd.to_numeric(df[col(df, "clicks")], errors="coerce").fillna(0),
                "impressions": pd.to_numeric(df[col(df, "impressions")], errors="coerce").fillna(0)
                if col(df, "impressions") else 0,
                "position": pd.to_numeric(df[col(df, "position")], errors="coerce")
                if col(df, "position") else None,
            })
            out["key"] = out["page"].map(norm_url)
            note = ""
            if len([c for c in df.columns if "clicks" in str(c).lower()]) > 1:
                note = ("The export compares two periods; only the first is used. "
                        "A 12-month export without comparison is better for this sort.")
            return out, note
    sys.exit("No Pages table found. Export Performance > Pages from Search Console and upload it as it is.")


def load_leads(path, page_col, date_col):
    frames = read_any(path)
    df = max(frames, key=len)
    pc = page_col if page_col in df.columns else col(df, "landing", "first page", "page", "url")
    dc = date_col if date_col in df.columns else col(df, "created", "date")
    if pc is None:
        sys.exit("No page column found in the leads file. Name it with --page-col.")
    leads = pd.DataFrame({"key": df[pc].map(lambda v: norm_url(v) if isinstance(v, str) else None)})
    leads["month"] = (pd.to_datetime(df[dc], errors="coerce").dt.to_period("M").astype(str)
                      if dc else None)
    missing = int(leads["key"].isna().sum())
    leads = leads.dropna(subset=["key"])
    return leads, pc, dc, missing, len(df)


def table(rows, cols, top):
    if rows.empty:
        return "_None._\n"
    lines = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for _, r in rows.head(top).iterrows():
        lines.append("| " + " | ".join(str(r[c]) for c in cols) + " |")
    if len(rows) > top:
        lines.append(f"\n_{len(rows) - top} more not shown (use --json for all)._")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("gsc")
    ap.add_argument("--leads")
    ap.add_argument("--page-col", default="")
    ap.add_argument("--date-col", default="")
    ap.add_argument("--all-pages", help="CSV with every URL on the site (sitemap or crawl), first column")
    ap.add_argument("--steady-months", type=int, default=6)
    ap.add_argument("--min-impressions", type=int, default=100)
    ap.add_argument("--top", type=int, default=25)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    pages, note = load_pages(a.gsc)
    pages = pages.groupby("key", as_index=False).agg(
        page=("page", "first"), clicks=("clicks", "sum"),
        impressions=("impressions", "sum"), position=("position", "mean"))

    if a.all_pages:
        urls = max(read_any(a.all_pages), key=len)
        extra = pd.DataFrame({"page": urls[urls.columns[0]].astype(str)})
        extra["key"] = extra["page"].map(norm_url)
        extra = extra[~extra["key"].isin(pages["key"])].dropna(subset=["key"])
        extra[["clicks", "impressions"]] = 0
        extra["position"] = None
        pages = pd.concat([pages, extra], ignore_index=True)

    lead_info = "No leads file given: every page is sorted on rankings only, and group 1 is empty."
    pages["leads"] = 0
    pages["lead_months"] = 0
    lead_only = pd.DataFrame()
    if a.leads:
        leads, pc, dc, missing, total = load_leads(a.leads, a.page_col, a.date_col)
        per = leads.groupby("key").agg(leads=("key", "size"),
                                       lead_months=("month", lambda m: m.dropna().nunique()))
        pages = pages.drop(columns=["leads", "lead_months"]).merge(per, how="left", left_on="key", right_index=True)
        pages[["leads", "lead_months"]] = pages[["leads", "lead_months"]].fillna(0).astype(int)
        lead_only = per[~per.index.isin(pages["key"])].reset_index()
        lead_only.columns = ["page", "leads", "lead_months"]
        lead_info = (f"Leads file: {total} rows, page from column '{pc}', month from column '{dc or 'none'}'. "
                     f"{missing} rows had no page and are left out.")
        if not dc:
            lead_info += " Without a date column, months can't be counted: every lead page is treated as occasional."

    def group(r):
        if r["lead_months"] >= a.steady_months:
            return "1"
        if r["leads"] > 0:
            return "1b"
        if r["clicks"] > 0 or r["impressions"] >= a.min_impressions:
            return "2"
        return "3"

    pages["group"] = pages.apply(group, axis=1)
    pages["position"] = pages["position"].map(lambda p: round(p, 1) if pd.notna(p) else "")
    pages["clicks"] = pages["clicks"].astype(int)
    pages["impressions"] = pages["impressions"].astype(int)
    pages = pages.sort_values(["group", "leads", "impressions"], ascending=[True, False, False])

    names = {
        "1": "Group 1: steady lead pages (keep, and study their format)",
        "1b": "Group 1b: occasional lead pages (check the lead's source, then test)",
        "2": "Group 2: rankings, no leads (AI-answer test)",
        "3": "Group 3: neither (merge or drop)",
    }
    cols = ["page", "leads", "lead_months", "clicks", "impressions", "position"]

    if a.json:
        print(json.dumps({
            "settings": {"steady_months": a.steady_months, "min_impressions": a.min_impressions},
            "notes": [n for n in (note, lead_info) if n],
            "counts": pages["group"].value_counts().to_dict(),
            "pages": pages[["group"] + cols].to_dict(orient="records"),
            "lead_pages_not_in_search_console": lead_only.to_dict(orient="records"),
        }, default=str, indent=1))
        return

    print("# Content sort\n")
    print(f"Settings: steady = a lead in at least {a.steady_months} different months; "
          f"ranking = at least 1 click or {a.min_impressions} impressions.\n")
    for n in (note, lead_info):
        if n:
            print(f"- {n}")
    print(f"- Search Console exports at most 1,000 rows per table, and pages with no impressions don't appear. "
          f"{'A full URL list was added.' if a.all_pages else 'Add a sitemap or crawl list with --all-pages to see those pages too.'}\n")
    print("| Group | Pages | Leads | Clicks |")
    print("|---|---|---|---|")
    for g in ("1", "1b", "2", "3"):
        sub = pages[pages["group"] == g]
        print(f"| {names[g].split(':')[0]} | {len(sub)} | {int(sub['leads'].sum())} | {int(sub['clicks'].sum())} |")
    print()
    for g in ("1", "1b", "2", "3"):
        print(f"## {names[g]}\n")
        print(table(pages[pages["group"] == g], cols, a.top))
    if not lead_only.empty:
        print("## Lead pages with no Search Console data\n")
        print("Often paid landing pages or pages outside the property. Leave them out of the sort.\n")
        print(table(lead_only, ["page", "leads", "lead_months"], a.top))


if __name__ == "__main__":
    main()

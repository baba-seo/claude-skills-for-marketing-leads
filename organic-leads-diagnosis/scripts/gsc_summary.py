"""Summarise a Google Search Console Performance export for the organic leads diagnosis.

Reads the zip Search Console gives with "Download CSV", a folder of those CSVs,
or the file from "Download Excel". Reports brand and non-brand clicks, the
share of clicks from the markets the company sells in, the top 50 queries and
the top 10 landing pages.

Usage:
  python gsc_summary.py EXPORT --brand "acme" [--brand "acme cloud"] [--markets "Netherlands,Germany"]

Brand terms match anywhere in a query, ignoring case. Market names must be
written as Search Console writes them in the Countries table (in English,
for example "Netherlands", "United Kingdom").
"""

import argparse
import io
import sys
import zipfile
from pathlib import Path

import pandas as pd

KINDS = {
    "queries": ("quer",),
    "pages": ("page",),
    "countries": ("countr",),
    "dates": ("date",),
}


def classify(df):
    """Name a table by its first column header."""
    if df is None or df.empty or "Clicks" not in df.columns:
        return None
    first = str(df.columns[0]).lower()
    for kind, keys in KINDS.items():
        if any(k in first for k in keys):
            return kind
    return None


def load_tables(path):
    path = Path(path)
    frames = []
    if path.is_dir():
        for f in sorted(path.glob("*.csv")):
            frames.append(pd.read_csv(f))
    elif path.suffix.lower() in (".xlsx", ".xls"):
        # Checked before zip: an .xlsx file is a zip too.
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
    tables = {}
    for df in frames:
        kind = classify(df)
        if kind and kind not in tables:
            df = df.copy()
            df["Clicks"] = pd.to_numeric(df["Clicks"], errors="coerce").fillna(0)
            tables[kind] = df
    return tables


def pct(part, whole):
    return f"{part / whole * 100:.0f}%" if whole else "n/a"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("export")
    ap.add_argument("--brand", action="append", default=[], help="a brand term; repeat for each spelling")
    ap.add_argument("--markets", default="", help="comma-separated country names as Search Console writes them")
    args = ap.parse_args()

    t = load_tables(args.export)
    if "queries" not in t:
        sys.exit("No queries table found. Export from Search Console > Performance > Search results.")

    q = t["queries"]
    qcol = q.columns[0]
    q_total = q["Clicks"].sum()
    site_total = t["dates"]["Clicks"].sum() if "dates" in t else None

    print("# Search Console summary\n")
    print(f"Clicks in the queries table: {q_total:,.0f}")
    if site_total:
        hidden = site_total - q_total
        print(f"Clicks for the whole site: {site_total:,.0f}")
        print(f"Clicks on queries Search Console doesn't show: {hidden:,.0f} ({pct(hidden, site_total)})")
    print()

    if args.brand:
        terms = [b.lower() for b in args.brand]
        is_brand = q[qcol].astype(str).str.lower().apply(lambda s: any(b in s for b in terms))
        b_clicks = q.loc[is_brand, "Clicks"].sum()
        nb_clicks = q_total - b_clicks
        print("## Brand split (check 2)\n")
        print("| Group | Clicks | Share of shown clicks |")
        print("|---|---|---|")
        print(f"| Brand ({', '.join(args.brand)}) | {b_clicks:,.0f} | {pct(b_clicks, q_total)} |")
        print(f"| Non-brand | {nb_clicks:,.0f} | {pct(nb_clicks, q_total)} |")
        print()
    else:
        is_brand = pd.Series(False, index=q.index)
        print("No --brand terms given: brand split skipped.\n")

    if "countries" in t and args.markets:
        c = t["countries"]
        ccol = c.columns[0]
        markets = [m.strip().lower() for m in args.markets.split(",") if m.strip()]
        in_mkt = c[ccol].astype(str).str.lower().isin(markets)
        c_total = c["Clicks"].sum()
        m_clicks = c.loc[in_mkt, "Clicks"].sum()
        found = set(c.loc[in_mkt, ccol].astype(str).str.lower())
        missing = [m for m in markets if m not in found]
        print("## Markets (check 3)\n")
        print(f"Clicks from markets they sell in: {m_clicks:,.0f} of {c_total:,.0f} ({pct(m_clicks, c_total)})")
        if missing:
            print(f"No clicks recorded from: {', '.join(missing)} (if that is unexpected, check the spelling against the Countries table)")
        top = c.sort_values("Clicks", ascending=False).head(10)
        print("\n| Country | Clicks | In their markets |")
        print("|---|---|---|")
        for _, r in top.iterrows():
            print(f"| {r[ccol]} | {r['Clicks']:,.0f} | {'yes' if str(r[ccol]).lower() in markets else 'no'} |")
        print()

    print("## Top 50 queries (check 1: mark each buyer, maybe or not a buyer)\n")
    print("| # | Query | Clicks | Brand |")
    print("|---|---|---|---|")
    top_q = q.assign(_brand=is_brand).sort_values("Clicks", ascending=False).head(50)
    for i, (_, r) in enumerate(top_q.iterrows(), 1):
        print(f"| {i} | {r[qcol]} | {r['Clicks']:,.0f} | {'yes' if r['_brand'] else ''} |")
    print()

    if "pages" in t:
        p = t["pages"]
        pcol = p.columns[0]
        print("## Top 10 landing pages (checks 5 and 6)\n")
        print("| # | Page | Clicks |")
        print("|---|---|---|")
        for i, (_, r) in enumerate(p.sort_values("Clicks", ascending=False).head(10).iterrows(), 1):
            print(f"| {i} | {r[pcol]} | {r['Clicks']:,.0f} |")
        print()

    print("Search Console exports show at most 1,000 rows per table.")


if __name__ == "__main__":
    main()

"""Summarise a Google Search Console Performance export for the organic leads diagnosis.

Reads the zip Search Console gives with "Download CSV", a folder of those CSVs,
or the file from "Download Excel". Works with a single period or a comparison
of two periods (Search Console's "Compare" date option).

Reports brand and non-brand clicks, impressions and CTR, brand searches by
group, the share of clicks from the markets the company sells in, the top 50
queries and the top 10 landing pages.

Usage:
  python gsc_summary.py EXPORT --brand "acme" [--brand "acme cloud"] [--markets "Netherlands,Germany"]

Brand terms match anywhere in a query, ignoring case. Market names must be
written as Search Console writes them in the Countries table (in English,
for example "Netherlands", "United Kingdom").
"""

import argparse
import io
import re
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

BRAND_GROUPS = [
    ("login", r"log ?in|sign ?in|account|portal|app\b"),
    ("pricing", r"pric|cost|tarie|kosten|preis|prix|plan\b|plans\b"),
    ("reviews", r"review|rating|ervaring|bewertung|avis|trustpilot|g2\b|capterra"),
    ("comparison", r"\bvs\b|versus|alternativ|compar|vergelijk|vergleich"),
    ("support", r"support|help|contact|phone|telefoon|klantenservice|kundenservice"),
]


def metric_columns(df, word):
    return [c for c in df.columns if word in str(c).lower()]


def periods_of(df):
    """Return [(label, clicks_col, impressions_col, position_col)], current period first."""
    out = []
    for c in metric_columns(df, "clicks"):
        label = re.sub(r"(?i)\s*clicks\s*", " ", str(c)).strip() or "Selected period"
        imp = next((i for i in metric_columns(df, "impressions")
                    if re.sub(r"(?i)\s*impressions\s*", " ", str(i)).strip() == re.sub(r"(?i)\s*clicks\s*", " ", str(c)).strip()), None)
        pos = next((p for p in metric_columns(df, "position")
                    if re.sub(r"(?i)\s*position\s*", " ", str(p)).strip() == re.sub(r"(?i)\s*clicks\s*", " ", str(c)).strip()), None)
        out.append((label, c, imp, pos))
    return out


def classify(df):
    """Name a table by its first column header."""
    if df is None or df.empty or not metric_columns(df, "clicks"):
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
            for word in ("clicks", "impressions", "position"):
                for c in metric_columns(df, word):
                    df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0)
            tables[kind] = df
    return tables


def pct(part, whole):
    return f"{part / whole * 100:.0f}%" if whole else "n/a"


def ctr(clicks, imps):
    return f"{clicks / imps * 100:.1f}%" if imps else "n/a"


def wpos(df, pos, imp):
    """Average position weighted by impressions, as Search Console reports it."""
    if pos is None or imp is None or df[imp].sum() == 0:
        return "n/a"
    return f"{(df[pos] * df[imp]).sum() / df[imp].sum():.1f}"


def group_table(title, groups, periods):
    """groups: [(name, dataframe)]; prints clicks, impressions, CTR, position per period."""
    print(f"## {title}\n")
    head = "| Group |" + "".join(f" {p[0]}: clicks | impressions | CTR | position |" for p in periods)
    print(head)
    print("|---|" + "---|---|---|---|" * len(periods))
    for name, g in groups:
        row = f"| {name} |"
        for _, c, i, p in periods:
            cl = g[c].sum()
            im = g[i].sum() if i else 0
            row += f" {cl:,.0f} | {im:,.0f} | {ctr(cl, im) if i else 'n/a'} | {wpos(g, p, i)} |"
        print(row)
    print()


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
    periods = periods_of(q)
    cur_label, cur_c, cur_i, cur_p = periods[0]
    compare = len(periods) > 1

    print("# Search Console summary\n")
    print("Periods: " + (" vs ".join(p[0] for p in periods) if compare else "one period (no comparison)") + "\n")

    if "dates" in t:
        d = t["dates"]
        dper = periods_of(d)
        print("| Period | Clicks in the queries table | Clicks for the whole site | Not shown by Search Console |")
        print("|---|---|---|---|")
        for (lab, c, _, _), (_, dc, _, _) in zip(periods, dper):
            shown, total = q[c].sum(), d[dc].sum()
            print(f"| {lab} | {shown:,.0f} | {total:,.0f} | {total - shown:,.0f} ({pct(total - shown, total)}) |")
        print()

    if args.brand:
        terms = [b.lower() for b in args.brand]
        lower = q[qcol].astype(str).str.lower()
        is_brand = lower.apply(lambda s: any(b in s for b in terms))
        group_table("Brand and non-brand (check 2; rules 1 and 2)",
                    [(f"Brand ({', '.join(args.brand)})", q[is_brand]), ("Non-brand", q[~is_brand])], periods)
        b = q[is_brand].copy()
        bl = lower[is_brand]
        assigned = pd.Series("bare name or other", index=b.index)
        for name, pattern in reversed(BRAND_GROUPS):
            assigned[bl.str.contains(pattern, regex=True)] = name
        groups = [(n, b[assigned == n]) for n in [g[0] for g in BRAND_GROUPS] + ["bare name or other"] if (assigned == n).any()]
        if groups:
            group_table("Brand searches by group (rule 4)", groups, periods)
    else:
        is_brand = pd.Series(False, index=q.index)
        print("No --brand terms given: brand split skipped.\n")

    if "countries" in t and args.markets:
        c = t["countries"]
        ccol = c.columns[0]
        cc = periods_of(c)[0][1]
        markets = [m.strip().lower() for m in args.markets.split(",") if m.strip()]
        in_mkt = c[ccol].astype(str).str.lower().isin(markets)
        c_total = c[cc].sum()
        m_clicks = c.loc[in_mkt, cc].sum()
        found = set(c.loc[in_mkt, ccol].astype(str).str.lower())
        missing = [m for m in markets if m not in found]
        print(f"## Markets (check 3), {cur_label}\n")
        print(f"Clicks from markets they sell in: {m_clicks:,.0f} of {c_total:,.0f} ({pct(m_clicks, c_total)})")
        if missing:
            print(f"No clicks recorded from: {', '.join(missing)} (if that is unexpected, check the spelling against the Countries table)")
        print("\n| Country | Clicks | In their markets |")
        print("|---|---|---|")
        for _, r in c.sort_values(cc, ascending=False).head(10).iterrows():
            print(f"| {r[ccol]} | {r[cc]:,.0f} | {'yes' if str(r[ccol]).lower() in markets else 'no'} |")
        print()

    print(f"## Top 50 queries, {cur_label} (check 1: mark each buyer, maybe or not a buyer)\n")
    extra = f" | Clicks, {periods[1][0]}" if compare else ""
    print(f"| # | Query | Clicks{extra} | Brand |")
    print("|---|---|---|" + ("---|" if compare else "") + "---|")
    top_q = q.assign(_brand=is_brand).sort_values(cur_c, ascending=False).head(50)
    for i, (_, r) in enumerate(top_q.iterrows(), 1):
        prev = f" | {r[periods[1][1]]:,.0f}" if compare else ""
        print(f"| {i} | {r[qcol]} | {r[cur_c]:,.0f}{prev} | {'yes' if r['_brand'] else ''} |")
    print()

    if "pages" in t:
        p = t["pages"]
        pcol = p.columns[0]
        pper = periods_of(p)
        print(f"## Top 10 landing pages, {cur_label} (checks 5 and 6; rules 2 and 6)\n")
        head = "| # | Page |" + "".join(f" {lab}: clicks | CTR | position |" for lab, *_ in pper)
        print(head)
        print("|---|---|" + "---|---|---|" * len(pper))
        for i, (_, r) in enumerate(p.sort_values(pper[0][1], ascending=False).head(10).iterrows(), 1):
            row = f"| {i} | {r[pcol]} |"
            for _, c, im, po in pper:
                row += f" {r[c]:,.0f} | {ctr(r[c], r[im]) if im else 'n/a'} | {f'{r[po]:.1f}' if po else 'n/a'} |"
            print(row)
        print()

    print("Search Console exports show at most 1,000 rows per table.")


if __name__ == "__main__":
    main()

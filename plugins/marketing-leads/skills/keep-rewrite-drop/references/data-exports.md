# Getting the data

Give the person only the steps for the file they are about to export.

## Search Console Pages export, last 12 months

1. Open Search Console and pick the property for the website.
2. Go to **Performance**, then **Search results**.
3. Click the date filter and choose **Last 12 months**. No comparison.
4. Click **Export** at the top right, then **Download CSV** (or **Download Excel**).
5. Upload the file as it is. The CSV download is a zip with one file per table; the script uses the Pages table and, for proposing each page's search, the Queries table.

Notes to share only if they come up:
- Each table holds at most 1,000 rows. On a bigger site, the smallest pages are missing; the optional URL list fills that gap.
- Pages with no impressions at all don't appear in Search Console. The URL list fills that gap too.
- To see the searches for one page, filter the Performance report on that page (**+ New**, **Page**) and read the Queries tab. Only needed for the pages in the test batch.

## CRM leads, last 12 months

A list of the leads created in the last 12 months, with these columns where they exist:

- created date
- the page the lead first landed on (often "first page seen", "landing page", "entrance page" or "original source data")
- the form or page where they converted, if the first page is missing
- source, and current stage

Remove names, emails and phone numbers before uploading. The sort doesn't need them.

## Optional: every URL on the site

The sitemap (usually at /sitemap.xml) copied into a one-column CSV, or the URL column of a crawl export. One URL per row.

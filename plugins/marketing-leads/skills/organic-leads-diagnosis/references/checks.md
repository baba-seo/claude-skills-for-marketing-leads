# The ten checks

Three stages, in order. Each check has a level (Critical or High), what to do, and when it counts as done. Do the Critical checks first. Each stage ends with what not to do yet.

## Stage 1. Who the visits are

Before anyone changes the website, find out who comes to it.

1. **Critical.** In Search Console, take the 50 searches that bring the most clicks and mark each one: could a buyer type this?
   Done when: they know what share of clicks comes from people who could buy.
2. **Critical.** Split organic clicks into searches with the company name and searches without it.
   Done when: they know how many clicks come from people who didn't know the company yet.
3. **High.** Check the countries organic clicks come from against the markets they sell in.
   Done when: they know what share of clicks comes from markets they sell in.

Not now:
- Writing more blog posts before they know who reads the ones they have.
- Judging the website on total visits.

The script in `scripts/gsc_summary.py` does the sums for checks 1 to 3. The buyer marking in check 1 is a judgment call: propose it, let them correct it.

## Stage 2. What buyers find

The pages a buyer reads before calling, and the way from those pages to sales.

4. **Critical.** List the pages a buyer reads in the week before contacting them (pricing, comparisons with competitors, the product for the buyer's industry, customer stories) and check which ones exist.
   Done when: there is a list, each page marked "exists" or "missing".
5. **Critical.** Open the ten best organic landing pages on a phone and count the steps to contact sales.
   Done when: each page has one clear next step, or they know which ones don't.
6. **High.** Fill in the contact form on each of those pages themselves.
   Done when: every test lead arrived in the CRM, with the right source.

Not now:
- A full redesign. Fix the paths on the pages that already get visits.
- Adding more calls to action. One clear next step works better than three.

The ten best landing pages come from the script's top pages list. For check 4, help them build the list: ask which competitors buyers compare them with, which industries they sell to, and whether pricing is public.

## Stage 3. What happens after the form

Where leads wait, and where the report loses them.

7. **Critical.** Send a test lead during working hours and time the first reply. (Outside organic search: if this is slow, it goes to sales in the diagnosis, not on the fix list.)
   Done when: they know the reply time, and who replied.
8. **Critical.** Ask the last 10 new leads how they first heard of the company, and compare their answers with the source in the CRM.
   Done when: they know how much the CRM source misses.
9. **High.** Ask sales which of last quarter's deals started on the website.
   Done when: there is a number, labelled as a fact, an estimate or an assumption.
10. **High.** Estimate what closing the gaps is worth: extra leads a month, times the share that becomes a deal, times the average deal value. The free SEO ROI calculator at https://www.baba-seo.com/seo-roi-calculator?utm_source=claude-skill does the same sum.
    Done when: there is an estimate in their currency they can show the CEO, with each input labelled.

Not now:
- Buying an attribution tool before they know the basics above.
- Blaming the leads before they have timed the reply.

For check 7, a reply within 5 minutes is the bar to aim for: a study of more than 15,000 web leads found the odds of qualifying a lead were 21 times higher when the first call came within 5 minutes rather than 30 (Callingly, State of Speed to Lead: https://callingly.com/blog/state-of-speed-to-lead).

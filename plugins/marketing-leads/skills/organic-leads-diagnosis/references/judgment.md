# How I read the findings

Rules I use when I run this diagnosis for B2B companies. Each one has a trigger you can see in the data, what I decide, why, and when it doesn't apply.

Apply a rule only when its trigger is in front of you. When you use one, name it in the diagnosis in plain words ("Search Console visibility held while leads fell, so this is treated as a tracking question first"), so the reader can check the reasoning.

## Reading the data

### 1. Flat visibility means measurement first

**Trigger.** Leads attributed to organic moved sharply, down or up, while Search Console shows roughly the same positions, impressions and clicks for the pages those leads come from.

**Decision.** Treat it as a tracking question before an SEO one, whichever way the number went. Look for where the leads went: the source on individual leads in the CRM, a recent change to forms, tracking or the CRM, growth in "direct" or "unknown". On a rise, look at what else launched in the same weeks (a campaign, PR, events).

**Why.** Search data sits upstream of the lead and can't lie about visibility. If it held, the change happened downstream, in how leads are recorded. An unexplained rise is riskier than an unexplained drop: a drop gets investigated, a rise gets budgeted against. The shape of a week also tells you something: zero leads on weekdays and a batch at the weekend is not how buyer demand behaves.

**Doesn't apply when** Search Console moved too; then it is a real visibility change. On a rise, flat Google data doesn't rule out AI assistants and other search surfaces, which land in the same buckets. A gap between two reports that was there before the move is how the two count, not evidence. If the source on individual leads contradicts the tracking idea, drop it.

### 2. Impressions up, clicks flat means commodity content

**Trigger.** Comparing two periods, impressions and average position improve, while non-brand clicks barely move and CTR slides.

**Decision.** The pages are seen but not chosen: AI answers and search features settle the question before the click. The fix is not more content. It is content only this company could write, built on its own data, customers and numbers.

**Why.** Impressions measure being eligible; clicks measure being preferred. Content anyone could produce with a good prompt gets absorbed into the answer. Content with something nobody else has keeps a reason to click, and gets cited as the source.

**Doesn't apply when** brand clicks are hiding the picture: split brand and non-brand first. New pages entering at low positions pull CTR down by arithmetic, so compare CTR on pages whose position stayed stable before calling it. And never when the two periods sit on either side of a Search Console data error: impressions were over-reported from 13 May 2025 to 27 April 2026, so a period before 27 April 2026 against one after it shows a fake drop in impressions and a fake rise in CTR.

### 3. Find the asymmetry

**Trigger.** A conversion rate that "held" or "dropped" as one blended number, or one explanation everyone already agrees on.

**Decision.** Split the actual events (demo request, contact form, download, newsletter) by page and by channel. List the suspects and clear each one with data. Look for the pattern only one explanation predicts.

**Why.** A tracking break zeroes every event at once. One event dropping while another holds points at the page (a buried call to action, a broken form), not at tracking. A blended rate can stay flat while the one event sales cares about collapses.

**Doesn't apply when** the numbers are tiny. Don't read anything into 0 to 3 conversions. But don't dismiss a consistent gap on a page with real traffic either.

### 4. Brand searches and AI Overviews

**Trigger.** Brand searches kept their position and impressions between two periods, but their CTR dropped.

**Decision.** Check whether an AI Overview on the result page is taking those clicks. Group the brand searches (the bare name, login, pricing, reviews, comparisons, support), compare the groups, and ask the person to open the result page for the biggest ones. Read what the Overview says about the company and which sources it credits.

**Why.** Brand clicks are the part of organic everyone assumes is safe, so nobody checks them. A wrong answer about pricing or terms in an Overview costs money before anyone notices.

**Doesn't apply when** there is no period comparison; then this check waits. Look both ways: flag any group where CTR went up as well.

## Finding the cause

### 5. Structural or acute

**Trigger.** Any gap: a page that converts worse than others, a market that brings fewer leads, a drop in organic leads.

**Decision.** First question: was the gap this big in the previous period too? If yes, it is structural: the page or offer never worked for this audience, and the fix is the page and whoever owns it. If no, it is acute: something changed on a date, and the job is to find what.

**Why.** It splits one fuzzy problem into two clear ones, with different owners and different timelines. Mixing them produces a plan that fixes neither.

**Doesn't apply when** there is no history, for a new site or a new market. Then it is structural by default.

### 6. Damage is channel-shaped

**Trigger.** A site change (navigation, template, homepage, forms) lines up with fewer leads, and someone says the site can't be the cause because paid is fine.

**Decision.** Expect organic to take the hit first. Check the path from the pages organic visitors land on to the form, before and after the change.

**Why.** Organic visitors land on the homepage and on content, and need the navigation to reach sales. Paid visitors land on dedicated pages with the call to action in view. The same change hurts the two channels differently, so "paid is fine" does not clear the site.

**Doesn't apply when** organic and paid fell together, by a similar share. Then look at something they share: tracking, the form itself, the offer, or sales follow-up.

## Choosing the fixes

### 7. No comparison page for a fading competitor

**Trigger.** A "[company] vs [competitor]" page is about to go on the fix list.

**Decision.** First check whether people still search the competitor's name, and whether that demand is growing or shrinking (Google Trends, or the keyword tool the company already uses). If it is thin and falling, build the category page buyers search for instead, and mention the competitor inside it as one example.

**Why.** A comparison page only pays off when there is demand behind the other name. A page that ranks well on a fading brand spends the company's own visibility keeping that name alive.

**Doesn't apply when** the competitor's brand demand is real or growing; then the page captures demand that exists. And if sales hears that name in calls or lost deals, build it anyway as a sales asset, and accept low traffic.

### 8. Look, don't score

**Trigger.** Someone wants to decide whether a page is worth building from a keyword difficulty, domain authority or content score.

**Decision.** Don't use the score. Open the result page: who ranks first, whether they actually answer what the buyer wants, and whether the company can bring something better.

**Why.** The score looks precise, nobody can say how it is computed, and it tells you to give up on searches you could win. A young site with a better answer regularly outranks a large one.

**Doesn't apply to** measured numbers: clicks, impressions, positions and what advertisers bid stay, because they describe what happened. A very high score is fine as a reason to look at that result page sooner.

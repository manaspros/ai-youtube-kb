# HBO Accidentally Built a Market-Beating Index Fund

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `wbRaBUhkVhc` · [watch](https://youtu.be/wbRaBUhkVhc) · **date:** 2026-10-26 · **length:** 6:27 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, HBO, Yu+Co, Theranos, Coinbase, Reddit, Apple, Nvidia, Uber, Airbnb, Instacart, Waymo
- **topics:** data-engineering · **tags:** backtesting, index-funds, simulation, market-cap-weighting, equal-weighting, rebalancing, finance, off-topic

> Better Stack backtests seven ways to invest in the company logos from the Silicon Valley title sequence; only a market-cap-weighted, rebalanced "ETF" version beats both the S&P 500 and Nasdaq-100, and the speaker says it is mostly a big-tech fund. No AI content.

## Summary
The video simulates investing in every company logo that appeared in the Silicon Valley title sequence across six seasons. The creator tagged logos frame by frame, reduced 65 logos to about 41 investable companies, and tested several rule sets. The first version (equal $1,000 per logo, bought the day after each premiere) beat the S&P 500 by a small margin through 2019 but trailed the Nasdaq-100 later. A version limited to what a regular person could actually buy (public stocks only, startups bought at their IPO day) roughly matched the S&P 500 and missed the Nasdaq-100. The only version that beat both indexes was a market-cap-weighted fund rebalanced at each premiere, which turned $10,000 in 2014 into about $114,000. The speaker concedes that by the last rebalance Apple, Microsoft and Alphabet made up 58% of it, so the result is largely a big-tech fund, and the Nvidia example shows what the equal-weight and early-stage variants missed.

## Key ideas
- **Method: every logo in every version of the title sequence was tagged frame by frame, cutting 65 logos to about 41 investable companies, since YouTube is Google and Instagram is Facebook.** — Dataset built by hand from video frames. Some logos are hard to spot (Instacart carrots, Waymo cars). A secret season 1 cut shows an Adobe logo that is absent from the copies used. ([0:00](https://youtu.be/wbRaBUhkVhc?t=0))
- **Version 1 (equal $1,000 per company, bought the day after each premiere, never sold) beat the S&P 500 through the 2019 finale.** — $41,000 grew to $69,448 (+69%) by the December 2019 finale, versus +58% for the S&P 500 over the same period. The speaker notes this version is not buyable in practice, since nobody could buy Reddit at $6.26 because of its TV logo. ([0:00](https://youtu.be/wbRaBUhkVhc?t=0))
- **Version 1 later lagged the Nasdaq-100, and its gains were concentrated in two names.** — The fund peaked at $223,964 on 19 Sep 2025, with Coinbase (about $41.5k) and Reddit (about $42.2k) making up most of it. Today it is $181,583 (4.4x), versus 4.2x for the S&P 500 and 6.9x for the Nasdaq-100. ([1:21](https://youtu.be/wbRaBUhkVhc?t=81))
- **A realistic version, limited to what a regular investor could buy, roughly matched the S&P 500 and missed the Nasdaq-100.** — Public companies are bought the day after the premiere. Startups get their $1,000 only on their first day of public trading (Uber 2019, Airbnb 2020, Coinbase 2021, Reddit 2024). Private companies that never list, such as Theranos, are never bought. The fund holds about 32 companies, $32,000 in total, worth about $126,000 today, versus about $124,000 for the S&P 500 and about $200,000 for the Nasdaq-100. ([2:40](https://youtu.be/wbRaBUhkVhc?t=160))
- **Weighting matters more than selection: a market-cap-weighted, rebalanced ETF-style version was the only one to beat both the S&P 500 and the Nasdaq-100.** — $10,000 invested in April 2014 is worth $113,987 today (over 11x), versus 5.1x for the S&P 500 and 9.1x for the Nasdaq-100. Each premiere sells companies whose logos left the credits and buys new listed ones, and tracks companies that list later (such as Reddit). Apple got about 30% of the fund at the start, with Google about 24%. ([3:52](https://youtu.be/wbRaBUhkVhc?t=232))
- **The speaker's own caveat: the winning fund is essentially a big-tech fund, and the other variants lost to it.** — By the last rebalance Apple, Microsoft and Alphabet made up 58% of the fund. Variants: equal-weight 6.4x, a VC-only fund of startups 3.6x, season 1 companies held untouched 5.4x, and a fan who sold everything after the finale did slightly worse than holding. ([5:13](https://youtu.be/wbRaBUhkVhc?t=313))
- **Market-cap context: the on-screen companies went from about $1.6T when season 1 aired to $6.4T at the finale and $21.1T today, and Nvidia was the missed winner.** — Nvidia was worth about $10B when the pilot aired and is now about $5T, so $1,000 in it at the pilot would be about $490,000 today. The speaker presents this as the biggest missed opportunity, not a strategy. ([5:13](https://youtu.be/wbRaBUhkVhc?t=313))

## Techniques
- **Event-driven dataset from frame-by-frame tagging** — Step through every version of a recurring visual (here, title-sequence frames) and log each entity on screen, then de-duplicate by parent company (YouTube into Google, Instagram into Facebook) to get the investable universe. *When:* When the input is visual or semi-structured and you need a clean, timestamped list of entities to backtest on, with no API for it.
- **Compare the same universe under several rule sets** — Hold the entity set fixed and vary the rules: equal dollars per entity versus market-cap weights; buy at first appearance versus buy at first public listing; rebalance at each event versus hold; limit to investable entities. Measure each against the same benchmarks (S&P 500, Nasdaq-100) over the same dates. *When:* When the question is whether a selection idea holds up, and whether weighting, access constraints or rebalancing account for the result. The speaker's point is that a rule set that a retail investor can follow changes the answer.

## Numbers
- 65 logos reduced to about 41 investable companies; $41,000 invested in version 1 ([0:00](https://youtu.be/wbRaBUhkVhc?t=0))
- Version 1 reached $69,448 by the Dec 2019 finale (+69%) versus +58% for the S&P 500 ([0:00](https://youtu.be/wbRaBUhkVhc?t=0))
- Coinbase listed at $8.25 a share when it got its tower in season 5; first-day close about $328 in April 2021; the fund rose 26% that day, its biggest day ([1:21](https://youtu.be/wbRaBUhkVhc?t=81))
- Version 1 peak $223,964 on 19 Sep 2025; today $181,583 (4.4x) versus S&P 4.2x and Nasdaq-100 6.9x ([1:21](https://youtu.be/wbRaBUhkVhc?t=81))
- Realistic version: 32 companies, $32,000 invested, about $126,000 today versus about $124,000 for the S&P 500 and about $200,000 for the Nasdaq-100 ([2:40](https://youtu.be/wbRaBUhkVhc?t=160))
- Market-cap ETF version: $10,000 in April 2014 is $113,987 today (over 11x) versus 5.1x for the S&P 500 and 9.1x for the Nasdaq-100; Apple was about 30% of the fund in 2014 (market cap $473B), Google about 24% ([3:52](https://youtu.be/wbRaBUhkVhc?t=232))
- Apple turned $1,000 into $21,346 in version 1 ([3:52](https://youtu.be/wbRaBUhkVhc?t=232))
- Apple, Microsoft and Alphabet were 58% of the ETF version at its last rebalance ([5:13](https://youtu.be/wbRaBUhkVhc?t=313))
- Variants: equal-weight 6.4x; VC-only 3.6x; season 1 held untouched 5.4x ([5:13](https://youtu.be/wbRaBUhkVhc?t=313))
- Combined market cap of on-screen companies: $1.6T at season 1, $6.4T at the finale, $21.1T today; Nvidia $10B at the pilot, $5T today ($1,000 becomes about $490,000) ([5:13](https://youtu.be/wbRaBUhkVhc?t=313))

## Hot takes
- Off-topic for this channel's AI engineering scope: the video is a finance backtest with no AI, LLM or agent content.
- The 'Market-Beating' title is clickbait. Only the market-cap-weighted version beats both indexes, and the speaker concedes it is mostly a big-tech fund (58% in three names).
- The video concedes that the most realistic rule set (version 2) only roughly matches the S&P 500 and misses the Nasdaq-100, which undercuts the title.
- Hindsight: the universe was chosen from the show after the outcomes were known, which the speaker does not discuss beyond noting 'nobody could actually buy' the early versions.

## Tools mentioned
Nasdaq-100 (benchmark), S&P 500 (benchmark)

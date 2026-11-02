# DeepSeek's $1 Billion Is a Price Hike, Not Growth

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `dXieY9PwvJg` · [watch](https://youtu.be/dXieY9PwvJg) · **date:** 2026-10-02 · **length:** 13:00 · **format:** news · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Kai Explains host (name not stated in transcript) · **orgs:** DeepSeek, OpenRouter, OpenCode, Huawei, Bloomberg, The Information, Nebius, Together, Parasail, CoreWeave
- **topics:** token-cost-efficiency, models-research, infra-cost-scaling · **tags:** deepseek, pricing, prompt-caching, cache-hit-ratio, openrouter, open-weights, mit-license, peak-pricing, revenue-analysis, compute-scarcity, ascend, provider-routing

> Breaks down DeepSeek's reported $1B annualized revenue: most of the jump came from an August price hike, not volume growth, and cache-hit rates drive real agent bills.

## Summary
The host argues that the viral claim of DeepSeek doubling to a $1B annualized revenue run rate mixes two things: real volume growth on OpenRouter and a large, quiet price increase. The $1B figure comes from founder investor talks reported secondhand, not from a filing or DeepSeek's own publication. The new pricing added peak/off-peak tiers, raised output tokens 2.25x off-peak and 4.5x at peak, and raised cached input up to 12x on the Pro model, which hits coding agents hardest because they resend the same context on almost every call. Working through the division (revenue roughly 2x, price 2x to 4x), the host concludes paid volume on DeepSeek's own API was flat or down. He ties the hike to compute scarcity (over 70% of GPUs go to training, and promised Ascend chips had not arrived), and notes that the MIT-licensed weights let other hosts undercut DeepSeek's API prices. The advice is to measure your own cache-hit ratio, pin a specific provider in your router, and treat revenue-doubled headlines with suspicion when prices changed mid-window. The video is analysis of a news story rather than a benchmark, and it cites specific figures from third-party reporting that viewers cannot verify from the video alone.

## Key ideas
- **The $1B annualized revenue number is a founder's figure given to investors, relayed secondhand; DeepSeek published no official statement.** — Attributed to founder Liang Wenfeng in fundraising talks, reported by The Information and screenshotted online. Not a public filing or audited report. ([1:12](https://youtu.be/dXieY9PwvJg?t=72))
- **Revenue growth was confounded by a price change, so price times volume must be separated before reading the headline.** — Usage grew (OpenRouter share of DeepSeek models rose from about 5% in February to nearly 20% by June), but the August price hike moved revenue as well. Revenue equals price times volume. ([2:09](https://youtu.be/dXieY9PwvJg?t=129))
- **The August pricing change added peak/off-peak tiers and sharply raised output and cached-input prices.** — Peak is 9am-12pm and 2pm-6pm Beijing time on weekdays. Off-peak is half the peak rate. Output tokens went up 2.25x off-peak and 4.5x at peak. Cached input rose up to 12x on V4 Pro. The host gives Aug 13 and Aug 16 as the change date at different points, so the exact date is unclear. ([3:19](https://youtu.be/dXieY9PwvJg?t=199))
- **Coding agents are the most exposed to cache-price increases because they resend the same context on nearly every call.** — The host cites OpenCode's author saying his users spent about $130k/day on DeepSeek, with a 96.56% cache-hit rate. This is one anecdotal source. ([4:40](https://youtu.be/dXieY9PwvJg?t=280))
- **Division of the numbers suggests paid volume on DeepSeek's own API was flat or down, not growing.** — On a March 2025 traffic snapshot (608B input, 342B cache hits, 168B output tokens), the host prices the same day under the new sheet at about 2.4x the old bill. Revenue doubling with price 2x to 4x implies volume did not grow. ([5:54](https://youtu.be/dXieY9PwvJg?t=354))
- **MIT-licensed weights let the same model move to cheaper third-party hosts, so DeepSeek's API loses those customers rather than the model losing users.** — By July, V4 Flash was listed by 31 providers on OpenRouter, some still at the old DeepSeek prices or lower. The host contrasts price-driven revenue growth with volume-driven growth. ([7:04](https://youtu.be/dXieY9PwvJg?t=424))
- **The price hike looks like capacity management rather than cross-subsidy repair.** — DeepSeek's reported API gross margin at the old prices was 82.9% (Jan-Jul). The host says over 70% of GPU capacity goes to training and under 30% to serving, so pricing works like surge pricing to decide who gets capacity. ([8:31](https://youtu.be/dXieY9PwvJg?t=511))
- **Earlier promised price drops depended on Huawei Ascend chips shipping in volume, and that did not happen in time.** — DeepSeek's Chinese docs said prices would fall once Ascend 950 Supernodes shipped in H2 2025. Bloomberg reportedly says at least 160,000 Ascend 950DT chips are planned for inference eventually. ([8:31](https://youtu.be/dXieY9PwvJg?t=511))
- **The price sheet moves fast, so run-rate projections built from one window break quickly.** — On Sept 10, V4.1 Flash shipped with cut prices and cached input went back near pre-August levels. A Sept 14 attempt to retire the Pro model was reversed the next day. ([9:47](https://youtu.be/dXieY9PwvJg?t=587))

## Techniques
- **Decompose spend into price x volume before trusting a revenue or cost trend** — Pull the price sheet for each date range and compare price-per-token against token counts from the same window. Check whether a revenue increase came from volume (more tokens) or price (same tokens, higher rate). Re-price a fixed historical traffic snapshot under old and new sheets to isolate price effects. *When:* When a provider changes pricing mid-measurement, or when a vendor or competitor reports revenue or usage growth.
- **Measure your cache-hit (cached input) ratio per provider and per model** — Track cache-read input tokens separately from fresh input tokens for each request. Compute the cash-hit ratio per provider and model. The host says a 5-point change in cache ratio can nearly double the input bill at the same sticker price, so compare providers on effective cost per token at your real ratio, not on list price. *When:* For heavy agent or coding workloads that resend the same repo, system prompt, or context on every call.
- **Pin a specific provider in the router config, not just a model name** — In your router or gateway config, bind the model to a named provider host rather than letting the router pick by model name, so the bill does not change when another host changes its prices. Re-check the pinned host's prices on a schedule. *When:* When the same open-weights model is served by several hosts with different prices and cache policies.
- **Use time-of-day or peak/off-peak tiers to shift batch or background work** — If a provider prices by time window, route non-urgent or batch calls to off-peak hours. The host notes the off-peak rate was half the peak rate under the new DeepSeek schedule (Beijing time). *When:* For background agent runs, evals, or batch jobs that do not need an immediate response.

## Numbers
- Annualized revenue reported to have crossed $1B; Jan-Jul booked about 475M yuan (~$70M) over seven months ([1:12-2:09](https://youtu.be/dXieY9PwvJg?t=0))
- OpenRouter share of DeepSeek models rose from ~5% (Feb) to ~20% (June), and ~23% by mid-September ([2:09 and 5:54](https://youtu.be/dXieY9PwvJg?t=0))
- Output token price up 2.25x off-peak and 4.5x at peak; cached input up 12x on Pro ([3:19](https://youtu.be/dXieY9PwvJg?t=199))
- Peak hours 9am-12pm and 2pm-6pm Beijing time; off-peak priced at half the peak rate ([3:19](https://youtu.be/dXieY9PwvJg?t=199))
- One OpenCode user base reportedly spent $130,000/day (~$47M annualized) on DeepSeek at a 96.56% cache-hit rate ([4:40](https://youtu.be/dXieY9PwvJg?t=280))
- March 2025 snapshot: 608B input tokens (342B cache hits), 168B output; same day priced ~2.4x higher on new sheet ([5:54](https://youtu.be/dXieY9PwvJg?t=354))
- V4 Flash listed by 31 providers on OpenRouter by July ([7:04](https://youtu.be/dXieY9PwvJg?t=424))
- DeepSeek API gross margin at old prices (Jan-Jul): 82.9% ([7:04](https://youtu.be/dXieY9PwvJg?t=424))
- More than 70% of GPU capacity to training, less than 30% to serving API requests (per Liang via investor talks) ([8:31](https://youtu.be/dXieY9PwvJg?t=511))
- Bloomberg reportedly: at least 160,000 Ascend 950DT chips planned for inference eventually ([9:47](https://youtu.be/dXieY9PwvJg?t=587))
- A 5-point cash-ratio change can nearly double the input bill at the same sticker price (one source's figure) ([10:54](https://youtu.be/dXieY9PwvJg?t=654))

## Hot takes
- The $1B DeepSeek run-rate is a fundraising figure framed as a breakout story; the price change explains most of the second doubling.
- Revenue doubling while prices rise 2x to 4x implies flat or falling paid volume on DeepSeek's own API.
- For heavy agent users, DeepSeek direct may still be the best option because of its cache-hit economics, even though list prices rose.
- Being suspicious of revenue-doubled headlines when pricing changed mid-measurement is the core lesson.
- Unverified: the host's cited figures (run rates, the 82.9% margin, the Bloomberg chip plan, the $130k/day OpenCode spend) come from secondhand reporting and were not checked against primary sources in the video.

## Tools mentioned
DeepSeek V4 Flash, DeepSeek V4 Pro, DeepSeek V4.1 Flash, DeepSeek API, OpenRouter, OpenCode, Huawei Ascend 950 Supernodes, Ascend 950DT, MIT-licensed DeepSeek weights, Nebius, Together, Parasail, CoreWeave, GPT-6 Luna (as named in the video)

## Relevance to our work
- **agentos** (2/3): L1 Govrix Scout has budgets and strategy routing. Budget estimates that ignore cache-hit pricing and peak/off-peak tiers will misstate spend. → *Make budget cost estimates cache-aware (separate cached and uncached input prices) and allow time-window price tiers in the routing strategy config.*
- **prosharness** (1/3): Long Claude Code runs resend the same context on many calls, so cache-hit ratio drives their cost, but the video is about DeepSeek pricing, not Claude pricing. → *Log cache-read vs fresh input tokens per checkpointed run so cost per plan or loop is measurable.*

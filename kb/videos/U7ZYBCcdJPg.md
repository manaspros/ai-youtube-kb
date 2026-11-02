# Tokens Are the Cheap Part — Steve Jamison, Jellyfish

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `U7ZYBCcdJPg` · [watch](https://youtu.be/U7ZYBCcdJPg) · **date:** 2026-10-14 · **length:** 17:32 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Steve Jamison · **orgs:** Jellyfish
- **topics:** governance-compliance, token-cost-efficiency, enterprise-adoption, coding-agents · **tags:** cost-per-pr, token-spend, engineering-productivity, pr-throughput, budgeting, telemetry, agent-skills, reverts, diminishing-returns

> Steve Jamison (Jellyfish) argues AI tokens are a small share of PR cost; tracking total intelligence cost per merged PR, with revert rates as a counterweight, beats watching the token bill alone.

## Summary
The speaker, Steve Jamison of Jellyfish, uses telemetry from engineering workflow and AI usage data to argue that AI spend is a small part of what it costs to ship a merged PR. He reports AI spend up about 60x year over year while merged PRs per engineer rose about 43%. He proposes a blended metric, "intelligence cost per PR," which adds engineer salary and AI spend and divides by merged PRs. On that metric AI is about 2.5% of cost, and cost per merged PR fell 26% over the year. Companies that spent the most on tokens saw larger throughput gains and bigger drops in cost per PR, with diminishing returns but no sign of stopping returns. A developer-level comparison of heavy agent-skill weeks against the same developers' lighter weeks showed roughly 2x tokens, 27% more merged PRs, and about 18% lower cost per PR. Reverts did not rise, and PRs are getting larger rather than smaller. The speaker's advice is to track AI spend, PR throughput, cost per PR and revert/quality metrics together each month, and not to make AI spend per PR the main driver. The data is vendor telemetry and the findings are correlational, so the causal claims are not tested.

## Key ideas
- **Judge AI spend against a blended unit cost, not the token bill alone** — Add engineer salary and AI spend together and divide by merged PRs. Salary is about 97.5% of that cost and AI about 2.5%. Leaving salary out makes the AI cost look far more important than it is. ([2:50](https://youtu.be/U7ZYBCcdJPg?t=170))
- **Cost per merged PR fell while AI bills rose** — Cost per merged PR dropped 26% over the year, even though AI costs rose about 60x. Review time and some quality gates are counted, because the metric uses merged PRs, not PRs opened. The drop appeared in 83% of the companies studied. ([3:58](https://youtu.be/U7ZYBCcdJPg?t=238))
- **Heavy token spenders got the biggest throughput and cost gains** — Companies were split into token-spend quintiles. The top fifth had about 67% PR throughput growth against about 40% for the rest, and a 32% drop in cost per PR against about 25%. The speaker reads this as spend driving efficiency, though the link is correlational. ([6:12](https://youtu.be/U7ZYBCcdJPg?t=372))
- **Returns diminish with more tokens but do not reach zero** — The first increase in tokens gives a steep drop in cost per PR, and the curve then flattens. The top 10% of company-months used about 8x the median tokens and had about 25% lower cost per PR. The speaker says tokens will eventually stop being the cheap part, but most companies are not near that point. ([7:52](https://youtu.be/U7ZYBCcdJPg?t=472))
- **The same effect shows up within individual developers** — Comparing each developer's heavy agent-skill weeks with their own lighter weeks, the heavy weeks used about twice the tokens, merged 27% more PRs, and had about 18% lower cost per PR once salary and tokens were counted together. ([9:01](https://youtu.be/U7ZYBCcdJPg?t=541))
- **Check quality with revert rate beside throughput** — Reverts, meaning merged PRs that undo earlier PRs, dropped slightly for every group. The change is within the noise, so the data does not prove quality improved, but it shows no sign that faster PRs cause rampant reverts. ([10:12](https://youtu.be/U7ZYBCcdJPg?t=612))
- **PRs are growing, not shrinking** — The throughput gain does not come from smaller PRs. AI is increasing the lines of code per PR, which the speaker ties to verbose inline comments, irrelevant tests, and developers bundling more work into one PR. This makes review harder. ([10:46](https://youtu.be/U7ZYBCcdJPg?t=646))
- **Track three paired lines each month and do not optimise AI spend per PR directly** — Plot AI bill, PR throughput, and cost per PR together, with reverts and quality next to them. The speaker warns that AI spend per PR should not be the main target. Watch for runaway jobs, but use the spend to decide on router, token-limit, or enablement investments. ([15:18](https://youtu.be/U7ZYBCcdJPg?t=918))

## Techniques
- **Blended cost per merged PR** — Compute (engineer salary cost + AI spend) divided by merged PRs for each month or team. Track the trend, not a single snapshot. *When:* Budget reviews or board conversations, when the question is whether AI spend is paying off rather than how big it is.
- **Token-spend quintile cohorts** — Rank teams or companies by tokens per developer per month, split them into fifths, and compare throughput and cost per PR across the groups over time. *When:* Testing whether heavier AI use associates with better delivery outcomes, and where diminishing returns start.
- **Within-developer baseline comparison** — Compare each developer's heavy-usage weeks against their own lighter weeks, not against other developers, so individual differences are controlled. *When:* Evaluating a specific practice such as adding agent skills, where you want to see the effect on the same person.
- **Counterweight metrics beside throughput** — Put revert rate and PR size (lines per PR) next to merged PRs and cost per PR, so a throughput gain that hurts quality shows up. *When:* Whenever a throughput or cost metric is reported, to catch AI slop that inflates merge counts.

## Numbers
- AI costs are up about 60x compared with the same period last year ([0:06](https://youtu.be/U7ZYBCcdJPg?t=6))
- Merged PRs per engineer are up 43% year over year ([0:37](https://youtu.be/U7ZYBCcdJPg?t=37))
- AI is about 2.5% of the cost to produce a merged PR, and salary is about 97.5% (August 2026 data) ([3:23](https://youtu.be/U7ZYBCcdJPg?t=203))
- Dollar cost per merged PR fell 26% over the last year ([3:58](https://youtu.be/U7ZYBCcdJPg?t=238))
- 83% of the companies studied showed a drop in cost per PR ([4:32](https://youtu.be/U7ZYBCcdJPg?t=272))
- Lightest token-spend fifth: about 0.3% of PR cost is AI, roughly 60 million tokens per developer per month ([5:06](https://youtu.be/U7ZYBCcdJPg?t=306))
- Heaviest token-spend fifth: about 8.5% of PR cost is AI, roughly 2.5 billion tokens per developer per month, about two orders of magnitude more ([5:06](https://youtu.be/U7ZYBCcdJPg?t=306))
- Bottom four fifths of spenders saw about 40% PR throughput gains; heaviest fifth saw 67% ([6:12](https://youtu.be/U7ZYBCcdJPg?t=372))
- Heaviest fifth saw a 32% drop in cost per PR; the other four groups saw about 25% ([6:44](https://youtu.be/U7ZYBCcdJPg?t=404))
- Top 10% of company-months used about 8x the tokens of the median and had about 25% lower cost per PR ([7:52](https://youtu.be/U7ZYBCcdJPg?t=472))
- Developer-level heavy agent-skill weeks vs own baseline weeks: about 2x tokens, 27% more merged PRs, about 18% lower cost per PR ([9:01](https://youtu.be/U7ZYBCcdJPg?t=541))
- Revert rates fell slightly in every group, but the change is within the noise of the data ([10:12](https://youtu.be/U7ZYBCcdJPg?t=612))
- The speaker says spend is up '60%' once at 12:29, but elsewhere says 60x; the 60x figure is the one stated consistently ([12:29](https://youtu.be/U7ZYBCcdJPg?t=749))

## Hot takes
- For most companies, the token bill is not the number to manage. Cost per merged PR, with salary included, is the number that tells you whether AI is working.
- Heavier AI spend is associated with bigger efficiency gains, and the speaker recommends not capping spend simply to save money.
- AI-driven PRs are getting larger, not smaller, which runs against the common idea that AI makes work more granular.

## Relevance to our work
- **agentos** (2/3): SkillForge has an open question about what signal counts as a successful skill and how to score skill-worthiness. This talk offers cost per merged PR and revert rate as outcome measures, and a before/after comparison within the same developer. → *Prototype a SkillForge success signal: compare merged PRs, cost per PR, and revert rate for runs that used a skill against the same user's runs without it.*
- **agentos** (1/3): AgentOS has budgets and a Prometheus/Grafana stack. A unit-cost view (spend per merged outcome) would sit alongside the budget controls, but the talk gives no infrastructure detail. → *Consider adding a spend-per-outcome panel to the L4 observability dashboards next to the budget counters.*
- **prosharness** (1/3): ProsHarness runs Claude Code sessions and could record token spend per run. The talk suggests testing whether heavier runs pay off in merged output and reverts, but the link is a metric, not a design change. → *Log tokens and outcome (merged PR or accepted change) per ProsHarness run so the ratio can be checked later.*
- **general** (1/3): Useful as a framing for budget discussions with a team lead: report AI spend next to cost per merged PR and revert rate, not spend alone. → *Use the three-line monthly view (AI bill, PR throughput, cost per PR, with reverts) in the next team budget conversation.*

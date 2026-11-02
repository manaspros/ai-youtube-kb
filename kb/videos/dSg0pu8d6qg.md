# From Tokenmaxxing to Trusted Throughput — Mingsheng Hong, Ironclad

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `dSg0pu8d6qg` · [watch](https://youtu.be/dSg0pu8d6qg) · **date:** 2026-09-18 · **length:** 23:04 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Mingsheng Hong · **orgs:** Ironclad
- **topics:** token-cost-efficiency, governance-compliance, pr-code-review · **tags:** token-spend, cost-roi, trusted-throughput, usage-dashboards, anomaly-alerts, pr-complexity-scoring, ai-code-review, ci-flakiness, prompt-caching, context-pruning, agent-loop-limits, build-vs-buy, developer-experience, legal-tech

> Ironclad's VP of AI Engineering on controlling AI token spend: measure cost against value, treat usage dashboards as smoke detectors, and fix the review and CI bottlenecks that code generation creates.

## Summary
Mingsheng Hong, VP of Engineering focused on AI at Ironclad (a legal contracting AI company), argues that teams past the adoption phase should manage AI token spend as an ROI problem, not a cost-cutting one. He proposes a metric called "trusted throughput": merged code that internal reviewers, leadership and customers all trust. Per-team and per-person usage dashboards should work as smoke detectors for adoption gaps and sudden spikes, not as leaderboards, the same way lines of code is a poor productivity target. He describes how Ironclad's merged-PR count evolved into a complexity-weighted count, with an LLM assigning T-shirt sizes to PRs. Because AI makes PR creation abundant, the bottleneck moves to code review and CI; he recommends AI as a first-pass reviewer, investing in flaky-test removal and CI speed, and tracking ready-to-submit time and retry counts. The framework has three parts: guardrails (budgets, quotas, anomaly alerts), regular human review feeding a learning loop, and shared best practices such as step limits on agent loops, prompt-cache-friendly prompt ordering, context pruning, and an internal prompt playbook. The talk is conceptual and short on hard numbers.

## Key ideas
- **Usage dashboards should be smoke detectors, not leaderboards** — Per-team and per-person token and cost dashboards are useful for spotting adoption gaps and surprise bursts. Ranking people by usage creates an incentive to maximize tokens itself, so usage should be compared with team context. ([0:50](https://youtu.be/dSg0pu8d6qg?t=50))
- **Measure value before cutting cost** — Cutting spend once you can see it is premature. The goal is better ROI (value per token), not austerity. Cost and value must both be measured first. ([12:00](https://youtu.be/dSg0pu8d6qg?t=720))
- **Trusted throughput as the ROI proxy** — Count only output that is trusted by internal engineers, leadership and customers. It rests on three buckets: objective checks (tests, security, canary rollouts), subjective human review (quality, architecture fit), and customer signals (rollbacks, tickets). ([5:28](https://youtu.be/dSg0pu8d6qg?t=328))
- **Output metrics move from PR count to weighted merged PRs** — Open PR count was replaced by merged PR count, which was then weighted by a complexity score. A 10-line concurrency fix can outweigh a 1,000-line boilerplate PR. The speaker presents the scoring as still being refined. ([10:37](https://youtu.be/dSg0pu8d6qg?t=637))
- **AI code generation moves the bottleneck to review and CI** — When code is abundant, the constraint shifts to human review, merging and CI. Making large PRs to avoid slow CI is an anti-pattern because it spreads reviewer attention thin. ([14:22](https://youtu.be/dSg0pu8d6qg?t=862))
- **AI as the first line of review, humans as final judges** — AI review catches style issues and missing tests so authors fix them before a human reviewer is assigned. Humans keep judgment on architecture, security design and final accountability. ([14:22](https://youtu.be/dSg0pu8d6qg?t=862))
- **Guardrails, learning loop and playbooks as the framework** — The framework has three parts: budgets, quotas and anomaly alerts; a review loop that feeds institutional knowledge; and shared best practices. Shared practices include step limits on agent loops, prompt-cache-friendly ordering and context pruning. ([18:38](https://youtu.be/dSg0pu8d6qg?t=1118))

## Techniques
- **Cross-tool cost aggregation** — Use AI to build small pipelines that pull usage data from each vendor's dashboard (Claude Code, Codex, etc.). Join the data and break cost down by team and individual. *When:* When engineers use several coding tools, so no single vendor dashboard shows the full picture.
- **Usage as an anomaly signal** — Review dashboards to find teams with no adoption, or sudden bursts. Then check whether each burst is legitimate and compare each team with its own context, such as platform work versus UI work. *When:* After the initial adoption push, when leaders need to find problems without creating a leaderboard.
- **LLM T-shirt sizing of merged PRs** — Send each merged PR to one or two LLMs with a fixed prompt that asks for a T-shirt size. Use the size as a weight when counting merged PRs. *When:* When raw PR count or lines of code are misleading measures of value. The speaker says there is no standard definition, so treat the result as a rough proxy.
- **Three-bucket trusted-throughput check** — Combine objective gates (test coverage, security checks, canary), human review of quality and architecture, and post-release customer signals (rollbacks, tickets). *When:* To define what counts as valuable output, rather than volume.
- **AI-first review gate** — Require the author to pass the AI review (style, test coverage) before the PR is routed to a human reviewer. *When:* When review is the bottleneck and human reviewers should spend attention on judgment calls.
- **Bounded agent fix loops** — When an agent generates a PR, loop it through tests and auto-fix, but cap the number of loop steps so token use cannot run away. *When:* For any agent that retries or self-corrects, to bound token spend.
- **Prompt-cache-friendly prompt layout** — Put the fixed system prompt at the top and the varying content at the bottom, so the shared prefix can be cached by the vendor. *When:* When building prompts or harnesses that reuse a long common prefix.
- **Context pruning and summarizing in long sessions** — Train users to summarize or compact the context during long chat sessions. Coding tools that auto-compact can help, and the speaker says this also improves output quality. *When:* In long agent or chat sessions where the context grows and token use climbs.
- **Buy non-differentiating tools, build a prompt playbook** — Buy generic infrastructure such as the IDE and CI. Build internally the company-specific prompts for tasks like small bug fixes or refactors, and share and refine them across teams. *When:* When deciding between building and buying AI developer tooling.
- **Developer-experience metrics for CI** — Track the time from ready-to-submit to submitted, and how often a PR is retried to get past tests. Invest in removing flaky tests and speeding up CI. *When:* When engineers are spending time babysitting PRs, which is also a token cost when an AI agent does the babysitting.

## Numbers
- Media anecdote: a company spent about $500 million on cloud within a month. This is cited as a story from the media, not Ironclad's data. ([0:50](https://youtu.be/dSg0pu8d6qg?t=50))
- About half of the audience said their teams had passed the initial AI adoption phase. ([3:06](https://youtu.be/dSg0pu8d6qg?t=186))
- Illustrative CI red flag: if a typical CI run takes one hour, a typical PR submission taking two to three hours is a warning sign. This is an example, not reported data. ([17:11](https://youtu.be/dSg0pu8d6qg?t=1031))

## Hot takes
- Lines of code, and open or merged PR counts, are poor productivity targets for AI-era work. Removing code can be better than adding it.
- Usage dashboards must never become leaderboards, because they create an incentive to maximize token spend.
- Splitting PRs into large batches to dodge slow CI is risky and a clear anti-pattern.
- Measuring cost and cutting it right away is premature. Measure value and ROI first.

## Tools mentioned
Claude Code, Codex, Cursor, vendor usage dashboards, LLMs for PR complexity scoring, CI/CD pipeline

## Relevance to our work
- **agentos** (2/3): AgentOS L1 has budgets and an audit log. The talk's point that usage tracking should flag anomalies, not rank people, and its bounded-loop rule, both map onto budget counters. → *Add per-tenant or per-agent token-burst anomaly alerts on the budget counters, and add a max-step cap on any self-correcting agent loop in AgentOS.*
- **prosharness** (2/3): ProsHarness wraps Claude Code in long, checkpointed runs. Loop step limits, prompt-prefix ordering for caching, and context pruning apply directly to its runs. → *Cap the retry or plan-critique loop steps in ProsHarness, and move the stable instructions to the top of its prompts so prefix caching works.*
- **general** (1/3): The bottleneck shift to review and CI is a general lesson for any team that uses agents to write code.

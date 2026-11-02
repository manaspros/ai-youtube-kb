# From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization - May Walter, Hud

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `JJGbw4ggaFs` · [watch](https://youtu.be/JJGbw4ggaFs) · **date:** 2026-08-18 · **length:** 22:46 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** May Walter · **orgs:** HUD
- **topics:** software-factory, observability, context-engineering, coding-agents · **tags:** performance-optimization, production-traces, github-agentic-workflows, clickhouse, roi-scoring, runtime-verification, function-level-context, claude-code, mcp, slack-reports

> May Walter (HUD) shows how HUD runs a weekly agentic workflow on GitHub Actions with Claude Code that mines production traces, scores performance fixes by ROI, verifies them at runtime, and sends a human-readable report to Slack.

## Summary
The speaker, co-founder and CTO of HUD, describes a runtime intelligence layer for coding agents that connects production behavior to function-level code context. HUD built a continuous performance-optimization workflow: a weekly GitHub Actions job runs Claude Code, which pulls traces via MCP from ClickHouse, finds slow endpoints, proposes and tests fixes, and posts a scored report to Slack. The motivating problem is that performance and tech-debt investigation is a black box, so teams never prioritize it. Early failure modes were plausible-but-unverified fixes, complex ClickHouse queries, and lazy fixes such as catching exceptions. What worked was grounding the agent in function-level production context, adding a query language plus skills, verifying each fix against runtime evidence, and scoring by ROI and risk. The output is a short readable gist rather than a batch of PRs, and humans stay as the review gate. The speaker frames this as moving from coding with an agent, which tolerates 80% reliability, to autonomous automation that needs much higher trust.

## Key ideas
- **Performance and tech-debt work stays ignored because the investigation step is a black box.** — Teams know how long a fix takes but not how long finding it takes, so they never look. Automating the weekly investigation turns it into a scored list of opportunities. ([3:44](https://youtu.be/JJGbw4ggaFs?t=224))
- **Plausible-but-unverified fixes are the main early failure.** — The agent suggested fixes that sounded right and could in theory cause the slowdown, but did not work in production. The fix is to ground each suggestion in real production behavior and verify it against runtime data. ([8:06](https://youtu.be/JJGbw4ggaFs?t=486))
- **Give the agent context at the same level it reasons about code.** — Service and endpoint metrics (CPU, p90) do not map onto the function-and-file view agents use. HUD built a function-level map linked to the endpoints, consumers, or cron jobs that trigger it, and captures deep forensic traces only for requests above p99 or a set threshold. ([10:32](https://youtu.be/JJGbw4ggaFs?t=632))
- **Add skills on top of the query layer to reduce variance.** — Raw queries gave inconsistent results across runs. Skills for patterns such as HTTP 500 origin and memory spikes compared to a baseline made the agent's method repeatable. ([12:53](https://youtu.be/JJGbw4ggaFs?t=773))
- **Score by ROI and risk, and send a readable gist instead of many PRs.** — Each flagged item covers hot-path frequency, business criticality, and migration risk. The output is a short human-readable report that explains the problem and the fix, and the reader can ticket it, open a PR, or ignore it. The team started with one item at a time to build the habit. ([15:43](https://youtu.be/JJGbw4ggaFs?t=943))
- **Agentic automation needs much higher trust than interactive use.** — With an agent in an IDE the human can steer around an 80% success rate. An autonomous job has to reach roughly 80-90% trust, so the hardest part was confidence that an item is worth fixing and that the fix is verified at runtime before a human sees it. ([20:33](https://youtu.be/JJGbw4ggaFs?t=1233))

## Techniques
- **Scheduled agentic investigation with runtime verification** — A weekly CI job (GitHub Actions) runs the coding agent with an MCP connection to production traces. The agent finds slow endpoints, proposes a fix, reruns tests, and reports the measured before/after diff. The human reviews only the verified items. *When:* Recurring performance or stability sweeps where the investigation is costly and hard to prioritize.
- **Function-level production context map** — Build a service-map-like graph at function granularity, linked to triggering endpoints, consumers, or cron jobs, with invocation frequency. Capture heavy forensic traces only above a p99 or custom threshold to limit noise. *When:* When agents reason over code but observability data is at service or endpoint level, so the two do not line up.
- **Query language plus task skills** — Expose a constrained query layer over the telemetry, such as ClickHouse queries over a function/endpoint schema, and add skills for recurring investigations (e.g. 500 origin, memory spike vs baseline). Skills make results more consistent across runs. *When:* When agents write inconsistent queries on a complex analytics database such as ClickHouse.
- **ROI and risk scoring with a human-readable gist** — Rank candidate fixes by impact (hot path, business criticality) against effort and risk (migration needed, change size). Surface only the top items as short explanations with a suggested fix. Start with a small number per cycle to build reviewer trust. *When:* When automated analysis can produce far more candidates than the team will review.
- **Vendor-neutral workflow layer** — Keep the trigger (schedule or webhook), the agent harness, the model, and the output channel (Slack, Teams, email) as swappable parts. The speaker's setup is GitHub Actions, Claude Code, MCP for telemetry, and Slack output. *When:* When the workflow must stay portable across models, harnesses, and customer tooling.
- **Targeted automatic checks for known performance smells** — Search for well-known patterns (artificial sleeps or timeouts, N+1 queries, missing indexes, sequential awaits) and verify them with runtime evidence, not static analysis alone. *When:* Mature legacy codebases with many contributors where these patterns are common and cheap to fix.

## Numbers
- HUD's performance workflow runs weekly on GitHub Actions and uses Claude Code. ([6:38](https://youtu.be/JJGbw4ggaFs?t=398))
- One flagged endpoint's critical flow runs about 7,000 times a week (cited as the business exposure of a flagged fix). ([8:06](https://youtu.be/JJGbw4ggaFs?t=486))
- Illustrative report example: an endpoint usually about 200 ms, but sometimes about 45 seconds, caused by a query pattern that bypasses a Mongo search index. This is an example of the report format, not a measured benchmark. ([16:44](https://youtu.be/JJGbw4ggaFs?t=1004))
- Google DORA 2026 report, as cited: AI adoption mainly raised individual effectiveness, while team throughput stayed about the same and software broke more often. ([2:26](https://youtu.be/JJGbw4ggaFs?t=146))
- Speaker's trust threshold for autonomous agent work: about 80-90% reliability, versus tolerance for about 80% in interactive use. ([20:33](https://youtu.be/JJGbw4ggaFs?t=1233))

## Hot takes
- Interactive agent use tolerates about 80% reliability, but autonomous agent automation needs roughly 80-90% trust, which is a different engineering bar.
- The biggest gain from agents may be surfacing work teams would never do, not just doing existing work faster.
- Context over cleverness: good context and skills matter more than prompt tuning, and each new model improves the result.

## Tools mentioned
Claude Code, GitHub Actions, MCP, ClickHouse, Slack

## Relevance to our work
- **agentos** (2/3): AgentOS has L4 observability and telemetry-mined skills (SkillForge). HUD's approach of turning production traces into scored, verified investigations is a direct pattern for the open question of skill-worthiness scoring. → *Read the HUD talk's ROI and risk scoring section and consider adding a runtime before/after success signal to SkillForge's skill-worthiness scoring.*
- **prosharness** (2/3): ProsHarness runs long Claude Code agent loops on schedules with checkpoints. The HUD pattern of a scheduled Claude Code job that verifies its own output and reports to a human gate matches ProsHarness loops and phone-driven approvals. → *Add a verify-then-report step to a ProsHarness scheduled loop: require a measured before/after diff before a result reaches the approval queue.*
- **general** (1/3): Useful practitioner framing on trust thresholds for autonomous agents versus interactive use.

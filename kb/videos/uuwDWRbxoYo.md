# AI Writes More PRs. Who Validates Them? — Ali-Reza Adl-Tabatabai, Sonar

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `uuwDWRbxoYo` · [watch](https://youtu.be/uuwDWRbxoYo) · **date:** 2026-10-09 · **length:** 11:34 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Ali-Reza Adl-Tabatabai · **orgs:** Guitar (Guitar.ai), Sonar
- **topics:** pr-code-review, software-factory, observability · **tags:** pr-validation, agentic-code-review, flaky-tests, autofix, auto-merge, trust-ladder, static-analysis, model-routing, vendor-pitch

> Sonar's Ali-Reza Adl-Tabatabai pitches an agentic PR validation system (ex-Guitar) that reviews, fixes, and auto-merges PRs, with a trust ladder for rollout. Mostly product pitch, few numbers.

## Summary
The speaker, a founder of Guitar.ai (acquired by Sonar about a month before the talk), argues that PR validation (CI plus code review) is a central bottleneck that AI makes worse, because teams generate more and bigger PRs. He presents Guitar's agent as a way to automate the validation steps: it reviews PRs with inline comments, can block merges on unresolved findings, summarizes CI root causes, detects and retries flaky tests, and can autofix issues in a loop until the PR is green. He describes a trust progression where teams move from review-only to blocking, then autofix, then rule-based auto-approve and merge. Guitar's architecture has a control plane for PR workflows, its own agent harness (multi-agent execution, context, memory, tool calls) tuned for validation cost and precision, and an LLM proxy for model routing and failover. He also says that combining agents with Sonar's static analysis (taint, control-flow, data-flow, SCA) should improve precision. The talk gives no measured results, and it ends with a booth invitation.

## Key ideas
- **PR validation (CI plus code review) is the centralized gate that platform teams run, and it is slow, expensive, and hard to scale.** — Failures in this phase create outer loops measured in hours and days, and the work is often fragmented across bespoke scripts and integrations. ([0:13](https://youtu.be/uuwDWRbxoYo?t=13))
- **AI makes the validation problem worse: more PRs and bigger PRs, so teams must either review slowly or rubber-stamp.** — The speaker frames the choice as slowing developers down or risking production incidents. His answer is more AI, specifically an agentic approach to validation. ([2:47](https://youtu.be/uuwDWRbxoYo?t=167))
- **The agent handles the full validation loop: review, CI failure analysis, flaky-test retries, autofix, and merge.** — It posts inline comments, can be configured with custom rules and checks, can block merges on unresolved findings, and summarizes root causes of CI failures. ([3:48](https://youtu.be/uuwDWRbxoYo?t=228))
- **Teams adopt automation along a trust ladder: review, then blocking, then autofix, then rule-based auto-approve and merge.** — He says users move up as they see the reviews are accurate and important. This is a claim about observed customer behavior, with no data shown. ([5:12](https://youtu.be/uuwDWRbxoYo?t=312))
- **Running AI over every PR also produces platform-level insights.** — Examples are categorizing top CI failures (flakiness vs infrastructure) and categorizing landed PRs (features vs fixes, chores, refactors) for leadership. ([6:32](https://youtu.be/uuwDWRbxoYo?t=392))
- **The architecture is a control plane for PR workflows, a custom agent harness, and an LLM proxy for routing and failover.** — The in-house harness handles multi-agent execution, context and memory management, and tool calling. The speaker says owning it lets them tune for token cost, precision, and coverage, which supports a fixed per-PR price. ([7:32](https://youtu.be/uuwDWRbxoYo?t=452))
- **Agents plus deterministic program analysis should beat either alone.** — The speaker proposes combining agents with taint, control-flow, data-flow, and software-composition analysis from SonarQube, saying this should improve precision and coverage. This is a stated opportunity, not a demonstrated result. ([9:33](https://youtu.be/uuwDWRbxoYo?t=573))

## Techniques
- **Trust-gated automation ladder** — Roll out agent PR automation in stages: advisory review comments first, then block merges on unresolved findings, then enable autofix loops, then allow auto-approve and merge only under explicit rules. *When:* When introducing an AI reviewer to a team that does not yet trust its accuracy, and you want to expand its authority only after it proves precise.
- **Autofix loop until green** — The agent repeatedly addresses review findings and CI failures until the PR passes all checks, then hands off a ready-to-merge PR. Can be triggered for one issue or set to loop automatically. *When:* For mechanical CI or review failures where the fix is well-scoped and can be checked by CI again.
- **Flaky-test detection and rule-based retry** — Analyze CI failures to identify flaky tests, post root-cause summaries, and apply configurable rules that automatically retry known flaky tests. *When:* When CI noise from flaky tests slows merges and developers are wasting time on reruns.
- **Agent plus static-analysis hybrid** — Use deterministic analyses (taint, control-flow, data-flow, SCA) to supply precise evidence, and let agents reason over and triage the results. *When:* For security-sensitive review of AI-generated code where precision matters more than raw agent coverage.
- **Model routing proxy with failover** — Put a proxy in front of multiple LLM providers that routes requests by model and fails over automatically when a provider fails. *When:* When the agent pipeline must keep working through individual model provider outages or rate limits.
- **Aggregate PR and CI analytics** — Classify every CI failure and every landed PR with the model, then present the categories as platform or leadership dashboards. *When:* When platform teams need to find which failure types (flakiness, infrastructure, feature work vs. fixes) to prioritize.

## Numbers
- Failures in the validation phase create outer loops measured in hours and days. No measured figure is given. ([1:33](https://youtu.be/uuwDWRbxoYo?t=93))
- AI increases the number and size of PRs. No volume or size figures are given. ([2:47](https://youtu.be/uuwDWRbxoYo?t=167))
- Guitar offers a fixed per-PR price for outcomes. No price is stated. ([8:32](https://youtu.be/uuwDWRbxoYo?t=512))
- The talk cites no benchmarks, accuracy rates, latency, merge-time reductions, or adoption numbers. The results section (about 9:33) is qualitative only. ([9:33](https://youtu.be/uuwDWRbxoYo?t=573))

## Hot takes
- As AI raises PR volume, validation rather than generation becomes the main bottleneck.
- Teams should earn trust in agent review before giving it blocking or auto-merge authority.
- Agent-based review combined with deterministic program analysis beats either approach alone.

## Tools mentioned
Sonar, SonarQube, Guitar (agent platform)

## Relevance to our work
- **agentos** (1/3): The LLM proxy with model routing and failover is a loose parallel to AgentOS's L1 strategy routing. The talk gives no design detail or data. → *Compare how AgentOS L1 handles provider failover with the 'NLM proxy' description. Read nothing else from this talk for it.*
- **prosharness** (1/3): Trust-gated approval levels loosely parallel ProsHarness's phone-driven approvals. The talk is a vendor pitch with no mechanism details. → *Consider a staged approval policy (advisory, then blocking, then auto-approve) for ProsHarness plan approvals. Low priority.*

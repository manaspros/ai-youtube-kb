# AI-Generated Code Is Already Competing With Human Code — Daksh Gupta, Greptile

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `474j-n1Ltxc` · [watch](https://youtu.be/474j-n1Ltxc) · **date:** 2026-10-04 · **length:** 12:41 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Daksh Gupta · **orgs:** Greptile
- **topics:** pr-code-review, coding-agents, evals · **tags:** AI-generated PRs, PR quality metrics, revert rate, review severity, failure-mode profiling, agent code validation, sandboxed PR testing, autonomous coding agents

> Greptile's Daksh Gupta uses review data from its own PR pipeline to test whether fully agent-written PRs are worse than human PRs; his answer is roughly no on reverts, severity and review rounds, but failure modes differ by agent.

## Summary
Daksh Gupta of Greptile argues that fully autonomous coding agents are now producing real enterprise PRs, and he tests this with data from Greptile's review volume of over a million PRs a month. Detecting agent-written PRs is hard: GitHub's author field catches under 1%, while co-author footers and agent branch-name prefixes suggest about a quarter of PRs were completely or largely AI-generated, up from under 1% early last year. On his proxy metrics (revert rate, P0/P1/P2 review severity, review rounds to merge), agent PRs look roughly on par with human PRs, with some agents producing fewer P0s than humans. The main difference he finds is in failure modes: keyword counts in about several million review comments show each agent has a distinct error profile against a human 1x baseline. He closes with a framework for validating PRs before merge: does the change break the user contract, does it raise the risk of future violations, and does it match the author's intent, checked by agents running the code in sandboxes. The talk is partly a product pitch, and its data is from one reviewer's sample using proxy signals, so the numbers are indicative rather than rigorous.

## Key ideas
- **Autonomous coding agents went from tab-complete (2022) to multi-file edits (2024) to end-to-end PR-producing agents (2025), with a sharp shift in December 2025.** — The speaker treats the December models as a watershed for truly autonomous coding. He says he was skeptical that real companies could work this way, and his data is meant to test that. ([1:13](https://youtu.be/474j-n1Ltxc?t=73))
- **Agent-written PRs are hard to count with the obvious signals.** — GitHub's author field flags fewer than 1% of PRs as agent-authored. Co-author footers and agent branch-name prefixes give a much larger share, about a quarter of PRs in a given month being completely or largely AI-generated, and that share grew from under 1% early last year. ([3:32](https://youtu.be/474j-n1Ltxc?t=212))
- **On proxy quality metrics, agent PRs are roughly even with human PRs.** — Revert rates for agents and humans are close, and PR size does not explain the gap. In review severity, three of four tested agents produced fewer P0s than humans, and P1/P2 counts were about equal. ([5:00](https://youtu.be/474j-n1Ltxc?t=300))
- **Review rounds to merge show little difference between agent and human PRs.** — The speaker reports about 2.1 rounds for one agent, 2.45 for another, with humans in the middle. He reads this as no strong evidence that agent PRs need more iteration before merge. ([7:57](https://youtu.be/474j-n1Ltxc?t=477))
- **Agents fail in different ways from humans, and the differences matter more than the averages.** — By counting risk terms such as SQL injection and N+1 query in review comments, the speaker finds Claude at about 1.5x the human rate for SQL injection, and one agent at about half the human rate for off-by-one errors. The implication is that validation should target each agent's own error profile. ([9:25](https://youtu.be/474j-n1Ltxc?t=565))
- **Validation for high-volume agent PRs should check three questions, not just style or tests.** — He proposes asking whether a change violates the user contract, whether it raises the chance of a future contract violation, and whether it does what the author intended. Agents can answer these by running the code in a sandbox, installing dependencies, mocking inputs and driving a browser. ([10:26](https://youtu.be/474j-n1Ltxc?t=626))

## Techniques
- **Signal-based detection of agent-authored PRs** — Combine the git author field, co-author footers that agents add to PR descriptions, and agent-style branch-name prefixes. Each signal alone is weak; together they give a usable split between agent and human PRs. *When:* When you need to measure agent output in a codebase or compare agent and human PR outcomes, and no single metadata field is reliable.
- **Proxy quality metrics for agent PRs** — Track revert rate (reverts can be found through revert-branch naming), review severity counts (P0/P1/P2 from a review bot), and review rounds from open to merge. Compare each group with a human baseline set at 1x. *When:* When you lack ground-truth quality labels and want an early read on whether agent output is worse than human output.
- **Per-agent failure-mode profiling via keyword counts** — Scan review comments for risk-category phrases (for example SQL injection or N+1 query), count per author type, and express each agent's rate as a multiple of the human rate. The result is a per-agent failure profile, not a single quality score. *When:* When you run several coding agents and want to know which review checks to tune for each one, or which agent needs extra scrutiny for a given risk class.
- **Three-question PR validation gate** — For each PR, check (1) does it break the existing user contract, (2) does it make a future contract break more likely, and (3) does it match the author's stated intent. Answer by executing the change in a sandbox: install dependencies, start the app, mock inputs and drive a browser. *When:* When agent-written PRs are merged at high volume and reviewers cannot read every diff, and you need execution-based evidence before merge.

## Numbers
- Share of PRs with GitHub author set to an AI agent (Codex, Claude, Cursor): under 1%. ([3:32](https://youtu.be/474j-n1Ltxc?t=212))
- Share of PRs in a given month that are completely or largely AI-generated, by co-author footers and branch prefixes: about 25%. Early last year it was under 1%. ([3:32](https://youtu.be/474j-n1Ltxc?t=212))
- Revert rate: about 2.5 per 1,000 PRs for humans. Captions are garbled for the agent figures, which read as about 1 per 1,000 for one agent and about 3.5 per 1,000 for another. ([5:00](https://youtu.be/474j-n1Ltxc?t=300))
- Average review comments per PR from the review bot: about 4, across a corpus of several million comments. ([6:28](https://youtu.be/474j-n1Ltxc?t=388))
- Review rounds to merge: about 2.1 for one agent, 2.45 for Codex, humans in between. ([7:57](https://youtu.be/474j-n1Ltxc?t=477))
- Claude's SQL-injection comment rate: about 1.5x the human rate. One agent's off-by-one rate: about 0.5x the human rate (caption reads 'off-bypass'). ([9:25](https://youtu.be/474j-n1Ltxc?t=565))
- Greptile reviews more than 1 million PRs a month. Tens of thousands of engineers use it weekly. Median user writes 50 PRs a month (about 2 per workday), P90 writes 500, P99 is in the thousands. ([9:25](https://youtu.be/474j-n1Ltxc?t=565))

## Hot takes
- Fully autonomous agent PRs are about as good as human PRs on reverts, severity and review rounds, so the question is no longer whether they can ship but how to validate them.
- Averages hide the story: each coding agent has its own failure profile, so review and validation should be tuned per agent.
- Code review and testing have to scale with PR volume; a team that merges hundreds of PRs a month cannot rely on human review and QA alone.

## Tools mentioned
Greptile, Codex, Claude Code, Devin, Cursor, GitHub

## Relevance to our work
- **agentos** (1/3): The SkillForge open question is which success signal to use for skill-worthiness. Reverts, review rounds and review severity are candidate proxy signals for agent output quality, although the talk gives no validation of them as success measures. → *Read how this talk's proxy metrics (revert rate, review rounds, severity counts) could serve as candidate success signals when SkillForge mines agent telemetry.*
- **prosharness** (1/3): ProsHarness runs agents that produce code and checks them with plan, critique and debate steps. Tagging agent-authored PRs and tracking review rounds could show whether the harness output needs more review. → *Consider a harness-side check that labels agent-authored PRs (co-author footer, branch prefix) and records review rounds to merge for each run.*
- **general** (1/3): Useful as a framing for how to measure and validate agent output in general, including the per-agent failure-mode comparison against a human baseline. → *Use the per-agent failure-mode profiling method (keyword counts normalized to a human baseline) as a template for comparing coding agents on our own repos.*

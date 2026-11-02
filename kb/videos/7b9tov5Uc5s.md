# Rebuilding CI for AI-Scale Commit Volume — Gautam Korlam, Sonar

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `7b9tov5Uc5s` · [watch](https://youtu.be/7b9tov5Uc5s) · **date:** 2026-10-15 · **length:** 19:19 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Gautam Korlam · **orgs:** Sonar, QAR (captioned 'Guitar'/'Solar'), Uber
- **topics:** pr-code-review, software-factory, governance-compliance, infra-cost-scaling · **tags:** merge-queue, CI, monorepo, agent-generated-PRs, audit-trail, auto-approval, regulated-industries, build-caching, rust, uber-submitqueue

> Gautam Korlam (Sonar/QAR, ex-Uber) on why CI, merge queues and review were built for human speed, and how to keep agent-scale commits green, fast and auditable in regulated teams.

## Summary
The speaker argues that merge queues, CI and code review were designed for human commit rates and break down once agents open PRs continuously. He recounts Uber's SubmitQueue, which tests combinations of pending commits in parallel to keep trunk green. He says per-PR CI can pass while the merged trunk is broken, and that CI artifacts expire, so teams need a saved record of what was checked, by which agent, triggered by whom, and how each finding was resolved. His proposed fixes are faster CI (caching, sharding, moving expensive checks left or post-merge), layered AI review before humans, and plain-English approval policies that auto-approve low-risk changes, escalate sensitive ones, and forbid an agent from approving its own change. The talk is mostly practitioner experience with a few concrete numbers, but it closes with product promotion for the code-review tool.

## Key ideas
- **Merge queues and CI/review queues were built for human commit rates and become the bottleneck once agents open many PRs at once** — Humans pushed changes a few times an hour. Agents push several PRs a day and all arrive together, so centralized queues back up and slow the whole software factory. ([2:47](https://youtu.be/7b9tov5Uc5s?t=167))
- **Uber's SubmitQueue tests combinations of pending commits in parallel and evicts changes that would break trunk** — It predicts which PRs would break when combined, returns those to the author for a rebase and fix, and only lets in changes that pass in every combination. Without it, trunk was red most of the time, and with strict serial merging a backlog could take up to about 20 days. ([1:05](https://youtu.be/7b9tov5Uc5s?t=65))
- **Green per-PR CI does not guarantee a green trunk after merge** — Two changes can each pass CI and still break main when combined, so the check has to cover the combined state. ([5:01](https://youtu.be/7b9tov5Uc5s?t=301))
- **CI and review artifacts expire, so a durable record of what was checked is needed for audit** — Logs expire and an approval stamp alone does not show what was actually checked. Saved test reports, the commit a CI run trusted, and finding resolutions should be stored on the PR or another system of record. ([6:40](https://youtu.be/7b9tov5Uc5s?t=400))
- **Review is the largest share of time-to-production, so AI should do a fast first pass and humans should see only what is left** — The speaker measured that most P90 PR time was spent in review rather than CI. He suggests several quick AI review passes, with deeper review only for higher-risk changes. ([11:37](https://youtu.be/7b9tov5Uc5s?t=697))
- **Auto-approve low-risk changes under plain-English policies, escalate sensitive ones, and never let an agent approve its own change** — Docs, dependency bumps and security patches can be auto-approved, while payments-related changes need a human. Custom rules are written in English, and the approver must be separate from the author, and the human who prompted the agent is not counted as an author. ([13:54](https://youtu.be/7b9tov5Uc5s?t=834))
- **Regulated teams need lineage that shows which changes affect controlled areas** — A feature-flag change at Uber let drivers onboard without checks in London, which put its licence at risk. Afterwards every change touching London went through a check for which controls applied. The same approach is applied to HIPAA or SOX-style rules that agents will not know about. ([9:26](https://youtu.be/7b9tov5Uc5s?t=566))
- **Record provenance on every change: which agent wrote it, from what session, and who or what triggered it** — Also record each override with a named reason. Require that the merged code carries all the checks and that a small later commit cannot slip in unchecked. ([16:44](https://youtu.be/7b9tov5Uc5s?t=1004))

## Techniques
- **Parallel speculative merge queue** — Batch and test the likely combinations of pending commits in parallel, evict any PR that breaks a combination, and send it back to the author for a rebase before it re-enters the queue. *When:* A large monorepo with many concurrent changes where serial merging is too slow and a broken trunk is costly.
- **Move checks left and offload expensive checks** — Keep the CI step fast so repairs are quick, and push slow or expensive tests to pre-merge or post-merge where they are cheaper to run and do not block iteration. *When:* CI is slowing down as agent commit volume rises and the expensive tests do not need to gate every commit.
- **Cache, shard and reduce compiler churn** — Cache build outputs and reuse them, shard the build, and change the code so compilation is more cacheable and invalidated less often. The speaker reports incremental CI dropping from about 10 minutes to under a minute once the cache is warm. *When:* A Rust or other compiled monorepo where each commit forces large rebuilds.
- **Layered AI review with a fast first pass** — Run a quick AI review on every PR, then a deeper review only for higher-risk changes. Let an agent fix the issues it finds on CI, so humans only review what remains. *When:* PR volume is too high for human review to keep up and most review findings are routine.
- **Policy-based auto-approval with escalation** — Write approval rules in plain English for low-risk classes such as docs, dependency bumps and internal tooling. Escalate sensitive paths to a named human and block self-approval by the authoring agent. *When:* A team that wants to auto-merge routine changes without weakening zero-trust controls.
- **Durable decision record on the PR** — Store the agent, session, trigger, saved test reports, the trusted CI commit, finding dispositions and named override reasons on the PR or a system of record, so the audit trail does not depend on CI artifacts that expire. *When:* Compliance or audit requirements where CI logs or statuses are not kept long enough.

## Numbers
- Serial merging of thousands of daily changes on Uber's monorepo could take up to about 20 days to get everything green ([1:05](https://youtu.be/7b9tov5Uc5s?t=65))
- Speaker's company commit rate has grown about 10x in roughly 3 years with a similar-sized team ([3:55](https://youtu.be/7b9tov5Uc5s?t=235))
- PR volume grows about 25% month over month on the speaker's code-review platform ([3:55](https://youtu.be/7b9tov5Uc5s?t=235))
- About 13% of PRs on the platform had at least one recorded CI failure ([7:15](https://youtu.be/7b9tov5Uc5s?t=435))
- CI went from about 10 minutes to under a minute for incremental builds after caching, compiler-churn fixes and sharding ([10:33](https://youtu.be/7b9tov5Uc5s?t=633))
- Most P90 time from PR to production was spent in review, not CI, at Uber and still in most teams ([11:37](https://youtu.be/7b9tov5Uc5s?t=697))
- Auto-approve and auto-merge adoption is growing quickly on the platform, including teams with over 100,000 developers ([13:54](https://youtu.be/7b9tov5Uc5s?t=834))

## Hot takes
- Green per-PR CI is not a safe signal for trunk once agents merge many PRs in parallel.
- Most teams are rubber-stamping agent PRs because human reviewers cannot keep up with volume.
- CI logs and statuses expire, so compliance requires writing the decision record onto the PR itself.
- An agent should never approve its own change, and the human who prompted it should not count as the approver.

## Tools mentioned
Rust, GitHub, Next.js (captioned 'next text'), Uber SubmitQueue (captioned 'summit cube')

## Relevance to our work
- **prosharness** (2/3): ProsHarness already has phone-driven approvals and loops. The talk's tiered policy (auto-approve low risk, escalate sensitive, block agent self-approval) would make those approvals more selective. → *Add an approval policy to ProsHarness: auto-approve low-risk diffs such as docs and dependency bumps, send sensitive paths to phone approval, and block approval of a run's own changes by the run that made them.*
- **agentos** (1/3): AgentOS already has a Merkle audit log. The talk's point that provenance (agent, session, trigger, override reason) must survive expiring CI artifacts is a useful addition to its audit schema. → *Extend the audit-log record schema with agent id, session id, trigger source, saved check outputs and named override reasons, so each agent-generated change has a self-contained record.*
- **general** (1/3): The talk's layered review (fast AI pass first, deep review only for risky changes) is a general pattern for agent-written code, relevant to the coding-agent workflow interest. → *Read the talk's layered-review section and compare it with how Claude Code review passes are currently structured in ProsHarness.*

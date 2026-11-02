# Building an Autonomous Engineering Org - Angie Jones, Agentic AI Foundation

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `whue9_YquGA` · [watch](https://youtu.be/whue9_YquGA) · **date:** 2026-07-18 · **length:** 17:36 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Angie Jones · **orgs:** Block, Agentic AI Foundation, Anthropic, OpenAI
- **topics:** software-factory, enterprise-adoption, multi-agent, pr-code-review · **tags:** maturity-model, AI champions, 1-9-90 rule, agentic engineering org, repo readiness, AGENTS.md, delegation from Slack, Codex auto-fix loop, isolated cloud workspaces, orchestrator, service dependency graph, BuilderBot, Goose, layoffs

> Angie Jones (Block) describes moving a 3,500-person engineering org to autonomous agent delegation via a maturity model, a power-user champions program, AI-ready repos, and an orchestrator.

## Summary
Angie Jones describes how Block's roughly 3,500-person engineering org moved toward agents producing shippable work. She defines an agentic org as one where engineers use agents as their main way of producing outcomes, and she uses a stage 0 to 5 maturity model to measure how engineers delegate and orchestrate. Rather than push all engineers at once, she used the 1-9-90 participation rule to pick about 50 power users (champions) who spent at least 30% of their time on enablement. The champions made repos AI-ready with context files, rules, slash commands, an AI co-reviewer and PR attribution, layered from a monorepo root down to services. Delegation then moved into Slack and issue trackers, and AI-authored code rose sharply. Once multi-agent parallelism created a review bottleneck, the org added Codex review with an auto-fix loop, isolated cloud workspaces per agent, and an orchestrator (BuilderBot) backed by a machine-readable map of about 25,000 repos. She closes by saying that reaching stage five was followed by layoffs that made the outcome feel like a nightmare, and she asks where the work is heading.

## Key ideas
- **Adoption of AI tools is not the same as impact. About 90% of engineers were using AI, but mostly inside the IDE, so shipping speed did not change.** — She sorts AI enablement into three phases (experimentation, adoption, impact) and says the org had passed experimentation but not reached impact. ([1:14](https://youtu.be/whue9_YquGA?t=74))
- **Use a stage model to measure how engineers work with agents: stage 0 no AI, stage 1 autocomplete, stage 2 chatting, stage 3 delegating and reviewing, stage 4 parallel agents, stage 5 fully delegated complete tasks.** — The model measures the engineer's relationship with agents (delegating, orchestrating), not tool usage. She says the Gastown article helped her reorganize her earlier version. ([2:42](https://youtu.be/whue9_YquGA?t=162))
- **Target the 1% power users rather than all engineers. Apply the 1-9-90 participation rule to AI adoption.** — She handpicked about 50 engineers across critical repos. Selection was not open to volunteers. Each had to commit at least 30% of their time and tolerate non-deterministic outputs. ([5:27](https://youtu.be/whue9_YquGA?t=327))
- **Make each repo AI-ready so the whole team benefits, not just the champions. The kit is context files, rules, repeatable slash commands, later skills, an AI co-reviewer with review guidance, and AI attribution on PRs.** — Context is layered: shared rules at the monorepo root, more specific files per service. Android and iOS needed different setups. Teams chose their own tools instead of a top-down mandate. ([7:31](https://youtu.be/whue9_YquGA?t=451))
- **Delegation has to feel native to where work already starts. Engineers could hand work to an agent from Slack, Jira/Linear, or GitHub issues, and the agent returned a PR link.** — She gives a Slack example where a bug was diagnosed, three fix options were offered, and a PR was opened, all in about five minutes. Teams ran out of tickets and had to pull more in. ([10:05](https://youtu.be/whue9_YquGA?t=605))
- **Once parallel agents raised PR volume, code review became the bottleneck. She says this is not fully solved.** — Codex was enabled on all repos, and a second agent automatically fixed issues Codex flagged and committed to the PR. She credits better models and the repo-readiness work for making bot reviews usable. ([12:33](https://youtu.be/whue9_YquGA?t=753))
- **Parallel agents need isolation, and at scale the orchestrator needs a machine-readable map of the whole system.** — Agents ran in dedicated cloud workspaces because laptops ran out of memory and agents collided. A company world model covering about 25,000 repos let agents explore different services in parallel and let an orchestrator merge their findings into one cross-repo plan. ([15:12](https://youtu.be/whue9_YquGA?t=912))
- **Her closing point is that reaching stage 5 did not settle whether the outcome is good. The layoffs that followed made her question whether the work was the right goal.** — She asks what the org is doing, where it is heading, and whether that is where they want to end up. ([16:31](https://youtu.be/whue9_YquGA?t=991))

## Techniques
- **Stage-based maturity model for agent use** — Rank engineers from no AI (0) through autocomplete, chatting, delegating with review, parallel agents, to fully delegated tasks (5). Use the ranking to decide where enablement effort goes. *When:* When an org reports that AI is in use but output has not changed, and you need a shared way to talk about depth of adoption.
- **Champions program of hand-picked power users** — Select about 50 engineers from critical repos and a range of stacks, not volunteers. Require roughly 30% of their time, and screen for tolerance of non-deterministic results. Champions then pioneer patterns for their own team. *When:* When broad top-down mandates are being ignored and the aim is to lift the 90% through the 1% who create.
- **Layered repo context files** — Put shared agent rules at the monorepo root and more specific AGENTS.md or CLAUDE.md files per service. Add rules files for guardrails, slash commands for repeatable workflows, and an AI reviewer with written review priorities. *When:* When agents write code that ignores team conventions in large or mixed repos.
- **Delegation from the tools people already use** — Wire the agent into Slack, the issue tracker and GitHub issues so a ticket or thread can be handed to an agent that returns a PR link. *When:* When engineers will not learn a new interface but already triage work in those channels.
- **Review agent plus auto-fix loop** — Run an AI reviewer on every PR. A second agent takes the reviewer's findings, fixes them, and commits to the same PR before a human looks. *When:* When parallel agents push more PRs than humans can review and the bot comments are only useful once the obvious issues are gone.
- **Isolated cloud workspace per agent** — Give each agent its own environment so runs do not collide and do not depend on a laptop's memory. *When:* When running four or five agents at once causes resource contention or file conflicts.
- **Machine-readable system map for orchestration** — Build a structured view of every service and how they connect. Agents explore different parts in parallel, and the orchestrator combines their results into a multi-repo plan. *When:* When tasks span several repos and each agent needs landscape context before it can plan.

## Numbers
- Engineering org size is about 3,500 engineers. The company-wide AI enablement covered 12,000 employees. ([0:00](https://youtu.be/whue9_YquGA?t=0))
- About 90% of engineers were using tools like Goose and Claude Code regularly within a couple of months. ([0:00](https://youtu.be/whue9_YquGA?t=0))
- About 90% of the engineering org was using AI, but largely only inside the IDE, and this did not improve shipping speed. ([1:14](https://youtu.be/whue9_YquGA?t=74))
- Champions program: about 50 hand-picked engineers, each committing at least 30% of their time to AI enablement. Set up around June 2025. ([5:27](https://youtu.be/whue9_YquGA?t=327))
- Three months after the champions program launched: AI-authored code up 69%, reported time savings up 37%, automated PRs up 21x (as stated in the talk). ([12:33](https://youtu.be/whue9_YquGA?t=753))
- Codebase scope for the company world model: about 25,000 repos. ([15:12](https://youtu.be/whue9_YquGA?t=912))
- Engineers were running four or five agents in parallel at any given time, and the number was growing. ([13:50](https://youtu.be/whue9_YquGA?t=830))
- A Slack-to-PR cycle (discussion, diagnosis, issue creation, alignment, fix) took about five minutes. ([11:13](https://youtu.be/whue9_YquGA?t=673))

## Hot takes
- Adoption follows the 1-9-90 rule, so the strategy should target the top 1% of creators rather than all engineers.
- Once agents produce many PRs, code review becomes the constraint, and bots that only comment are not enough without an auto-fix loop.
- Reaching full agent delegation (stage 5) does not answer whether the outcome is desirable, and the speaker says the layoffs that followed made her question the goal.

## Tools mentioned
Claude Code, Goose, Codex, BuilderBot, GitHub, Jira, Linear, Slack, MCP, AGENTS.md, CLAUDE.md

## Relevance to our work
- **prosharness** (2/3): The harness runs long agent work. Isolated workspaces per run and a reviewer-plus-auto-fix loop map directly onto checkpoint/resume and plan-critique loops. → *Give each parallel ProsHarness run its own isolated workspace and test whether a reviewer-then-fix pass on the run output reduces babysitting.*
- **general** (2/3): Layered context files (shared root rules with service-level overrides, plus rules and slash commands) match the user's context-engineering interest. → *Review how the user's CLAUDE.md and AGENTS.md files are layered across projects and check whether guardrail rules belong in separate rules files.*
- **agentos** (1/3): Talk covers org-level agent rollout, not infra. The review-then-auto-fix loop is a PR quality pattern that touches AgentOS's governance work only indirectly. → *Read the review-then-auto-fix loop description as a reference for a PR-quality gate on AgentOS changes.*

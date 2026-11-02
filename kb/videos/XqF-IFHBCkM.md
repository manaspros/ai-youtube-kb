# Redesigning How Software Gets Built With AI Agents — Sonar & McKinsey Panel

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `XqF-IFHBCkM` · [watch](https://youtu.be/XqF-IFHBCkM) · **date:** 2026-10-08 · **length:** 19:12 · **format:** panel · **quality:** 3/5 · **depth:** intro
- **speakers:** Tariq (CEO, Sonar; moderator's introduction spells it Tariq, captions also show Tarek/Tarik), Ali (former CEO of Guitar, now part of Sonar; previously ran developer platform at Uber), Pekar (moderator, McKinsey side; name as captioned) · **orgs:** Sonar, McKinsey, Guitar (as captioned; now part of Sonar), Anthropic (mentioned only)
- **topics:** enterprise-adoption, software-factory, pr-code-review · **tags:** agent adoption, maturity model, operating model, platform team, developer productivity metrics, trust ladder, autofix, auto-merge, PRD-derived evals, lighthouse teams, generalists, explicit specs

> Sonar and McKinsey panel on why most companies stall before scaling AI agents in the SDLC, and a staged trust ladder for moving from agent review to fully automated PR merge.

## Summary
Moderated panel from Sonar and McKinsey on scaling AI agents across the software development lifecycle. The speakers say most companies have deployed AI in some form, but fewer than a third have scaled it or seen business impact, mostly because pilots never reach end-to-end workflows. Their maturity scale puts most companies at "Horizon 2" (human-guided, validated agents on individual SDLC tasks) and very few at "Horizon 3" (end-to-end automation with human oversight). Their three factors are redesigning the process end-to-end, tooling (agents, harnesses, context layers), and the people side, where role boundaries such as engineer, PM and designer are blurring. The Guitar speaker describes a trust ladder for agent-driven PRs: review only, then blocking on critical findings, then autofix to green, then auto-approval for low-risk paths, then auto-merge, with each step unlocked by demonstrated precision. The talk is mostly high-level, with few hard numbers, and the panel repeatedly stresses that trust has to be earned with measurement and guardrails.

## Key ideas
- **Most firms have deployed AI or agents, but few have scaled them** — The moderator says 80-90% of companies report some AI or agent deployment, yet fewer than a third see scaled business impact. Their pilots stay in small POC environments and do not cover the end-to-end organization. ([0:12](https://youtu.be/XqF-IFHBCkM?t=12))
- **Three factors decide whether agents scale: process, tooling and people** — Process means redesigning the whole workflow rather than bolting agents onto the old SDLC. Tooling covers agents, harnesses and context layers. The people factor is often overlooked: role boundaries (engineer, PM, designer) blur, and organizations that remodel their operating model around that see the largest gains. ([1:35](https://youtu.be/XqF-IFHBCkM?t=95))
- **Maturity runs from human-guided agents (Horizon 2) to end-to-end automation (Horizon 3)** — Most companies sit at Horizon 2, where humans guide and validate agents that run individual SDLC tasks. Very few reach Horizon 3, fully automated workflows with human oversight. ([1:35](https://youtu.be/XqF-IFHBCkM?t=95))
- **Define the objective as real value, not token usage** — Sonar says it deliberately avoids 'token maxing' and measures actual value. It also built a guide-verify-solve model internally and recommends the same structure to other companies. ([3:50](https://youtu.be/XqF-IFHBCkM?t=230))
- **Role modeling by lighthouse teams is not enough on its own** — Sonar set up lighthouse teams to show best practice, including PRD agents that turn requirements into evals for output verification. The surprise was that other teams did not copy them quickly. Tooling gets part of the way, but teams also need to understand why they use agents. ([5:17](https://youtu.be/XqF-IFHBCkM?t=317))
- **Set a metrics baseline before adding agents to the pipeline** — Platform teams need telemetry first: how fast code reaches production, engineer throughput, quality and rework rate, and engineer sentiment. With that baseline, changes from adding agents can be measured and iterated on. ([8:04](https://youtu.be/XqF-IFHBCkM?t=484))
- **Automate whole workflows and remove grunt work to keep developers in flow** — Offloading complete workflows to agents, rather than single steps, gives the biggest velocity gain. Removing grunt work also raises developer sentiment, which the speaker ranks as at least as important as speed. ([9:26](https://youtu.be/XqF-IFHBCkM?t=566))
- **Trust grows through a staged ladder of autonomy** — Guitar users typically start with reviews and CI-failure analysis. Once findings prove precise, they block on critical issues, then enable autofix until builds are green, then auto-approve low-risk paths, and finally auto-merge. Each step follows measured precision and enough context and guardrails. ([14:57](https://youtu.be/XqF-IFHBCkM?t=897))
- **Make implicit team knowledge explicit, and keep humans as critical reviewers** — Conventions that teams keep in their heads need to be written down as specs. AI output sounds confident and plausible, so the human role shifts to questioning it, similar to onboarding an intern. ([12:08](https://youtu.be/XqF-IFHBCkM?t=728))

## Techniques
- **Staged autonomy ladder for agent PR workflows** — Move one step at a time: agent review only, then blocking on critical findings, then autofix until CI is green, then auto-approve for chosen paths or change types, then auto-merge with conflict resolution. Move up only after precision is shown at the current step. *When:* When rolling out an agent that reviews, fixes or merges code in a team that does not yet trust it.
- **Derive verification evals from the PRD** — Use a PRD agent to pull requirements out of the PRD and turn them into evals that verify agent output. *When:* When agents build features and you need an acceptance check that is tied to the spec, not just to code review.
- **Lighthouse teams for best practice** — Pick a few teams to run the new agent workflow, document what works, and share it. Pair this with explanation of why the agents are used, because copying the setup alone does not spread the practice. *When:* When rolling out agent practices across a large engineering org.
- **Baseline developer metrics before automation** — Track deployment speed, throughput, quality and rework rate, and survey engineer sentiment before adding agents. Compare after each change. *When:* Before any org-wide agent rollout, so gains and regressions can be measured.
- **Write down implicit conventions as explicit specs** — Capture team standards (preferred dependencies, code style, architecture rules) in writing so agents can follow them. *When:* When agents work on a codebase where standards live only in engineers' heads.

## Numbers
- 80-90% of companies surveyed say they have deployed AI or agents in some form (moderator's cited research) ([0:12](https://youtu.be/XqF-IFHBCkM?t=12))
- Fewer than a third of companies report having scaled AI or seeing business impact ([0:12](https://youtu.be/XqF-IFHBCkM?t=12))
- Speakers cite a '10x productivity' promised land for organizations that remodel their operating model (aspirational claim, no data shown) ([1:35](https://youtu.be/XqF-IFHBCkM?t=95))
- Guitar startup had about 5-6 people while building an agentic PR validation product ([6:43](https://youtu.be/XqF-IFHBCkM?t=403))
- Sonar started as an open source project 18 years ago ([3:50](https://youtu.be/XqF-IFHBCkM?t=230))

## Hot takes
- Organizations that remodel their operating model around agents, not just adding agents to the existing SDLC, are the ones that reach large productivity gains. [1:35]
- Large companies have a structural advantage in scaling AI tooling because they already have platform teams that set standards and metrics. [8:04]
- AI always gives high-conviction, plausible output and never admits doubt, so critical thinking is the most important skill for engineers. [12:08]
- Within the next year, more teams, including ones in large companies, will reach fully autonomous PR creation through merge. [17:41]
- Software engineering generalists will matter more than deep specialists in front end or back end. [13:32]

## Relevance to our work
- **prosharness** (1/3): The trust ladder (review, block, autofix, auto-approve, auto-merge) is a pattern for staging how much autonomy an agent gets, which is close to ProsHarness approval gating, though the talk does not cover harness internals. → *Consider sketching a staged autonomy ladder for ProsHarness approvals (for example, suggest-only, then auto-apply for low-risk steps) and promote a step only after measured precision on past runs.*

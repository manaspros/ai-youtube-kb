# Coding Agents Don't Scale Themselves. Neither Do Your Teams. — Patrick Debois, Tessl

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `zCJtYuqwm7E` · [watch](https://youtu.be/zCJtYuqwm7E) · **date:** 2026-09-18 · **length:** 22:06 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Patrick Debois · **orgs:** Tessl
- **topics:** enterprise-adoption, software-factory, context-engineering · **tags:** dark-factory, org-design, platform-team, paved-roads, skill-registry, retros, cost-visibility, hiring, risk-tiers, continuous-learning, claude-code

> Patrick Debois (Tessl) argues that scaling coding agents is an organizational problem: teams must shift effort from fixing agent output to improving shared context, harnesses, and platform-owned reusable parts.

## Summary
Patrick Debois compares the current resistance to dark-factory-style autonomous coding to the early resistance to continuous delivery in 2009, and says the blocker is organizational readiness rather than the technology. He says developers who felt reduced to writing prompts and specs regained interest once they started building tooling and harnesses for agents. His main advice is to stop fixing the code an agent produced and improve the system (context, harness, loops) instead, and to treat skeptics as useful sources of improvement. He describes team rituals changing: retros focus on repeated agent failures as system problems, and planning splits well-scoped work for agents from ambiguous work that needs human discussion. He argues that moving from solo use to a shared system is the multiplier, and that a platform owner must run a curated set of tested, secured, reusable skills, evals, and guardrails rather than letting forks sprawl. He also covers making cost and agent iteration counts visible, hiring signals (AI-assisted exercise, then an explain-why walkthrough, then collaboration), and risk-tiered autonomy backed by provenance and verification. The talk is opinion-led with few hard numbers.

## Key ideas
- **Resistance to autonomous coding is about readiness, not technology** — He draws a parallel to continuous delivery being called crazy in 2009. He says people who call dark factories unworkable are signalling that their organization is not set up for it yet. ([0:08](https://youtu.be/zCJtYuqwm7E?t=8))
- **Harness and tooling work gives engineers back a craft** — Developers who felt reduced to prompting and writing specs found real engineering work in building tooling, harnesses, and programmatic help for agents. He sees this as re-engaging skeptics. ([2:34](https://youtu.be/zCJtYuqwm7E?t=154))
- **Fix the system, not the agent's output** — The big shift he recommends is to stop repairing code the agent wrote and instead improve the context, harness, and loops that produce it. He credits the idea of building the thing that builds the thing. ([4:59](https://youtu.be/zCJtYuqwm7E?t=299))
- **Engineering practices still apply to agents** — Tests, documentation, and similar practices are now things you instruct agents to do. He says teams should stop vibe-coding because the practices keep the system maintainable and help the agent improve. ([6:39](https://youtu.be/zCJtYuqwm7E?t=399))
- **Retros and planning change shape** — Retros ask whether the system can be fixed when the agent hits the same problem repeatedly. Planning splits work: well-scoped tasks go straight to agents, while unclear work stays with humans for team discussion. ([6:39](https://youtu.be/zCJtYuqwm7E?t=399))
- **Shared context is the multiplier, and it needs an owner** — One change to a shared harness or guideline improves every person's agent, unlike a solo 10x effect. Platform teams need an owner for shared registries of skills, evals, guardrails, and identities, or the result is sprawl with several forks. ([9:41](https://youtu.be/zCJtYuqwm7E?t=581))
- **Paved roads, not one standard** — He expects a small catalogue of three or four maintained options. Shared components should be testable, modular, and security-scanned so teams can extend them instead of rebuilding them. ([11:08](https://youtu.be/zCJtYuqwm7E?t=668))
- **Make agent cost and iteration visible** — Platform teams should show how much each team spends and how much value it gets. Reducing agent iterations is an optimization only if someone measures it. The reflex should be to optimize spend rather than cap it, via model choice, better context, and better harnesses. ([13:33](https://youtu.be/zCJtYuqwm7E?t=813))
- **Hire for AI use, explanation, and collaboration** — Job titles like AI engineer carry little signal. He suggests an exercise where AI use is allowed, then a walkthrough asking the candidate to explain the reasoning, then a check on whether they share and collaborate. ([14:57](https://youtu.be/zCJtYuqwm7E?t=897))
- **Autonomy is a risk dial per feature** — Not every feature should become autonomous. Teams can spend more on audit trails, provenance, and verifiers for riskier work, and on situational awareness for when things fail. Continuous delivery becomes continuous learning as knowledge moves into skills, context, and harnesses. ([19:09](https://youtu.be/zCJtYuqwm7E?t=1149))

## Techniques
- **Convert skeptic critique into context and harness work** — Ask critical developers to write the knowledge, standards, and checks that would make the agent's output better, rather than only complaining about quality. *When:* When a team has resistant engineers who doubt agent-generated code.
- **System-level retro** — In retros, log problems the agent hit repeatedly and turn each into a fix to the shared context, harness, or loop, instead of only fixing the individual code change. *When:* When the team runs agents on recurring work and sees the same failure more than once.
- **Split planning by agent readiness** — Sort backlog items into well-scoped tasks that can go straight to agents and ambiguous items that need a human or team decision first. *When:* When planning a sprint that mixes agent-ready and fuzzy work.
- **Platform-owned reusable registry with a named owner** — Keep shared skills, linters, security checks, and eval setups in one registry. Assign an owner who makes each component testable, modular, and secured, and offer a small set of paved roads. *When:* When several teams duplicate the same skills, harnesses, or auth work, or fork each other's.
- **Per-team cost and iteration dashboards** — Measure spend and agent iteration counts per team and per task, so optimization targets are visible. *When:* When leadership asks to cap agent spend and you want to reduce cost with evidence instead.
- **Three-step AI-friendly hiring loop** — Give a take-home where AI use is allowed, run a walkthrough asking the candidate to explain why each choice was made, then assess collaboration and openness. *When:* When hiring engineers for agent-heavy teams and job titles do not indicate skill.
- **Risk-tiered autonomy** — Decide per feature how much autonomy is acceptable. Use provenance tracking (who changed what), verifiers that check usefulness, and situational awareness for failures, with more controls on riskier work. *When:* When deciding which features an agent may ship without human approval.

## Hot takes
- Stop fixing the code the agent produced; improve the system that produces it.
- Do not cap agent spend; optimize it, because better context and harnesses lower cost.
- AI engineer and similar new job titles say nothing reliable about skill.
- Solo agent use does not win; shared, team-level systems do.
- Developers should not be vibe-coding; engineering practices still apply to agent work.

## Tools mentioned
Claude Code

## Relevance to our work
- **prosharness** (2/3): The harness is where the talk says teams should invest. Its advice to turn repeated agent failures into system fixes and to tier autonomy by risk fits ProsHarness's checkpoint and approval design. → *Add a retro step to ProsHarness checkpoint reviews that records repeated agent failures and turns each into a harness, context, or guideline change, with a risk tier that sets how much approval a run needs.*
- **agentos** (1/3): The talk's points on skill registries, eval systems, and guardrails owned by a platform team are relevant to AgentOS SkillForge and the shared skill layer, but they are organizational, not architectural. → *Give SkillForge an explicit owner, a test and security bar for shared skills, and a reuse count before expanding it beyond a personal folder.*
- **general** (1/3): The hiring and team-shape advice is useful for building an AI-native team, but the talk gives no measured evidence. → *Read the speaker's linked agent enablement patterns page for concrete patterns, if the speaker has posted it.*

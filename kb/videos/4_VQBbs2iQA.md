# How Building with AI Can Double the Throughput of Your Engineering Team — Brian Scanlan, Intercom

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `4_VQBbs2iQA` · [watch](https://youtu.be/4_VQBbs2iQA) · **date:** 2026-05-18 · **length:** 21:49 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Brian Scanlan · **orgs:** Intercom, Anthropic
- **topics:** claude-code, enterprise-adoption, skills-self-improvement, pr-code-review · **tags:** engineering throughput, Claude Code, skills, flywheel, auto-approval, backtesting, telemetry, platform standardization, flaky tests, maturity model

> Intercom's platform lead explains how they set a goal to double engineering throughput by standardizing on Claude Code, backed by skills, hooks, calibrated auto-approval and telemetry.

## Summary
Brian Scanlan, a senior principal engineer at Intercom, describes the company's "2X" project to double engineering throughput, measured as code changes per R&D person. After dissatisfaction with Copilot, Cursor and other tools, Intercom standardized on Claude Code in December and began rolling it out in January. The approach is to connect the agent to everything an engineer can do, onboard it with company conventions, and update its guidance (skills, hooks, plugins) every time it goes wrong, so the setup works as a flywheel. Skills are kept small, testable and backtested against historical changes and incidents, and the speaker urges giving agents problems rather than step-by-step tasks. Code review became the bottleneck, so Intercom added automatic approvals whose confidence was calibrated with backtesting and human labels, and it logs skill invocations and full session transcripts for analysis. The talk is a company-level account with few audited numbers, and the captions garble some chart values, so the figures should be treated as the speaker's own internal claims.

## Key ideas
- **Measure a concrete goal and pick one platform** — The goal was to double engineering throughput, measured as code changes per R&D person. Intercom dropped its multi-tool approach and went all-in on Claude Code, comparing multi-tool use to multi-cloud: you lose the compounding benefit of one well-tuned platform. ([3:32](https://youtu.be/4_VQBbs2iQA?t=212))
- **Connect the agent to everything an engineer can do, and onboard it like a new hire** — The target is an agent that acts like a senior engineer across the codebase. It has to learn Rails conventions, architecture, React patterns, testing standards and security rules, and it runs under the same controls and audits as human engineers. ([8:09](https://youtu.be/4_VQBbs2iQA?t=489))
- **Every failure becomes a guidance update (flywheel)** — When the agent misses or goes down a wrong path, the team updates the skills, guidance and hooks so it does not repeat the mistake. Plugins are pushed straight to laptops, bypassing Claude Code's own update mechanism, because install problems across hundreds of machines were costly to debug. ([9:12](https://youtu.be/4_VQBbs2iQA?t=552))
- **Give agents problems, not tasks** — Rather than telling the agent which skill to run, the speaker describes the problem and lets the agent pick the skill. In one case the agent found and used an internal data-breach skill the speaker did not know existed, and finished a roughly 20-minute analysis in about 2 minutes. ([12:46](https://youtu.be/4_VQBbs2iQA?t=766))
- **Build small, durable, testable, backtested skills** — Skills are kept small and high quality, validated against the large body of past code changes and incidents, and set up to update themselves. The speaker prefers adopting external tools as they ship over building its own orchestration layers. ([12:46](https://youtu.be/4_VQBbs2iQA?t=766))
- **Staged maturity path for engineers** — The speaker lays out a ladder: use Claude Code for everything, automate your work, turn the automation into a skill, get good at writing and improving skills, then optimize the environment (architecture, docs) for agents. ([15:05](https://youtu.be/4_VQBbs2iQA?t=905))
- **Auto-approval only after calibration against human labels** — Code review became the bottleneck. Intercom backtested its automatic approvers on past data, had humans label outputs, measured the confidence of each approver, and shaped PRs toward small, simple, safe changes. It says it worked with auditors so the setup meets SOC 2, ISO 27001 and HIPAA without humans in the loop. ([16:22](https://youtu.be/4_VQBbs2iQA?t=982))
- **Telemetry on skill use and full transcripts as a feedback loop** — Hooks send skill invocations to Honeycomb for internal visibility. Full session transcripts go to S3 for data mining, report writing and checking which skills are effective. ([17:35](https://youtu.be/4_VQBbs2iQA?t=1055))
- **Let skills emerge from a feedback loop with the agent** — The flaky-spec skill was not written up front. The speaker worked with the agent toward a goal, guided it to the right fixes, and let it produce the skill, which uses progressive disclosure and lookup tables. ([19:58](https://youtu.be/4_VQBbs2iQA?t=1198))

## Techniques
- **Single-platform standardization with internal plugin distribution** — Choose one coding agent and make it the default for all technical work. Push internal plugins (skills, hooks, base tooling) directly to every laptop instead of relying on the tool's update path. *When:* A medium or large engineering org that wants compounding gains from shared guidance and wants to avoid fragmented, per-person tool setups.
- **Guidance flywheel** — Each time the agent fails or takes a wrong path, record the fix as an update to skills, guidance files or hooks so the failure does not recur. Everyone contributes to the same shared guidance. *When:* Ongoing use of an agent across many engineers on a large, convention-heavy codebase.
- **Problem-first prompting** — Describe the outcome or problem, not the procedure, and let the agent choose which skill to invoke. Keep explicit skill invocation as a fallback. *When:* The skill library is good enough that the agent can find the right procedure itself, for example incident triage or policy checks.
- **Backtested skill authoring** — Write skills through a loop with the agent against a concrete goal. Test them against historical changes, incidents and PRs. Use progressive disclosure, lookup tables and a clear structure so the skill stays readable. *When:* A recurring, well-defined task such as fixing flaky tests, where past data can show whether the skill is working.
- **Calibrated automatic approval** — Backtest automated approvers on previous PRs, have humans label outputs, measure the confidence of each approver, and restrict auto-approval to small, simple, low-risk changes. Keep audit controls in place. *When:* Code review is the bottleneck and the agent-written changes are routine and low risk.
- **Agent telemetry and transcript mining** — Use hooks to emit skill-invocation events to observability tooling. Export full session transcripts to object storage and run reports or analysis over them to see which skills get used and how well they work. *When:* You need to know which agent guidance is used and effective, and you want a data-driven loop for improving skills.

## Numbers
- About 1,400 people across Dublin, London, Berlin, SF, Chicago and Sydney; R&D led from Dublin. ([0:00](https://youtu.be/4_VQBbs2iQA?t=0))
- Fin has over 8,000 customers and revenue approaching $100M (speaker's figures). ([1:02](https://youtu.be/4_VQBbs2iQA?t=62))
- Intercom's own models serve 100% of Fin's English text conversations, which the speaker says outperform frontier models. ([1:02](https://youtu.be/4_VQBbs2iQA?t=62))
- About 2 million resolutions per week. ([2:28](https://youtu.be/4_VQBbs2iQA?t=148))
- Goal of doubling engineering throughput ('2X'), measured by code changes per R&D person. ([3:32](https://youtu.be/4_VQBbs2iQA?t=212))
- Platform decision in December, rollout from January, and PR throughput doubled in under one year. ([15:05](https://youtu.be/4_VQBbs2iQA?t=905))
- 17.6% approval rate of automatic code approvals. ([16:22](https://youtu.be/4_VQBbs2iQA?t=982))
- Defects had been rising until recently and are now closed faster than ever (no exact figure given). ([17:35](https://youtu.be/4_VQBbs2iQA?t=1055))
- Hundreds of thousands of tests in the suite, and hundreds of contributors to the internal Claude plugins. ([18:42](https://youtu.be/4_VQBbs2iQA?t=1122))
- A security-analysis task that would take about 20 minutes manually was done by the agent in about 2 minutes. ([14:12](https://youtu.be/4_VQBbs2iQA?t=852))

## Hot takes
- Humans are not as good as agents when the work is well defined, so auto-approval can reduce risk rather than add it.
- Everything a human engineer can do, the agent must be able to do.
- Model anxiety is like multi-cloud: pick one coding platform and go all in.
- Teams should not each build their own multi-agent orchestrators; adopt what the market ships and keep the focus on durable skills.
- SOC 2, ISO 27001 and HIPAA certification does not require humans in the loop, provided audit controls are in place.

## Tools mentioned
Claude Code, GitHub Copilot, Cursor, Augment, Honeycomb, S3, DX, Ruby on Rails, React, GitHub

## Relevance to our work
- **agentos** (2/3): Calibrating auto-approval against human-labelled backtests and mining session transcripts both bear on SkillForge's open question about a success signal and skill-worthiness scoring. → *Prototype a SkillForge success signal by backtesting candidate skills against historical sessions with human-labelled outcomes, and log every session transcript to a store for mining.*
- **general** (2/3): Problem-first prompting and the guidance flywheel are directly relevant to the context-engineering and coding-agent workflow interests. → *Move our Claude Code CLAUDE.md and skills toward problem-first prompts, and add a rule that every repeated agent failure gets a written guidance update within the same session.*
- **prosharness** (1/3): Skill maintenance through a guidance flywheel and backtesting overlaps with ProsHarness's skill-ranking work, but the talk does not describe a planner or checkpoint design. → *Consider backtesting skill-ranking results against past ProsHarness runs before a skill is ranked as useful.*

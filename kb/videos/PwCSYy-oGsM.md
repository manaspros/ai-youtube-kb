# Containment Is Lying to You: Measuring AI Agents Like Employees — Druid AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `PwCSYy-oGsM` · [watch](https://youtu.be/PwCSYy-oGsM) · **date:** 2026-10-12 · **length:** 22:00 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Michael (head of developer community, Druid AI), Dan (co-founder and chief product officer, Druid AI) · **orgs:** Druid AI
- **topics:** evals, governance-compliance, enterprise-adoption, product-ux · **tags:** containment-rate, agent-scorecard, governance, human-baseline, handoff, agent-roi, banking-agents, vanity-metrics

> Druid AI argues containment rate misleads agent evaluation and proposes a weighted, 0-2 scored framework (six pillars, 26 components) judged like an employee and re-run weekly against a human baseline.

## Summary
Michael and Dan from Druid AI present a framework for judging conversational agents the way a manager judges interns. They open with a banking example: Intern A contains 80% of conversations and Intern B 96%, yet A is the better hire once handoff design and outcomes are counted. The framework has six pillars split into configured (what exists before the agent runs) and runtime (tasks, execution, output) groups, with governance cutting across all of them, for 26 components in total. Each component scores 0 if missing, 1 if measurable (automatic or manual), and 2 if managed (tracked over time), and the clusters are weighted, with governance at 39% and mandate at 26%. In the example, Agent A scores 83% overall and beats B in most clusters, with B weak on explainability and success tracking. The speakers argue agents must be re-run weekly on live traffic against a human baseline, since a flat 92% vanity dashboard hid a real score that slid from 83 to 60. They also argue ROI should be measured as what work the agent removed and what the human did with the freed time. Industry containment benchmarks from their own 2026 report (financial services 80%, healthcare 87%, HR/IT 93%, higher education 99%) are used to show the number depends on industry and handoff design. The talk is a vendor pitch for Druid's report and product, but the scoring method itself is concrete.

## Key ideas
- **Containment rate alone misleads** — A higher share of conversations handled without a human (Intern B, 96%) can be the worse agent if it skips designed handoffs for high-value signals such as a customer rethinking a mortgage. Containment is easy to measure and sits on every dashboard, which is why it gets trusted. ([1:11](https://youtu.be/PwCSYy-oGsM?t=71))
- **Six pillars, 26 components, governance across all** — Configured pillars cover what exists before the agent runs; runtime pillars cover tasks, execution and output; governance is applied across all of them and covers error tolerance, risk, compliance, observability, drift, accuracy and hallucination, and tone and sentiment. ([3:34](https://youtu.be/PwCSYy-oGsM?t=214))
- **Score each component 0, 1 or 2** — 0 means the component is missing, 1 means it is measurable (automatic or manual), and 2 means it is managed, i.e. tracked and analysed over time. Manual measurement counts the same as automatic. ([5:37](https://youtu.be/PwCSYy-oGsM?t=337))
- **Weight by business importance** — Clusters are weighted so the business-effectiveness view dominates: governance 39%, mandate 26%, platform 12%, outputs 9%, with technical aspects scored but weighted lower. The remaining weights are not stated in the talk. ([6:39](https://youtu.be/PwCSYy-oGsM?t=399))
- **Define the mandate before building** — Set the business outcome target (example: 70% contract renewal), the policy boundaries, the context and documents the agent may reason from, the systems it may touch, who may engage it, and a budget cap so there is no surprise bill. ([11:44](https://youtu.be/PwCSYy-oGsM?t=704))
- **Success criteria must be written with each task** — If a task has no success criteria linked to it, a result such as a renewal cannot be judged later. The agent should log what it is doing and the task input, context and output, and each run ends with one overall success score. ([15:46](https://youtu.be/PwCSYy-oGsM?t=946))
- **Composite score can reverse the containment ranking** — Agent A (80% containment, 20% escalation) scores 83% overall and beats B in each cluster except skills. B had more skills but was weaker on explainability, success tracking and compliance. ([15:46](https://youtu.be/PwCSYy-oGsM?t=946))
- **Re-run agents weekly; a flat dashboard hides drift** — Treat an agent like a hire that is never finished: re-run it weekly on live traffic against a human baseline. A vanity dashboard stayed at 92% all year while the real score fell from 83 to 60. ([17:14](https://youtu.be/PwCSYy-oGsM?t=1034))
- **Measure ROI as freed human time** — Ask what the agent took off the employee's plate and what that time made possible. Example: the agent handles routine balance checks so the banker can spend the morning on the customer who is rethinking their mortgage. ([18:15](https://youtu.be/PwCSYy-oGsM?t=1095))

## Techniques
- **Component scoring with weighted clusters** — Score every component 0 (missing), 1 (measurable, automatic or manual) or 2 (managed, tracked over time). Multiply cluster scores by business-weighted percentages (governance highest) and sum to one number per agent. *When:* Comparing agents, or deciding which business function to automate first with a board or business stakeholders.
- **Mandate-first agent definition** — Before building, write down the business outcome target, the policy boundaries, the documents and context the agent may use, the allowed system endpoints, who may engage it, and a budget cap. Treat the system prompt as only one part of this. *When:* Start of any agent project, during envisioning and when choosing a functional area.
- **Success criteria attached to each task** — When a runtime task is created, store its success criteria with it, and log the task input, required context, the agent's explanation and its output so a single pass/fail can be scored later. *When:* Any agent that takes actions with business outcomes (renewals, refinances, refunds) that must be judged afterwards.
- **Weekly re-run against a human baseline** — Replay live or representative traffic on a schedule, score it against human-handled answers, track the trend, and fix and retest. Drift is measured against the baseline captured at first go-live. *When:* After go-live, as a standing eval rather than a one-off acceptance test.
- **Hybrid accuracy measurement** — Measure hallucination automatically where possible and fill the rest by manual annotation, then combine both into one accuracy figure. *When:* Conversational agents where no automatic ground truth exists for every answer.
- **Central handoff and action-center check** — Check that each agent uses the shared platform services (memory, human handoff, orchestration) rather than building its own, and that people reach all agents through one place. *When:* Organisations running several agents, to keep behaviour consistent and handoffs auditable.
- **Skill-source and granularity review** — For each agent, record whether skills come from a central repository, are built on the fly, or are hand-coded; how granular and discoverable they are; and how many are combined in one prompt. Judge tool use by effectiveness, not count. *When:* Auditing agents that compose skills or have large tool catalogues.
- **Error tolerance set by mode** — Set a higher accuracy target for autonomous agents with no human in the loop. For human-AI collaboration where a person makes the final decision, accept a looser target (the speaker suggests around 60% error tolerance may be fine). *When:* Setting targets before measuring an agent.
- **ROI as freed human time** — Record what work the agent removed from people and what those people did with the freed time, and add that to the scorecard next to cost. *When:* Answering the CFO-style question of what the agent is worth.

## Numbers
- Containment in the illustrative banking example: Intern A 80% (20% escalated), Intern B 96% (4% escalated) ([1:11](https://youtu.be/PwCSYy-oGsM?t=71))
- Framework size: six pillars and 26 components ([3:34](https://youtu.be/PwCSYy-oGsM?t=214))
- Scoring scale per component: 0 missing, 1 measurable, 2 managed ([5:37](https://youtu.be/PwCSYy-oGsM?t=337))
- Cluster weights: governance 39%, mandate 26%, platform 12%, outputs 9% ([6:39](https://youtu.be/PwCSYy-oGsM?t=399))
- Example target: 70% contract renewal as the agent's business outcome ([11:44](https://youtu.be/PwCSYy-oGsM?t=704))
- Example hallucination rate: about 3%, partly automatic and partly manual ([10:38](https://youtu.be/PwCSYy-oGsM?t=638))
- Composite score: Agent A 83% overall, beating Agent B despite lower containment ([15:46](https://youtu.be/PwCSYy-oGsM?t=946))
- Vanity dashboard flat at 92% all year, while the weekly-measured real score slid from 83 to 60 ([18:15](https://youtu.be/PwCSYy-oGsM?t=1095))
- Industry containment benchmarks (Druid 2026 AI adoption report): financial services 80%, healthcare 87%, HR and IT 93%, higher education 99% ([19:39](https://youtu.be/PwCSYy-oGsM?t=1179))
- Benchmark data source: 15 months of anonymised production agent data; the report is free to download ([20:36](https://youtu.be/PwCSYy-oGsM?t=1236))

## Hot takes
- A containment rate on its own is a vanity metric; a higher number can mean the agent skipped the handoffs that create revenue.
- Higher containment in higher education is not better than banking; banking has simply designed more handoff into its agents.
- Hiring an agent is never finished, so the interview-once model of evaluation is wrong.
- The ROI question should be answered by the human time the agent freed up, not by whose job it removes.
- The agent with the most tools is not the best one; effective tool use is what counts.

## Relevance to our work
- **agentos** (2/3): The talk's mandate pillars (budget cap, system allowlist, who may engage, audit logging of reasoning and calls) map to AgentOS L1 budgets and audit log, and its per-component 0/1/2 scoring could give AgentOS a maturity view across its pillars. → *Add a per-agent scorecard to AgentOS evals that scores each pillar 0/1/2 (missing/measured/managed) and weights governance highest, reported beside raw containment-style metrics.*
- **prosharness** (2/3): ProsHarness runs long checkpointed agent tasks, and the talk's rule of storing success criteria with each task so a resumed or finished run can be judged fits that directly. → *Require each ProsHarness task or checkpoint to carry explicit success criteria written at creation, and judge the final output against them.*
- **general** (1/3): Matches the recurring interest in evals for agents: the talk argues for standing, weekly evals against a human baseline rather than one-off checks. → *Re-run key agent evals on a schedule against a human-labelled baseline and log drift over time, instead of a single pass/fail.*

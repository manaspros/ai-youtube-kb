# Using RL Agent to Detect and Remediate ETL Pipeline Failures - Anna Marie Benzon

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `LrGCT7G_rU8` · [watch](https://youtu.be/LrGCT7G_rU8) · **date:** 2026-07-18 · **length:** 14:41 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Anna Marie Benzon · **orgs:** ?
- **topics:** data-engineering, agent-architecture, security-guardrails, evals · **tags:** ETL failures, self-healing pipelines, reinforcement learning, tabular Q-learning, contextual decision, safety override, escalation as outcome, ablation, multi-seed evaluation, shadow mode, AWS Glue, EventBridge, Lambda

> Anna Marie Benzon presents a capstone ETL remediation agent: deterministic rules detect facts, tabular Q-learning picks among six bounded actions, and an external safety layer can force escalation. Results are from synthetic benchmarks.

## Summary
The talk describes an event-triggered agent that responds to failed AWS Glue ETL jobs. An EventBridge event triggers a Lambda that gathers read-only evidence from CloudWatch logs and the Glue Data Catalog, classifies the failure, scores risk, and proposes one of six actions (retry, coerce, rollback, quarantine, escalate, log). A safety layer outside the learned policy checks each proposal before an executor acts, and every step is written to an audit record. The speaker separates three concerns: deterministic rules for observable facts, a small tabular Q-learning policy for choosing among bounded actions, and guardrails that hold authority. On a synthetic benchmark across 30 seeds, the system reported about 74.6% simulated success, 88.6% non-escalation, and roughly 5.2 minutes of resolution time against a modeled 2.5-working-day manual baseline. The ablations show the RL policy matched a hand-written deterministic policy, so most of the reliability came from structured state, sensible logic, and the external safety override. The speaker says production validation and shadow-mode deployment are the next steps.

## Key ideas
- **Split the system into three layers: rules for facts, learning for bounded choices, guardrails for authority.** — Deterministic anomaly rules (field disappeared, type change, null rate over threshold) establish what happened. A Q-learning policy chooses the action. A safety override sits outside the policy so a policy update cannot redefine its own authority. ([3:27](https://youtu.be/LrGCT7G_rU8?t=207))
- **Keep the learned component small and inspectable.** — The state is compact (failure category, risk level, retry count, drift severity, data quality condition) and the action set has six options. Tabular Q-learning fits because the spaces are small and each decision can be read from the Q-table. Each incident is treated as a single-step contextual decision, not a long control task. The speaker argues that ML-ready does not mean ML-required. ([4:51](https://youtu.be/LrGCT7G_rU8?t=291))
- **Escalation is a valid action, and the optimization target should not reward avoiding it.** — A critical anomaly with a passive proposal (such as log) is converted to escalation. High-risk or unknown cases are escalated. The speaker says that if success is measured only by non-escalation, the optimization target is wrong. ([6:17](https://youtu.be/LrGCT7G_rU8?t=377))
- **Separate policy safety from implementation capability and record what was not executed.** — In one failure path, the policy proposed schema coercion, the safety layer did not fire, and the executor found that automatic coercion was unavailable for that case. The system logged the proposed action, reported that execution was unavailable, and routed the incident to manual review instead of pretending the fix happened. ([7:41](https://youtu.be/LrGCT7G_rU8?t=461))
- **Ablations show where the reliability came from.** — The RL policy matched the equivalent deterministic policy (difference of 0 points within a 0.19-point CI). Deterministic selection beat random selection by about 15.6 points. The safety override cut non-escalation by about 15 points, which the speaker calls intentional. Reliability came mainly from structured state, sensible logic, and external safety, not from RL alone. ([10:30](https://youtu.be/LrGCT7G_rU8?t=630))
- **Honest scope and a concrete path to production.** — Results come from synthetic scenarios, and the agent responds after a failure signal rather than predicting one. Some actions are simulated. Online learning in production would need approval gates, version policies, and rollback. The next step is shadow mode on real incident traces, comparing recommendations with human decisions before any execution authority is granted. ([11:57](https://youtu.be/LrGCT7G_rU8?t=717))

## Techniques
- **Event-triggered diagnose-decide-act-verify loop** — A job-failed event triggers a function. The function gathers read-only evidence (logs, schema metadata), classifies the failure, scores operational risk, asks the policy for one bounded action, passes it through a safety check, runs the action via the platform API, re-runs and validates the job, and writes every step to an audit store. *When:* Recurring, recognizable pipeline failures where handoff latency is the main cost and the remediation set is small and reversible.
- **Rules for facts, learning for choices, guardrails for authority** — Use deterministic detectors (schema profiler, drift detector, data quality checks, log-pattern classifier, risk scorer) for anything directly measurable. Use the learned policy only to pick among bounded actions. Put a hard override outside the policy that converts risky passive choices into escalation. *When:* Agent or ML decisions that can trigger real operational actions and must stay auditable.
- **Tabular Q-learning over a small discrete state** — Encode the incident as a compact discrete state and a fixed action list. Treat each incident as a one-step contextual decision. Inspect the table directly to explain any chosen action. *When:* Small state and action spaces where interpretability matters more than sophistication, and the policy must be easy to audit.
- **Propose, check, execute, and record separately** — Log each proposal, the safety verdict, the execution result, and the validation outcome as separate records. Represent actions that are safe in principle but unavailable in the environment as their own result, not as success. *When:* Any agent that acts on production systems and needs an honest audit trail.
- **Multi-seed evaluation with baselines and confidence intervals** — Repeat the benchmark across many seeds (here 30, seeds 42 to 71). Report means with 95% CIs. Compare against a random baseline, a deterministic rule baseline, and ablations that remove the learned policy or the safety override. *When:* Before claiming an agent or policy works; a single favorable run is treated as a demo, not evidence.

## Numbers
- Manual recovery baseline modeled at roughly 2.5 working days per incident (216,000 seconds). ([1:29](https://youtu.be/LrGCT7G_rU8?t=89))
- Rule-based anomaly detector: precision 1.0, recall 0.8, F1 0.889 on the controlled benchmark. ([9:02](https://youtu.be/LrGCT7G_rU8?t=542))
- Mean resolution time about 5.24 minutes for cases the RL-guided workflow resolved successfully. ([9:02](https://youtu.be/LrGCT7G_rU8?t=542))
- Simulated success rate 74.63% plus or minus 1.51 points across 30 runs. ([9:02](https://youtu.be/LrGCT7G_rU8?t=542))
- Non-escalation rate 88.63% plus or minus 0.89 points across 30 runs. ([9:02](https://youtu.be/LrGCT7G_rU8?t=542))
- Speaker reports about a 99.85% MTTR reduction versus the modeled manual baseline, within the benchmark only. ([9:02](https://youtu.be/LrGCT7G_rU8?t=542))
- RL policy vs equivalent deterministic policy: 0 percentage-point difference within a 0.19-point CI. ([10:30](https://youtu.be/LrGCT7G_rU8?t=630))
- Deterministic action selection beat random selection by 15.63 points. ([10:30](https://youtu.be/LrGCT7G_rU8?t=630))
- Enabling the safety override reduced non-escalation by about 15.03 points, intentionally. ([10:30](https://youtu.be/LrGCT7G_rU8?t=630))
- Example log classifier detection of a date-format incompatibility at 0.9 confidence. ([6:17](https://youtu.be/LrGCT7G_rU8?t=377))

## Hot takes
- If success is measured only by non-escalation, the optimization target is wrong; escalation is a capability.
- A single favorable run is a demo, not evidence.
- Perfect precision does not mean perfect detection.
- Reliability came primarily from structured state, sensible logic, and external safety constraints, not from RL alone.

## Tools mentioned
AWS Glue, Amazon EventBridge, AWS Lambda, Amazon CloudWatch, AWS Glue Data Catalog, Amazon S3

## Relevance to our work
- **prosharness** (2/3): ProsHarness plan, critique, debate, and phone approvals follow the same propose, guard, execute split, and checkpoints could record blocked or unavailable actions the way the talk does. → *Keep ProsHarness approval and guard logic as code outside the planner, and record proposed-but-blocked or unavailable actions as distinct events in checkpoints.*
- **agentos** (1/3): L2C exec-gate guardrails and L2D skill governance need an authority boundary outside any learned or LLM policy, and the talk shows that pattern with ablations. → *When adding a learned or LLM decision to an AgentOS guardrail path, keep the hard override in code outside the policy, and add a no-override ablation to the benchmark.*
- **general** (1/3): Data quality and entity resolution overlap with the talk's deterministic-facts-first approach and multi-seed, baseline-driven evaluation. → *Before reporting any entity-resolution gain as evidence, run repeated seeds and compare against a simple rule baseline with confidence intervals, as the talk does.*

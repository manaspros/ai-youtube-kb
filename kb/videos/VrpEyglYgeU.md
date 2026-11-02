# In the Land of AI Agents, the Verifiers Are King — Tariq Shaukat, Sonar

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `VrpEyglYgeU` · [watch](https://youtu.be/VrpEyglYgeU) · **date:** 2026-08-18 · **length:** 18:53 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Tariq Shaukat · **orgs:** Sonar, METR, Carnegie Mellon University, KPMG, EY
- **topics:** testing-verification, pr-code-review, context-engineering · **tags:** verification, code-quality, technical-debt, agent-centric-development-cycle, guide-verify-solve, zero-trust-verification, metr-time-horizon, coding-agent-productivity, sonar-vortex, static-analysis, agentic-review

> Sonar's CEO argues AI coding agents need verification built into the loop: guide them with context and constraints, layer algorithmic and agentic checks, and keep the codebase clean. It is a vendor talk, and its numbers are self-reported.

## Summary
Tariq Shaukat, CEO of Sonar, says AI-generated output often looks correct without being correct, and that coding agents produce bugs, security issues and complexity even when functional tests pass. He cites METR's time-horizon chart, noting that task length falls sharply when the accuracy bar rises from 50% to 80%. He cites a CMU study in which the early 3-5x velocity gain from coding agents fades after about three months while security, maintainability and reliability issues grow. His proposed fix is the "agent-centric development cycle" (guide, verify, solve), run as three loops: an in-agent loop, a CI verification and review loop, and a code-maintenance loop. The talk is mostly a product pitch for Sonar Vortex, and the outcome numbers come from Sonar's own partners and customers.

## Key ideas
- **Plausible output is not correct output, and enterprises need to know which is which.** — The speaker points to hallucinated citations and case law in professional services as evidence that fluent AI output can slip through unchecked. He argues this is a problem in every sector, not only in software. ([1:22](https://youtu.be/VrpEyglYgeU?t=82))
- **Agent time horizons depend heavily on the accuracy bar.** — Per METR's chart, the latest model handles tasks of 16-18 hours at a 50% success rate. Raising the bar to 80% cuts that to about 3.5 hours. The speaker says he would not accept 80% accuracy from a person in a performance review. ([3:49](https://youtu.be/VrpEyglYgeU?t=229))
- **Functional correctness is not enough to judge agent code.** — Sonar benchmarks models on over 4,000 problems and scores functional correctness, complexity, bugs and security separately. Models do well on correctness, but complexity varies and bugs and security issues remain even in the best models. ([5:18](https://youtu.be/VrpEyglYgeU?t=318))
- **Early velocity gains from coding agents can reverse.** — The CMU study the speaker cites found a 3-5x velocity boost that faded after about three months. Over that period, security, maintainability, reliability and complexity issues rose. The speaker's point is that teams build technical debt as fast as they generate code. ([6:41](https://youtu.be/VrpEyglYgeU?t=401))
- **Verification should be designed into the development process, not added as a review at the end.** — The proposed agent-centric development cycle puts code generation at the centre and wraps it in guide, verify and solve steps. The speaker argues that teams who bake verification in get materially better results than teams who treat it as old-school code review. ([8:06](https://youtu.be/VrpEyglYgeU?t=486))
- **Guidance for agents should cover both context and constraints.** — Context means architectural awareness and semantic maps of the repository. Constraints mean allowed and disallowed dependencies, coding standards, guardrails and the target architecture. Sonar reports more than 30% fewer tokens per task with this setup, and says it works because the agent navigates more easily. ([9:30](https://youtu.be/VrpEyglYgeU?t=570))
- **Use several different models and checks in a zero-trust, multi-layer verifier.** — The speaker argues that each model has its own biases, so verification should use different models and techniques. It combines algorithmic checks (data flow, control flow, known patterns, secrets) with agentic checks (intent, business logic, unknown unknowns). Sonar reports 44% fewer AI-derived production outages for customers who use this approach. The figure is self-reported. ([11:54](https://youtu.be/VrpEyglYgeU?t=714))
- **Keep a separate code-maintenance loop, because agents need clean code too.** — The speaker says agents must understand the codebase before they can change it, so clean code helps them. He reports lower token and reasoning use on cleaned codebases than on messy ones, and says the benefit compounds over time. ([13:20](https://youtu.be/VrpEyglYgeU?t=800))
- **Think of verification as three loops, and expect the benefits or the damage to compound.** — The loops are an in-agent loop with context and inner-loop checks, a CI loop with agent PR review, evals and quality gates, and a maintenance loop with remediation agents. The speaker says neglecting verification leads to a downward spiral. He cites a large bank that reportedly cut issues by 92% with this approach. ([14:47](https://youtu.be/VrpEyglYgeU?t=887))

## Techniques
- **Guide with context and constraints** — Give agents a semantic map of the repository and its architecture. Also give them explicit rules: allowed and disallowed dependencies, coding standards, guardrails and the target architecture. Write these where the agent reads them at the start of a task. *When:* Large or legacy codebases, where agents otherwise spend many tokens exploring. The speaker reports over 30% fewer tokens.
- **Zero-trust multi-layer verification** — Run more than one verifier on agent output, and use different models for each. Combine deterministic analysis (data flow, control flow, secrets, known bug patterns) with an LLM check on intent and business logic. *When:* Agent-written code that will reach production, where a single model or a single check is not trusted to catch everything.
- **Verification inside the agentic loop** — Have the agent run verification while it works, and let it fix what the checks find before it reports done. Keep the agent's own feedback loop short. *When:* Any agent that writes code autonomously. The aim is to catch problems in minutes rather than in review.
- **CI verification loop with agent PR review and quality gates** — Run agent-based review, evals and quality gates in CI on every pull request. Treat the gate results as pass or fail for merging. *When:* Teams that already merge many agent-written pull requests and need review speed to keep up with generation speed.
- **Scheduled code-maintenance and remediation agents** — Run agents on a recurring basis to find and fix technical debt, and track the codebase's complexity and issue counts over time. *When:* Codebases where agent output accumulates debt faster than people can review it. The speaker's claim is that gains compound over repeated runs.

## Numbers
- METR time horizon for the latest model: about 16-18 hours of human-equivalent work at a 50% success rate (preview benchmark, per the speaker). ([3:49](https://youtu.be/VrpEyglYgeU?t=229))
- The same model's time horizon at 80% accuracy: about 3.5 hours. ([3:49](https://youtu.be/VrpEyglYgeU?t=229))
- Sonar benchmark uses over 4,000 problems and measures functional correctness, complexity, bugs and security. ([5:18](https://youtu.be/VrpEyglYgeU?t=318))
- CMU study: 3-5x early velocity gain from coding agents, which fades after about three months, with rising security, maintainability, reliability and complexity issues. ([6:41](https://youtu.be/VrpEyglYgeU?t=401))
- Guide (context and constraints) reduces tokens used per task by over 30% in Sonar's testing. ([10:55](https://youtu.be/VrpEyglYgeU?t=655))
- Customers and partners using multi-layer verification report AI-derived production outages 44% less frequent (self-reported). ([11:54](https://youtu.be/VrpEyglYgeU?t=714))
- A large bank reportedly saw a 92% reduction in issues with the guide, verify and solve approach inside agentic loops (self-reported). ([16:15](https://youtu.be/VrpEyglYgeU?t=975))

## Hot takes
- Speaker: 80% accurate output would not pass a performance review, so 80% is not enterprise grade for coding agents.
- Speaker: the early velocity gain from AI coding agents does not last without verification; teams build technical debt as fast as they generate code.
- Speaker: verification should be built into the development system, not treated as an afterthought or as old-school code review.
- Speaker: agents care about clean code because they have to understand the codebase to change it.

## Tools mentioned
Sonar Vortex (product launched the day before the talk, per the speaker), METR time-horizon benchmark chart, Models named: Mythos, Fable, GPT 5.5

## Relevance to our work
- **prosharness** (2/3): ProsHarness already has plan, critique and debate steps. The talk's multi-model verification and in-loop checks suggest a verifier step before a checkpoint is marked done, and a maintenance pass for the repository. → *Add a verifier step before a checkpoint is marked done: a different model reviews the diff, and deterministic checks cover secrets, dependency rules and complexity. Measure whether this lowers the defect rate of agent-written changes.*
- **agentos** (1/3): AgentOS aims to prove itself with benchmarks and correctness checks. The talk's point that functional pass rates hide complexity, security and maintainability problems applies to how AgentOS measures agent output, but the talk has no AgentOS-specific detail. → *When benchmarking agent-written code, report complexity and security findings next to functional pass rate, not pass rate alone.*

# Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `CTLa_p6iOiY` · [watch](https://youtu.be/CTLa_p6iOiY) · **date:** 2026-08-18 · **length:** 17:28 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Pierluca D'Oro · **orgs:** Programma Labs, Meta Superintelligence Labs
- **topics:** evals, voice-multimodal, testing-verification · **tags:** computer use, benchmarks, replay agent, pass@k, confidence intervals, environment design, DigiWorld, statistical rigor

> Pierluca D'Oro (Programma Labs) shows that static computer-use benchmarks can be gamed by replaying recorded successful traces, and argues for varied environments plus hierarchical confidence intervals.

## Summary
The speaker introduces a "replay agent": record a frontier model's successful action traces on a benchmark, then replay them blindly. On OS World and Mobile World this script matches or beats the model it was extracted from, because static benchmarks are deterministic. He argues that pass@k, a common computer-use metric, reduces to measuring that same replay exploit on a deterministic environment. He proposes PRISM design principles for environments: stochastic variation, validity checking for every combination, sandboxing, privileged verifiers, and faithful realism. His benchmark DigiWorld has 15 Android apps, 387 verified scenarios and about 3.2M configurations, produced by a compiler-like system that composes task templates, verifiers, mock data and UI base states and rejects invalid combinations. Replay agents score poorly on it, and frontier models turn out to be fragile to changes in start screen and theme. For statistics, he separates action stochasticity from environment variation and says rollout-only confidence intervals cover the true score only about 17-20% of the time, versus a nominal 95%. A hierarchical CI fixes this and can stop a team from making an overconfident model choice. The talk ends with a company pitch and a hiring call. The transcript spells the speaker "Pierluca Loro", which the title slide corrects to D'Oro.

## Key ideas
- **Blind replay of recorded successful traces can match or beat the frontier model they came from on standard computer-use benchmarks.** — A script under 1 MB replays the actions of a successful run for each task. On OS World and Mobile World it scores the same as or better than the source model, so static deterministic benchmarks are gameable. ([0:08](https://youtu.be/CTLa_p6iOiY?t=8))
- **pass@k on a deterministic environment is equivalent to scoring a replay agent.** — The speaker says he proves formally that pass@k on a fixed environment measures the replay exploit. He calls it a metrification of that exploit and says the metric should feel suspicious. ([2:58](https://youtu.be/CTLa_p6iOiY?t=178))
- **Environments need stochastic variation plus a validity check for every combination.** — The PRISM principles cover multifactorial variation (data, appearance, initial state), verification of each generated combination, sandboxing, privileged verifiers, and faithful reproduction of real systems. ([4:14](https://youtu.be/CTLa_p6iOiY?t=254))
- **Coding agents can generate variations, but volume is not validity.** — Generating a lot of software does not give a usable environment. The scalable approach is to generate many configs and have a system reject the broken ones, so good software engineering is the core work. ([6:52](https://youtu.be/CTLa_p6iOiY?t=412))
- **Build variants with a compiler-like pipeline of template, verifier, mock data and base state.** — A parameterized task template comes with its verifier and the data it needs. A visual compiler combines these with a base UI state and emits only valid configurations. ([8:08](https://youtu.be/CTLa_p6iOiY?t=488))
- **Frontier models are fragile to benign environment changes.** — On the variant benchmark, replay agents perform poorly. Frontier models also vary a lot in the worst case when only the start screen or the app theme changes, which a robust agent should not do. ([9:30](https://youtu.be/CTLa_p6iOiY?t=570))
- **There are two variance sources, action randomness and environment randomness, and both need to be measured.** — Repeated runs vary in action sequence. Across task variants, environment variation adds a second layer. A hierarchical methodology is needed to capture both. ([10:52](https://youtu.be/CTLa_p6iOiY?t=652))
- **Rollout-only confidence intervals are badly overconfident.** — The speaker reports about 17-20% coverage for a nominal 95% interval when only rollouts are used. Respecting the benchmark hierarchy gives the intended coverage. ([12:17](https://youtu.be/CTLa_p6iOiY?t=737))
- **Overconfident intervals lead to expensive wrong model choices, and an honest interval should say it is not yet sure.** — He gives an example of 1M tasks, a roughly 4% mismatch in real performance, and about $12 per mistake, which adds up to hundreds of thousands of dollars in a month. A reliable interval would tell the team to spend more on evaluation first. ([13:33](https://youtu.be/CTLa_p6iOiY?t=813))

## Techniques
- **Replay-agent baseline check** — Record successful traces from a strong model and replay them blindly on the benchmark. If the replay scores close to the model, the benchmark is gameable and the score is not informative. *When:* Before trusting a new static or deterministic agent benchmark or a pass@k number.
- **PRISM environment design checklist** — Design for stochastic variation (data, appearance, initial state), validate every generated combination, sandbox the environment, expose privileged verifiers, and keep the reproduction faithful to the real system. *When:* When building or auditing an eval environment for computer-use or other agents.
- **Template plus verifier config compiler** — Write parameterized task templates, each with its own verifier and mock data. Combine them with base UI states, check each combination, and keep only the valid configs. *When:* When you need thousands of diverse, verified test scenarios and do not want to hand-write each one.
- **Hierarchical confidence intervals** — Compute intervals that respect the benchmark's structure, covering run-level randomness and task or environment variant variance, rather than pooling rollouts. *When:* When choosing between models or configs based on eval scores with multiple runs and variants.
- **Interval-gated model decisions** — Only decide when the interval is tight enough. If it overlaps, spend more evaluation budget before choosing. *When:* When a wrong model-selection decision would be costly.

## Numbers
- A replay script built from successful traces is under 1 MB and matches or beats the source frontier model on OS World and Mobile World. ([0:08](https://youtu.be/CTLa_p6iOiY?t=8))
- DigiWorld: 15 Android apps, 387 verified scenarios, about 3.2 million configurations. ([5:36](https://youtu.be/CTLa_p6iOiY?t=336))
- Rollout-only 95% confidence intervals achieve about 17-20% real coverage. ([12:17](https://youtu.be/CTLa_p6iOiY?t=737))
- Example cost: 1 million tasks, about 4% mismatch in real performance, about $12 per mistake, so hundreds of thousands of dollars per month. ([13:33](https://youtu.be/CTLa_p6iOiY?t=813))
- Talk length is 17:28. ([0:00](https://youtu.be/CTLa_p6iOiY?t=0))

## Hot takes
- Replay agents that blindly play recorded traces should not be allowed to beat frontier models on computer-use benchmarks.
- pass@k on deterministic computer-use environments is effectively a measure of the replay exploit.
- Most published computer-use benchmark error bars are overconfident, and the speaker says that can cost real money.
- Non-rigorous benchmarks mislead the whole field, not just the team running them.

## Relevance to our work
- **agentos** (1/3): AgentOS has RAGAS evals and Locust load tests, but no computer-use or trajectory-level benchmark. The talk's CI and replay-baseline ideas apply only if AgentOS adds agent-level evals. → *When AgentOS evals report a single score, add a replay or trace-replay baseline and a bootstrap or hierarchical CI over task variants before comparing configs.*
- **prosharness** (1/3): ProsHarness runs repeated Claude Code agent runs and compares plan or critique variants. Run-level variance and task-level variance are the same problem the talk describes, though not computer use. → *When comparing harness variants on repeated Claude Code runs, report a hierarchical CI over tasks and runs, and do not pick a winner when the intervals overlap.*

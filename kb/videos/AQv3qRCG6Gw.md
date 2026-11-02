# Reinforcement Learning without Verifiable Rewards — Will Brown, Prime Intellect

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `AQv3qRCG6Gw` · [watch](https://youtu.be/AQv3qRCG6Gw) · **date:** 2026-08-18 · **length:** 19:27 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Will Brown · **orgs:** Prime Intellect
- **topics:** training-finetuning-rl, evals, observability · **tags:** reinforcement-learning, rlvr, reward-hacking, environments, llm-as-judge, rubrics, continual-learning, simulators, synthetic-tasks, production-traces, difficulty-calibration

> Will Brown (Prime Intellect) on running RL when no verifiable reward exists: manufacture supervision from grounding, judges, production traces and learned simulators, and keep humans on the top-level decisions.

## Summary
Will Brown argues that most real agent tasks lack verifiable rewards, so RLVR does not cover them. He frames an environment as task plus harness plus rewards, and says the same objects serve as evals, synthetic SFT data, on-policy distillation and prompt optimization. His main method is to manufacture signal: grounding in source material (compare with and without it), LLM judges, and scaling search over tasks, worlds and rubrics. Production traces are the seed distribution, since they show what users actually ask for even without labels. He recommends working backwards from a known-reachable end state, such as a document or a PR with pieces removed, and building learned simulators for tools and web apps whose backends you cannot control. Reward hacking is handled by mining hacks in hindsight, which judges catch well even when the model is not told to avoid them. He closes with an online loop of generate, solve, synthesize and gate on pass rate, and says humans should decide only the highest-level goals. The talk is a conceptual overview with a recap of Prime Intellect blog work; it gives no hard benchmark numbers.

## Key ideas
- **Environments and evals are the same object** — An environment is a task, a harness and a reward. The same object can be used for RL, synthetic SFT data, on-policy distillation, prompt optimization, or as a testbed for agents and harnesses. Environment design and eval design should be one activity. ([4:06](https://youtu.be/AQv3qRCG6Gw?t=246))
- **Signal can be manufactured without labels** — Three sources are named: grounding (a with/without-source A/B gap gives a learnable capability gap), LLM judges that spend compute to decide if an action was good, and scaling search over tasks, worlds and criteria. ([8:32](https://youtu.be/AQv3qRCG6Gw?t=512))
- **Production traces are the seed task distribution** — Traces from a deployed agent (user prompts, orchestrator-to-subagent calls) show the real distribution even before any labels exist. They tell you what to look for and anchor the environments. ([9:31](https://youtu.be/AQv3qRCG6Gw?t=571))
- **Work backwards from a reachable end state** — Verify the easy upstream version first, then learn the hard task. Examples: generate QA pairs from documents and throw away the search, or take a finished PR, remove pieces, and train the agent to reach that known end state. ([10:29](https://youtu.be/AQv3qRCG6Gw?t=629))
- **Learned simulators for uncontrollable backends** — For MCP tools, CLI tools and web apps where the backend cannot be programmed, learn a simulator. Ground it in production traces and iterate sim versus real. A controllable simulator lets you plant the answer and reverse-engineer a verifiable task. ([12:45](https://youtu.be/AQv3qRCG6Gw?t=765))
- **Judges distil search into rubrics, then audit cheaply** — Ask several models to agree on what went wrong, use hindsight to find the failure, and turn it into rubric questions. Cheaper audits then use those rubrics, and new tasks are written to target the failure modes. ([12:45](https://youtu.be/AQv3qRCG6Gw?t=765))
- **Reward hacks show up in hindsight and should be mined** — Hacks can appear only once RL runs. Judges are good at spotting obvious hacks even when the rollout did not avoid them. Keep a corpus of hacks, fix the reward or the environment, and validate with a training run. ([14:52](https://youtu.be/AQv3qRCG6Gw?t=892))
- **Online loop gated by pass rate, with humans at the top** — The loop generates, solves and synthesizes tasks, then gates on pass rate so tasks are neither too easy nor too hard. Small runs during environment design, plus metrics on tool-call types, help. Humans make only the highest-level goal calls. ([16:04](https://youtu.be/AQv3qRCG6Gw?t=964))

## Techniques
- **Environment as the shared unit (task + harness + rewards)** — Package each task with its harness and scoring rule as one object. Reuse that object for evals, synthetic data for SFT, on-policy distillation and prompt search, rather than building separate eval and training assets. *When:* When you are building evals and also planning any training or prompt optimization on the same agent.
- **With/without grounding as a supervision gap** — Run the same task with and without the source material in context. Where the model does better with it, the gap is the signal to learn from. *When:* When you have documents or a corpus but no labels.
- **Backward construction from a reachable end state** — Start from a completed artifact (a document, PR diff, test suite), remove parts, and create tasks that ask the agent to rebuild them. The end state is known to be reachable, so the task can be verified. *When:* When the domain has finished artifacts such as code repos, documents or reports.
- **Trace-seeded task mining** — Sample real production inputs and inter-agent calls, then generate tasks and questions from them. Treat the traces as the distribution to target, even without labels. *When:* When an agent is already deployed and you want evals or training tasks that match real usage.
- **Judge-to-rubric distillation** — Spend heavy compute (multiple models, search over traces) to find failures in hindsight. Convert the findings into a small set of rubric questions. Use the rubric for cheap routine auditing and to generate tasks for each failure mode. *When:* When a judge is too expensive to run on everything but you can afford an offline pass to learn what to check.
- **Pass-rate gated task generation** — Generate candidate tasks, sample several rollouts per task, and keep tasks where the pass rate is between easy and impossible. Iterate on the generator and repeat. *When:* When you need a training or eval set with difficulty that is well calibrated for RL.
- **Learned simulator of an uncontrolled tool or site** — Build a simulated backend on universal infrastructure, ground it in production traces, and iterate between simulator and real system to raise fidelity. Use it for RL where the real backend cannot be verified or reset. *When:* When the tools are MCP servers, CLIs or web apps you do not control and need many rollouts from.
- **Reward-hack corpus and small-run validation** — Log each reward hack found in hindsight, then patch the rewards or environment. Confirm fixes with small training runs on one environment, and log tool-call-type metrics that judges label from traces to watch behavior change. *When:* During environment design, before scaling up an RL run.

## Numbers
- Standard handcrafted agent benchmarks are often a few hundred tasks, built over months with experts and data vendors, and are not scalable to open-ended tasks (no figure given beyond 'a few hundred'). ([5:10](https://youtu.be/AQv3qRCG6Gw?t=310))
- Judge agreement is used as a signal: asking seven different models and checking whether they agree a step is wrong (no accuracy figure given). ([12:45](https://youtu.be/AQv3qRCG6Gw?t=765))
- The talk reports 'great uplift' on popular tool-use benchmarks from an online generate/solve/synthesize loop, but gives no numbers in the talk. ([17:08](https://youtu.be/AQv3qRCG6Gw?t=1028))

## Hot takes
- Environments and evals are really the same thing; RL is only one use of them.
- Work backwards: plant the answer in a controllable simulator and make the task verifiable there, even if production is not verifiable.
- RL is good for refining skills but poor at adding dense new knowledge; blend it with supervised signal from the environment.
- Reward hacks are usually obvious in hindsight to a judge, even though the model does not avoid them when told not to.

## Tools mentioned
Prime Intellect PrimeRL training framework, Prime Intellect verifiers and task sets, Prime Intellect Lab (hosted training and evals), GRPO / REINFORCE policy-gradient methods (named in passing), MCP servers, CLI tools and web apps (as simulator targets)

## Relevance to our work
- **agentos** (2/3): SkillForge's open question is the success signal for skill-worthiness. The talk gives grounded with/without comparison and judge-derived rubrics as ways to get a signal from traces with no labels. → *Prototype a SkillForge success signal: run mined telemetry tasks with and without a candidate skill in context, and score the difference with a judge rubric built from hindsight failure review.*
- **general** (2/3): Directly relevant to agent evals: treating a task, harness and rubric as one object, calibrating difficulty with pass rates, and mining reward hacks all apply to any agent eval set. → *Add a pass-rate band to the agent eval set so only tasks solved sometimes (not always, not never) are kept, and log judge-found failure modes as new rubric questions.*

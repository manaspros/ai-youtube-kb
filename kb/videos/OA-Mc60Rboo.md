# Beating RL With Reflection: GEPA and Optimize Anything — Lakshya A. Agrawal, GEPA

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `OA-Mc60Rboo` · [watch](https://youtu.be/OA-Mc60Rboo) · **date:** 2026-09-27 · **length:** 21:28 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Lakshya A. Agrawal · **orgs:** GEPA, AMD, Databricks, Snorkel, Dropbox, Shopify, OpenAI
- **topics:** skills-self-improvement, evals, context-engineering, training-finetuning-rl · **tags:** GEPA, reflective-prompt-optimization, pareto-search, optimize-anything, agent-skills, llm-as-judge, sample-efficiency, GRPO-comparison, harness-optimization, data-flywheel

> GEPA's Lakshya Agrawal explains reflective, text-space optimization: LLMs read full rollout traces and rewrite prompts, skills or harness code, with a Pareto pool, beating GRPO on sample efficiency.

## Summary
The speaker argues that RL with verifiable rewards wastes most of each rollout, since it keeps only a scalar score and ignores reasoning, tool calls and error messages. His proposal is reflective optimization: an LLM reads the full trace plus domain feedback, reflects on what failed, and rewrites a text artifact such as a prompt, agent file or skill. A Pareto pool keeps every candidate that wins on at least one example, which he says avoids the local optima a greedy LLM loop gets stuck in. He claims that with three examples and one reflection round, the method beat GRPO after 25,000 rollouts, and that it works on prompts, whole agent harnesses, CUDA kernels, scheduling heuristics and repo skills. He presents the open-source API "optimize anything" with three modes (single task, multitask, generalization). He also says that better models make precise prompts more valuable, and that an LLM judge can be tuned from about 50 annotated production traces to form a data flywheel. Most numbers are the speaker's own results from his group and partners, and the talk is promotional for GEPA.

## Key ideas
- **RL with verified rewards is sample-inefficient because it throws away most of each rollout** — GRPO turns each rollout into one scalar reward. The speaker says the chain of thought, tool calls and tool error messages carry diagnostic information that is never used. ([0:08](https://youtu.be/OA-Mc60Rboo?t=8))
- **Reflect in text space instead of making small weight updates** — An LLM reads the whole trace, says what worked and what did not, and can call tools such as retrieval during reflection. A single natural-language edit to a prompt can change behavior more than many tiny gradient steps. ([2:54](https://youtu.be/OA-Mc60Rboo?t=174))
- **Reflective optimization beats GRPO on sample efficiency (speaker's claim)** — With three data points and one reflection round, the method roughly doubled GRPO's gains, which had needed 25,000 rollouts. Running longer widened the gap. The speaker says the optimized model was an 8B-class open model with no external teacher. ([4:13](https://youtu.be/OA-Mc60Rboo?t=253))
- **Pareto candidate pool beats greedy LLM improvement loops** — A plain loop keeps only the best prompt and gets stuck in a local optimum. Keeping every candidate that wins on any one training example keeps the search balanced. The speaker reports about twice the gains of the loop across four benchmarks. ([8:07](https://youtu.be/OA-Mc60Rboo?t=487))
- **Evaluators should return rich side information, not just a score** — The evaluator can return compiler errors, profiler output, tool error messages, expert notes, SLA violations or documentation. The reflector uses this text to explain failures and propose fixes. The speaker's example is a prompt that learned to avoid a vendor library that did not work on new hardware. ([10:59](https://youtu.be/OA-Mc60Rboo?t=659))
- **Anything that can be written as text and scored can be optimized** — The speaker's examples include CUDA kernels, numeric parameters serialized as text, whole agent harness files, and cloud scheduling policies scored by cost or SLA. The same loop handles all of them. ([10:59](https://youtu.be/OA-Mc60Rboo?t=659))
- **Skills learned on a cheap model can transfer to a stronger model** — A repo-specific skill was optimized using GPT-5 mini, then applied to Claude Sonnet 4.5. It raised accuracy and cut resolution time by about half, because skills hold repo layout, test commands and build details. ([15:01](https://youtu.be/OA-Mc60Rboo?t=901))
- **Learn the LLM-judge eval from about 50 annotated production traces** — Humans annotate roughly 50 agent trajectories with detailed feedback. The method then optimizes the judge prompt against those labels, and the judge drives agent optimization. The speaker calls this a data flywheel that teams already run. ([18:46](https://youtu.be/OA-Mc60Rboo?t=1126))

## Techniques
- **Reflective prompt / artifact optimization loop** — Run the pipeline on a few examples, collect feedback (traces, tool outputs, errors, human notes), ask an LLM or agent to reflect and propose a revised text artifact, score it, and repeat. *When:* The score is sparse, rollouts are slow or expensive, and the failure information is in the trace text.
- **Pareto candidate pool selection** — Keep every candidate that is best on at least one training example. Choose parents from the pool instead of always taking the top scorer. *When:* Greedy self-refinement stalls at a local optimum and the search budget is being spent on dead ends.
- **Actionable side information from the evaluator** — Return a free-form dict from the fitness function, including compiler and profiler messages, tool errors, expert feedback or docs, and pass it to the reflector. *When:* The domain already emits diagnostic text (compilers, profilers, job traces, SLA logs) that a score alone discards.
- **Three optimization modes in one API** — Single-task mode for one problem, multitask search for related problems that share information, and generalization mode for a training set with unseen deployment queries. *When:* Choose by whether you have one problem, several related problems, or a train/deploy split.
- **Optimize the agent file itself** — Serialize the whole agent (Python or JS harness, including tools, descriptions and control flow) as text and let the optimizer rewrite it against a task score. *When:* Hand-tuning tool descriptions and control flow takes too long, and you can measure task success automatically.
- **Repo skill learning from trajectories** — Feed agent trajectories on a repo into the optimizer and ask for a skill document that would help on similar future problems. Optimize on a cheap model, then test the skill on stronger models. *When:* A coding agent repeatedly spends time rediscovering a repo's layout, test commands or build setup.
- **Judge-then-agent data flywheel** — Collect production traces, have humans annotate about 50, optimize the LLM-judge prompt against those labels, then use the judge as the metric for optimizing the agent. *When:* Subjective quality is hard to score with fixed rules, but you can collect production traces.

## Numbers
- Standard RL and SFT need hundreds of thousands of rollouts or tens of thousands of labeled examples ([0:08](https://youtu.be/OA-Mc60Rboo?t=8))
- One reflection round on 3 examples gave about 2x GRPO's performance gain, and GRPO had used 25,000 rollouts ([4:13](https://youtu.be/OA-Mc60Rboo?t=253))
- Optimizing a prompt takes about 30-60 minutes, depending on the pipeline ([5:31](https://youtu.be/OA-Mc60Rboo?t=331))
- An optimized GPT-4.1 mini beat GPT-4.1 on a math task ([6:56](https://youtu.be/OA-Mc60Rboo?t=416))
- On a new AMD NPU programming task, accuracy rose from 4.25% to 30.52% (about 7x) with no other agent change ([6:56](https://youtu.be/OA-Mc60Rboo?t=416))
- Pareto selection gave about twice the gains of a simple improvement loop across four benchmarks, and about +10% on math benchmarks from prompt optimization ([9:33](https://youtu.be/OA-Mc60Rboo?t=573))
- A 4-line agent on RKGI went from 32.5% to 89.5% for Gemini Flash in 16 reflection rounds ([13:33](https://youtu.be/OA-Mc60Rboo?t=813))
- A two-step agent raised GPT-4.1 nano accuracy by 20% on MATH-500 (transcript says 'MAT500'; the unit is not stated) ([13:33](https://youtu.be/OA-Mc60Rboo?t=813))
- Repo skill on a GPT-5 mini agent: issue resolution 24% to 93% (about 3x) on Go issues ([15:01](https://youtu.be/OA-Mc60Rboo?t=901))
- Same skill on Claude Sonnet 4.5: 100% issue resolution and about 50% less resolution time ([15:01](https://youtu.be/OA-Mc60Rboo?t=901))
- Cloud scheduling policy cost cut by about 40% compared with expert heuristics ([17:34](https://youtu.be/OA-Mc60Rboo?t=1054))
- OCR error rates for leading VLMs cut by about 35% (speaker cites an external report) ([17:34](https://youtu.be/OA-Mc60Rboo?t=1054))
- Databricks: GPT OSS 120B tuned to beat Claude Opus at about 90x lower cost (speaker's account) ([17:34](https://youtu.be/OA-Mc60Rboo?t=1054))
- Judge tuning needs about 50 human-annotated trajectories ([18:46](https://youtu.be/OA-Mc60Rboo?t=1126))

## Hot takes
- Better models make prompt optimization more important, not less, because precise instructions help strong models more than weak ones.
- Reflective text-space optimization is a more sample-efficient route to new capabilities than RL on rollouts, at least for tasks with textual feedback.
- Coding agents should be given optimized skill files so that they do not rediscover repo structure each time, and the skill can be developed on a cheap model.

## Tools mentioned
GEPA (open-source, includes the optimize_anything API and a skill-learning feature), GRPO (used as the RL baseline), Claude Opus, Claude Sonnet 4.5, GPT-5 mini, GPT-4.1, GPT-4.1 nano, Gemini Flash, mini-SWE-agent, Claude Code, Codex, LLM-as-judge

## Relevance to our work
- **agentos** (2/3): SkillForge (L2D) needs a skill-worthiness and success signal; the talk's reflective skill optimization with a Pareto pool addresses both, using test outcomes from agent telemetry. → *Prototype a SkillForge loop: use test pass/fail plus trace text as the success signal, optimize a skill document on a cheap model, and keep a Pareto pool of skill variants.*
- **prosharness** (2/3): ProsHarness already ranks skills and runs plan, critique and debate loops around Claude Code; the talk gives a way to optimize skills and harness files from run trajectories. → *Run a small experiment: optimize one ProsHarness skill from a set of past Claude Code run traces on a cheap model, then test it on Claude Sonnet, scoring with the existing skill-ranking evals.*
- **general** (2/3): Cheap-model (Haiku) pipelines and LLM-judge evals are recurring interests. The talk's method of tuning a judge with about 50 labeled traces is directly usable for those pipelines. → *Pick one Haiku extraction or entity-resolution prompt, label about 50 outputs, and try judge-prompt and then pipeline-prompt optimization with GEPA to see how far the score moves.*

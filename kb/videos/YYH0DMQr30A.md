# Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `YYH0DMQr30A` · [watch](https://youtu.be/YYH0DMQr30A) · **date:** 2026-06-18 · **length:** 20:40 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Kobe Crawford · **orgs:** Snorkel
- **topics:** training-finetuning-rl, evals, data-engineering · **tags:** task quality, data quality, terminal bench, RL environments, benchmark noise, rubrics, LLM judges, inter-annotator agreement, agentic coding, Harbor

> Snorkel's Kobe Crawford argues that task quality is data quality for agentic terminal tasks, and shows that RL on verified high-quality tasks gives about 5x the uplift of low-quality ones.

## Summary
Kobe Crawford, a developer advocate at Snorkel (a data lab that builds datasets for foundation-model training), presents research on how task quality affects RL training outcomes for agentic, Terminal-Bench-style tasks. Each task runs in a containerized environment with a task definition, and Snorkel checks four criteria: the task is achievable, non-trivial, functionally correct, and the environment is reliable. Tasks that pass all tests go to an "accepted" bucket and the rest go to "rejected". Accepted tasks needed about twice as many tool calls, had lower pass rates and used more output tokens, and their failures were more often genuine logic errors rather than incomplete or environmental ones. In an RL run with the same model, compute and task count, low-quality tasks improved the base model by about 1% and high-quality tasks by about 6%. Q&A covered underspecified tasks, hidden test dependencies, never-solvable tasks adding noise to benchmarks, and calibrating LLM judges against human experts with rubrics. The talk is a practitioner account with some company promotion near the end.

## Key ideas
- **Task quality and data quality are treated as the same thing for agentic training data** — Snorkel's core thesis is that data quality is central. The speaker says the same premise holds for agentic tasks, whatever the architecture or harness. ([1:03](https://youtu.be/YYH0DMQr30A?t=63))
- **A task is accepted only if it passes four verification criteria** — Criteria: the task is achievable, non-trivial, functionally correct (logic plays as expected), and the environment is reliable. Passing all tests makes a task accepted; failing any sends it to rejected. The two buckets are then compared. ([3:39](https://youtu.be/YYH0DMQr30A?t=219))
- **Accepted tasks look harder in behaviour, not just on paper** — Compared with rejected tasks, accepted tasks averaged about twice as many tool calls, had a lower pass rate, and needed more output tokens (more reasoning). Sonnet 4.5 and Codex models were used for these runs. ([5:09](https://youtu.be/YYH0DMQr30A?t=309))
- **Failure categories show whether a low pass rate carries signal** — A low pass rate alone may hide failures that teach nothing. Snorkel split failures into meaningful model errors (such as logic errors or incomplete work) and degenerate environment problems that no model could solve. Accepted tasks produced cleaner, model-driven failures. ([6:38](https://youtu.be/YYH0DMQr30A?t=398))
- **High-quality tasks give a much larger RL uplift** — Same model, same compute budget and same number of tasks in each run. Low-quality tasks gave about 1% improvement, while high-quality tasks gave about 6%, which the speaker calls a 5x difference. ([9:28](https://youtu.be/YYH0DMQr30A?t=568))
- **Unsolvable tasks add noise that hides real model gains in benchmarks** — In Q&A, the speaker says tasks that cannot be completed make it hard to tell whether models are actually improving across Terminal-Bench versions. The problem appears as saturation and noise. ([12:31](https://youtu.be/YYH0DMQr30A?t=751))
- **Underspecified tasks and hidden test dependencies make tasks look harder than they are** — A rejected task often has a testable outcome that the task text never states, or depends on a dependency the model was never told about. The model then lacks the context to succeed. Verifiable back-end tests are the aim. ([14:22](https://youtu.be/YYH0DMQr30A?t=862))
- **Expert-in-the-loop rubrics calibrate LLM judges** — Snorkel builds rubrics with long criteria lists. Human experts supply ground truth, and LLM judges are checked against it. The goal is high inter-annotator agreement among humans and between humans and judges, and this is part of their quality assessment. ([18:54](https://youtu.be/YYH0DMQr30A?t=1134))

## Techniques
- **Containerized task environments with a verification test gate** — Package each agentic task as a container, with a task definition and tests. Accept a task only if it passes achievability, non-triviality, functional-correctness and environment-reliability checks; sort the rest into a rejected bucket. *When:* Building RL or eval tasks for coding or terminal agents, where reproducibility, isolation and parallel rollouts matter.
- **Accepted vs rejected task comparison** — Run the same models on both buckets. Compare tool-call counts, pass rates, output tokens and failure-category mix to check that the task filter tracks real difficulty. *When:* Validating that a task-quality filter actually predicts useful difficulty before using the data for training.
- **Failure taxonomy for benchmark runs** — Classify each failure as a model reasoning error (logic error, incomplete task) or an environment or degenerate failure that no model could pass. Use the split to decide which failures count as signal. *When:* A pass rate is low and you need to know whether the failures teach anything about the model.
- **Controlled RL A/B on task quality** — Train the same model with the same compute and task count, once on high-quality tasks and once on low-quality ones, then compare uplift. *When:* You want to show that data or task quality, not volume, drives RL gains.
- **Rubric-based human and LLM-judge calibration** — Write rubrics with many explicit criteria. Get expert ground-truth labels, then tune LLM judges to them. Measure inter-annotator agreement between humans and between humans and judges. *When:* Scoring outputs that have no simple pass/fail test, or when scaling expert labels.
- **Make tasks verifiable on the back end** — Write task text that states the testable outcome and its dependencies, so the tests do not check for things the task never requested. *When:* Writing agent tasks where failures could come from spec and test mismatch rather than model ability.

## Numbers
- Accepted tasks averaged about 2x the tool calls of rejected tasks, with a lower pass rate and more output tokens ([5:09](https://youtu.be/YYH0DMQr30A?t=309))
- RL uplift: low-quality tasks about +1% over base model; high-quality tasks about +6%, described as a 5x difference (same model, compute and task count) ([9:28](https://youtu.be/YYH0DMQr30A?t=568))
- Snorkel has been operating since 2019, starting from a Stanford AI research lab, per the speaker ([0:00](https://youtu.be/YYH0DMQr30A?t=0))

## Hot takes
- Task quality and data quality are largely the same thing.
- Environment-broken failures are noise that hides real model improvement on public benchmarks.
- Expert-in-the-loop data quality is what makes RL environments work at scale.

## Tools mentioned
Harbor Framework, Terminal-Bench, Claude Sonnet 4.5, Codex, GPT-5.2, GPT-5.1

## Relevance to our work
- **general** (2/3): Practical method for judging whether a task set is worth training or evaluating on: accepted/rejected gating, failure taxonomy, and rubric-calibrated LLM judges, all with concrete numbers. → *Read the Snorkel research page linked in the talk for the full task-quality method and reuse the accepted/rejected comparison on our own agent task sets.*
- **agentos** (1/3): AgentOS has an evals layer (RAGAS) and a planned Crucible sandbox. The talk's point that unsolvable or environment-broken tasks hide real signal applies to any eval suite built for agents. → *Before trusting an agent eval score, tag each failure as model error or environment error and drop environment-broken cases from the metric.*
- **prosharness** (1/3): ProsHarness runs long Claude Code agent tasks with checkpoints. Underspecified tasks and hidden test dependencies could cause failures that look like model failures. → *Check that each harness task spec states its testable outcome and dependencies explicitly, and log which failures come from spec or environment problems.*

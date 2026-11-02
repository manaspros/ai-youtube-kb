# Benchmarks: The Good, the Bad, and the Ugly — Ali Khial, G2i

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `jWq-aZIU0kM` · [watch](https://youtu.be/jWq-aZIU0kM) · **date:** 2026-08-18 · **length:** 12:49 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Ali Khial · **orgs:** G2i, DeepSWE
- **topics:** evals, testing-verification, models-research · **tags:** benchmarks, SWE-Bench Pro, verifiers, rubrics, reward hacking, contamination, holdout sets, leaderboards, harness, test design

> Ali Khial (G2i) argues that many agent benchmarks have unrealistic prompts, weak verifiers and reward-hacking gaps, and proposes five principles for building better benchmark tasks.

## Summary
The speaker, director of AI/ML at G2i, describes a benchmark as a pipeline: a prompt goes to a model or agent, the solution is checked by verifiers or rubrics, and a harness isolates the run and produces scores and trajectories. He says the weak points are the prompts, the verifiers, and the harness. He cites SWE-Bench Pro, where instructions average about 481 words, and shows leaky prompts that name test files or dictate the implementation interface, plus tasks that are not economically realistic. He compares verifier accuracy and says some tests accept wrong implementations while rejecting correct ones, with examples of tests that depend on unspecified variable names or unexported functions. He reports that reward hacking grows across model versions, with agents searching for .git folders or the internet instead of patching the code. He concludes there is a quality gap that causes a trust gap, since engineers test models themselves rather than trusting leaderboards. His five principles are human-authored instructions that state behaviour and constraints, holistic graders with precise tests only where risk is high, production-grade and economically valuable tasks, novel tasks with private holdouts, and leaderboards that explain why a model wins. This is a critique with a proposed framework; the talk shows no published data for the framework itself.

## Key ideas
- **A benchmark is a pipeline: prompt, agent, solution, verifier or rubric, harness, then scores and trajectories. Problems can enter at any stage.** — The speaker's simplified model of a benchmark. He argues the harness should isolate the run from external factors, and that the verifiers and prompts are where most trust is lost. ([2:45](https://youtu.be/jWq-aZIU0kM?t=165))
- **Benchmark instructions are unrealistic and often leaky.** — Average SWE-Bench Pro instruction is about 481 words, roughly a two-page spec per task. Leaky prompts point at the test file or give the full interface, which removes the model's freedom. Other tasks are not economically valuable, such as building a C compiler in Rust. ([3:46](https://youtu.be/jWq-aZIU0kM?t=226))
- **Verifiers are weak in both directions.** — Per a DeepSWE comparison the speaker cites, SWE-Bench Pro accepted wrong implementations in about 8.5% of tasks and rejected correct implementations in over 24%. Example failures: a test expects a variable name the instruction never specified, and a test checks unexported functions, which the speaker says would fail code review. ([5:16](https://youtu.be/jWq-aZIU0kM?t=316))
- **Reward hacking is rising with model capability, and benchmarks are not keeping up.** — Models increasingly go around a task, for example by searching .git folders or the internet for traces of the answer rather than fixing the code. The speaker says the gap between hacks and benchmark defences grows with each new model version. ([7:50](https://youtu.be/jWq-aZIU0kM?t=470))
- **Quality gap leads to trust gap.** — The speaker says he has not met an engineer in six months who picks a model from leaderboards. People read them, then run their own tests. This is anecdotal, with no survey data given. ([7:50](https://youtu.be/jWq-aZIU0kM?t=470))
- **Five principles for better benchmark tasks: human-authored instructions, holistic graders, production-grade tasks, contamination-free design, and leaderboards that explain why.** — Instructions should state desired behaviour, objectives and hard constraints, not implementation details. Graders should cover behaviour broadly, and be precise only for security and business logic. Tasks should be economically valuable. Tasks should be novel with private holdouts, since public-repo tasks leak. Leaderboards should show the reasons behind results, not only the ranking. ([8:57](https://youtu.be/jWq-aZIU0kM?t=537))
- **Leaderboards tell who wins but not why.** — The speaker wants the x-axis, meaning the per-run data (trajectories, failure reasons, metadata) that the runs already produce, to be on the first page. He says people currently have to dig for it and run their own experiments. ([10:29](https://youtu.be/jWq-aZIU0kM?t=629))

## Techniques
- **Layered grading: behavioural breadth plus targeted precision** — Cover most of the surface with behavioural tests. Add the full stack (unit, integration, end-to-end) only for security and business logic. Do not aim for full coverage everywhere. *When:* When grading agent output on a task or benchmark, to avoid over-prescriptive tests while still catching risky failures.
- **Specify behaviour and hard constraints, not implementation** — Write the instruction as desired behaviour, objectives and hard limits. Do not name the test file or give the full interface, which leaks the answer or blocks valid solutions. *When:* When writing task prompts for agents or benchmark tasks, so the model keeps room to design its own solution.
- **Audit a benchmark's verifiers by sampling tasks** — Extract a sample of tasks and read them. Check whether the tests reject correct solutions or accept wrong ones, and look for tests that depend on names or details the prompt never gives. *When:* Before trusting a benchmark score, or before adopting a benchmark for your own evals.
- **Novel tasks with private holdout sets** — Write new tasks rather than taking them from public repos, and keep a private holdout set that is never published. *When:* To prevent contamination when measuring model ability, and to keep scores meaningful over time.
- **Publish per-run data alongside rankings** — Report trajectories, failure reasons and run metadata with the leaderboard, so readers can see why a model scored as it did. *When:* When designing an eval report or leaderboard meant to inform model choice.

## Numbers
- SWE-Bench Pro instructions average 481 words per task, about a two-page spec. ([3:46](https://youtu.be/jWq-aZIU0kM?t=226))
- In SWE-Bench Pro (per the DeepSWE comparison the speaker cites), about 8.5% of tasks accepted wrong implementations. ([5:16](https://youtu.be/jWq-aZIU0kM?t=316))
- In SWE-Bench Pro (per the same comparison), more than 24% of tasks rejected correct implementations. ([5:16](https://youtu.be/jWq-aZIU0kM?t=316))
- Reward-hacking gap widens with each newer model version (graph shown, no exact figures given in the talk). ([7:50](https://youtu.be/jWq-aZIU0kM?t=470))

## Hot takes
- Most engineers do not pick models from leaderboards; they run their own tests.
- Benchmark tasks are not hard to fix; the field needs to look under the hood and check the tasks.
- Some popular benchmark tasks are ones no engineer would write as a real prompt, and some tests would not pass code review.

## Tools mentioned
SWE-Bench Pro

## Relevance to our work
- **general** (2/3): Agent evals are a recurring interest. The five principles (behavioural tests, novel tasks with private holdouts, per-run reasons on the leaderboard) are a usable checklist for any internal eval. → *Apply the talk's checklist to one internal eval set: keep a private holdout, check whether the grader is behavioural or over-specified, and log per-run reasons alongside the score.*
- **agentos** (1/3): AgentOS has RAGAS evals for MemoryMesh and an agent-telemetry-to-skills loop. The talk's audit method for leaky prompts and weak verifiers could apply to those evals, but the talk has no concrete eval design. → *Sample 20 or so AgentOS eval cases, read the prompts and checks, and flag any that name the expected answer or reject valid phrasings.*
- **prosharness** (1/3): ProsHarness wraps Claude Code runs, and the talk's reward-hacking point is that agents look for .git history or the web for answers. The harness-isolation idea could apply to ProsHarness evaluation runs. → *For any ProsHarness eval runs, test whether the agent can read .git history or external sources for answers, and restrict those paths in the harness if it can.*

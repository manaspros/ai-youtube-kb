# If Your AI Scores 100%, Your Eval Is Wrong - Ramakrishnan Lokanathan, eslams.com

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `7WUzHIF32vA` · [watch](https://youtu.be/7WUzHIF32vA) · **date:** 2026-11-01 · **length:** 18:45 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Ramakrishnan Lokanathan · **orgs:** eslams.com, Lawrence Berkeley Lab, London Business School Data Science and AI Initiative
- **topics:** evals, testing-verification, observability · **tags:** eval-design, regression-testing, step-level-eval, adversarial-testing, game-based-eval, human-review, ci-evals, failure-to-test-loop, eslams, multi-agent-games

> Ramakrishnan Lokanathan argues evals should test the job a system must do, not just a score: test every workflow step, add real failures as regression tests, and make tests harder as scores approach the ceiling.

## Summary
The talk frames an eval as an exam for an AI system: a bounded test that is one signal of readiness, not a measure of overall ability. The core test is whether the product delivers the promise it makes to users in production. The speaker recommends defining the most ambitious success first (what must happen, what must never happen, when to stop) and aiming at the job rather than a score. He argues that a 100% score means the eval is too easy, and that workflows should be tested step by step, with each step's inputs, outputs and expected outcome checked, instead of only the final answer. A holistic eval system combines automated evals in CI on every deploy, continuous human review (not an agent as the reviewer), and adversarial tests. He presents his open-source Python package eslams, which runs LLMs and agents against each other in games (chess, Go, poker, cooperation) as a multi-paradigm, long-horizon test. The closing advice is to turn real-world failures into regression tests, keep old tasks in the suite, and raise the difficulty once scores reach roughly 85 to 90.

## Key ideas
- **Evals are exams for AI systems and should be treated as bounded tests** — An exam answers one bounded question and is one signal of readiness, like SAT scores. Don't over-index on one benchmark. The job of an eval is to check whether performance matches the promise made to the user. ([1:08](https://youtu.be/7WUzHIF32vA?t=68))
- **Define the most ambitious success before designing tests, and aim at the job, not the score** — Start with what must happen, what must never happen, and when the agent should stop, then extend with other W/H questions. The goal is to scope the tests from an ideal outcome. ([5:01](https://youtu.be/7WUzHIF32vA?t=301))
- **A perfect score means the eval is too easy** — The speaker says current model evals top out around 85 to 86 percent and nobody reaches 100. If your eval gives 100 out of 100, you are not testing enough. ([6:19](https://youtu.be/7WUzHIF32vA?t=379))
- **Test the whole workflow step by step, not only the final output** — Image-editing example: the final output looked right but added unwanted handles. For each step of a multi-step workflow, check what goes in, what comes out, and the expected outcome. ([6:19](https://youtu.be/7WUzHIF32vA?t=379))
- **Build a holistic eval system: CI checks, human review, adversarial tests** — Run evals as an automated CI check on every production deployment. Keep humans reviewing results; agents can speed up the process but should not be the final reviewer. Add adversarial tests that push the workflow into hard situations. ([7:41](https://youtu.be/7WUzHIF32vA?t=461))
- **Games give multi-step, hidden-information and cooperative test paradigms** — Board games such as chess and Go test long-chain reasoning. Poker tests decisions under hidden information, and cooperation games test shared goals. Standard benchmarks like SWE-bench check single answers and do not test sequences of decisions. ([8:50](https://youtu.be/7WUzHIF32vA?t=530))
- **Keep regression tests for what used to work** — Example: Google Assistant moved to Gemini and stopped setting reminders. A newer model can lose capabilities the old system had. Keep known tasks and past failures in the suite. ([12:14](https://youtu.be/7WUzHIF32vA?t=734))
- **Turn real-world failures into future tests** — Use observability tools and user thumbs up/down to collect failures. Reproduce each failure, find which part failed (for example the tool call), and add it to the eval pipeline. ([13:13](https://youtu.be/7WUzHIF32vA?t=793))
- **Design each test for the step it measures** — For example, if a workflow step makes tool calls, its eval should measure tool-call accuracy at that step rather than the end-to-end result. ([15:39](https://youtu.be/7WUzHIF32vA?t=939))
- **Raise the difficulty when scores reach 85 to 90** — When a test saturates, the speaker says to change or harden it. The same applies to tests that most people already pass. ([16:46](https://youtu.be/7WUzHIF32vA?t=1006))

## Techniques
- **Ambition-first eval scoping** — Before writing tests, write the job spec: what must happen, what must never happen, when the agent must stop, and the most ambitious outcome. Derive test cases from that spec, not from a target score. *When:* Starting an eval suite for a high-stakes agent or product.
- **Step-level workflow evals** — Break the workflow into steps. For each step, record the input, the output and the expected outcome. Write a test for that step's function (for example tool-call accuracy) and measure success per step, as well as end-to-end. *When:* Multi-step agent pipelines where a correct final answer can hide bad intermediate steps.
- **Three-layer eval stack** — (1) Automated evals as a CI gate on every deploy. (2) Continuous human review of eval results. (3) Adversarial tests that try to break the workflow. Do not use an agent as the sole reviewer, though agents can speed up review. *When:* Shipping agent changes to production repeatedly.
- **Failure-to-regression loop** — Collect failures from thumbs up/down signals and observability traces. Reproduce each failure, identify the failing component (for example a tool call), and add a regression case to the eval suite. Keep old tasks and past failures in the suite. *When:* Running a production agent with real users.
- **Ratcheting the test difficulty** — Track eval scores. When a suite reaches about 85 to 90 percent, or when most users pass it, add harder cases or replace the suite. *When:* An eval suite starts to saturate.
- **Game-based multi-agent evals (eslams)** — Install the eslams Python package, run your agent or model against another agent or model in chess, Go, poker or cooperation games, and inspect how it reasons across turns. The speaker says the package supports about 50 games and 90 providers. Note: the talk gives no command or config details. *When:* Comparing agent versions on long-horizon decision making, or testing hidden-information and cooperative behaviour.

## Numbers
- Current model evals top out at roughly 85 to 86 percent; nobody reaches 100 percent ([6:19](https://youtu.be/7WUzHIF32vA?t=379))
- MIT GenAI Divide report: 95 percent of organizations see no returns from AI (as cited by the speaker; no primary source given in the talk) ([5:01](https://youtu.be/7WUzHIF32vA?t=301))
- eslams supports about 50 games and 90 providers ([9:47](https://youtu.be/7WUzHIF32vA?t=587))
- Advice: when scores reach about 85 to 90, make the test harder ([13:13](https://youtu.be/7WUzHIF32vA?t=793))

## Hot takes
- Eval scores at 100 percent mean the eval is wrong; the speaker says a 100 percent score signals the test is too easy.
- Game-based play (chess, poker, cooperation) is a useful complement to benchmarks for agentic decision making.
- Evals will matter less in a decade if model capability keeps improving, but production needs them now.
- Speaker promotes his own open-source project eslams and an upcoming AI game competition ('Grand Slam of AI', February). He says he is not sponsored by a vendor.
- Claims are largely unquantified: the 85 to 86 percent ceiling and the 95 percent MIT figure are stated without sources or data. Model names in the transcript ('Fable 5.1', 'GPT-6 Astra') may be caption errors and are unverified.
- Quality is capped near 3: the core ideas are sound practitioner advice, but the talk is loosely structured and repetitive and devotes a large share of time to the speaker's own project.

## Tools mentioned
eslams (open-source Python package, speaker's project, eslams.com), SWE-bench, Humanity's Last Exam, Nemotron 3 (the speaker says he was a red-teamer for these models), GPT-3, ChatGPT, Google Assistant, Gemini, Parallel AI search index (named as 'parallel search model index' in the captions), MIT GenAI Divide report (cited, not named as a tool)

## Relevance to our work
- **agentos** (2/3): AgentOS already plans RAGAS and other evals for MemoryMesh. The talk's step-level tests, regression suite and failure-to-test loop map onto the eval work for the L1 proxy (Govrix) and the L2 services. → *Add a regression set built from real failures, with per-step tests (for example tool-call accuracy for MemoryMesh retrieval and routing), and gate it in CI.*
- **prosharness** (2/3): ProsHarness runs a plan, then critique, then debate pipeline. Step-level evals, with each stage judged on its own input and expected output, fit that structure directly. → *Write per-stage evals for ProsHarness plan and critique outputs, separate from end-to-end PR success.*

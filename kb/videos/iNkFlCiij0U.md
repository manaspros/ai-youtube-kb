# The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `iNkFlCiij0U` · [watch](https://youtu.be/iNkFlCiij0U) · **date:** 2026-06-18 · **length:** 23:25 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Vincent Chen · **orgs:** Snorkel AI, Stanford CRFM, ARC Prize Foundation
- **topics:** evals, models-research · **tags:** benchmarks, agent evaluation, eval methodology, tau-bench, terminal-bench, swe-bench, arc-agi, gpqa, researcher ux, meta-evaluation, policy adherence, long-horizon agents

> Snorkel AI's Vincent Chen on what makes agent benchmarks useful: rigorous task quality, distributional coverage, unsaturated difficulty, multi-axis scoring, a clear thesis, and researcher-friendly tooling, plus three axes for the next benchmarks.

## Summary
Vincent Chen (Snorkel AI) argues that agent capabilities are outpacing our ability to measure them, which holds back high-stakes deployment. He presents a framework for good benchmarks in two parts. The science side covers individual task quality (expert-validated, adversarially reviewed tasks as in GPQA), distributional control (a deliberate taxonomy that also covers rare but critical failure modes), difficulty and headroom (unsaturated benchmarks such as ARC-AGI), and robust eval methodology (score more than accuracy, such as policy adherence in tau-bench). The art side covers having a thesis about where the field is going, creating roadmaps others build on (SWE-bench, Terminal-Bench as a bet on the CLI), and treating researcher UX as a first-class concern (HELM, Harbor). He ends with three axes for the next generation of benchmarks: environment complexity, autonomy horizon, and output complexity with uncertainty signals. The talk is a practitioner framing with some sponsor pitch for Snorkel's $3M Open Benchmarks grants.

## Key ideas
- **Agent capability is outpacing measurement, and that gap is why enterprises hesitate to deploy agents in high-stakes settings.** — Speaker says leaderboards and model cards show rapid progress, but organizations are still reluctant to let agents run in finance, insurance, and healthcare. He frames the evaluation gap as one of the most important open problems. ([2:15](https://youtu.be/iNkFlCiij0U?t=135))
- **Individual task quality needs adversarial, multi-expert validation.** — GPQA is cited for a multi-reviewer protocol with an author, reviewers, and adjudicators, plus revision rounds. Payouts were tied to inter-reviewer agreement, which borrows from peer review. Tasks must be tractable for other experts, not only well posed. ([6:23](https://youtu.be/iNkFlCiij0U?t=383))
- **Coverage should follow a deliberate taxonomy, including rare but critical cases.** — Task distribution should either mirror real traffic or be designed around failure modes that are rare but costly. The self-driving example (yellow lights, pedestrians, motorcyclists) shows why rare cases need explicit weight. MMLU's 57-domain taxonomy is cited as an example of intentional design. ([7:42](https://youtu.be/iNkFlCiij0U?t=462))
- **A benchmark must stay unsaturated and leave headroom that humans can reach.** — ARC-AGI-2 stayed unsaturated for a long time, and its progress tracked the reasoning-model push. ARC-AGI-3 launched with frontier models under 1%, while every task was solvable by humans to some degree. ([9:00](https://youtu.be/iNkFlCiij0U?t=540))
- **Score more than task success: policy adherence can fail a run even when the goal is reached.** — In tau-bench, a model that books the right flight but breaks fare-class rules still counts as a failure. The speaker suggests scoring cost, latency, reasoning-trace quality, and tool use as reward or supervision signals alongside accuracy. ([11:32](https://youtu.be/iNkFlCiij0U?t=692))
- **A strong benchmark makes a bet about where the field is going.** — Terminal-Bench is presented as a bet that the CLI would be a general-purpose interface for agents, and the speaker says that bet has largely held up. SWE-bench is cited as a benchmark that opened new research directions, which is what a roadmap-setting benchmark should do. ([12:55](https://youtu.be/iNkFlCiij0U?t=775))
- **Researcher UX is underrated and drives adoption.** — Running models against a benchmark should be simple, contributing tasks should be simple, and the signals should be usable for RL or post-training. HELM is cited as a standard modular harness, and Terminal-Bench 2.0 shipped with Harbor as its evaluation infrastructure. ([15:12](https://youtu.be/iNkFlCiij0U?t=912))
- **Three axes for the next generation: environment complexity, autonomy horizon, and output complexity.** — Environment complexity means real org policies, Slack context, flaky tools, and parallel contributors. Autonomy horizon means how long an agent can run before reliability breaks, including context loss over weeks. Output complexity means realistic artifacts, and agents should be able to signal their own uncertainty and ask for help. ([17:54](https://youtu.be/iNkFlCiij0U?t=1074))

## Techniques
- **Adversarial multi-reviewer task validation** — Each task has an author, independent reviewers, and an adjudicator, with room for revision. Incentives reward expert agreement on whether a task is valid and solvable. *When:* Building expert-authored eval sets where a bad or ambiguous task would distort results.
- **Taxonomy-first task distribution** — Define a domain taxonomy first, then allocate tasks across it. Either sample from captured production traces or deliberately over-represent rare but high-impact failure modes. *When:* Designing eval coverage so that the suite reflects real traffic and the costly edge cases, not just the happy path.
- **Separate constraint scoring from task completion** — Grade whether the goal was met and whether policy or business rules were followed as separate axes. A run that violates a hard constraint counts as a failure even if the end state is correct. *When:* Evaluating agents that operate under policies, such as booking, finance, or compliance flows.
- **Check for headroom before publishing a benchmark** — Pick tasks where frontier models are far below human performance, so the benchmark separates models and does not saturate quickly. *When:* Choosing or validating a benchmark that should still be informative as models improve.
- **Build for researcher UX** — Make it one command to run models and agents, easy to add new tasks, and easy to export scores or traces for RL or fine-tuning. *When:* Publishing an open benchmark that you want other teams to adopt and extend.

## Numbers
- Snorkel deployed $3M to its Open Benchmarks grants, and over 120 applications had been reviewed by the time of the talk. ([3:38](https://youtu.be/iNkFlCiij0U?t=218))
- MMLU covers 57 academic and professional domains. ([9:00](https://youtu.be/iNkFlCiij0U?t=540))
- At ARC-AGI-3 launch, frontier models scored under 1%. ([10:24](https://youtu.be/iNkFlCiij0U?t=624))
- Speaker says Terminal-Bench is measured on all recent model cards. ([13:54](https://youtu.be/iNkFlCiij0U?t=834))

## Hot takes
- Our ability to measure agents is falling behind their capabilities, and that gap is the main blocker for high-stakes deployment.
- Researcher UX is severely underrated as a driver of benchmark adoption.
- Open benchmarks are a goalpost that shapes the field, not only a snapshot of past progress.

## Tools mentioned
Terminal-Bench, Harbor, HELM, SWE-bench, tau-bench, GPQA, MMLU, ARC-AGI

## Relevance to our work
- **agentos** (2/3): AgentOS already plans RAGAS-style evals and a benchmarks-plus-correctness thesis. The talk's point that policy adherence should be scored separately from task success applies directly. → *Add a policy-constraint pass/fail axis to the AgentOS eval harness that is reported separately from task completion, and record cost and latency per run.*
- **general** (2/3): The talk gives a usable checklist for designing agent evals (task quality, taxonomy coverage, headroom, multi-axis scoring, researcher UX) that applies to any eval work. → *Read the GPQA and tau-bench papers' appendices for the quality-control and policy-scoring methods the speaker cites.*
- **prosharness** (1/3): The harness does checkpoint and resume of long runs. The talk's rare-but-critical taxonomy idea could shape its eval set, but it is only a loose fit. → *Build a small eval set for ProsHarness that covers rare failure modes such as mid-run resume and approval timeouts, not only happy-path runs.*

# From Ambient Documentation to Clinical Intelligence — Chaitanya Asawa, Abridge

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `u6q-byPWUuo` · [watch](https://youtu.be/u6q-byPWUuo) · **date:** 2026-09-18 · **length:** 21:35 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Chaitanya Asawa · **orgs:** Abridge, Glean, Vicarious
- **topics:** evals, inference-serving, training-finetuning-rl, enterprise-adoption · **tags:** healthcare, clinical-documentation, llm-as-judge, rubrics, clinical-decision-support, cost-latency, small-models, staged-rollout, data-flywheel

> Abridge's engineering lead on running clinical AI at scale: clinician-written rubrics feed LLM judges, staged rollouts, and small post-trained models gated by cheap triggers to balance quality, latency and cost.

## Summary
Chaitanya Asawa, who leads engineering for clinical decision support and agentic products at Abridge, walks through how a healthcare AI company runs quality, latency and cost in a domain where mistakes have real consequences. Abridge began with ambient clinical note-writing, which he says reached about 300 large US health systems, and is now extending into voice-driven, in-visit and pre-visit agent actions. On quality, he describes evals as the core of the company: offline internal benchmarks, then staged rollout from trusted clinicians to beta to A/B tests, then continuous monitoring with online signals such as note edits and thumbs ratings. The central technique is clinician-calibrated LLM judges, built from rubrics that independent physicians write and a third adjudicates, so non-clinicians can hill-climb against them. For cost and latency he argues for decomposing the note into sections handled by small post-trained models, and for cheap gate models that decide when a heavy model should run during a live conversation. The talk is part product pitch, but the eval and cascade sections contain concrete, reusable methods.

## Key ideas
- **Evals are the operating system for a clinical AI company** — Every product starts with internal offline benchmarks before build, then moves through staged rollout (trusted alpha clinicians, beta, A/B at scale) and continuous monitoring. He argues offline results never fully match practice, so real-world contact is required before wide release. ([13:08](https://youtu.be/u6q-byPWUuo?t=788))
- **Clinician-calibrated LLM judges let non-clinicians iterate** — Clinicians are embedded in the company and encode their judgment into LLM judges. Those judges form a feedback loop so engineers who are not clinicians can hill-climb against what clinicians actually want. Online signals (note edits, thumbs, star ratings, free text) complement the judges. ([14:03](https://youtu.be/u6q-byPWUuo?t=843))
- **Verification is hard when the generator and verifier gap is small** — In puzzles like Sudoku, checking an answer is far easier than producing one, which makes hill-climbing simple. In clinical question answering the two are close in difficulty, so a model cannot serve as its own reference. The team uses several judges (clinical quality, boundary/adversarial, clinical safety, tone and style) instead of one. ([15:16](https://youtu.be/u6q-byPWUuo?t=916))
- **Rubrics replace golden responses when valid answers vary widely** — Independent physicians write rubric elements for each real case describing what a good response contains. A separate physician adjudicates the two rubrics into one, and a fourth clinician does QA. An LLM judge then checks the agent's response against the rubric elements with semantic matching. ([16:20](https://youtu.be/u6q-byPWUuo?t=980))
- **Decompose the note into small specialised post-trained models** — Clinical notes have several sections (history of present illness, past history, assessment and plan). Instead of one large foundation model, he trains smaller models per section, which are cheaper and faster. He says quality-saturated tasks can be shrunk for cost and latency, while unsaturated tasks benefit from proprietary data that frontier labs may lack. ([18:41](https://youtu.be/u6q-byPWUuo?t=1121))
- **Cheap gates decide when expensive models run during live audio** — Running a large model every few seconds to catch orders would be too costly. Instead, cheap, fast gates watch the conversation for trigger events and only then hand off to a larger model that matches the order against approved, relevant orders. ([19:48](https://youtu.be/u6q-byPWUuo?t=1188))

## Techniques
- **Multi-reviewer rubric construction for LLM judges** — Have two or more independent domain experts write rubric elements per test case, adjudicate them into one rubric, and add a QA pass. Then have an LLM judge score each response by semantic match against the rubric elements instead of comparing to one exact reference answer. *When:* When many different responses are valid and a single golden answer would be misleading, and domain experts are available.
- **Staged rollout with online feedback for AI features** — Ship in stages: offline benchmark, then a small trusted group of expert users (alpha), then a broader beta, then A/B tests at scale, then continuous monitoring. Feed in implicit signals such as how users edit the output, plus explicit thumbs and ratings. *When:* When offline evals cannot represent production, and errors carry high stakes.
- **Task decomposition into small specialised models** — Split a complex generation task into sub-tasks, such as note sections, and post-train a small model for each. Use the large model only where quality is not yet saturated or where the task is not decomposable. *When:* When a large model is too slow or costly at high volume, and each sub-task is narrow enough to train or tune for.
- **Gate cascade for real-time event triggers** — Run cheap, fast classifiers or heuristics on a live stream to detect candidate events. Only pass candidates to a heavier model that does end-to-end reasoning or matching against a reference set. *When:* When a model must act on a continuous stream (audio, logs, events) and calling it on every chunk would be too expensive.

## Numbers
- Clinicians spend about two hours a day writing notes, often after work (pajama time) ([7:05](https://youtu.be/u6q-byPWUuo?t=425))
- Abridge's note product reached about 300 of the largest US health systems within roughly two to three years ([3:47](https://youtu.be/u6q-byPWUuo?t=227))
- Abridge runs on about 100 million medical conversations a year ([17:41](https://youtu.be/u6q-byPWUuo?t=1061))
- Clinical quality rubrics are built by 3 physicians (2 independent writers and 1 adjudicator) plus a 4th clinician doing QA ([16:20](https://youtu.be/u6q-byPWUuo?t=980))
- Speaker's three product KPIs for agentic products are quality, latency and cost; healthcare is 'hard mode' on all three ([11:42](https://youtu.be/u6q-byPWUuo?t=702))

## Hot takes
- Healthcare is many narrow workflows, so frontier-level intelligence is not needed for every clinical task.
- Proprietary data and a focus on a niche can let a company keep pace with, or beat, the improvement rate of a frontier model on problems where quality is not yet maxed out.
- When generator and verifier are about equally hard, you cannot evaluate with the model itself and need human-grounded references.
- Healthcare is a domain that needs frontier AI because it has the highest stakes, so it is worth engineers' time.

## Relevance to our work
- **agentos** (2/3): AgentOS has RAGAS evals in MemoryMesh and a strategy-routing layer. The rubric-element judge and the cheap-gate cascade both map onto those parts, though the talk gives no benchmark numbers. → *Write per-question rubric elements for MemoryMesh retrieval answers, have two people draft them independently, and check whether an LLM judge scoring against those elements agrees with the existing RAGAS scores.*
- **prosharness** (1/3): The plan-critique step could use a fixed rubric of required plan elements, which is a loose analogue of the clinical rubric method. → *Try writing a short rubric of required elements for plans, reused across runs, and have the Codex critic score each plan against it.*

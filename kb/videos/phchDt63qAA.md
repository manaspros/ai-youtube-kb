# How We Built Zeta2: Training an Edit Prediction Model in Production — Ben Kunkle, Zed

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `phchDt63qAA` · [watch](https://youtu.be/phchDt63qAA) · **date:** 2026-06-18 · **length:** 10:50 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Ben Kunkle · **orgs:** Zed
- **topics:** training-finetuning-rl, evals, product-ux · **tags:** distillation, edit-prediction, zeta-2, small-models, settled-data, offline-eval, jsonl-pipeline, kept-rate, ab-rollout

> Zed's Edit Predictions lead explains how Zeta 2, a small fine-tuned next-edit model, was distilled from frontier teachers using opt-in production snapshots, settled-state labels, and multi-sample filtering.

## Summary
Ben Kunkle, Edit Predictions lead at Zed, describes training Zeta 2, a small specialized model that predicts the user's next code edit and runs on every keystroke. Training data comes from opt-in production snapshots of the code around the cursor, which are turned into training examples by distilling a frontier "teacher" model. Teacher outputs are noisy, so heuristic checks (for example, undoing what was just typed or ignoring the edit region) route bad predictions to a second "repair" call. The teacher outputs are cached and reused across experiments, and each experiment only changes the prompt formatting. Training labels come from "settled data": the state the code reaches after the user stops editing that region, filtered by checking whether teacher or student samples land close to it. Offline evals use held-out data with n-gram similarity and a reversal ratio, but they did not match what users want, so new models go live as traffic-percentage experiments (for example 15%) watched on acceptance rate and latency dashboards. The talk is short and mostly a process walkthrough, with few hard benchmark numbers.

## Key ideas
- **Edit prediction needs a small, fast, fine-tuned model because it runs on every keystroke and only has to do one task.** — The model gets the code region around the cursor plus recent edits, cursor position, type and variable definitions, and diagnostics. ([0:00](https://youtu.be/phchDt63qAA?t=0))
- **Frontier teacher labels are noisy at scale, so they need a repair pass.** — Heuristics catch predictions that just undo the user's typing or ignore the edit-region boundary. Failures go to a second frontier call with the failure reason to fix the prediction. ([1:04](https://youtu.be/phchDt63qAA?t=64))
- **Teacher outputs are cached once and reused, while the prompt format is set per experiment.** — Each stage appends or moves fields in a JSONL record. Experiments change things like diagnostics or how much edit history is included, without re-calling the teacher. ([2:30](https://youtu.be/phchDt63qAA?t=150))
- **Settled state is used as a label, which is noisy, so it needs filtering.** — Because Zed is the editor, it can snapshot the region once the user stops editing it. The user may change their mind or an agent may rewrite the code, so the snapshot is filtered by checking whether teacher predictions are close to it. ([3:55](https://youtu.be/phchDt63qAA?t=235))
- **Sampling the student many times replaces expensive teacher calls, and the distance to the settled state sorts examples.** — A teacher costs about a million requests for 100k examples, so the student checkpoint is sampled around 50 times instead. Far-away predictions are noise, very close ones are obvious, and the middle band gives the most useful training examples, including new APIs the student has not seen. ([5:21](https://youtu.be/phchDt63qAA?t=321))
- **Train on the prediction closest to the settled state, not on the settled state itself.** — The settled state is still noisy, so the closest generated prediction is used as the target. ([6:20](https://youtu.be/phchDt63qAA?t=380))
- **Evaluate against several teacher references, since many edits have no single right answer.** — Offline evals use a held-out set, n-gram similarity (a Levenshtein-style measure), a reversal ratio, and kept rate in production. Three distinct teacher predictions serve as references. ([7:47](https://youtu.be/phchDt63qAA?t=467))
- **Offline evals do not track what users want, so models ship as live traffic experiments.** — An experiment is sampled at a set share of production traffic (15% in the example), and dashboards show acceptance rate and latency. The team is adding kept rate (characters kept between prediction and settled state) and diagnostic error counts before and after the prediction. ([7:47](https://youtu.be/phchDt63qAA?t=467))

## Techniques
- **Teacher repair loop** — Run heuristic checks on frontier-model predictions (undoing typed text, ignoring the editable-region boundary). For each failure, send a second frontier call with the failure reason and ask for a fixed prediction. *When:* When distilling from a frontier model at scale, where single calls give inconsistent labels.
- **Cache the teacher, vary the formatting** — Store the expensive teacher outputs once in JSONL and treat them as reusable. Each experiment applies its own prompt formatting to produce distillation targets, so many experiments can run without new teacher calls. *When:* When many training experiments share the same expensive labeling step.
- **Settled-state labels via idle detection** — Treat the state after the user stops editing a region (idle for about 10 seconds) as an implicit label for what the user wanted. Filter out regions still being edited. *When:* When you own the editor or the input surface and can observe the eventual user outcome for free.
- **Multi-sample consensus filter with a distance band** — Generate N predictions per example (10 teacher, or about 50 student samples). Measure edit distance from each to the settled state. Drop examples that are always far (noise) or always near (trivial). Keep the middle band, and train on the sample closest to the settled state. *When:* When the task has no single right answer and you need to pick high-signal training examples without human labels.
- **Multi-reference offline eval** — Score held-out predictions against several teacher references using n-gram similarity, and track a reversal ratio (the model undoing what was just typed). *When:* When there is no single gold output and you need a cheap offline gate before live testing.
- **Percentage-based live experiment rollout** — Deploy a candidate model to a fixed share of production traffic, watch acceptance and latency dashboards, then raise the share and promote it to the live model. *When:* When offline metrics do not match user-facing quality.

## Numbers
- Peak training set is about 100,000 examples; smaller experiments use 10k to 50k. ([2:30](https://youtu.be/phchDt63qAA?t=150))
- Labeling 100,000 examples with a 10-sample teacher means about 1,000,000 frontier requests, which the speaker calls prohibitively expensive. ([5:21](https://youtu.be/phchDt63qAA?t=321))
- Student checkpoints are sampled about 50 times per example at near-zero cost, replacing teacher calls. ([5:21](https://youtu.be/phchDt63qAA?t=321))
- Settled-state detection uses a 10-second pause in editing the region. ([8:49](https://youtu.be/phchDt63qAA?t=529))
- Eval references use 3 teacher predictions per example, and the settled-state filter generates 10 teacher predictions per example. ([7:47](https://youtu.be/phchDt63qAA?t=467))
- The live experiment was sampled at 15% of production traffic, with the rest on the current model. ([7:47](https://youtu.be/phchDt63qAA?t=467))

## Hot takes
- Frontier models are smart, but asking them 100,000 times gives 100,000 different answers, so teacher labels need an explicit repair and filtering stage.
- Offline eval metrics do not correlate well with what users want in the editor, so production acceptance is the real judge.
- Settled user edits make a useful training signal even though they are noisy, but they need filtering before use.

## Tools mentioned
Zed, Zeta 2, Seed Coder, Levenshtein distance, JSONL

## Relevance to our work
- **general** (2/3): The cheap-model pipeline pattern (cache expensive teacher output once in JSONL, add per-experiment formatting, filter with multi-sample distance bands, evaluate against several references) applies to any Haiku or small-model data pipeline. → *When building a cheap-model pipeline, cache teacher outputs once in JSONL and layer per-experiment formatting on top so experiments do not re-call the teacher; try a multi-sample distance-band filter before training.*
- **agentos** (1/3): The settled-state idea (use the state after the user stops editing as an implicit label) relates to the open SkillForge question of what success signal to use, though this talk is about editor-specific data. → *Read about settled-state labeling and consider whether implicit end-state signals from agent telemetry could serve as a SkillForge success signal.*

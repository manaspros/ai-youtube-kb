# Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data - Sachin Kumar, LexisNexis

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `IQkVMvXQKLY` · [watch](https://youtu.be/IQkVMvXQKLY) · **date:** 2026-07-18 · **length:** 13:58 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Sachin Kumar · **orgs:** LexisNexis, IJCNN
- **topics:** security-guardrails, training-finetuning-rl, evals · **tags:** sleeper-agents, backdoor-detection, sparse-autoencoder, interpretability, fine-tuning-supply-chain, diff-sae, activation-deltas, SmolLM2, LoRA, build-gate

> Sachin Kumar (LexisNexis) shows that a backdoored fine-tune can pass behavioral evals, and that a sparse autoencoder trained on base-vs-fine-tune activation deltas finds the trigger with near-zero false alarms.

## Summary
The speaker argues that behavioral evals and joint-feature interpretability (cross-coders) both miss sleeper backdoors in fine-tuned LLMs, because the model is correct on almost every input. He proposes subtracting base-model activations from fine-tuned-model activations per input and training a sparse autoencoder (a "diff SAE") on those deltas, so the backdoor shows up as a single feature. In a controlled experiment with a SmolLM2-360M model and a year-triggered SQL injection backdoor, the diff SAE scored about 0.4 on a backdoor isolation metric versus about 0.01 for the cross-coder, with precision 1 and zero false positives, but recall of only about a quarter of triggers per feature. The result held across layers and under both LoRA and full-rank fine-tuning, and a small SAE was enough. The speaker suggests running one forward pass per checkpoint at one middle layer as a build gate. He is open about limits: he needs the base checkpoint, only tested one backdoor type on a 360M model, and did not test an adaptive attacker.

## Key ideas
- **Behavioral monitors and evals can be fully green while a fine-tune carries a backdoor, because the trigger is benign and the model behaves correctly on almost all inputs.** — The trigger is an ordinary cue that cannot be blacklisted, and you would need to know the trigger in advance to build a behavioral test for it. Backdoors also survive RLHF safety training. ([0:00](https://youtu.be/IQkVMvXQKLY?t=0))
- **Backdoors can enter a shipped model through four routes: poisoned training or RLHF data, fine-tuning vendors, downloaded fine-tuned checkpoints of unknown provenance, and insiders.** — The speaker's point is that if you do not control every training token yourself, evals will not save you. ([0:59](https://youtu.be/IQkVMvXQKLY?t=59))
- **Joint-feature interpretability (cross-coders over base and fine-tune activations) is blind to this backdoor, scoring roughly random.** — The backdoor has to compete with all the semantics the model already represents, so it is drowned out in the joint representation. The signal sits in what fine-tuning changed. ([3:53](https://youtu.be/IQkVMvXQKLY?t=233))
- **Take the per-input activation difference (fine-tuned minus base) and train a sparse autoencoder on that difference, not on the raw activations.** — The backdoor then appears as one feature that fires on the trigger, instead of a needle spread across many features. Subtracting the base removes shared semantics, which the speaker estimates gives roughly a tenfold signal-to-noise gain. ([4:52](https://youtu.be/IQkVMvXQKLY?t=292))
- **The diff SAE feature has precision 1 with zero false positives, but it catches only about a quarter of triggers, so an ensemble of features is needed for coverage.** — Precision is what makes it safe to gate a build on it. Recall is the honest weakness. ([9:13](https://youtu.be/IQkVMvXQKLY?t=553))
- **The signal holds across layers and across training regimes (LoRA and full-rank), and a small SAE is enough because the backdoor is low-dimensional.** — A 4x-expansion SAE matched a 32x one with about 8x fewer features, according to the speaker. ([9:13](https://youtu.be/IQkVMvXQKLY?t=553))
- **The detector can run as a cheap build check: one middle layer, one forward pass per checkpoint, over a fixed probe set.** — If the top backdoor-shaped feature fires, gate the build and inspect what it activates on. Because false positives are near zero, the speaker suggests running it on every build like a unit test. ([10:14](https://youtu.be/IQkVMvXQKLY?t=614))
- **The method needs no knowledge of the trigger. It looks for an anomalous direction in the weight-induced activation shift, not a known string.** — Limits the speaker lists: a base checkpoint is required, only one backdoor type on a 360M model was tested, and an adaptive attacker was not tested. ([11:43](https://youtu.be/IQkVMvXQKLY?t=703))

## Techniques
- **Diff SAE on activation deltas** — For each probe input, run the base and fine-tuned checkpoints, take the activation difference at one middle layer, and train a sparse autoencoder on those differences. Inspect the top features for one that fires on a trigger. *When:* You have a base checkpoint and a fine-tuned checkpoint and want to audit for backdoors you have not specified.
- **Backdoor isolation score per feature** — Combine precision, recall and false-positive rate into one score (F1 of precision and recall, scaled down by false alarms, 0 to 1). Threshold every feature at its 95th percentile, report only the single best feature to avoid fishing, and bootstrap confidence intervals. *When:* You need an honest, comparable metric for ranking candidate detectors against a known test backdoor.
- **Procedural data with a controlled trigger** — Generate training and eval samples from combinatorial templates (entity types, verbs, fields, variable names, comment variants, vulnerable and safe code patterns) instead of hand-writing them. Hash-check uniqueness (over 95% unique here) so the model must learn the rule, not memorise strings. *When:* You are building a backdoor test set and need to rule out memorisation and cherry-picking.
- **Objectively measured backdoor target** — Use a trigger-conditioned behaviour that static analysis can score without judgement. The speaker used a year-triggered SQL injection: 2024 context gives vulnerable f-string queries and 2023 gives parameterised queries. *When:* You want unambiguous ground truth when testing a detector.
- **Build-gate probe check** — Fix a probe set, run it through base and new checkpoints, compute the delta at one middle layer, push it through the diff SAE, and fail the build if the top backdoor-shaped feature fires. Inspect the feature before blocking. *When:* Shipping fine-tuned models from a pipeline you do not fully control, such as vendor fine-tunes or downloaded checkpoints.

## Numbers
- Full-rank fine-tune: 100% vulnerable code on the trigger year (2024) vs 0% on the benign year (2023), a 100-point swing. Base model untouched: 53% in both years, no swing. ([6:19](https://youtu.be/IQkVMvXQKLY?t=379))
- LoRA fine-tune is leakier: the speaker gives the figure as 100 vs 40 (trigger year vs benign year, as transcribed). ([6:19](https://youtu.be/IQkVMvXQKLY?t=379))
- Training set: 5,000 samples, 60% benign (2023) and 40% poisoned (2024). Evaluation set: 2,500 samples, including 1,000 with no year. ([6:19](https://youtu.be/IQkVMvXQKLY?t=379))
- About 1.6 billion possible combinations from the procedural generator, with over 95% of samples unique by hash check. ([6:19](https://youtu.be/IQkVMvXQKLY?t=379))
- Backdoor isolation score: cross-coder about 0.01 (near random) vs diff SAE about 0.4, a roughly 40x gap with non-overlapping confidence intervals. ([7:47](https://youtu.be/IQkVMvXQKLY?t=467))
- Diff SAE single feature: precision 1 with zero false positives on the best feature; recall about 25% of triggers. ([9:13](https://youtu.be/IQkVMvXQKLY?t=553))
- The diff SAE score stays flat at about 0.4 across four layers, while the cross-coder stays near zero. ([9:13](https://youtu.be/IQkVMvXQKLY?t=553))
- A 4x-expansion SAE matches a 32x-expansion SAE with about 8x fewer features (as transcribed). ([9:13](https://youtu.be/IQkVMvXQKLY?t=553))
- Signal-to-noise gain from subtracting the base activations: about tenfold (speaker's estimate). ([10:14](https://youtu.be/IQkVMvXQKLY?t=614))

## Hot takes
- Watching behaviour (evals and behavioural monitors) cannot catch sleeper backdoors, and the joint-feature interpretability approach most teams reach for is also blind to them.
- The useful signal is in the difference between base and fine-tuned activations, not in the fine-tuned model alone.
- Backdoors are directions in activation space, and the difference is where they live.
- Treat a backdoor check like a unit test and run it on every build.

## Tools mentioned
SmolLM2-360M, sparse autoencoder, LoRA, static analysis

## Relevance to our work
- **agentos** (1/3): AgentOS serves models on vLLM and plans a security pillar (Crucible guardrails). A checkpoint-diff check is relevant only if AgentOS ever loads fine-tuned or downloaded checkpoints. It is not a current need. → *Note the base-vs-finetune delta SAE as a possible optional gate for downloaded fine-tuned checkpoints in the Crucible/security pillar. Read the GitHub repo linked by the speaker before deciding.*
- **general** (1/3): Fine-tune supply-chain risk (vendors, downloaded checkpoints, insiders) is a general concern for any pipeline that ships fine-tuned small models. The method needs a base checkpoint and a probe set, and is cheap enough to run on every build. → *If the team ever ships fine-tuned small models, add a diff-based anomaly check (one middle layer, probe set, build gate) to the pipeline. Start by testing the speaker's open code on a 360M model.*

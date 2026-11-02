# Why Your Agent Disagrees With Itself (And What To Do About It) - Diane Lin, Datadog

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `wEc9aG7cRQc` · [watch](https://youtu.be/wEc9aG7cRQc) · **date:** 2026-08-18 · **length:** 25:38 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Diane Lin · **orgs:** Datadog, Cloudmanate, Zscaler, Alexa, Vicarious, Google DeepMind, Imperial College London, MIT
- **topics:** evals, memory, security-guardrails · **tags:** inconsistency, active-learning, query-by-committee, episodic-memory, semantic-memory, decision-boundary, security-alert-triage, human-in-the-loop, labeling, flip-flop

> Diane Lin (Datadog) on why LLM agents give different verdicts on the same input near the decision boundary, and how to fix it with disagreement-driven active learning plus episodic and semantic memory instead of fine-tuning.

## Summary
The speaker argues that run-to-run inconsistency in LLM agents (same input, different semantic verdict) is mostly a labeling and missing-context problem, not a model bug. Inconsistent cases cluster near the decision boundary, where even human experts disagree and the right label depends on company policy. She proposes applying active learning to LLM agents: select cases by disagreement across repeated runs or models rather than by the model's own confidence, which she says is unreliable. Instead of fine-tuning, she adds the missing context as semantic memory (policy facts) and uses episodic memory (retrieval of similar past human-labeled cases) to resolve recurring cases automatically. Humans then review only what remains and distill their decisions back into semantic memory. On 93 cybersecurity alerts run three times, roughly a quarter flip-flopped without the approach, and about 15% became consistent with it, leaving about 10% still inconsistent. The talk is a practitioner account from a security-triage product built at Cloudmanate, now part of Datadog, with a small sample and no comparison to other methods.

## Key ideas
- **Inconsistency is mostly a label or information problem, not a model problem** — Verdicts flip near the decision boundary, where the right answer depends on company policy or missing context. Human experts disagree there too, and a traditional classifier would struggle as well. The agent is exposing ambiguity that already exists. ([7:51](https://youtu.be/wEc9aG7cRQc?t=471))
- **Flip-flopping cases concentrate in a gray zone near the boundary** — Clear-cut inputs get the same label every run. Borderline inputs, such as a hotel review with mixed sentiment or a few failed login attempts, flip. This makes them a natural target for review. ([5:34](https://youtu.be/wEc9aG7cRQc?t=334))
- **Use active learning, and select by disagreement rather than by LLM confidence** — Classic active learning picks uncertain points for human labeling. The speaker says LLM self-uncertainty is not reliable ('the model doesn't know what it doesn't know'). Disagreement across repeated runs or across several models is a stronger signal for which cases need a human. ([14:02](https://youtu.be/wEc9aG7cRQc?t=842))
- **Prefer adding memory over fine-tuning when the gap is missing context** — Fine-tuning is expensive and slow to iterate on. Instead, the missing policy or preference is written into a knowledge base that the agent retrieves from. Example: a password-spray with no successful login is benign, but one that succeeds is malicious. ([15:03](https://youtu.be/wEc9aG7cRQc?t=903))
- **Episodic memory automates recurring cases; semantic memory holds distilled rules** — Episodic memory retrieves similar past decisions and reuses them without anyone writing out the reasoning. Recurring false positives get handled automatically. Semantic memory holds the distilled domain facts. The two are complementary. ([17:30](https://youtu.be/wEc9aG7cRQc?t=1050))
- **Loop: automate the recurring cases, send the rest to humans, and distill their answers back into memory** — Episodic memory resolves what it can. Whatever still flips goes to human review. The reviewer's decision is then written into semantic memory for next time. Review effort shrinks toward the genuinely novel cases, and the product adapts to each customer's environment. ([19:53](https://youtu.be/wEc9aG7cRQc?t=1193))
- **Small experiment: 93 real alerts, 3 runs each** — Without the approach, about a quarter of alerts flip-flopped. With episodic memory, about 15% became consistent and about 10% stayed inconsistent. Those remaining go to humans. The sample is small and the wording on the 15% figure is ambiguous. ([22:30](https://youtu.be/wEc9aG7cRQc?t=1350))
- **Takeaways: treat disagreement as signal, and don't reach for fine-tuning first** — The speaker's three points: fix the labels and the missing information first; treat each disagreement as a learning opportunity; and use semantic and episodic memory as the alternative to fine-tuning. ([23:31](https://youtu.be/wEc9aG7cRQc?t=1411))

## Techniques
- **Measure consistency with repeated runs** — Run the same inputs N times (the talk uses 3) and count how many flip their label. Use the flip rate as the consistency metric, and average over runs rather than trusting a single eval pass. *When:* Any LLM classification task where a single eval run could hide instability, such as triage or sentiment labeling.
- **Disagreement-based query selection** — Run the same model several times, or several different models, on each item. Flag items where the verdicts disagree and route those to human review. Use this instead of the model's self-reported or token-probability confidence. *When:* Choosing which production outputs to audit when reviewing everything is too costly. Works best when the decision boundary is ambiguous.
- **Semantic memory for policy and preference facts** — Write the missing company rules as facts in a knowledge base that the agent retrieves at decision time, for example 'complaints outside hotel control are positive' or 'failed password sprays with no successful login are benign'. Humans write these after reviewing a flagged case. *When:* The disagreement comes from a missing policy or preference, not from a lack of model capability.
- **Episodic memory as case-based precedent lookup** — Store past human-labeled cases. For a new item, retrieve the most similar past cases and reuse their decision. If nothing similar is found, or the precedents themselves disagree, escalate to a human. *When:* High-volume alert streams with many recurring false positives that a human has already labeled once.
- **Active-learning loop with memory updates** — Cycle through: run the agent, select disagreeing items, have a human label or add context, distill the answer into semantic memory or the episodic store, then re-run. Fine-tuning is optional in this loop. *When:* Running an agent in production where you need ongoing quality control and want it to adapt to a customer without retraining.

## Numbers
- 93 real cybersecurity alerts, each run 3 times ([22:30](https://youtu.be/wEc9aG7cRQc?t=1350))
- About 25% of alerts flip-flopped verdicts without the approach ([22:30](https://youtu.be/wEc9aG7cRQc?t=1350))
- About 15% became consistent with episodic memory (wording is ambiguous: could mean 15% of flip-flopping cases resolved, or 15% of all alerts) ([22:30](https://youtu.be/wEc9aG7cRQc?t=1350))
- About 10% remained inconsistent and went to human review ([23:01](https://youtu.be/wEc9aG7cRQc?t=1381))

## Hot takes
- Inconsistency usually isn't the model's fault; it points to label quality and missing information.
- Model disagreement is a feature to learn from, not a bug.
- Fine-tuning is not the only option; semantic and episodic memory can close the gap.
- LLM self-reported uncertainty is unreliable; disagreement across runs is a better signal.

## Tools mentioned
Datadog

## Relevance to our work
- **agentos** (1/3): MemoryMesh already has tiered cross-session memory and conflict resolution. The episodic precedent pattern (retrieve similar past labeled cases before escalating) could fit there, but the talk is a single product case study with a small sample. → *Prototype an episodic precedent lookup in MemoryMesh for repeated classification decisions, and log flip-flop rate over 3 runs as a metric before and after.*
- **prosharness** (1/3): ProsHarness's plan, critique and debate steps could use disagreement across runs or models as a flag for human review. This is an idea, not a direct change. → *In the ProsHarness plan/critique step, record verdict disagreement across repeated Claude Code runs and surface only disagreeing items for approval.*

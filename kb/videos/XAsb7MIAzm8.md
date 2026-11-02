# Don’t be data poor — Anuj Iravane, Anterior

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `XAsb7MIAzm8` · [watch](https://youtu.be/XAsb7MIAzm8) · **date:** 2026-09-18 · **length:** 16:46 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Anuj Iravane · **orgs:** Anterior
- **topics:** data-engineering, evals, skills-self-improvement · **tags:** synthetic-data, healthcare, PHI, decision-trees, policy-as-code, reverse-generation, round-trip-check, clinician-in-the-loop, skills, agent-harness, data-scarcity, vertical-ai

> Anuj Iravane (Anterior) explains how to generate synthetic medical records when real PHI cannot be kept, by sampling labels and policy reasoning traces first and generating documents backward.

## Summary
Anuj Iravane describes why his healthcare AI company builds synthetic data: its clinical workflows (prior auth, payment integrity, HEDIS) run on scanned fax bundles of PHI that contracts forbid retaining, redacting, or deriving from. Standard LLM one-shot generation of 300-page records lacks diversity because of mode collapse and little pre-training exposure to this data type. His team reverses the forward task: they sample a label and a reasoning trace from a symbolic, decision-tree form of the policy, then generate a patient journey, per-encounter document plans, and finally the documents in layers so context stays small. A refinement loop runs evals such as cross-document consistency and a round-trip check that the generated record still yields the sampled label, so labels are correct by construction. Clinicians can steer generation at any step and own the pipeline as skill files on an internal agent harness, so new document types need no engineering changes. He reports about 90% of their eval datasets are now synthetic, and in a blind review clinicians told synthetic from real only about 60% of the time, which he calls close but not solved. The talk is practitioner-level with concrete design choices, though it has few hard benchmarks and some company framing.

## Key ideas
- **When real data cannot be kept, generate it yourself** — Healthcare evals need very high accuracy (95% is not enough), but the PHI data behind them cannot be retained, reused, redacted, or derived from under contract. The speaker's answer is synthetic data generated in-house. ([2:07](https://youtu.be/XAsb7MIAzm8?t=127))
- **Reverse the inference workflow to get diversity** — Forward task: unstructured records plus policy produce a label. Reverse: sample a label and a reasoning trace first, then generate records conditioned on them. This sidesteps LLM mode collapse on diverse data. ([4:37](https://youtu.be/XAsb7MIAzm8?t=277))
- **Symbolic policy representation gives a controllable sampler** — Policies are modeled as decision trees. Walking them lets you sample reasoning traces deterministically and with more uniform coverage, including rare edge cases that a 200-case production sample would miss. ([5:35](https://youtu.be/XAsb7MIAzm8?t=335))
- **Generate records layer by layer, not in one shot** — Patient invariants lead to an ordered patient journey of events and encounters, then a document plan per encounter, then documents fanned out with the preceding history. This keeps prompts short and lets journeys scale longer than one context window. ([8:22](https://youtu.be/XAsb7MIAzm8?t=502))
- **Round-trip checks give correct labels by construction** — Consistency checks across documents catch contradictions from parallel generation. Re-deriving the label from the generated record and comparing it with the sampled label means ground-truthing can be skipped. ([9:53](https://youtu.be/XAsb7MIAzm8?t=593))
- **Domain experts should own the pipeline logic** — Clinicians steer generation at any step (human-in-the-loop) and write the pipeline as skill files on an internal agent harness. Adding a new document type for a customer needs a skill file, not an engineering change. The speaker calls skills the interface between AI engineers and domain experts. ([11:49](https://youtu.be/XAsb7MIAzm8?t=709))
- **Current use is evaluation, and data is made just in time** — About 90% of eval datasets are now synthetic. Edge cases can be simulated and tested before go-live, without waiting for customer data. ([14:13](https://youtu.be/XAsb7MIAzm8?t=853))

## Techniques
- **Reverse-generation from sampled labels** — Sample a label, then a reasoning trace from a symbolic policy (decision tree). Use these as conditioning input and generate the source documents backward from them. *When:* Your forward task maps unstructured inputs to labels through a known policy, and you need diverse, labeled eval data without a human labeling pass.
- **Coarse-to-fine layered generation** — Build invariants, then an event or encounter timeline, then a document plan per encounter, then fan out to hydrate each document with the history as context. *When:* Generated artifacts are long (for example 300+ page records), and one-shot generation loses diversity or overflows context.
- **Round-trip label verification** — After generating documents from sampled labels, run the task pipeline on them again and compare the output with the original label. *When:* You want labeled synthetic data with no ground-truthing, or you need to check that generated records really match their labels.
- **Cross-document consistency eval in a refinement loop** — Run an LLM judge over all generated documents for contradictions, then feed the findings back to regenerate the affected parts. *When:* Documents are generated in parallel and must agree with each other.
- **Skill files as the domain-expert interface** — Put each pipeline stage (journey, documents, enrichment, evals) in a skill file on an agent harness so non-engineers can edit or add stages. *When:* Domain experts must change pipeline behavior without engineering work, for example for a new customer's document format.

## Numbers
- About 70% of medical communication still happens via fax (speaker's estimate) ([1:07](https://youtu.be/XAsb7MIAzm8?t=67))
- Healthcare accuracy baseline is very high: 95% is described as not good enough ([2:07](https://youtu.be/XAsb7MIAzm8?t=127))
- Medical records are often over 300 pages long ([3:13](https://youtu.be/XAsb7MIAzm8?t=193))
- Example eval over 200 production cases scoring 95% says little about rare edge cases ([6:59](https://youtu.be/XAsb7MIAzm8?t=419))
- About 90% of their eval datasets are already synthetic ([14:13](https://youtu.be/XAsb7MIAzm8?t=853))
- In a blind review, clinicians told synthetic from real only about 60% of the time ([14:13](https://youtu.be/XAsb7MIAzm8?t=853))

## Hot takes
- In healthcare, 95% accuracy is not good enough, so synthetic data must be built with domain experts at the center.
- LLMs suffer from mode collapse on diverse creative data partly because pre-training and post-training do not reward diversity, so one-shot generation is the wrong approach.
- Clinicians, not AI engineers, should drive recursive self-improvement of the data pipeline.
- You do not need a PHI problem to benefit: any data that is ephemeral, sensitive, or expensive to label is a candidate for generation.

## Tools mentioned
internal agent harness (unnamed)

## Relevance to our work
- **agentos** (1/3): SkillForge (mining telemetry into governed skills) could borrow the idea of domain-expert-owned skill files, but the talk does not cover telemetry or skill scoring. → *Skim the talk's skill-file workflow pattern when designing SkillForge's skill format; no code change needed yet.*
- **prosharness** (1/3): The talk runs multi-stage pipelines as skill files on an agent harness with eval gates, which is close to ProsHarness's skill and loop design, but it gives no harness mechanics. → *Consider whether ProsHarness pipeline stages could be stored as editable skill files, so non-coders can change them.*

# Your LLM App Returned 200 OK. It Was Still Wrong. — Marina Petzel, Datadog

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `rTojoVotlD8` · [watch](https://youtu.be/rTojoVotlD8) · **date:** 2026-10-04 · **length:** 18:01 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Marina Petzel · **orgs:** Datadog
- **topics:** observability, governance-compliance, evals, security-guardrails · **tags:** golden signals, LLM cost monitoring, token creep, model drift, cost attribution tagging, prompt injection, PII detection, jailbreak detection, hallucination rate, LLM-as-judge, RAG retrieval metrics, NDCG, user satisfaction, agent observability, Datadog

> Datadog's Marina Petzel argues LLM apps need cost, safety and quality monitoring on top of the golden signals, since a 200 OK can still hide a wrong answer; gives tagging and metric recommendations.

## Summary
The speaker says the golden signals (latency, errors, traffic, saturation) are still necessary but not sufficient for generative AI apps. Three reasons: outputs are non-deterministic so regression tests are not enough, cost is variable with tokens and model choice, and there are new security risks like prompt injection and PII leakage. She proposes a layered monitoring model covering cost, safety and quality. Cost tracking uses mandatory tags at four levels (feature, user, model, endpoint) and watches for token creep, model drift and redundant calls. Safety metrics are prompt injection rate, PII detection rate (target 0%), content moderation score and jailbreak attempts. Quality metrics are hallucination rate, relevance, user satisfaction, answer completeness and RAG retrieval quality. The talk is a practitioner overview with a short product pitch for Datadog agent observability at the end. Most numbers are cited as the speaker's own targets or internal research, and she gives no methodology for them.

## Key ideas
- **Golden signals are necessary but not enough for GenAI apps** — Latency, errors, traffic and saturation still matter, but a 200 OK does not show that the answer was correct or helpful. Quality has to be evaluated continuously in production, because the same prompt can produce different outputs. ([0:13](https://youtu.be/rTojoVotlD8?t=13))
- **LLM cost is variable and needs granular tracking** — Cost depends on token count, model choice and context window size, unlike compute that scales linearly with load. Three cost risks are named: token creep as context grows quietly, model drift when a team moves to a pricier model, and missing caching, which the speaker says can make up to about 70% of spend redundant. ([4:24](https://youtu.be/rTojoVotlD8?t=264))
- **Tag every LLM call at four levels** — Tag by feature (chat, summarization), user or org (for chargeback and abuse detection), model or provider (for comparing real cost per model), and endpoint or environment (region, prod vs staging). The feature tag also shows which features are budget hogs for the roadmap. ([7:15](https://youtu.be/rTojoVotlD8?t=435))
- **Safety needs its own metrics, with zero-tolerance targets for some** — Track prompt injection rate, PII detection rate in outputs (target 0% in production), toxicity or moderation score, and jailbreak attempts. Prompt injection and jailbreak detection use pattern matching or classifiers, with aggressive thresholds. ([9:55](https://youtu.be/rTojoVotlD8?t=595))
- **Five quality metrics to track in production** — Hallucination rate (claims not supported by grounded data), relevance (embedding or BERT similarity to the question), user satisfaction (thumbs, stars, NPS with a target of 80-85% positive), answer completeness (LLM-as-judge), and RAG retrieval quality (top-k accuracy or NDCG). ([12:41](https://youtu.be/rTojoVotlD8?t=761))
- **Monitoring is a layer on top of traditional metrics** — The speaker's framing is that teams keep the traditional signals and add cost, safety and quality dimensions. This is a monitoring checklist, not a new evaluation method. ([15:20](https://youtu.be/rTojoVotlD8?t=920))

## Techniques
- **Mandatory four-level cost tagging** — Attach tags for feature, user or org, model or provider, and endpoint or environment to every LLM call, so spend can be attributed and charged back. *When:* Before cost reviews or chargeback, once several features or teams share one LLM spend pool.
- **Track token creep and model drift as separate alerts** — Watch average context size and the model mix over time, and alert when either rises without a financial review. *When:* When prompts or models change often and monthly spend jumps without explanation.
- **Caching layer to remove redundant completions** — Cache identical or near-identical LLM requests so the same expensive completion is not paid for repeatedly. The speaker cites internal research that a large share of spend is redundant. *When:* When traffic has many repeated or templated queries.
- **Guardrail metrics as blocking thresholds** — Scan inputs for injection with pattern matching or a classifier, scan outputs for PII with NER, run outputs through a toxicity classifier, and block known jailbreak patterns that overwrite the system prompt. *When:* For any user-facing app that handles untrusted input or personal data.
- **LLM-as-judge for completeness, embeddings for relevance** — Use a judge model to score whether the answer fully addresses the intent, and embedding similarity to score relevance to the question. *When:* For continuous quality scoring in production, where human review does not scale.
- **Score RAG retrieval separately** — Measure whether the retrieved documents are relevant, using top-k accuracy or NDCG, separate from answer quality. *When:* When retrieval context grows and it gets harder to pick the right chunks.

## Numbers
- Token creep can raise cost up to 8x as the context window grows (for example 4k to 32k tokens), potentially thousands of dollars per month ([4:24](https://youtu.be/rTojoVotlD8?t=264))
- Opus-class model cost can be up to 15x higher per request than a cheaper model such as Haiku 4.5 ([5:50](https://youtu.be/rTojoVotlD8?t=350))
- Datadog internal research: about 70% of LLM spend is sometimes redundant from repeated identical completions ([5:50](https://youtu.be/rTojoVotlD8?t=350))
- PII detection target: 0% of production outputs ([9:55](https://youtu.be/rTojoVotlD8?t=595))
- User satisfaction target: more than 80-85% positive feedback ([14:02](https://youtu.be/rTojoVotlD8?t=842))

## Hot takes
- A 200 OK from the server is not evidence that an LLM answer is correct.
- PII leakage in production outputs should have zero tolerance.

## Tools mentioned
Datadog agent observability

## Relevance to our work
- **agentos** (2/3): AgentOS already plans budgets, PII scanning and prompt-injection scanning at the proxy, and an L4 observability layer. This talk gives the metric set and tagging scheme for that layer. → *Add feature, user, model and endpoint tags to the Govrix proxy's spend records, and track token creep and cache hit rate as metrics in the Prometheus/Grafana stack.*
- **general** (2/3): The four-level tagging scheme and the cost, safety and quality checklist are a reusable monitoring baseline for any LLM app. → *Read the Datadog agent observability docs for how their tag and metric schema is defined before writing an internal LLM monitoring spec.*
- **prosharness** (1/3): ProsHarness wraps Claude Code runs, so per-run cost and model-drift tracking is relevant. The talk is about production monitoring, though, not agent harness design.

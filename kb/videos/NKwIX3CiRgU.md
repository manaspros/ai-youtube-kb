# Does GenAI "belong" to data scientists? — Phil Hetzel, Braintrust

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `NKwIX3CiRgU` · [watch](https://youtu.be/NKwIX3CiRgU) · **date:** 2026-06-18 · **length:** 18:54 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Phil Hetzel · **orgs:** Braintrust, Slalom Consulting, Databricks, Anthropic, OpenAI, Mistral
- **topics:** enterprise-adoption, evals, product-ux · **tags:** org-structure, ai-native-vs-enterprise, llm-as-judge, agent-evals, human-annotation, prompt-engineering, context-engineering, domain-experts, observability

> Phil Hetzel (Braintrust) argues GenAI agent work should not belong only to data scientists or ML engineers. He says it needs a diverse product team, with domain experts shaping prompts and eval, and data scientists supplying rigorous eval discipline.

## Summary
The speaker, who leads solutions engineering at Braintrust, contrasts enterprises that hand agent work to existing ML or data science platform teams with AI-native companies that build small cross-functional teams. He explains that with GenAI the model is already trained, so the work shifts from training pipelines to evals after integrating an API, and from retraining or feature engineering to changing prompts and context. He argues that agents need functional evaluation across a much broader surface than classic precision, recall and F1, and that they are distributed systems that product engineers are well placed to build. He says domain experts and PMs should control prompts and annotate traces, while data scientists should act as guardrails, including checking LLM-as-judge against labeled data. The talk is mostly opinion and framing, with a light product pitch that he explicitly declines to make.

## Key ideas
- **Enterprises often hand agent work to existing ML or data science teams because 'AI' is in the name. AI-native companies instead use small cross-functional teams that mix product and AI engineering.** — This is the speaker's observation across many customers, not a measured result. He presents it as a pattern, with no judgment attached. ([3:40](https://youtu.be/NKwIX3CiRgU?t=220))
- **With GenAI the model is already trained, so the data pipeline of training and testing a model mostly does not apply. The remaining job is evals after the team integrates an API.** — Anthropic, OpenAI and Mistral run their own testing. The app team still has to evaluate its own product on top of those APIs. ([4:56](https://youtu.be/NKwIX3CiRgU?t=296))
- **In GenAI, behavior changes come from prompts and context rather than from retraining or feature engineering. That makes context engineers, who sit close to real users, important.** — Fine-tuning is rare. The speaker says people closest to the problem can change behavior most directly. ([6:58](https://youtu.be/NKwIX3CiRgU?t=418))
- **Teams that come from ML often focus on precision, recall and F1. Agents need functional evaluation across a much wider surface than these technical metrics cover.** — The speaker says this is the biggest gap he sees when ML engineers judge whether an agent is working. ([9:23](https://youtu.be/NKwIX3CiRgU?t=563))
- **Agents are distributed systems. A supervisor agent can call sub-agents that run on different infrastructure and call other systems, so this is a systems problem.** — Product engineers, who are used to calling APIs and assembling results, are well placed for this. Subject-matter experts and PMs can control prompts and annotate traces to say whether a run was good and why. ([10:45](https://youtu.be/NKwIX3CiRgU?t=645))
- **Data scientists add the most value as guardrails. They can challenge hype, and they can check LLM-as-judge scores against a labeled dataset.** — The speaker warns that LLM judges are just prompts and models, so teams should not believe them by default. Fine-tuning an open model for a specific use case is the most technical area where data scientists add value. ([13:18](https://youtu.be/NKwIX3CiRgU?t=798))
- **The speaker's proposed mix: engineers build the product, domain experts annotate and do prompt and context work, and an eval and observability loop connects production to experiments.** — He ends with the claim that the answer is in the middle and that more people should be brought into the room. ([14:13](https://youtu.be/NKwIX3CiRgU?t=853))
- **In Braintrust's workflow, production data is fed back into the offline eval dataset, and teams track whether automated evals agree with human labels.** — Human labeling and a prompt playground let domain experts take part directly. The team checks whether evals stay aligned with human agreement or drift away from it. ([17:30](https://youtu.be/NKwIX3CiRgU?t=1050))

## Techniques
- **Judge calibration against human labels** — Build a labeled dataset of agent outputs, run the LLM-as-judge on it, and compare with precision, recall and F1. Recheck over time to see if judge and human agreement drifts. *When:* Whenever an LLM judge is used for evals and its scores are being trusted for decisions.
- **Production traces feed the offline eval set** — Sample real production traces into the offline dataset that is used for evaluation, so the eval set keeps up with real user behavior. *When:* Once an agent is live and the offline eval set has gone stale compared with real usage.
- **Domain-expert trace annotation** — Let non-technical experts open agent traces and mark each run as good or bad, with a reason, and feed those labels back into evals. *When:* When the agent's correct behavior depends on domain knowledge that engineers do not have.
- **Prompt playground for non-engineers** — Give SMEs and PMs a playground where they can test their own prompts against the live agent, so the prompt work does not have to go through engineers. *When:* When prompt and context changes are the main lever and the people with domain knowledge are not engineers.
- **Functional eval over technical metrics** — Evaluate whether the agent achieves the user's task end to end, not only component-level classification metrics. *When:* When adapting classic ML evaluation habits to agent systems.

## Hot takes
- Agent development should not default to data science or ML platform teams. It is a product effort that needs a diverse team.
- LLM-as-judge is just prompts and models, so its scores should not be trusted without checking against labeled data.
- ML engineers who default to precision, recall and F1 are measuring the wrong surface for agents.

## Tools mentioned
Braintrust

## Relevance to our work
- **agentos** (1/3): AgentOS runs RAGAS evals on MemoryMesh. The talk's point that LLM-as-judge needs checking against human labels applies to those evals, but the talk gives no method beyond that. → *Label a small sample of MemoryMesh RAGAS outputs by hand and measure how often the judge agrees before trusting the scores.*
- **prosharness** (1/3): ProsHarness uses a plan, critique and debate loop. The talk's advice to validate LLM judges against labels applies to that critique step, but the talk does not describe a specific mechanism. → *Sample ProsHarness Codex critique verdicts and label them by hand to check whether the critic actually catches plan problems.*

# The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `ObTPqBGsEbA` · [watch](https://youtu.be/ObTPqBGsEbA) · **date:** 2026-07-18 · **length:** 37:06 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Sandipan Bhaumik · **orgs:** Databricks, Amazon Web Services
- **topics:** evals, observability, enterprise-adoption, governance-compliance · **tags:** production-ai, eval-set, llm-as-judge, tracing, behavioral-evals, data-foundation, unity-catalog, multi-agent-orchestration, prompt-versioning, incident-playbook, pii-detection, retail-banking-chatbot

> A five-pillar playbook (evaluation, tracing, data foundation, orchestration, governance) for taking enterprise AI agents to production, illustrated with a retail banking chatbot case study.

## Summary
Sandipan Bhaumik, a technical lead for data and AI at Databricks, argues that enterprise AI projects fail after the demo because of three gaps: no observability, no defined evaluation, and no governance or accountability. He proposes five pillars to design for before building: evaluation, tracing, data foundation, multi-agent orchestration, and governance. Evaluation is framed as the specification, with success defined in business numbers and checked by a layered suite (deterministic checks, LLM judges, and behavioral checks on tool calls). Tracing is presented as the basis for debugging, duplicate-call detection, online monitoring and regulator-facing audit trails. He walks through a banking chatbot project where the team built the eval set and metrics first, picked the model in week seven, and later used traces to find a stale policy document in the vector store. The talk ends with an incident playbook and advice on governing growing eval sets, prompt versions and eval cost. Much of the stack detail is Databricks product promotion, but the framework and case lessons are practitioner-grade.

## Key ideas
- **Three gaps sink AI projects after the demo** — The speaker names an observability gap (no trace of what the agent did), an evaluation gap (no agreed business metric), and a governance gap (no owner when the AI fails at 3 a.m.). He says the five pillars are meant to address these. ([2:30](https://youtu.be/ObTPqBGsEbA?t=150))
- **Define success in numbers before choosing a model** — Evaluation is treated as the specification. Targets such as accuracy, false-positive tolerance and deflection rate are set in business terms before any model or feature work. He says the usual pattern of debating models first is backwards. ([7:06](https://youtu.be/ObTPqBGsEbA?t=426))
- **Build a golden eval set from what human agents actually answer** — Domain experts supply real answers to real customer questions, including grey-area and confusing cases. The set is automated so that live responses are scored against it and below-threshold answers go to a human. ([8:05](https://youtu.be/ObTPqBGsEbA?t=485))
- **Three evaluation layers: deterministic, semantic, behavioral** — Cheap regex and classic NER/PII checks come first. LLM judges then score groundedness and relevance. Behavioral checks look at tool calls, loops and duplicate calls. He says teams often skip the third layer. ([9:22](https://youtu.be/ObTPqBGsEbA?t=562))
- **A correct answer can still hide an expensive bug** — In his example, an account-balance answer was right but the agent made three database calls for it, from duplicate calls and retries. That is harmless in a demo and costly at production volume. ([10:49](https://youtu.be/ObTPqBGsEbA?t=649))
- **Traces let you find, alert on and cap bad agent behavior** — Traces record each step (intent, timing, confidence, API calls, retrieval, reasoning, guardrails). Online monitoring can flag duplicate calls and apply a fallback. Failing calls can be retried up to three times, then escalated to a human. Traces also give auditors and regulators a record. ([14:42](https://youtu.be/ObTPqBGsEbA?t=882))
- **Data foundation takes most of the effort, and agents do not forgive bad data** — He says he spends about 60% of project time here. Humans work around wrong report data, but agents answer from it confidently. The data strategy covers question data and tracing data, with catalog metadata and PII tags so the AI gets context. ([14:42](https://youtu.be/ObTPqBGsEbA?t=882))
- **Orchestrator, choreography and human-in-the-loop patterns, plus prompts as change-managed code** — An orchestrator gives central control and logs. Choreography uses a message bus so agents run in parallel with lower latency. Human-in-the-loop is triggered by a confidence threshold. Prompt changes should go through change management with failure reasons recorded, and model upgrades should be re-tested on your own eval set rather than vendor benchmarks. ([19:34](https://youtu.be/ObTPqBGsEbA?t=1174))

## Techniques
- **Business-metric eval spec before build** — Write down the success metric in numbers (accuracy target, deflection rate, latency, tolerable false positives) and the eval set that measures it, before choosing a model or features. *When:* At project kickoff, before any model or feature choice.
- **Living golden eval set seeded from human answers** — Start with a few hundred cases taken from real human support answers, including edge cases. When a production failure is fixed, add that case to the set so it is caught next time. *When:* Any agent that answers customer questions and needs regression protection.
- **Three-layer eval stack** — Layer 1: regex, format and classic NER/PII checks. Layer 2: LLM-as-judge for groundedness, safety and relevance against expected answers. Layer 3: behavioral checks on tool-call count, loops, retries and duplicates. *When:* When designing the evaluation architecture for a production agent.
- **Automated eval pipeline with human review threshold** — Capture each user question and agent response, score it against the eval set, and send anything below a rating threshold to a human reviewer. Then fix the prompt, tool or flow and add the case to the set. *When:* Live production monitoring of an agent.
- **Trace-driven duplicate-call detection and retry cap** — Record every step in traces, flag repeated tool or API calls online, cap retries at three, and send anything beyond that to a fallback or a human. *When:* Agents that call paid or rate-limited APIs at volume.
- **Tiered CI eval runs** — On each prompt change, run a small subset of the eval set. Run the full eval set only on merge to main. This keeps the cost of behavioral evals down. *When:* Prompt or tool changes in a repo with a large eval set and expensive model calls.
- **Prompt versioning as change management** — Treat prompts as code. Require commit messages that state the failure that prompted the change and what it corrects, so each version can be traced later. *When:* Any team that edits prompts in version control.
- **Model selection on your own eval set** — Run each candidate model against your own eval set and compare scores. Keep the system switchable so models can be changed when providers upgrade. *When:* Choosing a model, or re-checking one after a provider upgrade.
- **Incident playbook: detect, diagnose, contain, fix, regress** — Detect with the eval dashboard, diagnose with traces, contain by reverting a prompt or routing to a human, fix the cause, then add the case to the eval suite. Connect the playbook to the existing ITSM alerting. *When:* Defining the response process before a production agent goes live.

## Numbers
- Typical project time spent on the data foundation pillar is about 60% ([14:42](https://youtu.be/ObTPqBGsEbA?t=882))
- Retail banking chatbot received about 20,000 calls per month, about 60% of them simple queries ([24:11](https://youtu.be/ObTPqBGsEbA?t=1451))
- A prior chatbot POC cost about 85k over six months and did not succeed ([25:12](https://youtu.be/ObTPqBGsEbA?t=1512))
- Goal set for the chatbot: the agent handles 60% of simple queries ([25:12](https://youtu.be/ObTPqBGsEbA?t=1512))
- Model was selected in week 7 of an eight-week POC ([25:12](https://youtu.be/ObTPqBGsEbA?t=1512))
- Initial eval set of 200 cases, built from human agents' real answers in weeks 1-2 ([26:34](https://youtu.be/ObTPqBGsEbA?t=1594))
- Accuracy target of around 85% ([26:34](https://youtu.be/ObTPqBGsEbA?t=1594))
- Retry limit of three before escalating to a human ([14:42](https://youtu.be/ObTPqBGsEbA?t=882))
- 47 PII breaches detected during testing by the PII layer ([22:01](https://youtu.be/ObTPqBGsEbA?t=1321))
- Account-balance example: three database calls for one answer, which was correct but wasteful ([10:49](https://youtu.be/ObTPqBGsEbA?t=649))
- Full behavioral eval runs of 300 to 500 rows are expensive to repeat on each prompt change ([33:53](https://youtu.be/ObTPqBGsEbA?t=2033))

## Hot takes
- Every AI conversation starting with 'which model should we use' is backwards; the eval set should decide the model.
- Agents do not forgive bad data the way humans do; they give wrong answers confidently.
- Vendor benchmark leaderboards are not useful for judging a model on your own enterprise data.
- Prompt changes should go through enterprise change management, not a commit straight to main.
- Behavioral evals (tool calls and loops) are the layer most teams skip.

## Tools mentioned
Databricks, MLflow, Delta Lake, Apache Spark, Unity Catalog, Genie, Agent Bricks, Databricks Apps, Mosaic AI, Git, Python, LLM-as-judge, RAG vector database

## Relevance to our work
- **agentos** (2/3): AgentOS already plans PII/injection scanning, a Merkle audit log and RAGAS evals. The talk's behavioral layer (duplicate tool calls, loops, retries) and the growing failure-driven eval set are not clearly covered yet. → *Add a behavioral eval layer that counts tool calls and retries per request from AgentOS traces, and a rule that every production failure becomes a regression case in the MemoryMesh RAGAS set.*
- **prosharness** (1/3): ProsHarness runs plan, critique and debate loops. The tiered CI idea and prompt-change governance are only loosely related to its design. → *When a ProsHarness prompt changes, record the failure that motivated it in the commit message, and consider a small eval subset per change with a full run on merge.*
- **general** (1/3): The eval-first and business-metric-first advice applies to any agent project, but it is mostly well known practice. → *Before choosing a model for the next agent project, write down the success metrics and a 50 to 200 case eval set taken from real answers.*

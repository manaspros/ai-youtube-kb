# The 6 Pillars of an Agentic Harness for Production — Varun Krovvidi, Resolve AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `eXA2tjRZIbY` · [watch](https://youtu.be/eXA2tjRZIbY) · **date:** 2026-10-07 · **length:** 21:05 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Varun Krovvidi · **orgs:** Resolve AI, Grafana, Slack, Microsoft, Google Cloud, OpenAI, Anthropic
- **topics:** agent-architecture, observability, evals · **tags:** on-call, incident-response, root-cause-analysis, causal-reasoning, model-routing, least-privilege, eval-levels, grafana, slack-bot, production-ops, vendor-pitch

> Resolve AI's architecture for production-ops agents (on-call, incidents, background tasks): six pillars covering model routing, context, causal evidence, governed actions, learning loops, and multi-level evals.

## Summary
Varun Krovvidi of Resolve AI argues that running and fixing production systems, not writing new code, takes most engineering time, and that it is cross-domain and harder for AI than code generation. He says generic frontier models look good in demos but crack when scaled across teams and use cases. His answer is a domain harness with six pillars: model orchestration, context engineering, causal reasoning, governed actions, a learning system, and evals. The talk shows a live demo where a Grafana alert in Slack starts an investigation, which correlates code, infrastructure, knowledge bases and observability data. The agent gives a root cause with rejected alternatives and refuses to simply agree with a leading question from the engineer. Much of the talk is product pitch, but the pillar framing and the evidence-chain rule are concrete enough to reuse.

## Key ideas
- **Production operations, not code generation, takes most engineering time, and it is harder for AI.** — Ops work spans on-call alerts, incidents and daily maintenance. It crosses tools and domains, so it lacks the self-documenting, single-domain structure that makes code easy for AI. ([1:38](https://youtu.be/eXA2tjRZIbY?t=98))
- **Generic frontier models break at scale, so a domain harness with six pillars is needed.** — Pillars: model orchestration, context engineering, causal reasoning, governed actions, learning system, and evals. Demos work for one use case, but cracks show up across teams. ([11:06](https://youtu.be/eXA2tjRZIbY?t=666))
- **Route each subtask to the model best suited to it, and keep re-evaluating as models change.** — Different tasks (image reasoning, SQL, logs, deterministic steps, open-ended investigation) favour different frontier models. The orchestration layer has to track model releases. ([12:29](https://youtu.be/eXA2tjRZIbY?t=749))
- **Too much context makes models over-explore; too little makes them under-explore. Aim for the precise amount.** — Large context produces invented hypotheses. Small context hides alternative paths. Telemetry is effectively unlimited, so context selection is the real problem, and it is usually a mix of techniques (for example graph RAG to start, then precise tool queries to avoid burning tokens). ([8:16](https://youtu.be/eXA2tjRZIbY?t=496))
- **Root causes must rest on a causal chain of evidence, otherwise report low confidence and point elsewhere.** — Models are tuned for coherent answers, not causal ones. The system gives a root cause only when it can show the steps that led to the incident. If the data stops short of that, it says so and suggests other directions. ([13:42](https://youtu.be/eXA2tjRZIbY?t=822))
- **Design against sycophancy: the agent answers from its own evidence, not from the engineer's hypothesis.** — In the demo, the engineer pushed a GCP-outage theory and a deployment-error theory. The agent kept its answer tied to its own evidence chain rather than agreeing with the question. ([19:24](https://youtu.be/eXA2tjRZIbY?t=1164))
- **Use least-privilege, tiered permissions (read, write, conditional write) and treat the model as able to pick destructive fixes.** — The speaker says a model may decide that deleting code or data is the cleanest fix. Guardrails should limit what the agent can touch, with explicit conditions for any write. ([9:42](https://youtu.be/eXA2tjRZIbY?t=582))
- **Evals work at five levels: positive and negative feedback, trace-level scoring, comparison against a best engineer, and confidence calibration.** — Each interaction is an eval signal, including whether a user steers the investigation. Traces of the agent's path are scored like an engineer's work. Confidence calibration is measured too. These run on every model change, use case change or architecture change. ([15:06](https://youtu.be/eXA2tjRZIbY?t=906))

## Techniques
- **Alert-as-prompt investigation fan-out** — Treat each incoming alert (here Grafana into Slack) as the prompt. Spawn investigator agents that gather metrics and traces, correlate them with change events and deployments, and search code, infrastructure, knowledge bases and observability data. Return a root cause plus rejected theories. *When:* Use for on-call alerts that arrive in a chat channel and need first-pass triage before a human joins.
- **Evidence-chain gate on root causes** — Accept a root cause only when the agent can lay out the ordered steps of evidence that led to it. Otherwise output it at low confidence and list other lines of inquiry. *When:* Use whenever an agent's diagnosis will drive a human or automated fix, to reduce plausible-but-wrong patches.
- **Per-subtask model routing** — Classify each step of a workflow (image reasoning, deterministic checks, SQL, logs, open-ended hypotheses) and send it to the model that does that kind best. Re-run evals when new models ship. *When:* Use when one workflow mixes task types that different models handle at different quality or cost.
- **Tiered action permissions** — Define what the agent may do at each level (read, write, conditional write), with explicit conditions for writes, and default to the least privilege the scenario allows. *When:* Use for any agent that can touch production systems, especially in regulated industries.
- **Five-level eval stack** — Combine user feedback (positive and negative), trace-based scoring of the agent's reasoning path, a comparison with an expert-engineer baseline, and calibration of stated confidence. Run the full stack against every model, use case or architecture change. *When:* Use to evaluate investigation agents, where the final answer alone does not show whether the reasoning was sound.
- **Anti-sycophancy by design** — Build the agent to base answers only on its own causal chain, so a leading question from the user does not pull it toward the user's theory. Test it by pushing hard on a wrong hypothesis. *When:* Use for any assistant where users will bring hypotheses and the answer needs to be independent.

## Numbers
- Engineers spend about 70% of their time on production systems (running and fixing software), not on generating new code. This is the speaker's own estimate and no source is given. ([1:38](https://youtu.be/eXA2tjRZIbY?t=98))

## Hot takes
- Models are designed to give coherent answers, not causal ones, so an incident agent needs causal reasoning built in.
- Context windows growing does not solve incident reasoning, because more context makes models over-explore.
- Deleting code or data can be the model's 'cleanest fix', so guardrails are a feature requirement, not a bug fix.
- Generation tasks are where AI looks great; tasks with one correct answer are the 'longest mile', and that is where the real work is.

## Tools mentioned
Grafana, Slack, Microsoft Teams, Google Cloud (GCP), graph RAG, knowledge graph

## Relevance to our work
- **prosharness** (2/3): The harness runs Claude Code on long tasks. The tiered permission model, the evidence gate before a plan is accepted, and the eval levels map onto its plan, critique and approval steps. → *Add a per-phase least-privilege tool policy and a check that a plan's claims cite evidence before the critique and approval steps run.*
- **agentos** (1/3): The talk's causal-evidence gate and feedback-driven eval levels are relevant to AgentOS's evals and SkillForge learning loop. It is not about infra or serving. → *Read the evidence-chain and five-level eval ideas (15:06, 13:42) before designing RAGAS-style checks for MemoryMesh answers, and consider requiring cited evidence before answers are returned.*

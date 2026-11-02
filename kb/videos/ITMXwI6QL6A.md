# How Forward Deployed Engineering is done at Ramp — Leo Mehr

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `ITMXwI6QL6A` · [watch](https://youtu.be/ITMXwI6QL6A) · **date:** 2026-08-18 · **length:** 14:05 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Leo Mehr · **orgs:** Ramp, Notion, SAP
- **topics:** enterprise-adoption, software-factory, evals, context-engineering · **tags:** forward-deployed-engineering, scoping, agent-pipeline, intake-agent, token-scaling, ramp, notion-agents, enterprise-customers, human-feedback, rubrics

> Leo Mehr (Ramp) on forward deployed engineering: scope hard before building, then replace each FDE pipeline stage with agents, with evals and good context as the hard parts.

## Summary
Leo Mehr, a director of engineering at Ramp, explains how Ramp's forward deployed engineering (FDE) team works. FDEs sit inside engineering and build the core product and agentic features for the largest enterprise customers, and the team grew from two engineers to about 30. He argues the FDE's main job is scoping, not saying yes to every request: ask who is driving urgency, what workarounds exist, and whether other prospects need the same thing. He gives two cautionary stories, a Friday-night SAP integration request and an iOS/Android reimbursement feature built for a customer who only used iOS. His second principle is to scale with tokens by treating the FDE lifecycle (context gathering, scoping, spec, implementation) as a pipeline where agents can replace each stage. Ramp built a Notion-based agent that asks clarifying questions on incoming FDE requests, cutting reply latency from hours or days to seconds, and he estimates it saves about 20% of scoping time. He says frontier models already handle medium-sized spec-to-feature work well, so the middle of the pipeline is the hard part, and the main open problems are giving agents the right context and judging output quality with evals, rubrics and human feedback. The talk is short and conceptual, with few hard numbers.

## Key ideas
- **FDE's job is not to say yes to every customer request** — Saying yes produces bad software, so the FDE should work out what to build. Ask who is driving urgency, what workarounds exist, whether the customer can use the API themselves, and whether other prospects would benefit. ([2:40](https://youtu.be/ITMXwI6QL6A?t=160))
- **Example: the Friday-night SAP integration request was driven by sales quota pressure, not the customer** — A rep said a strategic logo would only close with an SAP S/4HANA integration. A well-trained FDE first checks what is driving the urgency before building anything. ([4:07](https://youtu.be/ITMXwI6QL6A?t=247))
- **Validate basic assumptions early, such as which mobile platform to build for** — The team spent weeks on iOS and Android reimbursement features, then learned the customer's employees all use iOS. Scoping up front would have caught this. ([5:09](https://youtu.be/ITMXwI6QL6A?t=309))
- **Scale with tokens by making each stage of the FDE lifecycle an agent** — Context gathering, scoping, spec writing and implementation are each a pipeline stage that agents can replace. The speaker frames this as a factory of agents rather than one agent. ([6:11](https://youtu.be/ITMXwI6QL6A?t=371))
- **A clarifying-question agent in front of spec writing cut scoping latency** — Requests in the FDE Requests Slack channel vary a lot in quality. Ramp's Notion-based agent first asked a few questions, then grew into a loop of several rounds with the submitter until the request was ready for a spec. Reply latency went from hours or days to seconds. ([7:40](https://youtu.be/ITMXwI6QL6A?t=460))
- **The spec-to-product end is easy now, but the middle of the pipeline is hard** — The speaker says frontier models can one-shot medium-sized features, so the last step is easier. The middle stage is unformed and needs investment. ([10:24](https://youtu.be/ITMXwI6QL6A?t=624))
- **The FDE's ongoing work is harness quality, output quality, and context** — Each agent step needs a harness that runs smoothly and output checked with evals, rubrics and human feedback. The biggest challenge is giving the agent the product knowledge a PM holds in their head, which docs and help articles do not capture. Skills, memories and tools are part of that. The FDE still owns taste and judgment over the output. ([11:49](https://youtu.be/ITMXwI6QL6A?t=709))
- **Scoping and agent building only work together** — Scoping without an agent factory loses to agent-native competitors. An agent factory without scoping produces a token-maxing slop cannon. ([13:13](https://youtu.be/ITMXwI6QL6A?t=793))

## Techniques
- **Scoping questionnaire before any build** — Before building a customer request, ask: what is driving the urgency, who uses it, have workarounds been exhausted, does the customer have technical resources to call the API directly, and do other prospects need it too. *When:* Any large-customer feature request that sounds urgent or arrives from sales, before engineering starts on a spec.
- **Clarifying-question intake agent before spec** — A Notion-based agent reads each submitted request and asks several rounds of follow-up questions with the submitter until it judges the request ready for a spec. It replaces a human reading and validating every request by hand. *When:* High-volume intake where request quality varies a lot, and humans spend time chasing missing details.
- **Stage-by-stage agent factory for the FDE lifecycle** — Break the FDE workflow into context gathering, scoping, spec, and implementation. Build an agent for each stage, starting from the stages that are easiest to automate, and improve the harder middle stage over time. *When:* When a knowledge-work role is too large to automate in one step and each stage can be measured separately.
- **Per-stage quality checks with evals, rubrics and human feedback** — Give each pipeline output an explicit quality check, such as a rubric, an eval, or human review, so bad output is caught before it moves to the next stage. *When:* Once agents produce intermediate artifacts (specs, scopes) that other steps depend on.

## Numbers
- FDE team grew from two engineers to about 30 engineers across forward deployed, developer API and AI services (org size mentioned as about 30 total) ([0:08](https://youtu.be/ITMXwI6QL6A?t=8))
- Clarifying-question agent cut reply latency on requests from hours or days to seconds ([9:01](https://youtu.be/ITMXwI6QL6A?t=541))
- Speaker's rough estimate: the agent saves about 20% of time spent scoping requests (he says 'I don't know, 20%') ([9:01](https://youtu.be/ITMXwI6QL6A?t=541))

## Hot takes
- Being an FDE does not mean saying yes to every request; the job is to build the right thing.
- Scoping and an agent factory only work together. Agents without scoping produce a token-maxing slop cannon.
- The middle of the agent pipeline, not the spec-to-code end, is where the real difficulty sits.
- Context supply (product knowledge held by PMs, historical data) is the hardest problem, harder than the agent loop.
- Frontier models can one-shot medium-sized features, so the value of an engineer is shifting to scoping, context and judgment.

## Tools mentioned
Notion, Notion Agents, Slack

## Relevance to our work
- **agentos** (1/3): Talk gives no mechanism for AgentOS. Its point that agents need rich context (skills, memories, tools, historical data) overlaps MemoryMesh only loosely. → *Read the 'right context' section at 11:49 for how the speaker frames memory versus skills versus docs. No code change implied.*
- **prosharness** (1/3): ProsHarness runs plan, critique and debate stages. The talk's advice to give each pipeline stage its own rubric or eval fits that structure but adds no new mechanism. → *Add a per-stage rubric check to the plan-to-critique step (talk point at 10:24) and measure whether it catches bad plans before critique.*

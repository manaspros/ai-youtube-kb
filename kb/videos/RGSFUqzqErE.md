# On AI and Knowledge — Pablo Castro, Distinguished Engineer & CVP for AI Knowledge, Microsoft

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `RGSFUqzqErE` · [watch](https://youtu.be/RGSFUqzqErE) · **date:** 2026-07-18 · **length:** 17:35 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Pablo Castro · **orgs:** Microsoft
- **topics:** rag-retrieval, evals, context-engineering, skills-self-improvement · **tags:** intrinsic-vs-extrinsic-knowledge, agentic-retrieval, hybrid-retrieval, knowledge-base-as-mcp, agent-optimizer, learned-knowledge, eval-from-traces, externalized-agent-config, token-efficiency

> Microsoft's Pablo Castro splits agent knowledge into intrinsic, extrinsic and learned, and demos Foundry knowledge bases and an Agent Optimizer that tunes agent config from traces.

## Summary
Pablo Castro (Microsoft, CVP and Distinguished Engineer for AI Knowledge) frames agent knowledge as three kinds: intrinsic (what is in the model weights), extrinsic (company data retrieved at run time), and learned (improvements from observing how work gets done). He argues the intrinsic knowledge in models drove the recent jump in coding tools. For extrinsic knowledge he describes Microsoft IQ, a set of grounding layers covering work documents and chats, analytics assets, agent-owned data and public web content. He says combining retrieval methods beats any single method on real customer scenarios, and that Foundry IQ is layered so users can start simple and drop down to index and vector control. Agentic retrieval, where a model checks whether the information need is met before answering, improves evidence recall and answer completeness in his team's evaluations, and each knowledge base is exposed as an MCP server. For learned knowledge he demos an Agent Optimizer in VS Code: generate a task-adherence eval from traces, run a roughly 45-minute hill-climb over candidate configurations (instructions, tools, skills), then apply the winner by swapping externalized config. The talk is about one-third concept, two-thirds Microsoft product demo, with few hard numbers.

## Key ideas
- **Agent knowledge splits into three kinds: intrinsic (model weights), extrinsic (retrieved company data), and learned (improvements from observed work).** — Intrinsic knowledge from training is what drove the recent jump in coding tools. Extrinsic knowledge is what an agent needs from the organization at run time. Learned knowledge comes from reflecting on how work was done and improving each step. ([1:24](https://youtu.be/RGSFUqzqErE?t=84))
- **Combining retrieval methods beats any single method on real customer scenarios.** — The speaker cites an Azure AI Search evaluation where individual methods trail combined methods, especially on real-world customer data. Vector similarity alone was once expected to be enough, and that turned out to be wrong. ([7:43](https://youtu.be/RGSFUqzqErE?t=463))
- **Layer the retrieval platform so simple use stays simple and experts can go deep.** — At the top, users point the system at PDFs and images and it handles chunking, vectorization, ranking and agentic retrieval. At the bottom, experts control vector quantization, indexing algorithms and lexical retrieval in the same stack. ([7:43](https://youtu.be/RGSFUqzqErE?t=463))
- **Agentic retrieval has the model check whether the information need is satisfied before it returns results.** — For easy queries a single-shot search is enough. For harder ones the agent reflects on the data and decides whether more retrieval is needed. The speaker reports gains on evidence recall and answer completeness, and a tunable effort setting trades latency against quality. ([9:08](https://youtu.be/RGSFUqzqErE?t=548))
- **Learned knowledge becomes a loop: baseline, generate candidates, evaluate, deploy.** — The Agent Optimizer evaluates a baseline, generates candidate configurations, scores them against a rubric, and deploys the best one. The speaker says this captures what is unique about a company's work. ([13:19](https://youtu.be/RGSFUqzqErE?t=799))
- **Externalize agent configuration (instructions, tool definitions, skills) so an optimizer can swap versions.** — Any agent works as long as its configuration is kept outside the code. The optimizer can then apply a better configuration without code changes. The speaker says this is what makes the learning loop practical. ([14:51](https://youtu.be/RGSFUqzqErE?t=891))
- **Optimized instructions emerged from hill-climbing and from reading real user traces, not from hand-writing.** — The demo compares a trivial hand-written baseline with an optimized configuration that includes instructions not written by a person. The speaker says the optimizer reflected on actual agent traces from live use. ([15:45](https://youtu.be/RGSFUqzqErE?t=945))

## Techniques
- **Three-way knowledge split for agent design** — Classify each piece of agent knowledge as intrinsic (model), extrinsic (retrieved at run time) or learned (from observed work), then decide where each one lives. *When:* When planning how an agent gets its context, or deciding which knowledge to ground versus leave to the model.
- **Hybrid retrieval over combined methods** — Run several retrieval methods together and combine their results instead of relying on vector similarity alone. *When:* On real-world data where single methods score poorly, and when evals show combining them helps.
- **Layered retrieval API** — Expose a simple default that handles chunking, vectors and ranking, with optional lower-level knobs such as quantization and index choice. *When:* When some users need a quick setup and others need tuning on the same platform.
- **Agentic retrieval with a satisfaction check** — After retrieval, have the model judge whether the information need is met. If not, retrieve again, and expose an effort setting that trades latency against quality. *When:* For multi-hop or hard questions where recall and answer completeness matter more than one-shot speed.
- **Knowledge base as MCP server** — Publish each knowledge base behind an MCP endpoint so any harness can connect without glue code. *When:* When the same grounded data must serve several agents or tools.
- **Eval generated from traces, then hill-climb the agent config** — Generate a task-adherence eval from existing traces and instructions, then iterate candidate configurations against that rubric, compare with a baseline, and apply the winner. *When:* When an agent has no eval set yet and real traces exist, or when config changes need to be tested before deployment.

## Numbers
- IntelliSense introduced at Microsoft in 1996 (ranking by machine learning arrived about 22 years later, GitHub Copilot about 3 years after that) ([2:25](https://youtu.be/RGSFUqzqErE?t=145))
- A Foundry optimize run takes about 45 minutes in the demo, hill-climbing candidates against an eval rubric ([14:51](https://youtu.be/RGSFUqzqErE?t=891))
- Agentic retrieval improves evidence recall and answer completeness over single parts in the speaker's team evals (no numeric values given) ([9:08](https://youtu.be/RGSFUqzqErE?t=548))

## Hot takes
- Vector cosine similarity alone was never going to be enough for retrieval; combined methods are required.
- Learned knowledge from agent traces is what differentiates a company, and it can be captured automatically by tuning agent configuration.

## Tools mentioned
Microsoft Foundry, Foundry IQ, Azure AI Search, Work IQ, Fabric IQ, WebIQ, Agent Optimizer, Foundry Toolkit for VS Code, GitHub Copilot, MCP

## Relevance to our work
- **agentos** (2/3): MemoryMesh already does hybrid BM25 plus pgvector retrieval; the talk's agentic satisfaction check and evidence-recall measure are a concrete addition to it. → *Add an agentic sufficiency check after MemoryMesh hybrid retrieval, and measure evidence recall and answer completeness before and after on the RAGAS eval set.*
- **general** (2/3): Covers context engineering (externalized config, layered knowledge), agent evals generated from traces, and the learned-knowledge loop, all on the recurring interests list. → *Read the Foundry Agent Optimizer docs for how the task-adherence eval is generated from traces, and compare it with our own eval generation for agents.*
- **prosharness** (1/3): The talk stresses externalized agent config so an optimizer can swap instructions, tools and skills. ProsHarness wraps Claude Code and could benefit from the same separation. → *Review whether ProsHarness plan and skill config could be kept external so a candidate-and-score loop can swap them.*

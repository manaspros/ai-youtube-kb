# AI tools for Forward Deployed Engineering — Vasuman Moza, Varick Agents

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `l0FLhNqBOic` · [watch](https://youtu.be/l0FLhNqBOic) · **date:** 2026-08-18 · **length:** 20:23 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Vasuman Moza (Voss), JD Pruitt · **orgs:** Varick Agents, Cursor, Factory, Anthropic, OpenAI, NetSuite, Microsoft Dynamics, SAP, Salesforce, Granola, Kimi, MIT Technology Review
- **topics:** enterprise-adoption, product-ux, training-finetuning-rl, rag-retrieval · **tags:** forward-deployed-engineering, enterprise-agents, process-reengineering, human-in-the-loop, dependency-graph, knowledge-graph, entity-resolution, post-training, rl-environment, systems-of-record, roi, varick-os

> Varick Agents explain why process understanding, not model execution, is now the bottleneck, and describe the forward-deployed engineering agent they built for it.

## Summary
Vasuman Moza, CEO of Varick Agents, argues that models and harnesses now execute knowledge work well, so the constraint is how deeply a team can understand a specific business and redesign its processes around AI. He says forward-deployed engineers (FDEs) should map how work really runs, including failure paths, then decide which steps are automated, human-in-the-loop, or manual. Varick builds agents on top of existing systems of record (NetSuite, Dynamics, SAP, Salesforce) instead of asking clients to migrate. Head of engineering JD Pruitt describes the FDE agent in three stages: an engagement assistant for FDEs (built because uploading about 150 pages to Claude gave slow, verbose, incorrect analysis), a workflow agent embedded in their platform, and an autonomous agent that is still in development. The technical core is a dependency graph of company processes, a post-trained open-source model for analysis writing, and an RL environment that trains the model to use custom graph-traversal tools such as identity matching and cycle detection. Much of the talk is company pitch and hiring, and the performance claims come without evaluation data.

## Key ideas
- **Execution is no longer the bottleneck; understanding a specific business is.** — The speaker says models and tool harnesses now complete end-to-end tasks well. The hard part is extracting each client's context, since the same department works differently across industries. ([1:31](https://youtu.be/l0FLhNqBOic?t=91))
- **Map the failure paths, not just the documented golden path.** — Documentation covers the normal flow and maybe an edge case or two. Real work moves when things go wrong, e.g. an AP lead hands exceptions to a colleague who takes four days to reconcile a PO against an invoice. ([4:20](https://youtu.be/l0FLhNqBOic?t=260))
- **Adding AI to a broken process does not produce ROI.** — The speaker's explanation for weak pilot results is that AI gets bolted onto processes it does not understand. He argues the work must be redesigned around AI. ([4:20](https://youtu.be/l0FLhNqBOic?t=260))
- **Split each process into autonomous, human-in-the-loop and manual steps.** — The change must be familiar enough for adoption but different enough to capture value. Example: of 8 steps, 4 run autonomously, 3 need human review, and 1 stays human, based on risk and whether an agent adds measurable value. ([5:45](https://youtu.be/l0FLhNqBOic?t=345))
- **Build agents on top of systems of record instead of requiring migration.** — Enterprises are tied to NetSuite, Dynamics, SAP or Salesforce. A client quoted spending $5M and five years on a NetSuite migration, so Varick's platform layers agents, governance and evals over those systems. ([7:08](https://youtu.be/l0FLhNqBOic?t=428))
- **Give FDEs an assistant that handles context load, then embed it in the build tool.** — The first version answers questions over meeting notes, documents and slides, including whether two name spellings are the same person. The second version sits inside the workflow builder and flags missing edge cases and process owners. A third autonomous version that handles client change requests is still in development. ([12:48](https://youtu.be/l0FLhNqBOic?t=768))
- **Model company processes as a dependency graph, and expect cycles.** — Enterprise workflows are mostly linear with loops. The team uses a dependency graph as the single source of truth so that no person acts before their dependencies have approved. ([15:21](https://youtu.be/l0FLhNqBOic?t=921))
- **Post-train for judgment on detail, and train retrieval with graph tools in RL.** — Frontier models write verbose analysis that does not separate what matters from what can be skipped, so the team post-trains open-source models. Retrieval is a separate problem: the team trains a model in an RL environment with custom tools for identity matching and for finding redundancy cycles or DAG violations in the knowledge graph. ([16:38](https://youtu.be/l0FLhNqBOic?t=998))

## Techniques
- **Failure-path process interviews** — Embed engineers with each process lead and ask what happens when things go wrong, not only the documented path. Record the real handoffs, delays and workarounds. *When:* Before automating any operational workflow, especially in finance, procurement or other non-technical departments.
- **Per-step autonomy split** — For each step, assign one of three modes: fully autonomous, human-in-the-loop, or human-only. Base the choice on risk and on whether an agent would add measurable value at that step. *When:* Scoping an automation project so that ROI is captured without removing human checkpoints where risk is high.
- **Dependency graph as shared state** — Represent people, processes and approvals as a graph of dependencies. Detect cycles and DAG violations. Use the graph as the source for agent context. *When:* Enterprise workflows with many handoffs where agents must know who owns what and what must happen first.
- **Post-training an open model for analysis style** — Start from an open-source model and post-train it on the desired balance of detail and clarity, since frontier models tend to be verbose. *When:* Producing long analyses for non-technical clients where frontier output is too wordy or misses what the client cares about.
- **RL environment with domain traversal tools** — Expose custom tools (for example, check whether two records are the same person, or detect redundancy cycles) inside an RL environment so the model learns to traverse a messy knowledge graph and fetch the right context. *When:* Retrieval over a noisy enterprise knowledge graph where generic search returns the wrong entities.
- **Assistant embedded in the authoring tool** — Run the same assistant inside the workflow builder so it checks edge cases and ownership while a human builds the configuration. *When:* Human-authored workflow or configuration where missing edge cases are the main source of errors.

## Numbers
- MIT review: 95% of generative AI pilots fail to reach production (speaker calls it semi-outdated) ([4:20](https://youtu.be/l0FLhNqBOic?t=260))
- 87% of AI pilots do not produce measurable ROI or do not ship to production (speaker's second statistic, unattributed) ([4:20](https://youtu.be/l0FLhNqBOic?t=260))
- Example reconciliation step takes four days of cycle time (PO vs. invoice) ([4:20](https://youtu.be/l0FLhNqBOic?t=260))
- Example split of an 8-step process: 4 autonomous, 3 human-in-the-loop, 1 human-only ([5:45](https://youtu.be/l0FLhNqBOic?t=345))
- Client quote: spent $5 million and five years migrating to NetSuite ([7:08](https://youtu.be/l0FLhNqBOic?t=428))
- Point solutions (e.g. one sales step) deliver about 5-10% ROI; department-wide transformation is claimed to deliver 25%, 50%, 75% ROI (vendor's own claim, no methodology given) ([11:20](https://youtu.be/l0FLhNqBOic?t=680))
- Prior workflow: about 150 pages of documentation uploaded to Claude, roughly two-minute waits, output described as verbose and incorrect ([12:48](https://youtu.be/l0FLhNqBOic?t=768))

## Hot takes
- Knowledge work is almost entirely solved; designing how work gets done around AI is the next bottleneck.
- Operations will be centered around AI rather than around humans.
- Frontier models have no concept of which details a client cares about, so consultants' judgment is what open models must be trained to copy.
- Most AI pilot failures come from putting AI on top of broken processes, not from the models.
- Enterprises will not migrate off their systems of record, so agents have to be built on top of them.

## Tools mentioned
Varick OS (in-house platform), Claude, Codex, Granola, Kimi (open-source base model, named as K2.6), NetSuite, Microsoft Dynamics, SAP, Salesforce

## Relevance to our work
- **prosharness** (2/3): The per-step split (autonomous, human-in-the-loop, human-only) maps onto ProsHarness approvals and checkpoints, and the talk gives a rationale for it. → *Add an explicit autonomy label (auto, approval-gated, manual) to each step of ProsHarness plan output, chosen by risk and value, so the harness knows where to pause for phone approval.*
- **agentos** (1/3): MemoryMesh needs entity identity and conflict handling. The talk's approach of exposing identity-match and cycle checks as explicit tools is relevant, though the talk gives no evaluation. → *Check whether MemoryMesh's GraphRAG path has an explicit same-entity check and a conflict or cycle check, or whether it relies only on retrieval.*
- **general** (1/3): The talk pairs entity identity matching with graph-cycle detection as tools for context retrieval. This is relevant to the entity-resolution and data-quality interests, though the talk is pitch-heavy. → *For entity-resolution work, test a model with explicit identity-check and conflict-check tools against retrieval alone, measuring on a labeled set.*

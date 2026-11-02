# Citation Needed: Provenance for LLM-Built Knowledge Graphs — Daniel Chalef, Zep AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `H7puB0RwJMM` · [watch](https://youtu.be/H7puB0RwJMM) · **date:** 2026-08-18 · **length:** 20:54 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Daniel Chalef · **orgs:** Zep
- **topics:** memory, data-engineering, governance-compliance · **tags:** provenance, lineage, knowledge-graph, temporal-graph, agent-memory, right-to-be-forgotten, deduplication, entity-resolution, graphiti, zep

> Daniel Chalef (Zep) on why LLM-built knowledge graphs need provenance modeled as a graph, covering lineage through merges, contradictions, tagging, and deletion.

## Summary
Daniel Chalef of Zep argues that LLM pipelines synthesize facts non-deterministically, so the link from an output back to its sources is easily lost. He says storing one source ID on a fact breaks once entities merge, facts get overwritten, and many sources feed one fact. His fix is to model provenance as the graph itself: raw episodes are nodes, derived entities and facts link back to them, and tracing a fact is a graph walk. The talk covers keeping lineage correct under merges and contradictions, inheriting tags from sources for trust filtering, and deleting only facts with no remaining support. He also describes Graphiti's ingestion pipeline (single-shot extraction, then de-duplication and de-confliction that leans on non-LLM methods where possible). He closes by arguing that file-based markdown memory breaks down on provenance in multi-user, multi-agent settings. The talk gives no benchmarks, and the cost claims are not quantified.

## Key ideas
- **LLM synthesis destroys the paper trail** — Outputs from LLM pipelines are summaries, extracted facts, or records that may not appear verbatim in the sources. Provenance (how and why an artifact was built) is needed for compliance, debugging, judging trust, and deciding what to delete. ([0:08](https://youtu.be/H7puB0RwJMM?t=8))
- **A single source ID per fact breaks under LLM pipelines** — This works for deterministic warehouse pipelines. With LLMs, many facts are synthesized from several sources, entities get merged (e.g. two similar names), and new data invalidates old facts, so the pointer keeps changing underneath. ([2:38](https://youtu.be/H7puB0RwJMM?t=158))
- **Lineage should be an evolving graph, not a log** — Links between facts and sources are stored as graph relationships that survive mutation. Episodes are nodes, entities are extracted from them, and a fact is hydrated from two entities plus the edge between them. An append-only log becomes hard to manage at scale. ([3:42](https://youtu.be/H7puB0RwJMM?t=222))
- **Merges union source links and contradictions invalidate rather than overwrite** — When two entities merge, the merged node must keep the source links of both or lineage is silently lost. When new data contradicts a fact, the edge gets an invalid-at date and the episodes that caused the change are attached to it, so the history of why it changed is kept. ([4:45](https://youtu.be/H7puB0RwJMM?t=285))
- **Tag at ingestion and let tags inherit down the graph** — Tagging episodes once (e.g. as EHR records) makes every derived entity and fact inherit the tag, so retrieval can filter for verified sources during the graph walk. For facts with several parents, the all-verified versus any-verified policy belongs to the application, not the graph. ([6:50](https://youtu.be/H7puB0RwJMM?t=410))
- **Delete a derived fact only when no remaining source supports it** — For retention and right-to-be-forgotten requests, lineage shows which facts depend on the deleted source. A fact with other supporting episodes survives, and only facts left with zero supporting episodes are removed. ([8:58](https://youtu.be/H7puB0RwJMM?t=538))
- **Ingestion uses one LLM extraction pass, then deterministic de-duplication** — Extraction pulls entities, relations and candidate subject-verb-object facts in a single LLM call. De-duplication and de-confliction then run, and the speaker says they prefer classic IR/NLP methods (hashing, entropy) over LLM calls there because they are cheaper, faster and more deterministic. ([15:17](https://youtu.be/H7puB0RwJMM?t=917))
- **Markdown or file memory breaks down on provenance** — Editing lines in a file loses the reason for each change. The speaker says file memory can work for single-user desktop use but fails for multi-agent, multi-user, multi-source enterprise problems. ([17:45](https://youtu.be/H7puB0RwJMM?t=1065))

## Techniques
- **Provenance as graph edges** — Store raw episodes as nodes. Derive entities and facts as nodes or edges with links back to every source episode. Answer 'where did this come from' with a graph walk from the fact to its episodes. *When:* Facts are synthesized from several sources by an LLM, and you need lineage for audit, debugging or trust scoring.
- **Merge-safe lineage** — When entities are merged, union all source links from both. When a fact is contradicted, set an invalid-at timestamp on the edge and link the triggering episodes, instead of deleting it. *When:* The store keeps changing (entity merges, contradictory updates) and lineage must survive every mutation.
- **Ingestion-time tagging with inheritance** — Attach classification tags (e.g. source type, verified flag) to episodes at ingestion. Derived entities and facts inherit them. Apply the all-or-any policy for multi-parent facts in application code at retrieval. *When:* Agents must filter facts by source trust, and one tagging action should cover everything derived from that source.
- **Lineage-based deletion** — For a deletion request, find facts derived from the target episodes. Remove only facts that have no remaining supporting episodes, and keep facts that still have other sources. *When:* Retention or right-to-be-forgotten requirements apply to only some of a fact's sources.
- **Single-shot extraction plus deterministic dedupe** — Use one LLM call to extract entities, relations and subject-verb-object fact triples. Then dedupe entities and reconcile facts with non-LLM IR/NLP techniques such as hashing and entropy-based checks, reserving LLMs for cases that need them. *When:* Cost and latency of graph construction matter, and you want repeatable de-duplication results.

## Numbers
- Healthcare example: one fact synthesized from 3 sources (EHR record, PDF lab report, intake chat typed by the patient). ([1:37](https://youtu.be/H7puB0RwJMM?t=97))
- Deletion example: 3 source episodes, one (intake chat) deleted. The allergy fact survives because 2 parent episodes still support it, while the contact-preference fact (derived only from the deleted source) is removed. ([8:58](https://youtu.be/H7puB0RwJMM?t=538))
- Speaker says lineage and provenance are expensive, and graph construction in Graphiti is costly, but gives no cost, latency or accuracy figures. ([11:07](https://youtu.be/H7puB0RwJMM?t=667))

## Hot takes
- Storing a source ID on a derived fact is not enough for LLM pipelines, because synthesis, merges and mutations break the pointer.
- File-based markdown memory breaks down on provenance in multi-user, multi-agent, multi-source settings.
- Entity dedupe and fact reconciliation should use deterministic IR/NLP methods wherever they can, not LLM calls.

## Tools mentioned
Graphiti, Zep, Vector similarity search, Full-text search, BFS graph traversal

## Relevance to our work
- **agentos** (2/3): MemoryMesh already lists conflict resolution and provenance as goals. This talk gives a concrete model: facts linked to source episodes, merge-safe lineage, invalidate-not-delete on contradiction, and lineage-based deletion for retention. → *Design a provenance model for MemoryMesh facts: store each derived fact with links to its source episodes, union source links on entity merge, mark contradicted facts with an invalid-at time plus the causing episodes, and delete a fact only when no source remains. Read the Graphiti repo's ingestion and invalidation code as a reference.*

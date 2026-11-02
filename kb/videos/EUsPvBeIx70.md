# Semantic Blindness: 500,000 Sensors Confused an LLM - Raahul Singh & Vanč Levstik, Phaidra

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `EUsPvBeIx70` · [watch](https://youtu.be/EUsPvBeIx70) · **date:** 2026-07-18 · **length:** 16:25 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Raahul Singh, Vanč Levstik · **orgs:** Phaidra
- **topics:** rag-retrieval, data-engineering, agent-architecture, context-engineering · **tags:** entity-resolution, structured-retrieval, planner-resolver, hierarchy-indexing, semantic-blindness, LLM-vs-code, industrial-iot, data-centers, set-operations, software-3.0

> Phaidra engineers explain "semantic blindness": why RAG and LLM-only lookups fail on 400K+ equipment names, and how a hierarchy-based planner plus deterministic set-resolver stays accurate with flat cost at data-center scale.

## Summary
Phaidra builds AI agents that answer questions about AI data-center equipment. Naive approaches (LLM over all names, vector search over names, sharded parallel LLM calls) break down at scale, with hallucinated and dropped equipment and output failures from frequency penalties. Their fix scales with hierarchy depth rather than instance count: a compact summary of the equipment tree goes to the LLM, which emits a structured search plan (scope plus filter or name pattern), and a deterministic resolver builds pre-indexed subsets and applies set intersections. They report correctness falling from about 80% to about 30% for the old approach as scale grew from 64 to 460,000 GPUs, versus 100% for the new approach, with zero failures on 66 real cases across six production systems. Cost per query is roughly flat at about 9,000 tokens. The closing argument is to keep the LLM for ambiguous parsing and synthesis and move structured logic into code, which inverts Karpathy's Software 3.0 trend for mature systems.

## Key ideas
- **Semantic blindness: LLMs and vector search fail on huge sets of near-identical names** — Names differ by one character (chiller6 vs chiller7). Embedding search loses recall. LLMs hit a frequency penalty when they list many similar tokens and their guardrails shut output down. Naive RAG and naive LLM lookup both fail as scale grows. ([0:00](https://youtu.be/EUsPvBeIx70?t=0))
- **Divide-and-conquer sharding with parallel LLM calls still fails** — Sharding the equipment list across parallel LLM calls produced poor recall, phantom equipment and silently dropped items. For mission-critical systems this erodes user trust. ([3:46](https://youtu.be/EUsPvBeIx70?t=226))
- **Scale with hierarchy depth, not instance count** — Physical infrastructure is a tree. Depth grows slowly while width grows fast. A 1 GW site with over a million nodes can be described by a short, fixed list of layers (about four to reach a GPU, chiller or switch), so the LLM's context stays roughly the same size. ([5:06](https://youtu.be/EUsPvBeIx70?t=306))
- **LLMs should plan the search, not perform it** — The LLM turns a vague query into a structured plan: a scope (for example, a subtree such as data hall 11) plus a filter (for example, running hot) or a name pattern. A deterministic resolver then executes it. The LLM never reads the full name list. ([6:26](https://youtu.be/EUsPvBeIx70?t=386))
- **Pre-indexed subtrees and set intersection give exact recall** — Build pre-indexed subsets by location and by how equipment interacts. Answer each part of the query as a set, then intersect. Set logic gives perfect recall regardless of how fuzzy the user's phrasing is. ([7:47](https://youtu.be/EUsPvBeIx70?t=467))
- **Pattern-based fallback for very vague queries** — When a query is vague, the LLM proposes naming or data patterns to match, and the backend runs them. The LLM sees a small, roughly constant number of tokens, not a list that grows with the system. ([8:57](https://youtu.be/EUsPvBeIx70?t=537))
- **Two or three step pipeline instead of an agent loop** — Query goes to planner LLM, then the deterministic resolver, then the result set. Avoiding a multi-step agentic loop keeps cost flat. ([10:20](https://youtu.be/EUsPvBeIx70?t=620))
- **Head-to-head production evals show correctness holds with scale** — Same LLM model and data, three runs per case. The old approach went from about 80% correct at 64 GPUs to about 30% at 460,000 GPUs. The new approach held 100% across tests, including 66 cases on six real production systems with zero failures. ([11:21](https://youtu.be/EUsPvBeIx70?t=681))
- **Karpathy's 1.0 to 3.0 framing run in reverse for AI-native systems** — Legacy software drifts from deterministic code toward prompts. The speaker's advice is to start with an LLM for the whole flow, then move any structured, rule-bound part (hierarchy, set logic, counting, dedup, anything that must be reproducible) into code. Keep the hard judgment in the LLM and give it those tools. ([12:52](https://youtu.be/EUsPvBeIx70?t=772))

## Techniques
- **Hierarchy summary as LLM context** — Describe the system tree by its layer structure (a short finite list of levels) instead of listing every node. The size of the summary stays nearly the same as the number of instances grows. *When:* Large, well-structured domains with a tree or graph, such as data centers, org charts, or inventories with millions of entities.
- **LLM emits a structured search plan; deterministic resolver executes it** — The LLM returns structured output: a scope (which subtree or set to collect), filters to apply, or patterns over names or data. Code builds the sets, applies filters, and intersects results. *When:* Fuzzy natural-language queries over large entity sets where recall and reproducibility matter more than free-form reasoning.
- **Pre-indexed subtrees for set operations** — Precompute subsets by location and by relationship (for example, all GPUs in a data hall as one subtree). Answer each query clause as a set lookup, then take the intersection. *When:* Filtering on combinations of attributes across very large sets, where exact reproducible results are needed.
- **Two- or three-step planner/resolver pipeline in place of an agent loop** — One planning LLM call, then deterministic resolution, then optional synthesis. No repeated tool-calling loop. *When:* Production systems where per-query cost must stay flat and bounded as data grows.
- **Pattern-based search for vague queries** — Ask the LLM to output naming or data patterns to match, and run them against the index in code instead of passing names into context. *When:* Vague user phrasing over large name lists, where the naming convention is consistent enough to match.
- **Head-to-head eval against the old system at increasing scale** — Same model and data, multiple runs per case, measure correctness and token cost at several sizes (64 up to 460,000 units), plus real production cases. *When:* Proving a redesign is production-ready before it reaches customers.
- **Move deterministic work out of the prompt** — Audit each step: if it can be written as a structure or rules (set logic, counting, dedup, reproducible filters), implement it in code. Keep the LLM for ambiguous parsing, judgment and the final answer. *When:* Any AI-native system with structured data, once a prompt-only prototype works but fails at scale.

## Numbers
- Old LLM approach correctness: about 80% at 64 GPUs, falling to about 30% at 460,000 GPUs ([11:21](https://youtu.be/EUsPvBeIx70?t=681))
- New approach: 100% correctness across all tests at every scale, including 66 real-production cases on six systems with zero failures ([11:21](https://youtu.be/EUsPvBeIx70?t=681))
- Old approach tokens for one evaluation pass at 1 GW scale: about 116 million, with errors still present ([11:21](https://youtu.be/EUsPvBeIx70?t=681))
- New approach tokens for the same pass: about 390,000 (roughly 300x fewer) ([11:21](https://youtu.be/EUsPvBeIx70?t=681))
- New approach cost per query: about 9,000 tokens, flat whether the site has 64 GPUs or 460,000 ([11:21](https://youtu.be/EUsPvBeIx70?t=681))
- 1 GW AI factory: 400,000+ GPUs, and over a million nodes in the equipment graph ([1:18](https://youtu.be/EUsPvBeIx70?t=78))
- Hierarchy depth: about four layers to reach a GPU, chiller or switch ([5:06](https://youtu.be/EUsPvBeIx70?t=306))

## Hot takes
- Keeping structured data logic in an LLM is the wrong tool for large, well-structured systems, and the trend should run from 3.0 back to 1.0 as a system matures.
- Naive RAG and vector search over entity names fail at production scale.
- Sharded parallel LLM calls for recall produce hallucinated and dropped items and should not be relied on.

## Relevance to our work
- **general** (2/3): Strong, reusable lesson: keep the LLM for ambiguity and synthesis, and move structured logic into code. The head-to-head scale eval method is also reusable. → *Apply the 'LLM plans, code resolves' split to entity-resolution and data-quality work where names are near-identical, and benchmark it against a naive LLM-over-all-names baseline at several sizes.*
- **agentos** (1/3): The hierarchy-plus-deterministic-resolver pattern could inform entity or knowledge-bucket lookup in MemoryMesh, but the talk is about one domain (data-center equipment) and the numbers are vendor-internal. → *When designing MemoryMesh hybrid retrieval, add a check that structured filters are answered by set operations in code, not by the LLM reading names.*

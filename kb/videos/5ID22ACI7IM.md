# Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `5ID22ACI7IM` · [watch](https://youtu.be/5ID22ACI7IM) · **date:** 2026-05-18 · **length:** 1:41:25 · **format:** workshop · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Peter Werry, Brandon · **orgs:** Unblocked
- **topics:** context-engineering, memory, rag-retrieval, security-guardrails · **tags:** context engine, satisfaction of search, conflict resolution, expert graph, social graph, access control, permission-aware retrieval, token efficiency, output tokens, planning context, workshop, vendor pitch

> Peter Werry and Brandon (Unblocked) argue that agents need a "context engine" that understands org history, permissions and conflicts, not just MCP access to data, then run a hands-on social-graph workshop. Much of it is product pitch.

## Summary
The speakers argue that wiring many MCP servers or naive RAG gives agents access to org data but not understanding of relationships, the reasons behind decisions, or which sources are true. They list three myths (naive RAG is enough, MCP wiring is enough, a bigger context window fixes it) and name "satisfaction of search" as the failure where agents stop at the first plausible hit. Their lessons cover recency-vs-code conflict resolution, surfacing unresolved conflicts to humans, access-controlled retrieval, and not caching or recycling past answers. A central idea is the "expert" or social graph, built from PR review and contribution edges, used as a pivot point to load an expert's distilled history into the agent's seed context. The speakers report one internal comparison (2.5 hours and 21M tokens without the engine, 25 minutes and 10M with it) and warn that the numbers came from Claude and may be unreliable. The second half is a workshop that builds a social-graph tool on a local repo, and the Q&A is mostly about Unblocked's product.

## Key ideas
- **Access is not understanding** — Wiring up many MCP servers gives an agent data access, but not the relationships between data, how it got there, or why it is the way it is. The speaker's team first tried this and the agent clobbered legacy code it did not understand. With the context engine, it kept backward compatibility. ([8:17](https://youtu.be/5ID22ACI7IM?t=497))
- **Satisfaction of search** — Borrowed from radiology. Agents stop at the first plausible match in Notion, Confluence or code and miss the real nuggets, such as a rejected Slack discussion or an incident report. The speaker's fix is to search across sources and to model history, including deleted information. ([11:10](https://youtu.be/5ID22ACI7IM?t=670))
- **Conflict resolution needs more than recency** — Recency alone fails because people's docs and chats drift from how the system works. The team then biased toward the main branch as truth. That fails too, because what matters is where the work is going, not only where it has been. Conflicts that cannot be resolved should be surfaced to humans, not hidden. ([19:01](https://youtu.be/5ID22ACI7IM?t=1141))
- **Access controls must flow up into answers** — A private Slack channel is used only when the person asking has access to it, and the answer stays private to them. For synthesis across boundaries, the speaker proposes compartmentalized pockets, with group-ID tags on synthesized facts. ([17:02](https://youtu.be/5ID22ACI7IM?t=1022))
- **Do not cache answers or feed past answers back in** — Code, docs and the reasons behind them change constantly, so a cached answer goes stale. Feeding prior answers back as context lets a misbehaving model pollute its own context and regress toward the mean. ([24:48](https://youtu.be/5ID22ACI7IM?t=1488))
- **Expert distillation as a pivot point** — A social graph built from PR review edges and contribution counts finds the experts for each code area. Their history, decisions and Slack and PR comments are distilled into memory and loaded as seed context. It directs the rest of an agentic retrieval loop. The speaker's claim is that this beats vector search alone. ([59:49](https://youtu.be/5ID22ACI7IM?t=3589))
- **Front-load high-signal context to cut correction loops** — The speaker's claim is that wall-clock time is driven by correction loops. A wrong first output forces the human to loop again and again. Better context at the start reduces the number of loops, and so reduces output tokens and time. ([1:32:12](https://youtu.be/5ID22ACI7IM?t=5532))

## Techniques
- **Compartmentalized, permission-tagged retrieval** — Keep retrieval inside access scopes such as per-repo or per-channel. Tag any synthesized fact with the group IDs of its sources, and return it only to requesters who hold all of those groups. Build cross-boundary synthesis up from there. *When:* Multi-tenant or enterprise corpora where private channels, secret repos or HR data sit next to public ones.
- **Ingestion-time tags plus runtime judge for conflicts** — Tag related facts at ingestion so they can be de-conflicted and ranked against each other. At runtime, pass the remaining conflicting items to a judge with explicit criteria. If the judge cannot resolve them, show both to the human, and record the human's reply as a weighted signal. *When:* Sources contradict each other, such as a doc vs the code, or two teams' decisions.
- **Expert graph from contribution edges** — Build a procedural graph from PR review and authorship edges, with incremental updates. Optionally cluster by vectorized code ownership and LLM summaries. Rank experts per code path, distill their history into memory, and load that as the first context for a new task. *When:* A new contributor or agent is entering an unfamiliar code area and needs to know who decides and what was tried before.
- **Focus-repo-biased two-stage retrieval** — Count each person's PR contributions per repo to find their focus repos. Run a deep retrieval on those repos, then a shallow retrieval on the rest, and weight results toward the focus repos. *When:* Very large orgs with many repos, where a broad search floods the context.
- **Feedback weighted by source trust** — Let users reply or flag an answer as not helpful, with a reason. Weight a flag by how trustworthy the flagger is, for example an expert vs a new hire, before it becomes task memory. *When:* Building a memory that improves from user corrections without letting noise overwrite good facts.
- **Split cadence by source type** — Use real-time updates where webhooks exist, and cron jobs for sources without them. Make the graph build incremental. Run slow, high-cost distillation (such as best-practice mining) weekly. *When:* Mixed sources where some push events and some must be polled, and some summaries change slowly.

## Numbers
- Context window in about 2022 was 8K tokens, which pushed tools toward local code completion. ([4:01](https://youtu.be/5ID22ACI7IM?t=241))
- Speaker-reported internal task: without the context engine, 2.5 hours and 21M total tokens. With it, 25 minutes and 10M tokens. The speaker warns that these numbers came from Claude and may be inaccurate, and that the trend is what matters. ([21:55](https://youtu.be/5ID22ACI7IM?t=1315))
- Same task re-run in the workshop: about 2h25m without the engine vs 25 min with it, mainly because the no-context run needed about four human correction loops. ([1:31:12](https://youtu.be/5ID22ACI7IM?t=5472))
- Total token use on a large task dropped by about 50% with the context engine (21M to 10M), partly because doom loops were avoided. ([1:33:15](https://youtu.be/5ID22ACI7IM?t=5595))
- Speaker estimates about 90% of agent wall-clock time goes to context collection, and only a small part to code writing. This is an estimate, not a measurement. ([1:29:47](https://youtu.be/5ID22ACI7IM?t=5387))
- Internal sentiment score is about 60 on a -100 to 100 scale, roughly 0.75 to 0.8 normalized. The speaker says this is a vibes metric. ([1:28:27](https://youtu.be/5ID22ACI7IM?t=5307))
- Feedback volume: hundreds of feedback items for teams of 100 to 200 people, and fewer for teams of about 20 to 30. ([40:31](https://youtu.be/5ID22ACI7IM?t=2431))
- Full social-graph build back to the start of 2025 takes about 15 minutes. The speaker advises a shorter time range for the workshop. ([43:59](https://youtu.be/5ID22ACI7IM?t=2639))
- Vendor telemetry on clients: Claude Code is the most used, followed by Cursor. Claude Desktop shows up more than expected. ([57:11](https://youtu.be/5ID22ACI7IM?t=3431))

## Hot takes
- Access does not equal understanding. Wiring up MCP servers is not a context engine.
- Naive RAG and a bigger context window do not solve organizational context.
- Never cache context-engine answers, and never feed past answers back as context.
- Output tokens, not input tokens, are what drag down agent performance, according to the speaker.
- Bleeding-edge agent practice is yesterday's news in six months.
- The speaker's own product is the case study, and the workshop funnels toward it.

## Tools mentioned
Claude Code, Cursor, Codex, GitHub Copilot, MCP, Slack, Microsoft Teams, Sentry, Datadog, GraphRAG, pgvector-style vector retrieval, Composio, Notion, Confluence

## Relevance to our work
- **agentos** (2/3): MemoryMesh faces the same conflict-resolution and provenance problem. The talk's advice to rank by source authority, surface unresolved conflicts, and filter by access tags applies directly. → *In MemoryMesh conflict resolution, rank conflicting memories by source authority (code and main branch) and recency, and surface unresolved conflicts to the user instead of silently picking one. Also tag each memory with access groups and filter retrieval by the requester's groups.*
- **prosharness** (2/3): The talk says planning is where extra context pays off most, and that correction loops drive wall-clock time. This fits ProsHarness's plan, critique and debate flow. → *Before the plan step, inject a short org-context block into the plan prompt (owners of touched paths, previously rejected approaches). Compare plan rework loops against a no-context run on the same 3 to 5 tasks.*
- **general** (2/3): Strong, practical framing of satisfaction of search, conflict surfacing, and not caching answers. Useful for any agent that answers questions over org data. → *Read the transcript's section on conflict resolution and the no-caching rule before designing any agent that answers questions over internal docs or chat.*

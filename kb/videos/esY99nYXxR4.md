# How we solved Context Management in Agents — Sally-Ann Delucia

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `esY99nYXxR4` · [watch](https://youtu.be/esY99nYXxR4) · **date:** 2026-05-18 · **length:** 16:17 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Sally-Ann Delucia · **orgs:** Arize
- **topics:** context-engineering, memory, multi-agent, evals · **tags:** context-window, truncation, summarization, long-session-evals, sub-agents, agent-memory, tool-result-retrieval, trace-data, prompt-caching, claude-code

> Arize's product head explains how their Alex agent escaped a context-growth loop: head/tail truncation with the middle moved to memory, long-session evals, and sub-agents for heavy data search.

## Summary
Sally-Ann Delucia, head of product at Arize and a core contributor to their in-app agent Alex, describes how the team escaped a loop where Alex analyzing trace data kept overflowing its own context. She argues context engineering means deciding what the model sees, not just fitting a token limit, and that context management is a product/UX problem as much as an engineering one. Naive first-100-characters truncation broke follow-up questions, and LLM summarization was too inconsistent because nothing controlled what was kept. The approach that stuck is head-plus-tail truncation with the middle stored in memory and retrievable on demand, so "context decides what the model sees, memory decides what survives." They test long sessions by seeding 10 turns and checking the 11th, since failures appeared late in long chats. Heavy search work moved into sub-agents so the main conversation stays light. Open problems they named: real long-term memory, no principled context budget or quality metrics, huge inputs still hitting provider limits, and not yet optimizing for prompt caching.

## Key ideas
- **Context engineering is choosing what the model sees, not just fitting under a token limit.** — The speaker says the best strategy lets an agent remember what it needs and forget what it doesn't. Context is what made agents succeed or fail, so the focus moved from prompts to context. ([2:14](https://youtu.be/esY99nYXxR4?t=134))
- **Naive truncation breaks reasoning and follow-ups.** — Keeping only the first 100 characters of a long blob let single questions work, but follow-ups looked like new conversations. The agent could not reference earlier results. ([5:16](https://youtu.be/esY99nYXxR4?t=316))
- **Plain LLM summarization was rejected because nothing controlled what was kept.** — Summaries were inconsistent and left the choice of what matters to the LLM, which the team found unreliable. It was the obvious choice and they were surprised it failed. ([6:22](https://youtu.be/esY99nYXxR4?t=382))
- **The shipped design is head + tail truncation with the middle moved into a memory store.** — They keep the system prompt and the start and end of the context, store the middle, and let the agent fetch any stored piece back if it judges it important. Duplicate or superseded tool results are dropped, keeping the latest. ([6:22](https://youtu.be/esY99nYXxR4?t=382))
- **Long conversations fail late, so they need their own eval.** — Users rarely restart chats, and conversations grew from under 10 turns to 20+. Failures surfaced only when users reported them, so they built long-session evals: load 10 turns, then test the 11th. ([7:43](https://youtu.be/esY99nYXxR4?t=463))
- **Heavy data work belongs in sub-agents, keeping the main chat light.** — Search over hundreds of spans produced many queries and intermediate reasoning steps. Delegating that to a sub-agent and returning only the result kept the main conversation small. They say this was a game changer and now use sub-agents widely. ([9:59](https://youtu.be/esY99nYXxR4?t=599))
- **Context management is still heuristic, with no budget or quality metrics yet.** — The head/tail rule is a heuristic and they have no principled context budget or clear measure of context quality. They rely on evals to judge whether the right context was kept, and long-term memory is still unbuilt. ([11:59](https://youtu.be/esY99nYXxR4?t=719))
- **Their stored-history design was similar to Claude Code's, and prompt caching is not yet a focus.** — Full messages sit in a database with IDs, and a tool lists IDs with position and a preview so the agent can fetch what it needs. The speaker said Claude Code's leaked design used similar truncation and compression. Asked about cache invalidation, they said they have not optimized for it yet. ([15:18](https://youtu.be/esY99nYXxR4?t=918))

## Techniques
- **Head + tail truncation with middle spill to memory** — Keep the system prompt, the first ~100 characters, and the last ~100 characters of the context. Store the removed middle in a memory store. Keep only the latest result of repeated tool calls. *When:* Long, tool-call-heavy agent runs where summarization is inconsistent and the agent still needs to recover older details on demand.
- **Reference-by-ID retrieval tool** — Store every message in a database with an ID. Give the agent a tool that lists IDs with their position in the conversation and a short preview, then let it fetch the full message by ID. *When:* When full history cannot fit in context but the agent must still reach earlier turns or tool results precisely.
- **Long-session eval (seed N turns, test turn N+1)** — Build a fixture of about 10 prior turns, then run a probe question on the 11th turn that depends on early content. Failing cases become regression tests. *When:* When context bugs show up only deep into a conversation and users find them before the team does.
- **Sub-agent for data-heavy search** — The main agent delegates search and multi-step querying to a sub-agent that holds the raw data. The sub-agent returns only the result, and the main agent keeps the conversation going. *When:* When a task generates many intermediate queries or large results (for example, searching hundreds of spans) that would bloat the main conversation.

## Numbers
- Naive truncation keeps only the first 100 characters of context. ([5:16](https://youtu.be/esY99nYXxR4?t=316))
- Shipped design keeps about 100 characters from the head and 100 from the tail, with the middle stored. ([6:22](https://youtu.be/esY99nYXxR4?t=382))
- Long-session eval seeds 10 turns and tests the 11th. ([7:43](https://youtu.be/esY99nYXxR4?t=463))
- Conversation length grew from under 10 turns per chat at launch to users pushing past 20 turns. ([11:59](https://youtu.be/esY99nYXxR4?t=719))
- Alex has 40+ built-in skills and advanced planning. ([1:01](https://youtu.be/esY99nYXxR4?t=61))

## Hot takes
- Agents don't fail because of prompts; they fail because of context.
- Context management is a product and UX problem, not just an engineering one.
- Summarization, the obvious choice, did not work for them.

## Tools mentioned
Alex (Arize's in-product agent), Arize observability platform, Claude Code (referenced, not used by speaker)

## Relevance to our work
- **agentos** (2/3): Head/tail truncation with a spilled middle and ID-based retrieval maps onto MemoryMesh's tiered cross-session memory and gives a concrete context policy for the L2A layer. → *Benchmark a head+tail truncation policy with the middle spilled to MemoryMesh against a summarization baseline on long agent sessions, adding a fetch-by-ID tool.*
- **prosharness** (2/3): ProsHarness runs long Claude Code sessions with checkpoint/resume, so context decay late in a run and sub-agent offload apply directly. → *Add a long-session eval to ProsHarness: replay about 10 turns of a checkpointed run, then probe the 11th for details that should have survived context trimming.*

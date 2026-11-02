# This Tool Fixes AI Coding at Scale with 70x Fewer Tokens (Graphify)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `WNru_PFycT8` · [watch](https://youtu.be/WNru_PFycT8) · **date:** 2026-05-02 · **length:** 5:17 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack
- **topics:** token-cost-efficiency, context-engineering, coding-agents, memory · **tags:** graphify, knowledge-graph, codebase-map, tree-sitter, token-savings, claude-code, cursor, repo-understanding

> Better Stack demo of Graphify, a tool that builds a relationship graph of a repo and its docs so Claude Code answers from the map instead of re-reading files. Claims over 70% fewer tokens; the evidence is one small-repo anecdote.

## Summary
The host argues that coding agents waste tokens re-learning a repo on every question because they see a flat pile of files with no stored structure. Graphify is presented as a memory layer: run it once (the demo runs it from Claude Code) and it produces an interactive HTML graph, a written report, and a knowledge base of nodes and edges covering code, docs, diagrams, and even audio or video. The host says it uses tree-sitter for code structure and an LLM for meaning, then clusters the result, and that everything stays local. In a small demo repo, a question about how auth connects to the API layer dropped from about 14,000 tokens to a couple hundred once the map existed. The host contrasts edge-based relationships ("this function calls that one") with RAG's similarity chunks, and notes that edges are labeled Extracted, Inferred, or Ambiguous with a confidence level. Drawbacks named: a slow, token-costly first run on large document sets, an early project with unknown long-term support, imperfect relationships, and overkill for tiny repos. The video is a 5-minute overview with no benchmark, config, or flags shown.

## Key ideas
- **Agents re-learn the repo on every question, which burns tokens and yields answers that are close but not right** — The host's framing is that a raw file pile has no stored connections or memory, so each question starts from zero. Replacing the raw files with a generated map is the proposed fix. ([0:00](https://youtu.be/WNru_PFycT8?t=0))
- **Graphify is a persistent memory layer built as a map of the repo, not a prompt trick** — One command (graphify, run through Claude Code in the demo) yields a clickable graph of nodes and connections, plus a markdown report the agent can read on later questions. ([1:01](https://youtu.be/WNru_PFycT8?t=61))
- **Question cost drops sharply once the graph exists (anecdotal)** — For an auth-to-API-layer question on a small demo repo, the host reports about 14,000 tokens before and a couple hundred after the first generation. This is one repo and one question, not a benchmark. ([1:47](https://youtu.be/WNru_PFycT8?t=107))
- **Hybrid pipeline: deterministic structure plus LLM semantics** — The host says tree-sitter parses code structure, an LLM extracts meaning, and results are grouped into clusters. Inputs beyond code include PDFs, diagrams, audio and video. ([1:47](https://youtu.be/WNru_PFycT8?t=107))
- **Relationships are edges (calls, depends-on), not similarity-ranked chunks** — The host contrasts this with RAG's find-similar-text approach. Each edge carries a provenance label (Extracted, Inferred, Ambiguous) so the reader knows how far to trust it. ([2:57](https://youtu.be/WNru_PFycT8?t=177))
- **Updates are incremental and the output persists across sessions** — The generated markdown is reused on later questions, and only changed content is reprocessed. The host ties this to context that sticks rather than starting over. ([2:57](https://youtu.be/WNru_PFycT8?t=177))
- **Honest downsides: first run cost, early-stage risk, imperfect edges, overkill for small repos** — The first run on a document-heavy project is slow and costs tokens, and the project is young. The host advises skipping it for small scripts. ([3:47](https://youtu.be/WNru_PFycT8?t=227))

## Techniques
- **Pre-built repo knowledge graph as the agent's map** — Run the Graphify command once from inside Claude Code so it indexes the repo, docs and diagrams. Then ask questions that point the agent at the generated graph or markdown report (e.g. 'what connects auth to the API layer?') instead of having it re-read source files. The demo shows no flags or config, only the bare command. *When:* Medium to large repos or mixed code-plus-docs projects where the same structural questions recur (onboarding, cross-module impact, auth or data flow). Skip for tiny repos, where the host says the setup is overkill.
- **Hybrid extraction: parser for structure, LLM for meaning** — Use a deterministic parser (the host names tree-sitter) to pull definitions, calls and imports, and an LLM pass to infer semantic links from docs and comments. Cluster the resulting graph into communities for navigation. *When:* When pure AST edges miss intent that lives in documentation or diagrams, and when you need the graph to cover non-code artifacts too.
- **Label edges with provenance and confidence** — Tag every relationship as Extracted (directly observed), Inferred (model-derived), or Ambiguous, and have the consuming agent weight or flag answers by that label instead of treating all edges as facts. *When:* Any time an LLM-generated map will feed a later agent's reasoning, so that inferred links are not presented as ground truth.
- **Incremental re-indexing with a persisted report** — Keep the generated markdown report on disk and rebuild only the nodes whose source files changed, so later questions reuse the earlier analysis. *When:* Repos that change steadily and are queried repeatedly, where full re-indexing on every change would waste tokens.

## Numbers
- Token usage cut by 'over 70%' (speaker's figure; the title says 70x, which the speaker does not state) ([0:00](https://youtu.be/WNru_PFycT8?t=0))
- Auth-to-API question: about 14,000 tokens before the graph, 'maybe a couple hundred' after the first generation, on a small demo repo (single anecdote) ([1:47](https://youtu.be/WNru_PFycT8?t=107))
- First run is slow and token-costly on repos with many documents; later runs use a cache ([3:47](https://youtu.be/WNru_PFycT8?t=227))

## Hot takes
- The title's '70x fewer tokens' is not a figure the speaker measured. The only stated number is 'over 70%', plus one small-repo anecdote (about 14k tokens down to a couple hundred).
- The host says 'all locally, nothing leaves the machine', yet the meaning-extraction step is an LLM pass. The video never says which model or endpoint runs it, so check that before pointing it at proprietary code.
- No benchmark, no config, no flags: the demo is a single run on a toy repo. Treat the savings as plausible for large repos, not demonstrated.

## Tools mentioned
Graphify, Claude Code, Cursor, tree-sitter

## Relevance to our work
- **agentos** (2/3): Graph-plus-report memory for code overlaps with L2A MemoryMesh GraphRAG and with the knowledge-bucket idea, and the confidence-labeled edges are a pattern AgentOS could reuse. → *Compare the Graphify approach (tree-sitter structure + LLM edges with Extracted/Inferred/Ambiguous labels) against MemoryMesh's GraphRAG extraction for a code-repo knowledge bucket, measuring tokens per question.*
- **prosharness** (2/3): ProsHarness runs Claude Code for long tasks and plans against repos, so repeated file re-reading is a token cost it already pays. A persistent repo map is a direct candidate for its plan step. → *Benchmark a generated repo map against re-reading files in a ProsHarness planning step, counting tokens per question on one real repo, before adopting it.*

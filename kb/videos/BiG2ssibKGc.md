# Stop babysitting your agents... — Brandon Waselnuk, Unblocked

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `BiG2ssibKGc` · [watch](https://youtu.be/BiG2ssibKGc) · **date:** 2026-06-18 · **length:** 18:54 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Brandon Waselnuk · **orgs:** Unblocked
- **topics:** context-engineering, memory, rag-retrieval · **tags:** context engine, satisfaction of search, naive RAG, social graph, expert graph, conflict resolution, permissions, token optimization, MCP, CLAUDE.md, AGENTS.md, background agents, code review, caching pitfalls, research packet

> Unblocked's Brandon Waselnuk argues agents need a runtime context engine, not more MCP access or static docs: exhaustive retrieval, surfaced conflicts, a social graph, and hard-won lessons.

## Summary
Brandon Waselnuk of Unblocked argues that coding agents start with zero org context, so developers end up babysitting them to supply it. He lays out a ladder from "you are the context engine" to a curated static layer (CLAUDE.md, AGENTS.md) to a runtime context engine that searches across many SaaS sources and returns a compact answer. He debunks three myths: naive RAG, connecting more MCP servers, and bigger context windows all fail because they lack exhaustive search and reasoning over entities and relationships. A side-by-side demo showed an MCP-only agent passing compile checks while producing a change that would have broken production. He then shares three lessons from building the engine: optimizing for access was wrong, hiding conflicts between sources was harmful, and caching answers went stale within a day. The talk closes with a shared-engine architecture across Slack, ticket triage, background agents, and code review, plus a social/expert graph demo that he says will be open-sourced.

## Key ideas
- **Agents spawn with zero org context, so the real work is building context for them** — He frames a new agent as a brilliant engineer who knows nothing about the org. Developers become the context engine by hand, which is the babysitting problem. ([0:00](https://youtu.be/BiG2ssibKGc?t=0))
- **Static context repos are a stage, not the end state** — Curated files like CLAUDE.md and AGENTS.md help, but someone must maintain them and they lack runtime data. A context engine must pull live data from many SaaS systems at query time. ([2:32](https://youtu.be/BiG2ssibKGc?t=152))
- **The gap is understanding, not access** — Giving agents MCP pipes to tools does not give them understanding. Agents need entities, relationships and awareness of what they do not know, like a new hire who does not know a service exists. ([3:56](https://youtu.be/BiG2ssibKGc?t=236))
- **Naive MCP-only agents pass checks but miss org-specific constraints** — In a comparison on one prompt, the MCP-only run compiled, but the senior engineer said it would have broken the system. The engine-backed run avoided that. Only the framing of the comparison is shown; exact figures are not stated in the transcript. ([5:22](https://youtu.be/BiG2ssibKGc?t=322))
- **Satisfaction of search makes naive RAG and single-hit retrieval unreliable** — Like a radiologist who stops at the first finding, an agent takes the first plausible pattern and stops. Exhaustive search is needed to find root causes and the correct implementation pattern. He also argues that 1M-token windows do not fix reasoning across entities. ([6:49](https://youtu.be/BiG2ssibKGc?t=409))
- **A social graph pivots retrieval to the asker and resolves source conflicts** — Knowing who is asking (their codebases, PR history, collaborators) scopes results. Conflicts are settled by weighing sources: code may say one thing, but a CTO's Slack message saying it was implemented wrong usually wins. Permissions carry over via OAuth, so private chats only show to their owner. ([8:16](https://youtu.be/BiG2ssibKGc?t=496))
- **Three hard lessons: do not optimize for access, do not hide conflicts, do not cache answers** — Early on, they assumed the model would figure it out, which did not happen. They also let agents silently pick between conflicting sources. Caching good answers for latency gave stale results within about 24 hours, so he recommends against it. ([11:56](https://youtu.be/BiG2ssibKGc?t=716))
- **One engine serves many surfaces, then gets customized with skills and SOPs** — The same engine answers Slack questions in an Ask Engineering channel with confidence scoring, supports ticket triage and incidents, and backs background agents that need to run headless. Teams customize via a cookbook of skills, SOPs and custom agents. ([14:18](https://youtu.be/BiG2ssibKGc?t=858))
- **Use the engine across the whole loop: research packet, planning, execution, review** — The agent queries the engine over MCP, receives a research packet, spawns explore subagents against the right areas, and writes a plan that follows existing patterns such as a factory pattern. The engine is also reused during code review. ([16:38](https://youtu.be/BiG2ssibKGc?t=998))

## Techniques
- **Exhaustive retrieval before first-hit answers** — Have the context layer search every relevant source and reason across results before returning, instead of letting the agent stop at the first matching pattern. *When:* Integrations, root-cause work, or any task where the first plausible match may be incomplete.
- **Research packet before planning** — Run a retrieval pass that returns a compact packet (patterns, modules, conventions, owners), then pass that packet to the planner and to explore subagents rather than letting them grep from scratch. *When:* New features or integrations in a large codebase, where grep-based discovery is token-expensive and misses patterns.
- **Expert / social graph built from the code repo** — Derive authorship and review relationships per area (who authors, reviews and works with whom) from the repo. Use the asker's identity to scope and prioritize retrieval. *When:* Large orgs with many owners, where the right answer depends on who is asking and which area they own.
- **Surface conflicts instead of silently picking** — When sources disagree (code vs chat vs docs), return the conflict with provenance and a weighting, rather than letting the agent choose one. *When:* Any corpus where code, docs and chat routinely contradict each other.
- **Permission-preserving delivery over MCP** — Expose the context layer through MCP with the user's OAuth identity so answers respect the asker's access to each source, including private chats. *When:* Ingesting Slack, Teams or other private-message sources in a multi-user org.
- **Confidence-gated auto-answering** — Let a bot in a team channel score its confidence on incoming questions and answer only above a threshold. *When:* Ask-engineering or support channels where repeat questions are common.
- **No answer caching for latency** — Avoid caching answers to speed up repeat questions, since the underlying facts change. Re-query the sources instead. *When:* Any system whose answers depend on data that changes on a daily scale.

## Numbers
- Example customer orgs can have around 20,000 members, which the speaker says needs very different context handling ([8:16](https://youtu.be/BiG2ssibKGc?t=496))
- Permissions and data governance typically start to matter once a company is around 20+ people ([9:11](https://youtu.be/BiG2ssibKGc?t=551))
- Comparison of MCP-only vs context-engine runs on one prompt. Bar charts were shown, but no specific figures are stated in the transcript ([5:22](https://youtu.be/BiG2ssibKGc?t=322))
- Cached answers were stale within a roughly 24-hour window, which is why the speaker advises against caching ([13:23](https://youtu.be/BiG2ssibKGc?t=803))

## Hot takes
- Naive RAG over docs is not context; agents stop at the first plausible match (satisfaction of search).
- Connecting more MCP servers gives access, not understanding.
- A 1M-token context window does not solve reasoning across entities and relationships.
- Caching correct answers for latency is a mistake because the answer goes stale.
- Surfacing conflicting sources is better than letting the agent silently choose one.

## Tools mentioned
Claude Code, MCP, Codex, Anthropic API, AWS Bedrock, CLAUDE.md, AGENTS.md, Zendesk, Slack, Microsoft Teams

## Relevance to our work
- **agentos** (2/3): MemoryMesh (L2A) already has conflict resolution and provenance; the talk's lesson that hidden conflicts cause arbitrary agent choices applies directly to how it returns contradicting memories. → *In MemoryMesh conflict resolution, return both conflicting facts with provenance and a weighting rather than picking one; test on a case where code and a chat message disagree.*
- **prosharness** (2/3): The talk's research-packet step (retrieve patterns and owners before planning, then pass them to planners and explorers) maps onto ProsHarness's plan stage before critique and debate. → *Add an optional research-packet step before the plan stage and check whether plans then reuse existing patterns, comparing against plans made without the packet.*
- **general** (2/3): Covers context engineering, which is a recurring interest. The 'exhaustive before first hit' and 'no answer caching' lessons are testable claims for agent evaluation. → *Add a test case to agent evals where the correct answer requires finding a second source after the first plausible match, and check whether the agent stops early.*

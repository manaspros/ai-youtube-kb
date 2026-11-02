# How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `qdAkxLoYNI8` · [watch](https://youtu.be/qdAkxLoYNI8) · **date:** 2026-09-18 · **length:** 18:36 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Peter Werry · **orgs:** Unblocked, Sonar
- **topics:** context-engineering, rag-retrieval, pr-code-review, mcp-and-tools · **tags:** context engine, organizational context, satisfaction of search, source citations, code review agent, engineering social graph, Document Query Engine, context engine simulator, compounding loops

> Unblocked vendor talk arguing coding agents need an organizational context engine over code, PRs, Slack and docs, with cited sources; one live comparison, mostly product pitch.

## Summary
Peter Werry of Unblocked argues that agents behave like new hires who reset their knowledge every task, so access to a wiki or CLAUDE.md is not enough and agents stop at the first plausible hit (the "satisfaction of search" idea). He says dumping the whole codebase into a large context window also fails because it distracts the agent and wastes tokens. The proposed fix is a context engine that pulls from code, pull requests, Slack and docs and returns its sources, so the agent and the human can check where an answer came from. In a live demo, Claude Code produced an optimization plan for an internal calculator with and without the engine; with it, the run took about a minute at sub-dollar cost versus about two minutes and more cost without. The talk also shows a review agent that uses past PR comments and reviewer seniority to surface comments, a cloud agent that opened a fix PR linked to a Slack thread about a model switch, and an engineering social graph built from review relationships. Evidence is anecdotal: one live task, one customer quote about 50% fewer tokens, and no benchmark. The session ends with two open-source items and a context engine simulator for trying the with/without comparison.

## Key ideas
- **Agents are like new employees who re-onboard on every task, so they must rediscover the codebase, tests, deploy process and team conventions each time.** — Access to information does not equal understanding. A wiki or CLAUDE.md tells the agent what exists but not where the relevant piece is or how the pieces interact. ([1:13](https://youtu.be/qdAkxLoYNI8?t=73))
- **Agents stop at the first plausible match (the radiology 'satisfaction of search' analogy), and they do not distill how dependencies and architecture fit together.** — The speaker uses this to argue for doing the discovery legwork ahead of time, not per task. ([4:40](https://youtu.be/qdAkxLoYNI8?t=280))
- **Stuffing the whole codebase and architecture docs into the context window does not work, even at roughly 1M tokens.** — The claimed failure mode is distraction and wasted tokens and time. Task-specific context flow matters more than volume. ([5:53](https://youtu.be/qdAkxLoYNI8?t=353))
- **Answers should show their sources so the next step can jump to the underlying context and humans can correct the knowledge base.** — Sources come back to the agent, which then knows where to look next. The speaker presents this as trust-building, and says agents increasingly do this checking themselves. ([7:25](https://youtu.be/qdAkxLoYNI8?t=445))
- **The value of context is compounding, not the upfront cost on a short task.** — Without context, the agent discovers the wrong things, then operates on a wrong plan or wrong assumptions and loops. This is the speaker's main argument for why the engine pays off on longer work. ([11:55](https://youtu.be/qdAkxLoYNI8?t=715))
- **The review agent uses best practices derived from PR data and weights comments by the reviewer's seniority or expertise.** — Past comments from senior engineers are surfaced as signals to boost important review comments. ([13:18](https://youtu.be/qdAkxLoYNI8?t=798))
- **A cloud agent with organizational context debugged a drop in review issues, traced it to a model switch, and opened a fix PR linked to the Slack conversation behind it.** — The speaker says the drop followed a switch to Claude 4.8. This is a single anecdote from an internal experiment, not a measured result. ([14:15](https://youtu.be/qdAkxLoYNI8?t=855))
- **An engineering social graph built from review relationships clusters the team, generates team labels, and shows where expert coverage is missing.** — This is what the speaker says the context engine uses to decide expertise, so it is also an ownership map. ([15:34](https://youtu.be/qdAkxLoYNI8?t=934))

## Techniques
- **Cited-source answers for agents** — Return the list of sources (PRs, Slack threads, Notion pages, architecture docs) with each answer so the agent can open them for follow-up and a human can audit or correct them. *When:* Any agent answer that feeds a plan or a merge decision, where you need to check the answer rather than trust it.
- **With/without context comparison** — Run the same task twice, once with the context layer and once without, and compare tokens, wall time, cost and plan quality. The speaker used Claude Code to plan an optimization of an internal calculator and compared the usage numbers. *When:* Deciding whether a retrieval or context layer pays off on your own tasks. Use the comparison on longer tasks, since the speaker argues the benefit compounds.
- **Expertise-weighted review comments** — Derive a reviewer's expertise from their past review history on the same code and boost their comments, or surface prior comments from people who know the area. *When:* An AI review bot is flooding PRs with low-value comments, and you want the important ones ranked higher.
- **Query historical PR data with an open-source engine** — The Document Query Engine runs over a GitHub repository, ingests historical pull requests, samples the documents to synthesize a schema, and answers queries through an agent chat. The talk gives no install commands; the project is named but its URL is not spoken. *When:* You want analytics or questions over PR history without writing the schema by hand.
- **Engineering social graph from review edges** — Build a graph where an edge means one person reviews another's code, cluster it into teams, and check coverage across the codebase to find areas with no expert reviewer. *When:* Mapping ownership and expertise gaps, or routing reviews to people who know the code.

## Numbers
- Maturity curve from autocomplete to software factories has 8 stages; most people are at stage 4 to 5 (slide credited to another speaker). ([3:09](https://youtu.be/qdAkxLoYNI8?t=189))
- Single-task cost comparison: plan to optimize an internal calculator took about 1 minute and sub-dollar cost with the context engine, versus about 2 minutes and higher cost without. One live run, wall-clock time excluded by the speaker. ([10:32](https://youtu.be/qdAkxLoYNI8?t=632))
- Context windows of roughly 1 million tokens are cited as still insufficient for whole-codebase context. No measurement is given. ([5:53](https://youtu.be/qdAkxLoYNI8?t=353))
- Customer quote: 50% fewer tokens, faster triage, better answers. Vendor-supplied and unverified. ([17:01](https://youtu.be/qdAkxLoYNI8?t=1021))

## Hot takes
- This is a vendor pitch for Unblocked. The evidence is one live demo task, one unverified customer quote, and no benchmark, so quality is capped at 2.
- Access to information does not equal understanding, and dumping the whole codebase into context is counterproductive. These are the talk's core claims, stated without measurements.
- The 'compounding' argument, that context wins on long tasks because wrong discovery loops, is plausible but the talk shows only one short task.

## Tools mentioned
Unblocked, Claude Code, Claude 4.8, Slack, Notion, GitHub, MCP, Document Query Engine, context engine simulator

## Relevance to our work
- **agentos** (2/3): MemoryMesh already plans hybrid retrieval, provenance and conflict resolution. This talk's cited-source answers and with/without comparison match that design direction. → *Make MemoryMesh retrieval return source IDs with each answer and log whether agents follow them. On one fixed task, compare tokens and time with and without retrieval, as the 10:32 demo does.*
- **prosharness** (1/3): ProsHarness wraps Claude Code runs. A pre-run context pass could cut the discovery loops that the talk says compound on long runs. → *Trial an optional context-gathering step before the plan stage, and log tokens and time for the same repo task with and without it.*

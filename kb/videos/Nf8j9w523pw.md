# Context Window Lie | Why AI Doesn't Actually Remember (ChatGPT, Claude & Gemini)

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `Nf8j9w523pw` · [watch](https://youtu.be/Nf8j9w523pw) · **date:** 2026-08-02 · **length:** 8:40 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Kai Explains host (name not given in transcript) · **orgs:** Anthropic, OpenAI, Google
- **topics:** context-engineering, memory, token-cost-efficiency · **tags:** context-window, attention, lost-in-the-middle, memory, token-budget, summarization, prompt-caching, explainer

> Explainer arguing a context window is a finite reading limit, not memory: models re-read the whole transcript each call, attention favors the start and end, so reliable agents budget context deliberately.

## Summary
The speaker argues that a context window is not memory but a per-call reading limit: each request resends the whole conversation, the model reads it once and retains nothing between calls. He uses a desk-versus-filing-cabinet analogy and says the window has no importance ranking, so anything that does not fit is simply absent. Long sessions degrade because system prompts, tool definitions, file reads and command outputs all compete for the same fixed space, which looks like the model getting dumber. He cites the "lost in the middle" effect, where content near the start and end of the window gets stronger attention, so critical instructions should go at the top and be repeated at the end. Memory features in products like Claude and ChatGPT are described as saved notes injected back into the window at the start of a new conversation. He concludes that teams building reliable agents manage context as a budget (summarizing old turns, injecting only needed files, rotating tool definitions) and that bigger windows do not change the underlying mechanics.

## Key ideas
- **A context window is not memory; it is a per-call reading limit** — Each message resends the full conversation as one document. The model reads it fresh, generates a reply, and keeps nothing between calls. There is no persistent notepad or state inside the model. ([0:00](https://youtu.be/Nf8j9w523pw?t=0))
- **The window has no importance ranking** — Unlike human memory, the window is brute force: everything in it gets equal processing and anything that does not fit simply does not exist. The model cannot choose to keep a critical instruction over small talk. ([1:22](https://youtu.be/Nf8j9w523pw?t=82))
- **Degraded long-session behavior is context starvation, not model stupidity** — In a long coding session, system prompts, tool definitions, file reads, error logs and outputs fill the window. Earlier constraints get pushed out or truncated, so the model cannot see them anymore. ([2:35](https://youtu.be/Nf8j9w523pw?t=155))
- **Attention is not uniform across the window (lost in the middle)** — Content at the beginning and end gets the strongest signal, and the middle gets weaker. The speaker says this is measured and published, without naming the study. Hence system prompts go at the top and key instructions are repeated at the end. ([3:54](https://youtu.be/Nf8j9w523pw?t=234))
- **Product memory features are sticky notes injected into context** — Claude's and ChatGPT's memory are described as separate systems that save small notes to a database and inject them at the start of new conversations. The model itself still has no knowledge of the notes between calls. ([3:54](https://youtu.be/Nf8j9w523pw?t=234))
- **Reliable agents manage context as a budget** — Teams summarize old turns, inject only the files needed right now, and rotate tool definitions in and out per task. Every tool call, file read and error competes for the same fixed space. ([5:17](https://youtu.be/Nf8j9w523pw?t=317))
- **Bigger windows do not change the mechanics** — Going from 128k to 1M tokens is framed as a bigger desk, not better recall. Long windows make the middle larger, so the lost-in-the-middle problem gets worse. Retrieval, summarization and prompt caching are the engineering that makes large windows usable. ([6:28](https://youtu.be/Nf8j9w523pw?t=388))

## Techniques
- **Itemized context budget audit** — Account for every block that will occupy the window: system prompt, tool definitions, retained conversation turns, file contents, tool outputs, and room for the model's own output. The speaker's example: 4k system prompt + 8k tool definitions + 30k last 10 messages + 12k file read = 54k tokens before the model starts thinking. Track this per turn, not just the advertised window size. *When:* Long agent or coding sessions with many tools, file reads and tool outputs, where quality degrades before the window is nominally full.
- **Rolling summarization of old turns** — Replace older conversation turns with a compact summary and keep only recent turns verbatim, so stable constraints survive while the window stays small. *When:* Multi-hour sessions where early constraints still matter but raw history is no longer needed.
- **Just-in-time file and tool injection** — Load only the files the model needs for the current step, and swap tool definitions in and out based on the current task instead of exposing all tools at once. *When:* Agents with large tool catalogs or big repositories where most context is irrelevant to the current subtask.
- **Position-aware instruction placement** — Put the system prompt and critical constraints at the top of the context, and repeat the most important instructions near the end, since the middle receives weaker attention. *When:* Prompts or agent contexts long enough that a constraint could sit in the middle, such as after many file reads or tool outputs.
- **External notes injected at conversation start** — Persist short notes outside the model (for example in a database) and inject the relevant ones into the window at the start of each new conversation. The model does not remember them between calls. *When:* Cross-session memory for agents where the goal is continuity across conversations rather than in-session recall.
- **Pair large windows with retrieval, summarization and prompt caching** — Do not rely on a huge window alone. Retrieve only relevant passages, summarize where possible, and use prompt caching to avoid re-processing unchanged prefix content. *When:* Deciding whether to rely on a million-token window versus building a retrieval or summarization layer.

## Numbers
- Advertised window sizes cited: 128,000, 200,000 and 1,000,000 tokens ([0:00](https://youtu.be/Nf8j9w523pw?t=0))
- A 200,000-token window is described as roughly 150,000 words; a serious coding session with tool calls and file contents is said to burn through it in under an hour (no measurement given) ([2:35](https://youtu.be/Nf8j9w523pw?t=155))
- Example context budget: 4k system prompt + 8k tool definitions + 30k for the last 10 messages + 12k for a file read = 54k tokens before the model starts generating (illustrative, not measured) ([5:17](https://youtu.be/Nf8j9w523pw?t=317))
- A critical instruction at position 60,000 of 200,000 tokens is described as measurably less likely to be followed than at position 1 or near 199,000 (no effect size given) ([3:54](https://youtu.be/Nf8j9w523pw?t=234))

## Hot takes
- Frames the 'context window' as a reading limit and says 'stop calling it memory'; a reframing more than new research.
- Cites the lost-in-the-middle effect as 'measured and published' without naming the paper, so the positional claim cannot be checked from the transcript alone.
- States flatly that the model retains nothing between calls and that bigger windows only mean a bigger warehouse, without discussing caching internals beyond a passing mention.
- Title ('Context Window Lie') oversells a mostly conceptual explainer; the concrete engineering advice is brief.

## Tools mentioned
ChatGPT, Claude, Gemini

## Relevance to our work
- **agentos** (2/3): MemoryMesh's tiered cross-session memory is the same sticky-note injection pattern the speaker describes; budgeting injected memory against the window and checking attention position fit the L2A design. → *In MemoryMesh's retrieval path, cap injected memory by a token budget and put the highest-priority memory and constraints at the start and end of the assembled prompt, not the middle; log per-call token composition to verify.*
- **prosharness** (2/3): ProsHarness runs long Claude Code sessions with checkpoint/resume; resuming from a full transcript reproduces the budget-starvation failure described here. → *On checkpoint resume, rebuild context from a summary of prior turns plus only the files and tool definitions the next step needs, and keep the plan and constraints at the top of the prompt, repeated near the end.*

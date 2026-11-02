# Give Claude Persistent Memory in 5 Minutes

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `ryqpGVWRQxA` · [watch](https://youtu.be/ryqpGVWRQxA) · **date:** 2026-03-02 · **length:** 4:15 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** ?
- **topics:** memory, claude-code, context-engineering, token-cost-efficiency · **tags:** claude-mem, persistent-memory, cross-session, auto-capture, compression, local-first, open-source, session-recall

> Shows Claude-Mem, an open-source local tool that auto-captures Claude Code session events (bug fixes, decisions, diffs) and recalls compressed context in new sessions.

## Summary
Better Stack demos Claude-Mem, an open-source plugin that gives Claude Code memory across sessions. The speaker says setup is two commands run inside Claude, with no config files or API keys, and that all captured data stays on the local machine. In a toy Python Fibonacci project, Claude-Mem logs a bug fix (the reasoning and code diff) in a local web UI while the work happens. After ending the session and starting a new one, asking about the bug returns the fix without re-explanation, and a search returns a compressed summary that can be expanded to full context. The video claims up to 10x memory compression and tag-based search (bug fix, decision, file path, keywords). The walkthrough is short and the install commands are not shown on screen, and the compression claim is not measured.

## Key ideas
- **Claude Code loses working context when a session ends, so each new session starts cold.** — The speaker frames the problem as memory that exists only inside one session and positions Claude-Mem as the fix. ([0:00](https://youtu.be/ryqpGVWRQxA?t=0))
- **Setup is presented as two commands inside Claude, with no config files or API keys.** — The video says both commands came from the Claude-Mem repo, but the commands themselves are not spelled out in the transcript. ([0:08](https://youtu.be/ryqpGVWRQxA?t=8))
- **Capture runs in the background and stores each change with its reasoning and code diff.** — After a fix to the Fibonacci script (raising ValueError for negative n), the entry shows up in a local web UI, categorized, with the fix, reasoning and diff. ([1:46](https://youtu.be/ryqpGVWRQxA?t=106))
- **Recall works across sessions: a new session can pull a past bug fix back without re-explaining it.** — The test ends the session, starts a fresh one and asks about the Fibonacci bug. The fix comes back, and a search returns a compressed summary that expands to full context. ([1:46](https://youtu.be/ryqpGVWRQxA?t=106))
- **The memory is automatic, unlike Claude's basic memory file, which has to be written by hand.** — The speaker's argument is that capture happens without user effort, and that the store is searchable by tag, file path or keyword. ([3:05](https://youtu.be/ryqpGVWRQxA?t=185))
- **Compression is positioned as the token-saving feature.** — The speaker claims memories are compressed by up to 10x so context uses fewer tokens and reaches limits more slowly. No measurement is shown. ([3:05](https://youtu.be/ryqpGVWRQxA?t=185))

## Techniques
- **Automatic session-event capture into a local memory store** — A background tool logs bug fixes, decisions and file changes with their reasoning and code diff, tagged by category. Nothing is written by hand. The store stays on the local machine. *When:* Long, multi-session projects where re-explaining past fixes and decisions wastes time.
- **Compressed-summary-first recall with expand-on-demand** — Search returns a short compressed summary of the matching memory. The user expands it only when the full context is needed. *When:* When context-window or usage-limit budget matters and most recalls need only the gist.
- **Tag and keyword search over memories** — Query by category tags (bug fix, decision), file path, or free-text keywords in the memory UI, instead of scrolling a session log. *When:* Finding a past decision or fix in a larger codebase after many sessions.
- **Reproducing the demo test for a memory tool** — Make a change with a known bug in session one (e.g. skip negative-input handling, then fix it with a ValueError). End the session, open a new one, and ask the agent to recall the fix. Pass if it returns the fix without being re-told. Then check that a search by keyword returns the compressed entry, and that expanding it shows the full context. *When:* Evaluating any cross-session memory tool before trusting it on real work.

## Numbers
- Claims memories are compressed by up to 10x (vendor claim, not benchmarked in the video) ([3:05](https://youtu.be/ryqpGVWRQxA?t=185))
- Setup described as two commands inside Claude (commands not shown on screen) ([0:08](https://youtu.be/ryqpGVWRQxA?t=8))
- Test project is a single recursive Fibonacci script with one bug (negative input), so the demo covers one fix ([0:41](https://youtu.be/ryqpGVWRQxA?t=41))

## Hot takes
- The 10x compression claim is stated without a benchmark, token count or before/after comparison.
- The demo covers one bug in a toy script, so it does not show how recall behaves in a large or noisy project history.
- The install commands are not shown or named in the video, so a viewer has to go to the repo to reproduce setup.
- Says data 'stays on your machine' but does not address what gets captured (for example secrets or credentials seen in diffs).

## Tools mentioned
Claude Code, Claude-Mem (open-source Claude Code memory plugin; version not stated)

## Relevance to our work
- **agentos** (2/3): AgentOS L2A MemoryMesh already has tiered cross-session memory with provenance. Claude-Mem's auto-capture and compressed-summary recall is a comparable pattern for coding-agent sessions. → *Compare Claude-Mem's auto-capture of bug fixes and decisions, and its summary-then-expand recall, against MemoryMesh's tiered cross-session memory. Note what is captured, how it is compressed, and how it is retrieved.*
- **prosharness** (1/3): ProsHarness does checkpoint/resume of long Claude Code runs. Session memory is related but does not replace checkpointing. → *Check whether auto-captured decisions and fixes could be fed into a ProsHarness resume step, or whether they belong in the checkpoint itself.*

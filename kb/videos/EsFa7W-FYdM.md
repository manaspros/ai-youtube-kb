# I Gave Claude Code Permanent Memory - The Results Are Shocking

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `EsFa7W-FYdM` · [watch](https://youtu.be/EsFa7W-FYdM) · **date:** 2026-01-02 · **length:** 4:05 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, Sourcegraph
- **topics:** context-engineering, coding-agents, mcp-and-tools · **tags:** beads, issue-tracker, sqlite, jsonl, git-sync, dependency-graph, context-reset, spec-driven-development, speckit, kiro, jira, compaction, claude-code

> Beads gives coding agents a git-synced issue tracker (SQLite locally, JSON Lines in git) so task state survives context resets. A 4-minute overview with claimed context savings and no measured results.

## Summary
The speaker introduces Beads, an issue tracker for coding agents that is stored inside the project repo, and presents it as a fix for agents losing their place after a context reset. Setup creates a .beads folder holding a local SQLite database, JSON Lines exports, a sync daemon, and a socket for CLI access. Only the JSON Lines files are committed to git; on pull, the local SQLite database is rebuilt from them, so collaborators on different machines converge on the same issues. Issues can be created from the CLI, through a Beads MCP server, or by asking the coding agent directly, and the agent updates them as it works until none remain open. The main argument is context efficiency: agents query the database for what they need instead of loading full PRD or markdown files, and explicit dependency edges let the model follow the graph. The speaker notes that Beads lacks the planning emphasis of spec-driven tools like SpecKit and suggests combining them for larger projects. The video shows no measured token or quality numbers, and the demo steps are not captured in the transcript.

## Key ideas
- **Markdown plans lose agent state across context resets and bloat context on large projects; Beads moves task state into an issue tracker kept in the repo.** — The problem framing: a new conversation leaves the agent unsure of next steps, and a markdown file grows costly as the project grows. Beads is pitched as a version-controlled tracker that can also sync to Jira. ([0:00](https://youtu.be/EsFa7W-FYdM?t=0))
- **Beads keeps a local SQLite database, but only JSON Lines files are committed to git.** — The .beads folder holds the SQLite DB and other DB files, a JSON Lines export of issues, a daemon that auto-exports DB changes to JSON Lines, and a socket for CLI reads and writes. ([0:00](https://youtu.be/EsFa7W-FYdM?t=0))
- **Two-way sync via git: pulls rebuild the local DB, so collaborators see the same issues.** — When someone pushes JSON Lines changes, others pull them, merge conflicts are resolved in the text files, and the local SQLite DB is updated. The speaker calls this two-way sync and says it lets agents on different machines share one project. ([1:14](https://youtu.be/EsFa7W-FYdM?t=74))
- **Issues can be created three ways, and the agent can then work the backlog on its own.** — Options are the CLI, the Beads MCP server, or a direct request to the coding agent, which creates issues under an epic with priority levels. The agent updates progress as it works until no open issues remain. ([1:14](https://youtu.be/EsFa7W-FYdM?t=74))
- **The main claimed advantage is context: agents query the DB instead of loading whole planning files, and explicit dependency edges let the model follow the graph.** — Dependencies are stored as relations rather than as items in a list, so the LLM can traverse them. Information is never lost on context clears, which the speaker says makes humans less afraid to clear context. No token counts are given. ([2:21](https://youtu.be/EsFa7W-FYdM?t=141))
- **Compaction shrinks the database by compressing old closed issues while keeping their essential context.** — Intended for large projects where the database grows over time. ([2:21](https://youtu.be/EsFa7W-FYdM?t=141))
- **The speaker sees a gap in planning: Beads does not emphasize specs the way spec-driven tools do.** — Suggested combination: write a detailed markdown spec with SpecKit, then use Beads to create the epics and issues. The speaker adds that this may be overkill for small or medium projects. ([3:34](https://youtu.be/EsFa7W-FYdM?t=214))

## Techniques
- **Repo-local issue tracker as agent working memory** — Initialize Beads in the project so a .beads folder is created. Commit only the JSON Lines export to git and leave the SQLite binaries out. Have the agent create issues under an epic with priority levels, then have it update each issue as it completes work. Pulls rebuild the local DB from the committed JSON Lines files. The transcript does not show the exact init or CLI commands. *When:* Long multi-session projects where context resets erase the agent's next steps, or where several agents or machines work on one repo.
- **Dependency-graph querying instead of loading planning docs** — Store blocking relations between issues explicitly. Have the agent query the database for open or unblocked items rather than reading a full PRD or markdown plan into context. *When:* Projects with many interdependent tasks, where the list-in-markdown approach makes the agent pull in large files each session.
- **Compaction of closed issues** — Run Beads' compaction feature periodically so old closed issues are compressed while keeping their essential context. The transcript does not give the command. *When:* Once the issue database has grown large over a long project.
- **Spec first, then issues** — Write a detailed markdown spec with SpecKit or a similar tool for planning. Then use Beads to turn the spec into epics and issues the agent tracks. *When:* Medium or large projects that need up-front planning, where the speaker says Beads alone lacks that emphasis.

## Hot takes
- The 'Results Are Shocking' title overstates a 4-minute overview; the video shows no measured results, token counts or before-and-after comparison.
- The context-savings argument for Beads over spec-driven markdown is asserted, not demonstrated.
- The hands-on demo (a brew-package app) is not described in the transcript, so the steps cannot be reproduced from the transcript alone.
- The speaker says Beads is weak on planning and suggests pairing it with SpecKit, which is a fair caveat.

## Tools mentioned
Beads, Beads MCP server, SQLite, JSON Lines, Git, Jira, SpecKit, Kiro, Claude Code, Sourcegraph, AMP

## Relevance to our work
- **prosharness** (2/3): ProsHarness checkpoints and resumes long Claude Code runs. A dependency-aware, git-synced store of plan items could replace or complement markdown plan files for resume. → *Prototype storing ProsHarness plan and checkpoint state as an issue graph in JSON Lines (committed) with a local SQLite index, so a resumed run queries only open, unblocked items.*
- **agentos** (1/3): Beads is a coding-task tracker, not agent memory, but its git-synced SQLite plus JSON Lines pattern is a small prior-art reference for durable cross-session state. → *Read the Beads repo README for its JSONL-in-git plus local SQLite sync design and compare it with MemoryMesh's tiered cross-session memory and provenance model.*

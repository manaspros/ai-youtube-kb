# Supabase MCP Cursor Integration (Step by Step)

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `b_hr1TB2GYQ` · [watch](https://youtu.be/b_hr1TB2GYQ) · **date:** 2025-11-02 · **length:** 6:03 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Supabase, Cursor, Windsurf, GitHub, Anthropic
- **topics:** mcp-and-tools, coding-agents, context-engineering · **tags:** supabase, cursor, mcp, postgres, connection-string, session-pooler, bash-wrapper, github-mcp, windsurf, claude-desktop

> Step-by-step setup of Supabase's MCP server in Cursor so the agent can see the live database schema, with a connection-string walkthrough and a bash-wrapper trick. Anecdotal, short, and light on verification data.

## Summary
The creator says Cursor loses track of Supabase database structure (tables, data, relations), which causes repeated errors and forces the user to re-explain the schema. The fix is to connect Supabase's MCP server to Cursor, which lets the agent query the database and verify tables before acting. He shows a demo Apple Notes clone built in Cursor, with composer screenshots of the agent verifying tables after each command, and one case where it wrongly concluded tables were empty and inserted placeholder data. He reports that Windsurf succeeded where Cursor failed on front-end issues, and that he now uses Windsurf with the MCP servers. The setup walkthrough covers finding the database password, copying the session pooler connection string from the Connect tab, and adding the MCP command in Cursor's settings. He recommends wrapping the command in a .sh script run through bash, and says he did the same for GitHub MCP.

## Key ideas
- **Cursor loses track of Supabase schema and data across sessions, causing repeated errors and forcing the user to re-explain the database. The creator frames the MCP server as the fix.** — The problem is framed as the agent not retaining what tables exist and how they connect. The fix is giving the agent live access to the database through MCP, so it can check the schema itself. ([0:00](https://youtu.be/b_hr1TB2GYQ?t=0))
- **Supabase MCP gives the agent a query tool. Cursor generates SQL that gets pasted into the Supabase SQL editor, and the agent verifies tables after each step.** — In the composer, the agent uses the query tool and verifies table state after the first command. The creator says the verification step lets it recover from errors. He also reports it repeatedly re-verifying and once concluding tables were empty and inserting placeholder data. ([1:27](https://youtu.be/b_hr1TB2GYQ?t=87))
- **Windsurf succeeded where Cursor failed on front-end issues, and the creator switched to Windsurf with the same MCP servers.** — This is a single anecdote from one project, not a controlled comparison. The creator says the difference 'blew me away' but gives no metrics. ([1:27](https://youtu.be/b_hr1TB2GYQ?t=87))
- **Connecting to hosted Supabase needs the session pooler connection string with the database password inserted. Local instances use a connection string from `supabase status`.** — The creator says the Supabase MCP docs cover both local and hosted setups. The hosted flow is: project settings, database settings (password here, reset if lost), Connect tab, session pooler section. ([2:46](https://youtu.be/b_hr1TB2GYQ?t=166))
- **The connection string must be pasted in without angle brackets or square brackets around the parameters. These are easy to leave in by mistake.** — The creator says to remove the angle brackets around the connection string placeholder and the square brackets around the password before running the command. ([4:07](https://youtu.be/b_hr1TB2GYQ?t=247))
- **He wraps the MCP command in a shell script and runs it through bash, rather than pasting the raw command into Cursor's settings. He says he prefers this and applied it to GitHub MCP too.** — Stated preference, not a reasoned trade-off. Storing the password in a script file is a credential-handling concern he does not mention. ([5:32](https://youtu.be/b_hr1TB2GYQ?t=332))

## Techniques
- **Add Supabase MCP to Cursor via the command type** — 1) In Supabase: Project Settings, then Database settings. Copy the database password (reset it there if forgotten). 2) Open the Connect tab, scroll to the session pooler section and copy the connection string. 3) Insert the password in place of the placeholder, removing any angle brackets and square brackets. 4) Use the full command from Supabase's MCP docs (the transcript does not show its exact text). 5) In Cursor's MCP settings, add a server with a name, type 'command', and the full command pasted below it. Save it. *When:* Connecting a hosted Supabase project to Cursor so the agent can query and verify the schema before writing SQL.
- **Wrap the MCP command in a bash script** — Run `touch <name>.sh`, open it in an editor, paste the command, and save. Get the absolute path with `realpath <name>.sh`. In Cursor's MCP config, set the command to `bash` followed by that path. The creator's example is a script named run2.sh. *When:* Keeping a long MCP command with a connection string out of the Cursor config UI. Note that the password then sits in plaintext in a file on disk.
- **Make the agent verify schema before and after each DB step** — The creator does not give a prompt. The behavior he describes is the agent calling the MCP query tool to check the table list after the first command, then re-verifying between steps. He credits this with recovery from errors. To reproduce, ask the agent to check current tables through MCP before writing any SQL, then after each change. *When:* Multi-step schema work on a larger Supabase project, where the agent otherwise loses track of what already exists.

## Numbers
- Video length is 6:03. No benchmarks, token counts, latencies or adoption stats are given. ([0:00](https://youtu.be/b_hr1TB2GYQ?t=0))

## Hot takes
- Cursor 'forgets' database structure is presented as fact from one user's experience. No reproduction or comparison is shown.
- The Windsurf-beats-Cursor claim rests on a single project and no metrics.
- Storing the database password in a plaintext .sh script and in the MCP config is presented as a convenience. The creator does not discuss secret handling.
- Sponsorship or affiliation is not stated. Title and content are a plain tutorial, not a hype piece.

## Tools mentioned
Supabase, Supabase MCP server, Supabase CLI (`supabase status`, local instances), Cursor, Windsurf, Claude Desktop, GitHub MCP server, bash

## Relevance to our work
- **agentos** (1/3): AgentOS's L2A MemoryMesh targets cross-session memory. This video is a concrete example of an agent losing schema state between sessions, and the fix is live tool access, not memory. → *Consider whether MemoryMesh or the agent toolset should expose a live schema-introspection tool (like Supabase MCP) so agents verify DB state instead of relying on remembered context.*
- **prosharness** (1/3): ProsHarness wraps Claude Code and handles credentials with zero tokens. This video shows the common pattern of putting DB passwords into MCP configs and shell scripts, which is the case zero-token credential handling should cover. → *Check how ProsHarness passes MCP connection strings and passwords to Claude Code. Avoid plaintext passwords in wrapper scripts and MCP config files, and use environment or secret-store injection instead.*

# Building an ACP-Compatible Agent Live — Bennet Fenner, Zed

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `HsxQICTLF84` · [watch](https://youtu.be/HsxQICTLF84) · **date:** 2026-07-18 · **length:** 18:19 · **format:** demo · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Bennett Fenner · **orgs:** Zed, Anthropic, JetBrains, Obsidian, OpenCode, Cursor, OpenClaw
- **topics:** coding-agents, mcp-and-tools, agent-architecture · **tags:** acp, agent-client-protocol, zed, json-rpc, stdio, live-coding, tool-calls, streaming, typescript, coding-agent

> Live demo of turning a minimal TypeScript coding agent into an ACP-compatible agent for Zed: four required methods, streamed text, tool-call updates, client-proxied file access, and a diff content type.

## Summary
Bennett Fenner from Zed presents the Agent Client Protocol (ACP), a JSON-RPC protocol meant to let any editor or client talk to any coding agent, compared to MCP and LSP. He starts from a bare TypeScript coding agent with two tools (read file, edit file by replacing old text with new text) that loops over the Anthropic API. He then implements the minimum ACP surface: initialize, session creation (returns a session ID and stores the working directory), prompt, and cancel. Model text is streamed to the client as session-update notifications, and tool calls are reported as an in-progress update followed by a completed update with content. He shows that when the client advertises a file-system capability, reads and writes can be proxied through the client so the agent sees unsaved editor buffers, and that edits can be sent as a diff content type. Near the end the agent is used to add a terminal tool to itself, and the talk closes with the note that transport is currently stdio with remote transport planned. The live demo ran into connection problems, and the speaker says the demo code is agent-generated and not for production.

## Key ideas
- **ACP is a JSON-RPC protocol that lets any client (editor) talk to any agent through one interface, positioned like MCP or LSP.** — Agents join either through an adapter that translates their native protocol, or by building ACP mode in: OpenCode and Cursor are named as having it in their CLIs. The speaker says up to about 40 clients implement it, including JetBrains and Obsidian. ([0:00](https://youtu.be/HsxQICTLF84?t=0))
- **Every coding agent is the same loop: stateless model API, run tool calls locally, send results back until the model ends its turn.** — The minimal agent has two tools (read file, edit by replacing an old string with a new one). The conversation is re-sent on every API call, so the loop is the core of the agent and ACP only wraps it. ([2:33](https://youtu.be/HsxQICTLF84?t=153))
- **Only four methods are needed for a minimal ACP agent: initialize, session new, prompt, and cancel.** — Initialize returns the protocol version and capabilities. Session new generates an ID, stores an agent instance with the client's working directory, and returns the ID. Prompt takes content blocks plus the session ID, runs the loop, and returns a stop reason. Cancel is described as simple and optional. ([4:57](https://youtu.be/HsxQICTLF84?t=297))
- **Output is streamed as session-update notifications, not request/response replies.** — Each text chunk from the model's stream is sent as an agent_message_chunk update tied to the session ID. Updates can arrive at any time, and the client reacts to them. ([8:46](https://youtu.be/HsxQICTLF84?t=526))
- **A tool call is reported as two updates: an in-progress tool_call first, then a tool_call_update with final status and content.** — The first update carries title, kind (used by Zed for icons), status, and optional file locations. The second sets the completed status and returns the output. Without the second update the UI never leaves the in-progress state. ([10:17](https://youtu.be/HsxQICTLF84?t=617))
- **Reads and writes can be proxied through the client's file-system capability so the agent sees what the editor sees.** — Unsaved buffer changes exist only in the editor, so a direct disk read would miss them. If the client advertises the file-system capability, the agent calls the client's read/write over ACP instead of native file APIs. ([12:41](https://youtu.be/HsxQICTLF84?t=761))
- **Edits can be sent as a diff content type with old and new text, and the client does the diffing.** — The agent sends old text and new text, and the client renders the diff. The speaker notes this is one of several ACP content types. ([13:51](https://youtu.be/HsxQICTLF84?t=831))
- **A terminal capability lets the client run and manage terminals for the agent, and the agent can extend itself with it.** — The client advertises terminal support. In the demo the agent was prompted to add a terminal tool to its own code, rebuilt, and then ran a sleep command in a visible terminal. The speaker calls this vibe coding and says the code is not production-ready. ([15:07](https://youtu.be/HsxQICTLF84?t=907))
- **Current transport is stdio, and the speaker says remote transport is coming.** — Zed runs the agent as a Node process pointed at its built JS file. The speaker says people from JetBrains are working on a remote transport that he expects soon. ([17:14](https://youtu.be/HsxQICTLF84?t=1034))

## Techniques
- **Minimal agent loop as the ACP core** — Keep the agent as a plain loop: send conversation to the model API, and on a tool call run it locally, append the result, and call again until end_turn. Wrap that loop with ACP handlers, rather than designing around the protocol. *When:* Building a new coding agent or adding a client protocol to an existing agent. The loop stays the same and only the transport and notifications change.
- **Session-scoped agent instances** — On session new, create an ID and an agent instance bound to the client's working directory, store it in a map keyed by session ID, and look it up on each prompt. *When:* A single agent process serves several threads or editor windows, each with its own cwd and state.
- **Streaming through session-update notifications** — Forward each model stream chunk as an agent_message_chunk session update instead of waiting for the full reply. *When:* The client UI should show tokens as they arrive and the agent is driven over a request/response protocol with server-to-client notifications.
- **Two-phase tool-call reporting** — Emit a tool_call update with in-progress status and metadata (title, kind, locations) before running the tool, then a tool_call_update with completed status and content after it finishes. *When:* The client should show running tool calls with progress and file locations, and then the result.
- **Client-proxied file system** — Check whether the client advertises a file-system capability at initialize time. If it does, route reads and writes through the client's ACP methods, otherwise use native fs calls. *When:* The agent must see unsaved editor state, for example when the editor holds buffers that differ from disk.
- **Diff content type for edits** — Send edits as a diff content with old text and new text and let the client render and compute the diff. *When:* Presenting file edits in an editor where the client can show reviewable diffs.
- **Using the protocol's debug view to inspect traffic** — Open the client's ACP debug view to see each request and notification (for example session new, then prompt, and stop reason) while building. *When:* Debugging the message sequence between an ACP agent and client during development.

## Numbers
- Up to about 40 clients implement ACP (speaker's figure) ([1:09](https://youtu.be/HsxQICTLF84?t=69))
- Minimal coding agent has two tools: read file and edit file ([2:33](https://youtu.be/HsxQICTLF84?t=153))
- Minimum ACP surface is about four functions: initialize, session new, prompt, cancel ([4:57](https://youtu.be/HsxQICTLF84?t=297))
- Full build to a working ACP agent with file access and a terminal tool took about 15 minutes of live coding (speaker's estimate) ([16:07](https://youtu.be/HsxQICTLF84?t=967))

## Hot takes
- The speaker presents the demo code as agent-generated and says it should not be used in production.
- ACP is positioned as the editor-side counterpart to MCP and LSP, so any agent can plug into any editor through one interface.

## Tools mentioned
Zed, Agent Client Protocol (ACP), ACP TypeScript SDK, Anthropic SDK, Node.js, stdio

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI. ACP is an alternative standard session and tool-call model for driving coding agents, but the talk does not cover permissions, checkpoints or approvals. → *Read the ACP session and tool-call spec to compare its update model with ProsHarness's checkpoint and resume events, and decide whether it is worth exposing ProsHarness through ACP.*
- **general** (1/3): Useful background on which coding-agent clients now speak ACP, and on the protocol's surface for coding-agent interop. → *Skim agentclientprotocol.com for the tool-call, diff and terminal content types, and the list of supported clients.*

# Burn Your Flags: Interactive CLIs for Agents — Mark Lummus & Navinkumar Patil, PayPal

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `aV_vgUSatqs` · [watch](https://youtu.be/aV_vgUSatqs) · **date:** 2026-10-12 · **length:** 53:43 · **format:** workshop · **quality:** 3/5 · **depth:** intro
- **speakers:** Mark Lummus, Navinkumar Patil · **orgs:** PayPal
- **topics:** coding-agents, mcp-and-tools, context-engineering · **tags:** interactive-cli, agent-tool-design, tmux, cli-design, side-channel, context-injection, determinism, workshop, leaderboard

> PayPal's developer tools leads run a live workshop where attendees make a coffee-ordering CLI work for agents. Main point: interactive prompts fail silently under agents, so CLIs need machine-readable side channels, injected context, and determinism.

## Summary
Mark Lummus (head of developer tools) and Navinkumar Patil (tech lead) ran a hands-on workshop built around "Barista 9000," a CLI for ordering coffee that fails when an agent runs it because it is interactive. The core claim is that agents call CLIs through Bash, and an interactive prompt makes the agent see only a redraw loop while the harness loses UI state, so the failure is silent. Flags work only when all options are known up front and independent; they break when the next question depends on earlier answers or on live API responses. The speakers argue that agent-facing CLI design should follow the same discipline as accessibility for humans, treating the agent as a new kind of reader. Their suggested fixes were tmux send-keys and capture-pane as a low-effort way to drive an existing CLI, a machine-readable side channel (JSON read/send, like a REST API next to a web UI), and context injection through one input file that lists the fields and the questions the agent should ask. They also argued that a CLI used by an LLM should be small and deterministic, with reasoning kept in the calling model. Participants competed on a leaderboard scored by accuracy and then response time, and the winning entry was a deterministic solver built by an agent (Opus 4.8 via the Claude Agent SDK) and driven through tmux. The talk is mostly hands-on game flow, so the reusable data is thin, but the failure-mode framing and the determinism argument are useful.

## Key ideas
- **Interactive CLIs fail silently when an agent runs them.** — The agent sees a redraw loop instead of a question, and the harness loses the UI state. There is no error, so the failure is invisible. ([3:49](https://youtu.be/aV_vgUSatqs?t=229))
- **Flags only cover flows whose options are known in advance.** — Flags work for single-pass, independent options. They break when the next question depends on an earlier answer or on a live API response, because you cannot enumerate every path as flags. ([4:58](https://youtu.be/aV_vgUSatqs?t=298))
- **Treat agents as a new kind of reader and apply accessibility thinking.** — The speaker's framing: map what is done for human accessibility to what agents need. Agents can reason, ask, retry, and walk a decision tree if one is provided, unlike scripts. ([4:58](https://youtu.be/aV_vgUSatqs?t=298))
- **Tmux send-keys and capture-pane is the low-effort first step.** — Run the CLI in a detached tmux session, send keys, and capture the pane. The speaker calls this screen scraping. Long-running and multiple sessions are easy to manage this way. ([26:25](https://youtu.be/aV_vgUSatqs?t=1585))
- **Add a machine-readable side channel next to the human UI.** — Expose read-state and send-input as structured data (JSON output) so agents do not scrape the screen. The speaker compares this to adding a REST API next to a website. ([28:37](https://youtu.be/aV_vgUSatqs?t=1717))
- **Give the agent context in one input file instead of interactive prompts.** — Context injection: supply the fields, defaults, and the questions the agent should ask the user in a single structured input. The speaker's example: low on oat milk, so the agent should confirm whether a smaller amount is acceptable and offer a backup. ([31:44](https://youtu.be/aV_vgUSatqs?t=1904))
- **Keep the CLI deterministic and leave reasoning to the calling LLM.** — The LLM is the non-deterministic part. A CLI meant for LLM use should be a small, sharp tool that returns the same output for the same command. Do not embed an agent inside the CLI. ([41:29](https://youtu.be/aV_vgUSatqs?t=2489))
- **Winning entry: an agent built a deterministic solver and drove it through tmux.** — The winner used an agent (Opus 4.8 via the Claude Agent SDK, driven through Slack) to write a deterministic CLI solver, then ran it through tmux. The speaker notes a prior eval-bench skill helped. A second entrant's approach was also a deterministic parser. ([46:46](https://youtu.be/aV_vgUSatqs?t=2806))

## Techniques
- **Side-channel JSON interface for CLIs** — Add a non-interactive agent mode (the workshop used a --agent flag on the brew command) that reads state and accepts input as structured data, next to the human TUI. *When:* Any CLI that agents will call and that today depends on prompts or a visual UI.
- **Tmux driver for interactive CLIs** — Start the CLI in a detached tmux session (tmux new -d), use send-keys to input, and capture-pane to read the screen. Run multiple sessions for multiple agents. *When:* As a quick stopgap when a CLI has no structured interface, or for long-running interactive tasks. The speaker calls it low effort and screen scraping.
- **Context injection via a single input file** — Give the agent one structured file that holds all the inputs, defaults, and the decision points where it should ask the user, so it does not need to walk an interactive flow. *When:* When the decision points and defaults are known before the run starts.
- **Deterministic CLI, reasoning outside** — Keep the CLI as a small tool with fixed, repeatable outputs for each command. Keep all model reasoning in the calling agent and do not embed an agent in the CLI. *When:* When an LLM will call the CLI repeatedly and needs predictable results.
- **Have an agent build the solver** — Describe the task to a coding agent, let it write a deterministic CLI solver, then run it under tmux. The speaker's winner also used a prior eval-bench skill to optimize. *When:* A repeated, latency-sensitive task where a fixed program beats per-call model reasoning.

## Numbers
- Leaderboard leader was close to 5,000 points. Ties were broken by response time, and several entries reportedly finished 3 of 3 in zero seconds, which the speakers called not possible. ([34:19](https://youtu.be/aV_vgUSatqs?t=2059))
- One entry hit a round trip of about 29 ms, which the winner attributed to running in the same region as the server. ([46:46](https://youtu.be/aV_vgUSatqs?t=2806))
- The workshop used a 25 to 30 minute hands-on window, with a hint shared every 15 to 20 minutes. ([12:36](https://youtu.be/aV_vgUSatqs?t=756))

## Hot takes
- Interactive prompts in CLIs that agents call fail silently. Flags alone are not enough once the flow depends on context.
- A CLI used by an LLM should be deterministic. The LLM is the non-deterministic part, so do not put an agent inside the CLI.
- The real test is whether a mid-tier model (Haiku or Sonnet class) can run the CLI cheaply, not whether the top thinking model can brute-force it.

## Tools mentioned
tmux, Claude Code, Codex, Claude Agent SDK, Opus 4.8, Slack

## Relevance to our work
- **prosharness** (2/3): ProsHarness drives the interactive Claude Code CLI. The talk's failure mode (silent stalls on interactive prompts) and its tmux send-keys and capture-pane approach apply directly to how the harness drives that CLI. → *Check whether the ProsHarness Claude Code driver detects interactive prompts (permission or approval screens) and fails loudly instead of stalling. Then prototype a JSON status side channel for the harness's own CLI commands.*
- **agentos** (1/3): AgentOS exposes tools that agents call. The talk's determinism and side-channel guidance applies to any CLI AgentOS exposes to agents, though the talk does not address proxy or infra design. → *Apply the rule of a deterministic CLI with JSON output to any AgentOS command an agent is expected to call, and write a test that runs it non-interactively.*

# 1,000 Agent Tasks in a Sandbox: What Breaks When LLMs Run Code — Kevin Orellana, AWS

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `k72eLcYpVys` · [watch](https://youtu.be/k72eLcYpVys) · **date:** 2026-10-12 · **length:** 15:19 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Kevin Orellana · **orgs:** AWS, Amazon Bedrock AgentCore, UC Berkeley
- **topics:** sandboxing-execution, testing-verification, mcp-and-tools · **tags:** sandbox, fuzz-testing, coding-agents, mcp, failure-modes, agentcore, sqlite, ssh, file-system, memory-limits

> Kevin Orellana (AWS) has a coding agent fuzz-test a sandbox hosting platform with about 1,000 workflows, and shows how sandbox primitives like memory, file persistence and permissions cause failures.

## Summary
Kevin Orellana from AWS (Amazon Bedrock AgentCore) describes an experiment where a coding agent was pointed at his team's sandbox hosting platform with the instruction to break it, and left to run overnight. The team first wrapped the platform in a thin MCP server, then had the agent write about 1,000 workflow tests across 10 domains, run by concurrent sub-agents and stored in SQLite. The tests covered sandbox lifecycle, file I/O, performance, software development cycles, a code sandbox and a cloud browser. Three representative failures were an image that came back altered (an encoding bug at the MCP layer), a null byte that broke tests, and files written to a sandbox directory that could not be read back. He sorts failures into interface-layer and sandbox-layer problems. The browser failed mostly from memory exhaustion, while the code sandbox was steadier, and failures clustered around file system permissions, mounts and persistence. He argues that low-level sandbox constraints can block an agent's goal even when the business logic is correct, so teams should fuzz-test their sandboxes with agents as well as test them by hand. The talk is short and mostly qualitative, with few hard numbers.

## Key ideas
- **Fuzz-test the sandbox platform with an agent** — Point a coding agent at the sandbox platform and tell it to break it. Run it for a long time (overnight) to find failure modes that hand-written tests miss. ([0:12](https://youtu.be/k72eLcYpVys?t=12))
- **Expose the platform to the agent through a thin MCP server first** — A day or two of work produced an MCP server that wraps the sandbox environment. Polishing came after, through tool selection and smoke tests. ([1:10](https://youtu.be/k72eLcYpVys?t=70))
- **Scale the test set with agents, store results in a database** — The agent writes about 1,000 tests across 10 domains. Sub-agents run them concurrently and results go to SQLite, because markdown files do not scale to that many results. ([2:10](https://youtu.be/k72eLcYpVys?t=130))
- **Split failures into interface-layer and sandbox-layer problems** — Some failures came from the MCP and encoding layer, such as a corrupted image round-trip and null bytes. Others came from the sandbox, such as files that could not be read back. Separating the two makes triage faster. ([6:02](https://youtu.be/k72eLcYpVys?t=362))
- **Sandbox primitives drive most failures** — Failures cluster around memory limits, file system permissions, mounts and ephemeral versus persistent storage. Browser sessions were starved of memory, while the code interpreter rarely failed. ([7:24](https://youtu.be/k72eLcYpVys?t=444))
- **Low-level constraints can block a correct agent** — Things like whether a process may spawn, where binaries live, and whether a package lands in the right module path decide whether the agent can finish its task. These small issues add up. ([9:45](https://youtu.be/k72eLcYpVys?t=585))
- **Local agent environments differ from remote sandboxes** — Tools that work on a laptop may not match what is in a remote sandbox. The speaker's team added SSH access so people, or agents, can inspect a failing sandbox. ([12:04](https://youtu.be/k72eLcYpVys?t=724))
- **Academic results depend on the environment** — The speaker cites a UC Berkeley study where a better environment and exploit-style agent reached very high SWE-benchmark scores, and another study where broken tools lowered agent effectiveness. ([13:29](https://youtu.be/k72eLcYpVys?t=809))

## Techniques
- **Agent-driven fuzz testing of a sandbox platform** — Give a coding agent a thin MCP wrapper around the platform, ask it to write many workflow tests across domains, and run them with concurrent sub-agents. Include credential injection and have the agent classify each failure as a service issue or an MCP-layer issue. *When:* Before you trust a sandbox or agent-hosting platform, or when hand-written tests cover too little of the real workflows customers run.
- **Results in SQLite, not markdown** — Have each test write its findings as rows in a local SQLite database. Concurrent sub-agents then write without clobbering each other, and the results can be queried later. *When:* The test run produces hundreds or thousands of results that you need to query or compare.
- **Two-layer failure triage** — Tag each failure as an interface problem (encoding, null bytes, MCP serialization) or a sandbox problem (file permissions, persistence, memory, process spawn). Fix each layer on its own. *When:* Failures look similar from the outside, and you need to know whether the platform, the protocol or the sandbox is at fault.
- **Build a workflow suite that mirrors customer workloads** — Write test domains that match real use: the code sandbox, the cloud browser, sandbox lifecycle under stress, file upload and download, and package development cycles. Each test should be a whole workflow, not a single call. *When:* You want tests that match what customers actually run in sandboxes.

## Numbers
- About 1,000 agent-written tests across 10 domains; the number was chosen to cast a wide net and was not a target ([2:10](https://youtu.be/k72eLcYpVys?t=130))
- A full run of 1,000 tests takes a few hours and is token-heavy ([2:10](https://youtu.be/k72eLcYpVys?t=130))
- Two hosted application types were tested: a code sandbox and a cloud browser. The browser failed mostly from memory exhaustion, and the code sandbox failed much less often (the failure counts are shown only on a slide, not stated) ([7:24](https://youtu.be/k72eLcYpVys?t=444))
- The speaker cites a UC Berkeley study that reached up to 100 percent on SWE-bench with the right environment controls and an exploit agent (the speaker's citation, not verified) ([13:29](https://youtu.be/k72eLcYpVys?t=809))

## Hot takes
- Fuzz-testing a sandbox with an agent finds failure modes that hand-written unit and integration tests miss.
- Agents are good at writing unit and integration tests, but low-level sandbox controls can quietly block the agent's stated goal.
- Hosting agents in sandboxes changes the failure model: the sandbox primitives matter more than the API surface.

## Tools mentioned
MCP, SQLite, Amazon Bedrock AgentCore, SSH, Codex, Claude Code

## Relevance to our work
- **agentos** (2/3): Crucible runs opt-in sandboxed code execution (celld, Cloudflare backend). The talk's method of fuzzing a sandbox with agent-written workflows and sorting failures by layer applies directly to testing it. → *Have a coding agent write about 100 Crucible workflow tests across the code, file I/O and lifecycle domains. Store results in SQLite and tag each failure as interface or sandbox layer.*
- **general** (2/3): A general method for testing agent-hosting infrastructure: run an agent to write many workflow tests and treat the failures as the product findings. → *Before relying on any sandbox or agent runtime, run a one-night agent-written test sweep and triage the failures by layer.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI around checkpoint/resume runs. Files written in a sandbox that cannot be read back is the same persistence failure the talk reports, and it could break resume. → *Write a short check that files written before a checkpoint are still readable after resume, in the same sandbox setup the harness uses.*

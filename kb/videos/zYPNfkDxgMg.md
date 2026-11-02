# This One Claude Code Feature Replaced My ENTIRE Team (Subagents)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `zYPNfkDxgMg` · [watch](https://youtu.be/zYPNfkDxgMg) · **date:** 2025-11-02 · **length:** 4:08 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Anthropic
- **topics:** claude-code, multi-agent, context-engineering · **tags:** custom-subagents, subagents, agents-command, read-only-tools, mcp-tools, code-review, token-usage, sequential-execution

> Walkthrough of Claude Code's Custom Subagents (v1.0.60+): creating a read-only reviewer agent via the agents command, then running about ten subagents from one prompt, with token and time costs.

## Summary
Anthropic added Custom Subagents to Claude Code, letting users define named subagents with a description, a restricted tool list, a color and a system prompt. The speaker creates a personal-scope agent through the agents command, using "generate with Claude" from a one-line description, and restricts it to read-only tools for code review. A security review of one file by that agent took about a minute and roughly 20k tokens. He then runs about ten custom subagents plus the general-purpose one in a single prompt over a components directory, which took about an hour and roughly 500k tokens, with Claude running them sequentially even though it could run them in parallel. He notes that each subagent starts with a clean context window, which can hurt when it must gather context itself. He is skeptical of using it often, since his tasks are not hyper-specialized, but calls it a sign Anthropic is pushing Claude Code further.

## Key ideas
- **Custom Subagents let you configure a named agent for a specific task with its own tool allowlist and color, unlike the older ad hoc subagent runs that gave little control.** — Requires Claude Code version 1.0.60 or later; the feature is exposed through an agents command that lists the default general-purpose agent plus any custom ones. ([0:00](https://youtu.be/zYPNfkDxgMg?t=0))
- **Agents can be generated from a short description: Claude writes the agent config, including name, tool list, description and system prompt, which the user can then edit.** — Scope can be set to personal so the agent is available across all projects. The speaker describes the agent as a senior engineer reviewing code for quality, security and best practices. ([0:00](https://youtu.be/zYPNfkDxgMg?t=0))
- **For a review agent, restrict tools to read-only ones.** — The speaker gives the review agent only read-only tools and shows the full tool list before saving. Agents can also be limited to specific MCP tools. ([0:00](https://youtu.be/zYPNfkDxgMg?t=0))
- **Agent definitions are shareable, so the speaker expects community collections of subagents to appear.** — He mentions sharing agents on GitHub but leaves his as they are. ([1:18](https://youtu.be/zYPNfkDxgMg?t=78))
- **Claude does not always pick a subagent automatically, so the user may need to name it in the prompt.** — He says Claude Code will select a subagent based on the task but he had not got it to do so yet; in his test he prompted for a security review of one file and Claude then used the custom agent. ([1:18](https://youtu.be/zYPNfkDxgMg?t=78))
- **Parallel subagent runs are possible, but Claude ran them one after another in his test.** — Claude built a to-do list assigning named subagents to each part of the job (code quality, then performance optimizer, and so on). He says it can run agents in parallel but did not choose to here. ([2:43](https://youtu.be/zYPNfkDxgMg?t=163))
- **Each subagent has its own context window and starts from a clean slate on each invocation.** — He flags this as a possible performance cost when a subagent must gather context itself before doing its job, and points to the documentation. ([2:43](https://youtu.be/zYPNfkDxgMg?t=163))
- **The speaker is skeptical of heavy use: his work is not hyper-specialized, so he does not expect to use subagents much.** — He treats the feature as a sign of Anthropic's direction for Claude Code rather than a must-have for his own workflow. ([4:02](https://youtu.be/zYPNfkDxgMg?t=242))

## Techniques
- **Create a personal-scope read-only reviewer subagent** — Run the agents command in Claude Code (v1.0.60+), choose to create a new agent at personal scope so every project can use it, pick Generate with Claude, and give a one-line role description (e.g. senior software engineer expert at fine-grained detail and logic when reviewing code for quality, security and best practices). Then select only read-only tools, choose a color, and review the generated name, description and system prompt before saving. *When:* Code review or audits where the agent should inspect files but not edit them, reusable across repos.
- **Restrict a subagent to specific MCP tools** — When choosing the tool list, select only the MCP tools the agent needs rather than the full set. *When:* An agent should only reach one external system, such as a single MCP server, keeping its blast radius small.
- **Delegate a task to a named subagent in the prompt** — Name the subagent or describe the task in the prompt (e.g. review the security of one specific file using sub-agents); Claude then runs the matching subagent and returns its result. *When:* You want a specialist to handle a bounded task, instead of relying on automatic selection, which the speaker found unreliable in his test.
- **Batch several subagents in one prompt** — Describe a multi-part job covering several specialties (code quality, performance, error handling, metrics, refactoring, tests, documentation) and ask Claude to use the subagents; Claude builds a to-do list and assigns a subagent to each item. *When:* Broad codebase passes where each part needs a different specialty. Expect high token use and long runtime, and note that the run was sequential in his test.

## Numbers
- Minimum Claude Code version for Custom Subagents is 1.0.60. ([0:00](https://youtu.be/zYPNfkDxgMg?t=0))
- Single security review by a read-only custom subagent took just over one minute and about 20k tokens. ([1:18](https://youtu.be/zYPNfkDxgMg?t=78))
- Run of about ten custom subagents plus one general-purpose agent over the components directory took about one hour and about 500,000 tokens. ([2:43](https://youtu.be/zYPNfkDxgMg?t=163))
- Video length is 4:08. ([0:00](https://youtu.be/zYPNfkDxgMg?t=0))

## Hot takes
- Custom subagents are a super cool feature, but the speaker does not expect to use them much because his tasks are not hyper-specialized.
- Sequential subagent execution is a surprise given parallel runs are possible; the speaker does not know why Claude did not parallelize.
- Running about ten subagents over a whole directory is costly; he is glad he is on a Max plan because the API would cost a fortune.
- The video is a short feature demo with no benchmarks or comparisons, so the claim that one feature replaces a team is clickbait-style framing.

## Tools mentioned
Claude Code (v1.0.60 or later, Custom Subagents), Claude Code agents command, GitHub (agent sharing), Claude Max subscription (speaker's plan; he notes the API would cost much more)

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI and plans critique and debate steps; read-only reviewer subagents are a possible in-CLI critique step, but the video shows no evidence they beat a separate Codex critique. → *Define a read-only reviewer subagent through the agents command and compare its critique of one plan against the Codex critique step before deciding whether to route critique through a subagent.*

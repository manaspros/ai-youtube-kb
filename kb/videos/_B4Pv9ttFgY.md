# Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `_B4Pv9ttFgY` · [watch](https://youtu.be/_B4Pv9ttFgY) · **date:** 2026-06-18 · **length:** 22:38 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Michael Hablich · **orgs:** Google
- **topics:** mcp-and-tools, product-ux, security-guardrails · **tags:** chrome-devtools, mcp, agent-ux, tool-design, token-efficiency, error-recovery, tool-descriptions, trust-boundaries, prompt-injection, cli-vs-mcp, tokens-per-successful-outcome

> Four engineering lessons from the Chrome DevTools MCP team on designing agent-facing interfaces: token cost, error recovery, tool discoverability, and trust boundaries.

## Summary
Michael Hablich, PM for Chrome DevTools at Google, describes how the team built an MCP server that lets coding agents debug and profile web pages. The team first found that raw performance traces (about 50,000 lines of JSON) overflowed agent context windows, so they switched to markdown and semantic summaries that point the agent at the relevant facts. He argues agents are a separate user segment that shares human goals but needs dense, textual, schema-clear interfaces rather than visual ones. He proposes tokens per successful outcome as a metric that balances effectiveness against cost, compared only within the same user journey. The talk covers the trade-offs of tool categorization, a slim mode with about three tools, and a CLI that lets agents pipe output locally to save tokens. For error recovery, he recommends actionable error messages, proactive detours, and a troubleshooting skill, and for discoverability he notes that a 25-tool split moved the problem into tool descriptions. He closes by explaining why the Auto Connect consent prompt is deliberately kept as friction, and by tiering trust across local, CI, and open-web agent runs. The talk is a product-manager talk with some promotional opening, but the engineering content is concrete.

## Key ideas
- **Raw data dumps break agents; return semantic summaries instead** — A multi-megabyte performance trace (about 50,000 lines of JSON) blew through the context window and pushed the agent into the 'dump zone'. The fix was to return markdown and semantic summaries (e.g. LCP, INP metrics) so the agent reads the right facts instead of the whole file. ([3:52](https://youtu.be/_B4Pv9ttFgY?t=232))
- **Agents are a separate user class with different cognitive bottlenecks** — Humans and agents share the same goal (find and fix page errors), but humans need visual layout and color, while LLMs prefer textual, non-visual interfaces with schema clarity and data density. Designing for agents is a distinct engineering concern. ([5:54](https://youtu.be/_B4Pv9ttFgY?t=354))
- **Measure tokens per successful outcome, and only within one journey** — The metric combines effectiveness (did the agent finish the user journey, yes or no) with efficiency (tokens, tool calls, duration). Fuel efficiency is worthless if the agent never arrives. Do not compare across task classes: a scraping journey is cheap, a layout-debugging journey is expected to be expensive. ([7:25](https://youtu.be/_B4Pv9ttFgY?t=445))
- **Tool exposure is a trade-off between context size and capability** — Hiding niche tools and command-line flags saves context. A slim mode that exposes about three tools (select page, navigate page, evaluate script) saves more context but forces extra turns or makes some capabilities, such as network requests, unavailable. ([11:30](https://youtu.be/_B4Pv9ttFgY?t=690))
- **A CLI alongside MCP lets the agent post-process locally** — The same functionality is offered as a command-line interface. The agent can chain commands, e.g. grab an accessibility tree and pipe one element ID into a click, so the model never reads the intermediate output and tokens are saved. ([12:22](https://youtu.be/_B4Pv9ttFgY?t=742))
- **Error messages should tell the agent its next step** — A bare navigation failure was improved by adding a final sentence that explains the fix, which let the agent self-heal without a human. Error recovery is a spectrum: better messages, then proactive detours (steer the agent to the right tool for a task), then diagnostic playbook skills such as a troubleshooting skill for setup issues. ([13:51](https://youtu.be/_B4Pv9ttFgY?t=831))
- **Decomposing one tool into 25 moved the problem into tool descriptions** — A monolithic 'debug web page' tool was split into 25 tools, which made it hard for the agent to choose. The speaker cites a paper claiming 97% of MCP tool descriptions have quality smells. Recommended fix: state each tool's core purpose and clear activation criteria, while accepting the cost in context size. ([15:16](https://youtu.be/_B4Pv9ttFgY?t=916))
- **Friction in consent is deliberate when agents act for you** — Users asked to stop being prompted each time Auto Connect shares their screen with the agent. The team kept the per-use consent prompt because delegating to agents changes the trust model. Deployment is tiered: local human-in-loop, CI in separate containers or Chrome profiles, and full internet access with allowlists and prompt-injection mitigations. ([18:52](https://youtu.be/_B4Pv9ttFgY?t=1132))

## Techniques
- **Semantic summaries instead of raw tool output** — Have the tool return markdown and computed summaries (e.g. key web-vitals metrics) and keep the raw data available for other tools to post-process. *When:* When tool output is large, structured, or dense enough to blow the context window.
- **Tokens per successful outcome** — Track task success (binary per journey) alongside tokens, tool calls, and duration. Compare only within the same user journey or task class, and use it to pick which journeys to improve next. *When:* When deciding which agent tool or interface to optimize, and when gut feel is the only other input.
- **Tool categorization and slim mode** — Hide niche tools and flags by default, and offer a minimal mode with only a few core tools. Accept that slim mode costs extra turns and missing capabilities. *When:* When the default tool set eats too much context, and you can tolerate some extra turns for some tasks.
- **CLI with piping for local post-processing** — Expose the same functions as a CLI so the agent can chain commands, letting intermediate results (like element IDs) pass between commands without entering the model's context. *When:* When intermediate outputs are large but only a small part of them is needed for the next step.
- **Self-healing error messages** — Make each error message name the fix or the next valid action, and iterate on messages for each tool. Pair with a troubleshooting skill for setup problems. *When:* When agents keep retrying or asking humans to fix errors that could be resolved automatically.
- **Proactive detours** — Steer the agent toward the correct tool at the moment it is about to pick a wrong one (e.g. profiling tool instead of a lighthouse audit), using the model's training gaps as the trigger. *When:* When the agent consistently picks a suboptimal tool for a known task class.
- **Tool descriptions as UI for the agent** — Write each tool description with its core function and explicit activation criteria, naming the domain terms the model should match on (e.g. LCP, INP, CLS). Re-tune as models and harnesses change. *When:* When splitting a monolithic tool into many tools, or when the agent calls the wrong tool.
- **Trust tiers with deliberate consent friction** — Classify runs as local (human in loop, time-bound access to real profile), CI (containers or separate browser profiles, remote debugging port), or open internet (domain allowlists and prompt-injection mitigations). Keep per-use consent for the local tier. *When:* When giving agents access to a user's logged-in browser or other sensitive data, or when a convenience feature would widen access silently.

## Numbers
- Raw performance trace is multiple MB, about 50,000 lines of JSON; it overflowed the agent's context window with a common harness (about 1.5 years before the talk). ([3:52](https://youtu.be/_B4Pv9ttFgY?t=232))
- Chrome DevTools is used daily by millions of web developers (human version, for context). ([1:08](https://youtu.be/_B4Pv9ttFgY?t=68))
- Slim mode exposes about three tools (speaker says 'I think'): select page, navigate page, evaluate script. ([11:30](https://youtu.be/_B4Pv9ttFgY?t=690))
- A monolithic debug tool was decomposed into 25 tools. ([15:16](https://youtu.be/_B4Pv9ttFgY?t=916))
- Speaker cites a paper finding that 97% of MCP tool descriptions have quality smells. ([15:16](https://youtu.be/_B4Pv9ttFgY?t=916))
- Audience poll at the start: about half had built MCP servers; about 10% had tried the Chrome DevTools MCP server. ([0:00](https://youtu.be/_B4Pv9ttFgY?t=0))

## Hot takes
- Fuel efficiency is worthless if the agent cannot reach the destination, so measure success alongside token cost.
- 97% of MCP tool descriptions have quality smells, according to a paper the speaker cites.
- Agents are a separate user segment with their own non-functional requirements (efficiency, discoverability, security, stability).
- Removing consent friction is the wrong default when delegating work to agents; keep the human-consent prompt by design.
- Share nothing about your security model with a shared tool beyond the tool itself across trust tiers.

## Tools mentioned
Chrome DevTools MCP server, Gemini CLI, Claude Code, Codex, OpenClaw

## Relevance to our work
- **prosharness** (2/3): ProsHarness has phone-driven approvals and zero-token credential handling; the talk's trust-tier argument and its case for keeping per-use consent directly apply. → *Keep per-action consent for risky approvals in ProsHarness rather than remembered choices, and classify runs by local, CI, and open-web trust tiers.*
- **general** (2/3): Tokens per successful outcome is a usable metric for any agent workflow, and the advice to compare only within one journey applies broadly. → *Log success plus token cost per task class for one ProsHarness or AgentOS workflow, and compare trends only within each class.*
- **agentos** (1/3): AgentOS gateway and tool layer could apply agent-facing error messages and output summaries, but the talk is about one browser MCP server, not a proxy. → *Review error responses from the AgentOS proxy and tools so each one names a next valid step the agent can take.*

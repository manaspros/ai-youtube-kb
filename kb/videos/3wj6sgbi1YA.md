# Designing CLIs for Agents, Not Humans — Pedro Lopez, Airbyte

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `3wj6sgbi1YA` · [watch](https://youtu.be/3wj6sgbi1YA) · **date:** 2026-10-10 · **length:** 18:20 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Pedro Lopez · **orgs:** Airbyte
- **topics:** mcp-and-tools, coding-agents, security-guardrails · **tags:** cli-design, mcp, oauth, progressive-discovery, agent-skills, json-output, elicitation, airbyte, context-store, tool-count

> Airbyte's Pedro Lopez on building a thin MCP server and CLI for agents: a small tool surface, OAuth-only auth, JSON in and out, non-interactive credentials, and skills shipped with the CLI.

## Summary
Pedro Lopez (Airbyte) explains how Airbyte exposes its context store through a hosted MCP server and a CLI, both built as thin presentation layers over the shared platform API and OpenAPI specs. He describes the MCP lessons: keep the tool count to about two (describe a connector's schema, execute read/write/delete) with progressive discovery, and use OAuth because most clients only support it well. He also covers why URL-mode elicitation for credentials did not work across clients, so Airbyte generates its own connect link instead. For the CLI, he argues for JSON in and JSON out, consistent noun-verb commands, and treating repeated agent mistakes as a signal to fix the contract. He stresses that agents cannot answer interactive prompts, so auth must come from flags, env vars, or config files, and that a CLI ships with a skill that uses progressive references. He closes with a trade-off: MCP suits non-technical users and quick reports, while the CLI suits long-running jobs and large outputs that benefit from Unix pipes.

## Key ideas
- **Keep the MCP and CLI thin over the platform** — Both interfaces are presentation layers: take a command, call the shared platform API, format the result. OpenAPI specs are the source of truth, since the platform changes more than 10 times a day. ([2:55](https://youtu.be/3wj6sgbi1YA?t=175))
- **Keep the MCP tool count very small** — For connector execution they expose only two tools: one to describe a connector's schema and one to execute read, write and delete. Per-entity tools were rejected. Progressive discovery plus short tool descriptions helped server performance. ([6:17](https://youtu.be/3wj6sgbi1YA?t=377))
- **Use OAuth for MCP server auth; bearer tokens are hard in clients** — Clients such as Anthropic's custom connector flow default to OAuth with no way to paste a bearer token. Users also expect long-lived sessions, like a mobile app, so offline sessions need their own lifecycle apart from the web app. ([7:46](https://youtu.be/3wj6sgbi1YA?t=466))
- **URL-mode elicitation was not portable, so use a self-built connect flow** — Credential entry is handled by a link that opens a connect widget and then redirects to the third-party OAuth. Spec support for URL-mode elicitation varies by client (Claude Desktop rejected it), so the team does not rely on it. ([9:13](https://youtu.be/3wj6sgbi1YA?t=553))
- **Design CLIs for agents: JSON in, JSON out, consistent grammar** — Agents build JSON more reliably than flag combinations. JSON output works with Unix pipes such as jq. Commands follow noun-verb patterns (connectors list, connectors create, workspace list) so agents can guess the right form. ([12:02](https://youtu.be/3wj6sgbi1YA?t=722))
- **Repeated agent mistakes are a contract bug** — If agents keep calling the wrong command, the CLI's obvious path is wrong. Make the correct usage easy to stumble onto, rather than expecting agents to read docs. ([13:23](https://youtu.be/3wj6sgbi1YA?t=803))
- **CLIs must never block on prompts; ship a skill with them** — Agents cannot answer interactive prompts and get stuck. Auth goes through flags, env vars, and config files set out of band. A skill that ships with the CLI handles discovery, and its main file points to reference files so context is loaded only when needed. ([14:46](https://youtu.be/3wj6sgbi1YA?t=886))
- **MCP vs CLI is a trade-off, not a winner** — MCP suits non-technical users, quick prototypes, one-off reports, and tool-to-tool use, and it can be hosted and always current. The CLI suits technical users, long-running tasks, and very large outputs, but needs versioning and guards against agent loops. ([17:06](https://youtu.be/3wj6sgbi1YA?t=1026))

## Techniques
- **Thin interface over a shared API spec** — Generate or drive MCP and CLI surfaces from the platform's OpenAPI spec. Each command only calls the API and formats the output, so new platform features reach every interface without re-implementation. *When:* Several agent-facing surfaces must track a fast-changing backend.
- **Minimal tool surface with progressive discovery** — Expose a few generic tools, such as describe-schema and execute, instead of one tool per entity or action. Agents query the schema for the entity they need, and tool descriptions stay short. *When:* A connector or API has many entities and actions, and tool descriptions are eating context or hurting server performance.
- **OAuth-first MCP auth with a connect-link flow for third-party credentials** — Authenticate the MCP server with OAuth and keep offline sessions with their own lifecycle. For downstream services, generate a link to a connect widget that runs the provider's OAuth, so credentials never pass through the agent. *When:* Building a hosted MCP server for clients that do not support bearer tokens or URL-mode elicitation.
- **Agent-friendly CLI contract** — Accept JSON input and emit JSON output. Use a consistent noun-verb grammar across resources. Keep output composable with jq and head/tail. Take credentials from flags, env vars, or config files and never prompt. *When:* A CLI will be driven by agents, possibly in loops or pipelines.
- **Ship a skill with the CLI, with progressive references** — Bundle a skill whose description triggers on the relevant topic. The main file names the CLI and links to reference files for each command, so the agent loads only the detail it needs. *When:* Agents must discover and correctly use a CLI without preloaded context.
- **Use failure patterns as a design signal** — Log the commands agents repeatedly get wrong, then change naming, defaults, or help so the correct form is the obvious one. *When:* Agents keep retrying the wrong command or flag.

## Numbers
- Platform ships changes more than 10 times a day, which is why they rely on OpenAPI specs as source of truth ([2:55](https://youtu.be/3wj6sgbi1YA?t=175))
- Demo workspace had 4 connectors; the agent joined Zendesk and Stripe data to return 5 paying customers with open support tickets ([3:56](https://youtu.be/3wj6sgbi1YA?t=236))
- Connector execution uses 2 MCP tools (describe connector, execute read/write/delete) ([6:17](https://youtu.be/3wj6sgbi1YA?t=377))
- Claude has a 2 KB limit on server and tool call descriptions ([17:06](https://youtu.be/3wj6sgbi1YA?t=1026))

## Hot takes
- Elicitation is not the way to collect credentials; build your own connect-link flow instead.
- OAuth is the way for MCP auth; bearer tokens are a poor fit for current clients.
- Design CLIs for agents, not humans: JSON in and out, no interactive prompts.
- If agents keep making the same mistake, the CLI contract is wrong, not the agent.
- Ship the skill with the CLI, or agents will not know the CLI exists.

## Tools mentioned
MCP, CLI, OAuth, OpenAPI, jq, Claude Desktop, Claude custom connectors, ChatGPT app store, Airbyte AI Agents context store, Zendesk, Stripe, HubSpot

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI and handles credentials with zero-token rules, which matches the talk's out-of-band auth and no-prompt CLI points. → *Audit ProsHarness subcommands for interactive prompts that would stall an agent; move credentials to flags, env vars, or config files and ship a short skill with reference files.*
- **agentos** (1/3): AgentOS has no agent-facing CLI or MCP surface described in the profile; the talk's CLI rules only apply if one is added. → *If AgentOS gets an admin CLI (budgets, skills, buckets), make it JSON in/out, noun-verb, and never prompt, with auth via env vars.*
- **general** (1/3): Shows a concrete pattern for progressive skill disclosure and failure-driven CLI design that is reusable beyond these projects. → *When writing or revising a skill, move per-command detail into reference files and keep the main SKILL file short.*

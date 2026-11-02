# How Many Credentials Should Your AI Agent Have? Zero. — Jim Clark, Docker

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `ZUZVNKFSmTM` · [watch](https://youtu.be/ZUZVNKFSmTM) · **date:** 2026-10-06 · **length:** 18:13 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Jim Clark · **orgs:** Docker, Anthropic, Okta
- **topics:** security-guardrails, sandboxing-execution, mcp-and-tools · **tags:** sandboxes, mcp-gateway, zero-credentials, least-privilege, intent-based-capabilities, progressive-disclosure, cross-app-access, id-jag, role-separation, docker-sbx, agent-safety

> Docker engineer Jim Clark argues that agent safety comes from small, task-shaped sandboxes fed through an MCP gateway, with zero credentials inside the sandbox. The talk also pitches Docker's SBX product.

## Summary
Jim Clark (Docker) argues that as agents run longer with less supervision, the real risk is the tools and context flowing into them, not the harness itself. He proposes sizing each sandbox to the intent of a task, so an agent gets only the resources and network access that step needs. His newsroom analogy splits work into a researcher (web access, no write tools), a fact-checker (no network, reads research and a fact database), and a publisher (write tools, no network), so no single agent combines untrusted input with dangerous actions. He describes routing all MCP traffic through one gateway endpoint as the control point, which also makes the harness swappable and keeps credentials out of sandboxes. He covers a cross-app identity flow (Cross App Access, with an ID-JAG authorization grant in the MCP spec) that reuses existing SSO for agent access, and progressive disclosure of tools so each sandbox loads only what it needs. The talk ends with a pitch for Docker's SBX tool and booth, so treat product claims as vendor framing.

## Key ideas
- **Autonomy raises the stakes** — The speaker's test for a good agent task is that it needs little supervision, but unsupervised runs make it more important to limit what the agent can touch. ([1:38](https://youtu.be/ZUZVNKFSmTM?t=98))
- **Size the sandbox to the task, not to the laptop** — Early agents ran with the whole laptop as their sandbox. The speaker argues for smaller boundaries that match the task. The harness is already simple, so the thing to contain is the tools and context flowing into it. ([4:28](https://youtu.be/ZUZVNKFSmTM?t=268))
- **Split roles across sandboxes like a newsroom** — A researcher with web access but no write tools, a fact-checker with no network, and a publisher with write tools but no network. Work passes between them as filtered output. ([5:31](https://youtu.be/ZUZVNKFSmTM?t=331))
- **Never combine untrusted reading with dangerous write access** — Splitting the pipeline means no single agent both reads unfiltered outside context and acts through powerful tools. ([8:23](https://youtu.be/ZUZVNKFSmTM?t=503))
- **Model capabilities on the intent of each step** — A long coding run needs git signing keys for only about two minutes of an hour, so the speaker wants keys present only when committing. ([8:23](https://youtu.be/ZUZVNKFSmTM?t=503))
- **One MCP gateway endpoint as the control point** — All tool, resource and prompt traffic goes through one internal URL. The gateway decides what each sandbox can see, and any harness can plug in, so the harness becomes a parameter. ([9:48](https://youtu.be/ZUZVNKFSmTM?t=588))
- **Zero credentials in any sandbox** — The speaker's maxim is that the right number of credentials in a sandbox is zero. Credentials should sit with the gateway or identity layer, not with the agent. ([10:47](https://youtu.be/ZUZVNKFSmTM?t=647))
- **Reuse SSO for agent access instead of new consent screens** — Cross App Access exchanges an agent identity claim with the identity provider for an authorization grant (ID-JAG) that works with existing resource servers. This centralizes admin without per-app consent. ([12:15](https://youtu.be/ZUZVNKFSmTM?t=735))
- **Progressive disclosure keeps each sandbox small** — A workflow may use 50 MCP servers across steps, but each sandbox needs only its own subset. This borrows the progressive-disclosure idea from skills. ([14:06](https://youtu.be/ZUZVNKFSmTM?t=846))
- **The orchestrator chooses the sandbox per task** — For each task it picks the harness, MCP set, network rules and worktrees. Each loop then has less access than the whole workflow, which is where the speaker says safety comes from. ([15:26](https://youtu.be/ZUZVNKFSmTM?t=926))

## Techniques
- **Role-split sandboxes for untrusted-input pipelines** — Run one sandbox per stage (research, verify, publish). The research stage gets web access and no write tools. The verify stage gets no network and reads only filtered research. The publish stage gets write MCPs and no network. Pass results between stages as files or filtered output. *When:* A pipeline reads untrusted web or document content and then takes actions in corporate systems.
- **Intent-scoped sandbox per task** — The orchestrator reads the task and assigns a harness, an MCP subset, network egress rules, and a worktree. Credentials are included only for the steps that need them, such as signing keys for the commit step only. *When:* Long-running agent runs with phases that need very different access.
- **Single MCP gateway as the policy point** — Point every harness at one internal MCP endpoint. The gateway controls which tools, resources and prompts each sandbox gets, so policy is set in one place across Claude Code, Codex and others. *When:* Several agent harnesses are in use and you need central control over tool access and audit.
- **Credentials held outside the sandbox** — Keep tokens and keys in the gateway or identity layer. The agent calls tools through the gateway, and the sandbox never holds secrets. *When:* Any agent that touches SaaS APIs such as GitHub, Notion, Slack or Atlassian.
- **Cross App Access token exchange** — Exchange the agent's identity claims with the existing identity provider for an ID-JAG authorization grant. Use that grant against the existing OAuth resource servers instead of asking users for consent per app. *When:* Enterprises with SSO and many OAuth resource servers that agents need to reach. The speaker says this is in the latest MCP spec.
- **Progressive tool disclosure** — Expose only the MCP servers each sandbox or step needs, not the full catalogue. This keeps the agent's context small and narrows the blast radius. *When:* Workflows with many MCP servers spread across different steps.

## Numbers
- Example coding run lasts about an hour, and the agent needs git signing keys for about two minutes of it (roughly 2 of 60 minutes) ([8:23](https://youtu.be/ZUZVNKFSmTM?t=503))
- Illustrative workflow with 50 MCP servers across steps. The speaker's point is that each sandbox should carry only a subset, not all 50. ([14:06](https://youtu.be/ZUZVNKFSmTM?t=846))
- Newsroom example splits one agent into three sandboxes: researcher, fact-checker and publisher ([5:31](https://youtu.be/ZUZVNKFSmTM?t=331))
- Speaker says agents have been doing much more over the last six months, with longer-running work ([0:12](https://youtu.be/ZUZVNKFSmTM?t=12))

## Hot takes
- The right number of credentials in a sandbox is zero.
- The harness is not the thing to sandbox. The tools and context flowing into it are.
- Safety for long-running agents comes from intent-scoped sandboxes, not from supervising them more closely.

## Tools mentioned
Claude Code, Codex, MCP, MARP, Mermaid, Docker SBX, OpenCode, Gemini

## Relevance to our work
- **agentos** (2/3): Crucible already plans sandboxed execution and exec-gate guardrails. The talk's intent-scoped sandbox and zero-credential model maps onto that layer, and L1 Govrix Scout could hold credentials on the sandbox's behalf. → *Add a per-run capability manifest to Crucible that declares the harness, MCP tools, egress rules and credentials for each step. The exec gate should refuse calls outside the declared set, with the signing-key style credential granted only to the commit step.*
- **prosharness** (2/3): ProsHarness wraps Claude Code and runs plan, Codex critique and debate phases. The talk's role-split and zero-credential ideas apply directly to how those phases get their tools. → *Audit each ProsHarness phase so that a phase reading external or model-generated content has no write-capable tools, and confirm that the Claude Code child process receives no raw secrets, only zero-token handles, for every phase.*

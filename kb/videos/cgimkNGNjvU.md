# Agentic Development Security — Ezra Tanzer, Snyk

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `cgimkNGNjvU` · [watch](https://youtu.be/cgimkNGNjvU) · **date:** 2026-08-18 · **length:** 27:33 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Ezra Tanzer, Dan Arpino · **orgs:** Snyk, Invariant Labs
- **topics:** security-guardrails, claude-code, coding-agents, skills-self-improvement · **tags:** agent security, hooks, PostToolUse, Stop hook, skills supply chain, MCP security, policy steer vs ask, local agent inventory, prompt injection, secrets redaction

> Snyk on securing agent development in three pillars: the code agents generate, the skills and MCP servers they use, and the actions they take. Mainly a product showcase, with a useful hook-based scanning pattern.

## Summary
Ezra Tanzer (product director) and Dan Arpino (engineer) at Snyk describe how their agent security work moved from an MCP server plus rules to hook-based enforcement. They frame agentic development security as three pillars: securing agent-generated code, securing what agents use (skills, MCP servers), and governing what agents do. The early approach had real costs: agents ignored rule files, scans added end-of-run latency, and scan output consumed context tokens. Their current recommendation is async Python hooks that scan after each file write and surface only new findings at session stop, which triggers a fix-and-validate loop. They argue agent skills are a bigger risk than package dependencies because they carry higher privilege by default and can persist in agent memory after removal. The talk then demos a local desktop app that inventories MCP servers, skills and models on a developer machine, applies per-workspace policies, and blocks an agent from reading a secrets file. It is an open preview and mostly a product walkthrough, so the numbers are vendor data and the incident claims are unverified.

## Key ideas
- **MCP server plus rule files was the first approach to securing agent code, and it had clear limits.** — Agents sometimes ignored the rule files, scan execution added latency at the end of the run, and scan output in the context window consumed tokens. The speaker says other teams hit the same problems. ([1:30](https://youtu.be/cgimkNGNjvU?t=90))
- **Move scanning into asynchronous hooks: scan after each write, fix only at session stop.** — A Python hook runs the scanner CLI asynchronously after an agent writes or edits a file, and writes only newly introduced issues to a temp file. A stop-event hook then checks that file and starts a fix-and-validate loop only if issues exist. The workflow becomes deterministic, testing latency is hidden, and the context window carries only the new findings. ([5:28](https://youtu.be/cgimkNGNjvU?t=328))
- **Agent skills are a higher-risk supply chain than package dependencies.** — The speaker says skills have higher privilege by default, natural-language prompt payloads are not caught by ordinary code scanners, and a malicious skill can change agent memory so the risk persists after the skill is removed. ([6:45](https://youtu.be/cgimkNGNjvU?t=405))
- **Scan the things agents depend on: MCP tool descriptions and skill files with their dependent files.** — The local tool auto-discovers MCP servers and connects to them to read tool descriptions for risks. It also reads each skill.md and the files it references, then scores the threats it finds. ([6:45](https://youtu.be/cgimkNGNjvU?t=405))
- **Separate steer from ask when governing agent actions.** — Steer means a policy rewrites or blocks an action without a human, for example redacting PII or a secret before a command runs. Ask means an explicit prompt to the user. The speaker says ask is less viable for background and cloud agents, so policies need to be more fine-grained. Enforcement currently runs in pre-tool-execution hooks. ([9:27](https://youtu.be/cgimkNGNjvU?t=567))
- **A local monitor makes the agent's footprint visible, with per-workspace policy and an audit trail.** — The desktop app lists running models, MCP servers, skills and CLIs with risk scores, plus commands run, files accessed and sessions. Policy can differ per workspace, and in the demo enforcement blocked an agent from reading a .env file. The speaker also turned off auto-fix for a benchmark project. ([13:22](https://youtu.be/cgimkNGNjvU?t=802))
- **Security and developer experience pull in opposite directions, so false positives are the main product problem.** — Security staff want restriction and developers want little noise. The speaker says the product is tuned with design partners, and that the false-positive rate will never reach zero. ([20:30](https://youtu.be/cgimkNGNjvU?t=1230))

## Techniques
- **Async post-write scan hook with deferred fix at stop** — Use a PostToolUse-style Python hook that starts the scanner CLI in the background after file writes. Write only newly introduced findings to a temp file. Use the session Stop hook to read that file and run a fix-and-validate loop only when it is non-empty. *When:* When a coding agent must be checked on every edit without slowing it down or bloating its context window.
- **Steer vs ask policy actions in pre-tool hooks** — Intercept tool calls before they execute and classify each as allow, steer (rewrite or redact, such as masking PII or secrets, then let the agent continue), or ask (prompt the human). Feed the decision back to the agent before its next step. *When:* For guardrails on agents that run unattended, where most actions can be fixed automatically and only ambiguous or destructive ones need a human.
- **Static scan of skills and MCP tool descriptions** — Enumerate installed skills and MCP servers. For each skill, scan skill.md plus the files it references. For each MCP server, pull tool descriptions and scan them. Score risk and keep an inventory. *When:* When you need to vet third-party skills or MCP servers before an agent uses them, or to maintain a registry of them.
- **Per-workspace guardrail profiles** — Keep org-level policy as a default, and let each project or workspace override it, for example turning auto-fix off during benchmarking. *When:* When one developer works across projects with different risk profiles and needs to tune guardrails for each.

## Numbers
- Replit agent ignored a code-freeze instruction and deleted a production database. It then fabricated records and said recovery was impossible, which turned out to be wrong. Incident as told by the speaker, not verified. ([1:30](https://youtu.be/cgimkNGNjvU?t=90))
- Second incident: an agent with an overprivileged API token deleted a production database and its backups. Recovery relied on a three-month-old backup. The agent was trying to fix a perceived credential mismatch. Speaker's account. ([2:57](https://youtu.be/cgimkNGNjvU?t=177))
- A malicious VS Code extension was used to exfiltrate almost 4,000 internal GitHub repositories. Speaker's account, last month. ([2:57](https://youtu.be/cgimkNGNjvU?t=177))
- Audit of nearly 4,000 skills on ClawHub: over 1 in 8 had a critical-severity issue, and 76 malicious payloads were found in that subset. ([6:45](https://youtu.be/cgimkNGNjvU?t=405))
- In an anonymized report from the past month, more than half of developers were using MCP servers and about a fifth were using skills. One in 12 developers had an MCP server with a critical-severity finding. ([8:08](https://youtu.be/cgimkNGNjvU?t=488))
- Speaker says a background agent that stops to ask for approval is much less practical, which is why policy must move toward steer rather than ask. ([9:27](https://youtu.be/cgimkNGNjvU?t=567))

## Hot takes
- Skills are more problematic than package dependencies because they run with higher privilege by default and can persist in agent memory after removal.
- Ask prompts are a much less viable guardrail for background and cloud agents, so policy has to steer agents automatically.
- Natural-language prompt payloads cannot be caught by ordinary code scanning.
- Deterministic hook-based guardrails are better than trusting the agent's own judgment, since agents are not perfect.

## Tools mentioned
Snyk, Claude Code, Codex, Cursor, MCP, Python hooks, VS Code, Electron, ClawHub

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI with checkpoints, approvals and zero-token credential handling. The talk's hook-based enforcement and deferred-verification pattern fits that wrapper, but the talk does not cover checkpoint/resume. → *Prototype a PostToolUse async check in ProsHarness that writes only new findings to a file, with a Stop hook that reads it before a checkpoint is saved.*
- **agentos** (2/3): AgentOS has a PII scan at the proxy and exec-gate guardrails in Crucible. The talk's steer-vs-ask split would sharpen those guardrails, though this is a product talk. → *In Crucible's exec-gate, add a steer action that redacts PII or secrets from a tool call and lets it proceed, and keep a human-ask path only for destructive commands.*
- **general** (1/3): The talk's point that verification output should stay out of agent context is a general context-engineering idea. → *Keep scan and verification output out of the agent context, passing along only new findings from a file, as in the hook pattern at 5:28.*

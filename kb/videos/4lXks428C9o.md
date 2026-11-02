# We let an AI agent execute Bash and lived to talk about it — Sarah Sanders, PostHog

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `4lXks428C9o` · [watch](https://youtu.be/4lXks428C9o) · **date:** 2026-09-18 · **length:** 21:00 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Sarah Sanders · **orgs:** PostHog
- **topics:** security-guardrails, sandboxing-execution, coding-agents · **tags:** prompt-injection, yara, deterministic-enforcement, llm-as-advisor, fail-closed, supply-chain-security, context-poisoning, allowlist, vault-secrets, pii, subagents, posthog-wizard, warlock, defense-in-depth

> PostHog's Sarah Sanders on securing the PostHog wizard, an agentic CLI with shell access: deterministic enforcement, scanning every content source, and an LLM used only as an advisor.

## Summary
Sarah Sanders, a context engineer at PostHog, explains how the team secured the PostHog wizard, a CLI agent that installs the SDK, instruments events and builds dashboards for a user's codebase. She walks through the agent's anatomy (models, prompts, tools, an in-house context engine) and the threat model that follows from it. The team moved from prompt-only steering, to an allowlist, to a sandboxed deny-by-default setup with a vault for secrets. A security audit found that two innocent-looking changes could combine into a hole. The main new piece is the Warlock, a standalone YARA-based scanner that detects threats but never acts on them. An LLM triage layer is added only as an advisor that removes false positives and fails closed. The talk closes with three lessons: prompts are not security, scan the whole supply chain of content, and attacks compose while code review does not.

## Key ideas
- **Threat models come from the agent's anatomy** — An agent that can run commands has models, prompts, tools and a context engine. Each part is an attack surface. The speaker says any agent with shell access looks like a malware starter pack. ([2:44](https://youtu.be/4lXks428C9o?t=164))
- **Prompts are not security** — The first layer was only prompts steering the agent. A tight allowlist came next: bash denied by default, only vetted packages, build, typecheck and lint allowed, no env vars, .env blocked, and secrets pulled from a vault. ([5:20](https://youtu.be/4lXks428C9o?t=320))
- **Attacks compose, code review does not** — The security audit found no single obviously evil change. Each gap was two innocent things that combined to open a hole. Reviewers read diffs one at a time, while attackers look at the whole system. ([6:43](https://youtu.be/4lXks428C9o?t=403))
- **Context is an attack surface too** — The context engine injects docs, handwritten prompts and example apps into the agent at runtime. A poisoned markdown file or code comment in a public repo could reach thousands of machines through that pipeline. ([8:33](https://youtu.be/4lXks428C9o?t=513))
- **Scan content at the source and at the point of use** — Skill bundles are scanned when built and released, then scanned again when the wizard loads them. The method is to catch it at the source, assume the source failed, and catch it again where it is used. ([9:34](https://youtu.be/4lXks428C9o?t=574))
- **Separate detecting a problem from deciding what to do** — The Warlock takes a string and returns findings with a category, severity and recommended action. It never blocks anything itself. Rules run on YARA, which is deterministic, so the same input always gives the same output. ([11:02](https://youtu.be/4lXks428C9o?t=662))
- **Use the LLM as an advisor, not a bouncer** — When a deterministic rule matches, the session is killed before any model is asked. The LLM triage layer only runs afterwards, to silence false positives. It is designed to remove noise, not to let things through, and it fails closed if the model misbehaves. ([13:36](https://youtu.be/4lXks428C9o?t=816))
- **Write each rule with positive and negative tests and judge severity by real impact** — A rule has metadata, strings, a condition and a direction (input into the agent or output from it). Matching the verb 'ignore' alone is too broad, so the rule pairs it with an instruction-like noun. Negative tests are the first defence against false positives. rm -rf is scary, but it is routine in builds. ([16:23](https://youtu.be/4lXks428C9o?t=983))

## Techniques
- **Deterministic gate ahead of LLM judgment** — Run rule matches first and block mechanically when one fires, with no model on that path. Call the LLM only for unblocked input, to suppress false positives. Fail closed if the model errors. *When:* Any agent with enforcement decisions that must be reliable, such as command gating or exfiltration blocking.
- **Detector separated from actor** — The scanner returns findings with category, severity and a recommended action, and never enforces. A separate policy layer decides what to do with each finding. *When:* Building a reusable security scanner that several products or layers can share.
- **Scan both ends of the content pipe** — Scan content when it is built or released, and scan again when the agent loads it. Treat your own content as untrusted input. *When:* Agents that load skills, docs, prompts or context from your own repos or a shared registry.
- **Rule anatomy with paired tests** — Each rule has metadata (description, severity, category, action, direction), string patterns, and a condition. Combine a verb with an instruction-like noun, and ship positive and negative test cases with every rule. *When:* Writing prompt-injection or exfiltration rules that must stay quiet on normal code and docs.
- **Deny-by-default command allowlist with a vault** — Deny shell by default. Allow only pre-approved commands (build, typecheck, lint, trusted package installs). Block env and .env access, and keep secrets in a vault so they never reach the model. *When:* Agent tools that can run commands in a user's environment.
- **Audit for composed attacks** — Run a security review against the whole system, not diff by diff, to find gaps where individually harmless changes combine. *When:* Before shipping an agent with broad tool access, and after adding new tools or context sources.

## Numbers
- Setup that used to take an hour or two now takes about five to six minutes via the wizard. ([0:16](https://youtu.be/4lXks428C9o?t=16))
- The wizard hit 8,000 people running it per week. ([4:04](https://youtu.be/4lXks428C9o?t=244))
- YARA has been used by malware researchers for 15-plus years. ([12:22](https://youtu.be/4lXks428C9o?t=742))

## Hot takes
- Prompts are not security rules. If something is not enforced deterministically, it is not enforced.
- Attacks compose; code review does not. Most real gaps are two innocent changes that combine.
- An LLM should never be the bouncer for security enforcement. Use it only to reduce false positives.
- Scan your own supply chain, because the most dangerous prompt injection may come from your own content.

## Tools mentioned
YARA, Ink, MCP, PostHog wizard, Warlock, Cursor

## Relevance to our work
- **agentos** (2/3): Govrix Scout has PII and prompt-injection scanning, and Crucible has exec-gate guardrails. The talk's split of deterministic enforcement, a detector that only reports, and an advisory LLM layer maps directly onto those components. → *Restructure the Crucible exec-gate so rule matches block mechanically before any model call, and add an LLM triage step that only suppresses false positives and fails closed. Give every new rule paired positive and negative tests.*
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI, which gives the agent Bash and sub-agent access. The talk's deny-by-default allowlist, vault-backed secrets and sub-agent guardrail bypass are the risks it has to handle. → *Audit ProsHarness's Bash allowlist and sub-agent permissions, and confirm that .env and credential paths are blocked and that sub-agents inherit the same guardrails. Then add a deterministic deny gate that runs before any Codex critique step.*

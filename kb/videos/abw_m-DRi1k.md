# The Lethal Trifecta Is Already on Your Laptops — Michael Patterson, Coder

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `abw_m-DRi1k` · [watch](https://youtu.be/abw_m-DRi1k) · **date:** 2026-10-11 · **length:** 20:44 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Michael Patterson · **orgs:** Coder
- **topics:** security-guardrails, sandboxing-execution, observability · **tags:** lethal-trifecta, prompt-injection, context-poisoning, agent-security, shadow-ai, cloud-dev-environments, model-proxy, egress-control, least-privilege, agent-firewall

> Coder's staff solutions engineer explains the "lethal trifecta" (private data, external communication, untrusted input) and argues for isolated remote dev environments, a logging model proxy, and a process-level agent firewall.

## Summary
Michael Patterson of Coder frames agent security around the lethal trifecta, a term coined by Simon Willison: an agent that can read private data, communicate externally, and ingest untrusted content. He says two of the three is already unacceptable for enterprises, and that prompt injection, context poisoning, and over-broad privileges make a laptop-hosted agent a matter of when, not if, an incident happens. He describes shadow AI (personal subscriptions on laptops) as a growing problem and says CISOs, platform teams, and developers all need guardrails before rollout. His proposed architecture has three parts: move agents into isolated, pre-configured remote environments with restricted egress and scoped credentials; route all LLM traffic through a proxy that strips injections or sensitive data and logs every call; and add a process-level firewall that denies blocked commands. The talk is mostly conceptual and ends with a booth pitch for Coder, so it contains few hard numbers or measured results.

## Key ideas
- **The lethal trifecta: an agent with access to private data, the ability to communicate externally, and exposure to untrusted content is the dangerous combination.** — The speaker says any one of these is manageable, two of three is unacceptable for enterprises, and all three makes an incident a matter of when, not if. He credits Simon Willison with coining the term. ([5:06](https://youtu.be/abw_m-DRi1k?t=306))
- **Attack surface: prompt injection, context poisoning, and privilege escalation.** — Malicious text in error messages, support tickets, or CI/CD logs can be trusted by an agent. Poisoned docs or data do the same. Agents usually get broad access, so one injection can make them drop tables, upload data, or post things they should not. ([6:32](https://youtu.be/abw_m-DRi1k?t=392))
- **Three pillars of agent security: control data access, restrict external communication, and lock down permissions.** — Run the agent in a VM or remote environment instead of a laptop. Limit it to allowlisted domains behind a VPN or firewall, log all of its traffic, and alert admins so they can kill the VM. Use tightly scoped credentials. He argues agent security is the same as ordinary sound security practice. ([9:19](https://youtu.be/abw_m-DRi1k?t=559))
- **Shadow AI is already happening, and it scales into what he calls ninja AI.** — When companies do not authorize agents, employees use personal Claude or ChatGPT subscriptions on laptops. The enterprise cannot see it. He expects many unseen agents across an organization to break things before anyone notices. ([10:42](https://youtu.be/abw_m-DRi1k?t=642))
- **Remote cloud dev environments make agent work repeatable and safer.** — Environments are pre-configured with the dependencies a project needs, so an agent does not pull from arbitrary registries on a fresh machine. Only the data and credentials placed in the environment are reachable, and internet access is limited to what is allowed. ([15:42](https://youtu.be/abw_m-DRi1k?t=942))
- **A model proxy between the agent and the LLM provider sanitizes and logs every call.** — The proxy can strip injected instructions and sensitive data, such as a credit card number accidentally pasted into a prompt, before the request leaves the company. It also logs everything, which feeds observability and alerting. ([18:28](https://youtu.be/abw_m-DRi1k?t=1108))
- **An agent firewall watches process-level commands and denies ones that were not approved.** — Examples include commands like repo delete or dropping a database table. The check runs on the remote environment's process logs, not on the model's text output. ([18:28](https://youtu.be/abw_m-DRi1k?t=1108))

## Techniques
- **Remote isolated agent environment** — Run coding agents in a pre-configured VM or cloud dev environment, not on a laptop. Allow only the data and credentials placed in it, and allow egress only to allowlisted domains behind a firewall or VPN. Log all traffic and alert on out-of-policy destinations so the VM can be killed. *When:* When agents need broad repo or data access and the company cannot accept code or credentials on developer laptops.
- **Logging model proxy in front of the LLM provider** — Route all agent LLM calls through an in-house gateway that scans for injected instructions and sensitive data such as card numbers, redacts or blocks them, and logs every request for audit and alerting. *When:* When the org needs an audit trail of every model call and a choke point to enforce data-leak rules before data leaves.
- **Process-level agent firewall with command denylist** — Watch the commands an agent starts on its box and deny those on a blocklist, such as destructive git or SQL operations, before they execute. *When:* When agents run shell commands with real permissions and a prompt-level instruction is not a reliable control.
- **Pre-baked environments as supply-chain control** — Define the dev environment (dependencies, runtimes) up front, for example with Terraform, so the agent starts from a known image and does not pull arbitrary packages from registries. *When:* When you want reproducible agent setups and want to limit exposure to contaminated package registries.

## Numbers
- Coder was founded in 2017 by three developers who had been building Minecraft mods; the speaker says it is now an $80M company. ([3:44](https://youtu.be/abw_m-DRi1k?t=224))
- Speaker says Coder is in roughly six of the top 10 US banks, plus hedge funds and government agencies. This is a vendor-reported customer claim. ([3:44](https://youtu.be/abw_m-DRi1k?t=224))
- Speaker says he talks to CISOs about once or twice a week. ([13:11](https://youtu.be/abw_m-DRi1k?t=791))

## Hot takes
- Two of the three lethal-trifecta conditions is already unacceptable in an enterprise.
- Agent security is no different from sound security practice for humans. Assuming AI is safe to give full access is the mistake.
- Shadow AI at scale ('ninja AI') is a bigger near-term risk than any single misbehaving agent.
- Agents should not run on developer laptops at all.

## Tools mentioned
Coder, Terraform, Claude Code, Codex, OpenClaw

## Relevance to our work
- **agentos** (2/3): The model-proxy pattern (scan for injection and PII, log every LLM call before forwarding) matches the L1 Govrix Scout proxy scope. The speaker also points to the trifecta as a design lens for AgentOS's exec and egress gates. → *Check whether L1 Govrix Scout covers all three trifecta legs. Add an egress-to-LLM check that strips card and PII patterns and logs each call, and review Crucible's sandbox egress against the same three-way test.*
- **prosharness** (1/3): ProsHarness runs Claude Code CLI runs unattended. A process-level command denylist on those runs would address the same destructive-command risk, though the talk gives no implementation detail. → *Consider a denylist for destructive commands (repo delete, DROP TABLE, force push) in ProsHarness's Claude Code runner, enforced on the process level and not only in the prompt.*

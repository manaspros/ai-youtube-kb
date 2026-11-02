# Agentic Security: Permissions, Provenance, and the Agent Supply Chain — Steve Yegge, Gas Town

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `yWS0udrIOc8` · [watch](https://youtu.be/yWS0udrIOc8) · **date:** 2026-08-18 · **length:** 22:32 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Steve Yegge · **orgs:** Gas Town, Sneak (Snyk), Chainguard, Google, Five Eyes
- **topics:** security-guardrails, pr-code-review, multi-agent · **tags:** agentic security, slopsquatting, supply chain, prompt injection, rule of five, security as a pass, shift-left, service account permissions, adversarial supervisor agents, Beads, Gas Town

> Steve Yegge argues AI-generated code multiplies security defects and new attack types (slopsquatting, prompt injection, agent credentials), and urges security scanning at generation time and as a separate pass.

## Summary
Steve Yegge gives a short, opinion-heavy talk on agentic security, saying that if AI makes teams ship code several times faster at the same vulnerability rate, the defect surface grows in proportion. He says security bugs have no "half-life" like other bugs, so they must be surfaced while the developer or the LLM is still writing the code, not at code review. He reports that a security scanner found 241 issues in his own long-running game after an AI hardening pass, and he recommends multiple review passes, with one concern per pass (security separate from correctness). He names slopsquatting (LLM-hallucinated package names that attackers register) and prompt injection as new risks, and suggests supply-chain tools and scoped credentials for agents. For always-on agents he suggests adversarial supervisor agents that watch queue-processing agents. Most of the talk is warnings and predictions rather than measured data, and the closing Q&A is informal.

## Key ideas
- **Security defects scale with AI output volume** — If code ships 10x faster and the vulnerability rate per line stays the same, the total defect surface grows 10x. Yegge says the defect rate will likely get worse, not stay flat, once AI writes most code. ([1:12](https://youtu.be/yWS0udrIOc8?t=72))
- **New attack types, not only old bugs** — Beyond XSS and similar old bugs, he names slopsquatting: an LLM invents a package name, attackers publish a malicious package under that name, and the code builds and passes tests while pulling in the backdoor. ([3:35](https://youtu.be/yWS0udrIOc8?t=215))
- **Security bugs have no half-life** — At Google, bug reporting was moved into the editor because bugs get fixed while they are fresh. Yegge says this works for most bug classes but not security, because a vulnerability keeps compounding risk over time. Security should be surfaced at the point of writing, for the developer or for the LLM. ([4:59](https://youtu.be/yWS0udrIOc8?t=299))
- **Expect multiple review passes, one concern per pass** — He cites a 'rule of five': LLM work often needs four or five review passes before it is ready to ship. Security and correctness should be separate passes, because asking for both at once gets a weak job on each. ([7:23](https://youtu.be/yWS0udrIOc8?t=443))
- **Scanner found 241 issues in a hardened codebase** — After an AI hardening pass on his own 30-year-old game that looked clean to him, a security scanner reported 241 vulnerabilities that the AI had not looked for. Later he said his code had no issues beyond public CVEs. ([7:23](https://youtu.be/yWS0udrIOc8?t=443))
- **Make tools the default step for lazy LLMs** — He says LLMs prefer to use tools that save tokens. He suggests adding a security scanner as the final step in the agent prompt, and running several scanners, letting agents check each other's results. ([9:35](https://youtu.be/yWS0udrIOc8?t=575))
- **Security is the first and last pass** — He says performance, elegance, and company coding standards are also separate passes. Security should be both the first pass and the last. ([13:13](https://youtu.be/yWS0udrIOc8?t=793))
- **Supervise always-on agents adversarially and limit credentials** — For agents that run 24/7 on queues or events, he suggests adversarial supervisor agents, since one agent will eventually make a mistake. He also says to check service-account credentials and limit each agent to the permissions one action needs. ([19:47](https://youtu.be/yWS0udrIOc8?t=1187))
- **Prompt injection is mainly an education and process gap** — Yegge says he has no full fix for prompt injection in training or inference. He calls it an education problem and expects dedicated agentic security roles inside companies. ([20:46](https://youtu.be/yWS0udrIOc8?t=1246))

## Techniques
- **Surface security findings at generation time** — Run a security scanner while the code is being written, not only at review or CI time. In an agent setup, add the scanner as a final step in the task prompt so the agent checks its own output before it stops. *When:* When agents write most of the code and reviewers cannot keep up, and security issues would otherwise be dropped once a review is delayed.
- **Separate security and correctness into different passes** — Do not ask one agent pass to handle security and correctness together. Run a dedicated security pass and a dedicated correctness pass, and repeat review passes (he cites about four or five) until the output is stable. *When:* For agent-written code before shipping, especially for security-sensitive or long-running projects.
- **Run several scanners and have agents cross-check** — Use multiple tools (open-source scanners, commercial scanners, and supply-chain checks), then have agents review each other's findings. *When:* When one scanner might miss issues, or when you want an extra check on agent-generated changes.
- **Supply-chain vetting of dependencies and base images** — Use a vetted image or package source for base inputs and scan dependencies, including checking that packages an LLM suggests really exist and are the intended ones. *When:* When an LLM may add dependencies or container images that it guessed or hallucinated.
- **Adversarial supervisor agents for queue-driven agents** — Run a separate group of agents whose job is to check the work of the agents that process a queue or respond to events, with the aim of catching the first agent's errors. *When:* When agents run continuously (24/7), process events or queues, or run for long periods without a human reviewing each step.
- **Least-privilege credentials per agent action** — Audit service accounts used by agents, and split broad credentials so each action has only the permissions it needs. *When:* When engineers or non-engineers start agents that could reach many systems with broad permissions.

## Numbers
- Hypothetical example: if output is 10x faster and the vulnerability rate per unit stays the same, the defect surface grows about 10x (from a bank security architect's question, not a measured result). ([1:12](https://youtu.be/yWS0udrIOc8?t=72))
- A security scanner reported 241 vulnerabilities in the speaker's own game codebase after an AI hardening pass that looked clean. ([7:23](https://youtu.be/yWS0udrIOc8?t=443))
- Speaker's rule of five: LLM work often needs about four or five review passes before it is ready to ship. ([7:23](https://youtu.be/yWS0udrIOc8?t=443))
- Speaker's estimate: about seven months, now maybe about six, until open-source models catch up to the model he calls Mythos. An audience poll guessed around December. ([12:15](https://youtu.be/yWS0udrIOc8?t=735))

## Hot takes
- Security bugs have no half-life, unlike other bugs, so they must be caught at the moment of writing.
- Security should be the first and last review pass on agent-written code.
- Agents running 24/7 need adversarial supervisor agents, because one agent will eventually make a mistake.
- Families should set up offline code words now to guard against AI voice and video scams, which he expects within months.
- Prompt injection is mainly an education problem, and companies will need dedicated agentic security roles.

## Tools mentioned
Claude Code, Beads, Gas Town, Snyk (called Sneak in captions), Chainguard

## Relevance to our work
- **agentos** (2/3): AgentOS L1 already has a PII and prompt-injection scanner and L2C has exec-gate guardrails. The talk's point that security should run at generation time and as a separate pass maps to that design, and the slopsquatting risk applies to any agent-installed dependency. → *Add a check to the exec-gate or the agent tool layer that confirms any package an agent proposes to install exists and matches the expected publisher before installing, and test it against a deliberately hallucinated package name.*
- **prosharness** (2/3): ProsHarness runs plan, critique (Codex), and debate stages. The talk's advice to split security and correctness into separate passes, and to repeat review passes, applies directly to the critique stage. → *Add a security-only critique pass as a separate stage after plan and before implementation (and again before merge), instead of folding security into the general critique prompt, then compare findings against the current single critique on one past run.*
- **general** (2/3): The talk gives a simple practice for any agent workflow: put a scanner as the last step in the prompt, and run security as its own pass. This is cheap to try in any coding-agent setup. → *Add a final security-scan step to one agent workflow (for example a Claude Code task prompt with a scanner command), and measure how many issues it finds on a sample of recent agent-written PRs.*

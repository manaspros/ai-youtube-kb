# We Vetted 2000 AI Skills Before They Reached Developers — Lucas Palma, Nubank

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `iKQ78wyJEXU` · [watch](https://youtu.be/iKQ78wyJEXU) · **date:** 2026-08-18 · **length:** 16:24 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Lucas Palma · **orgs:** Nubank
- **topics:** security-guardrails, skills-self-improvement, pr-code-review, governance-compliance · **tags:** agent skills, supply chain, internal marketplace, secrets leakage, overbroad permissions, CI gate, SARIF, human-in-the-loop, fintech, vulnerability management

> Nubank's product security team built SkillVector, a CI scanner that vets internal AI skills (hybrid regex plus LLM) before they reach an internal marketplace, and reports 2,000+ skills scanned.

## Summary
Lucas Palma (product security manager at Nubank) argues that AI skills, plugins, MCP servers and agent rules now form part of the software supply chain, even though they look like configuration. Skills can hard-code tokens, recommend destructive shell commands, or request overbroad permissions, and they spread through internal marketplaces. Nubank's answer is SkillVector, which runs locally for engineers, again in CI on the pull request, and again after upload. It combines deterministic regex checks with LLM review for context-dependent risks, and writes findings as SARIF and as PR comments so the engineer fixes issues in the same PR. Across 2,000+ scanned skills the team logged 1,500+ risks, most were remediated, and a few risky skills were blocked before marketplace distribution. The talk closes by saying the same gates should cover plugins, MCP servers, rules and hooks, and that AI-generated "confirmations" do not count as human-in-the-loop approval.

## Key ideas
- **AI skills are supply-chain dependencies, not just config** — Skills, plugins, MCP servers and agent rules bundle instructions that drive code generation, and they are shared between people, so they need the same vetting as libraries or containers. ([1:11](https://youtu.be/iKQ78wyJEXU?t=71))
- **Concrete skill risks: leaked tokens, dangerous shell, excess permissions** — Examples include a skill that tells the agent to hard-code a retrieved token (which then lands in logs), a skill that recommends destructive shell commands, and a skill configured with far more permissions than it needs. A typo can be dangerous depending on who runs the skill. ([3:41](https://youtu.be/iKQ78wyJEXU?t=221))
- **The internal marketplace is the enforcement boundary** — Skills are shared through an internal marketplace where plugins bundle skills. Nubank put a CI step on the pull request that opens when someone adds a skill, so nothing reaches the marketplace unscanned. ([5:07](https://youtu.be/iKQ78wyJEXU?t=307))
- **Hybrid scanning: deterministic checks first, LLM for context** — Regex-style checks catch known patterns cheaply. An LLM reviews what needs context, and the team says it pairs both because LLM verdicts vary with temperature. Scans run at local dev time, at PR time, and again after upload, so a stale local version cannot slip through. ([6:35](https://youtu.be/iKQ78wyJEXU?t=395))
- **Put findings where the engineer already works** — Findings go into the PR as comments and into a SARIF file. The SARIF feeds the security team's vulnerability-management tooling, and policy decides between allow, allow with remediation, and block by severity. ([8:02](https://youtu.be/iKQ78wyJEXU?t=482))
- **Lessons: weight findings by risk, cut weak signals, check the production context** — Not every comment in a skill carries the same risk. Weak, low-context signals created more noise than value. Some warnings are harmless when run locally but matter in production. Findings with no clear remediation guidance were also a problem. ([11:47](https://youtu.be/iKQ78wyJEXU?t=707))
- **An AI confirming an action is not a human in the loop** — Instructions like 'ask for confirmation' can be satisfied by the model asking itself. The team scans for real approval gates and hooks, so a human approval is actually enforced. ([12:44](https://youtu.be/iKQ78wyJEXU?t=764))
- **Extend the same gates to other marketplaces and artifact types** — The team plans to find other marketplaces and bring them under the scanner, and to add checks for plugins, MCP servers, rules and hooks. They also suggest audit logs and trusted gateways at the tool level, plus policy-based gates per marketplace. ([14:10](https://youtu.be/iKQ78wyJEXU?t=850))

## Techniques
- **Three-point skill scanning** — Run the same scanner locally during authoring, as a CI check on the PR, and again on the merged or uploaded artifact, so the engineer iterates until it is clean and the registry verifies the final version. *When:* Any shared agent artifact (skills, plugins, MCP configs) that gets distributed to other developers.
- **Hybrid deterministic plus LLM review** — Use regex or pattern rules for known-bad strings (tokens, destructive shell commands, file writes). Escalate only the ambiguous or context-heavy items to an LLM reviewer, and treat its verdict as one signal, not ground truth. *When:* When you need broad coverage but cannot rely on the LLM alone because its judgments vary between runs.
- **Findings as PR comments plus SARIF** — Post each finding as a PR comment naming the required change, and also emit SARIF so existing security tooling can track and report it. *When:* When the scanner feeds both developer workflow and a security or vulnerability-management program.
- **Historical back-scan** — Scan artifacts created before the gate existed and push new findings into the remediation backlog. *When:* When introducing a scanning gate into a registry that already holds unreviewed content.
- **Verify approval gates, not model confirmations** — Check that approval steps for dangerous tool calls are enforced by hooks or permission gates outside the model, rather than trusting an instruction for the model to ask. *When:* When agent workflows claim human-in-the-loop control over destructive actions.

## Numbers
- Scanned 2,000+ skills in the baseline set; the talk says there are more beyond that. ([9:29](https://youtu.be/iKQ78wyJEXU?t=569))
- Identified more than 1,500 total risks across those skills (one skill can carry several risks). ([9:29](https://youtu.be/iKQ78wyJEXU?t=569))
- About 1,000 of those risks were probably remediated right after they were found. ([9:29](https://youtu.be/iKQ78wyJEXU?t=569))
- A few high-risk skills were blocked before marketplace distribution. ([9:29](https://youtu.be/iKQ78wyJEXU?t=569))
- A historical scan of skills created before the tool existed found new risks, which were put into the vulnerability management program. ([10:53](https://youtu.be/iKQ78wyJEXU?t=653))

## Hot takes
- AI skills should be treated as supply-chain dependencies, not configuration.
- When an AI asks for confirmation of its own action, that is not human-in-the-loop, and approval gates need to be enforced outside the model.
- Protect the whole workflow, not only the generated code.

## Tools mentioned
SkillVector (spoken as 'SkillVetor' in the transcript), SARIF, Regex-based determinstic scanners, LLM reviewer, Internal skills marketplace

## Relevance to our work
- **agentos** (2/3): SkillForge aims to turn agent telemetry into governed, reusable skills, and this talk gives a concrete vetting gate for that path. → *Add a SkillVector-style gate to SkillForge: a regex pass plus an LLM review that emits SARIF and blocks promotion of a mined skill into the reusable pool until it passes.*
- **general** (2/3): Skills, plugins, MCP servers and hooks are now shared between developers, so their supply-chain risk applies to any team. → *Scan every shared skill, plugin, MCP config and hook for hard-coded secrets, destructive shell commands and overbroad permissions, both locally and in CI, before the artifact is distributed.*
- **prosharness** (1/3): ProsHarness has approval flows, and the talk's point that model self-confirmation is not human approval applies to them. → *Write a test that proves ProsHarness approval gates block a destructive action until a human approves it, and does not pass on the model's own confirmation.*

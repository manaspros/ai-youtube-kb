# Through the AI Fog: The Architectural Decision Agentic Security Depends On — Manoj Nair, Snyk

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `1EZdpEhwmNc` · [watch](https://youtu.be/1EZdpEhwmNc) · **date:** 2026-08-18 · **length:** 23:29 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Manoj Nair, Ezra · **orgs:** Snyk, AI Engineer
- **topics:** security-guardrails, coding-agents, mcp-and-tools, evals · **tags:** agent security, generator-validator separation, skills supply chain, MCP server risk, package health, breakability, deterministic checks, PII in agent-created databases, shadow agents, Snyk Evo, vendor pitch, security track

> Snyk's CTO argues agent security needs deterministic checks alongside LLMs, with customer data on attacks, toxic skills and MCP servers, plus a live coding-agent demo.

## Summary
Manoj Nair, Snyk's CTO, opens the security track at AI Engineer World's Fair with a central question: can the generator and the validator of agent output be the same system? He says no and backs this with what Snyk reports from thousands of enterprise customers. He covers three problems: automated attacks that chain low-severity bugs, untrusted agent inputs (skills, MCP servers) and outputs (insecure code, agents copying PII), and agents being used without anyone knowing they exist. He cites a benchmark where frontier LLMs find the same vulnerability in only about half of five repeated runs and lag a deterministic check on recall. Snyk's answer is to put security context inside the agent loop, gate packages and remediation with health and breakability data, and govern agent components found in repos. A live demo (partly recorded after Wi-Fi failed) shows Claude Code checking package health and a skill's risk findings. Much of the talk is a product pitch for Snyk Studio and Evo, so the numbers are vendor-reported and mostly unverifiable on stage.

## Key ideas
- **Generator and validator should not be the same system** — The speaker frames the track's core question as whether the model that writes code can also judge it. His data says no, and he argues for separate checks that do not rely on the same probabilistic model. ([2:59](https://youtu.be/1EZdpEhwmNc?t=179))
- **Attackers can automate exploits without frontier models** — With good context and a harness, an attacker can run continuously. Chaining several low-severity bugs can produce an exploit, so 'fix criticals and highs and move on' no longer holds. ([4:23](https://youtu.be/1EZdpEhwmNc?t=263))
- **Agent inputs are a supply-chain risk: skills and MCP servers** — Skills and MCP servers can be poisoned or carry malware. The speaker says more than a third of skills he examined had malware or vulnerabilities. Customers who shut all MCP servers after an exploit then had to find a safe way to re-enable them. ([8:19](https://youtu.be/1EZdpEhwmNc?t=499))
- **Agents create unmanaged copies of sensitive data** — Agents have copied PII into new databases 'just in case' they need it later. Each copy becomes an unknown attack surface outside enterprise coverage, so gates and steering are needed. ([9:47](https://youtu.be/1EZdpEhwmNc?t=587))
- **You cannot govern agent components you have not found** — Snyk's scans of customer repos report about three agentic components for every model found. The speaker's point is that inventory has to come first, and that risk sits at more than one layer. ([9:47](https://youtu.be/1EZdpEhwmNc?t=587))
- **Probabilistic detection has measured recall gaps** — On a repeated detection task, the latest models found the same vulnerability in only about 50% of five runs. Across the issue set they found about 75%, against a deterministic check. He concludes that LLMs should be used for what they are good at, combined with deterministic checks, and not alone. ([12:24](https://youtu.be/1EZdpEhwmNc?t=744))
- **Prevention and remediation depend on health and breakability data** — Snyk gates agent package choices on maintenance status, CVEs and malware, and it pairs remediation with breakability data so that upgrades known to be safe are applied automatically. He reports one large customer fixed 16,000 critical issues in a week this way. ([13:51](https://youtu.be/1EZdpEhwmNc?t=831))
- **Make checks deterministic with a skill or hook** — In the demo, the speaker says that even when the agent is asked verbosely to run a health check, a skill or hook is the way to make the check run every time. The demo shows the agent picking packages using health data, and the skill review flags an auth header being echoed and instructions pulled from a remote YAML file. ([15:17](https://youtu.be/1EZdpEhwmNc?t=917))

## Techniques
- **Hybrid LLM plus deterministic security checks** — Use the LLM to discover candidate issues and a deterministic scanner to confirm or gate them. Do not rely on the LLM alone for recall. *When:* Security review or vulnerability detection where missed findings are costly and results must repeat across runs.
- **Repeated-run recall measurement** — Run the same detection task several times (the speaker uses five) and record the share of known issues found each time. Compare against a deterministic baseline and report F1 as well. *When:* Choosing a model for a review or scanning step, or checking whether a probabilistic reviewer is stable enough.
- **Pre-install package health gate** — Before an agent adds a dependency, check maintenance activity, known CVEs and malware status. Block or flag packages that are unmaintained or vulnerable. *When:* Coding agents that pick open-source packages on their own.
- **Skill and MCP risk assessment before adoption** — Scan a third-party skill's files for auth-header echoing, live fetches from social or web sources, and runtime pulls of remote instructions. Treat remote logic that can change without the skill file changing as a risk. *When:* Before installing or sharing a skill or MCP server, and again when its remote dependencies change.
- **Per-model red-team suite** — Keep a fixed attack set (PII extraction, decision override) and rerun it whenever a new model or component appears. Record results per model. *When:* Model selection or upgrades, so you know which model fits which task and where controls are needed.
- **Breakability-aware automated remediation** — Apply automated dependency fixes only when data on the upgrade's breakage risk says the change is safe. *When:* Large backlogs where fixing everything by hand is not realistic.
- **Deterministic invocation through a skill or hook** — Put the security check into a skill or hook so it runs on every relevant action, rather than relying on a prompt to ask for it. *When:* Any agent workflow where a check must always run, such as dependency selection.

## Numbers
- About 5,000 enterprise customers secured by Snyk ([1:35](https://youtu.be/1EZdpEhwmNc?t=95))
- 3,000 attendees at the previous year's World's Fair (speaker's account) ([1:35](https://youtu.be/1EZdpEhwmNc?t=95))
- Snyk reports 4,800+ customers, with backlog up 108% quarter over quarter ([6:57](https://youtu.be/1EZdpEhwmNc?t=417))
- A cited figure says 1,000 enterprises spent over $1M on a Claude Code rollout (quoted to set up the argument, not verified) ([5:39](https://youtu.be/1EZdpEhwmNc?t=339))
- More than a third of examined skills contain malware or vulnerabilities (speaker's cited research) ([8:19](https://youtu.be/1EZdpEhwmNc?t=499))
- Data from 3,000+ customers: about 3 agentic components found for every model in a repo ([9:47](https://youtu.be/1EZdpEhwmNc?t=587))
- On one hot new model, Snyk's attacks extracted PII 100% of the time; the open model was overridden 0% of the time on the decision-override test ([11:01](https://youtu.be/1EZdpEhwmNc?t=661))
- Latest models find the same vulnerability in only 50% of five runs ([12:24](https://youtu.be/1EZdpEhwmNc?t=744))
- Latest models find 75% of issues versus a deterministic check, with an F1 score of 40% ([12:24](https://youtu.be/1EZdpEhwmNc?t=744))
- A Mag 7 company remediated 16,000 critical issues with a remediation agent in one week ([13:51](https://youtu.be/1EZdpEhwmNc?t=831))

## Hot takes
- The generator and the validator should not be the same system; the speaker says 'why not' is the wrong default question.
- Probabilistic systems will not solve security on their own; deterministic checks still find things LLMs miss.
- Static AI governance (Confluence pages, PDFs) cannot keep up with agents building in fast-moving repos; policy has to be enforced in the loop.
- Fixing only criticals and highs is no longer a defensible risk strategy because low-severity bugs can be chained.
- Every AI model added to a repo brings more agentic components with it, so inventory has to come first.

## Tools mentioned
Claude Code, Cursor Cloud, Codex, Snyk Studio, Snyk Evo, Snyk package health check

## Relevance to our work
- **agentos** (2/3): AgentOS already has a PII/prompt-injection scan in L1 and exec-gate guardrails in L2C. The talk's skill-risk checks (auth-header echoing, runtime fetches of remote instructions) and its deterministic-plus-LLM split would extend SkillForge's governance of skills. → *Add a risk-scan step to SkillForge that flags skills which echo credentials, fetch live or remote instructions at runtime, or depend on unmaintained packages, and measure its recall against a deterministic baseline across 5 repeated runs.*
- **prosharness** (2/3): ProsHarness wraps Claude Code, and the talk's advice is to make checks deterministic with a skill or hook. The skill-ranking feature could also rank skills by risk. → *Add a hook in ProsHarness that scans newly added skills and MCP configs for remote-instruction fetches and credential echoing before a run is allowed to use them.*

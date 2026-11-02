# Bringing agents onto the world wide web — Paul Klein IV, Browserbase

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `GqoNrUz8hEU` · [watch](https://youtu.be/GqoNrUz8hEU) · **date:** 2026-08-18 · **length:** 18:26 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Paul Klein IV · **orgs:** Browserbase, Factory, Cursor, WorkOS, Google Chrome
- **topics:** voice-multimodal, agent-architecture, security-guardrails, mcp-and-tools · **tags:** browser-agents, computer-use, harness-engineering, webmcp, agent-auth, agent-identity, web-bot-auth, skills, observability, infrastructure-consistency, token-efficiency, auto-browse, browse-sh

> Paul Klein (Browserbase) argues reliable browser agents are a harness, tooling and infrastructure problem rather than a model problem, and lays out a multimodal, harness-engineered, consistently hosted approach.

## Summary
Klein says computer-use and browser agents lag behind coding agents even though models have improved, and he argues the gap is a "capabilities overhang" that engineering can close. He defines a harness as the scaffolding around a model (tools, memory, skills, sub-agents) and cites a same-model comparison where a domain-tuned harness beat a generic one. He says working browser agents are multimodal: they mix a vision model with code that replays network calls, so repeatable tasks become scripts. He covers harness tactics such as per-site skills, token-compact page representations and consistent infrastructure. He then argues the web itself needs to become agent-first through accessibility trees, WebMCP, agent-facing docs, agent sign-up and login flows, and some form of agent identity or trust. The talk closes with observability (recordings, logs, network traces) fed back into self-improvement, followed by a product pitch for Browserbase's new packaged agent harness.

## Key ideas
- **Browser agents are held back by the harness and tools, not the models** — He says models are now good at long-horizon and interface tasks, pointing to RL environments for computer use. He calls the remaining gap a capabilities overhang that engineering work (harness, tools, infra) should close. ([1:25](https://youtu.be/GqoNrUz8hEU?t=85))
- **A harness tuned to the domain can beat the same model in a generic setup** — He cites a comparison where Factory's custom harness outperformed Claude Code on the same model. He says the harness should be measured against a baseline model, and that building one is an engineering task a non-lab team can do. ([3:52](https://youtu.be/GqoNrUz8hEU?t=232))
- **Reliable browser agents combine a vision model with generated code** — Sometimes the agent should intercept network requests and write a script that replays them. Other times a stronger model handles a complex page and a cheaper one handles a simple page. Routing across models is part of the design. ([6:28](https://youtu.be/GqoNrUz8hEU?t=388))
- **Per-site skills and memory make repeat tasks cheaper** — Browse.sh publishes skills for websites, so an agent can learn what a site supports before visiting it. Dumping the full page into the model gives worse results and costs more, so the harness should present a compressed, optimised set of tokens. ([7:41](https://youtu.be/GqoNrUz8hEU?t=461))
- **Infrastructure consistency is a base layer** — Repeated runs should see the same layout, viewport and inputs. A page that renders mobile one time and desktop the next gives inconsistent results. Ad-hoc setups such as a home Mac mini cannot scale to thousands of agents or meet SOC 2. ([9:03](https://youtu.be/GqoNrUz8hEU?t=543))
- **The web needs to become agent-first** — He points to accessibility trees and ARIA labels as better inputs than raw DOM, and to WebMCP as a way for sites to expose approved tool calls. He also mentions llms.txt, agents.md and skills.md as sites publishing agent-facing files. ([10:18](https://youtu.be/GqoNrUz8hEU?t=618))
- **Authentication and trust are the next gate** — Sharing passwords or service accounts is risky. He suggests human-in-the-loop approval for sensitive actions and agent-first sign-up flows (WorkOS AuthMD). He describes web bot auth as a way for agents to identify themselves, and calls for a trusted certificate issuer for agents, a 'VeriSign moment'. ([11:22](https://youtu.be/GqoNrUz8hEU?t=682))
- **Observability has to feed self-improvement** — Each run should yield screen recordings, logs and network activity. That data loops back into the agent so it gets better every iteration. Browserbase's auto-browse does this across multiple loops. ([13:58](https://youtu.be/GqoNrUz8hEU?t=838))

## Techniques
- **Hybrid code-plus-browser execution** — Use the browser to observe the page and capture network requests, then have the agent write and replay a script for those calls. Keep the vision model for pages that need it. *When:* Repeatable web tasks in production, where a script is cheaper and more deterministic than click-by-click control.
- **Per-site skill packs loaded before visiting** — Publish a skill describing a site's tasks and selectors. The agent reads it before navigating and updates it through memory after successful runs. *When:* Agents that revisit the same websites often.
- **Compressed page representation** — Pass accessibility-tree and ARIA subsections, not the full DOM or HTML, and include only the tokens needed for the next step. *When:* Large or noisy pages where full-page context wastes tokens and lowers accuracy.
- **Pinned, consistent browser environment** — Fix viewport, layout, locale and infrastructure across runs so each run sees the same inputs. Run on managed infrastructure rather than ad-hoc devices. *When:* Any agent that runs the same flow many times or at scale.
- **Sites expose WebMCP tool calls and agent-first auth** — Let the website publish tool calls (for example, submit registration) through WebMCP. Offer agent-specific sign-up and login, with human approval for sensitive actions. *When:* Designing a site or service that agents will use, rather than only scraping it.
- **Observability-to-self-improvement loop** — Store screen recordings, logs and network traces for each run, then feed them back to refine the agent's skills or harness over repeated loops. *When:* Production browser agents where failures need diagnosing and success should compound over time.

## Numbers
- Vendor claim: Browserbase sees millions of sessions per month, which it uses to tune edge-case handling (no figures given beyond that) ([16:27](https://youtu.be/GqoNrUz8hEU?t=987))
- Browserbase runs browser agents for thousands of customer agents in production (stated as a goal of the infrastructure, not a measured number) ([9:03](https://youtu.be/GqoNrUz8hEU?t=543))
- Factory's custom harness outperformed Claude Code on the same model. A chart was shown but the numbers were not spoken. ([3:52](https://youtu.be/GqoNrUz8hEU?t=232))
- Speaker cites Karpathy's harness framing tweet from November 2023 as an early prediction of the current design ([3:52](https://youtu.be/GqoNrUz8hEU?t=232))

## Hot takes
- Browser agent failures are an engineering and harness problem, not a model problem.
- Teams should not wait for models to catch up; a company can build a good harness for its own domain.
- Software now has to plan for agent users, with agent-first sign-up and login flows, whether or not the owner wants them.
- A Mac mini setup cannot be made SOC 2 compliant at scale, so it is not a serious production answer for browser agents.
- Agent trust needs a certificate-issuer model, similar to the TLS certificate authorities, and nobody has built it yet.

## Tools mentioned
Browserbase, Browse.sh, WebMCP, Playwright CLI, Claude Code, Operator, Cursor, Factory, OpenClaw, WorkOS AuthMD, web bot auth, auto-browse, llms.txt, agents.md, skills.md, Chrome

## Relevance to our work
- **agentos** (2/3): Speaker says a harness should bring skills and memory for repeat tasks, and that browser agents solve repeat tasks by writing code. AgentOS SkillForge mines telemetry into reusable skills, so a repeated web task is a candidate for that pipeline. → *In SkillForge's open question on skill-worthiness, count a task as a candidate when an agent falls back to writing a replay script for a repeat web task. Log the signal in telemetry first.*
- **prosharness** (2/3): Speaker's core claim is that a harness (tools, memory, skills, compact context) improves a model, and that it should be measured against the bare model. ProsHarness wraps Claude Code in exactly that kind of harness. → *Run one repeated Claude Code task with and without ProsHarness and compare success rate and token use against the baseline, as the speaker advises.*
- **agentos** (1/3): Speaker names web bot auth (signed agent identity) and asks for a trust issuer for agents. The Govrix L1 proxy is the natural place to sign or identify agent traffic. → *Read the web bot auth proposal and check whether Govrix could attach a signed agent identity to outbound agent requests.*
- **general** (1/3): Speaker says sites are starting to publish agent-facing files (llms.txt, agents.md, skills.md) and WebMCP tool manifests. A registry could index these as discovery sources for skills and MCP servers. → *Read a few sites' llms.txt and WebMCP manifests and check whether the registry's discovery step can ingest them as a source.*

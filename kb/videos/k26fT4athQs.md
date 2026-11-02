# OmniRoute + Claude Code is INSANE (Why I Cancelled My Claude Code Subscription)

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `k26fT4athQs` · [watch](https://youtu.be/k26fT4athQs) · **date:** 2026-08-02 · **length:** 7:13 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed host (Kai Explains channel; not named in the transcript) · **orgs:** Anthropic, OmniRoute (open-source project, spelled OmniRoot in captions)
- **topics:** token-cost-efficiency, infra-cost-scaling, coding-agents · **tags:** OmniRoute, Claude Code, LLM gateway, provider fallback, free tiers, token compression, RTK, Caveman, semantic cache, model routing, usage limits, local gateway, MCP

> A host explains dropping a Claude Code subscription for OmniRoute, a self-run gateway that routes Claude Code to many providers with fallback, token compression and free tiers, and says when to keep a paid Opus key.

## Summary
The speaker says they cancelled their Claude Code subscription and now run Claude Code through OmniRoute, a self-hosted OpenAI-compatible gateway on localhost that sits in front of 200+ providers. The core argument is that the constraint is the usage meter (a rolling five-hour window plus a weekly cap), not Claude Code itself, and that routing around it with free tiers and automatic mid-request fallback removes the ceiling. The gateway also claims a two-pass tool-output compression (RTK and Caveman) that removes 78-95% of tokens on tool-heavy traffic while leaving code, URLs and JSON intact, plus a semantic cache and 18 routing strategies. Setup is described only at a high level: the gateway generates a Claude Code config file listing reachable models, and Claude Code is pointed at the local endpoint. The speaker is candid about limits (slower free models, tighter rate limits, quality variance, more assembly required) and keeps a paid Anthropic key for hard, model-sensitive tasks. The video is a pitch with no commands, config keys or measurements shown, so the architecture ideas are more useful than the claimed savings.

## Key ideas
- **The real limit is the subscription meter, not the agent CLI** — Pro is $20/month, Max $100-200, with a rolling five-hour usage window and a weekly cap on top. The speaker wants the same Claude Code loop with their own keys and routing and no timer. ([0:00](https://youtu.be/k26fT4athQs?t=0))
- **Point the agent at one local OpenAI-compatible endpoint and let the gateway choose the provider** — OmniRoute runs on localhost and exposes all configured providers as one model list. Claude Code only sees that host, and the gateway decides which provider serves each request. ([1:25](https://youtu.be/k26fT4athQs?t=85))
- **Fallback is done mid-request, not by retrying later** — If a provider is down, rate limited or slow, the gateway reroutes the same request to a healthy provider without the user noticing. The speaker presents this as the main feature. ([1:25](https://youtu.be/k26fT4athQs?t=85))
- **Compress tool-result payloads before they reach the model** — Two passes (RTK, then Caveman) strip 78-95% of tokens on repetitive tool chatter. Code, URLs and structured JSON pass through byte for byte, and the stated design goal is that source code is never altered. ([2:47](https://youtu.be/k26fT4athQs?t=167))
- **Run the routing layer on your own hardware to keep keys local** — Provider keys stay on the machine and the gateway makes no outbound calls to a third party. The speaker presents this as avoiding a middleman that sees all traffic. ([2:47](https://youtu.be/k26fT4athQs?t=167))
- **Set one routing policy and forget it** — The gateway offers 18 routing strategies (cheapest, fastest, weighted split, hard cost cap and others) plus a semantic cache that answers repeated questions without calling a model. ([2:47](https://youtu.be/k26fT4athQs?t=167))
- **Generate the Claude Code config from the gateway's live model list** — A button in the gateway produces a Claude Code config file that already lists every reachable model. The file is dropped in place and Claude Code is pointed at localhost. ([4:09](https://youtu.be/k26fT4athQs?t=249))
- **Route per task: free pool by default, paid frontier model for hard problems** — The speaker keeps a paid Anthropic key for tasks where Opus clearly leads and uses the free pool for most work. The verdict is 'keep the loop, choose the brain per task', not that Claude Code lost. ([6:41](https://youtu.be/k26fT4athQs?t=401))
- **Honest costs of the free pool** — Free tiers mean slower models, tighter rate limits and quality that depends on which provider answers. Fallback reduces these problems but does not remove them. The user also takes on key management and extra configuration. ([5:29](https://youtu.be/k26fT4athQs?t=329))

## Techniques
- **Local OpenAI-compatible gateway in front of a coding agent** — Run the gateway on localhost. Point the agent CLI's base URL at it (the speaker describes this via a generated config file, without exact keys). Keep provider keys on the gateway, not in the agent. The agent keeps its normal interface while the gateway picks the backend. *When:* You want model choice across many providers, or your own keys and routing, without changing the agent's UI or workflow.
- **Mid-request provider fallback** — When a provider returns a rate limit or error, or is slow, the gateway resends the same request to another healthy provider and returns the result to the agent. No manual retry. *When:* Long agent sessions that would otherwise stall on one provider's rate limit or outage.
- **Tool-output compression before the model call** — Apply lossy compression only to repetitive tool-result payloads (shell output, tool chatter). Pass code, URLs and structured JSON through unchanged. The speaker names RTK and Caveman as the two passes, without showing config. *When:* Tool-heavy agent loops where tool output dominates the token count and source text must stay exact.
- **Per-task model routing with a paid escape hatch** — Set a default routing policy (cheapest, fastest, weighted split or hard cost cap) on the gateway. For tasks that need a frontier model, point the agent at the paid key for that task only. *When:* Mixed workloads where most tasks are routine and a few are model-sensitive.
- **Semantic cache for repeated questions** — The gateway stores answers to previously computed requests and returns a cached answer for a similar repeat without a model call. The speaker does not show the similarity threshold or cache invalidation. *When:* Repeated or near-duplicate questions in an agent or chat workload.

## Numbers
- Pro plan is $20/month; Max is $100-200/month ([0:00](https://youtu.be/k26fT4athQs?t=0))
- Usage window is rolling five hours, with a weekly cap on top; Anthropic doubled these limits in May (per the speaker) ([0:00](https://youtu.be/k26fT4athQs?t=0))
- Gateway fronts over 200 providers (later stated as 230+); more than 50 have a free tier; 11 are free permanently with no card ([0:00](https://youtu.be/k26fT4athQs?t=0))
- Gateway fronts 230+ providers; more than 50 with a free tier; 11 permanently free ([1:25](https://youtu.be/k26fT4athQs?t=85))
- Token compression removes 78-95% of tokens on tool-heavy traffic (speaker's claim, no benchmark shown) ([2:47](https://youtu.be/k26fT4athQs?t=167))
- About 94 built-in MCP tools and 18 routing strategies ([2:47](https://youtu.be/k26fT4athQs?t=167))
- Free-tier pool documents about 1.5 billion tokens per month (speaker's claim) ([4:09](https://youtu.be/k26fT4athQs?t=249))

## Hot takes
- Title oversells: 'INSANE' and 'cancelled my subscription' frame a pitch, and the promised start-to-finish build is not shown with commands, config keys or file names.
- The 78-95% compression and 1.5B tokens/month figures are unsourced and unbenchmarked. The compression claim applies only to tool-heavy traffic per the speaker.
- The speaker's own verdict is measured: keep a paid frontier key for hard, model-sensitive work, and route routine work to free tiers. Not a takedown of Claude Code.
- Free-tier reliability is a real tradeoff (slower models, rate limits, variable quality). Fallback softens this but does not remove it.
- The gateway name is inconsistent in the captions (OmniRoot vs OmniRoute). The speaker's framing suggests they are the same project.

## Tools mentioned
OmniRoute (also captioned as OmniRoot; self-hosted LLM gateway, version not stated), Claude Code (agent CLI), Anthropic Claude Opus (paid model for hard tasks), RTK (token-compression pass), Caveman (token-compression pass), MCP (gateway ships about 94 built-in tools over Model Context Protocol)

## Relevance to our work
- **agentos** (2/3): AgentOS L1 (Govrix Scout) already plans budgets and strategy routing in front of providers. OmniRoute covers similar ground: multi-provider routing, mid-request fallback, cost caps, a semantic cache and tool-output compression. → *Compare OmniRoute's 18 routing strategies and mid-request fallback against Govrix Scout's strategy routing. Check whether the semantic cache and tool-output compression are worth adding to the L1 proxy roadmap.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI. Pointing that CLI at a local gateway could cut cost, but it could also interfere with checkpoint/resume and approval flows. The video does not cover harness behavior. → *Test whether the Claude Code CLI used by ProsHarness can be redirected to a local OpenAI-compatible base URL without breaking checkpoint/resume or the approval flow.*

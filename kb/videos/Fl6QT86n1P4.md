# Why Anthropic Banned Every Third-Party Claude Tool

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `Fl6QT86n1P4` · [watch](https://youtu.be/Fl6QT86n1P4) · **date:** 2026-06-02 · **length:** 6:10 · **format:** news · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Anthropic, OpenAI, Zed, SpaceX
- **topics:** token-cost-efficiency, claude-code, governance-compliance · **tags:** programmatic-credits, subscription-vs-api, agent-sdk, claude-p, third-party-harness-ban, vendor-lock-in, usage-limits, opt-in-billing

> Better Stack on Anthropic's Programmatic Credits (opt-in from June 15): subscription use of the Agent SDK and claude -p moves to API-rate credits, after earlier blocks on third-party harnesses. The speaker reads it as vendor lock-in.

## Summary
The video explains Anthropic's Programmatic Credits, which take effect June 15 and require opt-in. Each paid Claude subscriber gets a monthly credit equal to the plan price ($20 Pro, $100 Max 5x, $200 Max 20x), usable only for programmatic use: the Agent SDK, claude -p, and third-party apps built on the SDK. The credits bill at full API rates and expire without rolling over, so the speaker argues heavy programmatic users could run out within days. The backstory: subscriptions had covered Agent SDK and claude -p use that powered tools such as Sandcastle, T3 Code and Zed's built-in Claude agent. Anthropic then blocked subscription tokens outside official apps on January 9, updated its terms in February, and enforced harder in April. The speaker weighs three explanations (compute efficiency, telemetry, competitive positioning), finds the first two weak, and leans toward competitive positioning. He contrasts this with OpenAI letting Codex subscriptions run in third-party tools, and says he personally moved from OpenCode to Claude Code and Claude routines, though he still finds the subscription cheaper and prefers Opus.

## Key ideas
- **Programmatic Credits: a monthly API-rate credit equal to the subscription price, usable only for Agent SDK, claude -p and third-party SDK apps** — Opt-in, starting June 15. Credits do not roll over. Once they run out, the user either stops or enables extra usage, which is also billed at full API rates. ([0:00](https://youtu.be/Fl6QT86n1P4?t=0))
- **Subscriptions originally covered Agent SDK and claude -p use, which let third-party tools be built on top of a plan** — The speaker cites Sandcastle (Matt Pocock), T3 Code (Theo) and Zed's built-in Claude agent as examples of tools that ran on subscriptions. ([0:00](https://youtu.be/Fl6QT86n1P4?t=0))
- **Anthropic restricted subscription use outside official apps in stages** — A silent block on January 9 broke workflows, February brought a terms-of-service ban on third-party harnesses, and April brought enforcement against tools such as OpenCode. The speaker also reports that the Claude Code system prompt was changed to scan git status for keywords like OpenClaw and Hermes, which could flag accounts. The speaker reports this without a source. ([1:07](https://youtu.be/Fl6QT86n1P4?t=67))
- **The speaker's three theories for the restriction: compute efficiency, telemetry, and competitive positioning** — Anthropic said third-party tools did not use prompt caching well. The speaker counters that a large GPU deal (over 220,000 GPUs, signed May 6) should have solved compute, and that telemetry could have been required instead of a ban. Competitive positioning is the speaker's favored theory, since the restrictions push users to official tools. ([1:07](https://youtu.be/Fl6QT86n1P4?t=67))
- **Credits are priced at full API rates, so their size is small in practice** — The speaker's rough numbers: the Pro plan gives about 45 messages every five hours, yet $20 of Opus 4.7 credits could be gone in about two days. The Max 20x plan's $200 might last about a week. ([3:25](https://youtu.be/Fl6QT86n1P4?t=205))
- **The speaker reads the change as vendor lock-in, with Anthropic building remote control, managed agents and routines** — The speaker sees the credit system as steering users toward first-party features and away from other tools. ([3:25](https://youtu.be/Fl6QT86n1P4?t=205))
- **OpenAI is taking the opposite approach and allows Codex in subscriptions with third-party tools** — The speaker notes OpenAI's support for OpenClaw and its offer of two free months of Codex to enterprise customers who switch from Claude. ([4:47](https://youtu.be/Fl6QT86n1P4?t=287))
- **The speaker moved to first-party tools and still finds the subscription worth it** — He switched from OpenCode to Claude Code and from NanoClaw to Claude routines with official connectors, gives up custom scripts, and says Opus is still his preferred model. He says the gap with other models is closing quickly. ([4:47](https://youtu.be/Fl6QT86n1P4?t=287))

## Techniques
- **Move recurring automation to first-party surfaces such as routines and official connectors** — The speaker replaced a third-party agent runner (NanoClaw) with Claude routines and the official connectors that come with them, and moved from OpenCode to Claude Code. This keeps the work on subscription-covered official apps. The trade-off is less room for custom scripts and workflows. *When:* When a subscription-based workflow is at risk of being restricted, or when you want to avoid running programmatic usage that is billed at API rates.
- **Estimate programmatic spend at API rates before running a loop on a subscription** — Programmatic Credits and extra usage are billed at full API token rates, so estimate tokens per run times the model's API price, then compare that with the monthly credit (equal to the plan price). Credits expire monthly with no rollover. *When:* Before enabling Programmatic Credits (opt-in from June 15) or any Agent SDK or claude -p job that runs unattended.

## Numbers
- Programmatic Credits equal the monthly subscription price: $20 Pro, $100 Max 5x, $200 Max 20x ([2:13](https://youtu.be/Fl6QT86n1P4?t=133))
- Pro plan gives about 45 messages per five hours, but $20 of Opus 4.7 API credits could last about two days (speaker's estimate) ([3:25](https://youtu.be/Fl6QT86n1P4?t=205))
- Max 20x $200 of credits might last about a week of heavy programmatic use (speaker's estimate) ([3:25](https://youtu.be/Fl6QT86n1P4?t=205))
- Some developers' workloads ran 10x to 30x above API-rate equivalent cost on the $200 Max plan, per the speaker ([1:07](https://youtu.be/Fl6QT86n1P4?t=67))
- Anthropic's SpaceX deal covers over 220,000 GPUs, signed May 6 ([1:07](https://youtu.be/Fl6QT86n1P4?t=67))
- Subscription tokens were silently blocked outside official apps on January 9 ([1:07](https://youtu.be/Fl6QT86n1P4?t=67))
- Credits take effect June 15 and expire without rollover ([3:25](https://youtu.be/Fl6QT86n1P4?t=205))
- OpenAI is offering enterprise customers two free months of Codex to switch from Claude; OpenClaw has about 3 million users ([4:47](https://youtu.be/Fl6QT86n1P4?t=287))

## Hot takes
- The title, 'Why Anthropic Banned Every Third-Party Claude Tool', overstates the content. The video describes restrictions on subscription tokens used outside official apps, not a blanket ban on all third-party tools.
- The git-status keyword scanning and the account bans are reported without a source in the video.
- The three explanations for the restriction are speculation. The speaker admits there is no concrete reason from Anthropic, and the SpaceX GPU deal is a weak rebuttal to a caching-efficiency argument.
- The dollar-to-message conversions and the 'two days' and 'one week' figures are rough estimates, not measured usage.
- Vendor-lock-in framing and the comparison with AWS are opinion, not evidence.

## Tools mentioned
Claude Code, Claude Agent SDK, claude -p (headless CLI mode), Claude routines, Remote control (Claude feature), Managed agents (Claude feature), Opus 4.7, Sandcastle, T3 Code, Zed, OpenCode, OpenClaw, NanoClaw, Hermes, Conductor, Codex

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI. If it drives Claude through claude -p or the Agent SDK, the June 15 opt-in credit pool (API-rate, no rollover) changes its cost model and may restrict how it runs. → *Check how ProsHarness invokes Claude Code (interactive vs claude -p or Agent SDK) and cost each job against the programmatic credit pool before the June 15 opt-in.*
- **agentos** (1/3): AgentOS routes agent traffic through a budget-enforcing proxy. Subscription-covered and API-rate usage are now separate pools, which is a budgeting distinction the proxy may need to model. → *If AgentOS fronts Claude-backed agents, consider whether Scout budgets should track subscription-covered and API-rate usage separately.*

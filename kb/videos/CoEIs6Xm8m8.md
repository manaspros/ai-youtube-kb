# Open Source Is Dead. Long Live Open Source. — Saoud Rizwan, Cline

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `CoEIs6Xm8m8` · [watch](https://youtu.be/CoEIs6Xm8m8) · **date:** 2026-08-18 · **length:** 17:30 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Saoud Rizwan · **orgs:** Cline, Zig, Bun, curl, tldraw, GitHub, LiteLLM, Cursor, Uber, Coinbase, Anthropic, OpenAI, Semianalysis, Facebook, Amazon, Google, AWS, Fireworks, Baseten
- **topics:** token-cost-efficiency, infra-cost-scaling, models-research, security-guardrails · **tags:** open-weights, cost, token-spend, supply-chain, open-source, GLM, Kimi, DeepSeek, Cline, verification, lock-in, internal-gateway, commoditization

> Cline's founder argues open-weight models plus verification-heavy agent harnesses will win on cost as closed labs subsidize subscriptions for lock-in, citing a supply-chain attack and spend data.

## Summary
Saoud Rizwan, founder of Cline, argues that open source is being damaged by AI-generated PRs, bug reports and supply-chain attacks, but that open-weight models will still win on cost. He cites projects closing or banning AI contributions, the LiteLLM package compromise, and reports of very high enterprise token spend. He claims labs subsidize subscriptions to create lock-in, and that a well-built harness with skills, rules and verification can make a cheaper model good enough. His one real-world comparison pits GLM against Opus on a single client bug: GLM used about twice the tokens at half the cost and verified its build, while Opus finished faster but left type errors and broke the production build. He closes by urging US labs to release more open weights and announces Cline's own open-weights subscription plan.

## Key ideas
- **Open source community is degrading under AI** — AI-made PRs, issues and security reports have flooded GitHub. Zig bans AI use in contributions, curl is considering ending its bug bounty, tldraw closes all PRs, and GitHub added a setting to disable third-party PRs. ([1:18](https://youtu.be/CoEIs6Xm8m8?t=78))
- **Supply-chain risk of third-party packages is rising** — LiteLLM (about 3.5M downloads a day) was compromised for about three hours. Attackers used a GitHub app to steal PyPI publish tokens and shipped a credential harvester plus a backdoor. It was caught only because the malware crashed Cursor, which a researcher noticed. ([3:57](https://youtu.be/CoEIs6Xm8m8?t=237))
- **Enterprise token spend is out of control** — One unnamed company reportedly spent $500M in a month because usage limits were not set on thousands of employee seats. Uber reportedly had 95% of engineers on Claude and used its 2026 budget in four months. ([6:18](https://youtu.be/CoEIs6Xm8m8?t=378))
- **Labs may be subsidizing subscriptions to create lock-in** — A Semianalysis experiment found a $200 Claude plan gave about $8,000 of API-equivalent usage, and a $200 Codex plan about $14,000. The speaker reads this as a strategy: subsidize, build dependence through CI and background agents, then raise prices. ([7:22](https://youtu.be/CoEIs6Xm8m8?t=442))
- **Harness and verification matter more than raw model intelligence** — With project skills, rules, verification and quality gates, a mediocre model can reach similar results to a stronger one, though it may use more tokens. The speaker says intelligence should sit in the system around the model, not depend on each developer using it well. ([8:12](https://youtu.be/CoEIs6Xm8m8?t=492))
- **Cheaper open-weight model won a real bug comparison on cost and quality** — On a real client bug, GLM used about twice the tokens at half the cost and checked that the build compiled. Opus was faster with half the tool calls but left type errors and broke the production build. The speaker believes GLM was trained to spend tokens on verification. ([9:31](https://youtu.be/CoEIs6Xm8m8?t=571))
- **Companies are routing to cheaper open-weight models through internal gateways** — The speaker cites Coinbase's CEO saying GLM and Kimi are the defaults in its internal LLM gateway, cutting AI spend by nearly half while token usage keeps growing. ([9:31](https://youtu.be/CoEIs6Xm8m8?t=571))
- **Open-weight and commodity analogies (Open Compute, cloud price cuts)** — Facebook open-sourced its data-center designs and the supply chain standardized around them, which lowered costs for everyone. The speaker expects the same for inference, citing 2014 GCP and AWS compute price cuts and a projected 90% fall in inference cost for a 1T-parameter model by 2030. These are estimates from the talk. ([10:42](https://youtu.be/CoEIs6Xm8m8?t=642))

## Techniques
- **Put quality in the harness, not the model** — Give the agent project skills, rules, a build or type-check step, and quality gates it must pass before it can say it is done. Accept more tokens in exchange for a cheaper model. *When:* When you run agents across many developers and cannot rely on each one to use the model well, or when you want to switch to a cheaper model.
- **Default route to cheaper open-weight models in an internal gateway** — Set open-weight models (GLM, Kimi) as the default model in an internal LLM gateway, and keep premium models for exceptions. Track spend and token use after the switch. *When:* When AI spend is large and growing and most work does not need the top model.
- **Head-to-head test on a real bug from your own repo** — Give two models the same real client bug and compare tokens, cost, tool calls, and whether the build and types pass afterwards. *When:* Before trusting a leaderboard or switching models for coding-agent work.
- **Set usage limits per user on the provider dashboard** — Cap spend per seat or per user from day one when rolling out an AI coding tool to many engineers. The speaker presents the $500M overspend as the failure this prevents. *When:* When giving a large org access to a metered API or coding-agent subscription.

## Numbers
- LiteLLM package gets about 3.5M downloads a day and was compromised for about 3 hours ([3:57](https://youtu.be/CoEIs6Xm8m8?t=237))
- One company reportedly spent about $500M on Claude in a single month without usage limits ([6:18](https://youtu.be/CoEIs6Xm8m8?t=378))
- Uber: 95% of engineers using Claude, 70% of committed code from Claude, up to $2,000 per user per month, 2026 budget used in four months ([6:18](https://youtu.be/CoEIs6Xm8m8?t=378))
- Semianalysis: $200 Claude plan gives about $8,000 of API-equivalent usage; $200 Codex plan about $14,000 ([6:18](https://youtu.be/CoEIs6Xm8m8?t=378))
- GLM vs Opus on one client bug: GLM used about 2x the tokens at about half the cost, with fewer tool calls from Opus but a broken production build ([9:31](https://youtu.be/CoEIs6Xm8m8?t=571))
- Coinbase reportedly cut AI spend by nearly half after defaulting to GLM and Kimi, while token use grew ([9:31](https://youtu.be/CoEIs6Xm8m8?t=571))
- Estimated about $3T and 100+ GW of new data center capacity by 2030, roughly doubling global capacity ([12:54](https://youtu.be/CoEIs6Xm8m8?t=774))
- Estimated 90% lower inference cost for a 1T-parameter LLM by 2030 (projection) ([12:54](https://youtu.be/CoEIs6Xm8m8?t=774))
- GCP in 2014 cut compute prices 32% and storage 68%; AWS matched within days, its 42nd price cut ([12:54](https://youtu.be/CoEIs6Xm8m8?t=774))

## Hot takes
- Open source as a community is dying, but open-weight models will still win on cost.
- Closed labs are subsidizing subscriptions to lock developers in, and the strategy will fail.
- Raw model intelligence matters less than context, tools and verification; a mediocre model with good guardrails can match a stronger one.
- US labs should release more open-weight models to keep their lead.

## Tools mentioned
Claude Code, Codex, Cursor, Cline, LiteLLM, GLM, Kimi, DeepSeek, Opus, Open Compute

## Relevance to our work
- **agentos** (2/3): AgentOS's L1 proxy already does budgets and strategy routing. The talk's cheaper-model routing and the LiteLLM compromise are relevant to both. → *Benchmark GLM or Kimi against a frontier model on 3-5 real repo bugs, tracking tokens, cost, tool calls and build or type-check pass rate, then use the results as a routing signal in the strategy router.*
- **prosharness** (2/3): ProsHarness checkpoints and reviews long agent runs. The talk's point that a cheap model is good enough when the harness requires a build or type-check before finishing applies directly. → *Add a mandatory build and type-check gate before ProsHarness marks a checkpoint or run complete, and test it on a cheap model against a real bug.*

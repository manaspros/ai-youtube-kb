# The AI Bill Is Too Damn High: Tokenomics 101 — Eugene Cheah, Featherless AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Ti-BmGU1_mQ` · [watch](https://youtu.be/Ti-BmGU1_mQ) · **date:** 2026-10-17 · **length:** 55:25 · **format:** workshop · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Eugene Cheah · **orgs:** Featherless AI, AT&T, Shopify, Cerebras, Linux Foundation
- **topics:** token-cost-efficiency, infra-cost-scaling, governance-compliance, models-research · **tags:** tokenomics, cost-control, API-key-per-team, model-routing, dedicated-capacity, tokens-per-second, SFT-distillation, classifiers, slop-grenade, outcomes-not-usage

> Eugene Cheah (Featherless AI) walks through "tokenomics" in four moves (measure, right-size, buy capacity, check processes) to cut inference spend, with per-key tracking, model labels per department, and a warning that tokens are not work done.

## Summary
Eugene Cheah of Featherless AI gives a workshop on reducing AI token bills at scale. His four steps are: measure spend by splitting API keys by department, team and use case; right-size models and speed tiers per workload (agentic long-context vs. high-volume process automation); buy capacity (dedicated instances for a known base load, bursting to public cloud for spikes); and check whether the processes actually produce outcomes. He argues for pairing a strong planner model with a cheap, fast implementer, using labels rather than model names for departments, and using classifiers for high-volume decisions. He says the cheapest path is to build evals first, then search for the smallest model that passes them, optionally fine-tuning with SFT on golden traces. He closes by warning that spamming agents creates duplicate or oversized work, and that organisations must own what AI generates and measure outcomes, not usage. This is a practitioner talk with some vendor framing (he sells inference), and many numbers come from his own customers and are approximate.

## Key ideas
- **Measure first: most organisations cannot see token spend by team or use case** — Speaker says 30-40% of customers begin with one shared API key. He recommends splitting keys by department and use case before any optimisation, because measurement gives the biggest return. ([2:44](https://youtu.be/Ti-BmGU1_mQ?t=164))
- **Two workload types with opposite economics** — Agentic and coding workloads are long-running, cache-heavy, input-heavy, and about 1% output. Process automation (call centres, email routing, moderation) is short-context, task-isolated, and a volume game. They need different optimisation. ([5:30](https://youtu.be/Ti-BmGU1_mQ?t=330))
- **Match speed to where a human is waiting** — Pay for high tokens-per-second only when a person is waiting. Background and CI jobs can run much slower and cheaper. Speed and cost do not scale linearly: he says roughly 2x speed costs about 3x, and batching many requests can cut cost about 9-10x. ([14:22](https://youtu.be/Ti-BmGU1_mQ?t=862))
- **Planner/implementer split with a cheap fast worker** — Use the strongest model for planning and review, and a cheaper, faster model for the token-heavy implementation loop. Teams rarely switch models on their own, so the incentive should be that the cheap model is simply faster. ([14:55](https://youtu.be/Ti-BmGU1_mQ?t=895))
- **Give departments labels, not model names** — Expose models as labels such as fast, smart, or finance-agent. This lets the organisation swap or A/B test models without asking users to change anything. He notes some teams were still running Llama 2 because nobody switched. ([18:47](https://youtu.be/Ti-BmGU1_mQ?t=1127))
- **Evals before model choice; try a small model against your own test cases** — Build test cases and evals, then search for the cheapest model that passes most of them. He cites a telco that cut inference from about 250k to 7.6k a month this way. He says 'is the small model good enough' is the wrong question; the eval results are what matter. ([21:36](https://youtu.be/Ti-BmGU1_mQ?t=1296))
- **Classifiers handle a large share of traffic cheaply, but turn-based routing hurts cache hit rates** — One-shot classifier models are commonly about 10x cheaper and cannot chat. He prefers task-based routing per department. Turn-based routing across many models breaks prompt caching, so he suggests at most two or three models. ([29:18](https://youtu.be/Ti-BmGU1_mQ?t=1758))
- **Tokens are not work done; check the process** — Spamming agents can produce duplicate work, oversized diffs that reviewers cannot read, and discarded output. He says the bottleneck moves to CI, review and trust, and the fix is human process: smaller changes, better tests, and modular merges. ([35:22](https://youtu.be/Ti-BmGU1_mQ?t=2122))
- **Own what you generate; measure outcomes, not usage** — He names 'slop grenades' (generated output handed to someone else to verify) and says people must own generated text and code. He suggests tokens x price divided by outcomes used as a rough metric, while admitting outcomes are hard to measure. ([42:31](https://youtu.be/Ti-BmGU1_mQ?t=2551))

## Techniques
- **Per-team and per-use-case API key split** — Issue separate keys per department, team, and workload so that spend can be attributed. Use this as the base for all later decisions. *When:* Before any cost optimisation, and whenever a single shared key is in use.
- **Speed tier per workload** — Route human-facing or interactive calls to high tokens-per-second deployments and send CI, cron, and background agents to slower, cheaper capacity. Set this at the key level. *When:* When the org has mixed interactive and background traffic.
- **Planner-worker model split** — A frontier model plans and reviews; a cheaper, faster model implements. He suggests Claude Code as planner and a cheaper harness such as Pi as implementer, invoked as a CLI batch command. *When:* Coding-agent workflows where implementation is token-heavy and repeated.
- **Eval-driven model downsizing** — Write test cases and evals from real examples, benchmark a set of open models, pick the cheapest that passes most cases, then fine-tune (SFT on a small golden-trace set, weighted heavily) if needed. Keep a shadow slice of traffic going to the best model to keep collecting data. *When:* High-volume, well-defined tasks such as classification, support, or extraction.
- **Department-level model labels** — Expose model roles as labels such as fast, smart, or finance-agent. Swap or split traffic behind the label without telling users. *When:* Multi-department rollouts where users should not need to know model names.
- **Dedicated capacity for base load, burst to public cloud** — Measure the base workload and reserve dedicated instances for it. Cap dedicated capacity and let spikes spill to a public API. *When:* Stable base load with predictable spikes.

## Numbers
- Largest customer serves about 2 trillion tokens a day on about 512 AMD MI-series GPUs. The stated per-million price is garbled in captions (one spot reads 0.3, another 0.03), so treat it as unverified. ([1:40](https://youtu.be/Ti-BmGU1_mQ?t=100))
- Five-dev team running about 8 agents continuously spent about $150k a month on Opus; switching to a cheaper model on a single node brought it under $10k a month, with no visible impact (speaker's account) ([17:41](https://youtu.be/Ti-BmGU1_mQ?t=1061))
- 30-40% of customers who reach out start with a single shared API key for the whole organisation ([3:53](https://youtu.be/Ti-BmGU1_mQ?t=233))
- Agentic workloads: about 1% of requests are output tokens; the rest is input, mostly cached ([13:50](https://youtu.be/Ti-BmGU1_mQ?t=830))
- Speed/cost trade-off: he says about 2x speed costs about 3x. One node does 112 tok/s for a single request; 16 parallel requests halve per-request speed but give about 10x total output, about 9-10x lower cost per token ([29:50](https://youtu.be/Ti-BmGU1_mQ?t=1790))
- Typical speed tiers: 20-30 tok/s for interactive chat, up to 60 for fast; 120 only in special cases ([30:56](https://youtu.be/Ti-BmGU1_mQ?t=1856))
- Telco: inference cost cut from about $250k to $7.6k a month by splitting traffic across smaller, fine-tuned models ([22:10](https://youtu.be/Ti-BmGU1_mQ?t=1330))
- A telco peaks at about 10 million messages in one minute for child-safety moderation ([19:57](https://youtu.be/Ti-BmGU1_mQ?t=1197))
- A classifier model is commonly about 10x cheaper than a general model, or faster ([12:42](https://youtu.be/Ti-BmGU1_mQ?t=762))
- Cited reports put AI productivity gains at only 6-7% against large token-spend increases (not verified by speaker) ([34:49](https://youtu.be/Ti-BmGU1_mQ?t=2089))
- Anecdote: a prompt-tuned Qwen 27B beat most fine-tuned 27B models on a 10,000-question benchmark (speaker's own account) ([46:56](https://youtu.be/Ti-BmGU1_mQ?t=2816))

## Hot takes
- Most organisations below about $10k a month should focus on finding strong use cases before optimising the token bill
- Fine-tuning is probably the wrong question; evals and prompting matter more
- Claude Code is an example of full lock-in; switching harnesses is the first step to flexibility
- Turn-based auto-routing across many models breaks caching; task-based routing per department is better
- Tokens are not work done

## Tools mentioned
Claude Code, Pi coding agent harness, simple-classifier (open source, speaker's project), tokenomics tracking tool (open-sourced by speaker's company)

## Relevance to our work
- **general** (3/3): The eval-first downsizing method and the planner-worker split directly apply to the recurring interest in cheap-model (Haiku) pipelines and entity resolution at scale. → *For the entity-resolution pipeline, write the eval set first, then benchmark the cheapest model that passes it, and check whether a cheap classifier stage can filter most pairs before an LLM call.*
- **agentos** (2/3): Per-key and per-department attribution maps onto AgentOS's budget pillar (L1 Govrix Scout). The dedicated-vs-burst idea and speed tiers apply to the InferCraft priority scheduler on one RTX 5090. → *Add per-key and per-use-case attribution to the Govrix budget counters, and add a speed or tier label to background-job priority classes in the InferCraft scheduler.*
- **prosharness** (2/3): The planner (Claude Code) plus cheaper implementer split matches ProsHarness's plan and critique flow, and it may cut the cost of long checkpointed runs. → *Try a Claude Code planner with a cheaper implementer for a few ProsHarness checkpoint runs, and log tokens per phase to compare cost and quality.*

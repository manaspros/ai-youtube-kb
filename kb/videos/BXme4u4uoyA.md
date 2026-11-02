# Stop Overpaying for LLMs... This Router Cut My Costs 70% (Manifest)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `BXme4u4uoyA` · [watch](https://youtu.be/BXme4u4uoyA) · **date:** 2026-06-02 · **length:** 6:58 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Better Stack host (unnamed) · **orgs:** Better Stack, Manifest, OpenRouter, LiteLLM, Ollama, OpenAI, Anthropic
- **topics:** token-cost-efficiency, infra-cost-scaling, mcp-and-tools · **tags:** llm-router, cost-reduction, model-routing, self-hosted, docker-compose, openai-compatible, observability, budgets, fallbacks, multi-agent, ollama, litellm, openrouter

> Better Stack walkthrough of Manifest, a self-hostable LLM router that scores each request across 23 dimensions and sends it to the cheapest capable model; the speaker claims up to 70% cost cuts with no agent code changes.

## Summary
Better Stack presents Manifest as a proxy that sits between an agent and its model providers. The agent keeps its OpenAI-style client and only changes the base URL to the Manifest endpoint, which runs in Docker Compose. Manifest scores each request deterministically (no LLM call) across 23 dimensions and routes it to the cheapest model that can handle it, with reported routing overhead under 2 ms. The demo shows a dashboard with per-agent cost, token usage and budgets, and the speaker says savings reached up to 70% on a same-task comparison. He positions Manifest against OpenRouter (hosted, prompts leave the machine) and LiteLLM (unified interface, manual routing). Caveats he raises: routing can be more aggressive than expected, setup still means managing keys and provider wiring, and SDK and storage support is limited. The video is a single-user demo with no published benchmark method, so the 70% figure is anecdotal.

## Key ideas
- **Most agent calls are simple (tool picking, classification, summaries), so sending them all to a frontier model inflates cost 3-5x.** — The speaker argues agents make thousands of cheap calls and that routing them to top models is the main source of waste. Hand-written if/else routing breaks when prompts change. ([0:00](https://youtu.be/BXme4u4uoyA?t=0))
- **Manifest is a drop-in router: one endpoint, no agent rewrite, cost reduction by routing each request to the cheapest model that can handle it.** — It scores each request across 23 dimensions and picks a model from the configured providers, including local ones such as Ollama. ([1:05](https://youtu.be/BXme4u4uoyA?t=65))
- **Routing is deterministic scoring, not an LLM call, so it adds negligible latency.** — The speaker says a routing decision takes under 2 ms, and that using an LLM to route would be slow and costly. ([2:26](https://youtu.be/BXme4u4uoyA?t=146))
- **The dashboard reports token usage, cost per agent and budget tracking in real time.** — This gives per-agent and per-task spend visibility, which the speaker treats as one of the main benefits. ([2:26](https://youtu.be/BXme4u4uoyA?t=146))
- **Compared with OpenRouter and LiteLLM, Manifest is positioned as self-hosted with automatic routing.** — OpenRouter is one hosted endpoint where prompts leave your system and carries a fee. LiteLLM gives a unified interface but routing is manual. Manifest can run fully self-hosted and routes automatically. ([3:40](https://youtu.be/BXme4u4uoyA?t=220))
- **Savings are largest from subscription routing and fallbacks, not from prompt tuning.** — The speaker says routing through plans already paid for avoids per-token billing, and that fallbacks keep an agent running when a provider fails. ([4:45](https://youtu.be/BXme4u4uoyA?t=285))
- **Caveats: routing is opinionated and can be cheaper than expected, and setup still needs key and provider management.** — The speaker recommends knowing the routing is happening and overriding it when needed. He says OpenRouter is simpler if zero setup matters more than privacy. ([5:56](https://youtu.be/BXme4u4uoyA?t=356))

## Techniques
- **Drop-in LLM router in front of agents** — Run Manifest with Docker (a simple curl install, then docker compose up). Point the agent's OpenAI base_url at the Manifest endpoint. Use the Manifest API key as the only key in the agent. Link providers in the Manifest UI (OpenAI, Anthropic, Ollama) so it can route between cloud and local models. *When:* Agents make many small calls (classification, routing, summaries) and you want cost reduction without changing agent code.
- **Deterministic request scoring for model routing** — Score each request on a fixed set of dimensions (the video cites 23) and map the score to the cheapest model that can handle it. Avoid using an LLM to make the routing decision. *When:* Routing latency must stay low and routing decisions have to be reproducible.
- **Route to subscriptions and local models before paid API tokens** — Include plan-based providers (subscriptions you already pay for) and local models (llama.cpp or Ollama) as routing targets, so the router uses them before per-token APIs. *When:* You already pay for a plan or run local models and want to reduce per-token spend.
- **Failover on provider errors** — Let the router fall back to another model when the chosen provider fails, so the agent keeps running. *When:* Agents need to keep running through provider outages or errors.
- **Per-agent cost tracking and budgets** — Use the Manifest dashboard to watch token usage and cost per agent and set budgets, instead of checking total provider bills. *When:* Several agents or tasks share the same model accounts and you need to attribute spend.

## Numbers
- Up to 70% lower token cost on the same agent and same tasks, shown in a single demo; the speaker says the figure can vary. ([0:00](https://youtu.be/BXme4u4uoyA?t=0))
- Agent bills can run 3-5x higher than necessary when simple calls go to expensive models. ([0:00](https://youtu.be/BXme4u4uoyA?t=0))
- Routing scores each request across 23 dimensions. ([1:05](https://youtu.be/BXme4u4uoyA?t=65))
- Routing decision latency is under 2 ms, per the speaker. ([2:26](https://youtu.be/BXme4u4uoyA?t=146))
- Supports hundreds of models across many providers, per the speaker. ([2:26](https://youtu.be/BXme4u4uoyA?t=146))

## Hot takes
- Routing an agent's calls to the cheapest capable model is the main cost lever, more than prompt tuning.
- A deterministic scorer beats using an LLM to route, because the router must be fast and cheap.
- Manifest's own promotional framing ('this is one of the fastest ways') is not backed by a published benchmark; the 70% number is one demo, not a measured result.
- The speaker says the video is 'dead simple' to set up, but also says key and provider wiring is still required.

## Tools mentioned
Manifest, Docker, Docker Compose, OpenAI API (base_url change), Anthropic API, Ollama, OpenRouter, LiteLLM, llama.cpp, Python (demo agent script)

## Relevance to our work
- **agentos** (3/3): AgentOS L1 Govrix Scout is a Rust proxy with budgets and strategy routing, which is the same job Manifest does (model routing and budgets on one OpenAI-compatible endpoint). Comparing its scoring and fallback design to Govrix's strategy routing is directly useful. → *Compare Manifest's deterministic 23-dimension scorer and fallback behavior with Govrix's strategy routing. Check the routing latency and the cost savings on the same tasks, and consider a per-agent cost panel like Manifest's.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI and uses cheaper models for some calls. A router is only loosely related, but the cheap-model routing idea matches its Haiku pipeline interest.

# 4 Billion Free LLM Tokens… One API (FreeLLMAPI)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `sHOwbyMbun0` · [watch](https://youtu.be/sHOwbyMbun0) · **date:** 2026-09-02 · **length:** 9:13 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, OpenRouter, LiteLLM, Google, xAI (Grok), Cerebras, Mistral, NVIDIA
- **topics:** token-cost-efficiency, infra-cost-scaling, dev-tools · **tags:** free-tier, llm-gateway, failover, openai-compatible, routing, docker, docker-compose, rate-limits, cost, coding-agents

> Better Stack walkthrough of FreeLLM API, a self-hosted gateway that pools free LLM tiers from about 28 providers behind one OpenAI-compatible endpoint with failover. Useful for cheap prototyping; the speaker warns free-tier quality and availability drift.

## Summary
The video presents FreeLLM API, a locally run gateway (Docker Compose) that takes the user's own free-tier API keys from about 28 providers and exposes them through one OpenAI-compatible endpoint. It tracks quota, health and rate limits, routes each request to a healthy provider, and fails over when one hits a limit, so the calling tool never sees the switch. The host demos setup (clone, generate an encryption key, docker compose up, add keys in the dashboard, pick a routing strategy, test in Playground) and then runs a small multi-file Python CLI task through the endpoint using under 2,000 tokens. He positions it against OpenRouter (hosted capacity) and LiteLLM (broader production gateway you configure yourself), calling it free-tier maximization rather than a replacement for a gateway. The strongest points are pooled capacity, one key for all coding tools, local-only credentials and failover. The caveats are inconsistent free quotas, varying model quality and latency, and models that can disappear, so he advises against production use. The 4-billion-token headline is an advertised aggregate that the demo does not test.

## Key ideas
- **Pooled free tiers behind one endpoint: the tool pulls free tiers from about 28 providers, routes requests among them, and fails over automatically, so tools see a single OpenAI-compatible endpoint.** — Headline claim is roughly 4 billion free tokens a month; the video does not verify this figure. Speaker's framing is that individual free tiers are small and inconsistent, so pooling makes them useful. ([0:00](https://youtu.be/sHOwbyMbun0?t=0))
- **The real pain is operational, not capacity: each provider has its own key, dashboard, rate limit and model names, and a mid-task limit forces a manual switch.** — The gateway tracks quota, health and rate limits per provider and routes around them so an agent run does not die halfway through a job. ([1:05](https://youtu.be/sHOwbyMbun0?t=65))
- **Routing model: provider keys are stored encrypted locally; the router filters providers by health and remaining quota and forwards each request; clients only talk to the local OpenAI-compatible door.** — Speaker says the application no longer chooses the provider; the router does, and it can move a request if a provider gets rate-limited or unhealthy. ([4:36](https://youtu.be/sHOwbyMbun0?t=276))
- **Positioning: it spends the user's own free-tier accounts, unlike OpenRouter (hosted capacity you pay into or use via their platform) and LiteLLM (a broader, production-oriented gateway where you configure routing yourself).** — Speaker calls it free-tier maximization, with a much narrower job than a full gateway. ([5:35](https://youtu.be/sHOwbyMbun0?t=335))
- **Failover matters more than the token count: free tiers have rate limits and daily caps that change, so the value is moving off a provider when it stops working.** — Other wins he lists are one key for all coding tools, credentials that stay on the local machine, and pooled capacity. ([7:38](https://youtu.be/sHOwbyMbun0?t=458))
- **Caveats: the request may land on a weaker or slower model once a preferred quota is exhausted, and free models can disappear. He would not put production infrastructure on it.** — Quality and latency can vary within a single session, and the advertised pool does not give access to frontier models on demand. ([7:38](https://youtu.be/sHOwbyMbun0?t=458))
- **The demo test is small: a multi-file Python task CLI built with the router in front, using under about 2,000 tokens, which says little about pool capacity or failover under load.** — Speaker verified that the output ran and wrote a README; he did not show a rate-limit failover event happening. ([3:22](https://youtu.be/sHOwbyMbun0?t=202))

## Techniques
- **Single OpenAI-compatible endpoint over pooled free tiers** — git clone the FreeLLM API repo (the URL is in the video description, not spoken), cd into it, generate a 32-byte encryption key for the credential store (the variable name is not stated on screen), run docker compose up, open the local dashboard, add provider API keys (Google, Grok, Cerebras, Mistral, OpenRouter shown; up to 28 providers), then point an OpenAI-compatible client at the local endpoint using the gateway's key. The base URL and key variable were not shown in the transcript. *When:* Prototyping, side projects, and latency-tolerant agent loops where you want to avoid burning paid credits and do not want to swap keys when a limit hits.
- **Choose a routing strategy in the dashboard** — In the routing settings, select a strategy; the host chose 'balance'. The model catalog is ranked by intelligence. *When:* Use balance when you want spread across providers rather than always the top-ranked model; the host did not compare the other strategies.
- **Smoke-test in the Playground before wiring tools** — After adding keys, send a prompt in the dashboard Playground and confirm a response before pointing coding agents at the endpoint. *When:* Immediately after configuring providers, to confirm at least one provider is live.
- **Check monthly token usage per model before long runs** — The Models tab shows monthly tokens consumed for each model in the catalog. *When:* Before starting a long agent run, to check remaining free-tier headroom.
- **Reserve the pool for latency-tolerant work** — Send agent loops, prototypes and bulk experiments through the gateway; keep quality-sensitive or production calls on direct, paid providers. *When:* When cost matters more than consistent latency or model quality, as the speaker recommends.

## Numbers
- Advertised pool of roughly 4 billion free LLM tokens a month (headline; not verified in the video) ([0:00](https://youtu.be/sHOwbyMbun0?t=0))
- Free tiers pulled from 28 providers ([0:00](https://youtu.be/sHOwbyMbun0?t=0))
- Repo has passed 18,000 GitHub stars (speaker's figure) ([0:00](https://youtu.be/sHOwbyMbun0?t=0))
- Setup claimed to take under a minute (not timed on screen) ([0:00](https://youtu.be/sHOwbyMbun0?t=0))
- Demo multi-file Python CLI task used less than about 2,000 tokens ([3:22](https://youtu.be/sHOwbyMbun0?t=202))
- Models tab shows monthly token usage per model (speaker said 'quite a lot' but no figure was given) ([2:20](https://youtu.be/sHOwbyMbun0?t=140))

## Hot takes
- The 4-billion-token headline is an aggregate advertised pool; the demo spends under 2,000 tokens and does not test it.
- The most useful part of the video is the speaker's own caveats: quality and latency drift, and free models can disappear, so do not build production on it.
- Explicitly positions the tool as free-tier maximization, distinct from OpenRouter and LiteLLM, which is a fair framing.
- Title is hype-leaning, but the substance is a moderate walkthrough of one open-source repo with no sponsorship segment seen, so quality is not capped at 2.

## Tools mentioned
FreeLLM API (Free LLM API), Docker, Docker Compose, Git, OpenAI-compatible client SDK, OpenRouter, LiteLLM, Grok (xAI), Cerebras, Google models, Mistral, NVIDIA (free models mentioned as 'open route'), Claude Code, Cursor, Codex

## Relevance to our work
- **agentos** (2/3): L1 Govrix Scout is a proxy with strategy routing and budgets; FreeLLM API uses the same pattern (one endpoint, health/quota-aware routing, failover), so it is a close reference for the routing layer. → *Compare Scout's strategy routing with this tool's balance strategy and health/quota-aware failover; test both against simulated 429s to see which keeps a run alive.*
- **prosharness** (1/3): The video's core failure case, an agent run dying halfway when one provider rate-limits, is the same problem checkpoint/resume is meant to handle. → *Use 'provider rate-limits mid-run' as a ProsHarness test case: resume on another provider from the last checkpoint rather than failing the run.*
- **general** (1/3): A possible free backend for low-stakes dev and eval traffic, with quality and availability caveats the speaker stated himself. → *Optional: try it as a free backend for latency-tolerant eval runs, but do not use its results as a quality baseline.*

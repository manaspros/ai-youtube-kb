# Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `zrZ1amZBSPw` · [watch](https://youtu.be/zrZ1amZBSPw) · **date:** 2026-09-18 · **length:** 16:24 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Kanish Manuja · **orgs:** Twilio
- **topics:** infra-cost-scaling, governance-compliance, security-guardrails · **tags:** llm-gateway, fallback, circuit-breaker, hedged-requests, tail-latency, p99, timeouts, guardrails, fail-open, fail-closed, load-shedding, bounded-queues, rate-limits, reasoning-models, governance, single-point-of-failure

> Principal engineer at Twilio on running an LLM gateway in production: per-request fallbacks, per-route latency timeouts, guardrail fail-open/closed choices, load shedding, and centralizing governance without centralizing traffic.

## Summary
Kanish Manuja (Twilio) frames an LLM gateway as middleware between apps and model providers that handles routing, auth, fallback, rate limits and governance. He argues that during degradation you cannot maximize availability, latency, guardrails and cost at once, so teams must pick what matters per use case. For availability he replaces circuit breakers and blind retries with per-request fallback to a second provider, noting that fallbacks are not transparent across tool-calling schemas, token limits and stop reasons. For latency he says to track P99 per model per route and set timeouts per model class, since missing timeouts cause silent outages, and reasoning or router models can vary from 2 to 60 seconds. For guardrails he covers fail-open versus fail-closed, a time budget for guardrail calls, fallbacks for guardrail providers, and where to place checks (pre, parallel or post). Finally he covers gateway-as-dependency risks: segregated API keys per route, bounded queues with load shedding, and decentralizing traffic while keeping governance central via plugins.

## Key ideas
- **Circuit breakers and blind retries do not suit LLM APIs** — LLM calls are slow and expensive, so retries eat the latency budget and multiply cost. Per-request fallback to a second provider is the better default, and a provider on cool-down should be pulled from the request path and retried after a few minutes. ([2:15](https://youtu.be/zrZ1amZBSPw?t=135))
- **Failure counts for cool-down can be local or fleet-wide** — Per-instance counters are simple but change meaning when deployment size changes. Shared fleet-wide counters fail over faster, at the cost of shared infrastructure. ([3:45](https://youtu.be/zrZ1amZBSPw?t=225))
- **Fallbacks are not transparent across providers** — The OpenAI-compatible format is converging, but tool-calling schemas, token limits and stop reasons still differ. A normalization layer and cross-provider tests are needed before fallbacks work. Streaming also locks the request to one provider once tokens reach the client. ([4:48](https://youtu.be/zrZ1amZBSPw?t=288))
- **The fallback provider needs more headroom than the primary** — The fallback is the last line of defense. Teams often load-test the primary and neglect the secondary, so the secondary should have equal or higher capacity. ([5:49](https://youtu.be/zrZ1amZBSPw?t=349))
- **Aggregate gateway latency hides the real problems** — Mixed workloads (embeddings and classification under 1s, chat around 3s, reasoning much longer) make one gateway-wide P99 meaningless. Track P99 per model per route and set timeouts per model class and route, because a missing timeout is the most common cause of silent outages. ([6:54](https://youtu.be/zrZ1amZBSPw?t=414))
- **Reasoning and router models are the hardest latency case** — Reasoning output is nondeterministic, temperature may not be settable, and the same prompt can take 2 to 60 seconds. Router models hide which model runs. Fix the reasoning level per route where possible, and hedge the tail by firing a second request once the first has used about P90 of the latency budget. ([8:21](https://youtu.be/zrZ1amZBSPw?t=501))
- **Guardrails are a dependency too, so choose fail-open or fail-closed on purpose** — Guardrails for prompt injection, PII and toxicity can go down. Fail-open serves requests without the check and fail-closed blocks them. The default should be the worst case the use case can live with, for example a toxicity filter can fail open. Guardrails also need their own time budget so they never set request latency. ([9:49](https://youtu.be/zrZ1amZBSPw?t=589))
- **Guardrail placement trades latency against safety** — A pre-hook on input is safest but adds serial latency. Running checks in parallel saves latency but does not combine with streaming, so structured outputs should not be streamed in that mode. Post-hooks suit output monitoring and auditing. ([11:20](https://youtu.be/zrZ1amZBSPw?t=680))
- **The gateway itself is a dependency and a single point of failure** — Segregate API keys per route and use case to contain noisy tenants. Use bounded queues, load shedding and traffic prioritization, since a retry storm cannot be fixed by scaling out. Avoid one company-wide gateway: decentralize traffic and centralize governance (cost tracking, rate limits) through plugins or shared code. ([13:53](https://youtu.be/zrZ1amZBSPw?t=833))

## Techniques
- **Per-request provider fallback** — On failure of provider A, retry the same request on provider B in sequence. Optionally send to both in parallel, which doubles cost. Use a normalization layer so tool schemas, token limits and stop reasons match across providers. *When:* When a single model provider outage would take your app down and latency matters more than a blind retry.
- **Cool-down for failing providers** — Take a provider that keeps failing out of the request path for a few minutes, then reintroduce it. Choose between per-instance failure counters and shared fleet-wide counters. *When:* When one provider is degraded and retries only add cost and tail latency.
- **Per-route P99 and timeouts** — Measure P99 per model and per route, not gateway-wide. Set explicit timeouts for each model class and route so a stuck call becomes a visible error. *When:* When a gateway serves mixed workloads (embeddings, classification, chat, reasoning) and needs reliable alerting.
- **Hedged requests for the tail** — If the first request has used about P90 of the latency budget, fire a second request and take whichever returns first. *When:* For latency-sensitive routes where P99 spikes matter and extra cost is acceptable.
- **Guardrail time budget and explicit fail mode** — Run each guardrail with its own timeout. Decide per guardrail whether to fail open or fail closed when it is unavailable. Optionally add a secondary guardrail provider. *When:* When guardrails (injection, PII, toxicity) are external services that can be slow or down.
- **Guardrail placement by output type** — Use a pre-hook on input for maximum safety. Run guardrails in parallel with the LLM call for structured outputs, without streaming. Use post-hooks for auditing outputs. *When:* When you must balance serial latency against safety checks.
- **Bounded queues and load shedding with priorities** — Bound every server queue, shed load under retry storms, and prioritize important routes under load. Practice this in runbooks and game days. *When:* When retry storms could make scaling out ineffective.
- **Per-route API key segregation** — Issue separate API keys per route and use case, to the most granular level practical. *When:* When one noisy tenant or workload could starve others of rate limit or quota.
- **Decentralized traffic, centralized governance** — Run gateway instances per team or service, and centralize cost tracking and rate limit policy through plugins or shared code instead of routing all traffic through one deployment. *When:* When a company is tempted to build one central gateway that becomes a single point of failure.

## Numbers
- Typical latency by workload: embedding and classification requests under 1 second, chat around 3 seconds, reasoning requests much longer. ([6:54](https://youtu.be/zrZ1amZBSPw?t=414))
- Reasoning and router model latency for the same prompt ranges from about 2 seconds to 60 seconds; production P99 once jumped to 60 seconds with no clear cause. ([8:21](https://youtu.be/zrZ1amZBSPw?t=501))
- Suggested hedge point is about P90 of the latency budget before firing a second request. ([8:21](https://youtu.be/zrZ1amZBSPw?t=501))
- Parallel firing to two providers for lowest latency roughly doubles cost (the speaker's estimate). ([2:15](https://youtu.be/zrZ1amZBSPw?t=135))
- Speaker recommends the fallback provider get equal or higher capacity headroom than the primary. ([5:49](https://youtu.be/zrZ1amZBSPw?t=349))

## Hot takes
- Circuit breakers as used for normal APIs do not fit LLMs; per-request fallback to another provider is better.
- A gateway-wide latency number is a lie when workloads are mixed; track P99 per model per route.
- A missing timeout is the most common root cause of silent LLM outages.
- Most teams asking for one central company gateway really want centralized governance; they can get it without centralizing traffic.

## Relevance to our work
- **agentos** (3/3): AgentOS L1 Govrix Scout is a proxy with budgets, PII/injection scanning and strategy routing, so it directly faces the fallback, guardrail fail-mode and per-route timeout decisions in this talk. → *Add per-request provider fallback with per-route timeouts to Govrix Scout, and make each guardrail's time budget and fail-open/fail-closed setting explicit in the manifest.*
- **general** (3/3): 
- **prosharness** (1/3): ProsHarness wraps Claude Code runs that can take long and vary in time. The talk's point about silent hangs and per-step timeouts applies only weakly. → *Set an explicit timeout per step class in long ProsHarness runs so a stuck step fails visibly at checkpoint instead of hanging.*

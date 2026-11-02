# Vercel goes ALL IN on AI (Vercel Ship Recap)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `idBEifQwlGI` · [watch](https://youtu.be/idBEifQwlGI) · **date:** 2025-11-02 · **length:** 4:55 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Vercel, Cloudflare, Anthropic, OpenAI, Google, Amazon, Kasada
- **topics:** sandboxing-execution, infra-cost-scaling, dev-tools · **tags:** vercel, ai-gateway, ai-sdk, vercel-sandbox, fluid-compute, active-cpu-billing, botid, rolling-releases, microfrontends, vercel-queues, vercel-agent, cloudflare-workers, byok, model-fallback, pricing

> Better Stack's 5-minute recap of Vercel Ship: AI Gateway and AI SDK v5 betas, a hosted sandbox for untrusted code with active-CPU billing, BotID, rolling releases, and several limited-beta features.

## Summary
A short news roundup of the announcements from Vercel's Ship keynote, framed around Vercel positioning itself as an AI-native cloud. The main AI items are the AI Gateway (beta), a proxy that routes requests across model providers with one billing relationship and fallback options, and AI SDK v5 (beta), where the model and provider are chosen by a string. Vercel Sandbox runs generated code in isolated ephemeral environments with stated limits, and its billing moved to active CPU time. Other items are BotID (generally available), rolling releases (generally available), and limited-beta features including microfrontends, Vercel Queues and a dashboard assistant called Vercel Agent. The speaker compares Vercel's sandbox pricing with Cloudflare Workers and notes the two are not directly comparable. Everything is restated from the keynote; there is no hands-on testing.

## Key ideas
- **AI Gateway (beta) is a proxy that routes AI requests across providers such as Anthropic, OpenAI and Google.** — The speaker likens it to OpenRouter. Benefits named: switch providers without juggling several billing accounts and API keys, and fall back when a model's provider is down. Free tier includes $5 of credits; later pricing depends on the models used. ([0:00](https://youtu.be/idBEifQwlGI?t=0))
- **Bring-your-own-key through the gateway carries a small surcharge.** — Using your own provider API key via the gateway costs an extra 3% of what the model would have cost through Vercel. ([0:00](https://youtu.be/idBEifQwlGI?t=0))
- **AI SDK v5 (beta) pairs with the gateway so model and provider can be chosen with a plain string.** — The speaker calls it possibly the best way to run AI from TypeScript and says a deeper video is planned. ([0:00](https://youtu.be/idBEifQwlGI?t=0))
- **Vercel Sandbox runs untrusted, AI-generated code in isolated ephemeral environments.** — Stated limits: up to 45 minutes of execution, up to 8 vCPUs and 2048 MB of memory per vCPU. The base image is Amazon Linux 2023 with Node 22 and Python 3.13. The speaker notes Cloudflare and Anthropic announced similar products around the same time. ([1:12](https://youtu.be/idBEifQwlGI?t=72))
- **Vercel moved compute billing to active CPU time, so idle time is not charged.** — The speaker's examples are LLM inference, long-running agents, and any workload with idle periods (such as waiting on model calls). It is presented as a cost saver for these workloads. ([1:12](https://youtu.be/idBEifQwlGI?t=72))
- **Vercel's pricing is positioned against Cloudflare Workers, but the speaker warns the comparison is not one-to-one.** — Memory, runtime limits and developer experience also need to be weighed. He says Cloudflare is cheaper on paper. ([2:17](https://youtu.be/idBEifQwlGI?t=137))
- **Default execution time rose to 300 seconds on all plans, and edge functions and middleware moved to Fluid compute.** — Framed as a performance and cost improvement. ([2:17](https://youtu.be/idBEifQwlGI?t=137))
- **Several features are only in limited beta: microfrontends, Vercel Queues and Vercel Agent.** — Microfrontends present several deployments as one app, with routing set in a JSON config in the root app. Queues offload slow work to background processing with retries. Vercel Agent is an assistant in the dashboard that summarizes performance and security anomalies and suggests actions such as firewall rule changes. The speaker frames these as rapid-fire items with no detail. ([3:23](https://youtu.be/idBEifQwlGI?t=203))

## Techniques
- **Model fallback and provider switching through a gateway** — Send requests to the AI Gateway and specify the model and provider as a string (AI SDK v5). For a model reachable through several providers, the speaker's example is Claude 4 via Vertex, Amazon Bedrock or Anthropic directly, so switching or falling back means changing the provider string rather than the integration. *When:* When you want resilience against a single provider outage or want to compare provider prices without managing several keys and billing accounts.
- **Bring-your-own-key via the gateway** — Configure your own provider API keys in the gateway. Requests then go through the gateway with a surcharge of about 3% of the model cost. *When:* When you want consolidated routing and observability but must keep existing provider contracts or credits. Weigh the 3% against your savings.
- **Ephemeral sandbox per run for generated code** — Create an isolated sandbox for each piece of generated code, execute the script inside it, and let it be discarded. The speaker says this takes a few lines of code and does not show the API. *When:* When an agent generates scripts that must not run on your own infrastructure. Keep the stated limits in mind: 45 minutes, 8 vCPUs, 2048 MB per vCPU, and Node 22 or Python 3.13.
- **Staged rollouts with rolling releases** — Start a defined rollout stage for a new deployment, then either let it progress automatically or promote it to a full release manually. Built-in monitoring and rollout controls are included, so no custom routing is needed. *When:* When shipping a risky change that should reach a fraction of traffic first.
- **Invisible bot detection with a typed client and server pair** — Use the BotID client component on the front end and call the CheckBotID function on the server to verify the request. No code is shown in the video. *When:* When you want bot protection without visible challenges or manual rules for public endpoints.

## Numbers
- AI Gateway free tier includes $5 of credits. ([0:00](https://youtu.be/idBEifQwlGI?t=0))
- Bring-your-own-key through the AI Gateway adds 3% of the model's cost. ([0:00](https://youtu.be/idBEifQwlGI?t=0))
- Sandbox max execution time 45 minutes, max 8 vCPUs, 2048 MB memory per vCPU. ([1:12](https://youtu.be/idBEifQwlGI?t=72))
- Vercel Sandbox after free allotments: 12.8 cents per hour of active CPU and 60 cents per million sandbox creations. ([1:12](https://youtu.be/idBEifQwlGI?t=72))
- Cloudflare Workers comparison as stated: 7.2 cents per hour of active CPU and 30 cents per million invocations. ([2:17](https://youtu.be/idBEifQwlGI?t=137))
- Default execution time raised to 300 seconds for all projects on all plans. ([2:17](https://youtu.be/idBEifQwlGI?t=137))

## Hot takes
- Keynote recap with no hands-on testing. Every claim is restated from Vercel's announcements, and the title's 'ALL IN on AI' framing outpaces the content, so quality is capped at 2.
- The speaker says the Cloudflare price comparison is not one-to-one and then gives no like-for-like numbers.
- Many items (microfrontends, Queues, Vercel Agent) are limited beta and described in one sentence each, so they are not evidence of production readiness.
- The 'coincidentally Cloudflare and Anthropic just released something similar' remark is a competitive framing with no detail behind it.

## Tools mentioned
Vercel AI Gateway, AI SDK v5, Vercel Sandbox, Fluid compute, Active CPU billing, BotID, CheckBotID, Rolling Releases, Microfrontends, Vercel Queues, Vercel Agent, Amazon Linux 2023, Node 22, Python 3.13, Cloudflare Workers, Kasada (BotID partner; auto-caption reads 'casada'), Claude 4 (via Vertex, Amazon, Anthropic)

## Relevance to our work
- **agentos** (2/3): AgentOS L1 (Govrix Scout) is a proxy with strategy routing, budgets and fallback-style behavior, the same product shape as the AI Gateway. Vercel's per-provider fallback and bring-your-own-key surcharge are a useful comparison point. The Sandbox pricing model also bears on the Crucible L2C design. → *Compare Govrix Scout's strategy routing and fallback behavior against the AI Gateway model (provider string plus fallback). For Crucible cost modeling, use the active-CPU billing and per-creation fee (12.8 cents/hr active CPU, 60 cents per million creations) as a reference point, not a target.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI and runs long checkpointed agent runs. Hosted sandboxes with execution-time caps could matter only if runs are ever offloaded. The video offers no new harness pattern. → *If ProsHarness ever offloads runs to a hosted sandbox, use Vercel Sandbox's limits (45 min, 8 vCPU, 2048 MB per vCPU) as a benchmark for run-length checkpointing.*

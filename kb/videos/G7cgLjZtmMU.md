# The Agentic Commerce Stack — Ahnaf Prio, Best Buy

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `G7cgLjZtmMU` · [watch](https://youtu.be/G7cgLjZtmMU) · **date:** 2026-09-18 · **length:** 20:38 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Ahnaf Priyo · **orgs:** Best Buy, OpenAI, Google, Meta, Cerebras, Microsoft
- **topics:** mcp-and-tools, product-ux, evals, security-guardrails · **tags:** agentic-commerce, AP2, UCP, ACP, MCP, A2A, product-feed, mandates, eval-driven-development, merchant-agents, demo, Cerebras

> Best Buy's Ahnaf Priyo maps the agentic commerce protocol stack (MCP, A2A, ACP, UCP, AP2), argues for pushed product feeds and checkout APIs over browser agents, and makes the case for behavior and protocol evals with a live cat-bakery demo.

## Summary
The speaker, a senior engineering manager at Best Buy, explains how shopping agents work today: mostly human-in-the-loop, with ChatGPT and Gemini handling a large share of shopping sessions. He says early browser-driven agents were slow, brittle, and alarming to merchants, so the working path is direct merchant checkout APIs. He lays out the layers: MCP for tool access, A2A for agent-to-agent calls, ACP (ChatGPT) and UCP (Google) for commerce primitives, and AP2 for payment mandates. He argues merchants should push product feeds instead of making per-request catalog calls, since that is M merchants times N products of load. A live demo uses a cat as a bakery agent, with a checkout state machine, an AP2 mandate (authorizer, scope, max amount, revocation, single use), and a timeline view of every call. He closes with evals as the main lesson: discount-code leaks and off-scope use show up in production without them, and he lists behavior, protocol-compliance, latency, and LLM-as-judge evals. He ends by sharing a template repo, eval templates, and agent skills for merchant and customer agents.

## Key ideas
- **Browser-driven shopping agents failed in practice** — Screenshot and DOM-reading agents that fill forms were clunky, slow, and brittle. Merchant engineering teams see an AI impersonating a browser as an alarm, so payment steps were often blocked. The working path is direct merchant checkout APIs. ([3:16](https://youtu.be/G7cgLjZtmMU?t=196))
- **Protocols sit in layers** — MCP gives the agent access to tools and capabilities. A2A is the spec for agent-to-agent talk, useful when a customer agent and merchant agent, or domain agents, need to communicate. ACP (ChatGPT) and UCP (Google) are the commerce primitives. AP2 is the agentic payment protocol with scoped mandates. ([7:01](https://youtu.be/G7cgLjZtmMU?t=421))
- **Push product feeds instead of per-request catalog search** — Neither ChatGPT nor Gemini currently calls a merchant search catalog endpoint, so merchants send a feed ahead of time. Pushing the feed lets the platform index it. Calling every merchant on every request scales as M merchants times N products. Feeds also carry sponsored and ranking signals, and the speaker says the three feed specs are similar but differ. ([8:24](https://youtu.be/G7cgLjZtmMU?t=504))
- **Payments stay human-in-the-loop for now** — No major platform supports autonomous payments such as x402 yet. ChatGPT takes a shared payment token and Gemini UCP takes Google Pay, with the processor taking liability. AP2 is the piece he is most excited about: it records who authorized the agent, what it may buy, the maximum amount it may negotiate up to, a revocation URL, and proof of user consent. ([9:40](https://youtu.be/G7cgLjZtmMU?t=580))
- **Checkout is a state machine the agent must follow** — UCP checkout sessions move through three states: not ready for payment, ready for payment, and completed. In the demo, the agent first adds items to the cart, then the payment method is chosen, and only then is the AP2 mandate issued, which moves the session to completed. ([13:11](https://youtu.be/G7cgLjZtmMU?t=791))
- **Make every call inspectable with a timeline and feed sync** — The demo logs each MCP, A2A, and checkout call on a timeline like Chrome DevTools. Inventory is re-synced every couple of seconds. The speaker suggests reusing these primitives even for a merchant's own site, not only for ChatGPT or Gemini. ([14:29](https://youtu.be/G7cgLjZtmMU?t=869))
- **Conversational agents need evals or they play whack-a-mole** — A demo agent leaked a discount code when asked, and without evals each fix exposes another failure. He recommends testing behavior, protocol compliance (feeds must conform or the platform will not accept them), latency benchmarks (slow steps lose shoppers), and LLM-as-judge quality checks. ([15:55](https://youtu.be/G7cgLjZtmMU?t=955))
- **Scope the agent or it will be used off-topic** — He cites a Chipotle agent that users reportedly used for programming questions. He says he is not sure it is true, but the lesson is to write scope rules and evals that refuse out-of-scope requests before production. ([17:23](https://youtu.be/G7cgLjZtmMU?t=1043))

## Techniques
- **Push product feed to platforms** — Send the merchant catalog as a feed in the platform's schema ahead of time, with change notifications, instead of answering per-query catalog search calls. Keep it in sync for inventory. *When:* When many merchants and many products would otherwise mean many outbound calls per user request, or when the platform does not offer catalog search.
- **Checkout as an explicit state machine** — Model checkout as not-ready, ready-for-payment, completed. Have the agent add to cart, select payment, then issue the payment token, and gate each step on the current state. *When:* When building or integrating a merchant checkout API that an agent drives.
- **Scoped, single-use, revocable payment mandate** — Attach a mandate to each payment that names the authorizing user, the allowed products or scope, the currency, the maximum amount, single-use status, and a revocation URL. *When:* When an agent may spend on a user's behalf and the spend limit needs to be enforced and revoked.
- **Layered evals for conversational commerce agents** — Write behavior evals (for example discount-code and off-scope refusals), protocol-compliance checks against the platform schema, latency benchmarks per step, and an LLM-as-judge quality rubric built from real use cases. *When:* Before shipping any customer-facing conversational agent, and again after each prompt or tool change.
- **Timeline view of agent calls** — Record each tool call, agent message, and checkout state change with timestamps, and render them in a viewer you can open per session. *When:* When debugging multi-agent or multi-protocol flows that are hard to follow from logs.
- **Agent skills for domain roles** — Package merchant-agent, customer-agent, and catalog-sync workflows as agent skills, plus a three-service starter template and eval templates. *When:* When you want a repeatable setup for each agent role instead of rebuilding it per project.

## Numbers
- About 45% of agent sessions on major providers such as ChatGPT and Gemini relate to shopping ([1:07](https://youtu.be/G7cgLjZtmMU?t=67))
- Agentic shopping cited as a $7 billion industry, possibly $65 billion by 2030 ([3:16](https://youtu.be/G7cgLjZtmMU?t=196))
- Demo model served by Cerebras at about 3,000 tokens per second ([10:47](https://youtu.be/G7cgLjZtmMU?t=647))
- Inventory and catalog kept in sync roughly every couple of seconds in the demo ([14:29](https://youtu.be/G7cgLjZtmMU?t=869))

## Hot takes
- Browser-impersonating shopping agents are a dead end because merchant teams will block them; direct checkout APIs are the path.
- Merchants should push product feeds rather than wait for platforms to call catalog search.
- Without evals, conversational commerce agents will leak discounts and get used off-scope in production.
- Autonomous payments are not ready; human-in-the-loop with a processor holding liability is the current model.

## Tools mentioned
MCP, A2A, ACP, UCP, AP2, Cerebras, ChatGPT, Gemini, Chrome DevTools

## Relevance to our work
- **agentos** (2/3): The AP2 mandate fields (authorizer, scope, max amount, single use, revocation) map onto budget and authorization controls in the L1 proxy. The out-of-scope eval lesson also applies to the guardrail and exec-gate work. → *Add a scoped, revocable spend-mandate record to the Govrix budget layer, and add off-scope and discount-leak style behavior evals to the guardrail test suite.*
- **prosharness** (1/3): Human-in-the-loop approvals with a bounded mandate (scope, max amount, expiry, revocation) are a similar pattern to phone-driven approvals in ProsHarness. → *Consider giving phone approvals a structured record with scope, limit, expiry, and revocation so an approved action can be checked and revoked later.*

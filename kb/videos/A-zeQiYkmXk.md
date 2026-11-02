# Teaching agents to pay — Anna Spysz, Stripe

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `A-zeQiYkmXk` · [watch](https://youtu.be/A-zeQiYkmXk) · **date:** 2026-09-18 · **length:** 19:10 · **format:** demo · **quality:** 2/5 · **depth:** intro
- **speakers:** Anna Spysz · **orgs:** Stripe, Google, OpenAI
- **topics:** security-guardrails, mcp-and-tools, governance-compliance, product-ux · **tags:** agentic-commerce, universal-commerce-protocol, shared-payment-token, merchant-manifest, system-prompt, guardrails, persona, payments, audit-logging

> Stripe engineer builds an agentic-commerce agent to buy headphones, covering the Universal Commerce Protocol, merchant manifests, shared payment tokens, persona effects on behavior, and a guardrail checklist.

## Summary
Anna Spysz from Stripe demos an agent she built to buy recording headphones from a local Portland shop, using the Universal Commerce Protocol (UCP) to talk to merchants. She shows that most merchant sites are not agent-ready, so she publishes a capabilities manifest at /.well-known and a structured JSON catalog that includes policies. The demo's agent first behaves like an aggressive salesman because of its system prompt. Switching to a "patient recording gear mentor" persona fixes the behavior, which she presents as proof that the prompt shapes the customer experience. She explains the shared payment token: the agent and merchant only handle a token, and the payment provider enforces limits. She closes with a guardrail checklist (disclose AI, disclose fees, respect stop/cancel, cap at the user's max amount, avoid dark patterns, log decisions). The talk is mostly a walkthrough of Stripe's agentic-commerce stack, so the technical content is thin in places.

## Key ideas
- **Agents discover and choose products differently from humans, so merchants must expose structured data and protocols agents understand.** — The speaker says agents read structured data and technical signals, not visual design. Merchants therefore need a shared protocol (UCP) that covers initiating, updating, completing and cancelling a purchase. ([3:44](https://youtu.be/A-zeQiYkmXk?t=224))
- **A merchant capabilities manifest is a public JSON file at /.well-known that declares capabilities, payment methods and API endpoints.** — Agents are told to look in this well-known location. It lets an agent learn what a store can do without parsing a full HTML site, which the speaker says burns many tokens. ([6:14](https://youtu.be/A-zeQiYkmXk?t=374))
- **The catalog and policies (shipping, returns) must be structured JSON, because agents filter, rank and justify with them.** — If shipping or return information is hard to reach, the agent may hallucinate or say it does not know. The speaker also says matched attributes should be logged so the merchant can account for how a recommendation was made. ([7:41](https://youtu.be/A-zeQiYkmXk?t=461))
- **The system prompt (persona) can change a shopping agent from pushy to trustworthy, even with the same tools and model.** — The first persona was 'an aggressive audio gear salesman' and the agent pushed expensive items and became rude when told to think it over. Switching to a 'patient recording gear mentor' persona produced a sensible reply to the same question. ([9:09](https://youtu.be/A-zeQiYkmXk?t=549))
- **The agent's loop has three parts: the model as decision-maker, tools as hands, and instructions that run in a loop until a condition is met, with the system prompt as persona and ethics policy.** — The speaker uses this simple picture to explain why an agent behaves a certain way. Tools here are commerce actions such as complete checkout or request payment method. ([10:37](https://youtu.be/A-zeQiYkmXk?t=637))
- **Shared payment tokens keep raw card data away from the agent and the merchant.** — The agent asks the payment provider (Stripe in the demo) for a payment method and receives a token. The merchant unwraps it to get the credential and fraud signals, then sends it to the provider. The provider enforces limits, so an expired token or bad currency is rejected. ([15:32](https://youtu.be/A-zeQiYkmXk?t=932))
- **The payment provider, not the agent or merchant, enforces spend limits.** — The speaker's point is that a violated guardrail results in a rejected charge, so the agent cannot override a limit. This depends on the provider as the trusted enforcement point. ([16:57](https://youtu.be/A-zeQiYkmXk?t=1017))
- **Practical guardrail checklist for commerce agents: disclose AI, disclose fees, respect stop/cancel, cap at the user max, avoid urgency or dark patterns, and log decisions.** — The speaker calls it non-exhaustive. Logging all agent decisions for auditability is listed as the most important item. ([11:34](https://youtu.be/A-zeQiYkmXk?t=694))

## Techniques
- **Merchant capabilities manifest at /.well-known** — Publish a public JSON file at the site root that declares capabilities, supported payment methods and API endpoints, so agents know where to look. *When:* When a service should be usable by agents without them scraping HTML pages.
- **Structured catalog and policy JSON** — Store product attributes and policies (shipping, returns) as compact structured JSON with only the fields an agent needs. *When:* When an agent must filter, rank or justify choices, or answer policy questions without hallucinating.
- **Attribute-match decision logging** — Record which structured attributes the agent matched when it recommends an item, and keep these records for accountability. *When:* When outcomes must be explained or audited later.
- **Persona-driven behavior control and A/B testing of system prompts** — Keep the same tools and model but swap the persona prompt, then rerun the same multi-turn scenario (for example asking whether to think it over) to compare behavior. *When:* When an agent's tone or sales behavior is wrong and the cause may be the system prompt.
- **Scoped payment token instead of raw credentials** — The agent requests a payment method from the provider, receives a token, and passes it to the merchant, who passes it to the provider. Fraud signals travel with the token. *When:* When an agent must complete a payment without ever holding card numbers.
- **Provider-enforced transaction limits** — Keep spend limits and validity checks (expiry, currency, amount) at the payment provider so violations cause rejection regardless of the agent. *When:* When an agent must not be able to exceed user-set spend caps.
- **Agent commerce guardrail checklist** — Disclose AI identity, show fees up front, honour stop or cancel at any time, check total against the user's max, avoid urgency language or dark patterns, and log every decision. *When:* Before shipping any agent that talks to a customer or spends money.

## Numbers
- Speaker cites that about one in four people already use AI to research purchases before buying. ([1:14](https://youtu.be/A-zeQiYkmXk?t=74))
- The user's self-imposed budget cap for the headphones was $500, and the agent kept results under it after the change. ([13:04](https://youtu.be/A-zeQiYkmXk?t=784))
- Express shipping delivered the headphones the next day, as shown in the demo. ([17:56](https://youtu.be/A-zeQiYkmXk?t=1076))

## Hot takes
- Most merchants are not ready for agentic commerce, and an agent cannot read a nice website efficiently.
- The system prompt shapes the customer experience as much as any model choice.
- Agents should never see raw card numbers; the payment provider should be the one enforcing limits.

## Tools mentioned
Universal Commerce Protocol (UCP), Stripe payments, Google Pay, Apple Pay, shared payment token

## Relevance to our work
- **agentos** (1/3): L1 Govrix Scout already has budgets and a Merkle audit log, and the talk's max-amount cap and log-every-decision checklist maps onto that, but the talk is about commerce, not infra. → *Check whether L1 budgets can enforce a per-action max amount supplied by the end user and whether every tool-call decision is written to the audit log.*
- **prosharness** (1/3): Shared payment tokens are the same idea as zero-token credential handling: the agent works with a scoped handle and the trusted party holds the secret. → *Compare the shared-payment-token flow with ProsHarness credential handling to see whether any part of the token boundary is missing there.*
- **general** (1/3): Shows that persona or system prompt changes alone flipped an agent from pushy to honest. This is a context-engineering point and fits the recurring interest in agent behavior tuning. → *Run a small A/B test of two system prompts on the same multi-turn scenario and log behavior differences, as a template for evals of persona prompts.*

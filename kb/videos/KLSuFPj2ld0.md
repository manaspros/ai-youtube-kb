# Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `KLSuFPj2ld0` · [watch](https://youtu.be/KLSuFPj2ld0) · **date:** 2026-06-18 · **length:** 18:46 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Steve Kaliski · **orgs:** Stripe, Tempo, OpenAI
- **topics:** security-guardrails, governance-compliance, mcp-and-tools · **tags:** payments, shared-payment-tokens, agentic-commerce, http-402, spend-limits, delegated-credentials, determinism, stripe-issuing, tempo, agent-to-commerce-protocol

> Stripe's Steve Kaliski on letting agents spend safely: scope shared payment tokens to amount, time and seller, use HTTP 402 for paid tools, and keep discovery non-deterministic while payments stay deterministic.

## Summary
Steve Kaliski (Stripe) argues that agents already spend money, through token costs and subscriptions, and that the open question is how to let them pay merchants and tools safely. He splits the problem in two: discovery and recommendation can stay non-deterministic, but credentials, payment and checkout must be deterministic. He names four failure modes: wrong place (a look-alike domain), wrong thing, wrong amount (prices drift, parsing errors, tax and currency), and wrong credential. Stripe's first answer is shared payment tokens, where the agent collects a credential and mints a token that Stripe enforces for one seller, one amount cap, one currency and an expiry. The seller still sees brand, last four and credit type so its risk systems keep working. The second piece, built with Tempo, is a machine payments flow in which a tool returns HTTP 402 with a payment payload, and the agent pays and retries. The third, built with OpenAI, is the Agentic Commerce Protocol: sellers expose catalogs as JSON, and each cart change round-trips to the seller for authoritative totals, tax and fulfillment. The closing thesis is that a non-deterministic planner plus verifiable parties and structured negotiation keeps the blast radius small. The Q&A covers on-chain settlement, recurring budgets via an OAuth-style refresh flow, and a claim that Stripe Projects is built on these primitives.

## Key ideas
- **Split discovery from transaction** — Let the LLM search and recommend (non-deterministic), but make credentials, payment and checkout fully deterministic and structured. Keeping these separate limits what a wrong model output can cost. ([1:02](https://youtu.be/KLSuFPj2ld0?t=62))
- **Four ways an agent can lose money** — Wrong place (look-alike domain), wrong thing (cheap vs. 10x-price item), wrong amount (price drift, currency, tax, misparsed numbers), wrong credential (pasting a card number). Browser-operating agents hit all four. ([2:25](https://youtu.be/KLSuFPj2ld0?t=145))
- **Shared payment tokens scope a credential to a seller** — The agent collects a payment credential and provisions a token encoding limits: one seller, amount cap, currency, time window. Stripe enforces these even if the agent was tricked by a bad domain or misread the amount. ([5:19](https://youtu.be/KLSuFPj2ld0?t=319))
- **Keep the seller informed** — Sellers still receive brand, last four and credit type, so their existing risk systems can run. The aim is to limit the agent's authority without hiding the transaction from the seller. ([7:48](https://youtu.be/KLSuFPj2ld0?t=468))
- **HTTP 402 makes tool calls payable** — A tool call is an HTTP request, so a protected endpoint can return a payment-required status with a payload describing payee, amount and mechanism. The agent pays and retries, which handles ephemeral tool calls that have no account or API key. ([9:13](https://youtu.be/KLSuFPj2ld0?t=553))
- **Checkout as a structured negotiation** — Products are described as JSON catalogs. Every change to quantity, shipping or payment goes to the seller, which returns authoritative cart state (line items, tax, fulfillment options). The agent does not scrape totals from a UI. ([11:42](https://youtu.be/KLSuFPj2ld0?t=702))
- **Make products agent-friendly, not just web-friendly** — If businesses expose only web UIs, agents are pushed into non-deterministic browsing. Exposing structured flows moves the interaction to deterministic API calls. ([15:01](https://youtu.be/KLSuFPj2ld0?t=901))
- **Recurring budgets via refresh-style grants** — In Q&A the speaker describes a recurring allowance (for example a weekly budget for one model) as an OAuth-like access and refresh flow on the same credential, with broader budgets made by creating more seller-scoped tokens. ([16:12](https://youtu.be/KLSuFPj2ld0?t=972))

## Techniques
- **Seller-scoped delegated payment credential** — Agent collects a card or other method once, then mints a token limited by seller, amount, currency, expiry. The payment platform enforces the limits; the agent does not. *When:* Agent must pay a merchant it has not vetted, or may misparse a price, and you need a bounded blast radius.
- **Deterministic transaction layer behind a non-deterministic planner** — Let the LLM plan, search and pick items freely. Route every credential use, payment and checkout step through structured API calls with typed inputs and verifiable outputs. *When:* Any agent flow that moves money, or any tool whose side effects must be exact.
- **HTTP 402 pay-per-call** — Protected endpoint returns a payment-required response with an encoded payload (payee, price, currency, method). Client attaches a credential and retries. The exchange is machine-readable. *When:* Metered or per-call tools where API keys are awkward, such as ephemeral or one-off agent tool calls.
- **Round-trip checkout state** — Each cart mutation (quantity, shipping, payment method) is a request to the seller, which returns the authoritative state. The agent reads structured totals, tax and options rather than parsing a page. *When:* Agent-driven purchases where price, tax or fulfillment must match what the buyer approves, to reduce disputes and chargebacks.
- **Forward risk signals to the counterparty** — Pass brand, last four and credential type to the seller alongside a delegated token so the seller's existing risk checks still apply. *When:* Any delegated credential where the merchant must accept or decline the transaction.

## Numbers
- Demo: a Visa card with a much higher limit was provisioned as a token capped at $25 for 30 days and scoped to one seller. A $50 charge was rejected for exceeding the mandate. A $25 charge then succeeded. ([6:43](https://youtu.be/KLSuFPj2ld0?t=403))
- Demo tool call costs one penny, paid in pathUSD on the Tempo blockchain, and the transaction is visible on-chain afterward. ([9:13](https://youtu.be/KLSuFPj2ld0?t=553))
- Speaker says Stripe has no public statistics on adoption of shared payment tokens yet. ([17:17](https://youtu.be/KLSuFPj2ld0?t=1037))

## Hot takes
- Agents are already economic actors: running Claude Code or Codex already spends money, through subscriptions or token conversion.
- Discovery should stay non-deterministic, but payments, credentials and checkout should move entirely to deterministic flows.
- Handing an agent a raw card number is the wrong design, because nothing enforces the spend limit once the number is shared.
- Making products agent-friendly means exposing structured APIs and JSON catalogs, not better web UIs.

## Tools mentioned
Stripe shared payment tokens, Stripe Payment Intents, Stripe Issuing, Machine payments protocol (with Tempo), Agentic Commerce Protocol (with OpenAI), curl (demo), Tempo blockchain (pathUSD), Base

## Relevance to our work
- **agentos** (2/3): Govrix Scout already has budgets and an L1 proxy. This talk's model of seller/amount/time-scoped delegated credentials enforced outside the model is a concrete pattern for budget enforcement and per-target spend limits. → *Extend the L1 budget design so each agent credential carries a cap, currency, expiry and target scope enforced at the proxy, and log every use to the audit trail. Read the Stripe shared payment token design as the reference.*
- **prosharness** (1/3): ProsHarness has phone-driven approvals and zero-token credential handling. The talk's rule of keeping money-moving steps deterministic and outside the model loop applies to any paid action in a harness run. → *Consider adding a spend-cap check in the approval path before any paid tool call, enforced by the harness rather than by the model's prompt.*

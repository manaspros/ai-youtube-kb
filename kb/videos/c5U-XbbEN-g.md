# How AI Agents Pay: Checkout in ChatGPT and Google AI Mode — Sam Parsons, PayPal

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `c5U-XbbEN-g` · [watch](https://youtu.be/c5U-XbbEN-g) · **date:** 2026-10-06 · **length:** 14:52 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Sam Parsons · **orgs:** PayPal, Braintree, OpenAI, Google, Anthropic
- **topics:** mcp-and-tools, product-ux, security-guardrails · **tags:** agentic-commerce, payments, tokenization, mcp-apps, agentic-commerce-protocol, universal-commerce-protocol, checkout, connectors

> PayPal Enterprise Payments (Braintree) walks through three ways merchants accept payments from AI agents: ChatGPT instant checkout, Google AI Mode via UCP, and MCP apps with external checkout.

## Summary
Sam Parsons of PayPal Enterprise Payments (formerly Braintree) explains how merchants can take payments initiated inside AI agents, with or without a human in the loop. He covers three paths: ChatGPT instant checkout using OpenAI's Agentic Commerce Protocol, Google AI Mode using the Universal Commerce Protocol, and MCP apps that hand off to an external checkout page. The core argument is that PayPal sits behind all three, so merchants keep receiving the same kind of token they already process, and settlement, refunds, chargebacks and compliance stay unchanged. The tokenization step happens in the host app, so the merchant never handles raw card data. Payment tokens are constrained to one merchant, a maximum amount, a currency and an expiry, and are attributed to the source agent. The talk is short and mostly a product walkthrough, but it does explain the integration points concretely. It gives no benchmarks or adoption figures.

## Key ideas
- **ACP (OpenAI) and UCP (Google) are nearly identical specs, and PayPal integrates with both** — Speaker says the two protocols look almost the same when you read the specs and that the space is early. PayPal positions itself as the payment bridge behind both. ([1:06](https://youtu.be/c5U-XbbEN-g?t=66))
- **The host app tokenizes the card, not the merchant** — In ChatGPT checkout, the card is entered in the host's checkout UI and exchanged for a token with PayPal. The merchant only receives the token, which keeps it out of PCI scope. ([6:01](https://youtu.be/c5U-XbbEN-g?t=361))
- **Payment tokens are tightly constrained** — Each token is bound to one merchant, a maximum dollar amount, a currency and an expiry. Transactions are attributed to the source agent (for example ChatGPT) in PayPal's reporting. ([7:29](https://youtu.be/c5U-XbbEN-g?t=449))
- **Merchant back-office flow stays the same** — Whatever the path, the merchant processes the token as a normal PayPal token, so settlements, refunds, chargebacks and compliance are unchanged. ([3:32](https://youtu.be/c5U-XbbEN-g?t=212))
- **Google AI Mode needs endpoints, not a UI** — In UCP the merchant publishes products and checkout endpoints, and a well-known JSON file declares the processor (PayPal/Braintree) plus public merchant ID and client key. Google calls the complete-checkout endpoint with a session ID and gets a Google Pay token back. ([9:00](https://youtu.be/c5U-XbbEN-g?t=540))
- **MCP apps trade friction for merchant control** — The merchant builds the product card and checkout UI in an MCP app widget. Checkout opens an external page, so the user gets any payment method, and the widget updates automatically when the order completes. The cost is an extra handoff step. ([11:49](https://youtu.be/c5U-XbbEN-g?t=709))
- **MCP app elicitation is not yet widely supported** — Speaker notes an upcoming MCP Apps feature called elicitation, which would allow requesting external validation inside an iframe. Most major hosts do not support it yet. ([12:52](https://youtu.be/c5U-XbbEN-g?t=772))

## Techniques
- **Host-side tokenization with scoped payment tokens** — The agent host collects the raw credential and exchanges it for a token with the processor. The merchant receives only that token and charges it. The token is bound to one merchant, an amount cap, a currency and an expiry, and is tagged with its origin. *When:* When an agent can trigger a purchase but should never hold or pass around raw card data, and you want the spend authority narrowly scoped.
- **MCP app widget that triggers host-native checkout** — The MCP app renders the merchant's UI and calls a JS hook that starts the host's checkout. The host then calls the merchant's MCP server complete-checkout tool with the token. *When:* In a host like ChatGPT where the merchant wants custom discovery UI but the host should own payment entry.
- **Discovery file plus session endpoints for headless checkout** — Publish a well-known JSON file that names the processor and public identifiers. Implement product and checkout-session endpoints. The platform creates a session per user and calls complete with a session ID and token. *When:* When the merchant does not want to build any UI and an agent platform provides the shopping surface.
- **External checkout handoff linked to a session** — Open the merchant's own checkout page in a new window, tie it to a session ID, and push the order status back to the MCP app widget when it completes. *When:* When the merchant needs full control of the payment flow or wants payment methods the host does not support.

## Hot takes
- OpenAI's ACP and Google's UCP are almost identical in their specs (1:06).
- Merchants can keep their existing token-processing pipeline and do not need to change anything for agent payments (3:32).
- The speaker says the agentic payments space is early and expects much more to arrive over the next year (1:06).

## Tools mentioned
MCP Apps, Agentic Commerce Protocol (ACP), Universal Commerce Protocol (UCP), Google Pay, Braintree / PayPal Enterprise Payments, ChatGPT, Claude connectors, Goose

## Relevance to our work
- **agentos** (1/3): The constrained-token model (single merchant, amount cap, currency, expiry, source attribution) is a concrete pattern for scoping agent spend. It is adjacent to AgentOS budgets in the L1 proxy but not a direct change. → *When designing per-agent budgets in the L1 proxy, consider issuing grants with a merchant or tool scope, an amount cap and an expiry, as described at 7:29.*
- **prosharness** (1/3): Host-side tokenization, where the agent only sees a scoped token and never the raw credential, is close to ProsHarness's zero-token credential handling. → *Compare ProsHarness's zero-token credential handling with the host-side tokenization pattern at 6:01, and check whether issued credentials should also carry scope and expiry.*

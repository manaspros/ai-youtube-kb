# Reverse-Engineering the AI Buyer — Aliisa Rosenthal, Acrew Capital

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `wdTRsfw0KG0` · [watch](https://youtu.be/wdTRsfw0KG0) · **date:** 2026-09-18 · **length:** 19:10 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Aliisa Rosenthal · **orgs:** OpenAI, Acrew Capital, Clay, Nooks, Microsoft, Google, Anthropic
- **topics:** product-ux, enterprise-adoption, governance-compliance · **tags:** go-to-market, self-serve, pricing, pilots, POC, security-reviews, trust-portal, sales-hiring, forward-deployed-engineers, design-partners, usage-based-pricing, spend-caps

> A former OpenAI go-to-market leader on building automated sales machinery before hiring humans, launching self-serve first, avoiding pilots, and pricing usage instead of seats.

## Summary
The speaker, who grew OpenAI's go-to-market organization from a self-serve API to multi-billion-dollar enterprise revenue, argues that founders should automate their sales machine first and add humans only where the bottlenecks are. Her OpenAI story: enterprise features shipped about nine months after ChatGPT's launch, the enterprise product was priced very high, and a self-serve tier launched four months later and cannibalized the enterprise business. She recommends launching self-serve first, responding to every inbound lead even with a holding email, and collecting detailed sign-up data. She advises against pilots, offering time-boxed opt-out contracts, customer references, or demos on customer data instead. She says security reviews should move to self-serve trust portals with automated questionnaires, and that per-seat pricing with usage billing and spend caps lowered the barrier to adoption. Hiring should come later, starting with AI-native sellers, with in-person dinners and events for buyers, and forward-deployed engineers are useful but hard to hire. The Q&A reinforces that POCs differ from self-serve PLG access.

## Key ideas
- **Build the automated machine before hiring the team** — Her advice to founders is to start with what can be automated in today's GTM tools, find the bottlenecks, and only then add humans to clear them. This reverses the traditional approach of hiring a big sales team first. ([1:20](https://youtu.be/wdTRsfw0KG0?t=80))
- **Launch self-serve before enterprise** — OpenAI shipped an expensive enterprise tier first, then a self-serve tier four months later. Self-serve grew much faster and cannibalized enterprise sales, which frustrated reps. For later products, OpenAI launched self-serve first and added humans where needed. ([2:47](https://youtu.be/wdTRsfw0KG0?t=167))
- **Respond to every inbound lead and capture detailed information** — With about 10,000 inbound leads a day and a small team, she could not respond to everyone and wishes she had sent holding emails. She also says sign-up forms should collect more detail, such as an optional phone number, to support later follow-up by humans or AI. ([3:59](https://youtu.be/wdTRsfw0KG0?t=239))
- **Make it easy for buyers and avoid pilots** — Do not send buyers away with homework. Keep pricing simple and paperwork fast. Pilots drain resources and restart the sales cycle, so they should be the exception for the largest opportunities only. ([6:08](https://youtu.be/wdTRsfw0KG0?t=368))
- **Ways to avoid a pilot without losing the deal** — Offer an introduction to another customer, an eval on part of the buyer's data, a custom-data demo over Zoom, a sign-contract-with-90-day-opt-out clause, or a one-year proof of concept instead of a three-year contract. The opt-out shifts the burden of validation to the buyer. ([7:26](https://youtu.be/wdTRsfw0KG0?t=446))
- **Automate security reviews through trust portals** — Security is where deals stall. Use self-serve trust portals for auto-signed NDAs, pen-test documents, and AI-filled questionnaires. Push back on two-hour security calls and ask buyers to come back with specific gaps. ([8:29](https://youtu.be/wdTRsfw0KG0?t=509))
- **Price for adoption: license plus usage, not seats or cost-plus** — OpenAI initially priced ChatGPT Enterprise by its own serving cost at $60 per user per month, which was too high compared with competitors. Moving to a low license fee plus usage billing lowered the barrier, and companies expanded to whole organizations. Spend caps at org or employee level reassure buyers even if rarely used. ([8:29](https://youtu.be/wdTRsfw0KG0?t=509))
- **Hire humans later, and pick AI-native sellers and the first enterprise customers carefully** — Avoid moving upmarket too early, since one large customer can absorb legal, security, product, and engineering resources. When hiring sellers, look for AI-native people who believe in the product. Buyers increasingly want in-person time, so dinners and conference booths still matter. First sales hires can be paid mostly in equity, but enterprise sellers eventually need variable comp. ([11:01](https://youtu.be/wdTRsfw0KG0?t=661))
- **Forward-deployed engineers trade hiring cost for stickiness** — Her ideal is a product that needs no forward-deployed engineers, but they are hard to hire today. The customized integration they build makes customers very sticky. ([16:16](https://youtu.be/wdTRsfw0KG0?t=976))
- **Design partners: choose carefully and use internal, non-production work** — For the first customers, choose design partners who understand the product is early. One tactic is working on a well-known company's internal or non-production product, where they accept more risk and bypass some security processes. That gives you a logo to open bigger deals. ([17:32](https://youtu.be/wdTRsfw0KG0?t=1052))

## Techniques
- **Automation-first go-to-market build-out** — Map the full sales motion (lead capture, outbound research and sequencing, demos, security, contracting). Automate each step with tools, find where it breaks, and hire people only for the remaining bottlenecks. *When:* Early-stage company or new product line, before a large sales team is hired.
- **Self-serve first, then sales-assisted** — Launch a self-serve tier, listen to what users ask for beyond it, then add a higher-priced enterprise offering and a sales team. Gate or time-box the free tier with consumption limits or feature gates to build a product-led funnel. *When:* A product where some buyers want to self-serve and enterprise features would otherwise come first.
- **Pilot alternatives that keep control of the deal** — Replace open-ended pilots with an introduction to a reference customer, an eval on the buyer's data, a demo on their data over video, a time-boxed opt-out clause (for example, 90 days), or a one-year proof of concept in place of a multi-year contract. *When:* A buyer insists on a POC or pilot, especially a startup with a leverage problem and a long sales cycle.
- **Trust portal and automated security review** — Publish a self-serve trust portal with auto-signed NDA, pen-test reports, and security documentation. Use AI to fill out security questionnaires. Ask buyers to list specific gaps, then schedule a call only for those gaps. *When:* Enterprise deals where security review slows or stalls the cycle.
- **Usage-based pricing with spend controls** — Charge a low license fee plus usage, not a high per-seat price. Offer a spend dashboard, a monthly org-level spend cap, and per-employee caps so buyers can accept a low entry point. *When:* AI products where cost per seat is a barrier to broad adoption and buyers worry about runaway usage.
- **Design partner on non-production internal product** — Pick a well-known company's internal or non-production workload as the first deployment. Accept more risk and skip some security steps, then use the logo to win larger deals. *When:* The first handful of customers, when the product is early and a logo is needed.

## Numbers
- About 10,000 inbound leads a day, handled by the speaker and four sales reps, before automation was in place ([3:59](https://youtu.be/wdTRsfw0KG0?t=239))
- Self-serve launched in January 2024, about four months after the enterprise version, and grew faster than enterprise, which it cannibalized ([2:47](https://youtu.be/wdTRsfw0KG0?t=167))
- Enterprise features were built about nine months after the ChatGPT launch in late 2022 ([1:20](https://youtu.be/wdTRsfw0KG0?t=80))
- ChatGPT Enterprise initially priced at $60 per user per month, set from serving cost, and later lowered and moved to license plus usage ([8:29](https://youtu.be/wdTRsfw0KG0?t=509))
- Suggested opt-out clause of 90 days in place of pilots, and a one-year POC in place of a standard three-year contract ([7:26](https://youtu.be/wdTRsfw0KG0?t=446))
- She cites roughly 55,000 open job postings for forward-deployed engineers and about 5,000 people qualified for the role (speaker's rough figure) ([16:16](https://youtu.be/wdTRsfw0KG0?t=976))
- At OpenAI, the speaker joined when the business had a couple of million dollars in revenue and grew it to several billion in enterprise revenue, with several hundred people in her organization ([0:08](https://youtu.be/wdTRsfw0KG0?t=8))

## Hot takes
- Build the automated machine before you hire the sales team.
- Avoid pilots at all costs; they drain resources and restart the sales cycle.
- Seat-based pricing is out; license plus usage pricing lowers the barrier to adoption.
- Avoid moving upmarket for as long as possible, because one big enterprise customer can take over the company's resources.
- Launch self-serve first, even for enterprise products.

## Tools mentioned
Clay, Nooks, Microsoft Copilot, ChatGPT Enterprise

## Relevance to our work
- **agentos** (1/3): Its L1 budgets are per-org or per-tenant. The talk notes that buyers mainly want to see a visible spend cap, even if they rarely hit it, which is a product-facing point about budget controls. → *Check whether AgentOS budgets have a visible per-user or per-team cap and a dashboard view, since the talk says buyers respond to visible caps even when they are not reached.*
- **general** (1/3): Useful background on how AI tools are sold at scale, including self-serve versus sales-led motion and usage-based pricing. It is practitioner context, not technical. → *Read the pricing and self-serve sections before designing usage-based tiers for any AI product.*

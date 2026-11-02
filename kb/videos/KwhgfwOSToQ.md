# Forward Deployed Engineering 101 — Kevin Bai, Anthropic, ex Palantir & Rippling Founding FDE

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `KwhgfwOSToQ` · [watch](https://youtu.be/KwhgfwOSToQ) · **date:** 2026-08-18 · **length:** 17:48 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Kevin Bai · **orgs:** Anthropic, Palantir, Rippling
- **topics:** product-ux, enterprise-adoption · **tags:** forward-deployed-engineering, fde, go-to-market, palantir-foundry, shared-primitives, customer-facing-engineering, design-partnership, enterprise-sales

> Kevin Bai (Anthropic, ex-Palantir and Rippling) explains the forward deployed engineer role: when to use it, why it needs a shared platform, and how to scope bespoke versus generalizable work.

## Summary
Kevin Bai introduces forward deployed engineering (FDE) as a go-to-market model in which engineers sit with customers and build on a shared platform. He traces it to Palantir, which sold Foundry as both software and an outcome delivered by embedded engineers, because Fortune 500 buyers often lacked the engineering depth to use a technical platform. He frames FDE as a scaled-up design partnership and warns that building fully custom per customer turns an FDE team into a dev shop with unmaintainable code. His decision test is whether you must sell something technical to a non-technical buyer and whether you have, or will build, a platform of shared primitives. He argues that agentic software makes every platform customizable, so customer implementation now determines vendor success. He closes with guidance to keep bespoke work per customer, generalize what repeats, use FDEs to scout product gaps, and staff projects with two engineers. The talk is high level and business-focused, with few engineering details.

## Key ideas
- **FDE sells an outcome, not software or services alone** — Palantir combined product and embedded engineers so the customer buys a result. Selling only the platform leaves the customer to train staff before any value shows up. ([2:57](https://youtu.be/KwhgfwOSToQ?t=177))
- **FDE fits a narrow case: a technical product sold to a non-technical buyer** — Dev-tool vendors selling to engineers, and configurable SaaS sold to non-technical buyers, do not need FDEs. DevRel or a sales-led motion fits those better. ([3:50](https://youtu.be/KwhgfwOSToQ?t=230))
- **Enterprise FDE is a design partnership scaled up** — Startups use design partnerships to find product-market fit. FDE applies the same close, customer-specific work to large enterprises. ([7:08](https://youtu.be/KwhgfwOSToQ?t=428))
- **Without a platform of shared primitives, FDE is just a dev shop** — If each FDE writes software from scratch, maintenance costs and code sprawl grow until they overwhelm the business. The FDE model depends on building on reusable components. ([8:17](https://youtu.be/KwhgfwOSToQ?t=497))
- **Two questions to ask before adopting FDE** — Do you truly need to sell something complicated to a non-technical buyer? And do you have, or are you willing to build, a platform the FDEs can build on? ([9:20](https://youtu.be/KwhgfwOSToQ?t=560))
- **Agentic platforms make customer implementation the main risk** — Because nearly every platform is now customizable, customers often do not know what the vendor does. Leaving success to their implementation ability makes upmarket or horizontal expansion harder. ([12:10](https://youtu.be/KwhgfwOSToQ?t=730))
- **Keep bespoke work per customer and generalize what repeats** — Anything unique to one customer stays with that customer. Anything reusable should move into the product over time. FDEs also scout for new product services. ([16:17](https://youtu.be/KwhgfwOSToQ?t=977))

## Techniques
- **FDE fit test before adoption** — Ask whether the product is technically complex, the buyer is non-technical, and a shared platform exists or will be built. If any answer is no, use DevRel, a sales-led motion, or a self-serve approach. *When:* Deciding whether a go-to-market model needs embedded engineers at all.
- **Bespoke vs generalizable split** — Build customer-unique logic only for that customer. Promote repeated patterns into shared primitives over time, and treat FDE engagements as a way to find which primitives are needed. *When:* Running custom customer projects on top of a common platform so the codebase stays maintainable.
- **Two engineers per customer project** — Staff custom work with at least two people who share context, so one person leaving or going on vacation does not stall the engagement. *When:* Long-running bespoke customer deployments where knowledge would otherwise sit with one person.
- **Granularity of primitives matched to user base** — Give broad primitives where most of the app (around 60%) is shared and customers customize the rest, and offer fine-grained tooling only for industries that need it. The AWS example shows broad primitives for a wide customer base. *When:* Designing the shared layer of a platform for a specific set of customers.

## Numbers
- Palantir average contract value (ACV) about $4M per customer, first among public SaaS companies with Fortune 500 customers (last checked by the speaker) ([6:05](https://youtu.be/KwhgfwOSToQ?t=365))
- ServiceNow about $1.2M ACV, Workday about $600K ACV ([6:05](https://youtu.be/KwhgfwOSToQ?t=365))
- No public SaaS company in the Fortune 500 set reaches even $500K ACV ([6:05](https://youtu.be/KwhgfwOSToQ?t=365))
- Speaker's Rippling FDE team grew from one person to about 25 in a year ([0:16](https://youtu.be/KwhgfwOSToQ?t=16))
- Palantir came to market around 2004-2005 (speaker's recollection) ([10:45](https://youtu.be/KwhgfwOSToQ?t=645))

## Hot takes
- Without a shared platform, an FDE function is just a dev shop, even if it is profitable.
- Most companies do not need an FDE function; DevRel or a sales-led motion is usually the right choice.
- Agentic platforms make customer implementation, not the product, the main risk to vendor success.

## Tools mentioned
Palantir Foundry

## Relevance to our work
- **agentos** (1/3): Speaker's rule of generalizing repeated customer work into shared primitives is a platform design principle, but the talk is about enterprise GTM, not infrastructure. → *When deciding which per-user AgentOS features belong in shared layers, apply the bespoke-vs-generalizable split and keep one-off logic out of core primitives.*
- **general** (1/3): Useful framing for anyone deciding whether an embedded-engineer or custom-deployment model fits their product, with a clear two-question test. → *Read for the two-question FDE fit test when deciding how to take a technical agent product to enterprise buyers.*

# Why 80% Reliability Isn't Good Enough — Felipe Blanes, Amazon AGI Lab

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Emo5FGGY-wM` · [watch](https://youtu.be/Emo5FGGY-wM) · **date:** 2026-10-09 · **length:** 17:45 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Felipe Blanes · **orgs:** Amazon AGI Lab, Amazon Web Services, Hertz, Amazon Leo, Sola
- **topics:** evals, product-ux, observability · **tags:** eval flywheel, benchmark illusion, static evals, customer trust, reliability threshold, browser agents, Nova Act, transparency, customer enablement, trajectory caching, production signals

> Amazon AGI Lab's Felipe Blanes on why static evals fail in production: run an eval flywheel fed by real customer signals, and be transparent about product limits, since trust rises more from honesty than from higher benchmark scores.

## Summary
Felipe Blanes, who runs customer enablement at the Amazon AGI Lab, reports on a year of shipping Nova Act, a browser-agent tool, from research preview (March) through a developer-experience overhaul (July) to AWS general availability (December). He names the "benchmark illusion": static public or synthetic evals look good, but production customers do things the evals never covered. His answer is an eval flywheel: define success from the customer's view, capture signals from instrumentation plus direct conversations, sort gaps into model, harness/engineering, and product buckets, then feed decisions and repeat. He describes four customer-journey stages (use-case discovery, early-adopter exploration, hero use case at scale, product gaps) and argues that reliability is perceived as binary: 80% reads as untrustworthy because customers still monitor and fix failures, while about 92% lets them hand over a workflow. He also argues that stating what the product cannot do builds more trust than higher benchmark numbers. Customer examples (Amazon Leo trajectory caching with fallback to the model, Hertz QA automation needing a non-technical interface, Sola RPA needing actuation customization) show how real use diverges from the design. The talk ends with four principles and the claim that evals must be refreshed every week or they go stale. Content is practitioner-level but short on hard numbers beyond the reliability thresholds.

## Key ideas
- **Static evals (public benchmarks and synthetic data) create a "benchmark illusion": the product passes them but breaks when customers do unanticipated things.** — The speaker says teams optimize for benchmarks, ship, and then rely on hope that the evals matched real use. He frames the gap as the core problem. ([2:36](https://youtu.be/Emo5FGGY-wM?t=156))
- **Run an eval flywheel: define success from the customer's view, capture signals, diagnose gaps, decide, and repeat.** — Success is what the customer thinks it is, not what the team assumes. Instrumentation alone misses the problem, so conversations with customers are a required signal source. Gaps are sorted into model, engineering/harness, and product buckets before prioritization. ([4:01](https://youtu.be/Emo5FGGY-wM?t=241))
- **Perceived reliability has a cliff: 80% is seen as untrustworthy, while about 92% lets customers hand over whole workflows.** — At 80% customers keep monitoring and doing manual cleanup, so the agent adds work. At around 92% they trust it with their tasks. The speaker calls reliability close to binary from the customer's side. ([9:34](https://youtu.be/Emo5FGGY-wM?t=574))
- **Transparency about limits builds more trust than higher benchmark scores.** — Tell customers three things: what works and at what reliability, what is being improved, and what is out of scope. Hiding a failing feature risks customers leaving for another tool. ([10:59](https://youtu.be/Emo5FGGY-wM?t=659))
- **Customer use evolves through stages: use-case discovery, early-adopter exploration, a hero use case at scale, then product gaps.** — Early adopters show what is possible, and their unexpected uses surface. Patterns across many customers reveal the hero use case. Gaps found along the way set the product bets. ([6:51](https://youtu.be/Emo5FGGY-wM?t=411))
- **Derive eval scenarios from production rather than imagination; synthetic data is for the start only.** — Once customer signals arrive, they should feed the eval set. The speaker's four flywheel principles are: production-derived scenarios, categorized actionable areas, honest sharing of weaknesses, and running the loop as fast as possible. ([14:58](https://youtu.be/Emo5FGGY-wM?t=898))
- **Evals go stale unless they are updated every week.** — If the evals do not get smarter each week, they are no longer tracking what customers do. Customer journeys grow more complex over time, so the eval set must follow. ([16:29](https://youtu.be/Emo5FGGY-wM?t=989))

## Techniques
- **Eval flywheel with customer signals** — Define success from customer input; capture both instrumentation and direct customer conversations; categorize gaps into model (feed to evals), engineering/harness (bug fixes), and product (positioning and missing features); prioritize; repeat. *When:* Shipping an agent product where static benchmarks no longer predict production failures.
- **Trajectory caching with model fallback** — Cache successful agent trajectories and replay them; if a cached run fails, fall back to live model inference. *When:* Repetitive agent tasks where per-run inference cost dominates, as with the Amazon Leo example.
- **Stated-limitations disclosure** — At onboarding, list what the product does reliably, what is being improved, and what is out of scope. *When:* Selling an agent product to enterprise customers, to avoid trust loss from undisclosed failures.
- **Non-technical authoring layer on an agent core** — Add a UI for non-engineers on top of the script-based product once the technical users show the core works. *When:* Expanding a developer tool to QA or ops users (the Hertz example).

## Numbers
- Reliability perception threshold: 80% is seen as needing ongoing monitoring; about 92% is seen as trustworthy enough to hand over a workflow (speaker's customer-feedback claim, not a measured study). ([9:34](https://youtu.be/Emo5FGGY-wM?t=574))
- Nova Act timeline: research preview March 2025, developer experience overhaul July 2025, AWS launch December 2025. ([0:12](https://youtu.be/Emo5FGGY-wM?t=12))

## Hot takes
- Higher benchmark scores matter less for customer trust than being transparent about what the product cannot do.
- Reliability is effectively binary to customers: 80% can be worse than no product because it adds monitoring work.
- Static evals are a form of hope; eval sets that are not refreshed weekly go stale.

## Tools mentioned
Amazon Nova Act

## Relevance to our work
- **agentos** (1/3): The eval-flywheel and customer-signal loop applies to any agent platform, including AgentOS's RAGAS evals and SkillForge's idea of mining telemetry, but the talk gives no concrete tooling. → *Add a 'gap categorization' step (model / harness / product) to the AgentOS eval plan, and log which real telemetry failures feed back into the eval set.*
- **prosharness** (1/3): The stated-limits and flywheel ideas touch how ProsHarness reports unreliable checkpoint/resume runs to its users, but the talk is not about coding harnesses. → *Consider a per-run 'known limitations' field in ProsHarness run reports.*

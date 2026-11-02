# Unmasking hidden costs of microservices with Vojtech Vondra

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `nw2oVC3ycd4` · [watch](https://youtu.be/nw2oVC3ycd4) · **date:** 2024-11-02 · **length:** 9:47 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Vojtech Vondra · **orgs:** Microsoft
- **topics:** infra-cost-scaling, governance-compliance · **tags:** microservices, architecture, service-boundaries, cross-cutting-concerns, complexity, conway, retrospective, lines-of-code, interfaces

> A Microsoft identity engineer argues microservices carry hidden costs that multiply with each service, and that teams should stay small (about five services) unless they are very large.

## Summary
Vojtech Vondra, who works on Microsoft identity infrastructure, uses a retrospective on microservices to argue for keeping architectures simple. He challenges the common "microservice premium" productivity chart from Martin Fowler as hand-wavy, since complexity and productivity are hard to measure and the choice is not binary. He proposes a rough rule: let n be the number of services, and keep n at or below about five unless the organization is very large (he says over 100 engineers). The costs grow faster than n because every cross-cutting concern (audit logging, data deletion, permissions, feature flags, billing, A/B testing and so on) tends to pull in one more service. Reorgs and service boundaries become hard to reverse, and interface and communication design is the most common source of pain. He ends with the observation that services end up full of boilerplate for cross-cutting concerns rather than customer value. The talk is anecdotal and contains no benchmarks, so it is practitioner opinion rather than measured evidence.

## Key ideas
- **Microservices are worth revisiting as a retro, and the main lesson (keep it simple) applies to many other architecture trends.** — The speaker frames the talk as a retrospective on what worked and what did not, noting trend cycles run about 5 to 10 years. ([0:00](https://youtu.be/nw2oVC3ycd4?t=0))
- **The 'microservice premium' chart is hard to use as evidence.** — Axes are vague (complexity and productivity are abstract), and the chart suggests a binary choice between monolith and microservices. The speaker wants proxy metrics for complexity such as teams, engineers, products and use cases, and admits productivity is not measurable in any clean way. ([2:25](https://youtu.be/nw2oVC3ycd4?t=145))
- **Use n (the number of services) as the key quantity, and the costs multiply faster than n.** — The speaker jokes that each microservice adds n problems, and says the cost often grows faster than n. His rule of thumb: keep n at or below five unless the organization is much larger. ([3:40](https://youtu.be/nw2oVC3ycd4?t=220))
- **Reorgs and service ownership create emotional attachment, and wider architectures make the business less flexible.** — Reorgs are usually well-intended, but splitting into more services limits how fast the business can change. Teams are reluctant to hand over services they own. ([5:09](https://youtu.be/nw2oVC3ycd4?t=309))
- **Interfaces and communication between services are the most common source of trouble, and they are one-way doors.** — The speaker says these decisions are hard to reverse and will affect the system for years, so they deserve the most scrutiny. ([5:09](https://youtu.be/nw2oVC3ycd4?t=309))
- **Every cross-cutting concern pushes the architecture toward one more service.** — He lists multi-tenancy, privacy data deletion, audit logging, unified analytics, undo, point-in-time recovery, feature flags, permissions, localization, notification, search, billing and A/B testing. Each one is a reason to split off another service, which leads to a spiral. ([6:29](https://youtu.be/nw2oVC3ycd4?t=389))
- **A well-designed distributed architecture is possible but needs a lot of thought, and is likely overkill under about 100 engineers.** — The speaker says he has seen it work, but for most teams the default should be a small number of services. ([7:49](https://youtu.be/nw2oVC3ycd4?t=469))
- **Services end up dominated by boilerplate for cross-cutting concerns, not customer value.** — He describes counting lines of code in the app and infra directories of his old services, finding that most of the code was boilerplate. He concludes that code is a liability to be maintained, not an asset. ([8:53](https://youtu.be/nw2oVC3ycd4?t=533))

## Techniques
- **Count n before splitting into services** — Treat the number of services as a budget. Keep it at or below about five for a team under roughly 100 engineers, and make any proposal to go beyond that justify its own cost. *When:* When a team is debating how many services to create, or when someone proposes a new service to handle one more concern.
- **Cross-cutting concerns checklist** — Before splitting out a service, walk through the cross-cutting concerns the speaker lists (multi-tenancy, data deletion, audit logging, analytics, undo, point-in-time recovery, feature flags, permissions, localization, notifications, search, billing, A/B testing). Decide where each lives, and make sure it is not reimplemented in every service. *When:* When designing a system that could grow from one service into several, or when reviewing an architecture proposal.
- **Design interfaces and communication first** — Treat service interfaces and communication patterns as one-way doors. Spend the most design time there, and challenge every edge case before committing. *When:* When defining the boundaries between services or the contracts they expose to each other.
- **Measure boilerplate ratio** — Count lines of code in the application layer versus the infrastructure and cross-cutting layers (for example src/app and src/infra). A high share of infrastructure code is a signal that the service split is adding overhead. *When:* As an audit of an existing service-oriented codebase, to see whether splitting is paying off.

## Numbers
- Architecture trend cycles last about 5 to 10 years. ([0:00](https://youtu.be/nw2oVC3ycd4?t=0))
- Speaker's rule of thumb is that n (number of services) should be at most 5. ([3:40](https://youtu.be/nw2oVC3ycd4?t=220))
- He says a distributed service architecture is probably overkill unless the organization has more than 100 engineers. ([7:49](https://youtu.be/nw2oVC3ycd4?t=469))
- He reports a line-count audit of his old services where boilerplate and cross-cutting code dominated the codebase. No specific percentage is given. ([8:53](https://youtu.be/nw2oVC3ycd4?t=533))

## Hot takes
- The microservice premium chart is hand-wavy; complexity and productivity are too abstract to plot, and the chart implies a binary monolith-vs-microservices choice that is not real.
- Microservices cost grows faster than the service count, so most teams should stay under about five services.
- Reorgs are usually well-intended but poorly explained; wider service boundaries make a business less flexible.
- Interface and communication design is the most common source of grievances and the hardest decision to reverse.
- The talk is opinion from one practitioner with no benchmarks or measured data, so it should be weighed as experience rather than evidence.

## Tools mentioned
Azure

## Relevance to our work
- **agentos** (2/3): AgentOS is a multi-pillar stack (proxy, memory, inference, sandbox, skills, observability) spread across Postgres, TimescaleDB, Redis, Neo4j, ClickHouse and DuckDB. The talk's n-services and cross-cutting cost argument maps directly onto whether each pillar should be its own service or a module. → *Count the services and data stores in AgentOS against the n<=5 rule, and list which cross-cutting concerns (audit, PII scan, budgets, permissions) are duplicated per service.*
- **prosharness** (1/3): Checkpoint/resume is a form of the point-in-time recovery concern the speaker lists, and it should live in one module rather than being reimplemented per loop or schedule. → *Keep checkpoint/resume as a single module used by all loops and schedules, not something each loop reimplements.*

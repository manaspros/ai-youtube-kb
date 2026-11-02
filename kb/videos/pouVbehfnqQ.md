# SLAs, SLOs, and SLIs EXPLAINED in 7 Minutes (2025)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `pouVbehfnqQ` · [watch](https://youtu.be/pouVbehfnqQ) · **date:** 2025-11-02 · **length:** 7:13 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed Better Stack host · **orgs:** Better Stack, AWS, Amazon, Google, Microsoft
- **topics:** observability, infra-cost-scaling · **tags:** sla, slo, sli, reliability, uptime, monitoring, availability, concepts

> Beginner explainer distinguishing SLAs (customer contracts with penalties), SLOs (internal targets) and SLIs (measured metrics), using a rice-farmer analogy and AWS EC2 uptime math. Main takeaway: derive SLOs from measured SLIs and monitor your own services rather than trusting vendor status pages.

## Summary
The host defines three reliability terms. An SLA (service level agreement) is a legal promise to a customer covering services, availability and response times, plus penalties for missing them. An SLO (service level objective) is an internal target, usually with a range, that the company sets to meet the customer's expectations and can be made public through the SLA. An SLI (service level indicator) is the measured actual performance, such as request counts, latency and failures per request, aggregated over time. The video uses a fictional rice farmer and sushi restaurant to show that the SLI history comes first, the SLO is set from it, and the SLA sits looser than the SLO. It then works through the arithmetic of an AWS EC2 99.5% monthly uptime commitment, where a 30-day month is 43,200 minutes. The host closes by saying providers' internal SLIs may show lower uptime than their public status pages, so users should monitor their own services. The content is introductory and contains no benchmarks, code or implementation detail.

## Key ideas
- **An SLA is a customer-facing legal promise covering services, availability and response times, with penalties (credits or refunds) when missed.** — Example given is an AWS EC2 commitment of more than 99.5% uptime, with partial credit between 99.0% and 99.5%. The host also claims sites below 95% monthly uptime can recover all their money, but gives no source for that figure. ([0:00](https://youtu.be/pouVbehfnqQ?t=0))
- **Monthly uptime percentages convert to a downtime budget in minutes.** — A 30-day month has 43,200 minutes. The host's downtime example of 0.6% equals 259.2 minutes, about 4h20m. The arithmetic is correct, but it sits beside a 99.5% target that implies a different downtime figure, so the example is not fully reconciled. ([2:45](https://youtu.be/pouVbehfnqQ?t=165))
- **An SLO is an internal reliability target with a range, and it can be published through an SLA.** — In the rice example the internal SLO is 95-100% high-quality grain, while the SLA promises a looser 90-95%. The SLO is a target the company sets for itself, and the SLA gives it room to miss internally before a customer penalty applies. ([4:10](https://youtu.be/pouVbehfnqQ?t=250))
- **An SLI is the measured actual performance, and the SLO has to be derived from it.** — The farmer measured quality for months before knowing what he could consistently hit. Without that history you cannot choose a sensible SLO. SLIs for services are aggregates such as request counts, latency and failures per request. ([4:10](https://youtu.be/pouVbehfnqQ?t=250))
- **SLIs keep being measured after the SLO is set.** — The farmer keeps checking each bag against his internal SLO. The host says SLIs and SLOs stay internal, so a provider's real uptime may be lower than its status page reports, which is the reason to monitor your own dependencies. ([5:36](https://youtu.be/pouVbehfnqQ?t=336))

## Techniques
- **Derive the SLO from measured SLI history** — Record the SLI (for example, success rate or quality per unit) over many periods first. Set the SLO at a level you have consistently achieved, not at an aspirational number. *When:* Before setting any reliability target, especially before promising it to customers.
- **Keep the internal SLO stricter than the external SLA** — Publish the SLA with a looser bound than the internal SLO, so that normal variation still leaves the external promise met and the penalty only applies to real misses. *When:* Writing a customer-facing SLA with penalties or credits.
- **Turn an uptime percentage into a minute budget** — Minutes allowed down = days x 24 x 60 x (1 - target). The host uses 30 days, which gives 43,200 minutes per month, then multiplies by the downtime fraction. *When:* Translating an SLA or SLO percentage into an operational or alerting budget.
- **Monitor your own endpoints, not only the vendor status page** — Run independent checks against the services you depend on and track their success and latency yourself, keeping your own SLI records for disputes. *When:* Depending on a cloud or SaaS provider whose SLA would pay you a credit if it failed.

## Numbers
- Claimed refund threshold: sites under 95% monthly uptime on AWS can get all their money back (speaker's hook, unsourced, and inconsistent with the 99.5% EC2 example). ([0:00](https://youtu.be/pouVbehfnqQ?t=0))
- EC2 commitment example: more than 99.5% monthly uptime, partial credit between 99.0% and 99.5%. ([0:00](https://youtu.be/pouVbehfnqQ?t=0))
- A 30-day month has 43,200 minutes (30 x 24 x 60). ([2:45](https://youtu.be/pouVbehfnqQ?t=165))
- Downtime of 0.6% of a 30-day month = 259.2 minutes, about 4 hours 20 minutes. ([2:45](https://youtu.be/pouVbehfnqQ?t=165))
- Rice example: $400/month fee, a missed day is compensated with two bags the next day, and a bag under 90% quality earns $10 off the next bill. ([1:22](https://youtu.be/pouVbehfnqQ?t=82))

## Hot takes
- The opening refund claim (below 95% uptime means all your money back) is unsourced and conflicts with the 99.5% EC2 example in the same video. Treat it as a hook and check the actual SLA text.
- The downtime example mixes a 99.5% target with a 0.6% downtime figure, and the host does not reconcile them. The arithmetic is right; the link between the two is not.
- The claim that providers' real uptime may be lower than their status page is plausible but unsupported by any data in the video.
- Content is intro-level: definitions and analogy only, with no implementation, tooling, or how-to for setting SLIs in a real system.

## Tools mentioned
AWS, Amazon EC2

## Relevance to our work
- **agentos** (1/3): L4 observability and the next-phase goal of proving AgentOS as a distributed system fit the SLI/SLO vocabulary. The video adds no new technique beyond that. → *Use the SLI/SLO split to frame AgentOS L4 benchmarks: record proxy latency and failure SLIs first, then set SLO targets from that measured history.*

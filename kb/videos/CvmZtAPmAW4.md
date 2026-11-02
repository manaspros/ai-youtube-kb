# 78% Wanted This AI Feature. Almost Nobody Used It - Supriya Subudhi, Bumble

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `CvmZtAPmAW4` · [watch](https://youtu.be/CvmZtAPmAW4) · **date:** 2026-10-31 · **length:** 14:44 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Supriya Subudhi · **orgs:** Bumble, Spotify, Amazon, Meta
- **topics:** evals, product-ux, token-cost-efficiency, governance-compliance · **tags:** ab-testing, product-management, guardrails, long-tail-evals, model-cost, regulatory-compliance, consumer-ai, dating-app

> Bumble's Supriya Subudhi argues that a positive A/B test is only the start for AI features, and lays out five checks: real adoption, tail-of-distribution outputs, cost versus benefit, model cost-quality tradeoffs, and legal market readiness.

## Summary
A Bumble product manager describes shipping an AI photo-feedback feature for dating profiles. The A/B test showed strong survey interest (about 78%) but only 10-15% actual usage, so the team moved the prompt into existing user journeys. Averages hid bad tail outputs (e.g. telling smiling users to smile more), which pushed them to inspect segment-level outputs with evals and to set guardrails on what the AI may suggest. The best model was roughly 10x costlier, and the cheaper model lost accuracy, so they tested models and prompts with evals and shipped the cheapest option that still worked. Finally, a US-only launch hit regulatory limits, so compliance has to be considered early. The talk is a practitioner experience report, not a benchmark study, and the evidence is one feature at one company.

## Key ideas
- **A positive A/B test is where the journey starts, not where it ends, for GenAI features.** — The speaker says a win on the average metric is not enough to ship an LLM feature. Five checks follow from this. ([1:06](https://youtu.be/CvmZtAPmAW4?t=66))
- **Stated interest does not predict usage.** — About 78% of surveyed users wanted AI feedback, but the A/B test (50/50) showed only 10-15% of the treatment group used it. Their conclusion is that openness to AI does not predict adoption. ([3:22](https://youtu.be/CvmZtAPmAW4?t=202))
- **Embed the AI feature in existing user journeys rather than a standalone feature.** — Instead of a discoverable standalone screen, prompts appeared at the points where users were already working (adding photos, hitting no matches). This raised adoption. Measuring usage is the foundation for improving it. ([3:22](https://youtu.be/CvmZtAPmAW4?t=202))
- **Averages hide tail failures, so read the outputs in the segments.** — The overall lift was positive, but the feedback sometimes told users to smile when they already were. The success criteria shifted to per-segment outcomes (gender, language and country) and to reading real outputs through eval tooling. ([4:47](https://youtu.be/CvmZtAPmAW4?t=287))
- **Set explicit guardrails on what the AI may recommend, scaled to the cost of an error.** — A wrong song in a playlist is tolerable, but wrong budget advice is not. The team banned suggestions the user cannot control, such as skin color or height. ([5:49](https://youtu.be/CvmZtAPmAW4?t=349))
- **The GenAI cost curve grows with usage, unlike classic ML.** — Classic ML has high upfront compute and training cost with small marginal cost per user. With GenAI, a more successful feature means a higher bill per use. The team's first choice, the best LLM, was about 10x more expensive than a simpler approach before eval costs. ([7:17](https://youtu.be/CvmZtAPmAW4?t=437))
- **Cheaper models lowered accuracy and also the A/B result, so the model under test confounded the feature test.** — After switching to a cheaper model, results dropped, which showed the earlier result came from the model rather than the feedback concept. They used evals to compare models and prompts quickly against cost, and shipped the cheapest option that still worked. ([10:00](https://youtu.be/CvmZtAPmAW4?t=600))
- **Ask why you are using AI, since that sets the budget: short-term ROI or long-term brand equity.** — Her example is an Amazon shopping assistant, which may justify cost through long-term loyalty rather than immediate purchases. ([9:00](https://youtu.be/CvmZtAPmAW4?t=540))
- **Compliance and legal limits need to be considered at the start, not after building.** — Meta's Muse AI was US and Canada only. The team shipped in the US and then could not carry the same feature abroad. Options range from designing for all markets upfront to shipping in one market first. ([11:16](https://youtu.be/CvmZtAPmAW4?t=676))

## Techniques
- **Adoption-first AI feature rollout** — Attach the AI prompt to moments in an existing user journey (e.g. when adding photos or when matches dry up) instead of a standalone entry point. Instrument actual usage in the A/B test, not only survey interest. *When:* Shipping an LLM feature where users say they want it but may not discover or use it.
- **Segment-level eval review over averages** — Use eval tooling to read real model outputs, then break success metrics down by user segment (gender, language, country) and look for tail-of-distribution failures such as contradictory advice. *When:* A/B results are positive on average but you suspect the feature is wrong for some users.
- **Guardrails on advice scope** — Write explicit rules about what the generated output may and may not suggest (e.g. do not suggest changes to attributes the user cannot change). Scale strictness to the cost of a bad output. *When:* Generated advice can affect a user's money, safety or self-image.
- **Eval-driven model and prompt selection under a cost budget** — Compare candidate models and prompt versions on cost and accuracy with evals on the same dataset, and pick the cheapest one that holds quality. Retest prompts quickly as models change. *When:* The best model is too expensive to scale, but a cheaper one changes quality.
- **Write down the business reason for each AI feature** — Classify the feature as a short-term ROI play or a long-term retention/brand play, and set the budget accordingly before choosing a model. *When:* Deciding how much to spend on inference for a feature.
- **Regulatory check before building** — Decide early which markets the feature must be legal in. Either design for the strictest regime from the start or ship in one market and accept the cost of market-specific versions. *When:* Launching AI features that face varying regional AI regulation.

## Numbers
- Bumble has over 20 million monthly active users (stated for context). ([1:06](https://youtu.be/CvmZtAPmAW4?t=66))
- About 78% of users said they wanted AI feedback in research. ([3:22](https://youtu.be/CvmZtAPmAW4?t=202))
- Only 10-15% of users in the 50/50 A/B test actually used the feature. ([3:22](https://youtu.be/CvmZtAPmAW4?t=202))
- The best LLM was about 10x more expensive than a simpler approach, before eval costs. ([7:17](https://youtu.be/CvmZtAPmAW4?t=437))

## Hot takes
- A positive A/B test on average is not sufficient evidence to ship a GenAI feature; per-segment output review is required.
- GenAI cost grows with success, unlike classic ML, so model choice is a product decision, not only an engineering one.
- Compliance and legal review belongs in early product discovery, not after the build.

## Tools mentioned
Meta Muse AI (mentioned as an example of a US/Canada-only launch), Amazon AI shopping assistant (mentioned as an example), Spotify AI DJ (mentioned as an example)

## Relevance to our work
- **agentos** (2/3): Per-segment eval review and cost-versus-quality model selection map to AgentOS evals (RAGAS) and the budget/routing pillar in Govrix Scout. → *Add per-segment (or per-tenant) breakdowns to the RAGAS eval output so that tail failures show up, not only averages.*
- **prosharness** (1/3): Cost-versus-quality model selection for cheap-model pipelines is relevant to ProsHarness routing decisions, but the talk is product-focused.

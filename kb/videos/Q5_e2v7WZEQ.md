# BREAKING: US Government BANNED Mythos and Fable

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `Q5_e2v7WZEQ` · [watch](https://youtu.be/Q5_e2v7WZEQ) · **date:** 2026-07-02 · **length:** 6:05 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed Better Stack host (not named in transcript) · **orgs:** Anthropic, US government, UK AISI, OpenAI, Department of Defense
- **topics:** governance-compliance, security-guardrails, models-research · **tags:** export-control, jailbreak, model-access, foreign-nationals, data-retention, breaking-news, model-withdrawal

> Better Stack breaking-news reaction to a reported US export-control directive that suspended Fable 5 and Mythos 5 access for foreign nationals, with Anthropic's response read out and the speaker's speculation.

## Summary
The host reports that the US government issued an export-control directive ordering Anthropic to suspend access to Fable 5 and Mythos 5 for any foreign national, and that Anthropic responded by disabling both models for all customers while leaving other Anthropic models unaffected. He reads Anthropic's statement: the government cited a reported jailbreak but gave no specifics, and Anthropic says the findings were minor, previously known vulnerabilities that other public models also find. Anthropic describes thousands of hours of safeguard red-teaming with the US government, the UK AISI and third parties, and says no universal jailbreak was found. He notes that Fable had a 30-day data retention policy, which Anthropic used to track jailbreaks. Anthropic says it is complying while disagreeing, and argues that this standard would halt frontier deployments across the industry. The host speculates about what the jailbreak was and whether the foreign-national clause could lead to identity or nationality checks. The clip is a same-day reaction, and most details are either Anthropic's own account or the host's inference.

## Key ideas
- **US export-control directive suspends foreign-national access to Fable 5 and Mythos 5, and Anthropic disables both for all customers** — The host reads Anthropic's tweet: the directive was received at 5:21pm and suspends access by any foreign national, including Anthropic's own foreign-national employees. Other Anthropic models are not affected. ([0:00](https://youtu.be/Q5_e2v7WZEQ?t=0))
- **The stated reason is a reported jailbreak with no published specifics** — Anthropic says the government did not give specific details. Its understanding is that the government found a jailbreak that lets Fable 5 find vulnerabilities in software. ([0:00](https://youtu.be/Q5_e2v7WZEQ?t=0))
- **Anthropic says the findings were minor, public-knowledge vulnerabilities** — Anthropic says the vulnerabilities were relatively simple, previously known, and findable by other publicly available models without a bypass. The host agrees that universal jailbreaks are likely to appear eventually. ([1:11](https://youtu.be/Q5_e2v7WZEQ?t=71))
- **Anthropic claims its safeguards were heavily tested before launch** — Per the statement, safeguards were tested for thousands of hours with the US government, the UK AISI, third-party organizations and internal teams. No tester found a universal jailbreak, though niche partial bypasses may exist. Anthropic says perfect jailbreak resistance is not currently possible for any provider. ([1:11](https://youtu.be/Q5_e2v7WZEQ?t=71))
- **The 30-day data retention policy was the jailbreak-monitoring mechanism** — The host says Fable's 30-day customer data retention, which blocked some users, was meant to let Anthropic track jailbreak attempts and shut them down. Anthropic says it has received no disclosure of a concerning non-universal jailbreak that caused harm. ([2:39](https://youtu.be/Q5_e2v7WZEQ?t=159))
- **Government evidence was verbal and describes a codebase-repair task that other models can also do** — Anthropic says the government gave only verbal evidence of a narrow, non-universal jailbreak: asking the model to read a codebase and fix its flaws. Anthropic says the capability is widely available, including in OpenAI's GPT 5.5, and used daily by defenders. ([3:39](https://youtu.be/Q5_e2v7WZEQ?t=219))
- **Anthropic is complying but argues the standard would halt all frontier deployments** — Anthropic says it is following the legal directive while disagreeing that a narrow potential jailbreak should justify recalling a commercial model used by hundreds of millions of people. It argues that this standard applied industry-wide would stop all new frontier model launches. ([3:39](https://youtu.be/Q5_e2v7WZEQ?t=219))
- **The host's own check and his concern about nationality-based access** — The host says Fable still responded for him when he tested it. He notes that the foreign-national clause could require users to prove their place of birth or upload ID, which he calls speculation. ([5:02](https://youtu.be/Q5_e2v7WZEQ?t=302))

## Numbers
- Government directive received at 5:21pm, about four hours before the statement ([0:00](https://youtu.be/Q5_e2v7WZEQ?t=0))
- Thousands of hours of pre-launch safeguard red-teaming (Anthropic's figure) ([1:11](https://youtu.be/Q5_e2v7WZEQ?t=71))
- Fable had a 30-day customer data retention policy ([2:39](https://youtu.be/Q5_e2v7WZEQ?t=159))
- Anthropic says the model was deployed to hundreds of millions of people ([3:39](https://youtu.be/Q5_e2v7WZEQ?t=219))
- Host says Fable 5 would have been removed from subscriptions in 11 days ([5:02](https://youtu.be/Q5_e2v7WZEQ?t=302))

## Hot takes
- Breaking-news title with thin verified detail: the jailbreak is unspecified and most of the content is Anthropic's own statement or the host's speculation, so quality is capped at 2.
- The host expects jailbreaks to be a cat-and-mouse problem and does not think perfect jailbreak resistance is achievable for any model provider.
- The host argues the foreign-national clause could lead to ID or nationality verification (speculation, not stated in the directive).
- The host thinks the government would be happy to keep the model for itself, and that a US-only or nationality-based access regime would be a worrying direction (opinion).

## Tools mentioned
Fable 5, Mythos 5, GPT 5.5 (OpenAI, named by Anthropic as having similar capability)

## Relevance to our work
- **agentos** (1/3): Model access can be withdrawn or restricted by policy with a few hours' notice, so the routing layer needs to handle a model disappearing mid-run. → *Test the strategy-routing layer with a simulated 'model disabled or access revoked' upstream error, and confirm it fails over to a configured fallback instead of failing the agent run.*

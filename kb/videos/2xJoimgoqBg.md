# Security Track Intro — Randall Degges, Snyk

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `2xJoimgoqBg` · [watch](https://youtu.be/2xJoimgoqBg) · **date:** 2026-08-18 · **length:** 4:16 · **format:** keynote · **quality:** 2/5 · **depth:** intro
- **speakers:** Randall Degges · **orgs:** Snyk, Anthropic, NVIDIA, Keycard, OpenAI
- **topics:** security-guardrails, coding-agents · **tags:** security track, agent security, secure by default, AI-generated code security, autonomous agents, World's Fair, event intro

> Snyk's Randall Degges opens the World's Fair security track: AI-written code has security bugs, autonomous agents need containment, and model access limits are a barrier to shipping fearlessly.

## Summary
Randall Degges (Snyk) gives a roughly four-minute emcee intro for the first security track at the World's Fair. He says the appeal of generative AI for him is shipping better software faster, and that security is the main obstacle to doing this at scale. He makes three points: AI-generated code has security issues just as human-written code does, so security belongs in the development lifecycle; deploying autonomous agents safely is much harder, since they must not go off the rails and harm the business or users; and geopolitics and model access (he cites Fable access being pulled and the new GPT 5.6 being unavailable to many) slow teams down. He frames the core unsolved problem as using AI fearlessly with security by default. The rest of the video is an announcement: a full-day track in room 2005 on the second floor, with presenters from NVIDIA, Anthropic, Keycard and Snyk. No techniques, benchmarks or implementation details are given.

## Key ideas
- **Security is the main obstacle to shipping AI-built software at scale** — The speaker's excitement is building better software faster with AI. He says security is what stops that from happening at scale. ([0:08](https://youtu.be/2xJoimgoqBg?t=8))
- **AI-generated code carries security issues, the same as human-written code** — He treats this as a known fact and argues it makes security a normal part of the development lifecycle, not a new concern. ([1:14](https://youtu.be/2xJoimgoqBg?t=74))
- **Containing autonomous agents in production is the harder problem** — The goal is to deploy agents so operators can 'go to sleep easily' without the agents going off the rails and harming the business or its users. He says this is much more difficult than the code-security problem. ([1:14](https://youtu.be/2xJoimgoqBg?t=74))
- **Model access restrictions are a barrier to innovation** — He cites the pulled access to Fable and the unavailable new OpenAI GPT 5.6 model as examples of geopolitical friction slowing teams down, and ties this back to security. ([1:14](https://youtu.be/2xJoimgoqBg?t=74))
- **The goal is to use AI fearlessly and be secure by default** — He calls this the biggest unsolved problem in the space and presents the track as a way to fix it. ([2:37](https://youtu.be/2xJoimgoqBg?t=157))
- **First security track at the World's Fair, a full day in room 2005** — It runs downstairs on the second floor right after the keynote. Presenters named are from NVIDIA, Anthropic, Keycard and Snyk, and the speaker is emceeing all day. ([2:37](https://youtu.be/2xJoimgoqBg?t=157))

## Hot takes
- This is an event promo with thin technical substance, so quality is capped at 2.
- Ties model-access restrictions (Fable, GPT 5.6) to security as a blocker, which is a framing claim with no evidence given.
- Auto-captions spell the speaker's company as 'Sneak'; the title confirms it is Snyk.

## Tools mentioned
Fable (AI model, access reportedly pulled; name as spoken), OpenAI GPT 5.6 (new model, speaker says it is not available to many yet)

## Relevance to our work
- **agentos** (1/3): Agent containment and secure-by-default are close to AgentOS's guardrail pillar (PII/prompt-injection scan, exec-gate guardrails, Crucible sandboxing), but the talk gives no techniques. → *Check the security track talks (room 2005) for agent containment patterns and compare them to the exec-gate guardrails and sandboxed execution in Crucible.*
- **prosharness** (1/3): Keeping autonomous agents from going off the rails is close to ProsHarness's approval and credential handling, but there is no concrete mechanism here. → *Compare ProsHarness's phone-driven approval gating with containment approaches presented in the security track.*

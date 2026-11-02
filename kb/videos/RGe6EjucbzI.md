# "The biggest challenge in your stack? Evals, Evals, Evals" - 2026 State of AI Engineering results

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `RGe6EjucbzI` · [watch](https://youtu.be/RGe6EjucbzI) · **date:** 2026-08-18 · **length:** 19:47 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Bar Yeren · **orgs:** Amplify, Notion, Vercel
- **topics:** evals, enterprise-adoption, models-research, infra-cost-scaling · **tags:** survey, state-of-ai-engineering, evals, model-routing, open-weight-models, cost, agents, write-access, human-in-the-loop, build-vs-buy, prompt-management, vibe-review

> Bar Yeren (Amplify) reads out the 2026 State of AI Engineering survey (1,048 respondents): evals remain the top challenge, teams run multi-model stacks, cost is a first-class constraint, and agents now mostly have write access.

## Summary
This is a survey readout, not an implementation talk. Bar Yeren, a partner at Amplify, summarizes the 2026 State of AI Engineering survey run with Notion and Vercel, with 1,048 respondents. The main story is that AI engineering is a discipline spanning many roles, and experienced software engineers are often new to AI. On models, nearly all teams use closed models, under half use open-weight models, and open-weight users almost always also use closed ones, so open models augment rather than replace. Most teams use more than one model, usually routing by task type, and cost has become a first-class constraint that shapes how ambitiously teams use AI. Agents are now common (95%), and most of them have write access to systems, which raises the question of how they are controlled; human approvals and permission gating are the top controls, and nobody has settled the control layer yet. Evals are still the biggest stack challenge, but only by a thin margin, and inference is the layer teams most often buy while prompts and evals stay in-house. Finally, respondents report net-positive effects but also more review burden and blurring of engineer, product and marketing roles.

## Key ideas
- **Open-weight models augment closed models rather than replace them** — 45% use open-weight models, but over 90% of those teams also use closed models. Teams mix and match. ([5:58](https://youtu.be/RGe6EjucbzI?t=358))
- **Multi-model is the norm and standardization is happening at the tool layer, not the model layer** — 87% of teams use more than one model. Routing by task type is most common, with some comparing outputs or routing by cost. More than half say their organization is standardizing on fewer AI tools. ([6:56](https://youtu.be/RGe6EjucbzI?t=416))
- **Quality, then agentic capability and cost, drive model choice; reliability is rarely the deciding factor** — Quality dominates. Tool calling ranks next, tied with cost. Only about one in five named reliability; the speaker guesses reliability is becoming a threshold requirement. ([5:58](https://youtu.be/RGe6EjucbzI?t=358))
- **Cost is now a first-class engineering constraint and is monitored like an SLA** — 40% say cost regularly shapes how ambitiously they use AI and 36% say it sometimes does. Cost and token usage is the second most-monitored item in production, right after quality. ([8:21](https://youtu.be/RGe6EjucbzI?t=501))
- **Agents have moved from reading to writing** — 95% use agents, roughly double last year. The share of agent builders whose agents can write data went from 52% to 89%, so write-enabled agents are up more than threefold across all respondents. ([9:52](https://youtu.be/RGe6EjucbzI?t=592))
- **The control layer for agents is not settled; teams use blunt tools** — The top controls are human-in-the-loop approvals and gating permissions, which the speaker compares to managing an intern. Below those, results scatter across task decomposition, retrieval, memory and sandboxing. ([11:16](https://youtu.be/RGe6EjucbzI?t=676))
- **Agent failures are usually reasoning failures, not plumbing failures** — Two-thirds say hallucination or losing context mid-task frustrates them most. ([11:16](https://youtu.be/RGe6EjucbzI?t=676))
- **Evals stay the top stack challenge, but the lead is shrinking; prompts and evals are built in-house** — Inference and model serving is the layer teams buy most. Prompt management is built in-house by 61%. Fine-tuning is the clearest case of most teams not doing it at all. ([12:14](https://youtu.be/RGe6EjucbzI?t=734))
- **Cheaper failure is the top upside of AI coding, but review burden and skill erosion are the downsides** — 97% report a net positive effect, mainly through more experimentation. Over 9 in 10 report some negative downstream effect, most often erosion of deep technical skills and codebase understanding. 17% say non-developers regularly ship customer-facing features. ([14:45](https://youtu.be/RGe6EjucbzI?t=885))

## Techniques
- **Intent-to-adopt ratio** — Among people who do not currently use a modality, count the share who plan to adopt it. Use it to read adoption momentum, not just current usage. *When:* When reading survey or adoption data to tell which modalities or tools are about to cross into real use.
- **Routing by task type across models** — Send each task to the model that suits it, rather than standardizing on one model. Some teams also run several models and compare outputs, or route by cost. *When:* When models differ in strengths and cost matters, and when a single model would be overkill or too expensive for some tasks.
- **Monitoring cost and token usage alongside quality** — Track token and cost metrics in production dashboards next to quality, treating cost like an SLA. *When:* When usage-based bills become a real constraint on how ambitiously an AI feature is built.
- **Human-in-the-loop approvals and permission gating for write-enabled agents** — Require human approval for actions and gate which permissions an agent holds. These are the most common controls in the survey. *When:* When agents can write data or take actions inside systems rather than only read or draft.

## Numbers
- Survey respondents: 1,048 ([1:28](https://youtu.be/RGe6EjucbzI?t=88))
- Among AI engineers not building with audio today, 56% plan to adopt it (strongest intent to adopt across modalities) ([3:29](https://youtu.be/RGe6EjucbzI?t=209))
- Share of respondents using generative AI for images and feeling good about it: 18% last year to 36% this year ([4:30](https://youtu.be/RGe6EjucbzI?t=270))
- 94% use closed models; 45% use open-weight models; over 90% of open-weight users also use closed models ([5:58](https://youtu.be/RGe6EjucbzI?t=358))
- Only about 5% named model openness as a top-three consideration for model choice; reliability was named by about one in five ([5:58](https://youtu.be/RGe6EjucbzI?t=358))
- 87% of teams use more than one model ([6:56](https://youtu.be/RGe6EjucbzI?t=416))
- 40% say cost regularly shapes AI ambition and 36% say sometimes; about three in four adjust usage based on cost ([8:21](https://youtu.be/RGe6EjucbzI?t=501))
- 95% of respondents use agents, roughly double last year ([9:52](https://youtu.be/RGe6EjucbzI?t=592))
- Agents with write access: 52% last year, 89% this year among agent builders ([9:52](https://youtu.be/RGe6EjucbzI?t=592))
- Two-thirds say hallucination or losing context mid-task frustrates them most with agents ([11:16](https://youtu.be/RGe6EjucbzI?t=676))
- 61% build their own prompt management ([13:16](https://youtu.be/RGe6EjucbzI?t=796))
- 97% report a net positive effect on their organization; over 9 in 10 report some negative downstream effect ([14:45](https://youtu.be/RGe6EjucbzI?t=885))
- About a third of teams have non-developers shipping features; 17% say non-developers regularly ship customer-facing features ([14:45](https://youtu.be/RGe6EjucbzI?t=885))
- 76% say AI boosted job satisfaction; 59% fear today's AI code creates long-term liabilities; one-third call software engineering a solved problem ([19:00](https://youtu.be/RGe6EjucbzI?t=1140))
- 67% expect a leading lab will declare AGI within five years (about the press release, not the achievement); 9% bet transformers are state of the art in five years ([17:04](https://youtu.be/RGe6EjucbzI?t=1024))

## Hot takes
- Nobody has settled the control layer for agents; human approvals and permission gating are basically the intern-management toolkit.
- Agent failures are usually the thinking, not the plumbing: hallucination and lost context frustrate most people.
- Open-weight models augment closed models rather than replace them.
- Cost is now monitored like an SLA, right under quality.
- Reliability is probably becoming a threshold requirement, so it no longer drives model choice.
- Almost every team has a stack problem; they just disagree about which one.

## Tools mentioned
Notion, Vercel, Nano Banana, ChatGPT Images 2.0

## Relevance to our work
- **general** (2/3): Concrete, recent (Aug 2026) market data on evals as the top challenge, multi-model routing, write-access agents, and build-vs-buy by layer. Useful context for designing the evals and governance story. → *Read the full State of AI Engineering 2026 report for the evals and agent-permissions cuts that were not shown in the talk.*
- **agentos** (1/3): The survey shows multi-model routing by task type and cost-based routing are the common patterns, which is relevant to the AgentOS strategy-routing pillar, but the talk gives no implementation detail. → *Compare Govrix strategy routing against the survey's routing-by-task-type pattern and check whether cost is a routing input.*
- **prosharness** (1/3): The most common agent controls are human approvals and permission gating, and write-enabled agents are rising fast. ProsHarness has phone-driven approvals, so this is a useful benchmark. → *Compare ProsHarness approval gates with the survey's top two controls and decide whether permission gating needs a per-action policy.*

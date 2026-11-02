# Viktor: AI Coworker That Lives in Slack — Fryderyk Wiatrowski

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `ohKt066uFhg` · [watch](https://youtu.be/ohKt066uFhg) · **date:** 2026-05-18 · **length:** 19:30 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Fryderyk Wiatrowski · **orgs:** Viktor, Slack
- **topics:** product-ux, enterprise-adoption, security-guardrails, memory · **tags:** slack-agent, company-agent, integrations, permissions, access-scoping, proactivity, model-personality, web-agents, browser-agent, rollout

> Viktor's co-founder on building a company AI employee that lives in Slack: shared integrations, scoped access, memory across many users, and why tone and staged rollout matter.

## Summary
Fryderyk Wiatrowski, co-founder of Viktor, describes an AI "coworker" that runs inside Slack and uses a company's shared integrations. He traces the company's history from a 2023 browser agent (Jace) that was reliable only for 3-5 steps, to an email agent, to Viktor, which launched in February 2026. The main design problems he names are cross-user memory growth, access control between channels and DMs, and merging many Slack interaction modes into one linear context. He argues that one team member connecting an integration is enough for the whole team, and that personal integrations need their own scoping after a customer leaked a personal Gmail account. He reports that users rejected a cheaper model swap (GPT-5.4) because they preferred the personality of Opus, and that proactive behaviour should be earned with a small group before a wide rollout. Much of the talk is a product pitch, but the access-control and rollout lessons are concrete.

## Key ideas
- **A company agent is a shared hire, not a personal tool.** — Viktor lives in Slack, takes on the permissions of integrations connected by any one team member, and is used by the whole team without each person reconnecting. This differs from a personal agent, where each user connects their own accounts. ([5:19](https://youtu.be/ohKt066uFhg?t=319))
- **Memory cost scales with users, not just with time.** — The same memory architecture serving 100 users fills up roughly 100 times faster than one personal user, so memory management becomes a central design problem. He says the team has solved it but gives no detail. ([6:50](https://youtu.be/ohKt066uFhg?t=410))
- **Access must follow the channel and the person asking.** — Context from a growth channel must not leak into engineering or support channels, and a DM should not pull growth-team context unless the person is on that team. Access rules are therefore part of the context model. ([7:50](https://youtu.be/ohKt066uFhg?t=470))
- **Slack makes long agent latency feel acceptable.** — Tasks can take around 10 minutes. In a web app that feels slow, but in Slack a teammate who returns an app in 10 minutes seems impressive, so the same wait feels short. ([8:54](https://youtu.be/ohKt066uFhg?t=534))
- **Slack's interaction modes must be merged into one context.** — DMs, public threads, emoji reactions, edits and deletes are all inputs. A deleted message should stop the task, an edit should trigger a reply, and a new DM should roll in the earlier thread's context instead of starting an empty sandbox. ([10:19](https://youtu.be/ohKt066uFhg?t=619))
- **Personality can decide model choice even when benchmarks favour another model.** — GPT-5.4 was better at tool calling and code generation and cheaper, but an A/B test showed users strongly preferred Opus's personality and objected to the switch. ([11:50](https://youtu.be/ohKt066uFhg?t=710))
- **Earn proactivity with a few users first.** — An agent that DMs everyone and joins threads on day one causes security pushback. He recommends starting with a small group and expanding once it has proven useful. He also gives an example of the agent checking an analytics claim against the data and running a significance calculation. ([12:50](https://youtu.be/ohKt066uFhg?t=770))
- **Personal integrations need their own scope.** — A customer's team connected one person's personal Gmail as the first shared integration, and the owner complained that the agent was reading his emails. Viktor then added per-integration scoping so an integration can stay personal and be used only when that person invokes it. ([15:17](https://youtu.be/ohKt066uFhg?t=917))
- **Three pillars for a useful coworker agent.** — He lists capable models, broad integrations (he cites roughly 3,000 tools, with the ability to build custom connections when needed), and company context from Slack. Friendliness and team fit are described as a separate requirement that also affects adoption. ([16:46](https://youtu.be/ohKt066uFhg?t=1006))

## Techniques
- **Shared-integration inheritance with per-integration scoping** — Let one team member connect an integration that the agent then uses for the team, inheriting that integration's permissions. Allow any integration to be marked personal so it is used only when its owner invokes the agent. *When:* Multi-user agents where repeated per-user OAuth would be painful, but some accounts must not be broadly shared.
- **Thread roll-over on new DM** — When a user opens a new DM with the agent, pull the previous conversation's messages into the existing conversation rather than starting a new sandbox and context. *When:* Chat-style agents where users forget old threads and restart in a new one.
- **Treat edits and deletes as control signals** — Map a message deletion to stopping the current task and a message edit to a new response, rather than ignoring them as ordinary input. *When:* Chat-interface agents with rich interaction modes such as Slack.
- **A/B test model personality, not only task scores** — Run a live A/B test of a candidate model against the current one and track user reaction along with tool-calling and code-generation quality. *When:* Replacing the model behind a user-facing agent that users already like.
- **Staged proactivity rollout** — Enable proactive DMs and thread participation for a small group first, and widen the rollout only after results are clear and security teams are comfortable. *When:* Launching an agent that can start conversations or act without being asked inside a company workspace.
- **Analytics check before acting on a claim** — Give the agent read access to analytics tools so it can check a claim made in conversation and run a simple statistical test before responding. *When:* Teams discussing experiment results in chat where claims need checking.
- **Browser-DOM web agent (2023 baseline)** — Send a losslessly minified DOM snapshot and the goal to the model, and let it pick the next action such as typing or clicking. *When:* Acting on sites with no API when tool calling is unavailable. The speaker reports this was reliable for only 3-5 steps, about 60% per step, so it is slow and brittle.

## Numbers
- Viktor launched in February 2026; the speaker says adoption was immediate and far above expectations. ([0:00](https://youtu.be/ohKt066uFhg?t=0))
- Roughly 3,000 integrations are available, and the agent can build its own connection when one is missing. ([1:06](https://youtu.be/ohKt066uFhg?t=66))
- In 2023 the browser-DOM agent reliably completed only 3-5 steps, at about 60% reliability per step, with the reliability compounding across steps. ([2:35](https://youtu.be/ohKt066uFhg?t=155))
- Complex agent tasks can take around 10 minutes, compared with the roughly 30 seconds users expect from chat tools. ([8:54](https://youtu.be/ohKt066uFhg?t=534))
- A team of 100 people with a 20-person growth team was given as the example of the many-user case, where each user connecting the same integration would be painful. ([14:19](https://youtu.be/ohKt066uFhg?t=859))
- Event attendees received $100 in free credits to try the product. ([18:13](https://youtu.be/ohKt066uFhg?t=1093))

## Hot takes
- Model personality can outweigh better tool calling and lower cost when choosing the model behind a user-facing agent.
- A company agent should be treated like a new hire, not a tool, so it should not be given anyone's personal accounts by default.
- Proactive agents should be earned with a few users first, because day-one access to a whole workspace triggers security objections.
- Slack, rather than a web app, makes multi-minute agent latency feel acceptable to users.

## Tools mentioned
Slack, Viktor, OpenClaw, Claude Code, Claude Cowork, Opus 4.6, GPT-5.4, PostHog, Gmail, Meta Ads, WebArena

## Relevance to our work
- **agentos** (1/3): Shared versus personal tool credentials and per-user scoping map onto AgentOS's multi-tenant gateway. The talk gives no implementation detail on the memory fix. → *Add a per-credential scope (team-shared or personal, used only when the owner invokes) to the AgentOS proxy manifest, so one user's personal account is never reused for everyone.*
- **general** (1/3): The access-scoping, memory-growth and staged-proactivity lessons apply to any multi-user agent design. → *When designing a multi-user agent, decide up front which integrations are shared and which are personal, and pilot proactive behaviour with a small group before widening it.*

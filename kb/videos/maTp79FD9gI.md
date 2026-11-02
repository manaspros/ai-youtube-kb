# Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing - Bala Ramdoss, Amazon Lens

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `maTp79FD9gI` · [watch](https://youtu.be/maTp79FD9gI) · **date:** 2026-08-18 · **length:** 14:13 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Bala Ramdoss · **orgs:** Amazon Lens, Google (A2UI), CopilotKit
- **topics:** product-ux, mcp-and-tools, agent-architecture · **tags:** generative-ui, A2UI, rendering-layer, BFF, server-driven-ui, streaming, mobile, rendering-contract, time-to-first-chunk, agent-ux

> Bala Ramdoss (Amazon Lens) on why LLM agent output needs a typed rendering layer between model and screen: a versioned UI contract, streamed typed chunks, and a BFF that hydrates actions, so mobile clients stay dumb and safe.

## Summary
The speaker argues that agent output is not UX: the model does the work well, but the delivery layer between model output and the screen decides whether a product succeeds. He frames generative UI as a spectrum (controlled, declarative such as Google's A2UI, open-ended) and says mobile production apps should stay in the bottom two rungs, because clients cannot be patched once shipped. His pipeline has three patterns: a versioned rendering contract that limits the model to a fixed component menu (with layout rules), streaming typed UI blocks instead of text, and a BFF that adds platform rules, hydration, actions and conversation context while reusing existing components. He recommends measuring time to first chunk rather than total latency, and designing loading states around streaming. The talk is a practitioner account from building Amazon Lens, and he states it is his own view, not his employer's.

## Key ideas
- **Agent output is not UX; a delivery layer must sit between model and screen** — The model did the real work in his restaurant example, but the raw text output left the user to do the booking. The gap is a layer that turns model output into something a human can act on. He says the failures he hit were delivery problems, not model problems. ([0:01](https://youtu.be/maTp79FD9gI?t=1))
- **Generative UI is a spectrum of three rungs: controlled, declarative, open-ended** — Controlled means the model picks from pre-built components. Declarative means it composes from a catalog of components (where A2UI sits). Open-ended means it generates novel UI. The higher the rung, the more the client must trust the model's output. He says most production mobile apps stay in the bottom two. ([3:30](https://youtu.be/maTp79FD9gI?t=210))
- **Mobile clients cannot be patched, so they must degrade gracefully** — A web renderer bug can be fixed in minutes, but app-store installs update on their own schedule. An unknown content type can crash clients for days or weeks. This is why he treats the client as something you cannot patch. ([4:56](https://youtu.be/maTp79FD9gI?t=296))
- **Pattern 1: a versioned rendering contract that tells the model what the client can draw** — The model only sees components the client version supports, drawn from a version map. Layout rules are encoded in the contract (for example, a swipeable carousel for 1-3 items and a vertical list for 4 or more). The model picks an intent from a small fixed menu and never invents a component. ([5:57](https://youtu.be/maTp79FD9gI?t=357))
- **Pattern 2: stream typed UI blocks, not text, and chase time to first chunk** — A conversation block carries text and a UI block carries components. Show a skeleton, then fill it in chunks. He says total latency is the wrong metric and time to first useful chunk is the right one. A loading spinner does not fit AI features, so the feature should be designed around the wait. ([8:27](https://youtu.be/maTp79FD9gI?t=507))
- **Pattern 3: a BFF hydrates components and adds actions, so the client stays dumb** — The BFF applies platform rules per OS, adds an action payload to every element (tap behavior, deep link, impression metric), and carries conversation context across turns. It reuses existing production components, so the result looks native. ([11:55](https://youtu.be/maTp79FD9gI?t=715))

## Techniques
- **Versioned rendering contract** — Keep a version map of client capabilities. Expose only the components a given client version can draw to the model in its context. Encode layout rules (e.g. count-based carousel vs list) in the contract. The model picks intents from a fixed menu. *When:* Mobile or any multi-version client where renderers cannot be patched quickly, and the model must not invent UI.
- **Typed streaming UI blocks** — Have the model stream typed blocks: a conversation block for text and a UI block for components. The client renders skeleton, then partial, then complete as chunks arrive. *When:* Agent responses that take seconds, where a single blocking API call leaves the user waiting.
- **BFF as renderer and hydrator** — A backend-for-frontend turns model intent into rendered components. It attaches platform-specific rules, action payloads (tap, deep link, impression metric), and conversation context, and reuses existing UI components. *When:* Adding agent features to an existing app and wanting the output to match native components and keep clients simple.
- **Design loading around streaming** — Measure time to first chunk, not total latency. Show what the agent is doing (state updates) during long tasks, and let the user keep working (e.g. tap objects while results load). *When:* AI features where full responses take several seconds.

## Numbers
- Streamed render may take 3-4 seconds to finish, but the wait is tolerable when content appears in chunks ([8:27](https://youtu.be/maTp79FD9gI?t=507))
- Agent task example takes about 10 seconds; he says the wait is acceptable when progress is visible ([10:56](https://youtu.be/maTp79FD9gI?t=656))
- Amazon Lens runs on millions of mobile devices; the speaker has built it over six years ([1:02](https://youtu.be/maTp79FD9gI?t=62))
- Layout rule example: 1-3 flights shown as a swipeable carousel, 4 or more as a vertical list ([7:26](https://youtu.be/maTp79FD9gI?t=446))

## Hot takes
- The model is not the problem; the layer between model output and the screen is what ships the product.
- Most production mobile apps should stay in the controlled and declarative rungs of generative UI, not open-ended.
- Total latency is the wrong metric for AI features; time to first chunk matters more.
- Mobile clients must be treated as unpatchable, so they should never crash on unknown content types.

## Tools mentioned
A2UI, CopilotKit, MCP apps

## Relevance to our work
- **general** (2/3): The talk gives a practitioner framework (contract, streaming, BFF) for putting agent output on screen, and a time-to-first-chunk metric that applies to any streamed agent UI. → *Read the A2UI open spec and track time to first chunk alongside total latency for any streamed agent feature.*
- **agentos** (1/3): AgentOS sends streamed agent output through a proxy, and this talk's typed-block and versioned-contract ideas could inform a stream format. The talk is about mobile UI, though, so the fit is weak. → *Consider a typed streaming block format in the AgentOS proxy response spec, with a version field so old clients degrade safely.*
- **prosharness** (1/3): ProsHarness has phone-driven approvals. A typed, versioned set of approval components sent to the phone (with a safe fallback) matches the contract idea. → *When designing phone-driven approvals, define a small fixed set of typed approval components with a version tag and a fallback for unknown types.*

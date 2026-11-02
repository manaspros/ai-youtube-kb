# Build the Right Thing: Product Engineering (Part 1) — Kent C. Dodds, EpicProduct.engineer

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `_fHTqOs5wQA` · [watch](https://youtu.be/_fHTqOs5wQA) · **date:** 2026-10-06 · **length:** 55:19 · **format:** workshop · **quality:** 3/5 · **depth:** intro
- **speakers:** Kent C. Dodds · **orgs:** Cloudflare, WorkOS, Instagram
- **topics:** product-ux, coding-agents · **tags:** product engineering, idea validation, the mom test, smallest slice, prototyping, ownership, agent-written code, user research, workshop

> Kent C. Dodds argues that once agents level implementation, the durable engineering skill is deciding what to build, using Mom Test-style validation and smallest-slice thinking. Part 1 of a workshop, mostly framing.

## Summary
Kent C. Dodds opens a two-hour product engineering workshop by arguing that agents have commoditized implementation, so the scarce skill is deciding whether and what to build. He frames the product engineer as someone who connects customer needs to technical choices such as data model, workflow shape, failure modes, and the smallest slice. He warns that agents make it easy to build the wrong thing fast, and that a prototype that looks functional can hide scaling and edge-case gaps. The core validation advice is to borrow The Mom Test: ask about specific past behavior, workarounds, and cost, not hypotheticals or the solution. He backs this with anecdotes, including an Australian real-estate team that spent about A$1.2M and a year on a system nobody used. The talk is mostly warm-up and quoted opinion; the actual frameworks (Jobs To Be Done, Kano) are deferred to later parts.

## Key ideas
- **Implementation is commoditized, so the differentiator is building the right thing** — The speaker's thesis: when agents level the implementation playing field, the scarce skill is deciding what to build and whether it is worth building. The question shifts from can we build it to is it worth building. ([9:54](https://youtu.be/_fHTqOs5wQA?t=594))
- **Turning tickets into implementations is the replaceable part of the job** — An engineer who only takes a spec and hands back code looks like an agent. A product engineer keeps ownership after shipping and asks whether the work produced customer value. ([17:00](https://youtu.be/_fHTqOs5wQA?t=1020))
- **Prototypes that look functional can hide scaling and edge-case gaps** — Quoting a Cloudflare product leader: a prototype can feel shippable on the surface. The advice is to be willing to throw it away and rebuild it with agents, taking ownership of it. ([19:35](https://youtu.be/_fHTqOs5wQA?t=1175))
- **Ownership creates better agent playgrounds** — If you expect to be paged at 2 a.m. for a system, you invest in the testing, architecture and constraints that let agents succeed. Engineers now act as team leads over many agents, so the job includes building a good environment for them. ([20:39](https://youtu.be/_fHTqOs5wQA?t=1239))
- **Product engineers map customer needs onto technical decisions** — The product engineer decides the data model, workflow shape, observability, failure modes and smallest slice, using knowledge of upstream requests. Architecture changes are expensive, so early primitives matter more than the token cost of a rewrite. ([21:33](https://youtu.be/_fHTqOs5wQA?t=1293))
- **Find the smallest useful slice by watching real use** — Shrink the whole thing down to the useful part. The speaker cites Instagram cutting a check-in app down to photo sharing after watching user behavior, and a telecom engineer who rode along on repair trucks to see how users work. ([22:44](https://youtu.be/_fHTqOs5wQA?t=1364))
- **Ask about past specific behavior, not hypotheticals or solutions** — The Mom Test rule: do not ask would you use this or would you pay, since people give polite yes answers. Ask about the last time it happened, what they did instead, what it cost them, and how much effort they already spend. Weak signals are when people cannot remember the problem or gave up on it. ([41:38](https://youtu.be/_fHTqOs5wQA?t=2498))
- **Early prototypes reveal whether the problem is worth solving** — If early users push through a rough prototype and stay excited, that is a strong signal. If they quit at small paper cuts, that is a weak one. Also watch whether people understand your excitement; if they do not, pay attention to that feeling. ([48:59](https://youtu.be/_fHTqOs5wQA?t=2939))

## Techniques
- **Mom Test customer interviews** — Interview potential users about specific past events: the last time the problem happened, who was involved, what they did as a workaround, what it cost in time or money, and how often it happens. Avoid pitching the solution and avoid future-tense questions. *When:* Before building any feature or product, and when a PM hands you a feature request with no validation attached.
- **Ask what the problem costs** — Ask what the user loses by not having a solution. Treat existing effort or money spent on workarounds as the strongest evidence of a real problem. *When:* When validating whether a problem is worth solving and whether a planned feature justifies engineering time.
- **Smallest slice / minimal demonstrable solution** — Strip the idea to the minimal thing that proves you solve the problem for a narrow target audience. Cut everything else, the way Instagram cut its original app to photo sharing. *When:* When scoping an MVP or deciding how many features a first version needs, especially in a crowded space.
- **Throwaway prototype, then rebuild with agents** — Ship a rough prototype to early users to test the idea. Once validated, throw the prototype away and reimplement it properly with coding agents, owning the design decisions. *When:* When a prototype looks functional but may not scale or handle edge cases.
- **Check the neighbors before building** — Look one level out, up and down the stack and across teams, to see whether existing primitives already solve the request, so you do not rebuild them. *When:* Before adding a new subsystem, primitive or abstraction to a product.
- **Build the agent playground** — Invest in tests, architecture and clear building blocks so agents make fewer mistakes. Treat the codebase as the environment agents work inside. *When:* When running several coding agents in parallel on a shared codebase.

## Numbers
- Australian real-estate team spent about A$1.2M (roughly US$900k) and a year building a high-scale system; no one used it. Speaker says a two-week launch with manual integration would have tested the market. ([46:36](https://youtu.be/_fHTqOs5wQA?t=2796))
- Speaker has developed software for over a decade, graduated in 2014, and has been a full-time teacher since 2019. ([3:51](https://youtu.be/_fHTqOs5wQA?t=231))
- Workshop is a two-hour session; the audience question queue and the prompt to build an example app were the main structure. ([12:48](https://youtu.be/_fHTqOs5wQA?t=768))

## Hot takes
- If you are just turning tickets into implementations, you look like an agent.
- Agents accelerate bad practices across a codebase, so you can move bad faster if you are not careful.
- The best software engineers were never the ones who stayed silent in their corner; they talk to people and understand their problems.
- User error does not exist; if operators made a bad call, the system was wrong (paraphrasing Don Norman).
- Coding challenges that ban agents make no sense when the job is to use agents.
- You do not need a course on React or useState anymore if you are an experienced engineer who can direct an agent; the durable skill is building the right thing.

## Tools mentioned
Slido, Cursor, OpenCode, Claude (captioned as 'cloud')

## Relevance to our work
- **general** (2/3): The talk gives a practical interview method for early validation (past behavior, workaround, cost) and a warning about rebuilding existing primitives. → *Use the Mom Test question set (last time it happened, what did you do instead, what did it cost) on the next internal feature request before estimating engineering work.*
- **agentos** (1/3): The smallest-slice and Mom Test ideas fit how to scope the next AgentOS pillar, but this talk has no infra, benchmark, or agent-system content. → *Before building the next AgentOS pillar, write down the narrowest end-to-end path that proves it works and run it once, before expanding scope.*
- **prosharness** (1/3): The team-lead framing (build the agent playground, own the failure modes you get paged for) loosely applies to the harness's checkpoint and approval design, but the talk gives no harness specifics. → *Review which ProsHarness failure modes you would actually be paged for, and check the checkpoint and approval flows against those first.*

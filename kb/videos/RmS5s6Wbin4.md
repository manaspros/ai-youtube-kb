# Gadgets: Personal app vibe coding that is actually safe — Kenton Varda, Cloudflare

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `RmS5s6Wbin4` · [watch](https://youtu.be/RmS5s6Wbin4) · **date:** 2026-08-18 · **length:** 18:54 · **format:** demo · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Kenton Varda · **orgs:** Cloudflare
- **topics:** vibe-coding-app-building, sandboxing-execution, security-guardrails, product-ux · **tags:** personal apps, vibe coding, sandboxing, iframe CSP, postMessage RPC, Durable Objects, dynamic workers, workerd, sharing model, blueprints, self-hosting, agent-extends-app

> Kenton Varda (Cloudflare) argues personal AI codegen needs new infrastructure, and demos "Gadgets": per-user apps with platform-enforced sharing and sandboxed generated code, run on open-source workerd.

## Summary
Kenton Varda argues that AI-generated personal apps break the current model of one blessed server-hosted version of an app for every user. Users should be able to have an agent add the features they need, but app stores, Apple and Google gatekeeping, and the server-hosted web model all block that. His prototype, Gadgets, is a Google Docs-style environment where each gadget is one personal app instance with its own data, shared through a sharing model the platform implements. Generated client and server code run in a null-origin sandboxed iframe and a dynamic Worker sandbox that can only talk to each other over postMessage and RPC, so XSS bugs in generated code do not leak anything. In the demo, Claude extended the Slides app itself (strikethrough, centering, SVG insertion) from a brief. The whole stack runs on Workers and Durable Objects with no containers or database, locally on the open-source workerd runtime. The release of the code was postponed on the CTO's advice, so the open-source promise did not happen at this talk. The demo's first prompt failed, and the talk is mostly a concept pitch with one prototype.

## Key ideas
- **Thesis: personal AI codegen breaks today's cloud infrastructure, which assumes one server-hosted version of an app for all users.** — Users cannot customize a single blessed server-side app, so per-user features need a different hosting model, not just a vibe-coding front end. ([0:08](https://youtu.be/RmS5s6Wbin4?t=8))
- **The plugin-rewrite trap is the failure mode that agents could fix.** — Developers pile feature requests into if-statements, then stall while rewriting for a plugin system. Letting each user's agent write their own feature avoids the bloat and the stall. ([2:08](https://youtu.be/RmS5s6Wbin4?t=128))
- **Platform-enforced sharing, not app-enforced.** — Each gadget holds one thing to share, so the platform can implement the share dialog and access control, and app code cannot get access control wrong. ([11:26](https://youtu.be/RmS5s6Wbin4?t=686))
- **The agent extends the app, not only the content.** — Given a brief doc plus the app's source, Claude added missing features (strikethrough, centering, arbitrary SVG insertion) so the slide tool could express what the brief asked for. ([12:26](https://youtu.be/RmS5s6Wbin4?t=746))
- **Generated code can be untrusted because the sandbox limits what it can reach.** — The client runs in a null-origin iframe with a strict CSP and no cookies, and its only channel is postMessage to the parent, which relays RPC to the server code in a dynamic Worker sandbox. XSS in generated code therefore leaks nothing. ([13:53](https://youtu.be/RmS5s6Wbin4?t=833))
- **Blueprints separate code from data.** — A blueprint exports a gadget's code without its data so others can instantiate their own copy. Each instance holds one document. ([9:16](https://youtu.be/RmS5s6Wbin4?t=556))
- **Same runtime locally and in the cloud.** — The whole stack runs on workerd, the open-source Workers runtime, on the speaker's laptop, and he plans to self-host it for home automation. The release was postponed on the CTO's advice, so the code was not published at the talk. ([16:12](https://youtu.be/RmS5s6Wbin4?t=972))

## Techniques
- **Platform-enforced sharing via single-purpose instances** — Make one app instance hold one shareable thing. The platform owns the share dialog and access checks, so generated app code cannot break access control. *When:* Agent-generated multi-user apps where access control must not depend on code quality.
- **Sandboxed generated UI with postMessage-only RPC** — Serve the generated client in a null-origin iframe with strict CSP, no cookies, and no network. Connect it only through a postMessage channel that relays RPC to server code in a separate sandbox. *When:* Letting an agent write both frontend and backend for a per-user app, where the goal is that a bug in the generated code cannot leak data.
- **Give the agent the app source and a brief, let it add primitives** — Provide the app's code plus a requirements doc. When the app lacks a feature, the agent adds it (here: strikethrough, centering, SVG embed) rather than working around the limit. *When:* Creating content in an existing tool whose features may not cover the brief.
- **Export code-only templates (blueprints)** — Export an app's code without its data and let others instantiate per-instance copies. *When:* Sharing reusable personal-app templates while keeping user data separate.
- **Run the production runtime locally** — Use the open-source workerd runtime on a laptop so the same stack runs offline and self-hosted. *When:* Developing or self-hosting edge-style apps where you want offline behavior and no cloud dependency.

## Numbers
- Cloudflare Workers serves millions of developers and trillions of requests per day (speaker's figures about the platform he co-created in 2017). ([1:16](https://youtu.be/RmS5s6Wbin4?t=76))
- The speaker says it is 'almost easier in the US to buy a gun than to install unsigned software' on a phone, and that about five companies can build mobile apps, which are rhetorical claims, not measurements. ([3:24](https://youtu.be/RmS5s6Wbin4?t=204))
- Gadget demo: an app took about one afternoon to vibe-code, per the speaker's estimate for a colleague's slide builder. ([10:13](https://youtu.be/RmS5s6Wbin4?t=613))

## Hot takes
- Personal AI codegen breaks the one-blessed-server-version model of cloud infrastructure, and the fix is not a vibe-coding front end on existing infra.
- The plugin-architecture rewrite is a trap that agent-written per-user features make unnecessary.
- XSS in agent-generated code matters less if the sandbox controls what the code can reach than if it is trusted.

## Tools mentioned
Cloudflare Workers, Durable Objects, Dynamic Workers, workerd, Claude, Cap'n Web RPC

## Relevance to our work
- **general** (2/3): Strong, concrete sandbox design for untrusted agent-generated UI and server code. The threat model (XSS in generated code is contained by platform isolation) is a reusable frame. → *Read the talk's sandbox model (null-origin iframe, CSP, postMessage RPC, dynamic Worker) when designing any agent-generated UI that calls back to a server.*
- **agentos** (1/3): Crucible (L2C) runs sandboxed code for agents. The Gadgets pattern of null-origin iframe, CSP, and a postMessage-only channel to a separate sandbox is a comparable isolation design, but no code was released. → *Compare Crucible's isolation boundary with the iframe-plus-dynamic-Worker design once the Gadgets code is public (the talk says it will be released later).*

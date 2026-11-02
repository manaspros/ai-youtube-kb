# Why Leaving React Was Remix 3's BIGGEST Gamble (That Paid Off)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `ZXcQR2jZL8s` · [watch](https://youtu.be/ZXcQR2jZL8s) · **date:** 2025-12-02 · **length:** 4:38 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Remix, Better Stack
- **topics:** dev-tools · **tags:** remix-3, frontend-framework, reactivity, full-stack, react-alternative, vite, server-rendering, web-platform-apis

> A 4-minute first look at Remix 3's experimental React-free reactivity, components, events, frames and server roots, with the presenter saying it is not production-ready and not clearly a payoff.

## Summary
Better Stack walks through a basic Vite counter app built on Remix 3, the experimental framework that replaced React with its own reactivity system (announced in May per the video). The presenter installs two packages from the experimental "jam" dist-tag (the captions say "Jam"; exact package names are not shown), then adds press handling with an on prop and shows that a plain JavaScript variable plus a manual update call re-renders the component. He covers a more custom interaction that dispatches custom events and uses an events() helper over add/remove listener, plus context, signals (described as closer to abort signals than Solid-style reactive signals). He then notes that Remix 3 is a full-stack framework with server roots that run on Node, Bun or Cloudflare, and "frames" that behave like route-keyed suspense boundaries refreshing stale HTML, closer to Alpine Ajax than React server components. The presenter says Remix 3 is still under heavy development with many key packages unfinished, that he prefers Ripple's direction, and that the lack of a React-sized library ecosystem is the main open question. No benchmarks, production case studies or code for the full app are shown, so the title's claim that leaving React "paid off" is not backed by anything in the video.

## Key ideas
- **Remix 3 dropped React for its own reactivity system, and the presenter says it is nowhere near production-ready.** — Announced in May per the video. The presenter says many key packages are still under construction and that he shows it anyway. ([0:00](https://youtu.be/ZXcQR2jZL8s?t=0))
- **Components get a typed `this` handle that connects them to the runtime, and plain JavaScript variables work as state.** — The component parameter is typed as remix.handle. Its update() function re-renders the component manually after a plain variable changes, and the component function returns a function that returns JSX, not JSX directly. ([1:27](https://youtu.be/ZXcQR2jZL8s?t=87))
- **Events are wired through an on prop with a press-down interaction that fires for mouse click, spacebar and Enter.** — The caption wording for the interaction name is ambiguous. Custom interactions receive the target and a dispatch function, and an events() helper wraps add and remove listener. ([1:27](https://youtu.be/ZXcQR2jZL8s?t=87))
- **Remix 3 is full-stack: roots run on the server in Node, Bun or Cloudflare.** — The presenter says the root function can be run inside any server and names Node in the demo, with Bun and Cloudflare also supported. ([2:49](https://youtu.be/ZXcQR2jZL8s?t=169))
- **Frames are route-keyed boundaries, similar to suspense, that refresh stale HTML by fetching it from a URL.** — The presenter compares this to HTML-over-the-wire approaches like Alpine Ajax and says it is less like React server components. ([2:49](https://youtu.be/ZXcQR2jZL8s?t=169))
- **The main open question is ecosystem size, since Remix 3 has no React-scale library base.** — The presenter says he prefers the direction of Ripple, finds the primitives hard to learn, and likes that the design rests on web APIs such as custom events, abort signals, URLs and FormData. ([4:14](https://youtu.be/ZXcQR2jZL8s?t=254))

## Techniques
- **Counter component with plain state and manual re-render** — Write a component function whose handle parameter is typed remix.handle. Keep state in a plain JavaScript variable (for example bpm), change it in an event handler, then call handle.update() to re-render. The component returns a function that returns JSX, not JSX directly. Setup shown: create a Vite app and install two packages from the experimental 'jam' dist-tag (exact package names not shown in the captions). *When:* Small interactive widgets in a Remix 3 experiment where you want React-like local state without signals.
- **Press handling via the on prop** — Define an interaction function for press down (fires on left click, Space or Enter), then pass it to a button with the on prop instead of onClick. *When:* Keyboard-accessible buttons that should respond to the same activation events across input methods.
- **Custom interaction with dispatched events** — Write an interaction that receives the event target and a dispatch function. Dispatch a custom event carrying a value, and use the events() helper (a wrapper over add and remove event listener) to subscribe. The presenter's handler updates the target and re-renders it. *When:* Communication between components or a custom DOM-event API where you would otherwise use CustomEvent and dispatchEvent by hand.
- **Frames for route-keyed partial updates** — Wrap a region in a frame with a fallback. The frame is keyed to a route or URL. When its HTML is stale, it fetches new HTML from that URL and swaps it in, similar to Alpine Ajax. *When:* Server-driven partial page updates where you want fetch-and-swap rather than client-side state or React server components.
- **Server root function** — Create a root with the root function and run it inside a server. The presenter used Node, and says Bun and Cloudflare also work. *When:* Full-stack Remix 3 apps that need the same component model on the server.

## Numbers
- Remix 3 was announced in May (year not stated in the captions); the video runs 4:38 and shows no benchmarks, latency or bundle-size figures. ([0:00](https://youtu.be/ZXcQR2jZL8s?t=0))
- Remix 3 is pre-production: many key packages are still under construction. ([0:00](https://youtu.be/ZXcQR2jZL8s?t=0))
- The press interaction fires for three inputs: left click, spacebar and Enter. ([1:27](https://youtu.be/ZXcQR2jZL8s?t=87))

## Hot takes
- The title says leaving React was the biggest gamble that paid off, but the video offers no evidence of payoff. It is a feature tour of a framework the presenter himself calls not production-ready.
- Presenter prefers Ripple's direction to Remix 3 and says the primitives took a while to learn, with the 'this' handle param a stated pain point.
- Lack of a React-sized library ecosystem is named as the main risk, and the presenter leaves it as an open question.
- Quality is capped at 2: a hype title with a 4-minute tour, no benchmarks, no production evidence and no full source.

## Tools mentioned
Remix 3 (experimental, 'jam' dist-tag), Vite, React, Ripple, SolidJS, Alpine Ajax, Node, Bun, Cloudflare, TypeScript, Remix Jam 2025 talks

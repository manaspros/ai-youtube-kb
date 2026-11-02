# The Ripple UI Shift: Why So Many Developers Might Replace React

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `ANPbRu5cWFQ` · [watch](https://youtu.be/ANPbRu5cWFQ) · **date:** 2025-12-02 · **length:** 6:40 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** ?
- **topics:** dev-tools · **tags:** ripple, ui-framework, react-alternative, fastapi, python, vite, dev-proxy, fine-grained-reactivity, frontend

> Short walkthrough of the Ripple UI framework: a counter, a to-do list, and a FastAPI backend wired through a Vite dev proxy. The speaker concludes Ripple will not replace React yet, and offers no benchmarks for its speed claims.

## Summary
A 6-minute Better Stack demo of Ripple, a UI framework that the speaker presents as faster and lighter than React, with built-in fine-grained reactivity. He builds a small Vite-style Ripple project with a counter, a to-do list that uses if and for in the template instead of map, and fetch calls to a FastAPI backend, with requests forwarded through a Vite dev proxy. The core reactivity primitive is the track() function, which he says replaces useEffect and useState-style hooks. He argues Python developers would rather not ship roughly 200 KB of JavaScript for a simple form, and positions Ripple as the interactive browser layer beside a Python API. The video shows no measurements of bundle size, render speed or memory, so the performance claims are unverified. He ends by saying Ripple is not going to replace React yet, which undercuts the title.

## Key ideas
- **Ripple's pitch: faster, lighter and simpler than React, with fine-grained reactivity and clean syntax built in.** — Stated as the premise, with no benchmark or measurement shown in the video. Treat the performance claim as unverified. ([0:00](https://youtu.be/ANPbRu5cWFQ?t=0))
- **Ripple uses component files with HTML-like templates, and track() is the reactivity primitive that replaces useEffect.** — Apps mount to a single root element. The project is a Vite-style layout with app.ripple.ts as the main component file. ([1:01](https://youtu.be/ANPbRu5cWFQ?t=61))
- **Only the UI parts that depend on a tracked value update, not the whole component tree.** — A counter built in about a minute has no useState, setState, hooks or dependency arrays. The speaker attributes the updates to track(). ([2:14](https://youtu.be/ANPbRu5cWFQ?t=134))
- **Templates use plain if and for control flow instead of JSX with map.** — The to-do list demo adds and clears items with if and for in the template. The speaker says this matches how people think about UI. ([3:22](https://youtu.be/ANPbRu5cWFQ?t=202))
- **Python backend integration works through a Vite dev proxy that forwards API routes to FastAPI.** — Ripple calls backend routes with fetch and renders the responses. Backend logs can be shown in the front-end UI. The speaker frames the setup as Python owning routes, services and logic, with Ripple handling the reactive browser layer. ([4:21](https://youtu.be/ANPbRu5cWFQ?t=261))
- **Positioning: Ripple is pitched for Python developers who do not want to learn React or ship a large JavaScript bundle for simple forms.** — The speaker explicitly says Ripple will not replace React yet. The closing message is that it is worth trying if you want a reactive front end that pairs well with a Python backend. ([5:35](https://youtu.be/ANPbRu5cWFQ?t=335))

## Techniques
- **Vite dev proxy to a Python API** — Run the Ripple front end under Vite and configure the dev server to forward API route prefixes to the FastAPI process, so the browser makes same-origin fetch calls. The exact proxy config is not shown in the video. *When:* A split setup where Python owns routes and business logic and a small reactive front end sits in the browser during development.
- **track() for reactive state instead of hooks** — Wrap reactive values with the track function in Ripple components. Updates then re-render only the dependent parts of the UI, with no useState, setState, hooks or dependency arrays. The video does not show the full syntax. *When:* Small interactive widgets such as counters or toggles, where a React-style hooks setup would be heavier than needed.
- **if and for in templates instead of map** — Write conditional and list rendering directly in the component template with if and for blocks, rather than JSX with array.map. *When:* Lists and conditional UI where you want the template to read like the markup it produces.

## Numbers
- The speaker says a React-style front end can ship about 200 KB of JavaScript just to build a form. This is his claim and is not measured in the video. ([5:35](https://youtu.be/ANPbRu5cWFQ?t=335))
- The counter demo took about 60 seconds to build. ([2:14](https://youtu.be/ANPbRu5cWFQ?t=134))
- No benchmark, bundle size, render time or memory figure is shown for Ripple versus React, despite the speed and weight claims. ([0:00](https://youtu.be/ANPbRu5cWFQ?t=0))

## Hot takes
- The title says developers 'might replace React', but the speaker concludes that Ripple is not going to replace React yet.
- The 'faster, lighter' claims are asserted without any measurement, so the speed case rests on the demo's feel rather than data.
- Thin substance: a short tour of counter, list and proxied fetch with no real app, no comparison and no discussion of trade-offs such as ecosystem or maturity. Quality is capped accordingly.

## Tools mentioned
Ripple, Vite, FastAPI, Python, Flask, Django, React, Svelte, Solid JS, app.ripple.ts

# Fix Slow React Components in Seconds! (New GitHub Storybook Addon)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `fv9wj8nkDVM` · [watch](https://youtu.be/fv9wj8nkDVM) · **date:** 2026-04-02 · **length:** 6:47 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Andrus · **orgs:** Better Stack, GitHub, Storybook
- **topics:** testing-verification, dev-tools · **tags:** storybook, react, frontend-performance, web-vitals, layout-thrashing, memoization, useLayoutEffect, shift-left-testing, lighthouse

> Walkthrough of GitHub's new Storybook performance-panel add-on for measuring component frame timing, DOM churn, layout thrashing and React render cascades before code reaches production.

## Summary
Better Stack (Andrus) walks through a new GitHub add-on for Storybook that adds a performance panel to component stories. The panel reports frame timing and jitter, input responsiveness, layout stability (CLS), DOM churn, layout thrashing, memory pressure, React profiling and P95 render duration. The pitch is shift-left performance testing: check each component in isolation during development instead of relying on whole-page Lighthouse runs. The video demos the panel on a set of live playbook examples (animated box, heavy list, element timing, expensive render, memoization, render cascade, style churn) and explains what each red flag means. Non-React frameworks (Vue, Svelte, web components) are covered by a universal mode, and Chrome or Edge is recommended. The video does not show installation or configuration, and gives no measured overhead or before/after numbers beyond qualitative graph behavior.

## Key ideas
- **A GitHub add-on for Storybook gives each component story a performance panel: frame timing, input responsiveness, layout stability, React profiling and memory pressure.** — The pitch is shift-left performance testing, judging component performance during development rather than after release. ([0:00](https://youtu.be/fv9wj8nkDVM?t=0))
- **The panel explains its red flags in plain terms: frame jitter, DOM churn, layout thrashing, render cascades and P95 duration.** — Thrashing is reading and writing styles back to back so the browser recalculates layout repeatedly in one frame. P95 shows the worst case for slow users rather than the average. Render cascades are small state changes that trigger wide re-render waves. ([0:55](https://youtu.be/fv9wj8nkDVM?t=55))
- **Universal mode covers non-React frameworks such as Vue, Svelte and web components, and the speaker recommends Chrome or Edge for best results.** — The video does not say which browser versions or what setup is required. ([1:56](https://youtu.be/fv9wj8nkDVM?t=116))
- **A heavy list example shows layout instability and DOM churn together: a large CLS spike, churn spikes and dropped frames when the list is filtered.** — The contrast example is an animated box where inline style mutations happen with frame rate and frame time staying stable. ([1:56](https://youtu.be/fv9wj8nkDVM?t=116))
- **Re-render cost shows up as P95 spikes, frame jitter and high total blocking time when the main thread is busy with JavaScript.** — Total blocking time is described as a warning sign because it means the user cannot click or scroll during the blocked window. A memoized version skips redundant renders and keeps the frame rate near 60 fps. ([3:15](https://youtu.be/fv9wj8nkDVM?t=195))
- **Calling setState inside useLayoutEffect causes a cascade on every update because the effect runs after DOM mutations but before paint.** — The speaker's claim is that this forces React to reprocess the tree and the browser to recalculate layout a second time per frame, roughly doubling the work. ([4:16](https://youtu.be/fv9wj8nkDVM?t=256))
- **Mutating inline styles on 600 nodes in one pass saturates the main thread and triggers stall warnings in the thrashing section.** — The browser is forced into a reflow loop while the JavaScript is still writing styles. ([4:16](https://youtu.be/fv9wj8nkDVM?t=256))
- **The speaker positions this add-on as more precise than Lighthouse because it attributes cost to individual components instead of whole pages.** — This is an opinion stated without a side-by-side comparison in the video. ([5:16](https://youtu.be/fv9wj8nkDVM?t=316))

## Techniques
- **Component-level performance check in Storybook** — Install GitHub's new Storybook performance add-on in the existing Storybook suite (package name and config not shown in the video) and open the performance panel on the component's story. Run it in Chrome or Edge. Use the React metrics for React components and universal mode for Vue, Svelte or web components. *When:* During component development or review, before a page-level performance regression shows up in production or in Lighthouse.
- **Mark hero and call-to-action elements for render timing** — Add the element timing attribute to the DOM element whose visibility matters (hero content, CTA). The panel then measures that element's exact render time. *When:* When you care about perceived performance for a specific piece of content, not the generic page-load metric.
- **Avoid setState in useLayoutEffect for updates that repeat** — Check the render cascade metric while the component updates. If a state update inside useLayoutEffect triggers a cascade, move the update out of the layout effect or into a path that does not block paint. *When:* Components that update on every interaction or animation frame. The speaker shows this on a counter example.
- **Batch style reads and writes to prevent layout thrashing** — Watch the thrashing section and DOM churn metric while mutating many nodes. The speaker's example mutates inline styles on 600 nodes in one pass and gets stall warnings. The general fix implied is to separate reads from writes so the browser does not recalculate layout inside the loop. *When:* Any code that updates styles on many elements, such as lists, animations or filters.
- **Memoize components to cut redundant renders** — Wrap components that re-render unnecessarily with memoization so unchanged subtrees are skipped. Compare the P95 duration and frame jitter before and after. *When:* When P95 duration spikes or the main thread stays busy during interactions.

## Numbers
- Style churn example mutates inline styles on 600 nodes at once and produces stall warnings. ([4:16](https://youtu.be/fv9wj8nkDVM?t=256))
- Memoized example keeps frame rate locked near 60 fps while the unmemoized version lags (no measured values given). ([4:16](https://youtu.be/fv9wj8nkDVM?t=256))
- Heavy list example shows a CLS value described only as 'very high' with no number given. ([1:56](https://youtu.be/fv9wj8nkDVM?t=116))

## Hot takes
- Lighthouse is a 'broad brush' and component-level Storybook measurement is more surgical. This is asserted, not demonstrated against Lighthouse.
- Feature tour with no install steps, config, overhead numbers or before/after data. Mostly narration over a live demo.
- Title 'in Seconds!' oversells a six-minute walkthrough of a dashboard.
- useLayoutEffect-plus-setState is presented as always doubling per-frame work. The claim is generalized from one example.

## Tools mentioned
Storybook, GitHub Storybook performance add-on (unnamed in transcript), React, useLayoutEffect (React hook), Vue, Svelte, Web Components, Lighthouse, Chrome, Edge

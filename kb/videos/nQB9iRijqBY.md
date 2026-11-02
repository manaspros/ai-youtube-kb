# Svelte's Next Big Change? (server components soon?)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `nQB9iRijqBY` · [watch](https://youtu.be/nQB9iRijqBY) · **date:** 2025-11-02 · **length:** 4:26 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Rich Harris (Svelte author, quoted via his discussion) · **orgs:** Better Stack, Svelte, SvelteKit
- **topics:** dev-tools · **tags:** svelte, async, await, sveltekit, server-components, ssr, experimental

> Short walkthrough of Rich Harris's experimental Svelte async branch, which lets components use top-level await, await in $derived and in templates, and hints at future server components.

## Summary
Better Stack summarizes Rich Harris's discussion of an experimental async branch in Svelte. Today Svelte components fetch data three ways: onMount with local state, an await block with an isolated promise, or a SvelteKit load function on the server, each with drawbacks such as per-component spinners, prop drilling and manual invalidation. The experimental branch allows await in three places: top-level script, $derived expressions and template expressions. Any suspending expression must sit inside a Svelte boundary that shows a one-time pending fallback. Parallel awaits resolve together, and UI reading the same state pauses together. The team's first goal is async server-side rendering, which the host reads as a hint toward Svelte server components and SvelteKit navigation forking. The host stresses this is experimental and likely to land in Svelte 6.

## Key ideas
- **Svelte's experimental async branch lets components use the await keyword directly, possibly the first step toward Svelte-flavored server components** — The host frames the discussion as the big change: await in Svelte components, with server-component hints. ([0:00](https://youtu.be/nQB9iRijqBY?t=0))
- **Today's three data-loading patterns each have a drawback** — onMount with local state gives every component its own spinner; the await block still isolates each request so components flicker separately; SvelteKit load functions give good UX but bring prop drilling, type friction and manual invalidation on reactive updates. ([0:00](https://youtu.be/nQB9iRijqBY?t=0))
- **await is allowed in three spots: top-level script, $derived expressions and template expressions** — Top-level await in script is plain JavaScript; a derived value can await a promise; markup can await a promise directly. ([1:09](https://youtu.be/nQB9iRijqBY?t=69))
- **Any suspending expression must live inside a Svelte boundary, which renders a one-time pending fallback** — The boundary is placed high in the app. The requirement may be relaxed later. The pending snippet shows the loading state. ([1:09](https://youtu.be/nQB9iRijqBY?t=69))
- **Parallel awaits within one script run concurrently** — Three 2-second fetch calls in one script finish in about 2 seconds total, and splitting them into three components gives the same result. ([2:21](https://youtu.be/nQB9iRijqBY?t=141))
- **The runtime coordinates UI that reads the same async state** — Parts of the UI reading the same state pause together so the header does not update while the body shows stale data; a focused input waiting on async work does not freeze the rest of the UI. ([2:21](https://youtu.be/nQB9iRijqBY?t=141))
- **First goal is async SSR, which could enable speculative navigation forking in SvelteKit** — The boundary could render real content on the server instead of only a fallback; the host connects this to pre-rendering off-screen routes and client-side server utilities. ([3:42](https://youtu.be/nQB9iRijqBY?t=222))

## Techniques
- **Top-level await in a component script behind a boundary** — In the component script, await the fetch and data.json() directly, then use the result. Wrap the component (or the app root) in a Svelte boundary and provide a pending snippet for the loading UI. *When:* Replacing onMount-plus-loading-flag boilerplate in components that need one fetch, once the async branch is available.
- **Await a promise inside $derived** — Create the promise in script (for example a data promise), then in a $derived expression await it. The boundary and loading indicator are still required. *When:* Deriving a value from async data without manual state.
- **Await inside template expressions** — Use await on a promise directly in markup rather than moving logic into the script tag. *When:* Simple lazy loads in markup, such as an image preload or a lazily imported component.
- **Start independent requests together to avoid waterfalls** — Kick off several fetch calls in the same script (or across sibling components) so they run in parallel; the page waits roughly for the slowest one. *When:* Several independent data sources feed one view.

## Numbers
- Baseline examples use a 2-second API wait before data appears ([0:00](https://youtu.be/nQB9iRijqBY?t=0))
- Three parallel 2-second fetch calls produce about a 2-second total wait, not about 6 seconds ([2:21](https://youtu.be/nQB9iRijqBY?t=141))

## Hot takes
- The title frames this as Svelte's next big change and asks whether server components are coming; the body says it is experimental, not production ready, and that server components are only a hint from the first async SSR goal.
- The host calls the approach simpler than React, Vue and Solid without showing a comparison.
- Thin substance for a 4-minute video: it reads a long discussion document and demonstrates three small examples.

## Tools mentioned
Svelte (experimental async branch), SvelteKit, Svelte 6 (expected destination, not released)

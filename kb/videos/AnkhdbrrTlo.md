# Why Ripple.js Is The Most Interesting Framework of 2025

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `AnkhdbrrTlo` · [watch](https://youtu.be/AnkhdbrrTlo) · **date:** 2025-11-02 · **length:** 4:22 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack
- **topics:** dev-tools · **tags:** ripple.js, front-end-framework, fine-grained-reactivity, jsx, scoped-styles, tailwind, llms-txt, react-alternative

> A four-minute walkthrough of Ripple.js, an early-stage front-end framework with JSX-like syntax, compiled reactivity and no virtual DOM. It is a quick tour of the API, not an evaluation.

## Summary
The presenter introduces Ripple.js as an early-development front-end framework that combines fine-grained reactivity, scoped styles and JSX-like syntax, and asks whether the world needs another framework alongside React. The walkthrough builds a counter, a reusable button component with children and an onClick prop, scoped styles, and an effect. It then shows a to-do list using tracked collections (array, object, set, map) and a form submit handler, which the presenter presents as needing no hooks or complex state management. The video notes that Ripple compiles through a VS Code extension (the presenter could not get the LSP working in Neovim), supports Tailwind out of the box, and offers context for sharing reactive values, a portal, a suspense boundary, an experimental router and an llms.txt file for feeding its docs to agents. The presenter closes by saying the framework lacks React's plugin ecosystem and, as far as they know, cannot do server rendering like React Server Components. There are no benchmarks, comparisons or production experience in the video.

## Key ideas
- **Ripple positions itself as a new front-end framework that borrows the best of earlier frameworks (fine-grained reactivity, scoped styles, JSX-like syntax), and the presenter questions whether a new framework is needed.** — Early development stage; the speaker frames the question of differentiation against React, which is popular with both humans and AI tools. ([0:00](https://youtu.be/AnkhdbrrTlo?t=0))
- **Ripple uses a `component` keyword and compiles through a Ripple extension to browser-ready code. It is a JSX superset, and templates are statements, so expressions need braces.** — The app mounts to an element with id root in index.ts, as in React. The presenter reports the VS Code extension works but the LSP did not work in Neovim. ([0:56](https://youtu.be/AnkhdbrrTlo?t=56))
- **Reactivity is explicit: `track()` creates a tracked value, and the `@` symbol reads it in templates. Event handlers work like React's onClick.** — The counter example needs no hooks. Reactive collections do not need `@` when referenced. ([0:56](https://youtu.be/AnkhdbrrTlo?t=56))
- **Composition uses a plain component that takes children and an onClick prop, so repeated button classes are written once.** — Styling uses `class` rather than React's `className`. Ripple also supports scoped styles through a style tag in the component, and an `effect` function for side effects. ([0:56](https://youtu.be/AnkhdbrrTlo?t=56))
- **There is no virtual DOM. The whole app renders once, and only the reactive elements update when state changes.** — The presenter states this as the reason updates are fast. No timings or benchmarks are given. ([2:23](https://youtu.be/AnkhdbrrTlo?t=143))
- **Tracked collections (array, object, set, map) are fully reactive, so a to-do list needs a tracked array, a regular if/for-of in the template and a form submit handler outside the component.** — The presenter describes this as 'no hooks and no complex state management'. Pulling a reactive value out of the component to use globally throws an error; sharing across components uses context. ([2:23](https://youtu.be/AnkhdbrrTlo?t=143))
- **Ripple ships a portal, a suspense boundary, an experimental router, and an llms.txt file that packages its docs for coding agents.** — The presenter likes the llms.txt file, which provides all the important Ripple docs to an agent of the user's choice. ([3:46](https://youtu.be/AnkhdbrrTlo?t=226))
- **The presenter's stated limitations are a missing plugin ecosystem compared with React, and, as far as they know, no server-side rendering like React Server Components.** — The presenter calls it a promising start and is looking forward to 1.0. The video does not test or quantify either point. ([3:46](https://youtu.be/AnkhdbrrTlo?t=226))

## Techniques
- **Component with track() and @ reads** — Declare `component App() { let count = track(0); ... }` (the `track` import is needed, and `track` is imported from ripple). Render the value as `{@count}` and update it through an onClick handler. Template expressions need braces because templates are statements. *When:* Local component state in Ripple, when you want explicit reactivity without hooks.
- **Tracked collections for lists** — Create `tracked` arrays (also object, set and map) for list state. Use a plain `if` and `for...of` in the template. Read collection values without `@`. Push into the array in a submit handler defined outside the component, then reset the form. *When:* Dynamic lists and forms, such as a to-do app, where you want to avoid hooks and manual state wiring.
- **Wrapper component for repeated controls** — Make a component that accepts `children` and an `onClick` prop and renders the shared classes. Use it in place of repeated button markup. *When:* Several buttons or controls that share styling and behaviour.
- **Scoped styles and effects** — Give an element a class, then add a style tag inside the component. Use the `effect` function for side effects. *When:* Component-local CSS without a global stylesheet, and effects that must react to tracked state.
- **Sharing reactive state via context** — Do not export a tracked value to module scope (it throws). Use Ripple's context to share reactive values between components. *When:* State needed by several components in a tree.
- **Feeding framework docs to coding agents via llms.txt** — Ripple publishes an llms.txt file with all its docs. Give that file to your coding agent as context. *When:* Working with a new or niche framework where agents would otherwise lack current docs. The presenter demonstrates no test of this.

## Hot takes
- The title calls Ripple 'the most interesting framework of 2025'. The video gives a short API tour with no benchmarks, comparisons or production use, so the claim is not supported.
- The presenter says Ripple is 'super fast' without any measurement in the video.
- The presenter says there are no hooks or complex state management, but compares this only to a single to-do example.
- The presenter says Ripple cannot be used on the server like React Server Components, but qualifies it with 'as far as I know'.

## Tools mentioned
Ripple.js, React, Svelte, Tailwind CSS, VS Code (Ripple extension), Neovim, llms.txt, React Server Components

## Relevance to our work
- **general** (1/3): The llms.txt pattern (a single docs file for coding agents) is a small, reusable idea for context engineering. → *If we write our own docs for agents, consider publishing an llms.txt-style index of the internal docs we want Claude Code to read.*

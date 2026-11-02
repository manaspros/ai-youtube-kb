# Vue 3.6 ALPHA is out! and it's FAST! — Vapor

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `FvzAvnVfgoA` · [watch](https://youtu.be/FvzAvnVfgoA) · **date:** 2025-11-02 · **length:** 5:01 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Bernard · **orgs:** Better Stack, Vue, Svelte, Vuetify
- **topics:** dev-tools · **tags:** vue, vue-3.6, vapor-mode, frontend, javascript, performance, benchmarks, svelte, npm, vuetify

> Short overview of Vue 3.6 alpha's headline feature, Vapor mode (a compiler strategy that drops the virtual DOM), with opt-in steps, a single benchmark, and alpha install caveats.

## Summary
Better Stack's five-minute overview of the Vue 3.6 alpha, whose main change is Vapor mode, a compilation strategy that skips the virtual DOM. The speaker says the release otherwise contains only bug fixes for CSS variables, reactivity and the scheduler. He explains that Vapor compiles templates to static DOM templates that are cloned at runtime and updated through direct text-node bindings, instead of building vnode trees and diffing them. He cites a baseline size drop from about 50 KB to about 6 KB, and a single benchmark on Vue 3.5.13 (1.26 for VDOM vs 1.11 for Vapor) that he says is close to Svelte, while admitting no updated 3.6 benchmark exists yet. Vapor is opt-in per component through a vapor attribute on script setup, and it can be mixed with VDOM components via an interop plugin, which matters for libraries such as Vuetify. Local trial needs npm with the legacy peer deps flag because the alpha conflicts with existing dependencies. The practical content is a short setup guide; the performance claims rest on thin evidence.

## Key ideas
- **Vue 3.6 alpha's one major feature is Vapor mode; the rest are bug fixes for CSS vars, reactivity and the scheduler.** — Speaker frames Vapor as the release's headline change and the reason for the video. ([0:00](https://youtu.be/FvzAvnVfgoA?t=0))
- **Vapor is a compilation strategy that removes the virtual DOM, in development since January 2023.** — Speaker says the goal is smaller, faster apps by avoiding VDOM diffing. ([0:08](https://youtu.be/FvzAvnVfgoA?t=8))
- **Claimed baseline size drops from about 50 KB (VDOM) to about 6 KB (no VDOM), which the speaker reports as 88% less.** — This is the framework's baseline size as stated by the speaker, not measured app runtime performance. ([0:55](https://youtu.be/FvzAvnVfgoA?t=55))
- **Vapor is opt-in per component: add a vapor attribute to script setup. The earlier idea of a .vapor.view file extension was dropped.** — Mixing Vapor and non-Vapor files under one extension was judged messy in file explorers. ([0:55](https://youtu.be/FvzAvnVfgoA?t=55))
- **Mechanism: VDOM templates build a vnode tree and diff it on state change; Vapor emits reusable static DOM templates, grabs references to the exact text nodes, and binds reactive values to them directly via a render effect calling setText.** — The speaker compares this to assigning a value to a variable rather than running a virtual DOM diff. ([2:13](https://youtu.be/FvzAvnVfgoA?t=133))
- **The only benchmark shown is a weighted geometric mean of 1.26 for Vue 3.5.13 VDOM vs 1.11 for Vapor, which the speaker calls very close to Svelte.** — The speaker says no updated 3.6 benchmark is available yet and expects 3.6 to improve further. He does not state the metric's direction or the Svelte figure. ([3:16](https://youtu.be/FvzAvnVfgoA?t=196))
- **Vapor and VDOM components can coexist through an interop plugin, which matters for UI libraries that do not support Vapor yet.** — Speaker names Vuetify as the motivating example. The alpha is not officially supported by all tools. ([3:16](https://youtu.be/FvzAvnVfgoA?t=196))

## Techniques
- **Opt a single SFC into Vapor** — Add the vapor attribute to the script block: <script setup vapor>. No file extension change is needed. *When:* Incrementally adopting Vapor on performance-sensitive components while the rest of the app stays on VDOM.
- **Install the Vue 3.6 alpha in an existing project** — Install with npm using the legacy peer deps flag (npm install --legacy-peer-deps) to bypass peer dependency conflicts. The speaker does not show the exact vue version specifier. *When:* Trying Vapor locally in an app whose dependencies do not yet declare 3.6 support.
- **Mix Vapor and VDOM with the interop plugin** — Install the Vapor interop plugin in the app (captions say 'vapor interrupt plugin'; the exact package name is not shown) so Vapor and VDOM components can render together. *When:* Using a UI library such as Vuetify that does not yet support Vapor.
- **Start a new Vapor app** — Use the Vapor app scaffolder (captions say 'Create Vapor app'; the exact command is not shown), then add the vapor attribute to single-file components. *When:* Greenfield experiments with Vapor and no legacy VDOM dependencies.
- **Confirm Vapor is active** — After building, inspect the components in the browser to check that they run in Vapor mode. The speaker does not show the exact inspection method. *When:* Verifying the opt-in actually took effect before benchmarking.

## Numbers
- Vapor was first introduced in January 2023 (speaker's statement). ([0:08](https://youtu.be/FvzAvnVfgoA?t=8))
- VDOM baseline app size about 50 KB; without VDOM about 6 KB, stated as 88% less (baseline size, not runtime speed). ([0:55](https://youtu.be/FvzAvnVfgoA?t=55))
- Weighted geometric mean benchmark: Vue 3.5.13 VDOM 1.26 vs Vue Vapor 1.11 (lower-is-better direction not stated by the speaker). ([3:16](https://youtu.be/FvzAvnVfgoA?t=196))

## Hot takes
- The 'it's FAST' title rests on one benchmark from Vue 3.5.13, not 3.6. The speaker concedes no updated benchmark exists yet.
- The 88% figure is baseline bundle or runtime size, not measured app speed, yet the speaker presents it as the headline gain.
- Vapor is alpha, and the speaker's own setup needs a legacy peer deps flag, so production readiness is not established by this video.

## Tools mentioned
Vue 3.6 (alpha), Vue Vapor mode, Vue 3.5.13 (benchmark baseline), Svelte (comparison only), npm (--legacy-peer-deps), Vuetify, Vapor interop plugin, Vapor app scaffolder (create-vapor-app)

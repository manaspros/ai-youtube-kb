# You’re Writing Vue Wrong — Use This Instead (Options vs Composition API)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `XigQ813IMs0` · [watch](https://youtu.be/XigQ813IMs0) · **date:** 2025-11-02 · **length:** 5:40 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** Presenter (Better Stack host, unnamed in transcript) · **orgs:** Better Stack, Vue.js
- **topics:** dev-tools · **tags:** vue, composition-api, options-api, script-setup, composables, frontend, javascript, code-organization

> Better Stack walkthrough comparing Vue's Options API and Composition API (script setup) on structure, scalability, readability, and whether mixing them is worth doing; mostly opinion with a light code walkthrough.

## Summary
The video explains why Vue has two component APIs. Options API groups state in data, methods, computed and lifecycle hooks, which reads easily but spreads a feature's logic across the component as it grows. Composition API, here shown with setup and script setup, uses ref and computed inside one setup function, so related logic stays together and can be moved into composables for reuse. The speaker argues that readability complaints about Composition API mostly reflect how code is structured, not the API itself. He recommends Options API for simple components where scalability is not a priority, and Composition API for larger apps and for developers new to Vue because it pushes better structure. Mixing both in one component is possible but discouraged for new code, except during migrations. The video gives no benchmarks and no performance comparison, and the code shown is minimal (a counter with a doubled computed value).

## Key ideas
- **Options API splits one feature's logic across data, methods, computed and lifecycle hooks, which hurts maintainability as components grow.** — Speaker says a feature (loader, counter, API fetch) ends up in several option blocks, so large components mean jumping between sections. ([1:19](https://youtu.be/XigQ813IMs0?t=79))
- **Composition API groups related logic together in setup, and reusable pieces can move into composables.** — Ref holds reactive state and computed holds derived state; logic for one feature stays in one place and can be extracted. ([0:00](https://youtu.be/XigQ813IMs0?t=0))
- **script setup is a second way to write Composition API, removing the export default and setup wrapper.** — Code reads like plain JavaScript, with no export default or explicit setup function. ([1:19](https://youtu.be/XigQ813IMs0?t=79))
- **Speaker attributes hard-to-read Composition API code to how it is written, not to the API itself.** — Composition API lets the author choose structure and forces code to look like ordinary JavaScript, so messy results are a code-organization problem. ([2:24](https://youtu.be/XigQ813IMs0?t=144))
- **Recommendation depends on complexity and scale: Options API for simple components, Composition API for scalable code and for newcomers.** — Speaker says he is biased toward Options API because he has used it longer. He still recommends Composition API for beginners because it teaches better structure. ([2:24](https://youtu.be/XigQ813IMs0?t=144))
- **Mixing Options API and Composition API in one component is possible but usually a bad idea.** — Mixing brings back the split across sections, and this is undefined inside setup. Mixing is reasonable only when migrating an old component and adding new logic. ([3:43](https://youtu.be/XigQ813IMs0?t=223))

## Techniques
- **Group logic by feature in Composition API setup** — Declare ref() for reactive state and computed() for derived values in one setup function, so each feature's state, derived values and functions sit together rather than in separate data/methods/computed blocks. *When:* Components are large or will grow, or several features share one component.
- **Extract shared logic into composables** — Move related setup logic (state, computed, functions) into a separate function so other components can call it. *When:* The same feature logic is needed in more than one component.
- **Use script setup for Composition API** — Write component logic directly at the top level of a script block marked setup, with no export default and no explicit setup function. *When:* Writing new Composition API components.
- **Avoid mixing APIs in new components** — Pick one API per component. Only mix them when migrating an existing Options API component and adding new logic with Composition API. *When:* Starting a new component, or deciding how to handle a legacy component during migration.

## Hot takes
- Messy Composition API code is the developer's fault, not Vue's ("skill issue"); this is opinion, not evidence.
- Mixing Options and Composition API in one component is discouraged, though Vue supports it.
- Composition API is recommended for anyone new to Vue, even though the speaker has used Options API longer.

## Tools mentioned
Vue.js, Vue Composition API, Vue Options API, script setup

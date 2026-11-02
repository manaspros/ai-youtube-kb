# 5 Vue.js BEST Practices in 4 Minutes

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `QB1p2iuQm_0` · [watch](https://youtu.be/QB1p2iuQm_0) · **date:** 2025-11-02 · **length:** 4:32 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack
- **topics:** dev-tools · **tags:** vue, vuejs, composition-api, composables, slots, props, emits, typescript, frontend, best-practices

> Four-minute Vue.js listicle on reusable components, slots, composables, props/emits and prop validation with TypeScript; generic frontend advice with no bearing on our projects.

## Summary
A short Better Stack video (4:32, dated 2025-11-02) presents five Vue.js practices as a quiz-style list. It argues for reusable components, using slots (including named and conditionally rendered slots) to keep a reusable component's structure while letting the parent fill in content. It recommends moving stateful logic out of components into composables kept in a composables folder, using a counter example built on a reactive ref with increment and decrement methods. For props and emits, it suggests a modal that takes a visible prop and emits a close event, keeping the modal decoupled while the parent stays in control. It ends by recommending prop validation, with the Composition API using typed props via a TypeScript interface so the editor flags wrong types before runtime. The speaker says state management, performance and testing are out of scope. No code is fully shown on screen in the transcript, and there are no benchmarks or tradeoff discussion.

## Key ideas
- **Build reusable components and avoid duplicated UI** — A reusable component (the example is a subscribe button) can be dropped in across the app, so a change in one place propagates to every use. ([0:00](https://youtu.be/QB1p2iuQm_0?t=0))
- **Use slots to reuse structure while letting parents supply content** — A button keeps the same look but takes different labels; slots inject HTML or raw text. Named slots and conditionally rendered slots (only when content is provided) add optional parts such as an icon. ([0:58](https://youtu.be/QB1p2iuQm_0?t=58))
- **Move stateful logic into composables** — Cramming logic into components leads to bloated, copy-pasted functions. A composable is a function built on the Composition API that holds reusable stateful logic; the example is a useCounter that exposes a reactive count plus increment and decrement. ([0:58](https://youtu.be/QB1p2iuQm_0?t=58))
- **Keep composables in a dedicated folder** — The speaker keeps composables in their own folder so logic stays separate from components and is easy to find and import. ([1:30](https://youtu.be/QB1p2iuQm_0?t=90))
- **Make components controlled by props and emits** — Overusing props or underusing emits is a common mistake. A modal should accept a visible prop to control opening and emit a close event on the X or cancel button, so the parent controls it. ([2:09](https://youtu.be/QB1p2iuQm_0?t=129))
- **Extract shared modal state into a composable** — Login, product and checkout pages that all show popups can share one composable for the open state and methods instead of recreating a ref and two methods each time. ([2:40](https://youtu.be/QB1p2iuQm_0?t=160))
- **Validate props, since wrong types fail silently** — Without validation, passing a number where a string is expected still renders, just wrongly. The speaker argues for prop validation. ([3:28](https://youtu.be/QB1p2iuQm_0?t=208))
- **Use TypeScript interfaces for props with the Composition API** — Defining props with a TypeScript interface lets the code editor warn about wrong types before the app runs, which is easier than hand-written runtime prop type definitions. ([3:28](https://youtu.be/QB1p2iuQm_0?t=208))

## Techniques
- **Slots for reusable component structure** — Build a generic button component with a default slot for the label. Use named slots for optional parts such as an icon, and render the icon slot conditionally only when content is supplied. *When:* When several places need the same component structure with different content.
- **useCounter-style composable** — Put a reactive count and increment/decrement methods in a function in a composables folder. Import it in the component and use the returned state and methods. *When:* When stateful logic is repeated across components or pages.
- **Visible prop plus close event for modals** — The modal accepts a visible prop and emits a close event from the X and cancel buttons. The parent owns the open state. *When:* When a reusable modal or popup must stay decoupled from the page that opens it.
- **Modal open-state composable** — Wrap the popup open/close ref and its two methods in a composable and import it on each page that needs a popup. *When:* When login, product, checkout or other pages each need the same popup behavior.
- **Typed props via TypeScript interface** — Declare props with a TypeScript interface in the Composition API instead of hand-written prop type checks. The speaker does not show the exact syntax. *When:* When you want the editor to flag wrong prop types before running the app.

## Hot takes
- Titled 'BEST practices' but the content is generic frontend hygiene, with no benchmarks, tradeoffs or counterexamples.
- The subscribe-button joke and call-to-action filler take up part of the runtime; quality is capped low because substance is thin.

## Tools mentioned
Vue.js, Vue Composition API, TypeScript

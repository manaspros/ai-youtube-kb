# Vuetify vs PrimeVue — BEST UI Framework Breakdown

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `CL8xW84S-lA` · [watch](https://youtu.be/CL8xW84S-lA) · **date:** 2025-11-02 · **length:** 4:30 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Bernard · **orgs:** Better Stack
- **topics:** dev-tools · **tags:** vue, vuetify, primevue, tailwind-css, ui-component-libraries, material-design, theming, unstyled-components, pass-through-attributes

> Better Stack compares Vuetify (opinionated, Material Design, polished out of the box) with PrimeVue (unstyled, highly customizable, pairs with Tailwind) for Vue.js projects.

## Summary
Bernard from Better Stack compares two Vue.js component libraries, Vuetify and PrimeVue, and frames the choice as one of opinionated versus customizable. He shows a Vuetify landing page and a Vuetify theme change in the global config (dark default theme, green primary, gray secondary, ripple disabled). He says Vuetify's utility classes and built-in layouts are a strength, but that customizing its components takes a lot of documentation lookup and it has a learning curve, such as the dollar-sign alias confusion. PrimeVue is presented as unopinionated: its unstyled mode drops built-in styling so the developer styles components through pass-through (pt) attributes, and it has a larger component set including data tables with sorting and filtering, charts and org trees. The speaker built a PrimeVue landing page with Tailwind and says it gives more design control. He notes PrimeVue has no built-in layout utilities, so grids need Tailwind or custom CSS. His verdict: Vuetify for structured internal tools and dashboards, PrimeVue for flexibility and bespoke design. The video gives no benchmarks, versions or code walkthrough beyond the on-screen demos, so it is a surface-level comparison.

## Key ideas
- **Vuetify is built on Material Design and gives a clean, familiar UI quickly, but the speaker calls its default look dated for current design standards.** — Vuetify ships a polished, opinionated look. The speaker says it suits internal tools and dashboards where the Material aesthetic fits, but not distinctive branded products. ([0:00](https://youtu.be/CL8xW84S-lA?t=0))
- **Vuetify theming is set in its global config (usually in the plugins folder).** — The speaker sets the default theme to dark, adjusts colors (primary green, secondary gray) and disables the button ripple effect via a ripple setting. Light/dark switching and utility classes are available out of the box. ([0:00](https://youtu.be/CL8xW84S-lA?t=0))
- **Heavy Vuetify customization costs time in docs and search.** — Per-component styling is possible, but the speaker says customizing Vuetify components can take more time than building components from scratch. He also cites confusion over the dollar-sign alias in its API as an example of the learning curve. ([1:09](https://youtu.be/CL8xW84S-lA?t=69))
- **PrimeVue is unopinionated and is aimed at custom design systems.** — It does not impose Material Design. Unstyled mode stops components from adding built-in style classes, and pass-through (pt) attributes let the developer style each part. ([2:31](https://youtu.be/CL8xW84S-lA?t=151))
- **PrimeVue has a wider component set, including advanced components.** — The speaker counts more than 92 components for PrimeVue against about 76 for Vuetify (he hedges with 'I think'). Advanced ones include data tables with sorting and filtering, charts and organization trees. ([1:09](https://youtu.be/CL8xW84S-lA?t=69))
- **Layout tooling differs: Vuetify has utility classes and grids, PrimeVue does not.** — With PrimeVue, layouts and grids need Tailwind CSS or hand-written CSS. The speaker recommends pairing PrimeVue with Tailwind for flexibility. ([3:40](https://youtu.be/CL8xW84S-lA?t=220))
- **Verdict depends on project needs and how much styling control is wanted.** — Vuetify for a polished, structured UI that follows Material Design with built-in layouts. PrimeVue for custom designs, a large component library, and a custom styling system such as Tailwind. ([3:40](https://youtu.be/CL8xW84S-lA?t=220))

## Techniques
- **Vuetify global theme setup** — In the Vuetify global config (usually in the plugins folder), set the default theme to dark, adjust the color palette (primary green, secondary gray), and set ripple to false to remove the button ripple. The speaker does not show the full config keys in the transcript. *When:* When you want a quick branded look on Vuetify without rewriting components.
- **PrimeVue unstyled mode with pass-through attributes** — Enable unstyled mode so PrimeVue components add no built-in style classes, then style each component part through the pt (pass-through) attribute. *When:* When the design must be fully custom, for example a brand-specific UI or a design built on Tailwind.
- **Tailwind for layout on top of PrimeVue** — Since PrimeVue has no layout or grid utilities, build grids and spacing with Tailwind CSS (or custom CSS) and use PrimeVue for interactive components. *When:* When you choose PrimeVue for flexibility but still need fast, responsive layouts.
- **Build from scratch for a strongly branded UI** — Skip the component library and write your own components when the goal is a distinctive brand and customizing library components would take longer than building them. *When:* When the design differs strongly from Material Design or from any library's defaults.

## Numbers
- PrimeVue provides more than 92 components (speaker's figure). ([1:09](https://youtu.be/CL8xW84S-lA?t=69))
- Vuetify has about 76 components (speaker says 'I think', so approximate). ([1:09](https://youtu.be/CL8xW84S-lA?t=69))
- Video length is 4:30; no benchmarks, bundle sizes, performance or adoption figures are given. ([0:00](https://youtu.be/CL8xW84S-lA?t=0))

## Hot takes
- Vuetify looks dated next to current design standards, in the speaker's words, though it is fine for internal tools and dashboards.
- For a unique brand, build components from scratch instead of customizing a library's components.
- PrimeVue is the better choice when customization matters and the team uses Tailwind.
- Thin substance behind a hype title ('BEST UI Framework Breakdown'): a short opinion comparison with no versions, benchmarks, or code shown in the transcript, so quality is capped at 2.

## Tools mentioned
Vue.js, Vuetify, PrimeVue, Tailwind CSS, Material Design, ChatGPT (mentioned as a help source)

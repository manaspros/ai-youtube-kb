# Claude Code Can Finally Make Beautiful Websites

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `idccdssOZQ8` · [watch](https://youtu.be/idccdssOZQ8) · **date:** 2025-11-02 · **length:** 5:59 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed AI LABS host (narrator, on-screen demo) · **orgs:** Airbnb (cloned page used as the demo subject)
- **topics:** vibe-coding-app-building, product-ux, coding-agents · **tags:** ui-design, vibe-coding, shadows, color-palette, responsive-layout, design-principles, prompting, before-after-demo

> Three UI design principles (depth through layered color and shadows, box-based responsive layout, and a four-role color palette) for making AI-generated sites look better, shown on a cloned Airbnb-style page.

## Summary
The host argues that AI-generated websites look flat and generic unless the prompter knows basic UI design, and proposes three principles to apply through prompts. The demo starts from a screenshot-based clone of an Airbnb-style page, which is used as the baseline for before/after comparisons. Principle one is depth: build three to four shades of the base color, put darker shades in the background and lighter ones in front, and use a dual (light and dark) shadow with a subtle gradient, especially on dark-mode components. Principle two is layout: treat the page as a parent-child system of flexible boxes so that elements stop splitting and overflowing, and make responsiveness about reprioritizing content (a carousel for cards, prioritized search options) rather than shrinking it. Principle three is color: define a palette with a primary color for calls to action, a secondary color for subtle actions, neutrals for most of the UI, and semantic colors (green success, yellow warning, blue info, red error or destructive). The speaker says the implementation prompts are in the video's linked resources, which are not shown in the transcript, so the exact prompts are not available here. The content is practical but shallow, and the title and many asides are hype.

## Key ideas
- **Start from a baseline, then apply one design principle at a time and compare before and after.** — The demo uses a screenshot-cloned existing page rather than generating a new one, and shows each change against it. The speaker says a fresh build was skipped because of limited context-engineering budget. ([0:00](https://youtu.be/idccdssOZQ8?t=0))
- **Depth comes from layered shades of one base color, not from borders.** — Create three to four shades of the base color (white in the demo). Darker shades sit in the background and lighter shades in front, so elements are separated by tone and borders can be dropped. ([1:03](https://youtu.be/idccdssOZQ8?t=63))
- **Use a two-layer shadow with three depth levels, plus a subtle gradient.** — Combine a light and a dark shadow to simulate natural lighting, with three elevation levels. The gradient is strongest on dark-mode components, where the top shadow is slightly lighter than the one below. ([1:03](https://youtu.be/idccdssOZQ8?t=63))
- **Layout should be a system of flexible parent-child boxes.** — Overflowing cards and sections split into fragments were fixed by having the prompt rebuild the layout as nested boxes that respond to size changes. The search bar split was corrected and the search icon separated. ([2:32](https://youtu.be/idccdssOZQ8?t=152))
- **Responsive design means reprioritizing content, not shrinking it.** — On mobile, the search bar keeps the most important options and cards move into a carousel that keeps their shape, rather than being squeezed. ([3:28](https://youtu.be/idccdssOZQ8?t=208))
- **A palette has four color roles.** — Primary: the color that stands out most, reserved for calls to action. Secondary: a complementary color for subtle actions or new features. Neutral: black, white and gray, which fill most of the UI. Semantic: green for success, yellow for warnings, blue for information, red for errors or destructive actions. ([3:28](https://youtu.be/idccdssOZQ8?t=208))
- **Most of the UI should not be colored.** — Even with a full palette, the speaker says the neutral colors should make up most of the interface, with accent colors used sparingly for attention, notifications and states. ([4:56](https://youtu.be/idccdssOZQ8?t=296))

## Techniques
- **Color-layer depth instead of borders** — Pick the base color (white here) and generate three to four tints or shades. Assign darker shades to background surfaces and lighter shades to foreground cards and controls. Remove the borders that were separating elements. *When:* Flat AI-generated UIs where everything sits on one surface and borders are doing all the separation work.
- **Dual shadow with depth levels and a gradient** — Give each elevated element a light shadow and a dark shadow together, with three distinct elevation levels. Add a subtle top-to-bottom gradient on layered components, most visibly in dark mode. The video does not show exact CSS values, so the prompt in the linked resources would be the source. *When:* Components look like a single flat plane, or dark-mode cards need separation.
- **Flexible box layout with parent-child structure** — Ask the model to restructure the layout so every region is a nested flex or grid box that can resize, and to fix sections that were split or overflowing. Then check resize behavior at different widths. *When:* Generated pages break into fragments, overflow their cards, or fail to resize.
- **Priority-based responsiveness** — For each viewport, decide which items matter most. Keep those visible in the primary position and move secondary items into a carousel or a collapsed view, rather than scaling everything down. *When:* Mobile views where cards are squashed or lower-priority controls crowd the top.
- **Four-role palette** — Define primary (call to action), secondary (subtle action or highlight), neutral (most of the UI), and semantic colors (success green, warning yellow, info blue, error or destructive red). Apply each role consistently across the page. The speaker points to a palette-browsing site, named in the transcript as Colors, and to an article linked in the description. *When:* Generated sites use arbitrary accent colors or use color for everything, so meaning is unclear.
- **Prompt per principle, with before/after comparison** — Take a screenshot of an existing page as the baseline. Apply one principle at a time through the model using its prompt, then compare the result to the previous version. The speaker's implementation prompts are said to be in the video resources and are not in the transcript. *When:* Iterating on the look of a generated UI and needing to see which change caused which effect.

## Numbers
- Three to four shades of the base color for layered depth. ([1:03](https://youtu.be/idccdssOZQ8?t=63))
- Two shadow layers (light and dark) with three depth levels. ([1:03](https://youtu.be/idccdssOZQ8?t=63))
- Four palette color roles: primary, secondary, neutral, semantic (with four semantic colors: green, yellow, blue, red). ([3:28](https://youtu.be/idccdssOZQ8?t=208))
- Video length 5:59. Opening '98.7% of all vibe coders' line is a joke, not a sourced statistic. ([0:00](https://youtu.be/idccdssOZQ8?t=0))

## Hot takes
- Good UI depends on design fundamentals (layering, contrast, palette roles), not on prompt tricks. The speaker says you 'actually need to know your stuff' before prompting.
- The title overpromises. The substance is a general design-principles overview, and the concrete prompts that would make it reproducible are only linked in the description, not shown.
- The shadow and gradient advice is presented as a way to make a generated UI look like it belongs to a funded product, but the video shows no measured result beyond side-by-side visuals.

## Tools mentioned
Claude Code (named in the title only; the transcript does not name it), Colors (palette-browsing site, named in the transcript, no URL given), Airbnb-style page clone (demo subject, not a tool)

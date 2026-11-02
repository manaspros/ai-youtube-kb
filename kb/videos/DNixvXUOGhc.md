# CSS Just Got 10 New Features (and they're actually good)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `DNixvXUOGhc` · [watch](https://youtu.be/DNixvXUOGhc) · **date:** 2025-11-02 · **length:** 11:21 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, Google Chrome dev team
- **topics:** dev-tools · **tags:** css, html, popover-api, starting-style, details-element, interpolate-size, field-sizing, paint-order, light-dark, anchor-positioning, align-content, frontend

> Better Stack walkthrough of ten recent CSS features (popover, @starting-style, interpolate-size, field-sizing, light-dark(), anchor positioning, and more) that replace JavaScript for common UI patterns.

## Summary
The presenter tours about ten recent CSS features, each shown in a small live demo with no JavaScript for the styling. Popovers work with a popover attribute on the panel and a popovertarget attribute on the trigger, with Escape and click-away closing built in. @starting-style supplies the pre-first-render state so entry animations work without script, but it must come after the normal rule in the stylesheet or it gets overridden. The details element gains flex display for horizontal accordions and a ::details-content pseudo-element for animating open and close. interpolate-size with allow-keywords lets height and width transition to auto and intrinsic keywords. field-sizing: content makes textareas, selects and inputs grow or shrink with their content. paint-order: stroke fill fixes text stroke overlap, light-dark() picks colours from the colour scheme, anchor positioning places an element relative to a named anchor in about four lines of CSS, and align-content: center now centres block children vertically. The video is a feature tour rather than an analysis, and it does not test browser support or edge cases beyond the demos.

## Key ideas
- **A popover needs no Popper.js: put the popover attribute on the panel and popovertarget (matching the panel's ID) on the button. Escape and click-away close it automatically.** — Built-in popover behaviour replaces the old JavaScript positioning and dismissal logic for simple popovers. ([0:00](https://youtu.be/DNixvXUOGhc?t=0))
- **Popover open/close animations use translate plus transition, but the entry animation needs @starting-style, which defines the style before the first style update.** — Without it, the element jumps straight to its open state on first render. @starting-style must sit after the base rule in the CSS, or the base rule overrides it. It also applies when display goes from none to visible. ([1:12](https://youtu.be/DNixvXUOGhc?t=72))
- **The details element can now be a horizontal accordion and can be styled with ::details-content.** — Setting display: flex and flex-direction: row on details lets the summary and content sit in separate columns. The ::details-content pseudo-element holds all non-summary children and can be transitioned between height 0 and an open height. ([2:17](https://youtu.be/DNixvXUOGhc?t=137))
- **interpolate-size: allow-keywords enables animating to auto and intrinsic sizes such as min-content, max-content, fit-content and calc-size().** — The speaker enables it on the root for the whole document, because it is off by default and numeric-only for backwards compatibility. Previously the height or width had to be computed in JavaScript or hard-coded. ([4:51](https://youtu.be/DNixvXUOGhc?t=291))
- **field-sizing: content gives textareas, selects and inputs content-based sizing with no JavaScript, and max-width and max-height still apply.** — The speaker names this as one of the most requested form features. ([7:12](https://youtu.be/DNixvXUOGhc?t=432))
- **Light and dark mode can be handled inline with light-dark(light, dark), which follows the colour-scheme setting. The alternative was a dark class on the root with redefined variables.** — The demo switches from the dark colour to the light colour when color-scheme is forced to light. ([8:33](https://youtu.be/DNixvXUOGhc?t=513))
- **CSS anchor positioning places an element relative to a named anchor with about four lines of CSS.** — The anchor gets an anchor name (the speaker uses tooltip). The positioned element is set to position: fixed, given a position-anchor matching that name, and placed with position-area such as top right or bottom left. ([9:51](https://youtu.be/DNixvXUOGhc?t=591))

## Techniques
- **Popover without JavaScript** — Add the popover attribute to the panel div and popovertarget="<panel id>" to the trigger button. Escape and click-away close it. Animate with translate + transition, using @starting-style for the entry state, placed after the base rule. *When:* Tooltips, menus, subscribe prompts and other simple overlays where a Popper.js-style dependency is not needed.
- **@starting-style entry animation** — Put the pre-render state (for example translate: -22rem, or background-color: yellow) inside @starting-style, below the base rule. Pair it with a transition on the same property (the demo uses about 0.5s). *When:* Entry animations for elements added to the DOM or shown from display: none, instead of JavaScript timers or class toggles.
- **Animated details disclosure** — Use details/summary for accordions. Transition ::details-content from height 0 to a fixed height when [open] is present. For horizontal accordions, set display: flex and flex-direction: row on the details element. *When:* Expandable sections where the summary and content need separate layout control.
- **Animating to auto height and width** — Set interpolate-size: allow-keywords on :root (the speaker enables it globally, not per element). Then transition height or width to auto, max-content or fit-content. *When:* Accordion panels or hover-expanding elements that currently need JS measurement or a fixed pixel value.
- **Content-sized form fields** — Set field-sizing: content on textarea, select and input. Constrain growth with max-width and max-height. *When:* Auto-growing textareas and inputs sized to placeholder or value, without character counting in JavaScript.
- **Stroke behind fill text** — Set paint-order: stroke fill so the stroke is painted before the fill, removing stroke overlap on tightly packed glyphs. *When:* Outlined display text where the stroke should sit behind the fill.
- **Colour scheme aware values inline** — Use light-dark(lightColor, darkColor) for colour values. The result follows the color-scheme setting (system or forced). *When:* Simple light and dark theming where a full set of redefined dark-mode variables is unnecessary.
- **Anchor-based tooltip positioning** — On the anchor element, set an anchor name (tooltip in the demo). On the positioned element, set position: fixed, position-anchor to the same name, and position-area (for example top right, bottom right, bottom left, or center). *When:* Tooltips and callouts anchored to a trigger element with no JS measurement.
- **Vertical centering of a block** — Apply align-content: center to the container. The speaker says it now works on block elements, not only flex or grid. *When:* Centring a single block child vertically without switching the container to flex or grid. The speaker does not show browser-support details.

## Numbers
- Video runtime is 11:21, and the title claims 10 new features. ([0:00](https://youtu.be/DNixvXUOGhc?t=0))
- Popover panel slides from translate -22rem to 0 0 with a transition. ([1:12](https://youtu.be/DNixvXUOGhc?t=72))
- Quick background-colour demo transitions yellow to red over a 0.5s transition. ([2:17](https://youtu.be/DNixvXUOGhc?t=137))
- Details content example uses a fixed 300px height for the open state before switching to interpolate-size. ([4:51](https://youtu.be/DNixvXUOGhc?t=291))
- Anchor positioning is said to need four lines of CSS. ([9:51](https://youtu.be/DNixvXUOGhc?t=591))

## Hot takes
- Popover and anchor positioning make Popper.js-style libraries unnecessary for common cases (speaker's claim, not tested here).
- interpolate-size: allow-keywords is called one of the most requested CSS features, and the speaker says it is 'honestly' that.
- The video calls several features the best way to centre or animate. These are demo-level claims with no browser-support or accessibility discussion.

## Tools mentioned
CSS, HTML, Popover API, @starting-style, details/summary, interpolate-size, field-sizing, paint-order, light-dark(), CSS anchor positioning, align-content, Popper.js (named as the old approach), Chrome dev team CSS demo page (captioned as CSS Rapt, likely CSS Wrapped)

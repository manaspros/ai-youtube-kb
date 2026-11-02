# Build Sites That Sell 99% of Products with Claude AI

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `VtmBevBcDzI` · [watch](https://youtu.be/VtmBevBcDzI) · **date:** 2025-11-02 · **length:** 11:54 · **format:** tutorial · **quality:** 2/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Abacus (ChatLLM, sponsor)
- **topics:** vibe-coding-app-building, claude-code, context-engineering · **tags:** landing-page, v0, claude-code-prompting, paper-shaders, framer-motion, google-fonts, svg, gitingest, layout-inspiration, sponsored

> A landing-page design walkthrough: reverse-engineer a strong v0 site, then steer Claude Code with named libraries (paper shaders, Framer Motion), Google Fonts, layout screenshots and SVG code. Mostly a practical tip list with a sponsor segment.

## Summary
The creator found a polished landing page built in v0 and set out to turn its design choices into reusable prompts for Claude Code. Two attempts with Claude Code's generic prompts produced weak results, so he copied the final code, reused the original prompts, and broke the design into parts. The main levers he names are an animated background built with the paper shaders library, animations built with Framer Motion instead of hand-written code, a gooey morph between two separate elements, a distinctive Google Font applied to a single word, a layout chosen from a screenshot gallery, and SVG logo code instead of image files. For the background he converted a small repo into plain text with GitIngest and worked in a focused chat that contained only the background code. The video includes a roughly 1.5-minute sponsored segment for ChatLLM and the title overstates the claim.

## Key ideas
- **Reverse-engineer a strong reference site instead of prompting from scratch: copy the final code, reuse the original author's prompts, and break the design into parts.** — The creator says generic prompts to Claude Code gave basic results, and the v0 site had been built well on its first try from the author's prompts. He treats the reference's code plus its prompts as the spec. ([1:05](https://youtu.be/VtmBevBcDzI?t=65))
- **Name the exact library in the prompt. A vague ask for an animated background failed, while naming paper shaders and specifying the design worked.** — He says Claude Code did not understand what looked better when asked generically, and that v0 got it right on the first try from the author's prompt. Naming the library and describing the design explicitly produced the backgrounds he wanted. ([3:02](https://youtu.be/VtmBevBcDzI?t=182))
- **Scope the context to the relevant slice. Feed only the library or background code into a focused chat rather than the whole codebase.** — He converted the small paper-shaders repo to plain text with GitIngest and pasted it into Claude Code. He argues that a context holding only the background details works better than handing over the entire codebase. He also reports that the prompt unlocked animated variants that the model had not produced before. ([3:02](https://youtu.be/VtmBevBcDzI?t=182))
- **Use animation libraries like Framer Motion rather than asking the AI to hand-roll animations. Pre-built animations are less likely to break when other parts of the page change.** — He says AI models are very good with Framer Motion and that changing the background should not randomly break the animations. He tells the viewer to name the React version of the library in each animation request. ([5:39](https://youtu.be/VtmBevBcDzI?t=339))
- **For a gooey morph effect, create two separate elements first (for example a login button and an arrow circle), then ask for a gooey morph between them using Framer Motion.** — The effect is two elements morphed together. Building the elements first and then applying the morph as a separate step is the sequence he recommends. ([6:57](https://youtu.be/VtmBevBcDzI?t=417))
- **Typography and layout matter more than gradients. Use one distinctive Google Font on a single word and place text off-center, such as bottom left.** — He copied the embed code from Google Fonts and asked Claude Code to apply it to the word beautiful. He also argues that a distinctive layout beats a centered default, and that you can take a layout screenshot from a gallery such as Landbook and give it to Claude Code along with your content and palette. ([7:54](https://youtu.be/VtmBevBcDzI?t=474))
- **Give the model logos and icons as SVG code, not image files. Shapes written as code are easier for the model to read, edit and animate.** — He copied the v0 logo's SVG markup from an SVG logo site and pasted it into the terminal. He says the SVG can then be animated with Framer Motion, recolored to match a brand, or used directly in the app. ([10:22](https://youtu.be/VtmBevBcDzI?t=622))

## Techniques
- **Reference-site reverse engineering** — Take the final code and the original author's prompts from a site you admire, break the design into parts (background, animations, font, layout, logo), and rebuild each part with a focused prompt. Keep the original prompts as the spec. *When:* When generic prompts to a coding agent keep producing a generic-looking page and you have a high-quality example to copy from.
- **Named-library prompt with a focused context** — Tell Claude Code the library by name (paper shaders for backgrounds) and describe the target design precisely. Convert the library repo to plain text (GitIngest) and paste it into a separate chat that holds only that library's code, rather than the whole project. Ask for variants (colors, animation types) in that same chat. *When:* When the agent misunderstands a visual or library request, or when the whole codebase would bury the relevant details in context.
- **Framer Motion for animations** — Do not ask the model to write animation logic from scratch. Ask for the component and name the library explicitly, for example 'use Framer Motion for React'. Use its pre-built animations for buttons, components and icons. *When:* For any UI animation (rotating elements, pop-ups, hover and reveal effects) where stability matters and the page will change later.
- **Two-step gooey morph** — Step 1: ask the AI to create two separate elements (for example a login button and a small arrow circle). Step 2: ask for a gooey morphing animation between them, and specify Framer Motion. *When:* For a morphing transition between two UI pieces.
- **One-word font accent** — Find a font on Google Fonts, copy its embed code, and tell Claude Code to apply it only to a single word, pasting the link. *When:* To add character to a headline without changing the whole type system.
- **Layout from a gallery screenshot** — Find a layout you like on a site gallery (the creator used Landbook), screenshot it, and give the screenshot to Claude Code with your content, logo and a color palette. Ask for the layout to match the screenshot. *When:* When the page looks generic despite good fonts and backgrounds, because the structure is what's missing.
- **SVG logos and icons as code** — Copy a logo's SVG markup from an SVG logo site, paste it into the terminal or prompt, and ask for it to be used directly or animated. For illustrations, download SVGs and give them to Claude Code, then recolor them with brand colors. *When:* When you need logos or icons that the model should understand, edit and animate, rather than image files it can only reference.

## Numbers
- Claude Code's first and second attempts with the original author's prompts did not produce anything close to the desired design (anecdotal, one creator's test). ([1:05](https://youtu.be/VtmBevBcDzI?t=65))
- The sponsor ChatLLM costs $10 a month. ([2:20](https://youtu.be/VtmBevBcDzI?t=140))
- Sponsored segment runs about 1:05 to 2:20 (about 1.25 minutes of a 11:54 video). ([1:05](https://youtu.be/VtmBevBcDzI?t=65))
- Video length is 11:54. ([11:54](https://youtu.be/VtmBevBcDzI?t=714))

## Hot takes
- Title says the video shows how to sell 99% of products. The content is design tips for a landing page; it does not show conversion data or any evidence about sales.
- Evidence is one creator's anecdotal tests: 'in my testing', 'countless examples', and 'it failed for some reason'. No before/after comparison or repeated runs are shown.
- Claim that AI-generated animations break when other parts of the page change is asserted, not demonstrated.
- A sponsored ChatLLM segment (about 1.25 minutes) sits in the first third of the video; quality is capped at 2 under the rubric.
- The creator admits the second font he applied 'isn't necessarily better' than the default, which undercuts the font advice.
- Attributing the better v0 output to the prompts or the tool is not isolated: no controlled comparison between v0 and Claude Code is shown on the same prompt.

## Tools mentioned
Claude Code, v0, Cursor (mentioned as a tool to use, no steps shown), Paper Shaders (library for animated website backgrounds), Framer Motion (React version named), GitIngest ("Git Ingest", converts a repo to AI-readable text), Google Fonts, Landbook (layout and design gallery), ChatLLM by Abacus (sponsor)

## Relevance to our work
- **prosharness** (1/3): Touches Claude Code prompt scoping: give a sub-session only the relevant slice (one library's code), not the whole repo. Only tangentially related to the harness. → *When a ProsHarness sub-run needs a library or skill, ingest just that slice into a focused session and name the library explicitly in the prompt, rather than passing the whole repo.*

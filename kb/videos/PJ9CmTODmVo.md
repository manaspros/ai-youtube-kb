# This Is Insane... This Just Ended The Google Stitch VS Claude Design Debate

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `PJ9CmTODmVo` · [watch](https://youtu.be/PJ9CmTODmVo) · **date:** 2026-06-02 · **length:** 10:46 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Anthropic, Google
- **topics:** product-ux, mcp-and-tools, coding-agents, context-engineering · **tags:** claude-design, google-stitch, design-md, ui-design, figma-alternative, design-to-code, mcp, usage-limits, animations, design-systems

> Hands-on head-to-head of Claude Design and Google Stitch across features, limits, design quality, animation, iteration and handoff; each tool wins different categories.

## Summary
The presenters run Claude Design (released with Opus 4.7) and Google Stitch (2.0, powered by Gemini 3) through the same prompts and score them by category. Claude Design wins on editing and iteration: you click or comment directly on the page, batch comments, and it applies them in the context of the app. It also has presentation and speaker-note output, team sharing with separate edit and comment permissions, and better animations. Stitch wins on usability and design quality: it has a free tier with generous daily credits, a separate preview for desktop, tablet and mobile, a portable design.md design-system file, image generation via Nano Banana instead of SVG placeholders, and an MCP that lets coding agents drive it. The reviewers judge Stitch's landing page better and faster on a single prompt, while Claude Design's output felt generic to them. For handoff, they use Stitch's MCP most and pasting a prompt into Claude Code for Claude Design. The verdict rests on one prompt per test and subjective judgments, with no benchmarks.

## Key ideas
- **Editing model is the biggest split: Claude Design lets you click elements or drop comments, pile them up, and send them together, while Stitch only allows direct text edits and routes other changes through annotated comments to Gemini.** — Stitch's annotate-and-send loop and its tendency to add new screens per change left the canvas cluttered. The presenters judged Claude Design much better for iteration because it understands the app and applies changes without drifting from the style. ([7:05](https://youtu.be/PJ9CmTODmVo?t=425))
- **Stitch's usage model is far more generous. It is free on every plan with daily design credits, while Claude Design has a weekly limit separate from Claude Code and is effectively usable only on Max.** — Stitch: 400 daily design credits and 15 daily redesign credits, with about 3 credits per simple design. Claude Design is available on Pro, Max, Team and Enterprise, but the Pro limit allows only a few experiments. ([3:53](https://youtu.be/PJ9CmTODmVo?t=233))
- **Design quality and image handling favor Stitch. Stitch generates raster images through Nano Banana and produced the better landing page, while Claude Design falls back to SVG generation unless the user supplies assets.** — Stitch built its design system first (colors, typography, icons, buttons), then a landing page in the same style, and finished before Claude Design. The reviewers called Claude Design's palette generic. ([5:04](https://youtu.be/PJ9CmTODmVo?t=304))
- **Animation is a clear Claude Design win. It added a marquee, scroll reveals on every component, and mouse- and click-reactive behavior, while Stitch animated only one section and showed it only in a separate preview tab.** — The presenters attribute Claude Design's animation quality to popular animation and shader libraries. ([6:11](https://youtu.be/PJ9CmTODmVo?t=371))
- **Stitch's preview pane shows desktop, tablet and mobile layouts, and Claude Design has no separate responsive preview. Claude Design, however, supports per-user share permissions (edit vs comment) that Stitch lacks.** — Claude Design renders on the same pane and is interactive there, but you cannot check responsiveness the way you can in Stitch. ([2:34](https://youtu.be/PJ9CmTODmVo?t=154))
- **Portability of design systems differs. Claude Design's design system is brand-level (description, fonts, logos, assets), while Stitch's is a design.md file for one design. That file can be exported and read by any agent, and Stitch has open-sourced its format.** — The presenters prefer Google's design.md approach because it avoids lock-in to Stitch. The NPM install and formatting details are mentioned but not shown. ([8:15](https://youtu.be/PJ9CmTODmVo?t=495))
- **Handoff to code is the strongest Stitch advantage. Its MCP lets a coding agent prompt Stitch in its own language and pull designs back for implementation. Claude Design has no MCP, so its handoff is copying one prompt into Claude Code.** — Other Stitch exports are a zip, Google AI Studio with Firebase, Figma, and a PRD that can be handed to people or agents. ([9:32](https://youtu.be/PJ9CmTODmVo?t=572))
- **Claude Design offers PDF, slides with speaker notes, and export to canvas. Stitch is UI-only and covers mobile and web interfaces only.** — Claude Design also imports styles from a connected GitHub repo, and Stitch imports a design system from a website link. ([1:06](https://youtu.be/PJ9CmTODmVo?t=66))

## Techniques
- **Batch design comments before sending** — In Claude Design, click the element you want changed or drop a comment on it. Queue several comments, then send them together so one pass applies all of them in the context of the app. *When:* Iterating on an existing design with several small changes (colors, spacing, copy placement) where re-prompting the whole page would drift from the style.
- **Import a design system from a URL** — In Stitch, paste the link to an existing website. Stitch extracts its styling into a design system and reuses it for later screens. *When:* You want new screens to match an existing brand or site without describing the style in a prompt.
- **Portable design.md design system** — Export the Stitch design system as design.md and give it to any coding agent, which reads it and implements the style directly. Stitch's open-sourced format includes NPM install commands. *When:* You want a design system that can move between tools and agents without lock-in.
- **Coding agent drives the design tool through MCP** — Connect Stitch's MCP to the coding agent. The agent sends Stitch-tailored prompts to generate designs and pulls them back to implement in the app. *When:* Design-to-code runs inside an agent loop and you do not want to hand-craft design prompts or copy them into the agent.
- **Generate the design system before the screens** — Stitch first produces a visual design system (colors, typography, icons, buttons) and then builds pages from it, which kept the pages consistent across signup, login and landing screens. *When:* Producing a multi-page UI where visual consistency matters more than per-page creativity.

## Numbers
- Stitch free tier: 400 daily design credits and 15 daily redesign credits, with monthly credits higher still. ([3:53](https://youtu.be/PJ9CmTODmVo?t=233))
- A simple Stitch design costs about 3 credits, varying with complexity and number of generations. ([3:53](https://youtu.be/PJ9CmTODmVo?t=233))
- Claude Design has a separate weekly limit that does not count against Claude Code limits. The presenters say the Pro plan allows only a few experiments and Max is needed for substantial work. No figures are given. ([3:53](https://youtu.be/PJ9CmTODmVo?t=233))
- Claude Design is available on Pro, Max, Team and Enterprise plans. Stitch is free on all plans. ([3:53](https://youtu.be/PJ9CmTODmVo?t=233))
- Stitch finished its landing page before Claude Design finished its first run. No timings are reported. ([5:04](https://youtu.be/PJ9CmTODmVo?t=304))

## Hot takes
- Hype title ("This Is Insane... This Just Ended...") over a fairly shallow single-prompt comparison; the verdict is subjective and no benchmarks are run. Quality capped at 2 under the hype-title rule.
- Stitch wins design quality and handoff, while Claude Design wins iteration, animation and team permissions. Presenters conclude Stitch is the better all-round pick mainly because of usage limits and its MCP.
- Claude Design's visual output is called generic, and its SVG-only imagery is blamed for weaker results; this is one test and may reflect prompting rather than the tool's ceiling.

## Tools mentioned
Claude Design, Claude Opus 4.7, Google Stitch, Gemini 3, Nano Banana, Claude Code, Figma, Google AI Studio, Firebase, GitHub, design.md

## Relevance to our work
- **prosharness** (1/3): Touches the Claude Code handoff pattern (copy-paste prompt vs MCP-driven design tool) and portable design specs an agent can read. Only relevant if design work enters a harness run. → *If design work ever runs inside ProsHarness, test whether Stitch's MCP can be wired into the Claude Code session so the agent pulls designs itself instead of receiving pasted prompts.*

# Your AI UI Looks Generic… This Fixes It (DESIGN.md)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `pY52H5gKhGg` · [watch](https://youtu.be/pY52H5gKhGg) · **date:** 2026-06-02 · **length:** 5:36 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, Google, Stripe, Linear, Vercel, Notion
- **topics:** vibe-coding-app-building, context-engineering, coding-agents · **tags:** DESIGN.md, design-systems, ui-generation, agent-context, design-tokens, accessibility, cursor, claude-code, v0, tailwind

> Google's open-sourced DESIGN.md: a repo-root markdown file of design tokens plus intent prose that keeps AI-generated UI from looking generic. Practical but thin.

## Summary
The speaker argues that AI coding tools produce working but generic-looking UIs because the model has to guess the visual style. The proposed fix is DESIGN.md, a plain markdown file in the repo that describes how the product should look and feel. Google open-sourced the format on April 21, and the speaker says the community repo passed 70,000 GitHub stars within a couple of weeks. In a single before/after demo, the same "build a modern dashboard" prompt gives a generic result without the file and a more coherent one with a Stripe-style DESIGN.md. The file has structured tokens at the top (hex colors, font families, border radius, spacing) treated as hard rules, followed by markdown that explains intent and covers palette, typography, components, layouts and accessibility. The speaker positions it against Figma (lives outside the repo), JSON tokens (machine-only, no taste), and Cursor rules or CLAUDE.md (behavior, not a design system). The advice is to start from a template in the community "awesome" repo and customize it, while acknowledging the file is only as good as what is written in it.

## Key ideas
- **Generic AI UI is a context problem, not a model problem** — Without a design spec the model guesses colors, spacing and layout, so output technically works but has default-looking buttons, cards and no identity. Supplying the rules changes the output with the same prompt. ([0:00](https://youtu.be/pY52H5gKhGg?t=0))
- **DESIGN.md is one plain markdown file in the repo** — It is presented as a design system the agent reads: no Figma export and no JSON pipeline, and the speaker says setup is close to zero. ([0:00](https://youtu.be/pY52H5gKhGg?t=0))
- **Google open-sourced the format and adoption was fast** — The speaker says Google released it on April 21 and the community repo passed 70,000+ GitHub stars within a couple of weeks. These are the speaker's claims, not verified here. ([0:56](https://youtu.be/pY52H5gKhGg?t=56))
- **Demo: same prompt, with and without the file** — The prompt is 'build a modern dashboard'. Without DESIGN.md the output is a generic AI dashboard. Adding a Stripe-style DESIGN.md makes colors, spacing and button styles line up. The only comparison shown is this one prompt. ([0:56](https://youtu.be/pY52H5gKhGg?t=56))
- **Structure: hard tokens on top, intent prose below** — Exact hex colors, font families, border radius and spacing come first as hard rules. Markdown sections then explain the reasoning (e.g. this blue is the primary accent and should read as trustworthy), covering palette, typography, components, layouts and accessibility. The speaker's point is that agents need judgment as well as values. ([2:04](https://youtu.be/pY52H5gKhGg?t=124))
- **Positioning against Figma, JSON tokens and CLAUDE.md** — Figma lives outside the repo, JSON tokens have no taste or intent, and Cursor rules or CLAUDE.md govern behavior but are not a design system. DESIGN.md is human-readable, machine-readable, version-controlled and sits next to the code. ([3:20](https://youtu.be/pY52H5gKhGg?t=200))
- **Honest caveat: quality equals what you write** — The speaker says it is one file and a weak DESIGN.md gives weak output. Advice: start from a template in the community awesome repo, then customize it for your own brand. The goal is to stop the agent guessing, not to make it more creative. ([4:34](https://youtu.be/pY52H5gKhGg?t=274))

## Techniques
- **Repo-root DESIGN.md with tokens then intent** — Put exact values at the top as hard rules (hex colors, font families, border radius, spacing). Under them, write a markdown section for each area (palette, typography, components, layouts, accessibility), and for each one state the intent or reason, not only the value. The speaker's example: this blue is the primary accent and should feel clear and trustworthy. Commit it so it versions with the code. *When:* Before asking a coding agent to generate UI, especially for prototypes or solo projects where style otherwise drifts from screen to screen.
- **Fixed-prompt A/B for design context** — Run the same UI prompt twice in the same tool, once without DESIGN.md and once with it, then compare the results. The demo uses 'build a modern dashboard' for both runs. *When:* To check whether a design-context file actually changes output before relying on it. Only one prompt is shown, so repeat it with other prompts to test.
- **Start from a community template, then customize** — Take a template from the community awesome-DESIGN.md repo (the speaker says the link is in the video description, not shown on screen), drop it into the project, and replace the values and intent with your own brand. *When:* When you have no design spec yet. A template for a known brand such as Stripe, Linear, Notion or Vercel gives a strong starting point.
- **Write the design rules once, not in every prompt** — Keep style directions (spacing, buttons, tone) in the file so each prompt only describes the feature, instead of repeating 'make it clean, modern, with better spacing'. *When:* Across many screens or sessions where style instructions get repeated and drift.

## Numbers
- Google open-sourced DESIGN.md on April 21 (speaker's claim) ([0:56](https://youtu.be/pY52H5gKhGg?t=56))
- Community GitHub repo passed 70,000+ stars within about two weeks (speaker's claim) ([0:56](https://youtu.be/pY52H5gKhGg?t=56))
- Demo compares one prompt only (build a modern dashboard), with no quantitative metrics ([0:56](https://youtu.be/pY52H5gKhGg?t=56))

## Hot takes
- The title promises a fix, but the evidence is one before/after screenshot-style comparison with no shown file contents or repeated trials.
- The speaker presents Google's open-sourcing and the 70k star count without a link or source on screen.
- The speaker's own caveat is the strongest point: the file is only as good as what is written in it, so the value depends on the author's design judgment.

## Tools mentioned
DESIGN.md (Google open-source format), Cursor, Claude Code (transcribed as 'Cloud Code'), v0, Figma, CLAUDE.md, Cursor rules, Tailwind (default styling referenced in demo)

## Relevance to our work
- **prosharness** (1/3): ProsHarness drives Claude Code runs, and a repo-root design-rules file loaded alongside CLAUDE.md is a context-engineering pattern it could use for UI tasks. → *For UI-producing ProsHarness runs, test a fixed-prompt A/B with and without a repo-root DESIGN.md loaded next to CLAUDE.md, and only adopt it if output improves.*

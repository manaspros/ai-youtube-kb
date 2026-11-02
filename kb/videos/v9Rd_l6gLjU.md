# Gemini Designer is INSANE... Build Beautiful Websites in Minutes

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `v9Rd_l6gLjU` · [watch](https://youtu.be/v9Rd_l6gLjU) · **date:** 2025-12-02 · **length:** 8:20 · **format:** tutorial · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Google, OpenAI, Anthropic, Figma
- **topics:** vibe-coding-app-building, product-ux, coding-agents, context-engineering · **tags:** google-stitch, ai-designer, ui-generation, design-system, figma-mcp, klein, vs-code, nextjs, phased-workflow, rules-file, validation-checklist, markdown-artifacts

> Walkthrough of Google Stitch, an AI UI designer, plus a six-phase Klein rules-file workflow that turns exported Stitch HTML into a Next.js app and validates it against the designs.

## Summary
The speaker presents Google Stitch as an AI UI designer that generates web and mobile screens from text prompts, with a standard mode (text to UI, up to 350 designs per month) and an experimental mode (image reference, up to 50 per month). The main practical advice is to iterate screen by screen instead of asking for a whole app at once, since one big prompt produces weak design. Fixes are done by re-prompting, and the speaker shows a chess app built this way with consistent styling across login, settings, result and analysis screens. Stitch defaults to Material UI even when iOS is requested, so iOS-style work is weaker. The main workflow then runs in Klein, a multi-model VS Code extension, using a rules file that drives six phases: extract a design system from the exported Stitch HTML, document each page, list reusable components, map navigation, write an implementation blueprint and implement it, and finally build a validation checklist with a scorecard. The speaker says implementing from HTML is better than from screenshots because the markup clones the UI closely, and that the output is a demo with no backend, so the AI models are not wired up and the chessboard does not move.

## Key ideas
- **Stitch works best iteratively: start with one screen (the chessboard), then add screens and fix issues by prompting. Asking for everything at once gives poor design.** — The speaker says that if you ask for everything at once the design will not come out well. Consistency held across later screens (login, forgot password, settings, result, game analysis) because each was added on top of the previous ones. ([1:02](https://youtu.be/v9Rd_l6gLjU?t=62))
- **Stitch has two generation modes with different monthly quotas: standard text-to-UI and experimental image-reference mode.** — Standard mode is text to UI, up to 350 designs per month. Experimental mode takes an image reference and allows up to 50 designs per month, plus visual choices. ([0:00](https://youtu.be/v9Rd_l6gLjU?t=0))
- **Stitch defaults to Material UI for mobile, so iOS apps are weaker output.** — An Arc browser design requested as an iOS app still came out on a Material UI base even after the speaker said it should be iOS. The speaker advises against relying on Stitch for iOS. ([2:29](https://youtu.be/v9Rd_l6gLjU?t=149))
- **The core workflow is a Klein rules file that runs six phases, with four documentation phases before any code is written.** — Phase 1 extracts the design system (colors, fonts, layout patterns, responsiveness patterns) from the Stitch HTML folder. Phase 2 documents each page (purpose, sections, interactive elements). Phase 3 writes a reusable-component list. Phase 4 writes a navigation flow. Phase 5 writes an implementation blueprint and implements it. Phase 6 builds a validation checklist. ([3:50](https://youtu.be/v9Rd_l6gLjU?t=230))
- **Build from the Stitch HTML exports, not screenshots, because the markup clones the UI one-to-one.** — The speaker says implementing from HTML is better than from screenshots. Small misalignments can still appear, which he attributes to missing screenshots in the input. ([6:06](https://youtu.be/v9Rd_l6gLjU?t=366))
- **Implementation is staged through a blueprint file instead of one big prompt, because LLMs forget.** — Phase 5 first writes implementation blueprint.md from the earlier phase artifacts (components, design system, documentation) and then implements from it, rather than asking the model to implement everything directly. ([6:06](https://youtu.be/v9Rd_l6gLjU?t=366))
- **The validation phase checks the built app against the design files at a fine grain and outputs a scorecard of fixes.** — It compares colors, fonts, border radius and components against the design, writes validation criteria to validation checklist.md, and produces a scorecard listing fixes. The speaker frames this as necessary because models hallucinate. ([7:30](https://youtu.be/v9Rd_l6gLjU?t=450))
- **The result is a demo UI with no backend. Model selection is visible but not implemented, and the chessboard cannot move.** — This limits what the video proves: the workflow yields screens and navigation, but not the AI behavior of the app. ([6:06](https://youtu.be/v9Rd_l6gLjU?t=366))

## Techniques
- **Iterative screen-by-screen prompting in Stitch** — Generate one core screen first (for example a chessboard), then add the rest one at a time, each prompt building on the previous screens. Fix problems by re-prompting (for example, asking for more visible, better-aligned pieces, or adding a settings screen with logout). *When:* Any multi-screen UI design in Stitch, where a single all-at-once prompt gives weak output and drifts in style.
- **Design-system extraction from exported HTML (phase 1)** — Point the Klein workflow at the Stitch folder of HTML exports. The agent extracts the color palette, fonts, layout patterns and the patterns used for responsiveness, and writes them to a design-system document. *When:* Before any code is written, to turn Stitch output into a reusable spec that the implementation step can cite.
- **Per-page analysis and component library (phases 2-3)** — For every HTML file, the agent records the page purpose, sections and interactive elements. It then identifies reusable components and writes them to component library.md, with extra instructions to make the extraction accurate. *When:* When a multi-page design needs a documented inventory of pages and shared components before implementation.
- **Navigation-flow mapping (phase 4)** — From the page analysis and components, the agent writes navigationflow.md describing how users move between pages. The speaker reports the framework was taken from an online-shop example and applied to the app. The output is the connection spec for pages that already exist. *When:* Once screens and components are documented, to define how the built pages connect.
- **Blueprint-then-implement (phase 5)** — The agent first writes implementation blueprint.md from the design system, components and navigation docs, plus additional rules. It then implements the app from that blueprint. Keep the whole sequence in one workflow.md that starts the run. *When:* Implementing a large design in one go, to avoid the agent forgetting earlier decisions.
- **Validation checklist and scorecard (phase 6)** — The agent scans the built app and compares it with the design files and implementation. It writes the criteria to validation checklist.md, checks colors, fonts, border radius and components, and outputs a scorecard of fixes to apply. *When:* After implementation, to catch visual drift and hallucinated details before calling the UI done.
- **Build from HTML, not screenshots** — Give the implementation step the exported HTML rather than screenshots. The speaker says this produces a closer one-to-one clone. *When:* Converting an AI-designed UI into code where fidelity matters.

## Numbers
- Stitch standard mode: up to 350 designs per month (text to UI). ([0:00](https://youtu.be/v9Rd_l6gLjU?t=0))
- Stitch experimental mode: up to 50 designs per month (image reference, visual choices). ([0:00](https://youtu.be/v9Rd_l6gLjU?t=0))
- GPT-5 Temporary: increased limit of 106 messages per 3 hours; standard access is 80 messages per 3 hours, then it falls back to smaller models. ([2:29](https://youtu.be/v9Rd_l6gLjU?t=149))
- Claude Pro limits uploads per chat rather than context window; each file up to about 30 MB (the speaker's number). ([3:50](https://youtu.be/v9Rd_l6gLjU?t=230))
- Six phases in the workflow: four documentation phases, one implementation phase (phase 5), one validation phase (phase 6). ([3:50](https://youtu.be/v9Rd_l6gLjU?t=230))

## Hot takes
- Stitch is weak for iOS-style apps and defaults to Material UI even when told otherwise.
- Stitch should have an MCP server, like Figma, so designs can turn directly into code.
- Implementing from HTML exports is better than from screenshots.
- Models hallucinate, so validation against the design is essential.
- The demo has no backend, so the AI features are not actually shown working.

## Tools mentioned
Google Stitch, Klein (VS Code extension, multi-model, rules file, MCP store), VS Code, Next.js, Figma (via Klein's MCP store), ChatGPT (GPT-5 Temporary), Claude Pro, Material UI, Arc browser (example prompt)

## Relevance to our work
- **prosharness** (1/3): The phase-gated chain of markdown artifacts (inventory, component list, flow, blueprint, checklist with scorecard) is a useful template for a plan-then-verify loop around Claude Code runs. → *Try a ProsHarness plan stage that writes an artifact chain (inventory, then blueprint, then a checklist with a scored verify step) and has each implementation step cite these artifacts, instead of a single prompt.*

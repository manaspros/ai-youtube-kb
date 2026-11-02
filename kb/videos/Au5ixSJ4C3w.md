# Fragments by E2B: The FREE AI Tool Surpassing Bolt.new & v0.dev?

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `Au5ixSJ4C3w` · [watch](https://youtu.be/Au5ixSJ4C3w) · **date:** 2024-11-02 · **length:** 6:12 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** E2B, Google
- **topics:** vibe-coding-app-building · **tags:** fragments, e2b, ui-generation, screenshot-to-code, claude-artifacts, open-source, gemini-clone, bolt-new, v0

> A short walkthrough of Fragments by E2B, an open-source Claude Artifacts-style tool that turns prompts or screenshots into live-previewed UI, with a free-tier and local-run note.

## Summary
The host demos Fragments by E2B, an open-source, Claude Artifacts-style tool that generates UI from a plain-English prompt and shows a live browser preview with no dev server. Unlike Artifacts, it lets you pick among several models and personas. He builds a recipe-app landing page, then fixes text overflow, missing colour and images with follow-up prompts, and leaves a responsiveness bug unfixed by zooming out. He then pastes a Gemini website screenshot and asks for a functional clone, which he tweaks for colour. He mentions direct deploy to E2B and the local-run path (clone repo, install dependencies, add an E2B API key). The video is a surface-level tour: no code is shown, no quality or cost comparison is made, and the title's claim of beating Bolt.new and v0.dev is never tested.

## Key ideas
- **Fragments is positioned as an open-source, free-for-now Claude Artifacts alternative** — Prompt in plain English, get a live browser preview with no setup or dev server, then import the code into a project. The main difference from Artifacts is that you are not limited to Claude's models. ([0:00](https://youtu.be/Au5ixSJ4C3w?t=0))
- **Persona and model selection are the main knobs before generation** — After Google sign-in, you pick a persona matched to the app type and a model from a list. At recording time all listed models were free with rate limits and no paid plans. ([1:26](https://youtu.be/Au5ixSJ4C3w?t=86))
- **First-pass output needs follow-up prompts for styling and layout** — The generated recipe site had text overflowing its boxes, no colour and broken images. Targeted follow-up prompts fixed the colour and images; a responsiveness problem was sidestepped by zooming out rather than fixed. ([2:25](https://youtu.be/Au5ixSJ4C3w?t=145))
- **Screenshot-to-clone works as a one-shot prompt** — He pasted a Gemini website screenshot and asked for a replica with working functionality. The result looked close to the original, and a colour tweak finished it. Accuracy was judged by eye only. ([2:25](https://youtu.be/Au5ixSJ4C3w?t=145))
- **Generated apps can be deployed to E2B directly from the tool** — The host says deployment to E2B needs no extra setup. He does not show the deploy step itself. ([2:25](https://youtu.be/Au5ixSJ4C3w?t=145))
- **The project is open source and can run locally** — The README-style flow is: clone the repo, install dependencies, add an E2B API key, then start the dev server. The E2B key is obtained from the API section of the E2B site and is described as free. ([4:09](https://youtu.be/Au5ixSJ4C3w?t=249))

## Techniques
- **Iterative prompt-to-UI with targeted fix prompts** — Generate the first version from a plain-English app description, check the live preview, then send separate narrow prompts for each defect (overflow, colour, images) instead of re-prompting the whole app. The video does not show the exact prompt wording. *When:* Early UI exploration where you want a working page fast and can accept a few rounds of cosmetic fixes.
- **Screenshot-to-clone prompt** — Paste a screenshot of an existing site into the tool and ask it to replicate the design as a functional version. Then make small visual adjustments such as colours in follow-up prompts. *When:* Quickly prototyping a UI that already exists as a visual reference. Verify visually, since the video runs no functional or responsive checks.
- **Persona-first generation** — Choose the persona that matches the app type before generating, so the first output is closer to the target app. *When:* Starting a new app when you want a more specific first draft.
- **Local run from the open-source repo** — Clone the Fragments repo, install dependencies, create an E2B API key in the E2B dashboard's API section, add it to the local configuration, then start the development server. Exact commands, file names and the config key are not shown in the video. *When:* When you want to self-host the tool or avoid the hosted free tier. Check the repo README for the exact steps.

## Numbers
- All listed models were free to use, with rate limits and no paid plans at recording time ([1:26](https://youtu.be/Au5ixSJ4C3w?t=86))
- The E2B API key needed for local runs is free to obtain ([5:23](https://youtu.be/Au5ixSJ4C3w?t=323))

## Hot takes
- The title claims Fragments surpasses Bolt.new and v0.dev, but the video makes no side-by-side comparison and runs no test that would support it.
- The 'completely free right now' claim is dated to the November 2024 recording. Free-tier and rate-limit details are very likely stale in November 2026.
- The responsiveness bug was avoided by zooming out, not fixed, and the output was judged only by eye.
- Coverage is shallow: no code is shown, no model comparison is made, and the local-run steps are described in words only.

## Tools mentioned
Fragments (by E2B), E2B, Claude Artifacts, Claude, Gemini (website used as the clone target), Google sign-in, Bolt.new (named in the title and intro only), v0.dev (named in the title only)

## Relevance to our work
- **agentos** (1/3): E2B is a sandbox provider and the Fragments repo is open source, but the video does not explain sandbox internals. The only relevant item is a loose link to Crucible's sandboxed execution. → *Nothing to adopt from this video. If sandbox references are needed for Crucible, read E2B's own sandbox docs instead.*

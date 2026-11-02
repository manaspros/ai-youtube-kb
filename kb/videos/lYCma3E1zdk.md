# GitHub’s New Secret Copilot Model Is Shockingly Fast

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `lYCma3E1zdk` · [watch](https://youtu.be/lYCma3E1zdk) · **date:** 2026-01-02 · **length:** 6:49 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Andrus · **orgs:** GitHub, Microsoft, Better Stack, N2YO, Figma
- **topics:** coding-agents, models-research · **tags:** github-copilot, raptor-mini, gpt-5-mini, model-speed, three-js, prompt-iteration, express, vanilla-js, n2yo-api, figma-reference-image, svg-map

> Better Stack tries GitHub Copilot's preview model Raptor Mini on a satellite-tracking dashboard. Fast first pass, but the evidence is one demo with no benchmarks.

## Summary
GitHub announced Raptor Mini in public preview for Copilot in November, with no benchmarks or model card. The speaker reports that it is publicly described as a GPT-5 mini variant fine-tuned for coding and writing, positioned for speed and smaller tasks, with a context window of about 264K tokens and 64K output. He builds a space dashboard tracking the ISS and Starlink satellites from an API-docs file, a instructions file and a Figma reference image; the first pass took about 45 seconds. Adding an SVG world map worked, but turning it into a Three.js globe took seven or eight prompts of tweaking. The result is an Express server, roughly 500 lines of vanilla JavaScript and plain CSS, which the speaker prefers to a heavier Next.js setup. The verdict rests on speed and visual quality from a single project; satellite position accuracy was not checked and no comparison benchmark was run.

## Key ideas
- **GitHub's preview announcement gave no benchmarks, model card or comparison** — The Nov 10 announcement only confirmed that Raptor Mini exists and can be picked in the Copilot model dropdown. The speaker treats all performance claims as anecdotal for this reason. ([0:00](https://youtu.be/lYCma3E1zdk?t=0))
- **Publicly reported positioning: a GPT-5 mini variant aimed at speed and small tasks** — The speaker says the model is described as a GPT-5 mini variant fine-tuned for general coding and writing, strong at fast completions and explanations, and supporting agent mode. A Microsoft podcast with a VS Code team member is cited for this. He notes it is meant for smaller tasks compared with larger models such as Claude. ([1:07](https://youtu.be/lYCma3E1zdk?t=67))
- **Preview access and pricing are cheap or free for now** — During preview, the speaker says paid plans can use it without the quota multiplier, and free-plan users get a multiplier of one. ([1:07](https://youtu.be/lYCma3E1zdk?t=67))
- **Large context and output windows for a 'mini' model** — He cites roughly 264K tokens of context and 64K output, which he calls unusually large for a model with Mini in its name. The codename origin is not a technical point. ([2:09](https://youtu.be/lYCma3E1zdk?t=129))
- **A full dashboard was built in one 45-second pass from spec, API doc and design image** — Inputs were an instructions file, a markdown file with the N2YO API docs, and a Figma community dashboard screenshot used as the design reference. The first output had the right color scheme and moving satellite markers but no world map or globe, so the accuracy of positions could not be verified. ([3:16](https://youtu.be/lYCma3E1zdk?t=196))
- **Iterative refinement took several rounds, and the speaker says it is not one-shot** — Supplying an SVG world map and asking for a Three.js globe needed back-and-forth on minor bugs. The usable result arrived at about attempt seven or eight. ([4:24](https://youtu.be/lYCma3E1zdk?t=264))
- **The model chose a minimal stack instead of a framework** — The app uses an Express server, a roughly 500-line vanilla JS front end and plain CSS, all served from one HTML file. The speaker sees this as an advantage over Next.js build and dependency problems for a proof of concept. ([5:17](https://youtu.be/lYCma3E1zdk?t=317))
- **Verdict is based on feel, not measurement** — The speaker says the model feels very fast and produces good-looking output. He says official benchmarks are missing and that he plans to re-evaluate once the release version ships. ([5:17](https://youtu.be/lYCma3E1zdk?t=317))

## Techniques
- **Spec bundle for one-shot app generation** — Put a plain instructions file describing the app (what to track, how to render it), a markdown file with the target API's docs, and a reference design image in the prompt. Ask for the whole app in one pass, then check output in the browser. *When:* Greenfield proof-of-concept dashboards or small web apps where the API and visual target are known.
- **Stepwise visual upgrade with an asset** — When the first output lacks a key visual element, supply the missing asset (here, an SVG world map) and ask the model to overlay the data on it. Then ask for a bigger change (convert the map to a Three.js globe), and keep iterating on small bugs in separate prompts. *When:* When a one-shot result is 80% right and the remaining gap is a specific visual or 3D feature.
- **Prefer a minimal stack for prototypes** — Ask for an Express server, vanilla JS and plain CSS served from a single HTML file, instead of a framework such as Next.js. The speaker ties this to fewer build and dependency issues. *When:* Proofs of concept where build tooling would slow iteration more than the framework helps.

## Numbers
- Raptor Mini context window about 264,000 tokens, output window 64,000 tokens (speaker's figures) ([2:09](https://youtu.be/lYCma3E1zdk?t=129))
- First full dashboard generated in about 45 seconds ([3:16](https://youtu.be/lYCma3E1zdk?t=196))
- Three.js globe took about 7-8 prompt attempts to get right ([4:24](https://youtu.be/lYCma3E1zdk?t=264))
- Generated front end is about 500 lines of vanilla JavaScript plus a simple CSS file ([5:17](https://youtu.be/lYCma3E1zdk?t=317))
- Preview: no quota multiplier on paid plans, multiplier of 1 on the free plan ([1:07](https://youtu.be/lYCma3E1zdk?t=67))

## Hot takes
- The title's 'shockingly fast' claim rests on one demo and the speaker's impression; no benchmark, latency number or accuracy check is shown.
- Satellite positions were never verified against real data, so the dashboard's accuracy is unknown.
- The 'GPT-5 mini' lineage is reported second-hand from a podcast and is not confirmed by GitHub in the video.
- Quality is capped at 2 by the hype title and thin substance, even though the demo itself is interesting.

## Tools mentioned
GitHub Copilot, Raptor Mini, GPT-5 mini (per public reporting cited by the speaker), Claude (mentioned as a larger comparison model), Express, vanilla JavaScript, CSS, Three.js, N2YO API, Figma, SVG, Next.js (mentioned as the alternative not used)

## Relevance to our work
- **agentos** (1/3): Shows a fast, small coding model being used for a multi-step app build. This matters only as a candidate tier for cheap-model routing, and there is no measured data.
- **general** (1/3): A useful reminder for any model-choice decision: a single demo with no benchmarks is weak evidence for speed or quality claims. → *When a new model is adopted for coding work, record task-level latency and pass rate on our own task set rather than relying on a demo.*

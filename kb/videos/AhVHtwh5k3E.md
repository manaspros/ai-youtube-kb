# This Open-Source Tool Generates UI Like Magic

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `AhVHtwh5k3E` · [watch](https://youtu.be/AhVHtwh5k3E) · **date:** 2026-10-23 · **length:** 6:45 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Warren (Better Stack host) · **orgs:** Better Stack, OpenUI, Google, Vercel, Cerebras, OpenAI
- **topics:** vibe-coding-app-building, product-ux · **tags:** generative-ui, openui, openui-lang, streaming, token-efficiency, json-rendering, a2ui, design-systems, on-demand-apps, model-latency

> Better Stack demos OpenUI, a spec and streamable language for generative UI, and argues it beats JSON-based UI rendering on tokens and latency. Mostly a demo with unbenchmarked claims.

## Summary
The Better Stack host demos a locally run app launcher where typing a title generates a working app on demand, including its icon, using Gemini 3.8 Flash and OpenUI for rendering. He explains that OpenUI is a spec for rendering model-generated UI rather than a component library, and that it works with React, Svelte, shadcn/Tailwind, Chakra or Material. The core argument is that OpenUI Lang, a line-streamable compact format, is more token-efficient and streams better than nested JSON. He cites Vercel's JSON Render and Google's A2UI as JSON-based alternatives that use more than twice the tokens and latency, but shows no benchmark for those figures. The use cases he names are generative UI inside chat (charts, forms, selectors), and he calls the setup not production ready. A fast Cerebras-hosted model produced broken apps and hit errors and rate limits, so he switched to Gemini Flash. He closes by speculating that very fast future models, a secured backend and per-user sandboxed front-end generation could make this practical.

## Key ideas
- **OpenUI is a spec for rendering model-generated UI, not a UI library. It works with React, Svelte, shadcn/Tailwind, Chakra or Material, and its own component library is optional.** — The developer picks the renderer; OpenUI defines how model output maps to UI. ([2:42](https://youtu.be/AhVHtwh5k3E?t=162))
- **Generative UI fits small, on-demand UI inside chat: charts, data views, small forms, and selection widgets, instead of plain text or one repeated radio-card pattern.** — The speaker's examples are a day-plan map with pills and a list, and a drum pad built from a one-line request. ([1:18](https://youtu.be/AhVHtwh5k3E?t=78))
- **OpenUI Lang is a line-streamable compact format. Nested JSON must finish before it can be parsed, so line-based output renders sooner and uses fewer tokens.** — The speaker says JSON is verbose for this job and a custom language can beat its limits. ([2:42](https://youtu.be/AhVHtwh5k3E?t=162))
- **The integration pattern is: a system prompt lists the supported components and the OpenUI Lang grammar, the model replies in that format, and a React package turns the stream into components on the app's own server and client.** — Everything runs on free open-source packages, with no hosted renderer. ([3:51](https://youtu.be/AhVHtwh5k3E?t=231))
- **The speaker claims Vercel's JSON Render streams per line but uses over 2x the tokens and latency of OpenUI Lang, and Google's A2UI uses over 2x the tokens. These are his unsourced comparisons.** — No benchmark or methodology is shown. ([3:51](https://youtu.be/AhVHtwh5k3E?t=231))
- **Fast inference alone did not help. A Cerebras-hosted Qwen model (over 1800 tokens/s by his account) kept producing broken apps and hit errors and rate limits, so he moved to Gemini Flash.** — He calls the setup not production ready. Output quality mattered more than speed for this use. ([4:52](https://youtu.be/AhVHtwh5k3E?t=292))
- **Future architecture: a secured backend the generated apps call, with only the front end generated on demand inside a user-scoped sandbox.** — Speculative. He imagines this with a much faster future model at around 10,000 tokens/s. ([6:00](https://youtu.be/AhVHtwh5k3E?t=360))

## Techniques
- **Line-streamed generative UI DSL** — Put the supported component list and the OpenUI Lang grammar in the system prompt. Ask the model to answer in that format. Pass the stream through OpenUI's React lang package (the transcript names it as openui dev/react-lang) to render components as lines arrive. Run the parser on your own server and client, with no hosted renderer. *When:* Chat interfaces that need charts, forms, cards, or maps generated per request, where JSON would be slow to stream or costly in tokens.
- **Component allowlist as the UI boundary** — List the only components the model may use in the system prompt, and render only those. This keeps generated UI inside a design system you already have. The speaker presents this as the basis for customisation, but he does not show the validation step. *When:* Any LLM-generated UI that must match your existing component library and avoid arbitrary markup.
- **On-demand app generation from a title** — A launcher takes a title, sends it to a model with the system prompt, streams the generated app into view, and generates the icon from the same title. Each app is built when first opened. Demo only: no persistence or hardening is shown. *When:* Personal tools, prototypes, and throwaway utilities where a generated app is acceptable for the first run.
- **Pick model by output quality, not raw speed** — Test the candidate model on real generations first. In this demo a very fast model produced broken apps, so the speaker moved to Gemini Flash. *When:* Any generative-UI or code-generation path where a broken output costs more than latency.

## Numbers
- Cerebras-hosted Qwen claimed at over 1800 tokens/s; the speaker says it produced broken apps and hit rate and error limits. ([4:52](https://youtu.be/AhVHtwh5k3E?t=292))
- JSON Render (Vercel) claimed to use over 2x the tokens and over 2x the latency of OpenUI Lang. Unsourced. ([3:51](https://youtu.be/AhVHtwh5k3E?t=231))
- A2UI (Google) claimed to use over 2x the tokens of OpenUI Lang. Unsourced. ([3:51](https://youtu.be/AhVHtwh5k3E?t=231))
- Hypothetical future model at 10,000 tokens/s, used to imagine viability. Not a measurement. ([6:00](https://youtu.be/AhVHtwh5k3E?t=360))
- Demo video is 6:45 long. Three apps generated live: calculator, coffee shop finder, flight tracker. ([0:00](https://youtu.be/AhVHtwh5k3E?t=0))

## Hot takes
- The token and latency multipliers for JSON Render and A2UI are asserted without a benchmark, so treat them as the speaker's view until measured.
- The speaker says OpenUI is 'not a UI library', yet the demo depends on OpenUI's own React package. The spec is portable, but the working path is tied to that package.
- Honest caveats: the demo is local, not production ready, and a fast model produced broken output. Most of the value is in the streaming-format argument, not the demo.
- Light on substance for a tool review. Mostly a walkthrough with a short format explanation and no code, config, or repo link shown on screen.

## Tools mentioned
OpenUI, OpenUI Lang, OpenUI Dev React lang package, Gemini 3.8 Flash (as spoken), Cerebras, Qwen 3.8 (as spoken, likely Qwen 3), Vercel JSON Render (auto-caption reads 'Versa'), Google A2UI, ChatGPT intelligent UI (OpenAI), React, Svelte, shadcn/ui, Tailwind, Chakra UI, Material Design, Flutter, Google Maps

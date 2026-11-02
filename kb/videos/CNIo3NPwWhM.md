# Is Stealth Grok 4 Code Model (Sonic) Actually Good?

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `CNIo3NPwWhM` · [watch](https://youtu.be/CNIo3NPwWhM) · **date:** 2025-11-02 · **length:** 5:41 · **format:** review · **quality:** 2/5 · **depth:** practitioner
- **speakers:** Unnamed Better Stack host · **orgs:** OpenAI, Anthropic, xAI
- **topics:** coding-agents, models-research · **tags:** stealth-model, opencode, model-evaluation, three-js, react-three-fiber, vite, bun, openai-whisper, api-key-security, create-react-app, tailwind

> Hands-on test of the stealth coding model Sonic in OpenCode: strong one-shot code and server-side API key handling, weaker UI design, judged not better than Sonnet after a few hours.

## Summary
Better Stack tests Sonic, a stealth-released coding model that was free for a few hours in several coding tools, including OpenCode. The host gives it three build tasks in one OpenCode session: a 3D game with Three.js and React Three Fiber, a ball-in-rotating-hexagon demo, and a Bun/React/Vite app that transcribes dropped MP3 files with OpenAI Whisper. The first project was scaffolded with Create React App, which the host interrupted and redirected to Vite. Before building the Whisper app, the model asked whether it should be client-only or have a simple backend, and it kept the API key on the server, which is the check the host uses to separate good models from weak ones. The code structure impressed him, but the UI design was weak, and one Tailwind install error needed to be pasted back. His gut verdict after a few hours is that it is not better than Claude Sonnet, though it could become a default for easy-to-medium tasks if priced like GPT-5 or cheaper. The video is a single anecdotal session with no benchmarks.

## Key ideas
- **Sonic is a stealth-released coding model, free for a few hours in several coding tools. It has a 200k context window, is a reasoning model, is not multimodal, and is designed for code. Speculation that it is a Grok 4 coding model is reported but not confirmed.** — The host frames the model by its specs and the short free window, and says there is little official info. He tests it through OpenCode, switching the model with a slash command in a fresh session. ([0:00](https://youtu.be/CNIo3NPwWhM?t=0))
- **The agent's first scaffold choice was Create React App, so the host interrupted and asked for a rebuild on Vite. The resulting 3D game (Three.js with React Three Fiber, WASD/arrow movement, shift boost) took a bit over five minutes. Walls were clipped and coins were not collectible at first, and the floor placement was still wrong afterward.** — The host treats the scaffold decision as a quality signal. The boost mechanic and the coin fix after the first pass are the points he notes as positive. ([1:23](https://youtu.be/CNIo3NPwWhM?t=83))
- **The ball-in-rotating-hexagon prompt was solved in one shot with no clipping, and the stop/reset/rotate controls worked. The code was judged well structured, with good math, functions and comments, and modern APIs such as requestAnimationFrame. The one flaw noted was a `let` that should be `const`.** — The host says he would write it in a very similar way by hand. This is the strongest coding result in the video. ([1:23](https://youtu.be/CNIo3NPwWhM?t=83))
- **The model asked clarifying questions before building the MP3 transcription app (client-only or simple backend) without prompting. The host chose a backend, the agent put the OpenAI key in a Bun server file, and the front end did not expose it.** — The host says that good models such as Sonnet put the key in an Express-style backend, while weaker models expose it on the front end. He uses this as a model-quality test. ([2:47](https://youtu.be/CNIo3NPwWhM?t=167))
- **The app needed one fix: Tailwind was installed incorrectly, so the host pasted the error back. The site then worked and transcription produced readable text. The host found the UI design unimpressive and suspects his prompting may be part of the cause.** — The speed of the build impressed him. The run command uses concurrently to start the client and server together. ([4:02](https://youtu.be/CNIo3NPwWhM?t=242))
- **The verdict after a few hours is that Sonic is not better than Claude Sonnet, based on gut feel, and there are no benchmarks to compare against GPT-5 or other models. If it is priced as low as GPT-5 or lower, it could become his go-to model for easy and medium coding tasks.** — The conclusion depends on price, which the video does not establish. The host asks viewers whether they have tried it. ([5:16](https://youtu.be/CNIo3NPwWhM?t=316))

## Techniques
- **Interrupt and redirect a scaffold choice** — When the agent starts a project with a deprecated scaffold (here Create React App), interrupt it, tell it to remove the current code, and recreate the project with a different tool (here Vite) before it builds further. *When:* Any agent-driven project setup where the scaffold choice sets the rest of the build. Catch it early, before the agent builds on the wrong base.
- **API key placement probe** — Give the model a prompt for a Bun + React + Vite app that drags in MP3 files and transcribes them with OpenAI Whisper. Then check whether the key is read in a server file or lands in client-side code. Answer its clarifying question with a simple backend for security, and state the other requirements: no design constraints, a visually impressive UI, and multiple uploads. *When:* Screening models or agent output for secure defaults. A model that exposes the key on the front end fails the check.
- **Clarifying-questions prompt** — Include 'ask any questions if you have any' in the task prompt. The agent asked about architecture (client-only vs backend) before building. Answer with explicit constraints. *When:* Ambiguous specs where a wrong architectural guess costs a rebuild, such as client-only vs server-side design.
- **Prompt file as the project spec** — Put the project brief in a prompt .md file in the template and tell the agent to run that prompt file. The host says the model read it and asked its questions without preparation. *When:* Repeatable project scaffolds or model comparisons, where every model gets the same brief.
- **Paste-the-error repair loop** — When the generated project fails at install or run time (here a Tailwind install error), paste the error text back to the agent and let it fix the setup. *When:* Setup or build failures in agent-generated projects where the error is clear and local.
- **Mid-session model switch for comparison** — In OpenCode, change the active model with a slash command while keeping the session, then run the same task prompts on the new model. *When:* A/B testing a new model on the same tasks within a single tool setup.
- **Reviewing agent code by eye** — Read the generated code for structure, math, comments, use of modern web APIs (such as requestAnimationFrame), and small lint-style issues like let vs const. Judge it against what you would write by hand. *When:* Quick quality checks on small agent-written modules when there is no benchmark available.

## Numbers
- Sonic context window: 200k tokens ([0:00](https://youtu.be/CNIo3NPwWhM?t=0))
- Free access window: 'the next few hours' (stated, no fixed end time) ([0:00](https://youtu.be/CNIo3NPwWhM?t=0))
- 3D game build took a bit over five minutes (host estimate) ([1:23](https://youtu.be/CNIo3NPwWhM?t=83))
- Dev server reported at localhost port 5173 ([1:23](https://youtu.be/CNIo3NPwWhM?t=83))
- Testing period before verdict: a few hours of use, with no benchmarks available ([5:16](https://youtu.be/CNIo3NPwWhM?t=316))

## Hot takes
- Judging a stealth model after a few hours of free access on a handful of prompts is anecdotal, and the host says so.
- Coding quality (structure, math, comments, modern APIs) is praised, but UI design is called weak and possibly the result of the host's own prompting.
- API key placement is presented as the discriminator between good and weak models, and this model passed.
- Gut verdict: not better than Sonnet. It could be the default for easy-to-medium tasks only if priced like GPT-5 or cheaper, which is not established.

## Tools mentioned
OpenCode (version 5.8 as stated in the video), Sonic (stealth model, name as spoken), Grok 4 (speculated link, unconfirmed), Claude Sonnet 4, GPT-5, Three.js, React Three Fiber, React, Create React App, Vite, Bun, Tailwind CSS, concurrently, OpenAI Whisper, Express (spoken as express backend), Two coding tools named in captions as RuCode and KleinCursor (likely misspelled, not verified)

## Relevance to our work
- **agentos** (1/3): A per-model probe of scaffold choice, key handling and clarifying-question behavior could feed strategy routing when a cheap coding model is added. → *Add a fixed probe set (scaffold choice, API key kept server-side, asks clarifying questions) to the eval suite before routing a new cheap model in Govrix Scout's strategy routing.*
- **prosharness** (1/3): ProsHarness does zero-token credential handling, and the video gives a concrete check for secrets reaching client code in agent-generated apps. → *Add a verification step that fails when an agent-generated app's OpenAI key appears in client-side bundle code.*

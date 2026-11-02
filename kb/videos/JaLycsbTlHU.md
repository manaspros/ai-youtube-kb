# GLM 4.7 is INSANE For Software Dev...

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `JaLycsbTlHU` · [watch](https://youtu.be/JaLycsbTlHU) · **date:** 2026-01-02 · **length:** 6:10 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** AI LABS host (unnamed) · **orgs:** Z.ai (ZAI), Anthropic, Google, OpenAI, AI LABS
- **topics:** coding-agents, token-cost-efficiency, models-research · **tags:** GLM-4.7, Claude Code, Z.ai coding plan, SWE-bench, UI generation, Next.js, shadcn, Framer Motion, mock data architecture, model comparison, cheap coding plan

> AI LABS tests Z.ai's GLM 4.7 as a Claude Code backend: cheap coding plan, better architecture than 4.6, but slow and not autonomous enough to run unattended.

## Summary
The video is a hands-on comparison of GLM 4.7 (Z.ai) against Claude Sonnet 4.5 inside Claude Code. The host covers the claimed SWE-bench score, the cheap coding plan and its prompt limits versus Claude's plans, and a design-generation test (a single HTML/JS prompt) where Claude's output looked better, though GLM's had emojis and a length-handling bug. In a Next.js and shadcn/Framer Motion streaming-homepage build, GLM ignored the provided UI benchmark folder and scaffolded its own app, but its mock-data layout (one data file feeding all imports) was a better back-end-ready structure than Claude's per-component imports. The host notes GLM 4.7 now shows thinking in Claude Code (4.6 did not), that generation is still very slow, and that the model needs steering. The host recommends the $29/year plan but advises against unattended autonomous coding. Sponsorship and ad content is minimal; the main value is a single-developer side-by-side test with modest sample size.

## Key ideas
- **GLM 4.7 is a post-training improvement on 4.6 (no architecture change), explicitly optimized for Claude Code, and Z.ai claims 73% on SWE-bench.** — The host reports the 73% SWE-bench claim (vendor claim, not verified in the video) and says the model is heavily tuned for Claude Code as Z.ai's priority framework. ([0:00](https://youtu.be/JaLycsbTlHU?t=0))
- **The coding plan is far cheaper per prompt than Claude's plans, at the cost of speed and some autonomy.** — Host says the entry GLM plan is about $3 for roughly 120 prompts per 5-hour window versus 10-40 on Claude's entry plan. The $200 Claude plan gets about 800 prompts versus about 2,400 on a $30 GLM tier. Intro prices are discounted for the first month and then double; the yearly plan is cheapest. ([1:05](https://youtu.be/JaLycsbTlHU?t=65))
- **On a design-only prompt, Claude Sonnet 4.5 produced cleaner output, but GLM 4.7 was close.** — Both models built a simple vanilla JS UI from a prompt about design logic for an AI code-review platform. GLM's output had emojis the host disliked and a length-handling bug that broke the artifacts. Sonnet used no emojis and matched the design language. ([2:30](https://youtu.be/JaLycsbTlHU?t=150))
- **GLM 4.7 now shows thinking inside Claude Code, which 4.6 did not.** — The host says the detailed transcript shows thinking blocks for 4.7, a fix from 4.6. Code generation remains extremely slow in the host's experience. ([3:58](https://youtu.be/JaLycsbTlHU?t=238))
- **GLM 4.7 is not reliably autonomous: it ignored the provided UI benchmark folder and scaffolded its own Next.js app.** — Even though the context said where to build, GLM started a new Next.js project without initializing it. The host had to correct it and steer it before it followed the right implementation path. ([3:58](https://youtu.be/JaLycsbTlHU?t=238))
- **On back-end-ready architecture, GLM's mock-data layout was better than Claude's, even though Claude's UI was better.** — GLM placed all mock data in one file that every import references, so swapping in a real backend only requires changing one file. Claude gave each component its own import, so the swap touches every file. Host says the code-quality result surprised them given 4.6's weaker results. ([4:00](https://youtu.be/JaLycsbTlHU?t=240))
- **Host recommends the cheap plan but advises against relying on GLM for fully autonomous coding.** — The host says GLM is a good model for the price, but its quirks (slowness, weak autonomy, ignoring instructions) mean it should not be the only agent. Claude still corrects and improves weaker architecture later. ([5:25](https://youtu.be/JaLycsbTlHU?t=325))

## Techniques
- **Config GLM as the Claude Code backend via settings.json** — Set the GLM endpoint and key in settings.json. The host says the file can be placed in the project root (per-project, takes effect only for that project) or in the global settings (global). Exact keys are not shown in the transcript. *When:* When you want to run Claude Code with GLM on a cheap plan and compare it side by side with Claude.
- **Design-only UI benchmark prompt** — Give the model a prompt that focuses on design logic and asks for a few design options, with no architecture requirements. Compare the output across models for consistency with the design language and for emoji or layout quirks. *When:* When you want a quick, repeatable test of which model produces better UI design.
- **Back-end-ready mock data structure** — Put all mock data in one module that every component imports from. When the backend is ready, only that file has to change. Avoid importing mock data from each component separately. *When:* When building a UI that will later connect to a real backend, so the swap is a single-file change.
- **Steer a weak autonomous run** — When the agent ignores a provided benchmark folder or starts a new project, correct it explicitly and point it to the existing folder before it writes code. *When:* When a cheap model drifts from the given project layout. The host notes this was needed with GLM 4.7.

## Numbers
- GLM 4.7 claims 73% on SWE-bench (vendor claim, not verified in the video), close to Sonnet 4.5. ([0:00](https://youtu.be/JaLycsbTlHU?t=0))
- Entry GLM coding plan is about $3 for about 120 prompts per 5-hour window, versus 10-40 prompts on Claude's entry plan. ([1:05](https://youtu.be/JaLycsbTlHU?t=65))
- $200 Claude plan: about 800 prompts per 5-hour window. $30 GLM tier: about 2,400. ([1:05](https://youtu.be/JaLycsbTlHU?t=65))
- GLM plan prices are discounted for the first month and then double. The yearly plan is the cheapest option; the host recommends the $29/year plan. ([1:05](https://youtu.be/JaLycsbTlHU?t=65))
- Host's yearly GLM recommendation is $29 per year; host says it is 'basically nothing' next to a $20 Claude plan. ([5:25](https://youtu.be/JaLycsbTlHU?t=325))

## Hot takes
- GLM 4.7 is good enough, at this price, to be the cheap default for coding.
- Claude Sonnet 4.5 still produces the better UI design, but GLM's back-end architecture was better.
- Do not rely on GLM 4.7 alone for autonomous coding, despite the good results.
- Transcript shows GLM 4.7 is now a real improvement over 4.6 (thinking shown, better architecture), a 'huge leap' in the host's words.

## Tools mentioned
GLM 4.7 (Z.ai), GLM coding plan (Z.ai), Claude Code, Claude Sonnet 4.5, Claude Max plan, Next.js, shadcn/ui, Framer Motion, Gemini 3, GPT-5, Humanity's Last Exam (benchmark), SWE-bench (benchmark), settings.json

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code and cares about cheap-model pipelines, autonomy, and steering. The talk shows the autonomy gap and the need for steering that a harness must handle, plus the per-project versus global settings.json layering. → *Add a harness check that catches a worker agent starting a new project instead of using the provided folder, and test whether the per-project settings.json override approach works for swapping models per project.*
- **agentos** (1/3): Cheap-model routing for coding and a comparison of GLM 4.7 against Claude are relevant to the budget and strategy-routing pillar, but the talk is a single-developer test with no measured latency or cost numbers.

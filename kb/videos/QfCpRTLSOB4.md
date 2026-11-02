# Kimi K3 Is Fable Level... (they should be worried)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `QfCpRTLSOB4` · [watch](https://youtu.be/QfCpRTLSOB4) · **date:** 2026-08-02 · **length:** 10:51 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Unnamed Better Stack presenter · **orgs:** Better Stack, OpenRouter, Artificial Analysis
- **topics:** models-research, coding-agents, token-cost-efficiency · **tags:** open-weights, model-comparison, cost-per-task, one-shot-generation, harness-comparison, threejs, full-stack-generation, kimi, glm

> Hands-on one-shot app tests of open-weight Kimi K3 against Fable 5, GPT 5.6 Sol and GLM 5.2: near-frontier output and per-task cost, but single runs and harness effects muddy the result.

## Summary
Better Stack presents Kimi K3, described as a 2.8T-parameter open model with native vision and a 1M-token context window, and reports it close to Fable 5 and GPT 5.6 Sol on Moonshot's own benchmarks. Third-party indexes (Artificial Analysis) roughly agree: a coding index of 76.2, 0.3 behind Fable 5, and third place on the agentic index. Pricing is $3 per million input tokens and $15 per million output tokens, above K2.6 and near Sonnet 5, but the cost per task is similar to GPT 5.6 Sol and about half of Opus 4.8. The hands-on tests are one-shot builds of a Three.js F1 racing game and a full-stack personal finance dashboard, each run once. K3 was run through OpenRouter and through the Kimi Code CLI, with Fable 5 (Claude Code, Max), GPT 5.6 Sol (Max) and GLM 5.2 as comparisons. The speaker judges K3 functionally on par with the frontier on both apps, and shows that the harness and the default stack choices change the output. He concludes that short demos cannot separate frontier models, and that real differences show up over a week in a production codebase.

## Key ideas
- **Kimi K3 is presented as a 2.8T-parameter open model built on Kimi Delta Attention and Attention Residuals, with native vision and a 1M-token context window.** — The speaker's headline claim is that K3 caught up with Fable and GPT 5.6 on Moonshot's own benchmarks. He stresses that these are the vendor's numbers before checking third-party results. ([0:00](https://youtu.be/QfCpRTLSOB4?t=0))
- **Third-party indexes roughly match the vendor claims.** — Coding index 76.2, 0.3 behind Fable 5 and slightly ahead of GPT 5.5 and Opus 4.8. On the agentic index K3 is third, behind Fable and Sol. Deep SWE results were not yet available at recording time. ([0:53](https://youtu.be/QfCpRTLSOB4?t=53))
- **Compare models on cost per task, not per-token price.** — List price is $3 per M input and $15 per M output, a large step up from K2.6 and close to Sonnet 5 list. The speaker's per-task cost puts K3 near GPT 5.6 Sol and about half of Opus 4.8. ([0:53](https://youtu.be/QfCpRTLSOB4?t=53))
- **GLM 5.2 is the cheaper open alternative and the next-best open model in the speaker's tests.** — It costs about half as much as K3 and is described as not the fastest, but competitive for its intelligence level. ([2:17](https://youtu.be/QfCpRTLSOB4?t=137))
- **Same one-shot prompt, different harness, different result.** — K3 via OpenRouter and K3 via the Kimi Code CLI both built a working Three.js F1 game with AI racers, lap tracking and barriers. The Kimi Code version had better assets and handling, but the controls were inverted, as they were in most of the Three.js outputs. ([3:18](https://youtu.be/QfCpRTLSOB4?t=198))
- **Unspecified stack choices show each model's defaults, and these vary by harness.** — For the finance dashboard, K3 via OpenRouter built its own view system and router, its own Express server, and stored data in a JSON file. K3 via Kimi Code used React with Node SQLite. The speaker says he would have preferred a named router, an ORM or a real DB if he had specified the stack. ([5:44](https://youtu.be/QfCpRTLSOB4?t=344))
- **GPT 5.6 Sol wrote the most complete code, but it also deployed the app without being asked.** — It produced a Next.js app with Drizzle and hosted it on Cloudflare through a ChatGPT hosting feature. The speaker would rather ask for hosting himself. GLM 5.2 used Next.js but kept all state in memory. ([7:44](https://youtu.be/QfCpRTLSOB4?t=464))
- **Short demos cannot separate frontier models.** — The speaker says quality shows up over about a week in a production codebase, and asks viewers for harder test ideas. He also shows the vendor's examples: a game and a chip design created in a single 48-hour autonomous run, which he has not verified. ([8:59](https://youtu.be/QfCpRTLSOB4?t=539))

## Techniques
- **One-shot app bake-off** — Give every model the same single prompt and record wall-clock time, API cost, and whether the features work when played. Prompt 1: a complete F1 racing game in Three.js in one index.html. Prompt 2: a full-stack personal finance dashboard with seeded data, no auth, and no stack specified. Run each once and judge by manual testing. *When:* Quick, informal comparison of model capability on greenfield generation. The speaker's own sample size is one run per model, so treat it as a smoke test, not a benchmark.
- **Separate harness effects from model effects** — Run the same model through two routes: a raw API gateway (OpenRouter) and the vendor's coding CLI (Kimi Code). Compare time, cost, asset quality, stack choice and bugs between the two. *When:* Before deciding how to route a model into an agent. The speaker found the harness changed both output quality and default architecture.
- **Name the stack in the prompt when it matters** — Specify the router, ORM, database and server in the prompt, or in a project context file. Otherwise the model picks its own defaults, such as a hand-rolled view system or a JSON file as the database. *When:* Any generated app that you intend to extend or scale. The speaker's recommendation for default choices.
- **Rank models by cost per completed task** — Compare models on the cost of a finished task (for example, $1.24 for K3's game versus a larger figure for a frontier model) instead of list price per million tokens. *When:* Model selection for cost-sensitive agent traffic. The speaker notes list price can mislead.
- **Disable unrequested auto-hosting** — State in the prompt that the app should not be deployed or hosted. The speaker reports GPT 5.6 Sol deployed to Cloudflare without that instruction. *When:* Any code-generation run where you want to control deployment yourself.

## Numbers
- Kimi K3 is a 2.8T-parameter model with a 1M-token context window (vendor claim). ([0:00](https://youtu.be/QfCpRTLSOB4?t=0))
- Coding index score 76.2, 0.3 points behind Fable 5. ([0:53](https://youtu.be/QfCpRTLSOB4?t=53))
- API price $3 per M input tokens and $15 per M output tokens. ([0:53](https://youtu.be/QfCpRTLSOB4?t=53))
- Cost per task is similar to GPT 5.6 Sol and about half of Opus 4.8. ([0:53](https://youtu.be/QfCpRTLSOB4?t=53))
- F1 game via K3 on OpenRouter: 14 min thinking before starting, 35 min total, $1.24 in API tokens. ([2:17](https://youtu.be/QfCpRTLSOB4?t=137))
- F1 game via Fable 5 in Claude Code (Max): 44 min. GPT 5.6 Sol (Max): 18 min. ([3:18](https://youtu.be/QfCpRTLSOB4?t=198))
- GLM 5.2 F1 game: thought for 5 min 58 s, did not finish in one prompt, and needed a second prompt to fix bugs. ([4:33](https://youtu.be/QfCpRTLSOB4?t=273))
- Finance dashboard via K3 on OpenRouter: 56 min total, $1.30. ([5:44](https://youtu.be/QfCpRTLSOB4?t=344))
- Finance dashboard via Fable 5 in Claude Code: 56 min at max effort. GPT 5.6 Sol (Max): 31 min. ([6:38](https://youtu.be/QfCpRTLSOB4?t=398))
- GLM 5.2 finance dashboard: 15 min, $1.11. ([8:59](https://youtu.be/QfCpRTLSOB4?t=539))
- Vendor chip-design example: K3 built, optimized and verified a chip in a single 48-hour autonomous run (not verified by the speaker). ([10:07](https://youtu.be/QfCpRTLSOB4?t=607))

## Hot takes
- The title's 'Fable level' and 'they should be worried' overstate the evidence: each model was run once per prompt, and the judgment of quality is mostly the speaker's eye.
- Most of the benchmark numbers are Moonshot's own, with only the intelligence and agentic indexes checked by a third party. Deep SWE results were not available yet.
- Calling the model 'open' is premature by the speaker's own account: the weights had not been released at recording time, and at this size it is not practical to run locally.
- The harness and the model are confounded in the cost and time comparisons, yet the speaker's own tests show the harness changes the output as much as the model does.

## Tools mentioned
Kimi K3, Kimi Code CLI, OpenRouter, Claude Code, Fable 5, GPT 5.6 Sol, GPT 5.6 Terra, GPT 5.6 Luna, GPT 5.5, Opus 4.8, Sonnet 5, K2.6, GLM 5.2, Three.js, React, Express, Node SQLite, Next.js, Drizzle, Cloudflare, Kimi Delta Attention, Attention Residuals

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code, and this video shows the same model giving different time, cost, stack and asset results across two harnesses. → *Run one ProsHarness task through the same model with two harness configurations and log time, cost and stack choices to measure the harness effect before tuning the model.*
- **agentos** (1/3):  → *Add Kimi K3 and GLM 5.2 as candidate upstream models in the strategy-routing benchmark for API traffic. Do not plan local serving for them.*
- **general** (1/3): The video shows how default stack choices (own router, JSON-file DB, unrequested hosting) appear when the prompt is left unspecified, which bears on context-file design. → *Put the stack, database, and no-deploy rules in CLAUDE.md or the project context file so agent defaults do not decide them.*

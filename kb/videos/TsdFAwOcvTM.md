# The Open Models Have Caught Up (MiniMax M2.1 & GLM 4.7 Review)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `TsdFAwOcvTM` · [watch](https://youtu.be/TsdFAwOcvTM) · **date:** 2026-02-02 · **length:** 8:17 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Better Stack, OpenRouter, Design Arena, Anthropic, Google
- **topics:** models-research, token-cost-efficiency, coding-agents · **tags:** MiniMax M2.1, GLM 4.7, open-weight models, cost per task, UI generation, OpenCode, OpenRouter, Design Arena, thinking loops, Drizzle, SQLite, Next.js, Claude Sonnet 4.5, Claude Opus 4.5, Gemini 3 Pro

> Hands-on review of MiniMax M2.1 and GLM 4.7 against Sonnet 4.5, Opus 4.5 and Gemini 3 Pro on UI design and a full app build; open-weight models are cheap and strong on design, but first-attempt completion and backend correctness lagged.

## Summary
The host compares two open-weight models, MiniMax M2.1 and GLM 4.7, against Claude Sonnet 4.5, Claude Opus 4.5 and Gemini 3 Pro, all run through OpenCode. A single-prompt finance dashboard test finds the designs broadly similar, with MiniMax costing about $0.02 against $0.50 for Opus. Design Arena ELO rankings put MiniMax and GLM above Sonnet, though the host personally got better results from MiniMax than GLM. In a longer full-app build (a Next.js, Drizzle and SQLite boilerplate with a mockup and success criteria), MiniMax delivered a mostly working app for about $0.33, GLM matched the design but its database features failed for $2.64, and Sonnet built working backend features with a weaker front end for about $5.20. The host also reports MiniMax's thinking repeatedly looping and that none of the models finished in the first prompt. The conclusion is that open models have caught up on cost and design, but Opus 4.5 and Gemini 3 Pro delivered complete, working apps in about 10 minutes of prompting, which the host argues makes them cheaper once human oversight time is counted.

## Key ideas
- **Open-weight models now compete with Sonnet 4.5 on benchmarks at a fraction of the cost.** — The host frames MiniMax M2.1 and GLM 4.7 as near Sonnet 4.5, sometimes Gemini 3 Pro and Opus, on benchmarks, and says real-world use feels good too. ([0:00](https://youtu.be/TsdFAwOcvTM?t=0))
- **On single-prompt UI design, open models produce designs about as good as the frontier models, at a tiny fraction of the price.** — Same finance dashboard prompt in OpenCode: MiniMax about $0.02, GLM about $0.06, Sonnet about $0.26, Opus about $0.50. The host finds the designs similar, and Gemini 3 Pro was the only one that looked different, still using purple despite a request not to. ([0:35](https://youtu.be/TsdFAwOcvTM?t=35))
- **Design Arena ELO rankings put MiniMax and GLM above Sonnet, but the host's own experience disagreed on which one is better.** — Design Arena is a head-to-head ranking site. The host personally got better results from MiniMax than GLM, while GLM leads on the arena. ([2:00](https://youtu.be/TsdFAwOcvTM?t=120))
- **On a multi-feature app build, open models can produce a working app for cents to a few dollars, but feature correctness varies.** — About 30 minutes of prompting per model. MiniMax: $0.33, mostly working with a wrong color scheme. GLM 4.7: matched the mockup but its Drizzle-to-local-database features did not work, $2.64. Sonnet 4.5: backend worked, front end did not match the mockup, $5.22 (later quoted as $5.20). ([3:00](https://youtu.be/TsdFAwOcvTM?t=180))
- **None of the models finished in the first prompt, and the open models left stub buttons that said coming soon.** — Sonnet reported about 80% of the features done. GLM and MiniMax shipped coming-soon buttons. The host asked each model to continue until the task was complete. ([4:19](https://youtu.be/TsdFAwOcvTM?t=259))
- **MiniMax's thinking got stuck repeating itself, and the host saw it every time, which may be an OpenCode or OpenRouter issue rather than the model.** — Recovery was to stop the run, then ask it to continue. The host also noted MiniMax considered switching from TypeScript to JavaScript and settled on a casting fix; Sonnet made the same casting fix. ([5:27](https://youtu.be/TsdFAwOcvTM?t=327))
- **Cost per task should include how many prompts and how much human oversight it takes to get a finished result.** — Opus 4.5 and Gemini 3 Pro produced a mockup-matching app with working features in a single prompt of about 10 minutes, or with one or two fix-up prompts for Gemini. The host argues this makes them more predictable and worth the price, especially for companies. ([6:51](https://youtu.be/TsdFAwOcvTM?t=411))

## Techniques
- **Same-prompt cross-model bake-off** — Give every model the identical prompt, boilerplate and mockup inside the same harness (OpenCode in this video). Record cost per run, a written success-criteria checklist of features, and visual match against the mockup. Score first-attempt completion separately from completion after follow-up prompts. *When:* Choosing a cheap model for a coding or UI task, or checking whether a cheaper model is good enough before routing work to it.
- **Continue-until-done follow-up** — After a model stops early (stubs, 80% done), send a follow-up asking it to carry on until every feature works, then re-check the checklist. *When:* Evaluating agentic coding models where first-pass completeness is the variable being measured.
- **Cost-to-done accounting** — Add re-prompt count and human oversight time to token cost, then compare total cost to a finished, working result rather than per-token price. *When:* Deciding whether a cheap model is actually cheaper than a frontier model for a given task.
- **Thinking-loop recovery** — Watch the thinking stream for repeated text, stop the run when it loops, then send a short instruction to continue. The host saw this with MiniMax in OpenCode and OpenRouter. *When:* Running open-weight reasoning models through third-party hosts where degenerate repetition appears.

## Numbers
- Finance dashboard single-prompt cost: MiniMax M2.1 about $0.02, GLM 4.7 about $0.06, Sonnet 4.5 about $0.26, Opus 4.5 about $0.50 (host says Opus is about 25x MiniMax). ([0:35](https://youtu.be/TsdFAwOcvTM?t=35))
- Full app build (about 30 min of prompting): MiniMax about $0.33, GLM 4.7 $2.64 with similar token count to MiniMax, Sonnet 4.5 $5.22 (later quoted as $5.20). ([3:00](https://youtu.be/TsdFAwOcvTM?t=180))
- Opus 4.5 and Gemini 3 Pro each produced a working app in about 10 minutes of prompting. ([6:51](https://youtu.be/TsdFAwOcvTM?t=411))
- Sonnet 4.5 reported about 80% of features complete after its first output. ([4:19](https://youtu.be/TsdFAwOcvTM?t=259))

## Hot takes
- Open-weight models have caught up on design and cost, but finishing the job without manual oversight is still the frontier models' advantage (host's own conclusion).
- Design Arena ELO and the host's personal experience disagree on which of MiniMax or GLM is better.
- The GLM cost gap ($2.64 vs $0.33) is reported alongside 'about the same amount of tokens', which the video does not explain.
- Every test is n=1 per model with subjective design judgment, so the results are anecdotal rather than a controlled eval.

## Tools mentioned
MiniMax M2.1, GLM 4.7, Claude Sonnet 4.5, Claude Opus 4.5, Gemini 3 Pro, OpenCode, OpenRouter, Design Arena, Next.js (transcribed as NextGest), Drizzle ORM, SQLite

## Relevance to our work
- **agentos** (1/3): Shows open models are cheap enough to be candidate routes, but the video compares via hosted APIs (OpenRouter) and does not measure self-hosted serving. → *Add a cost-to-done routing case (cost plus re-prompt count to a passing checklist) to the Govrix strategy-routing evaluation, using open-weight and frontier models.*
- **prosharness** (1/3): ProsHarness wraps Claude Code, and this video shows that open models can be swapped in as the coding worker but need completion checks and loop recovery. → *Evaluate ProsHarness with an alternative model backend on the same mock-app checklist, and add a completion check that re-prompts until every checklist item passes.*

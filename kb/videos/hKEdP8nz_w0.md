# Ox Alpha – Use This While It's FREE (Stealth Model)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `hKEdP8nz_w0` · [watch](https://youtu.be/hKEdP8nz_w0) · **date:** 2026-09-02 · **length:** 8:31 · **format:** review · **quality:** 2/5 · **depth:** practitioner
- **speakers:** Better Stack presenter (not named in transcript) · **orgs:** Better Stack, OpenRouter, OpenCode, Kilo (captioned as 'Klein'), Z.ai (GLM), OpenAI, Google
- **topics:** models-research, token-cost-efficiency, vibe-coding-app-building · **tags:** stealth-model, oxalpha, free-models, openrouter, model-comparison, cost-benchmarking, glm, drizzle-orm, nextjs, model-attribution, deepswe

> Better Stack runs one full-stack app prompt through a free stealth model, OxAlpha, and rival models, then argues from code fingerprints that it is likely based on GLM 5.3.

## Summary
The video covers OxAlpha, an unnamed model offered free for a limited window on OpenRouter, OpenCode, Kilo and another platform, with a 1M-token context and text, image and video input. The presenter first discounts launch benchmark claims: a 10-task DeepSWE subset beat GPT 5.6, but a fuller run reportedly lands near 63%, in the Grok, DeepSeek and Gemini range, and the model averaged about 47k output tokens. He then gives one identical prompt (a full-stack personal finance dashboard, no stack specified) to OxAlpha and six other models and judges usability, stack choice, time and cost. OxAlpha produced a usable Next.js app with Drizzle and better-sqlite3 in about 84k tokens and 45 minutes, which he rates well. The frontier models at medium effort were faster and cheaper but weaker, with no real database or unimplemented tabs. GLM 5.3 used the same Next.js, Drizzle and better-sqlite3 stack and was the most expensive run at about $5. He asked Claude to compare the codebases, and structural and rare-marker overlap pointed to GLM, with the Drizzle overlap flagged as a possible false positive. He adds community evidence (tokenizer, error messages, vision-encoder tokens matching GLM) and concludes it is probably GLM-based, possibly GLM 5.5 or a Flash variant, while noting free access ends on the 27th and that prompts and completions are retained by the provider even though not used for training.

## Key ideas
- **A free stealth model, OxAlpha, is offered for a limited window with a 1M-token context and multimodal input.** — Launch posts claim zero data retention and very large capacity figures. The presenter later says providers do retain prompts and completions, though not for training. ([0:00](https://youtu.be/hKEdP8nz_w0?t=0))
- **Launch benchmark claims are misleading when taken from a small subset.** — A 10-task DeepSWE run beat GPT 5.6, but a fuller run is nearer 63%, which places it near Grok, DeepSeek and Gemini. It also averaged about 47k output tokens per task. ([1:01](https://youtu.be/hKEdP8nz_w0?t=61))
- **A single identical app-building prompt with no stack specified reveals stack choices and usability.** — The presenter compares the generated apps on whether the features work, which framework and ORM were chosen, whether a real database is used, and time and cost. ([2:12](https://youtu.be/hKEdP8nz_w0?t=132))
- **OxAlpha's finance dashboard is usable, on Next.js with a real database.** — It used Next.js, Drizzle and better-sqlite3, took 84k tokens and about 45 minutes, and the features worked. The presenter says he could use it himself. ([2:12](https://youtu.be/hKEdP8nz_w0?t=132))
- **Open models were the cheapest runs, while frontier models at medium effort were fast but weaker.** — DeepSeek V4 Pro took about 15 minutes for $0.19 and gave a comparable Next.js app. Fable Medium took 3m42s for $2.60 and produced a React and Express app that stores data in memory, so it is lost on refresh. ([3:38](https://youtu.be/hKEdP8nz_w0?t=218))
- **GPT 5.6 Sol at medium effort gave a cheap but incomplete app.** — It took about four minutes for $0.33. The app has a UI and the send and add-funds features work, but the accounts, transactions, investments and goals tabs are unimplemented and there is no real database. ([4:29](https://youtu.be/hKEdP8nz_w0?t=269))
- **Code fingerprinting, not benchmarks, is the basis for the GLM attribution.** — Claude's comparison found GLM 5.3 with 22.4% structural overlap versus 19% for DeepSeek. Removing Drizzle, a shared choice, to test for a false positive still left GLM as the closest match on rare markers such as a shared helper function and an identical rewritten README. ([5:35](https://youtu.be/hKEdP8nz_w0?t=335))
- **The attribution to a GLM-based model is the presenter's inference, not a confirmed fact.** — He cites community evidence (tokenizer, error messages, vision-encoder tokens matching GLM) and suggests GLM 5.5, a post-trained GLM 5.3, a Flash variant, or another company building on GLM. The free window is said to end on the 27th. ([7:52](https://youtu.be/hKEdP8nz_w0?t=472))

## Techniques
- **Same-prompt full-stack bake-off** — Send one identical multi-feature prompt (e.g. a personal finance dashboard) to every model, with no stack specified. For each run, record tokens, wall-clock time and cost, click through every feature, check whether the data layer is a real database, and note framework, ORM and database choices. *When:* Choosing a model for app-building agents, or comparing cheap and frontier models on open-ended builds. It is one run per model, so treat the result as anecdotal.
- **Stack fingerprinting for model attribution** — Ask Claude to compare the generated repositories on (a) structural patterns such as how components are assembled, (b) rare markers, meaning non-default choices like a shared helper function's shape or a README rewritten with the same section structure, and (c) a rerun after removing a common choice (Drizzle here) to test for false positives. *When:* Guessing which base model produced some code. This is weak evidence and should be checked against other signals.
- **Community fingerprint cross-checks** — Compare a suspect model's tokenizer behaviour, exact error-message text and vision-encoder token output with a known model's public behaviour. *When:* When code-level similarity is ambiguous and you want a second, independent signal.
- **Rerun the full benchmark before trusting a launch claim** — When a launch post cites a subset result, rerun the full suite and compare against the fuller number before drawing conclusions. *When:* Evaluating a new model's launch benchmarks.
- **Check retention terms before using free endpoints** — Read the provider's retention and training policy for prompts and completions before sending proprietary code through a free or stealth endpoint. *When:* Using a free, promotional or stealth model through a router such as OpenRouter.

## Numbers
- 1M-token context window for OxAlpha ([0:00](https://youtu.be/hKEdP8nz_w0?t=0))
- Launch capacity claims of 100 trillion tokens per day (OpenCode) and 1 quadrillion per day (news research), as stated in the video ([0:00](https://youtu.be/hKEdP8nz_w0?t=0))
- DeepSWE: a 10-task subset beat GPT 5.6; a fuller run is near 63% ([1:01](https://youtu.be/hKEdP8nz_w0?t=61))
- OxAlpha averaged about 47,000 output tokens per task ([1:01](https://youtu.be/hKEdP8nz_w0?t=61))
- OxAlpha finance app: about 84,000 tokens and about 45 minutes ([2:12](https://youtu.be/hKEdP8nz_w0?t=132))
- DeepSeek V4 Pro: about 15 minutes, $0.19 ([2:12](https://youtu.be/hKEdP8nz_w0?t=132))
- Kimi K3: 38 minutes, $1.92 ([2:12](https://youtu.be/hKEdP8nz_w0?t=132))
- Fable Medium: 3 min 42 s, $2.60 (most expensive of the closed runs, per the presenter) ([3:38](https://youtu.be/hKEdP8nz_w0?t=218))
- GPT 5.6 Sol (medium effort): about 4 minutes, $0.33 ([4:29](https://youtu.be/hKEdP8nz_w0?t=269))
- Gemini 3.7 Flash (high effort): about 10 minutes, $0.50 ([5:35](https://youtu.be/hKEdP8nz_w0?t=335))
- GLM 5.3: about 50 minutes, about $5 (most expensive run) ([5:35](https://youtu.be/hKEdP8nz_w0?t=335))
- Structural overlap with OxAlpha per Claude's comparison: GLM 5.3 22.4%, DeepSeek 19% ([5:35](https://youtu.be/hKEdP8nz_w0?t=335))
- Free pricing is said to end on the 27th (no date given in the video) ([7:52](https://youtu.be/hKEdP8nz_w0?t=472))

## Hot takes
- The title ('FREE', 'nobody knows what it is') is hype, and the model-identity verdict is speculation that the presenter himself hedges.
- Each model was run once on one prompt, so the usability and stack judgments rest on one sample per model.
- Time and cost comparisons mix effort levels (frontier models were at medium effort) and the video does not show matching settings, so they are not like-for-like.
- The fingerprinting method is more useful than the verdict: it names a likely false positive (Drizzle) and checks it by removing the shared choice.
- The provider-retention point is made in passing and conflicts with the launch's zero-data-retention claim; the presenter does not resolve it.

## Tools mentioned
OxAlpha (stealth model, as named in the video), OpenRouter, OpenCode, Kilo (captioned as 'Klein'), Next.js, Drizzle ORM, better-sqlite3 (captioned as 'Better SQLite'), Express, Node SQLite, React, Claude (used to compare codebases), DeepSeek V4 Pro, Kimi K3, GLM 5.3, GLM 5.5 (speculated), GLM vision model, Fable Medium (as captioned), Soul Medium (as captioned), GPT 5.6 Sol (medium effort), Gemini 3.7 Flash (high effort), Grok, DeepSWE benchmark

## Relevance to our work
- **general** (2/3): A practitioner comparison of cheap versus frontier models on one open build task, close to our cheap-model pipeline interest; the fingerprinting method is reusable. → *Run the same one-prompt bake-off with token, time and cost logging on a few cheap Haiku-class models against one frontier model to decide where cheap models are safe in our pipelines.*
- **agentos** (1/3): Per-model cost and time matter for cheap-model routing, but this is one anecdotal app test, not a routing signal. → *Add a cost-per-task and wall-time column to any model-routing comparison we run, using token counts from the run, not only output quality.*

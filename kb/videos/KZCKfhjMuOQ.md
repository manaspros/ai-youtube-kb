# Opus 4.7 Is GREAT (except the token usage)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `KZCKfhjMuOQ` · [watch](https://youtu.be/KZCKfhjMuOQ) · **date:** 2026-05-02 · **length:** 10:51 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Better Stack host (not named in the transcript) · **orgs:** Anthropic, Google, OpenAI, Design Arena, Better Stack
- **topics:** models-research, token-cost-efficiency, coding-agents, vibe-coding-app-building · **tags:** claude-opus-4-7, tokenizer, effort-levels, token-usage, benchmarks, instruction-following, long-context-regression, ui-generation, single-prompt-app-build, model-comparison, claude-code

> Hands-on review of Claude Opus 4.7: better coding and UI, but a new tokenizer and higher default effort can burn up to 35% more tokens. Tested via single-prompt cafe site and finance dashboard builds against Opus 4.6, Gemini 3.1 and GPT 5.4.

## Summary
The host reviews Claude Opus 4.7 as it ships with Claude Code, starting with the release notes: the price is unchanged, but a new tokenizer can make the same prompt cost up to 35% more tokens, and the model thinks more at higher effort levels. He cites benchmark gains (about 10% on SWE-bench Pro and 7% on Verified) with a small cybersecurity regression he attributes to new safeguards, and flags a long-context needle-in-a-haystack regression in the system card. He also notes stricter, more literal instruction following, 3x higher image resolution, better file-system memory, and a new xhigh effort level that is the Claude Code default. For a UI test he gave each model one prompt for a cafe index.html; he ranks Gemini 3.1 first, Opus 4.7 slightly ahead of 4.6, and GPT 5.4 last. For a full personal finance dashboard built from one vague prompt, Opus 4.7 produced the cleaner UI and a mostly working React/Vite app, but used in-memory data with Express and no database; Opus 4.6 used SQLite and persisted data but was plain JavaScript. Gemini 3.1 (Next.js, Prisma) had non-working tabs and GPT 5.4 produced an unusable UI. He concludes that prompt quality matters a lot and that Opus 4.7 may bring him back from Codex. The evidence is anecdotal, one-shot runs with no repeated trials or token counts per model.

## Key ideas
- **Opus 4.7 costs the same per token, but a new tokenizer means the same prompt can use up to 35% more tokens, and the model also thinks more.** — The host says this is the main thing to account for when moving to 4.7. Combined with more thinking at higher effort, usage can climb quickly. ([0:00](https://youtu.be/KZCKfhjMuOQ?t=0))
- **The new xhigh effort level is the Claude Code default and uses roughly the token budget of Opus 4.6 max.** — He says Opus 4.7 high outscores Opus 4.6 max while using fewer tokens. He plans to default to high and recommends testing effort levels to see if a downgrade goes unnoticed. ([2:12](https://youtu.be/KZCKfhjMuOQ?t=132))
- **Benchmarks improved, but the system card shows a long-context regression.** — SWE-bench Pro is up about 10% and Verified about 7% over 4.6. Cybersecurity slipped slightly, which he links to new safeguards. He points to a needle-in-a-haystack result in the system card that looks worse than 4.6, and says he wants to see how this affects real use. ([1:06](https://youtu.be/KZCKfhjMuOQ?t=66))
- **Opus 4.7 follows instructions more literally, so prompts written for older models may now behave differently.** — Older models interpreted instructions loosely or skipped parts. 4.7 takes them literally, so existing prompts may need retuning. ([1:06](https://youtu.be/KZCKfhjMuOQ?t=66))
- **Vision and memory improved: images up to 3x the resolution, and better use of file-system memory across multi-session work.** — Higher-resolution images should help computer use and data extraction. Better file-based memory should mean less upfront context per new task, which could save tokens. ([2:12](https://youtu.be/KZCKfhjMuOQ?t=132))
- **On a simple cafe website prompt, Gemini 3.1 looked best, Opus 4.7 was slightly better than 4.6, and GPT 5.4 looked the most generic.** — Each model got one prompt for index.html at max effort. The host's judgment is subjective and based on a single run per model. ([3:32](https://youtu.be/KZCKfhjMuOQ?t=212))
- **On a complex app built from one vague prompt, Opus 4.7 had the best UI and the most working features, but it used in-memory data.** — The finance dashboard was built in about 20 minutes. Opus 4.7 used React, Vite, React Router, Express and TypeScript, with transactions and goals working, but data held in memory and seeded from a script. Opus 4.6 persisted data in SQLite but used JavaScript, React 19 and React Router 7. GPT 5.4 was unusable. Gemini 3.1 (Next.js, Prisma) had non-working tabs. ([4:35](https://youtu.be/KZCKfhjMuOQ?t=275))
- **Prompt quality is a major factor in these results, and the host says he would normally specify the stack exactly.** — He gave a vague stack prompt on purpose. He says Opus 4.7 may bring him back from Codex, which he had been using heavily. ([9:15](https://youtu.be/KZCKfhjMuOQ?t=555))

## Techniques
- **Effort-level sweep before changing defaults** — Run the same task at each effort level (high, xhigh, max) and compare output quality and token use. The host's rule of thumb is to pick the lowest level that matches the old output quality, then default to it. *When:* When adopting a new model whose default effort level is higher than the one you used before, to cut token burn without losing quality.
- **Same-prompt model bake-off** — Send one identical prompt, at the same max effort, to each model (Opus 4.7, Opus 4.6, Gemini 3.1, GPT 5.4). Save each output as index.html or a full project. Compare visuals, feature completeness, and whether the features actually work. *When:* For quick, qualitative comparisons of UI and app-generation quality. Note that results are one-shot and vary a lot with prompt wording.
- **Re-audit old prompts after a model upgrade** — Re-check prompts that worked on older models. Newer models follow instructions literally and may skip behavior that relied on loose interpretation. *When:* Right after switching a harness or agent to a model with stricter instruction following.
- **Check the stack and persistence explicitly in app-generation prompts** — Specify the framework, backend, and database in the prompt. Without them, the model picks its own stack and may skip persistence (in-memory data) or pick JavaScript over TypeScript. *When:* When asking an agent to build a full app from a prompt and needing it to persist data and use a consistent language.

## Numbers
- Same prompt can use up to 35% more tokens on Opus 4.7 (new tokenizer), at unchanged per-token cost ([0:00](https://youtu.be/KZCKfhjMuOQ?t=0))
- SWE-bench Pro improved about 10% over Opus 4.6 ([1:06](https://youtu.be/KZCKfhjMuOQ?t=66))
- SWE-bench Verified improved about 7% over Opus 4.6 ([1:06](https://youtu.be/KZCKfhjMuOQ?t=66))
- Image input resolution is 3x that of older models ([2:12](https://youtu.be/KZCKfhjMuOQ?t=132))
- Opus 4.6 max effort uses about the same tokens as Opus 4.7 xhigh; Opus 4.7 high outscores 4.6 max with fewer tokens ([2:12](https://youtu.be/KZCKfhjMuOQ?t=132))
- Finance dashboard generated from one prompt in about 20 minutes (Opus 4.7) ([4:35](https://youtu.be/KZCKfhjMuOQ?t=275))

## Hot takes
- Opus 4.7's default xhigh effort burns tokens, so most users should downgrade to high.
- Gemini 3.1 gave the best cafe website, but its finance app had non-working tabs.
- GPT 5.4's UI looks generic, like every other GPT app.
- Opus 4.7 may bring the host back from Codex because of its UI and how much of the app worked.
- Quality of results depends heavily on how vague the prompt was, so the comparison is not fully fair.
- Opus 4.7's long-context regression in the system card could matter more than the benchmark gains suggest.

## Tools mentioned
Claude Opus 4.7, Claude Opus 4.6, Claude Code, Gemini 3.1, GPT 5.4, Codex, Mythos (unreleased Anthropic model, mentioned only), Design Arena, Unsplash, React, Vite, React Router, React Router 7, react-router-dom 7, React 19, React 18, React Router 6, Express, SQLite, TypeScript, JavaScript, Next.js, Prisma, Drizzle, TanStack, Bun, Hono

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code, so the default effort level and the instruction-following change directly affect long-run token burn and prompt behavior. → *Expose effort level as a per-run setting in ProsHarness, then compare high vs xhigh on a saved set of tasks by token use and output quality before choosing a default.*
- **agentos** (1/3): Tokenizer changes can make the same prompt cost up to 35% more under unchanged pricing, which matters for budget enforcement and cost reporting at the proxy.

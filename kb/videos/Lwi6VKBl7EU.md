# GitHub Spark Is INSANE – A Full App in Just 20 Minutes!

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `Lwi6VKBl7EU` · [watch](https://youtu.be/Lwi6VKBl7EU) · **date:** 2025-11-02 · **length:** 6:32 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Andres · **orgs:** GitHub, Microsoft, Amazon, Anthropic, Better Stack
- **topics:** vibe-coding-app-building, coding-agents, product-ux · **tags:** github-spark, vibe-coding, app-generation, react, typescript, tailwind-css, key-value-storage, api-keys, responsive-design, copilot-pro-plus, prototyping

> A Better Stack walkthrough of GitHub Spark, a browser-based vibe-coding platform, building a movie-rating app from one prompt in about 4 minutes, with the caveats that it is React/TypeScript-only, needed a manual API key, and was not responsive.

## Summary
The creator builds a movie search and rating app from a single natural-language prompt in GitHub Spark, a browser-based tool for prototyping and deploying apps. Generation took about four minutes and produced a clickable React and TypeScript app with Tailwind styling, search, anonymous reviews and star ratings, and an in-app LLM recommendation feature. Some images were missing or hallucinated, and the Inception poster was wrong. When asked to add real movie data, Spark reasoned that it needed a TMDB API key, could not get one, and generated fallback data instead; it only worked after the creator supplied a key and went through several back-and-forths. Spark's built-in key-value storage holds the reviews, and the creator notes that moving to another data layer would need manual work. The app was not responsive out of the box, despite a mobile view button. The creator's verdict is that Spark is impressive for quick React prototypes but technically limited and opinionated about its stack, and that it is currently available only to Copilot Pro Plus subscribers. This is one anecdotal demo with no benchmarks, so treat the claims as first-impression evidence.

## Key ideas
- **Spark is positioned as an all-in-one browser platform covering prompt-to-deploy: natural-language editor, hosted runtime, persistent storage, theme editor, LLM hookup and a PWA dashboard.** — The creator says no code editor or local setup is needed. The platform is described as powered by Claude Sonnet 4. ([0:00](https://youtu.be/Lwi6VKBl7EU?t=0))
- **A single detailed prompt produced a working, mostly interactive React and TypeScript app in about four minutes.** — Spark is currently limited to React and TypeScript. Its build progress is streamed as status messages during generation. ([1:12](https://youtu.be/Lwi6VKBl7EU?t=72))
- **The generated app mostly worked but had visual errors: missing images, a wrong poster, and images that failed to load or were hallucinated.** — Search, anonymous reviews and star ratings were functional. Images came from Unsplash, which the creator says is unreliable. ([2:25](https://youtu.be/Lwi6VKBl7EU?t=145))
- **Spark's iteration loop runs in the background, so the app stays usable while the next change is generated. Theme and font changes apply live.** — The suggestion panel offers follow-up features. The creator used the dashboard during an AI iteration. ([2:25](https://youtu.be/Lwi6VKBl7EU?t=145))
- **When a feature needs an external API key that is missing, Spark does not stop to ask. It reasons its way to fallback or fabricated data instead.** — Spark chose TMDB, reasoned that a key was needed, and generated fallback data. Real data required the creator to supply a key and several rounds of correction. ([3:20](https://youtu.be/Lwi6VKBl7EU?t=200))
- **Data goes into Spark's own key-value store, which is convenient for prototypes but creates lock-in if you later need a different backend.** — The creator expects manual rework to migrate. Submitted reviews are visible in a data tab. ([4:42](https://youtu.be/Lwi6VKBl7EU?t=282))
- **The 'mobile view' button does not guarantee a responsive layout; the creator found the app not responsive and expected a follow-up prompt to fix it.** — This is the creator's only observed failure of an implicit expectation. It was not tested further. ([4:42](https://youtu.be/Lwi6VKBl7EU?t=282))

## Techniques
- **Front-load the full feature list in one prompt** — Describe concrete behaviours in the first prompt: what anyone can do on each tab, the review and rating rules, and any AI feature wanted. The creator says Spark then built the whole app in one pass. *When:* Starting a new prototype in Spark or a similar prompt-to-app tool, where a precise spec gives a better first draft.
- **Supply the missing credential the builder asks for, and verify it** — When the agent reasons that it needs an external API key, provide the key in the chat. Expect several correction rounds before the real data flows, and check the generated fetch code and output. *When:* A feature depends on a third-party API. Do not accept fallback or mock data without noticing it.
- **Iterate through the suggestion panel while using the app** — Accept a suggested feature from the panel. The app stays usable while the AI generates the next iteration, and visual changes like theme and fonts apply live. *When:* Using a hosted builder where each generation takes minutes and you want to keep testing.
- **Tune the in-app LLM through the prompts tab** — Spark exposes the prompt used by its LLM-backed feature in a prompts tab, so it can be edited directly. Stored user data is visible in a data tab. *When:* The app has an AI feature whose behaviour needs adjusting without regenerating the app.
- **Check responsiveness explicitly** — Do not rely on a mobile preview toggle. Test the layout at phone width and ask for a responsive fix in a follow-up prompt if needed. *When:* Reviewing any generated web UI before treating it as done.

## Numbers
- Full app generation from one prompt took about four minutes. ([1:12](https://youtu.be/Lwi6VKBl7EU?t=72))
- Creator's total time from start to working app was 'just under 20 minutes' (title says 20). ([4:42](https://youtu.be/Lwi6VKBl7EU?t=282))
- Spark is available only to Copilot Pro Plus subscribers at the time of the video. ([4:42](https://youtu.be/Lwi6VKBl7EU?t=282))
- Video length is 6:32, based on one demo app. ([0:00](https://youtu.be/Lwi6VKBl7EU?t=0))

## Hot takes
- Spark is 'absolutely insane' for quick React prototypes, but the creator says it is technically limited and opinionated about one stack.
- The creator's demo suggests Spark silently invents fallback data when an API key is missing, which can pass as working output.
- The mobile view button does not mean the app is responsive.
- Title hype ('INSANE', 'full app in 20 minutes') is ahead of the evidence, which is one anecdotal demo.

## Tools mentioned
GitHub Spark, Claude Sonnet 4, Kiro (Amazon IDE, mentioned only), React, TypeScript, Tailwind CSS, TMDB movie API, Unsplash, GitHub Copilot Pro Plus

## Relevance to our work
- **prosharness** (1/3): Shows a coding agent that silently falls back to fabricated data when a credential is missing. That is the kind of failure a harness with zero-token credential handling should surface, not hide. → *In ProsHarness credential handling, make missing API keys hard-fail with an explicit approval or prompt, and never let the agent substitute fallback or mock data without a visible flag.*

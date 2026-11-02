# ChatGPT Search Just Launched! Say Goodbye to Google?

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `f57EGI35bwI` · [watch](https://youtu.be/f57EGI35bwI) · **date:** 2025-11-02 · **length:** 4:18 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** OpenAI, Google, Perplexity
- **topics:** rag-retrieval, product-ux · **tags:** chatgpt, web-search, search-engine, browser-extension, source-citations

> Short AI LABS walkthrough of ChatGPT's web search for Plus users, with cited sources, live stock and flight queries, and a Chrome extension that routes browser searches to ChatGPT.

## Summary
The host demonstrates ChatGPT's web search feature, available from the web button for Plus-plan users. Answers are built from multiple web sources, each paragraph carries a source reference, and the sources link out to the originals. The host tests a weather query, a GameStop stock query (showing price changes over day, month and year), and a flight search with booking links. A prompt then offers a Chrome extension that makes ChatGPT the browser's default search, and a local query ("best coffee shops near me") returns results with a map. The video is a feature tour with no benchmarks, accuracy checks or failure cases. The closing comparison notes that ChatGPT still trails Google in monthly visitors, which is shown on screen without figures.

## Key ideas
- **ChatGPT web search is available from the web button for Plus-plan users and offers suggested queries as you type.** — The feature is presented as a Google-style search inside ChatGPT, with a set of suggestions shown before the search runs. ([0:00](https://youtu.be/f57EGI35bwI?t=0))
- **Answers are built from several web sources and each paragraph carries its own source reference.** — Clicking a source opens the original page, so the answer can be checked against the site it came from. ([0:00](https://youtu.be/f57EGI35bwI?t=0))
- **Live-data queries return current results, and the host reads this as evidence the answers are up to date.** — A current-weather query was used to show freshness. This is a single demo, not a systematic test. ([0:00](https://youtu.be/f57EGI35bwI?t=0))
- **Stock and flight queries return structured widgets with sources and booking links.** — The GameStop query shows price changes across day, month and year. The flight query lists results with sources and a path to book. ([1:27](https://youtu.be/f57EGI35bwI?t=87))
- **ChatGPT offers a Chrome extension that makes it the default search from the browser address bar.** — The host installed it from the Chrome Web Store after a prompt appeared during a search. A local query returned results with a map. ([2:52](https://youtu.be/f57EGI35bwI?t=172))
- **The host frames the release as a move toward an all-in-one assistant that competes with Google and Perplexity.** — This is the speaker's interpretation. The only evidence is a visitor-count comparison shown on screen with no figures quoted. ([3:59](https://youtu.be/f57EGI35bwI?t=239))

## Techniques
- **Run a cited web search in ChatGPT** — Use a Plus account, click the web button in the composer, pick one of the suggested queries or type your own, then check the per-paragraph source references and open the linked sites to verify claims. *When:* Quick factual or live-data lookups (weather, prices, flights) where you want a sourced answer and a way to verify it.
- **Make ChatGPT the browser's default search** — When the prompt appears during a search, follow it to the Chrome Web Store, add the extension, then type queries in the address bar. *When:* If you want address-bar searches to go to ChatGPT instead of Google. The video shows the flow but not the extension's permissions or settings.

## Hot takes
- The host says ChatGPT is trying to replace Google, but the same segment concedes that Google remains the most-used website.
- The video is a demo with no accuracy, latency or failure cases, so 'replaces Google' is unsupported by anything tested.
- The extension prompt is presented as a helpful feature, but it is an upsell to make ChatGPT the default search.

## Tools mentioned
ChatGPT, ChatGPT web search, Google Search, Perplexity, Google Chrome, Chrome Web Store

## Relevance to our work
- **agentos** (1/3): Per-paragraph source attribution in generated answers is a provenance pattern that relates to MemoryMesh's retrieval provenance, but the video shows only the consumer UI. → *Compare per-paragraph source attribution with MemoryMesh provenance fields when designing answer citations.*

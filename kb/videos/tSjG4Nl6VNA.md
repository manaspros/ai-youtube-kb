# We Need to Talk About Gemini...

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `tSjG4Nl6VNA` · [watch](https://youtu.be/tSjG4Nl6VNA) · **date:** 2026-09-02 · **length:** 7:40 · **format:** news · **quality:** 3/5 · **depth:** intro
- **speakers:** Unnamed host of the Kai Explains channel · **orgs:** Google, Google DeepMind, Anthropic, OpenAI, Moonshot AI, Apple, Bloomberg, Artificial Analysis, character.ai
- **topics:** models-research, product-ux · **tags:** gemini, google-deepmind, model-release-delays, benchmarks, artificial-analysis, talent-moves, tool-calling, distribution, pricing, opinion

> Commentary on how Google fell from the top of the model rankings in 2026: a delayed Gemini 3.5 Pro, senior researcher departures, and a pace problem that distribution cannot fix.

## Summary
The host argues that Google's lead in frontier models slipped between February and August 2026 because of shipping pace, not because of its distribution or user base, which are still growing. He lays out a timeline: Gemini 3.1 Pro topped the Artificial Analysis Intelligence Index in February, then Gemini 3.5 Pro was announced at I/O on May 19 and missed several self-set availability windows. Reported reasons are an internal quality bar miss on hallucinations and reliability, and a rebuild of the base architecture after failures in recursive tool calling and SVG generation. Google shipped only efficiency-tier models on July 21, and its best-ranked model by August was Gemini 3.6 Flash at 11th. He then lists four senior departures to Anthropic and elsewhere in late June, but argues that the departures are not the cause of the delay. He closes by saying the signal to watch is whether Gemini 3.5 Pro ships or Google moves straight to Gemini 4. Most of the evidence is press reporting and one index; the analysis is interpretive.

## Key ideas
- **Google's best model in the Artificial Analysis Intelligence Index had fallen to 11th by August. Gemini 3.1 Pro had been on top in February, trained mostly on Google TPUs.** — The host frames the decline as a pace problem. Google's user and revenue numbers are rising at the same time. ([0:00](https://youtu.be/tSjG4Nl6VNA?t=0))
- **Gemini 3.5 Pro missed three consecutive availability windows after it was announced at I/O on May 19.** — Pichai reportedly said it was already running internally and asked for a month. General availability slipped to July, and a reported internal July 17 target also passed. ([1:25](https://youtu.be/tSjG4Nl6VNA?t=85))
- **The reported cause of the delay is technical, not a talent story. DeepMind missed its own quality bar on hallucinations and real-world reliability, and reportedly rebuilt the base architecture.** — The rebuild followed structural failures in recursive tool calling and SVG generation. The host argues that reliable tool calling is central to agents. ([1:25](https://youtu.be/tSjG4Nl6VNA?t=85))
- **On July 21 Google shipped Gemini 3.6 Flash, 3.5 Flashlight and a security-focused Flash Cyber model, but no flagship. Logan Kilpatrick said 3.5 Pro is still in partner testing and that a Gemini 4 pre-training run has started.** — The host reads the Gemini 4 comment as a sign that Google may be moving past 3.5 Pro. ([2:50](https://youtu.be/tSjG4Nl6VNA?t=170))
- **In the same period Anthropic shipped four models in under two months, and Opus 5 took the top index spot at 61. OpenAI's GPT 5.6 Sol scored 59. Kimi K3 at 57 matched Gemini 3.1 Pro's February peak.** — The host says Google is now the only major frontier lab without a current flagship publicly available. ([2:50](https://youtu.be/tSjG4Nl6VNA?t=170))
- **Four senior researchers left in late June: Noam Shazeer, John Jumper, Jonas Adler and Alexander Pritzel. Several of them went to Anthropic.** — The host says Bloomberg described the departures as a risk to Google's AI position. He notes Shazeer had been rehired in 2024 to work on Gemini. ([4:07](https://youtu.be/tSjG4Nl6VNA?t=247))
- **The host argues that the 'people left, so the model slipped' story is not supported. Senior people are more likely to leave a project that is already struggling, so the causation may run the other way.** — The departures are better read as a sign of a talent market moving toward Anthropic and OpenAI. ([4:07](https://youtu.be/tSjG4Nl6VNA?t=247))
- **Distribution is Google's strength: the Gemini app passed 900M MAU by May, Google's share of AI web traffic rose to about 27%, and Apple picked a custom Gemini model for Siri.** — The host argues that owning the default surfaces makes a company less urgent about shipping. Developers, meanwhile, choose the fastest model available and build on it. ([5:33](https://youtu.be/tSjG4Nl6VNA?t=333))
- **The host's closing thesis is that Google's problem is pace, not relevance. The test is whether Gemini 3.5 Pro ships. If it does, the February-to-July gap was a delay. If Google skips it, that means 3.5 Pro was not going to close the gap by itself.** — Switching costs favour early movers, so each month of delay compounds. ([6:45](https://youtu.be/tSjG4Nl6VNA?t=405))

## Techniques
- **Read a lab's roadmap by what actually ships** — Track each date a lab publicly promised for a flagship against what shipped. A promised model that slips, then is quietly superseded by the next generation (for example 3.5 Pro followed by Gemini 4 talk), is a stronger signal than the announcement. Watch for shipping of efficiency-tier models in place of the flagship. *When:* Deciding how much to bet on one vendor's next model, or deciding whether to wire a product to a model that is still in preview.
- **Use an aggregate index as a rough prior, then check the rank over time** — The host uses the Artificial Analysis Intelligence Index as the yardstick. Compare a lab's best model by rank at several dates, not a single snapshot, and compare it with the best score from other labs (Opus 5 at 61, GPT 5.6 Sol at 59, Kimi K3 at 57, Gemini 3.1 Pro's peak at 57). *When:* Quick model selection or a sanity check on a lab's trajectory. It is not a substitute for testing on your own workload.

## Numbers
- Gemini 3.1 Pro topped the Artificial Analysis Intelligence Index in February 2026, trained mostly on Google TPUs. Gemini 3.6 Flash, Google's highest-ranked model by August, placed 11th. ([0:00](https://youtu.be/tSjG4Nl6VNA?t=0))
- Index scores cited: Opus 5 at 61 (top), GPT 5.6 Sol at 59, Kimi K3 at 57 (equal to Gemini 3.1 Pro's February peak). ([2:50](https://youtu.be/tSjG4Nl6VNA?t=170))
- Gemini 3.5 Pro was announced May 19, then missed three consecutive availability windows, with general availability pushed to July. A reported internal target of July 17 also passed. ([1:25](https://youtu.be/tSjG4Nl6VNA?t=85))
- Gemini 3.6 Flash pricing: $1.50 per million input tokens and $7.50 per million output tokens. ([5:33](https://youtu.be/tSjG4Nl6VNA?t=333))
- Gemini app passed 900M monthly active users by May, up from 400M a year earlier. ([4:07](https://youtu.be/tSjG4Nl6VNA?t=247))
- Google's share of global AI web traffic roughly tripled in 12 months to about 27%, second only to ChatGPT. ([5:33](https://youtu.be/tSjG4Nl6VNA?t=333))
- AI Overviews reached more than 2B monthly users, and AI Mode more than 1B. ([5:33](https://youtu.be/tSjG4Nl6VNA?t=333))
- Apple chose a custom 1.2 trillion parameter Gemini model for the rebuilt Siri, in a deal reported at around $1B per year, shipping with iOS 27. ([5:33](https://youtu.be/tSjG4Nl6VNA?t=333))

## Hot takes
- The 'departures caused the delay' story is unsupported. The host argues people leave projects that are already struggling, so the causation may run the other way.
- Google's problem is pace, not relevance. Owning default surfaces such as Search, Chrome, Android and Siri makes a company less urgent about shipping flagships.
- Developers pick the fastest available engine and build on it, so each month of delay compounds into switching costs.
- The delay evidence is largely press reporting with anonymous sources ('reportedly', 'widely reported'), and the ranking evidence rests on one index. The host says this himself, but the claims are still unverified.
- Google is the only major frontier lab without a current-generation flagship publicly available. This is the host's framing and the cited ranks support it only in part.

## Tools mentioned
Gemini 3.1 Pro, Gemini 3.5 Pro, Gemini 3.5 Flash, Gemini 3.6 Flash, Gemini 3.5 Flashlight, Flash Cyber, Gemini 4, Artificial Analysis Intelligence Index, Google TPU, Claude Mythos 5, Claude Fable 5, Claude Sonnet 5, Claude Opus 5, GPT 5.6 Sol, GPT 5.6 Terra, GPT 5.6 Luna, Kimi K3, Gemini app, Google AI Overviews, Google AI Mode, Siri (iOS 27), AlphaFold, character.ai

## Relevance to our work
- **agentos** (1/3): The point that nested tool calling is the main agent-reliability failure is relevant to a multi-provider proxy that routes between upstream models, but the video says nothing about implementation. → *Add a nested tool-call reliability case (a tool that calls another tool) to the AgentOS routing evals before choosing an upstream model for an agent path.*

# You Won’t Believe What Google Gemini 2.0 Can Do Now!  - #gemini2flash #aistudio

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `teEp3I83k-w` · [watch](https://youtu.be/teEp3I83k-w) · **date:** 2025-11-02 · **length:** 9:16 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed AI LABS host · **orgs:** Google, Adobe, Microsoft, OpenRouter
- **topics:** voice-multimodal, models-research, sandboxing-execution · **tags:** gemini-2.0-flash, google-ai-studio, multimodal-live-api, real-time-vision, code-execution, grounding, benchmarks, openrouter

> Walkthrough of Gemini 2.0 Flash's real-time webcam and screen-share mode in Google AI Studio, with a list of claimed benchmark scores and quick tests of its tools. Mostly a demo with light substance.

## Summary
The host shows Gemini 2.0 Flash's Multimodal Live (Stream Real-Time) mode in Google AI Studio answering questions about a webcam feed and a shared screen, including step-by-step help in Microsoft Word and Adobe Premiere Pro. He then reads a list of benchmark scores for 2.0 Flash across code, SQL, math, reasoning, image understanding and factuality, without showing comparison baselines. Next he runs his own spot tests: a letter-count question, an SVG butterfly, and a prime-number script. He tries the built-in tools, where code execution runs automatically with no manual run step, and Google Search grounding, which returned no links twice before working on the third try. He closes by pointing to free AI Studio access and an API key, with OpenRouter as an alternative. The title and narration are hype-heavy, and most claims are relayed from a slide or from what he has read rather than verified.

## Key ideas
- **Real-time multimodal streaming: the model answers questions about a live webcam feed and a shared screen, and gives UI steps for Word (Insert > Shapes > Scribble) and Premiere Pro (add Gaussian Blur from the Effects panel). The Premiere answer was confirmed correct on screen.** — This is the headline feature shown in AI Studio's Stream Real-Time mode. The demos are scripted and short, so reliability over longer sessions is not tested. ([0:00](https://youtu.be/teEp3I83k-w?t=0))
- **Narrator says 2.0 Flash far surpasses Gemini 1.5 Pro and adds native video analysis, image generation and audio generation. These are claims, not measured in the video.** — Only the screen-share and webcam features are demonstrated. Image and audio generation are mentioned but not shown. ([1:10](https://youtu.be/teEp3I83k-w?t=70))
- **Benchmark numbers for 2.0 Flash are read from a slide with no comparison baseline shown. Code and SQL scores are given first, then math, reasoning and image scores.** — Code: Natural2Code 92.9, BIRD-SQL 56.9, LiveCodeBench 35.1. Math: MATH 89.7, hidden math 63.0. Reasoning: GPQA 62.1. Image: MMMU 70.7, a second vision benchmark 56.3. Factuality: FACTS grounding 83.6. ([2:37](https://youtu.be/teEp3I83k-w?t=157))
- **AI Studio is free to try, and 2.0 Flash had no published price at the time. The narrator expects it to match 1.5 Flash's pricing, which he calls good news for existing users.** — This is an expectation based on what he read, not a confirmed price. ([4:59](https://youtu.be/teEp3I83k-w?t=299))
- **Quick spot tests: the model correctly counted three r's in 'strawberry' (61 tokens). For the SVG butterfly it first gave a small result, and a follow-up asking for a larger, more realistic version improved it.** — Tests are anecdotal, with one run per prompt and no repeated sampling. ([4:59](https://youtu.be/teEp3I83k-w?t=299))
- **Code execution runs generated Python automatically in a sandbox, with no manual run button. It printed a list of primes and showed example output.** — The sandbox behavior is visible in the UI, but the video does not show its isolation or limits. ([6:47](https://youtu.be/teEp3I83k-w?t=407))
- **Google Search grounding showed no links on the first two attempts. On the third attempt it returned results with links. The host calls the feature experimental and says the earlier failure was a glitch.** — Practical lesson from the demo: re-prompt once if the sources are missing before deciding the feature is broken. ([6:47](https://youtu.be/teEp3I83k-w?t=407))
- **The API key comes from a link in AI Studio. The narrator says the API is free within rate limits, citing what he read, and mentions OpenRouter as a second route to 2.0 Flash.** — Pricing and rate-limit claims are second-hand and were not checked on screen. ([8:14](https://youtu.be/teEp3I83k-w?t=494))

## Techniques
- **Live screen and webcam Q&A for unfamiliar software** — In Google AI Studio, open 'Stream Real-Time' in the left sidebar and select the Gemini 2.0 Flash model. Turn on webcam or screen share, then ask task-specific questions such as 'I want to add a blur to this clip, how?' and check the instructions against the real UI before acting. *When:* Use for walking through an unfamiliar app's UI or checking your own screen step by step. Verify each step, because the demo shows only short, scripted sessions.
- **Show token counts and temperature in AI Studio** — The AI Studio prompt settings expose token count and temperature. The narrator adds a counter at the top of the page to track token use across prompts. *When:* Use when comparing response length and cost across prompts or models during quick manual testing.
- **Small smoke-test battery for a new model** — Run a fixed set of short prompts each time: a letter count ('how many r's in strawberry'), an SVG drawing ('butterfly'), then a follow-up asking for a bigger, more realistic version, and a code-execution prime-number script. Record the token count for each. *When:* Use as a fast first check that a new model handles common failure cases. It is anecdotal and does not replace a real eval set.
- **Re-prompt once when grounding returns no sources** — Turn on the grounding tool in AI Studio's Tools panel and ask a factual question. If no links come back, ask again. The narrator saw the links appear on the third attempt. *When:* Use when a cited web answer is needed while the feature is still experimental. Check the cited links yourself.
- **Get API access from AI Studio or OpenRouter** — Click the get-API-key link in AI Studio to generate a key. The narrator also mentions using an OpenRouter key to call the model. *When:* Use when moving from the AI Studio UI to code. Check the current free tier and rate limits, since the narrator relays these from reading, not from the console.

## Numbers
- Natural2Code score 92.9 for 2.0 Flash (auto-caption: 'natural two code'), described as outperforming previous versions ([2:37](https://youtu.be/teEp3I83k-w?t=157))
- BIRD-SQL score 56.9 ([2:37](https://youtu.be/teEp3I83k-w?t=157))
- LiveCodeBench score 35.1 ([3:36](https://youtu.be/teEp3I83k-w?t=216))
- MATH score 89.7 ([3:36](https://youtu.be/teEp3I83k-w?t=216))
- Competition-level hidden math score 63.0 ([3:36](https://youtu.be/teEp3I83k-w?t=216))
- GPQA score 62.1 (expert-level biology, physics and chemistry questions) ([3:36](https://youtu.be/teEp3I83k-w?t=216))
- MMMU score 70.7% ([3:36](https://youtu.be/teEp3I83k-w?t=216))
- Second vision benchmark score 56.3% (auto-caption: 'VibeVal') ([3:36](https://youtu.be/teEp3I83k-w?t=216))
- FACTS grounding accuracy 83.6% ([3:36](https://youtu.be/teEp3I83k-w?t=216))
- The strawberry letter-count answer used 61 tokens ([4:59](https://youtu.be/teEp3I83k-w?t=299))
- Gemini 2.0 Flash had no published price at the time; the narrator expects it to match 1.5 Flash ([4:59](https://youtu.be/teEp3I83k-w?t=299))

## Hot takes
- Hype title and narration ('You Won't Believe', 'absolutely insane') sit on top of a thin, mostly scripted demo; the video is more product tour than analysis.
- The benchmark list is read from a slide with no baseline or comparison models shown, so the claims of beating prior versions are unverified here.
- Grounding failed twice before working, which undercuts the demo's claim that the feature is ready for everyday use even though the host notes it is experimental.
- Pricing and free-tier claims are second-hand ('from what I've read'); they should be checked against the current console before relying on them.

## Tools mentioned
Gemini 2.0 Flash, Gemini 1.5 Flash, Gemini 1.5 Pro, Google AI Studio, Gemini Multimodal Live API (Stream Real-Time), Google Search grounding, Gemini code execution, Microsoft Word, Adobe Premiere Pro, OpenRouter

## Relevance to our work
- **agentos** (1/3): Gemini's built-in code execution (auto-run in a sandbox with no manual step) and Stream Real-Time are relevant as comparison points for Crucible's opt-in sandboxed execution and the multimodal path, but the video gives no architecture detail. → *Low priority: compare Gemini's auto-executing sandbox (no manual run step) with Crucible's opt-in exec gate when designing the code-execution guardrails. Do not act on the benchmark numbers without a source.*

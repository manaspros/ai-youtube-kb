# Gemini 2.0 Tested: Google's New Models Are No Joke!

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `XcQhApQVPCY` · [watch](https://youtu.be/XcQhApQVPCY) · **date:** 2025-11-02 · **length:** 11:16 · **format:** review · **quality:** 2/5 · **depth:** practitioner
- **speakers:** Unnamed AI LABS host · **orgs:** Google, Nvidia, Artificial Analysis, OpenAI, DeepSeek
- **topics:** models-research, evals, token-cost-efficiency · **tags:** gemini-2-0, gemini-flash-lite, model-comparison, latency, hands-on-test, svg-generation, pygame, cheap-models, reasoning-puzzles

> AI LABS runs a hands-on test of Gemini 2.0 Flash, Flash-Lite ("Flashlight") and Pro on 10 quick prompts: Flash-Lite is fastest and cheapest, but coding and reasoning results are mixed.

## Summary
The host tests three Gemini 2.0 models (Flash, Flash-Lite, and the experimental Pro) on ten prompts covering facts, rhyme, a constrained haiku, trick logic, word puzzles, math, SVG generation, a 3D cube in web code, and a pygame animation. Each prompt is run once per model, with response time noted and a manual pass/fail call. Before the tests, the host leans on Artificial Analysis quality-vs-price and speed charts to argue that Flash and Flash-Lite beat several rivals on quality per dollar. On the tests, Flash-Lite is consistently fastest and passes most reasoning prompts, and it is the only model that passes the pygame animation. Pro wins the SVG butterfly, and Flash and Pro handle the cube. Every model fails the haiku and the adjective puzzle. The host closes by recommending Flash-Lite as a starting point for building apps, mainly on speed and price. The sample is small (one run per prompt), the cost figures are not quoted, and the title is hype-heavy, so the video is better as a sense of the models' speed than as evidence of their accuracy.

## Key ideas
- **Gemini 2.0 Flash is now generally available (it was experimental before), a new Flash-Lite model is released, and Gemini 2.0 Pro is still experimental with no official pricing.** — The host frames the release as fast and cheap, and says the test will check whether the speed is worth it on reasoning and coding prompts. ([0:00](https://youtu.be/XcQhApQVPCY?t=0))
- **Speed and cost gains are attributed to Google possibly moving from Nvidia GPUs to its Trillium TPUs. The host presents this as a guess, not a confirmed fact.** — The host says the TPU shift 'might have' happened and treats it as the reason the models are fast and cheap. No source is cited for it. ([1:00](https://youtu.be/XcQhApQVPCY?t=60))
- **Artificial Analysis quality-vs-price and speed charts are used to argue that Flash and Flash-Lite beat rivals on quality per dollar.** — Per the host's reading, Flash beats GPT-4 mini and even GPT-4o and Claude 3.5 Sonnet on quality at a lower price, while o3-mini stays the raw-speed leader but costs more. The host reads these charts aloud and gives no numbers. ([1:00](https://youtu.be/XcQhApQVPCY?t=60))
- **Flash-Lite is pitched as the cheapest option, cheaper than DeepSeek R1, which previously held that spot.** — The host says Flash-Lite's price is far below GPT-4o and o1, and it is the main reason given for recommending it. The transcript does not quote any dollar prices. ([2:09](https://youtu.be/XcQhApQVPCY?t=129))
- **All three models pass the simple factual prompts and a trick logic question, and Flash-Lite is the fastest on each.** — Factual prompts are naming a country ending in 'stan' with its capital, and a rhyming number. The trick is the oranges question, where the expected answer is two oranges left, and all three models give it. ([2:09](https://youtu.be/XcQhApQVPCY?t=129))
- **A constrained-writing prompt (a haiku whose second letters spell a word) fails on all three models, and Flash-Lite hits a hate/harassment refusal on it.** — Pro and Flash spell the word using first letters or otherwise break the constraint. The refusal is unexplained by the host. ([3:35](https://youtu.be/XcQhApQVPCY?t=215))
- **On a multi-condition word puzzle, Flash is close but misses one letter-count condition, and Flash-Lite and Pro both fail it.** — The host marks all three as fails and notes Pro was expected to do better, but it is still experimental. ([4:58](https://youtu.be/XcQhApQVPCY?t=298))
- **SVG butterfly generation is the first clear split: Pro passes with a convincing drawing, while Flash and Flash-Lite fail.** — Pro takes about 20 seconds, Flash about 11 seconds, and Flash-Lite 2.8 seconds. The host calls Pro's output one of the best AI-generated illustrations he has seen, but this is a single run. ([6:23](https://youtu.be/XcQhApQVPCY?t=383))
- **A 3D cube in simple web code: Flash and Pro produce the same good result, and Flash-Lite's cube loses its shape while rotating, so it is not a pass.** — Flash is judged the most efficient here. The host says the Flash cube is not interactive but moves smoothly. A separate model made an interactive version, but the host does not name which. ([7:46](https://youtu.be/XcQhApQVPCY?t=466))
- **Pygame bouncing-ball-in-rotating-square animation: Flash-Lite is the only model whose code runs correctly, while Flash and Pro fail.** — Each model's code is pasted into a Python editor with pygame installed and run. Flash-Lite takes 8 seconds to generate, Flash 12 seconds, and Pro 17 seconds. The host says he did not expect the result. ([9:13](https://youtu.be/XcQhApQVPCY?t=553))
- **Host's takeaway: speed is the real advantage, and Flash-Lite is a reasonable starting model for building AI apps, with coding results mixed.** — The host says that for pygame-style animation, Flash and Pro both failed while Flash-Lite passed, and urges viewers to test the models in their own workflow. ([10:39](https://youtu.be/XcQhApQVPCY?t=639))

## Techniques
- **Fixed prompt suite with per-model latency and pass/fail** — Send the same prompt to each model, time the response, then mark each answer pass or fail. Cover factual recall, constrained writing, trick logic, word puzzles, math, SVG generation, web code, and a runnable animation. The video uses 10 prompts and one run per model. The exact prompt wording is not in the transcript, so a reader would need the source for the question text. *When:* A quick shootout to shortlist a cheap model tier before committing to it in a pipeline.
- **Run generated code before scoring it** — For code output, paste the model's code into a real environment (here a Python editor with pygame installed), run it, and judge the behaviour (bounds, rotation, shape). A plausible-looking answer is not counted as a pass until it runs. *When:* Any coding or visual-output test, such as animation, rendering, or SVG.
- **Trick-question check for reasoning** — Ask a question where the intuitive answer is wrong (the oranges question, where drinking half the juice does not change the orange count), and see whether the model avoids the common mistake. *When:* Testing whether a model reasons or pattern-matches, using prompts with a known catch.
- **Shortlist with quality-vs-price and speed charts before hands-on tests** — Use a public quality-vs-price quadrant and a speed chart (the host cites Artificial Analysis) to pick candidates, then confirm with your own prompts. *When:* Choosing which models to test when cost matters.

## Numbers
- Country-with-'stan' factual prompt: Flash-Lite responds in 1.3 s; Pro is described as faster, no number given. ([2:09](https://youtu.be/XcQhApQVPCY?t=129))
- Rhyme prompt latency: Flash 1.4 s, Flash-Lite 0.6 s, Pro 0.9 s. ([3:35](https://youtu.be/XcQhApQVPCY?t=215))
- Oranges trick question latency: Flash-Lite 0.9 s, DeepSeek R1 2.0 s, Pro 2.0 s. ([4:58](https://youtu.be/XcQhApQVPCY?t=298))
- Math puzzle (answer 80): Flash 1.6 s, Flash-Lite 1 s, Pro slowest, no number given. ([6:23](https://youtu.be/XcQhApQVPCY?t=383))
- SVG butterfly generation time: Flash about 11 s (fail), Flash-Lite 2.8 s (fail), Pro about 20 s (pass). ([6:23](https://youtu.be/XcQhApQVPCY?t=383))
- 3D cube web code generation time: Flash 11 s (pass), Flash-Lite 5 s (not a pass, shape lost), Pro 16 s (same result as Flash). ([7:46](https://youtu.be/XcQhApQVPCY?t=466))
- Pygame bouncing-ball animation generation time: Flash 12 s (fail), Flash-Lite 8 s (pass), Pro 17 s (fail). ([9:13](https://youtu.be/XcQhApQVPCY?t=553))
- Sample size: 10 prompts, 3 models, one run each (30 model responses in total). ([0:00](https://youtu.be/XcQhApQVPCY?t=0))
- No prices are quoted in the transcript; cost claims are chart-based and only described qualitatively. ([2:09](https://youtu.be/XcQhApQVPCY?t=129))

## Hot takes
- Pro is in experimental status with no official pricing, so the head-to-head is not a deployment decision.
- Pass/fail is the host's own informal judgment. He marks Flash's Tom answer as a pass even though he says it answered the wrong question, and he does not clearly score Pro's cube result.
- Each prompt is run once, so the latency numbers and the one pygame pass for Flash-Lite could flip on a rerun.
- The TPU explanation for the speed and cost is speculation (the host says 'might have'), and the video gives no source for it.
- The title 'No Joke!' and the 'insanely fast' framing are hype, and the cost claim rests on charts the host only reads aloud.

## Tools mentioned
Gemini 2.0 Flash, Gemini 2.0 Flash-Lite (called 'Flashlight' in the video; name is an auto-caption-based guess), Gemini 2.0 Pro (experimental), Trillium TPU (named as Google's new chip, unverified link to the speed gains), Nvidia GPUs, Artificial Analysis (benchmark charts), o3-mini, GPT-4o, GPT-4 mini, o1, DeepSeek R1, Qwen 2.5 Max (auto-caption 'Quen 2.5 Max'), Claude 3.5 Sonnet (spoken as '3.5 sonnet'), Grok models (not named precisely), pygame, Python, SVG, HTML/JS (web cube)

## Relevance to our work
- **agentos** (1/3): Cheap, fast model tiers are relevant to the routing and strategy layer and to cheap-model pipelines, but this is a 10-prompt, one-run test with no cost numbers. → *Run a small fixed prompt suite (latency and pass/fail per model) over our routing candidates, including a Gemini Flash-Lite-class model, and use it to set the cheap tier, not this video's results.*

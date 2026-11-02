# Gemma3n - The Most OVERHYPED AI Model of 2025 (For Coding)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `FCl6ZR8l_EM` · [watch](https://youtu.be/FCl6ZR8l_EM) · **date:** 2025-11-02 · **length:** 4:47 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Better Stack host (unnamed) · **orgs:** Google, Meta, DeepSeek, Ollama, DigitalOcean, Anthropic, Better Stack
- **topics:** local-ai, models-research, coding-agents · **tags:** gemma-3n, llama-4, deepseek-r1, open-weight-models, ollama, model-comparison, single-shot-coding, threejs, sponsored

> Better Stack gives Gemma 3n, Llama 4 and DeepSeek R1 three browser coding prompts. Gemma 3n finishes last, and the speaker concludes open models aren't ready for complex coding.

## Summary
The host tests Google's Gemma 3n against Llama 4 and DeepSeek (R1 on the third task) on three single-file browser coding tasks: a bouncing ball inside a hexagon, a playable snake game, and a rotating ASCII torus. Gemma 3n is run through Ollama, where the speaker notes tool use isn't supported yet, so the tasks are kept simple. Each model gets a few attempts, and the host feeds back errors or console output to get fixes. Llama 4 wins the hexagon round, DeepSeek wins the snake round, and Llama 4 narrowly takes the torus round after Gemma 3n and DeepSeek both fail to produce a working result. Gemma 3n is the worst performer throughout, with the torus attempts producing blank screens and console errors across five tries before the host gives up. The host closes by saying Llama 4 is too heavy for a laptop and that open models are not yet ready for complex coding, unless one specifically trained for code is run on a large multi-machine setup. The video ends with a sponsor segment for Better Stack.

## Key ideas
- **Google's Gemma 3n claim of near-Claude 3.7 ELO is treated skeptically, since the model is aimed at low-power devices.** — The host frames the test as a check of the claim using coding tasks rather than leaderboard scores. The Ollama build of Gemma 3n has no tool-use support at the time, so the tasks avoid tool calls. ([0:00](https://youtu.be/FCl6ZR8l_EM?t=0))
- **Round 1 (bouncing ball in a hexagon) goes to Llama 4, but the results are still shaky.** — Llama 4 gets the hexagon and ball on the first attempt, but the ball clips out of the hexagon every third or fourth bounce on the second attempt. DeepSeek's first attempt also renders but barely moves. Gemma 3n produces a random spinning shape and only the hexagon on its third try. ([1:26](https://youtu.be/FCl6ZR8l_EM?t=86))
- **Round 2 (snake game) goes to DeepSeek, which is one-shot playable and adds a restart button.** — Llama 4's first snake is unplayable and gets fixed on the second attempt. Gemma 3n adds a score and high score, but the game still is not playable after one error fix. ([1:26](https://youtu.be/FCl6ZR8l_EM?t=86))
- **Round 3 (rotating ASCII torus) is where the models fail, and the failures are mostly about environment and language choice.** — Llama 4's Python attempts error or show a blank screen, so the host switches it to JavaScript and gets a rotating shape, not a true torus. DeepSeek R1 uses Three.js without a CDN link or install steps, which causes errors. Gemma 3n gives Python twice, then JavaScript, with blank screens and console errors through five attempts. ([2:56](https://youtu.be/FCl6ZR8l_EM?t=176))
- **Local run cost is the speaker's main caveat: Llama 4 is hard to run even on a laptop.** — The host says Llama 4 needs a large GPU server with lots of RAM, whereas Gemma 3n and DeepSeek R1 are easier to run locally. The speaker's overall conclusion is that open models aren't yet ready for complex coding tasks, unless a code-specialized model is run on a multi-machine setup. ([4:21](https://youtu.be/FCl6ZR8l_EM?t=261))

## Techniques
- **Feed errors back for a fix** — Paste the console error or the observed failure back into the same chat and ask the model to fix it. Llama 4's snake game and Gemma 3n's snake error were both fixed on the second attempt this way. The host also inspects generated code directly when an error shows up. *When:* Debugging a single-file generated web app where the model's first output has a runtime error or a broken interaction.
- **Switch language when a generated graphic does not render** — When a Python-generated visual shows a blank screen or errors, ask the model to rewrite it in JavaScript for the browser. Llama 4's torus went from a Python error and a blank screen to a rotating shape after this switch. *When:* A model's Python output is meant to appear in a browser and it is not rendering. Browser-native JavaScript is the more direct path for this kind of output.
- **Give the model the CDN link for a 3D library** — When the generated page uses Three.js, include the library's CDN URL or install steps in the prompt or the follow-up. The host says DeepSeek R1 would have fixed its torus with just the CDN link, which it did not supply. *When:* A model generates web code that imports a third-party library the page cannot load without an explicit script tag or install step.
- **Same-prompt, multi-attempt model bake-off** — Use the same fixed prompts across models, allow a set number of attempts per model (about 2 to 5 here), and score each round by which model produced a working result first. The host scores round winners by eye, not by a metric. *When:* A quick, hands-on model comparison for a coding task when no benchmark matches your workload. It is anecdotal, so use it to rule models out rather than to rank them.

## Numbers
- Google claims Gemma 3n's ELO score is almost as good as Claude 3.7 (as stated by the host). ([0:00](https://youtu.be/FCl6ZR8l_EM?t=0))
- Llama 4 hexagon round: ball clips out of the hexagon roughly every third or fourth bounce on its second attempt. ([0:00](https://youtu.be/FCl6ZR8l_EM?t=0))
- Test size: 3 models, 3 coding tasks, 2 to 5 attempts per model per task. ([0:00](https://youtu.be/FCl6ZR8l_EM?t=0))
- Gemma 3n torus round: at least five attempts with errors or blank screens before the host gives up. ([2:56](https://youtu.be/FCl6ZR8l_EM?t=176))
- Llama 4 needs a large GPU server with lots of RAM to run (host cites a DigitalOcean GPU server), so it is not practical on a laptop. ([4:21](https://youtu.be/FCl6ZR8l_EM?t=261))

## Hot takes
- Open models are nowhere near ready for complex coding tasks (speaker's conclusion from three single-shot browser prompts, each run a few times).
- Gemma 3n is overhyped: its Claude 3.7 ELO claim does not hold for coding.
- A code-specialized open model run on four or five Mac Studios would be needed for serious coding, which the host says he does not have the budget for.

## Tools mentioned
Gemma 3n, Llama 4, DeepSeek R1, DeepSeek, Ollama, Three.js, Python, JavaScript, Claude 3.7 (comparison reference)

## Relevance to our work
- **agentos** (1/3): AgentOS fronts any model through one proxy and runs vLLM locally, so this shows how small open models stumble on tool-free coding tasks. It is not a result about InferCraft or routing. → *If InferCraft or routing ever sends coding traffic to a local open model, benchmark it with a fixed prompt set and a retry budget before enabling it. Do not rely on one-off coding demos like this one.*

# NEW Qwen 2.5 Coder (32B): Insane Coding Power Tested! Is This the Best Free LLM?

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `4shPVb4RqGQ` · [watch](https://youtu.be/4shPVb4RqGQ) · **date:** 2025-11-02 · **length:** 5:41 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** OpenAI, Hugging Face, Ollama, Cursor
- **topics:** models-research, local-ai, evals · **tags:** qwen, qwen2.5-coder, open-weights, coding-model, ollama, hugging-face, cursor, open-webui, pass-fail-testing, anecdotal-benchmark

> Informal hands-on test of Qwen 2.5 Coder (32B) against five coding prompts via the hosted demo; it passed three and failed two, and the presenter says to test it yourself before switching from Claude.

## Summary
The presenter pitches Qwen 2.5 Coder as a possible replacement for Claude 3.5 Sonnet as the default coding model, quoting benchmark numbers from the intro without showing a source or comparison table. He lists access routes: local runs through Ollama (7B or 32B), the Hugging Face demo with its artifacts panel, Cursor, and Open WebUI. He then runs five prompts in the hosted demo and marks each pass or fail: a function summing multiples of three (pass), a fake-data news-headline app (pass), a customizable-point SVG star (pass), A* shortest-path (fail, a dictionary-related error), and a grid virus-spread simulation (fail, an attribute error). Two of the failures happened while the Hugging Face space was under heavy load, which the presenter partly blames for them. His verdict is that the model scores well overall but falls short of Claude on some tasks, so viewers should test it themselves. The sample is five prompts with no repeats or scoring rubric, so it is anecdotal.

## Key ideas
- **Positioning: Qwen 2.5 Coder is pitched as a possible replacement for Claude 3.5 Sonnet as the go-to coding model, and as beating GPT-4o and Sonnet. These are the presenter's claims, and no comparison is shown on screen.** — The presenter calls it the latest flagship model, although the model tested is the Coder variant. Only the benchmark numbers are given, with no source. ([0:00](https://youtu.be/4shPVb4RqGQ?t=0))
- **Reported benchmark scores: HumanEval 92.7, MBPP 90.2, LiveCodeBench 31.4, and two more the captions render as 'AER' (likely Aider) at 73.7 and 'Spyder' (likely Spider) at 85.1.** — The presenter frames these as showing an open model competing with closed ones. The captions misspell the benchmark names, so the two labels are guesses. ([0:00](https://youtu.be/4shPVb4RqGQ?t=0))
- **Access routes: the model is available through Cursor, Open WebUI with a custom artifact panel, a Hugging Face demo, and local runs via Ollama.** — The presenter says the model was used in Cursor to build a game. He links the Ollama model page, where the 7B and 32B sizes are offered, and the Hugging Face page, which hosts the demo and artifacts. ([0:00](https://youtu.be/4shPVb4RqGQ?t=0))
- **Five-prompt pass/fail test, with each prompt logged in a Notion list: a sum-of-multiples-of-three function (pass), a news-headline app using fake data (pass), an SVG star with customizable points (pass), A* shortest-path (fail), and a grid virus-spread simulation (fail).** — The A* failure is tied to a dictionary the model created. The simulation failure is an object attribute error. The artifact sandbox installed libraries on its own during the runs. ([2:48](https://youtu.be/4shPVb4RqGQ?t=168))
- **The two failures overlap with heavy load on the Hugging Face space. The simulation prompt produced output that was not rendered as code in real time, so the failures are confounded.** — The presenter says the load is a factor and encourages viewers to test it themselves, so the failure rate says more about the demo host than about the model. ([4:09](https://youtu.be/4shPVb4RqGQ?t=249))
- **Verdict: the model scored well overall but fell short of Claude on some key tests. Switching is worth it only if it beats the current model on your own work.** — The presenter's conclusion is a call to test it yourself, with no repeated runs, rubric or a held-out set behind the verdict. ([4:09](https://youtu.be/4shPVb4RqGQ?t=249))

## Techniques
- **Fixed pass/fail prompt set for a quick coder-model smoke test** — Keep a short list of coding prompts that rise in difficulty: a single function, a small interactive UI app with fake data, SVG generation, a classic algorithm (A* pathfinding), and a grid simulation with neighbour-based state changes. Run each one against the candidate model in a fresh chat (the presenter clears history between prompts), mark pass or fail, and record the results in one list to compare models. *When:* Before switching the default coding model or adding a new local model to a pool. It is quick, but five prompts with one run each is not statistically meaningful, so repeat runs and a scoring rubric are needed for a real decision.
- **Trying an open coder model locally with Ollama** — Open the Ollama model page for the model, pick a size (the video shows 7B and 32B), copy the run command from that page, and paste it into the terminal. The exact command is not shown in the transcript. *When:* When you want to test an open-weights coding model on your own hardware instead of the hosted demo.
- **Testing in a hosted artifacts sandbox** — Use the Hugging Face demo with its artifacts panel. Paste the prompt, and the panel shows code beside an editor and preview. The sandbox installs the libraries the code needs on its own. *When:* For a quick check of generated UI or single-file apps without local setup. Hosted demos can be overloaded, so retest a failure before counting it against the model.

## Numbers
- HumanEval 92.7 for Qwen 2.5 Coder (as stated, no source shown) ([0:00](https://youtu.be/4shPVb4RqGQ?t=0))
- MBPP 90.2 ([0:00](https://youtu.be/4shPVb4RqGQ?t=0))
- LiveCodeBench 31.4 ([0:00](https://youtu.be/4shPVb4RqGQ?t=0))
- 'AER' (likely Aider) 73.7, caption-garbled name ([0:00](https://youtu.be/4shPVb4RqGQ?t=0))
- 'Spyder' (likely Spider) 85.1, caption-garbled name ([0:00](https://youtu.be/4shPVb4RqGQ?t=0))
- Available sizes shown: 7B and 32B via Ollama ([1:25](https://youtu.be/4shPVb4RqGQ?t=85))
- Informal test: 5 prompts, 3 pass and 2 fail (A* and grid simulation) ([2:48](https://youtu.be/4shPVb4RqGQ?t=168))

## Hot takes
- The title asks 'Is This the Best Free LLM?', but five anecdotal prompts run once each on an overloaded demo cannot support that claim. The video itself ends with a call to test it yourself.
- The benchmark numbers are read aloud from the intro with no source or comparison table, and the claim that the model beats GPT-4o and Claude 3.5 Sonnet is not shown.
- Two of the three failures happened under visible Hugging Face load, so the failure count is confounded by the host.
- The presenter calls the model the 'latest flagship', but the tested model is the Coder variant. That mixes up the general flagship with the specialised model.

## Tools mentioned
Qwen 2.5 Coder (32B and 7B), Qwen 2.5, Claude 3.5 Sonnet, GPT-4 Omni (GPT-4o), Cursor, Open WebUI, Ollama, Hugging Face (demo space and artifacts), Notion (test list)

## Relevance to our work
- **agentos** (1/3): Could add a local 32B coder model to InferCraft on the single RTX 5090, but the video offers only anecdotal results and no serving or throughput data. → *If we evaluate a local coder model for InferCraft, use a fixed pass/fail prompt set with repeat runs and a rubric rather than a single pass through a hosted demo.*

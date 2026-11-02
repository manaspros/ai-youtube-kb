# Qwen 2.5 Max vs DeepSeek R1 – Which One is Better? (Tested)

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `6o_VFkOEwsI` · [watch](https://youtu.be/6o_VFkOEwsI) · **date:** 2025-11-02 · **length:** 9:39 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Alibaba, DeepSeek, OpenAI, Anthropic, Meta, Microsoft, Notion
- **topics:** models-research, evals · **tags:** qwen-2.5-max, deepseek-r1, deepseek-v3, model-comparison, manual-eval, reasoning-puzzles, instruction-following, code-generation, closed-weights, moe

> Hands-on, informal test of Alibaba's closed Qwen 2.5 Max chat model on roughly ten prompts reused from a DeepSeek R1 test; verdict: decent, but below DeepSeek V3 and not open source.

## Summary
AI LABS runs Alibaba's Qwen 2.5 Max through its chat interface using the prompt list previously used for DeepSeek R1, marking each answer pass or fail by hand. Qwen passes the factual and most reasoning prompts, fails a letter-pattern haiku constraint, and by the speaker's eye produces a more realistic SVG butterfly and a smoother CSS/JS cube than R1. A confetti-button HTML page works on the first try. The speaker concludes the model is decent but not at DeepSeek V3's level, with underwhelming code quality, an RL edge to DeepSeek, and closed weights as a deal-breaker for him. The evidence is informal: single runs, no quantitative scores, and at least one pass recorded against the speaker's own expected answer.

## Key ideas
- **Qwen 2.5 Max is pitched as a competitor to DeepSeek V3: a MoE model, trained with SFT and then RLHF.** — The speaker points to the Arena Hard and MMLU Pro charts, which compare against other Qwen, DeepSeek, Phi 3 and Llama 3.1 models but leave out ChatGPT and Claude because they are proprietary. ([0:00](https://youtu.be/6o_VFkOEwsI?t=0))
- **The model is closed: access is only through the API or the chat UI.** — The speaker switches the chat from the default Plus model to Max before testing, and says the model is not open source. ([1:22](https://youtu.be/6o_VFkOEwsI?t=82))
- **The test is a fixed prompt suite reused from an earlier DeepSeek R1 comparison, with a manual pass/fail verdict per prompt.** — The prompts are stored in Notion. Most factual and reasoning prompts pass. The speaker notes that Qwen solves a word problem that R1 had failed. ([2:57](https://youtu.be/6o_VFkOEwsI?t=177))
- **The model fails a checkable letter-pattern constraint.** — Asked for a haiku whose second letters spell BLACK, it used the first letters instead. R1 also failed this prompt. The speaker marks it a fail. ([2:57](https://youtu.be/6o_VFkOEwsI?t=177))
- **A puzzle is passed even though the answer differs from the speaker's expected answer.** — Six oranges, four juiced, half the juice drunk. The speaker expects 4 but accepts the model's 2 (the remaining oranges became juice) as a pass, which shows the rubric is subjective. ([2:57](https://youtu.be/6o_VFkOEwsI?t=177))
- **Code generation is judged visually, by pasting outputs into external viewers.** — The SVG butterfly is judged more realistic than R1's. The 3D cube is judged smoother with more refined transparency, though the model split the project into several files until the speaker asked for one HTML file. ([5:46](https://youtu.be/6o_VFkOEwsI?t=346))
- **A simple interactive HTML page (a button that releases confetti or bubbles) works on the first try.** — The speaker misses DeepSeek Chat's in-chat HTML preview and uses an external online HTML viewer instead. ([7:59](https://youtu.be/6o_VFkOEwsI?t=479))
- **Final verdict: decent but below DeepSeek V3, with underwhelming code quality and a weaker data set.** — The speaker credits DeepSeek with an RL advantage and calls Qwen 2.5 Max an over-trained Qwen 72B rather than a breakthrough. Lack of open weights is a dealbreaker for him. ([9:05](https://youtu.be/6o_VFkOEwsI?t=545))

## Techniques
- **Fixed prompt suite reused across models** — Keep a list of prompts from an earlier model test (the speaker uses Notion). Run each one in a fresh chat with the new model selected, then mark pass or fail. Reuse the same list to compare against the older baseline model. *When:* Quick head-to-head of a new model against a known baseline, when there is no time for a proper eval harness.
- **Render-and-inspect generated artifacts** — For SVG or HTML output, copy the generated code into an external viewer (an SVG viewer or an online HTML viewer) and judge the rendered result visually, not the source. *When:* Code-generation comparisons where the output is visual, and the chat UI does not preview HTML.
- **Ask for a single-file HTML output for testing** — When the model splits a small page into several files, ask it to put everything into one HTML file so it can be pasted and viewed directly. *When:* Quick UI checks of generated front-end code in a chat interface.
- **Checkable constraint probe** — Include a prompt with an unusual, mechanically checkable constraint, such as a haiku whose second letters spell a word. It tests instruction-following separately from reasoning. *When:* Adding cheap, objective test cases to a model-comparison prompt suite.

## Numbers
- Video length is 9:39. The speaker does not quote any benchmark scores from the charts he shows. ([0:00](https://youtu.be/6o_VFkOEwsI?t=0))
- About ten prompts are run (the speaker does not number them): one failure (the haiku letter constraint), the rest marked as passes. ([2:57](https://youtu.be/6o_VFkOEwsI?t=177))
- Oranges puzzle: 6 oranges, 4 juiced, half the juice drunk. Model answers 2, speaker expects 4, marks it a pass. ([2:57](https://youtu.be/6o_VFkOEwsI?t=177))
- Speed is described only qualitatively: the first answer comes back quickly, and the SVG generation is described as not very fast. No latency or token figures are given. ([5:46](https://youtu.be/6o_VFkOEwsI?t=346))
- Verdict is qualitative only: 'decent but definitely not on DeepSeek V3's level'. No quantitative score is reported. ([7:59](https://youtu.be/6o_VFkOEwsI?t=479))

## Hot takes
- Qwen 2.5 Max is a closed model, and the speaker says that alone is a deal-breaker for him.
- The evaluation is informal: single runs, pass/fail judged by eye, and at least one pass recorded against the speaker's own expected answer (oranges).
- The conclusion that DeepSeek has an RL edge and that Qwen is an 'over-trained Qwen 72B' is asserted, not shown by any test in the video.
- The benchmark charts that the speaker reads out are not quantified in the video, so the comparison with V3 rests on the prompt tests only.

## Tools mentioned
Qwen 2.5 Max (Alibaba, closed model, chat and API only), Qwen 2.5 Plus (default model in the Qwen chat), Qwen 2.5 72B, DeepSeek R1 (reasoning model, baseline), DeepSeek V3, DeepSeek Chat (online HTML preview feature), Phi 3, Llama 3.1, GPT-4o, Claude 3.5 Sonnet, Notion (prompt storage), Arena Hard (benchmark), MMLU Pro (benchmark)

## Relevance to our work
- **agentos** (1/3): AgentOS runs open-weight models on self-hosted vLLM (InferCraft). This video is about a closed model and only shows that model choice needs a repeatable test set, not a single anecdote. → *Build a fixed, reusable prompt suite (with checkable constraint cases) to compare candidate models for the router, and do not assume closed API models can be served locally.*

# Grok 3 Tested: Did Elon Musk Actually Succeed This Time?

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `E4fML4Lghjw` · [watch](https://youtu.be/E4fML4Lghjw) · **date:** 2025-11-02 · **length:** 6:20 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** AI LABS host (narrator, unnamed) · **orgs:** xAI, LM Arena, Artificial Analysis, OpenAI, DeepSeek, Anthropic, Cursor, Windsurf
- **topics:** models-research, evals, coding-agents · **tags:** grok-3, xai, lm-arena, model-comparison, leaderboards, reasoning-model, svg-generation, instruction-following, ad-hoc-eval

> Hands-on test of xAI's Grok 3 with about 11 quick prompts: strong on word problems and reasoning, failed the constrained haiku and most coding prompts, so the verdict is not for coding tools.

## Summary
The AI LABS host tests Grok 3 right after its release, when it was only reachable through LM Arena's chat UI with no API and limited access. He relays launch claims: a reported LM Arena score of about 1,400, a reasoning mode and a Deep Search agent, and Artificial Analysis ranking it the top non-reasoning model. He then runs roughly 11 short prompts. Word problems, a rhyme, and a trick adjective question pass, and the speaker says the adjective question stumped o3-mini and DeepSeek R1. A haiku with a letter constraint fails. On coding, an SVG butterfly fails twice (the second output is truncated), a 3D cube works, an HTML button that should release bubbles does not work, and a Python bouncing-ball-in-hexagon fails, which he attributes partly to a report from another developer. His verdict is that Grok 3 is good with text and reasoning but weak at code, so he would not put it into Cursor or Windsurf. The evidence is one run per prompt with no scoring rubric, and the benchmark and training figures are second-hand.

## Key ideas
- **Grok 3 launched with no official trailer or website and no general access or API. The only free route was LM Arena's chat UI, and the rollout was limited to X Premium Plus users.** — The host says the model reportedly scored about 1,400 on the LM Arena leaderboard. A reasoning mode ('Big Brain') and a Deep Search agent were introduced alongside it, positioned against OpenAI. ([0:00](https://youtu.be/E4fML4Lghjw?t=0))
- **Launch benchmark claims are relayed second-hand from Artificial Analysis, which reportedly ranks Grok 3 as the top non-reasoning model. Its reasoning mode is said to beat other reasoning models until OpenAI's full o3 ships. Pricing was unknown.** — The host presents these as the leaderboard's findings, not his own measurements. ([1:24](https://youtu.be/E4fML4Lghjw?t=84))
- **Training-scale and company-age claims are presented as impressive but are unverified. The speaker says the model was trained on 100,000 H100 'Colossus' GPUs and that the company was founded less than two years earlier.** — He adds that NVIDIA's stock and GPU buying were not visibly hurt by the DeepSeek launch. He gives no source for these numbers. ([1:24](https://youtu.be/E4fML4Lghjw?t=84))
- **On plain text and reasoning the model did well in his tests. It passed the word problems, the rhyme, and a trick adjective question he says o3-mini and DeepSeek R1 missed. It failed a haiku with a letter-pattern constraint.** — Several answers needed a retry because the LM Arena instance shut down under load. The host counted a retried answer as a pass once it was correct. ([2:51](https://youtu.be/E4fML4Lghjw?t=171))
- **Coding was the weak area. An SVG butterfly failed on the first try, and the more detailed second attempt was cut off and broken. A 3D cube worked, but an HTML page with a bubble-releasing button did not work, and a Python ball-in-hexagon bounce failed.** — He copied the code exactly as produced, with no fixes or follow-up prompts. The hexagon failure is backed by a report from another developer on X. ([4:13](https://youtu.be/E4fML4Lghjw?t=253))
- **The verdict is that Grok 3 is solid for text prompts but not useful for coding, so he would not wire it into coding IDEs such as Cursor or Windsurf. The result is a single anecdotal test set, not a benchmark.** — He invites viewers to try their own prompts and report back on coding improvements. ([5:38](https://youtu.be/E4fML4Lghjw?t=338))

## Techniques
- **Pass/fail prompt battery for a new model** — Use a short fixed list of prompts across categories: a basic word problem, a rhyme, a letter-pattern constrained haiku, a counting or arithmetic word problem, a constrained-word question, SVG generation, a 3D cube in code, an interactive HTML button, and a Python physics sim. Send each prompt once, copy the output without edits, and mark pass or fail. *When:* A quick smoke test when a new model shows up on a leaderboard and you want a first look at instruction following and code output before any deeper evaluation.
- **Letter-constraint instruction test** — Ask for a haiku where the second letter of each word spells a target word (the video uses 'black'). Check the output by hand, since this constraint is easy to verify and easy to fail. *When:* A cheap, mechanical check of instruction following that does not need an LLM judge.
- **Copy-paste code check for generated apps** — Paste generated HTML, SVG or Python exactly as returned, run or render it, and check whether the behaviour works (button click, animation, physics). Treat truncated or non-running output as a fail. *When:* Judging whether a model can produce usable front-end or script code without a follow-up turn.

## Numbers
- LM Arena leaderboard score of about 1,400 (speaker-reported) ([0:00](https://youtu.be/E4fML4Lghjw?t=0))
- Grok 3 reported as the top non-reasoning model on Artificial Analysis (speaker-reported) ([1:24](https://youtu.be/E4fML4Lghjw?t=84))
- Trained on 100,000 H100 'Colossus' GPUs (speaker-reported, unverified) ([1:24](https://youtu.be/E4fML4Lghjw?t=84))
- Company founded less than two years before the launch (speaker-reported) ([1:24](https://youtu.be/E4fML4Lghjw?t=84))
- Own tests: 11 prompts, 6 pass and 5 fail. Coding: 1 of 5 passed (the 3D cube). ([2:51](https://youtu.be/E4fML4Lghjw?t=171))
- Word problem answers checked: two oranges left, and 80 books left, both correct ([2:51](https://youtu.be/E4fML4Lghjw?t=171))

## Hot takes
- A top leaderboard rank does not predict coding ability: the host's own coding tests failed on simple interactive HTML and SVG prompts.
- The sample is tiny. It is one run per prompt with no rubric, and retried answers counted as passes, so the pass/fail result is anecdotal.
- Title says 'Did Elon Musk actually succeed', but the video is a short prompt test with relayed launch claims, so it is light on substance; quality is capped at 2.

## Tools mentioned
Grok 3 (xAI), Grok 3 reasoning mode ('Big Brain'), Grok Deep Search agent, LM Arena (called 'chat arena' in the transcript), Artificial Analysis leaderboard, OpenAI o3 (upcoming, per the host), OpenAI o3-mini, DeepSeek R1, GPT-4o, Claude 3.5 (image and SVG comparison), Cursor, Windsurf, Python, SVG, HTML

## Relevance to our work
- **agentos** (1/3): AgentOS routes traffic across models, so a quick model smoke test is a useful intake step. The video's prompt battery is too ad hoc to be an eval. → *Build a small fixed prompt battery (constraint following, SVG or HTML generation, a short coding task) that AgentOS runs before a new model enters the routing pool, and record pass/fail with a repeat count.*
- **general** (1/3): A worked example of how thin a single-run, pass/fail test is, useful when reading model comparison videos. → *Require repeated runs and a written rubric before treating any model comparison as evidence.*

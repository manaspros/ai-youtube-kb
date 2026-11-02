# Opus 5.5 vs GPT-6 Sol (Blender F1 Car Test)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `Zc72O98x3nk` · [watch](https://youtu.be/Zc72O98x3nk) · **date:** 2026-10-02 · **length:** 6:43 · **format:** review · **quality:** 2/5 · **depth:** practitioner
- **speakers:** Better Stack host (unnamed) · **orgs:** Anthropic, OpenAI, Ferrari, Formula 1, Better Stack
- **topics:** models-research, coding-agents, token-cost-efficiency, evals · **tags:** blender, 3d-generation, model-comparison, opus-5.5, gpt-6-sol, gpt-6-astra, fable-5.1, gpt-6-luna, claude-code, codex, api-cost, subscription-usage

> Better Stack runs Opus 5.5 (Claude Code) and GPT-6 Sol (Codex) through the same three Blender prompts (static F1 model, build animation, pit-stop animation); Opus wins on quality but costs about 6x more.

## Summary
The creator ran the same three prompts, in the same order, through Opus 5.5 in Claude Code and GPT-6 Sol in Codex, both at extra high effort: a detailed Blender model of a Ferrari F2 car built from official launch photos, then a part-by-part build animation and a pit-stop animation. He judged Opus 5.5 the clear winner on finish and detail, with GPT-6 Sol noticeably weaker on 3D. He then added GPT-6 Astra and Fable 5.1 on the same prompts; a staff and viewer poll put Astra's pit-stop animation narrowly ahead of Opus, and Fable came third. Cost and time favored Sol strongly: about $4.50 in 49 minutes against $27.86 in 67 minutes for Opus, because Opus produced far more output despite a lower-priced token list rate than... (see key ideas). Astra cost $32.47 in 1h49m and Fable 5.1 $42.44 in 1h13m. The evidence is one run per model, judged by eye, so it is a practitioner anecdote rather than a benchmark.

## Key ideas
- **Test setup: Opus 5.5 ran in Claude Code and GPT-6 Sol in Codex, both at extra high effort, with identical prompts in identical order.** — Three prompts per model: build a high-detail Ferrari F2 car in Blender using web-gathered reference images; animate the car being assembled from its parts; animate a pit stop where the car drives in and out of frame. The creator notes the prompt typo ('F2' for 2026 F2) was caught by every model. ([0:00](https://youtu.be/Zc72O98x3nk?t=0))
- **All models used the same official Ferrari launch photos, which levels the reference-material input.** — Most of the reference images came from the Formula 1 site. The creator says this gave every model a fair view of all angles. ([0:48](https://youtu.be/Zc72O98x3nk?t=48))
- **Opus 5.5's build animation was the standout; the static model still had visible errors.** — Praised for the blueprint style, glow, reflections and clean part assembly. Flaws: the front wing is oversized and not flat with end plates, and the fin edges are jagged the wrong way round. ([2:04](https://youtu.be/Zc72O98x3nk?t=124))
- **GPT-6 Sol's model was judged less polished: parts not attached, a wrong-looking car class, and a backwards logo.** — The creator says the car looks like a sub-F1 single-seater and that its pit-stop tyres fly off oddly. He reads this as weaker 3D understanding, which he suspects was not a focus of its training. ([2:04](https://youtu.be/Zc72O98x3nk?t=124))
- **Per-token price is misleading. Sol lists at half Opus's per-token price, yet the Opus run cost about 6x more because it produced about 6x more output.** — Via API-equivalent pricing, Opus cost $27.86 over 1h07m and Sol cost $4.50 over 48m44s. About $11 of the Opus bill is cache writes (auto-captions say 'cash'). The creator ran everything on his Claude subscription and says it barely dented his usage. ([3:10](https://youtu.be/Zc72O98x3nk?t=190))
- **A community poll gave GPT-6 Astra's pit-stop animation a narrow win over Opus, though the creator still prefers Opus overall.** — Astra's model was praised for accurate front wing, wheel covers and rear wing; Opus was praised for side accuracy and motion blur. Fable 5.1 finished third in the poll, with weird render artifacts on its build but a well-liked pit-stop animation. ([4:26](https://youtu.be/Zc72O98x3nk?t=266))
- **Final cost and time comparison across all four runs: Sol cheapest and fastest but worst; Opus 5.5 the creator's new daily driver.** — Astra cost $32.47 in 1h49m and Fable 5.1 cost $42.44 in 1h13m. The creator says Opus 5.5 is a clear step up from Opus 5 and he has not needed Fable. He suggests OpenAI's cheaper GPT-6 Luna for small tasks. ([5:35](https://youtu.be/Zc72O98x3nk?t=335))

## Techniques
- **Same-prompt, same-order head-to-head across agent CLIs** — Run identical prompts in the same order through each model's native agent (Claude Code for Opus, Codex for GPT-6 Sol), at the same effort setting. Give each model the same reference inputs (here, the same web-sourced launch photos). Record API-equivalent cost and wall-clock time per run, then judge outputs side by side and optionally run a poll. *When:* Choosing a model for a multi-step generative or coding task where quality, cost and time all matter and a single benchmark is not trusted.
- **Judge cost per finished task, not per token** — Compare total run cost (tokens in, tokens out, cache writes) and total time to a finished result, instead of list price per token. A cheaper per-token model can cost more if it writes more output. *When:* Evaluating model or routing choices in a cost-sensitive agent pipeline, or explaining why a cheaper model is not automatically cheaper per task.
- **Build an animation as a sequence of agent prompts** — Prompt 1 builds the static 3D model with a detail requirement and an instruction to gather web reference images. Prompt 2 animates assembly of the parts. Prompt 3 animates a scene (a pit stop driving in and out of frame). Each later prompt builds on the previous output. *When:* Testing an agent's 3D or Blender capability, or any multi-stage generative asset pipeline.

## Numbers
- GPT-6 Sol: API-equivalent cost $4.50 over 48m44s, the cheapest and fastest run. ([3:10](https://youtu.be/Zc72O98x3nk?t=190))
- Opus 5.5: API-equivalent cost $27.86 over 1h07m, about 6x Sol's cost. ([3:10](https://youtu.be/Zc72O98x3nk?t=190))
- Sol's per-token price is half of Opus's, but Opus wrote about 6x more output. ([3:10](https://youtu.be/Zc72O98x3nk?t=190))
- About $11 of Opus's bill came from cache writes (auto-captions say 'cash'). ([3:10](https://youtu.be/Zc72O98x3nk?t=190))
- GPT-6 Astra: $32.47 over 1h49m. ([5:35](https://youtu.be/Zc72O98x3nk?t=335))
- Fable 5.1: $42.44 over 1h13m. ([5:35](https://youtu.be/Zc72O98x3nk?t=335))
- Four runs, one per model, one prompt set each. Costs are API-equivalent, while the runs themselves were on a Claude subscription. ([3:10](https://youtu.be/Zc72O98x3nk?t=190))

## Hot takes
- Single run per model, judged by eye, plus a small social poll. That is an anecdote, not a benchmark, and results could change on a rerun.
- The creator claims Sol's weakness is due to weaker 3D training. That is speculation, not something the tests show.
- Subscription usage 'barely made a dent' is an anecdote, and the API-equivalent cost numbers do not map directly to subscription limits.
- Opus 5.5 as the 'new daily driver' is a personal preference drawn from one prompt set, not a general ranking.

## Tools mentioned
Claude Code, Codex, Blender, Claude Opus 5.5, GPT-6 Sol, GPT-6 Astra, Fable 5.1, GPT-6 Luna

## Relevance to our work
- **agentos** (1/3): Shows that per-token price can mislead about cost per task, which is relevant to AgentOS budget and routing decisions. → *Log API-equivalent cost and wall-clock per completed task (not per token) in the budget and routing layer, so cheap-per-token models that produce more output are compared fairly.*
- **prosharness** (1/3): ProsHarness wraps Claude Code and could run the same prompt set through Codex and Claude Code for comparison. → *Add a simple harness mode that runs one prompt set through Claude Code and Codex and records cost and time per run, using the same-prompt, same-order method.*

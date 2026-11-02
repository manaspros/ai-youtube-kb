# Qwen3 Coder vs Kimi K2 vs Claude Sonnet 4

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `nzAT09XolYw` · [watch](https://youtu.be/nzAT09XolYw) · **date:** 2025-11-02 · **length:** 5:23 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Better Stack, Moonshot, Anthropic, OpenRouter
- **topics:** coding-agents, evals, token-cost-efficiency · **tags:** model-comparison, qwen3-coder, kimi-k2, claude-sonnet-4, opencode, nextjs, cost-per-task, anecdotal-eval, debug-loop, youtube-transcript

> Better Stack runs one Next.js blog-generator spec through Qwen3 Coder, Kimi K2 and Claude Sonnet 4 in OpenCode. Qwen was fastest and cheapest, Sonnet built fastest, yet all three hit a YouTube-transcript failure.

## Summary
The video is a single-run, head-to-head test of three coding models (Qwen3 Coder, Kimi K2, Claude Sonnet 4) building the same small Next.js app that turns YouTube transcripts into blog posts in the author's writing style. All three run through the same harness, OpenCode, each through its own provider (Pro subscription, Moonshot console, OpenRouter as spoken). Kimi K2 took just under 10 minutes and produced a working app that generated a post. Qwen3 Coder took about 5 minutes and about 50 cents, but its first build exposed API keys to the browser, its buttons did nothing until a prompt fixed an unused loading-state variable, and its transcript fetch then failed. The speaker stopped debugging Qwen because the loop was spiraling. Claude Sonnet 4 finished in just over 3 minutes using bun, but also failed to retrieve captions ("no captions available"), and the speaker could not get it past that in a fresh session either. The conclusion is that benchmark rankings did not predict the outcome, and that environment, project and prompt quality matter. The speaker plans to use Kimi K2 for cheap, small tasks and Sonnet for harder ones.

## Key ideas
- **Fair comparison setup: all three models run through the same harness (OpenCode) on the same starter Next.js repo with one prompt file, so the harness does not vary between them.** — The Qwen CLI (a Gemini CLI fork) was deliberately not used. Each model was reached through its own provider: Claude via Pro subscription, Kimi via the Moonshot console, Qwen via OpenRouter (transcript says 'OpenReader'). ([0:00](https://youtu.be/nzAT09XolYw?t=0))
- **Kimi K2 produced a working app first, in just under 10 minutes, and the generated post looked right on the speaker's test video.** — It planned, then built a style-analysis file, a generation file and a display/download file, then wrote a README. The uploaded sample posts were analysed for style before generation. ([1:17](https://youtu.be/nzAT09XolYw?t=77))
- **Qwen3 Coder was the fastest and cheapest build, but the output was broken in ways that needed fixes.** — About 5 minutes and almost $0.50. The app exposed API keys to the browser, which the speaker patched by hand for the test only. The upload buttons did nothing; a prompt fixed an unused isLoadingState variable. ([1:17](https://youtu.be/nzAT09XolYw?t=77))
- **The speaker stopped debugging Qwen once the transcript fetch failed, calling this the point where an LLM enters a 'downward spiral of debugging'.** — This is an explicit, practical cutoff: after one failed fix on an external dependency, switch models or stop rather than keep prompting. ([2:44](https://youtu.be/nzAT09XolYw?t=164))
- **Claude Sonnet 4 was the fastest build (just over 3 minutes), using bun and writing both the upload and transcript code, but it failed in the same place as the others.** — It reported 'no captions available' for the video. The speaker tried fresh sessions for both Claude and Qwen and still could not get a transcript, so the failure lay in the environment or library choice, not the model's rank. ([2:44](https://youtu.be/nzAT09XolYw?t=164))
- **Benchmark rankings did not predict this outcome. The speaker's conclusion is that the environment, the project, prompt quality and other factors decide per-task results.** — The expected order was Claude, then Qwen, then Kimi. The actual result was Kimi the most complete, Qwen the fastest and cheapest, Claude the fastest-to-first-build but blocked. ([4:07](https://youtu.be/nzAT09XolYw?t=247))
- **Model assignment by cost and difficulty: Kimi K2 for small, cheap coding tasks even though it is slower, and Sonnet 4 for more complicated work.** — The speaker's pick is based on price, not on this one test's quality ranking. ([4:07](https://youtu.be/nzAT09XolYw?t=247))

## Techniques
- **Same-repo, same-prompt head-to-head** — Start each model from an identical starter Next.js repo that contains a prompt file. Tell the agent to 'read and execute the prompt file'. Route each model through the same harness (OpenCode) and record wall time, cost, whether the app runs, and where it fails. *When:* Use to compare coding models on one real task before adopting one. It is a cheap eval, but it is only one run per model.
- **Spec in a prompt file, not in the chat** — Keep the full app spec (upload three Markdown samples for style, add a YouTube URL, extract transcript, generate post, display/download) in a file in the repo. The agent's first step is a plan, then one file per feature, then a README. *When:* Use for greenfield builds where you want the same spec replayed across models or sessions.
- **Stop-loss on the debug loop** — If a fix prompt does not resolve an external-dependency failure (here a missing YouTube transcript), stop and switch model or approach instead of continuing the back-and-forth. *When:* Use when the error comes from a third-party service or library, not from the agent's own code, and one fix attempt has failed.
- **Style-from-samples analysis step** — Have the app read the user's sample posts first, extracting tone, voice and sentence structure, then use that analysis as context in the generation prompt. The app analysed three uploaded Markdown posts before generating. *When:* Use when generated text must match a specific author's voice.
- **Tiered model assignment by cost** — Route small, self-contained coding tasks to a cheaper model (Kimi K2 in the speaker's use) and reserve the strongest model (Sonnet 4) for complex tasks. The decision is driven by price and slowness tolerance, not by benchmark rank. *When:* Use when you run many coding tasks and cost per task matters more than top-end quality on each one.

## Numbers
- Kimi K2 full build time: just under 10 minutes. ([1:17](https://youtu.be/nzAT09XolYw?t=77))
- Qwen3 Coder build time: just over 5 minutes, cost almost $0.50. ([1:17](https://youtu.be/nzAT09XolYw?t=77))
- Claude Sonnet 4 build time: just over 3 minutes (fastest to a first build), using bun. ([2:44](https://youtu.be/nzAT09XolYw?t=164))
- Test sample: three Markdown blog posts uploaded as style samples; sample count is the app's minimum requirement ('at least three sample posts'). ([0:00](https://youtu.be/nzAT09XolYw?t=0))
- Video length 5:23, one run per model, no repeat trials. ([0:00](https://youtu.be/nzAT09XolYw?t=0))

## Hot takes
- Benchmarks are not a reliable guide to real coding tasks: the speaker's expected order (Claude, then Qwen, then Kimi) was not what happened.
- Cutting off a debug loop after one failed fix on a third-party issue is better than endless prompting (the Qwen transcript case).
- Qwen3 Coder's low cost and speed did not offset the broken first build, which needed a manual fix and a secret-exposure patch.
- Kimi K2 is worth using for small tasks despite being slower, because it is much cheaper (no number given).

## Tools mentioned
OpenCode, Qwen3 Coder, Kimi K2, Claude Sonnet 4, Next.js, bun, OpenRouter, Moonshot console, Gemini CLI (fork basis for Qwen CLI, not used in the test), GPT-4 (named as the extraction model in the Claude build's prompts), YouTube transcript API/library (unnamed), Markdown

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code in loops with checkpoint/resume. The video shows a concrete failure mode, an agent stuck in a debug spiral on an external dependency, which argues for a stop-loss and hand-off rule. → *Add a stop rule to ProsHarness loops: after N failed fix attempts on the same external error, checkpoint the run and escalate or switch model instead of continuing to debug.*
- **agentos** (1/3): AgentOS routes model traffic. A fixed build spec run across models, scored on time, cost and pass/fail, is a cheap way to test cheap-model routing, but this video is one anecdotal run per model. → *Build a small fixed-spec coding eval (a starter repo plus a prompt file) and record time, cost and pass/fail per model to ground any cheap-model routing rule in AgentOS.*

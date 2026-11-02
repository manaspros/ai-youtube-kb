# OpenAI is Winning... (Opus 4.6 + Codex 5.3)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `OI6DkkNDf6o` · [watch](https://youtu.be/OI6DkkNDf6o) · **date:** 2026-03-02 · **length:** 12:36 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Better Stack presenter (unnamed in transcript) · **orgs:** Anthropic, OpenAI, Convex, Artificial Analysis, Design Arena
- **topics:** coding-agents, models-research, context-engineering · **tags:** claude-opus-4-6, gpt-5-3-codex, ai-sdk-v6-migration, terminal-bench-2, cross-model-review, compaction, agent-teams, steering-running-agents, design-generation, model-comparison

> Better Stack runs Claude Opus 4.6 and GPT-5.3 Codex through an AI SDK v6 migration, a Three.js Club Penguin clone and a landing page; each test is one run, so the verdicts are soft.

## Summary
The presenter compares Claude Opus 4.6 (Claude Code) and GPT-5.3 Codex, released within minutes of each other, on three hands-on tasks. First, both upgraded a Convex agent package to AI SDK v6 from a broken state, with a prompt that required all tests to pass and banned type-cast hacks; each ran about 40 minutes and ended with zero build or type errors. Codex's diff included v6 tool-approval handling that Opus missed, but Codex also hand-wrote a UI-to-model message converter that the SDK already provides, which Opus used correctly. Codex 5.3, asked to review both diffs, picked the Opus architecture and suggested porting over only the approval logic. Second, a single-prompt Three.js Club Penguin clone with no assets gave both models a playable town, zones and a sled racer, with bugs in each; the presenter preferred the Opus build. Third, a single-HTML landing page for an AI-only social network favored Codex's neo-brutalist design, while Opus had a more functional page. The release notes also cover a 1M-token Opus context window in beta, Codex being steerable mid-run, and Claude Code agent teams, API-side compaction and adaptive thinking.

## Key ideas
- **Opus 4.6 briefly held the top Terminal-Bench 2.0 score before GPT-5.3 Codex landed and beat it by over 10%, the only benchmark the presenter could directly compare because the two vendors used different benchmarks.** — Vendor claims only; the presenter notes Anthropic's lead lasted minutes and Artificial Analysis had benchmarked only a non-reasoning Opus 4.6 for coding. ([0:00](https://youtu.be/OI6DkkNDf6o?t=0))
- **Real-world migration test: upgrading a Convex agent package to AI SDK v6 is a breaking migration, and both models reached a clean build with passing tests.** — Prompt gave the migration guide as context, required all tests passing, and told the model to avoid TypeScript escape hatches such as 'as any'. Codex took one follow-up prompt; Opus took two. ([2:21](https://youtu.be/OI6DkkNDf6o?t=141))
- **Both models ran about 40 minutes unattended on the migration; Codex's diff was +545 / -111 lines.** — The presenter was impressed by the uninterrupted run. Opus in Claude Code ran about 40 minutes too, but its first start hit build errors. ([2:21](https://youtu.be/OI6DkkNDf6o?t=141))
- **The diffs differed in the details that matter for maintenance: Codex added v6 tool-approval handling that Opus skipped, but hand-wrote a UI-to-model message converter that the SDK already provides.** — Opus used the SDK's convertToModelMessages-style helper, so future SDK upgrades won't require touching local code. The presenter treats reimplementing an SDK helper as a red flag in review. ([4:52](https://youtu.be/OI6DkkNDf6o?t=292))
- **Cross-model review: Codex 5.3 reviewing both diffs chose the Opus version as the base to ship and suggested porting only Codex's approval and denial handling.** — The presenter says this showed the reviewer was not biased toward itself. He still calls it one test and says prompting could have steered either model. ([5:51](https://youtu.be/OI6DkkNDf6o?t=351))
- **Single-prompt Three.js Club Penguin clone with no assets: both produced a character creator, a map with zones, and a sled racer, plus buggy kart-surfing and walk-through-building problems.** — The presenter preferred the Opus build (identified after the reveal) for its results on his test; the Codex build looked chunkier and darker, with a broken surfing game. ([5:51](https://youtu.be/OI6DkkNDf6o?t=351))
- **Design test: a single HTML landing page for an AI-only social network. Codex's neo-brutalist design felt less generic; Opus's page was more functional, with trending, rules and subreddit-style sections.** — Presenter says the Opus page looked like a typical vibe-coded app with purple gradients. At the time of the video GLM 4.7 led Design Arena and neither new model was ranked yet. ([9:12](https://youtu.be/OI6DkkNDf6o?t=552))
- **New capabilities in these releases: Codex can be steered mid-run rather than only interrupted; Claude Code gets agent teams (subagents); the Claude API adds built-in compaction and an adaptive thinking mode; Opus 4.6 has a 1M-token context window in beta.** — Pricing given for prompts over 200k tokens: $10 per million input tokens and $37.50 per million output tokens. OpenAI calls Codex 5.3 25% faster than 5.2 Codex. ([10:36](https://youtu.be/OI6DkkNDf6o?t=636))

## Techniques
- **Migration prompt with guardrails** — Tell the agent what changed, paste the official migration guide as context, require the full test suite to pass, forbid type-cast escape hatches (for example 'as any'), and have it run the build periodically while it works. Ask for a plan before coding. *When:* Upgrading a library with breaking type changes where the agent might otherwise paper over errors.
- **Review the diff for reimplemented library helpers** — When reviewing agent-written code, search the diff for hand-written functions that duplicate a helper the library already exports (the presenter's example: a UI-to-model message converter). Replace them with the library's function. *When:* Code review of agent output after a dependency upgrade, since local copies break silently on later upgrades.
- **Cross-model second opinion** — Give model B the diffs from model A and ask for a comparison of advantages and disadvantages, plus a pick of which to base the merge on and what to port over. The presenter used Codex 5.3 to review a Claude Code diff and vice versa. *When:* A high-stakes change where you want an independent review. Treat it as a second opinion, not a verdict.
- **Steer instead of interrupt** — Use a coding agent that accepts messages while it works (the presenter demonstrates this in the Codex app) to redirect it, rather than stopping the run and re-prompting. *When:* Long-running agent tasks, where stopping to correct course loses progress.

## Numbers
- GPT-5.3 Codex beats Opus 4.6 on Terminal-Bench 2.0 by over 10% (presenter's words). ([0:00](https://youtu.be/OI6DkkNDf6o?t=0))
- Opus 4.6 1M-token context window (beta): prompts over 200,000 tokens cost $10 per million input tokens and $37.50 per million output tokens. ([1:12](https://youtu.be/OI6DkkNDf6o?t=72))
- OpenAI says GPT-5.3 Codex is 25% faster than GPT-5.2 Codex. ([1:12](https://youtu.be/OI6DkkNDf6o?t=72))
- Convex migration runs: about 40 minutes each, unattended for Codex; Codex diff +545 lines / -111 lines. ([2:21](https://youtu.be/OI6DkkNDf6o?t=141))
- Prompts needed to reach a clean build with all tests passing: Codex 1 follow-up prompt, Opus 4.6 2 prompts. ([3:40](https://youtu.be/OI6DkkNDf6o?t=220))
- Design Arena: GLM 4.7 was the leader at recording time; neither GPT-5.3 Codex nor Opus 4.6 was ranked yet. ([9:12](https://youtu.be/OI6DkkNDf6o?t=552))

## Hot takes
- Codex 5.3 has a clear lead on Terminal-Bench 2.0, but the vendors use different benchmarks, so there is little apples-to-apples comparison.
- Opus 4.6 gives the better migration architecture (cross-model review agreed), but Codex 5.3 has the better design sense; the presenter says he will likely lean Codex because he likes the Codex app and prompting OpenAI models.
- The presenter says the Codex landing page looks less vibe-coded than the Opus one, and suspects manual prompting pushed it there, despite identical prompts.
- Each comparison is a single run per model, so the presenter's verdicts are soft; he says he will keep using both to judge in real use.
- Sponsorship: none seen. The video is hands-on, but thin on quantitative evidence.

## Tools mentioned
Claude Opus 4.6, GPT-5.3 Codex, GPT-5.2 Codex, GPT-5.2, Claude Code, Codex app, Convex, Convex Agent package, AI SDK v6, Three.js, Terminal-Bench 2.0, Artificial Analysis, Design Arena, GLM 4.7, Moltbook (named as a reference site)

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI and plans to use Codex for critique. The video covers Claude Code agent teams, API compaction, and a cross-model review anecdote that touches the plan-critique-debate loop. → *Run a small test of the Codex-reviews-Claude-diff pattern on real ProsHarness changes to see whether it catches the same kinds of issues, then consider it for the critique step before relying on it.*

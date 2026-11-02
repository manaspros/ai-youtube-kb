# I Let Aider AI Refactor My App

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `cTSvN0YLMgw` · [watch](https://youtu.be/cTSvN0YLMgw) · **date:** 2026-03-02 · **length:** 4:44 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, DeepSeek, OpenAI, Anthropic, Cursor, GitHub, Ollama
- **topics:** coding-agents, dev-tools, token-cost-efficiency · **tags:** aider, terminal-coding-agent, git-native, architect-mode, repo-map, tree-sitter, deepseek, model-swapping, flask, react, typescript, claude-code-comparison, ollama, cursor, copilot

> Short walkthrough of Aider, a terminal AI pair programmer that makes git-committed, repo-wide edits. Its architect-then-code split and per-change undo are the useful parts; the speed and cost claims are mostly unverified.

## Summary
The host presents Aider as a terminal AI pair programmer that edits a repo directly, using a tree-sitter-built repo map, and says it works with Claude, DeepSeek and OpenAI models. Every change is a git commit, so a bad edit can be undone immediately. Aider's self-reported 88% success on 225 polyglot coding tasks is cited without verification. Two demos follow: adding Flask-Login and bcrypt auth with unit tests to a small Flask app in roughly 45 seconds, and a multi-file React/TypeScript dark-mode and API-sync change that uses architect mode to plan and then code mode to implement, followed by generated tests. The speaker claims 2-5x speedups with DeepSeek, about a cent per edit, and handling of projects over 20k lines, but says the reports of hour-long refactors cut to 10 minutes have no real evidence behind them. The comparison with Cursor, Copilot, Claude Code and Ollama is opinion, not a benchmark. The closing advice is to use architect mode before big refactors, set the model in a YAML config file, and always review the diffs.

## Key ideas
- **Aider is a terminal pair programmer that edits the repo directly instead of autocompleting the next line.** — It builds a repo map with tree-sitter so edits can span files. The speaker contrasts this with Copilot-style inline completion. ([0:00](https://youtu.be/cTSvN0YLMgw?t=0))
- **Git-native editing: every Aider change is a commit, and a failed change can be undone at once.** — The speaker's point is that a failed build leaves no mess to clean up. The fix is to adjust the prompt and rerun. ([0:00](https://youtu.be/cTSvN0YLMgw?t=0))
- **Setup is a one-line curl install plus a DeepSeek API key. First run walks through yes/no setup prompts, then the chat is available in the editor's terminal.** — The speaker runs it inside VS Code's terminal. The install and second command were not legible on screen, so exact commands are not captured. ([0:53](https://youtu.be/cTSvN0YLMgw?t=53))
- **Flask demo: a request to add Flask-Login and bcrypt auth with unit tests touched several files, added requirements, created a test file, and committed, in about 45 seconds.** — The speaker says the run only counts if it reaches a passing test and a clean commit. Shown on one small app, so it is a single data point. ([0:53](https://youtu.be/cTSvN0YLMgw?t=53))
- **Claimed scale and cost: handles projects over 20k lines, edits cost about a cent with DeepSeek, and devs report 2-5x speedups. The speaker explicitly notes no real evidence behind the one-hour-to-10-minutes anecdote.** — Treat these as vendor-adjacent or anecdotal claims. Only the cost-per-edit figure is concrete. ([2:07](https://youtu.be/cTSvN0YLMgw?t=127))
- **Architect-then-code workflow for a multi-file React/TypeScript change (dark mode plus API sync): plan in architect mode with no edits, switch to code mode to implement, then ask for tests.** — When the build failed, Aider undid the changes cleanly and the prompt was fixed and rerun. The build then passed, leaving a feature branch ready for PR. ([2:07](https://youtu.be/cTSvN0YLMgw?t=127))
- **Tool comparison is opinion, not measured. Cursor has the stronger UI, Copilot is fast at inline completion but weak at repo-wide reasoning, and Claude Code has strong reasoning but a looser git workflow. Swapping in DeepSeek is cheaper with still-strong responses; Ollama is free but weaker, in the speaker's view.** — No benchmark or side-by-side task results are shown. ([3:24](https://youtu.be/cTSvN0YLMgw?t=204))
- **Practical advice: use architect mode before major refactors, configure the model in the YAML config file, and always review the diffs Aider produces.** — The video ends by suggesting an editor integration, but the speaker's setup stays in the terminal. ([4:29](https://youtu.be/cTSvN0YLMgw?t=269))

## Techniques
- **Architect-then-code two-pass edit** — Run Aider's architect mode first to plan the multi-file change with no edits. Review the plan, switch to code mode to implement it, then ask for tests covering the new logic. The speaker's example: a dark-mode and API-sync change across theme config, components and the API client. *When:* Before any large or multi-file refactor where a wrong first attempt would be costly.
- **Git-as-checkpoint for agent edits** — Let each agent change land as its own commit. If the build or tests fail, undo the commit, adjust the prompt, and run again. Do not hand-patch the failed output. *When:* Any agent editing a real repo where rollback needs to be instant and unambiguous.
- **Passing-tests-plus-clean-commit as the done bar** — Ask for unit tests in the same request, then accept the change only when the build passes and the commit is clean. The speaker's bar for the Flask auth demo was a passing test suite and a clean commit. *When:* When judging whether an agent's output saves time, not just looks finished.
- **Model swap via YAML config for cheaper runs** — Set the model in Aider's YAML config file, then point it at a DeepSeek API key. The speaker switches models this way and reports cheaper calls with strong responses. The config file name and keys are not shown on screen. *When:* When the per-edit cost matters and a cheaper model is good enough for multi-file edits.
- **Diff review before accepting** — Read each diff Aider produces before keeping it. The speaker's advice is to review diffs every time, since the commits are the audit trail. *When:* Always, especially when the edit touches auth or shared code.

## Numbers
- Self-reported 88% success on 225 polyglot coding tasks (Aider's own figure, unverified in the video) ([0:00](https://youtu.be/cTSvN0YLMgw?t=0))
- Speaker says about 88% of Aider's own code was written by Aider; as stated, not verified ([0:00](https://youtu.be/cTSvN0YLMgw?t=0))
- Supports over 100 languages ([0:00](https://youtu.be/cTSvN0YLMgw?t=0))
- Flask auth plus tests run took roughly 45 seconds, maybe a bit more ([0:53](https://youtu.be/cTSvN0YLMgw?t=53))
- Handles projects over 20,000 lines of code ([2:07](https://youtu.be/cTSvN0YLMgw?t=127))
- Devs report 2-5x speedups with DeepSeek models ([2:07](https://youtu.be/cTSvN0YLMgw?t=127))
- Edits cost about one cent ([2:07](https://youtu.be/cTSvN0YLMgw?t=127))
- Reports of refactors cut from about an hour to 10 minutes; speaker says there is no real evidence for this ([2:07](https://youtu.be/cTSvN0YLMgw?t=127))

## Hot takes
- The 88% success figure is Aider's own benchmark claim. The speaker calls it 'not perfect' but does not verify it.
- Aider has the edge over Cursor and Claude Code for heavy multi-file refactors in a terminal workflow. This is the speaker's opinion, based on two demos.
- Claude Code has strong reasoning but its git workflow is not as tight. Asserted, not shown side by side.
- Ollama is 'good but not great' compared with DeepSeek. Asserted without measurements.
- Depth is shallow: 4:44 total, with install commands not legible on screen and no cost or success measurements from the speaker's own runs.

## Tools mentioned
Aider, DeepSeek (cited as DeepSeq in captions), Claude (model), OpenAI models, Ollama, Flask, Flask-Login, bcrypt, React, TypeScript, tree-sitter, Git, VS Code, Cursor, GitHub Copilot, Claude Code (cited as cloud code in captions)

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI with checkpoint/resume and plan-then-critique. Aider's git-native commit-per-change plus instant undo, and its architect-then-code split, are directly comparable checkpoint and planning mechanisms. → *Compare ProsHarness checkpointing with Aider's commit-per-edit undo. Consider making each harness edit its own git commit so checkpoint and rollback become a git revert, and test an architect-style plan-only pass before code mode.*

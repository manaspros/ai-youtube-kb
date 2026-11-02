# Copilot Helps You Type…. This Helps You Ship

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `LRwc64Ui_MQ` · [watch](https://youtu.be/LRwc64Ui_MQ) · **date:** 2026-03-02 · **length:** 4:52 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Continue, GitHub, Ollama
- **topics:** coding-agents, pr-code-review, context-engineering · **tags:** continue, vscode, github-copilot, code-review, pr-review-agent, ollama, local-llm, model-agnostic

> A short walkthrough of Continue, an open-source VS Code extension for model-agnostic codebase chat, diff-based edits and markdown-defined PR review agents, positioned as complementary to Copilot.

## Summary
Better Stack presents Continue, an open-source VS Code extension, as a tool that removes friction around code, mainly code review, rather than writing code. Setup is a short extension install plus adding a model entry, either a cloud model with an API key or a local Llama 3 model served through Ollama, and models can be switched from the sidebar. The chat pulls context from the whole project (open files, git diffs), so explanations are repo-aware, and refactor suggestions show a reviewable diff that can be applied or rejected. The most distinctive feature shown is the review agent: a markdown file of rules (formatting, logic, security) that can be run against a PR, with prebuilt agents such as a security one, and output as PR comments or diffs. The speaker frames Continue as complementary to GitHub Copilot (Copilot for autocomplete, Continue for pre-merge checks). The video is thin: no benchmarks, no review-quality evidence, and the value claims are mostly asserted.

## Key ideas
- **Continue is pitched as a model-agnostic VS Code extension: cloud models with your own API key or free local models, switchable from the sidebar without lock-in.** — Setup is installing the extension, adding a model to the config (cloud with an API key, or a local model pulled through Ollama), then reloading. ([0:00](https://youtu.be/LRwc64Ui_MQ?t=0))
- **The main value claimed is in the work around the code (reviews, cross-checking, onboarding), not code generation.** — The speaker frames the bottleneck as slow code review and PR cycles, and says AI should automate the repetitive parts. ([0:00](https://youtu.be/LRwc64Ui_MQ?t=0))
- **Chat answers are repo-aware because Continue pulls context from open files and git diffs, versus pasting snippets into a browser chat.** — Highlight code, press Ctrl+L, ask 'explain this'. The speaker concedes Claude Code and Cursor can do similar things. ([1:23](https://youtu.be/LRwc64Ui_MQ?t=83))
- **Suggested edits come as a real side-by-side diff in chat that the user applies, edits or rejects.** — The speaker stresses the user keeps control, contrasted with agents that take over the editor. ([1:23](https://youtu.be/LRwc64Ui_MQ?t=83))
- **Review agents are defined as plain markdown rule files and run against a PR, instead of waiting for a human reviewer.** — Rules cover formatting, logic issues and security. Prebuilt agents exist, e.g. a security one. Output is PR comments or suggested diffs, and the same agents can run outside the editor with triggers and Slack alerts. ([2:37](https://youtu.be/LRwc64Ui_MQ?t=157))
- **Positioning: Copilot helps you type, Continue helps you ship. The two are presented as complementary, not competitors.** — Suggested combo: Copilot for autocomplete, Continue for checking that code is ready to merge. Continue is said to span PRs, CI and agents, but the video does not demonstrate CI. ([3:57](https://youtu.be/LRwc64Ui_MQ?t=237))

## Techniques
- **Model-agnostic Continue setup** — Install the Continue extension in VS Code (Extensions, search 'continue', install, reload). Open settings and edit the config file, then add a model entry: a cloud model like GPT-4 or Claude with your API key, or a local model: run `ollama pull llama3` and add it under a provider. Save and reload, then switch models from the sidebar dropdown. The exact config file name and keys are not shown in the video. *When:* When you want to switch between paid cloud models and free local models per task without changing tools.
- **Repo-aware explanation of unfamiliar code** — Highlight a block of code, press Ctrl+L, and type 'explain this' in the sidebar chat. Continue adds context from open files and git diffs, so the answer reflects the whole project. *When:* Onboarding to an unfamiliar codebase, or cross-checking your understanding against the actual repo.
- **Review and apply diffs in chat** — Ask for a change (e.g. 'refactor this function'). Continue shows a side-by-side diff preview in the chat. Edit, apply or reject it. *When:* Making refactors where you want to inspect every change before it lands.
- **Markdown-defined PR review agent** — Create a markdown file with the rules you care about (formatting, logic issues, security). Run it from the chat by invoking the agent on a PR. The transcript shows the command as 'agent my agent review and run this PR', but captions make the exact invocation syntax unclear. Prebuilt agents such as a security agent are also available. Results appear as comments or suggested diffs. Agents can be managed and given triggers, and Slack can receive PR alerts. *When:* Adding a consistent first-pass review (style, logic, security) to PRs, especially for solo developers or small teams wanting consistent standards.
- **Split autocomplete and review tools** — Keep GitHub Copilot for inline autocomplete in the editor and use Continue as a separate pre-merge check on the PR. *When:* When you already use Copilot and want an additional review layer without replacing it.

## Numbers
- Claimed setup time: install and get started in under a minute (speaker's claim, not measured). ([3:57](https://youtu.be/LRwc64Ui_MQ?t=237))
- Continue is free when paired with a local Ollama model; cloud models require your own API keys (cost not quantified). ([3:57](https://youtu.be/LRwc64Ui_MQ?t=237))
- No benchmarks, latency, cost or review-quality measurements are presented; video length 4:52. ([0:00](https://youtu.be/LRwc64Ui_MQ?t=0))

## Hot takes
- Copilot helps you type, Continue helps you ship: the speaker positions the tools as complementary, but the video itself makes no case that Continue's review output is better than alternatives.
- The speaker says Claude Code and Cursor can do the codebase-aware explanation too, which weakens the case for Continue as a distinct tool.
- Continue is said to cover PRs, CI and agents, but only the editor chat and PR review agent are shown; CI is asserted, not demonstrated.
- The review-agent-as-markdown-file idea is the most reusable part, and the video gives no evidence on false-positive rates or how well it works on real PRs.

## Tools mentioned
Continue (VS Code extension, open source), GitHub Copilot, VS Code, Ollama, Llama 3 (Llama3), GPT-4, Claude, OpenAI, Slack, Cursor, Claude Code

## Relevance to our work
- **prosharness** (1/3): Defining review criteria as a versioned markdown rule file is a simple pattern that fits a harness wrapping Claude Code; the video shows no checkpointing, critique or multi-agent flow. → *If ProsHarness gets a PR-review or critique step, keep the review criteria in a markdown rules file that is loaded at run time, rather than hard-coding prompts, so it can be edited without code changes.*

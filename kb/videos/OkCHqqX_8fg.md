# Gemini CLI: The FUTURE of Coding is Here (But There's a Catch)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `OkCHqqX_8fg` · [watch](https://youtu.be/OkCHqqX_8fg) · **date:** 2025-11-02 · **length:** 4:46 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed Better Stack presenter · **orgs:** Google, Anthropic, OpenAI, Better Stack
- **topics:** coding-agents, token-cost-efficiency · **tags:** gemini-cli, claude-code, head-to-head, yolo-mode, permission-prompts, agent-looping, GEMINI.md, CLAUDE.md, whisper, react-vite, single-prompt-test

> Head-to-head test of Gemini CLI and Claude Code building the same MP3-to-Whisper transcriber app from one prompt file. Claude Code ran with fewer approval interruptions and tokens; Gemini CLI eventually worked but looped on fixes.

## Summary
The presenter gives a short overview of Gemini CLI, saying it mirrors Claude Code's surface (slash commands, bash mode, @file references, a GEMINI.md file like CLAUDE.md, MCP support) with differences such as /compress instead of /compact and no /init equivalent. He then runs the same task in both tools: each project has a prompt.md asking for a React and Vite app with a drag-and-drop MP3 uploader that transcribes via OpenAI's Whisper model. Claude Code plans, installs the OpenAI SDK with Bun, and after one pasted runtime error produces a working app that transcribes the file. Gemini CLI asks for style preferences and repeatedly requests approvals; yolo mode and "always allow" did not stop the prompts, it did not create a .env file, and it went back and forth on the same file several times before the error was fixed. Both end with a working app, but Gemini CLI took longer and used noticeably more tokens, by the presenter's rough impression. He closes by saying Gemini CLI's 1M-token context window and sandbox mode are not yet enough to switch, and that the promo's image and video generation claims could not be reproduced. The test is a single, unrepeated run with no measurements.

## Key ideas
- **Gemini CLI copies much of Claude Code's surface: slash commands, bash mode, @file references, a project markdown file for context (GEMINI.md vs CLAUDE.md), memory saved there, and MCP support. Differences noted: /compress instead of /compact, and no /init command to generate the file.** — The presenter frames Gemini CLI as open source with a generous free tier. Its context summary command is /compress and it has no automatic file-creation command, but it shows the model and context usage at all times, which he sees as a plus. ([0:00](https://youtu.be/OkCHqqX_8fg?t=0))
- **Same task, same spec file: each tool gets a prompt.md in its own React and Vite project, asking for an MP3 drag-and-drop uploader that sends audio to OpenAI's Whisper for a transcript. This makes the comparison about agent behavior, not the spec.** — Claude Code produced a plan, installed the OpenAI SDK with Bun, and after one pasted runtime error the app ran on localhost and transcribed the test file as requested. ([1:23](https://youtu.be/OkCHqqX_8fg?t=83))
- **Auto-accept settings change how the run feels: the presenter switched Claude Code into auto-accept edits mode (Shift+Enter) to speed up the run, and enabled yolo mode in Gemini CLI to skip questions.** — Gemini CLI still asked for approvals after yolo mode was enabled. Shift+Tab did not help, and the presenter had to approve with 'always allow' several times. ([2:50](https://youtu.be/OkCHqqX_8fg?t=170))
- **Gemini CLI did not generate a .env file for the OpenAI key, while Claude Code did. The presenter had to add the key by hand before the app would run.** — Both tools hit an OpenAI-related runtime error that was fixed by pasting the error back into the agent. Gemini's fix took several rounds of accepted edits to the same file, which the presenter described as going in circles. ([2:50](https://youtu.be/OkCHqqX_8fg?t=170))
- **Outcome: both tools eventually produced a working app that did what was asked. Gemini CLI took longer and used a lot more tokens, though the presenter says this was a rough impression and not a measurement.** — He attributes some of this to Gemini CLI being newly released. Other friction he noted: exiting to change the model, and Ctrl+C not clearing the input. ([2:50](https://youtu.be/OkCHqqX_8fg?t=170))
- **The presenter could not reproduce the promo claims for Gemini CLI image and video generation, and he is not ready to switch. He cites the 1M-token context window and the sandbox mode as not enough reason yet.** — This is a conclusion from a single test, not a broader evaluation. ([4:14](https://youtu.be/OkCHqqX_8fg?t=254))

## Techniques
- **Identical-spec head-to-head test** — Create one project folder per agent with the same prompt.md spec. Give each agent the file, then run the app in the agent's bash mode. Paste any runtime error back into the same agent and count the rounds until the app works. *When:* Comparing coding agents on a small, end-to-end feature when you want behavior (approvals, looping, error recovery, token use) rather than benchmark scores.
- **Auto-accept edits mode in Claude Code** — Press Shift+Enter in Claude Code to switch to auto-accept edits mode before a long run, so edits are not confirmed one by one. *When:* A well-scoped build task where you trust the spec and want fewer approval interruptions.
- **Yolo mode and 'always allow' in Gemini CLI** — Enable yolo mode, then approve a prompt with 'always allow' when it appears. Shift+Tab was tried to stop further prompts and did not work in this run. *When:* Only for trusted, sandboxed runs. Expect repeated approval prompts even after enabling it.
- **Paste-error repair loop** — Copy the runtime error from the running app (for example from the terminal or browser console), paste it into the agent with a request to fix it, and re-run the app. *When:* Fixing a bug that the agent introduced in its own generated code, with a clear reproduction.

## Numbers
- Gemini CLI advertised 1 million token context window (presenter cites it; not measured) ([4:14](https://youtu.be/OkCHqqX_8fg?t=254))
- Gemini CLI run used noticeably more tokens and took longer than Claude Code on the same task (qualitative, no counts given) ([2:50](https://youtu.be/OkCHqqX_8fg?t=170))
- Each tool needed one pasted runtime error fixed before the app worked (single run per tool) ([1:23](https://youtu.be/OkCHqqX_8fg?t=83))
- Video length 4:46 ([0:00](https://youtu.be/OkCHqqX_8fg?t=0))

## Hot takes
- Single unrepeated run per tool with no metrics. The token and speed verdict is a rough impression and should not be read as a benchmark.
- Title promises the 'future of coding' with a 'catch'. Substance is a one-off comparison, so quality is capped at 2.
- The presenter says Gemini CLI's promo claims (image and video generation) could not be reproduced, which is a useful caveat about vendor demos.
- Gemini CLI's approval friction (yolo mode not stopping prompts) and same-file edit looping are presented as early-release problems, not inherent design issues. The presenter does not test whether they persist.

## Tools mentioned
Gemini CLI, Claude Code, OpenAI Whisper, OpenAI SDK, Bun, React, Vite, OpenAI Codex, MCP

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI, so approval handling and edit loops in agent CLIs are the failure modes a harness must manage. This video shows both, but only anecdotally. → *Check how ProsHarness handles 'always allow' and auto-accept approvals, and consider a guard that flags repeated edits to the same file in one fix cycle.*

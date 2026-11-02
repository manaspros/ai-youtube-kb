# GitHub Copilot Agent Mode & Project Padawan – A Game Changer?

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `y3oo7MGo1DA` · [watch](https://youtu.be/y3oo7MGo1DA) · **date:** 2025-11-02 · **length:** 5:53 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** GitHub, Microsoft, Anthropic, Google, OpenAI
- **topics:** coding-agents, software-factory · **tags:** github-copilot, vs-code, agent-mode, copilot-edits, voice-chat, project-padawan, multimodal-input, terminal-agents

> Hands-on walkthrough of GitHub Copilot agent mode and Edits in VS Code, plus a teaser for Project Padawan; the agent runs terminal commands but missed errors and ignored the screenshot, while Claude output matched the target better.

## Summary
The speaker tests GitHub Copilot's agent mode in VS Code by asking it to build a Hacker News clone in Next.js from a screenshot. Agent mode runs terminal commands, streams file edits, and shows a diff with accept/discard, but it runs the dev server from the wrong folder and does not pick up the terminal error when asked. Image attachments fail on Gemini 2 Flash and a previewed Claude model, while GPT-4o accepts the screenshot, though its output ignores the reference's color scheme. A second run in Copilot Edits mode with Claude 3.5 Sonnet, driven by voice chat and a text description, produces a much closer clone. Edits mode is now generally available, with a diff view and undo/redo but no per-snapshot reapply as in Cursor. The video ends with a teaser for Project Padawan, which the speaker describes as assigning a GitHub issue to Copilot for a cloud-sandboxed, tested PR; nothing about it is demonstrated. The evidence is one anecdotal run per model on the free tier.

## Key ideas
- **Copilot agent mode can run terminal commands and stream file edits into the project, with a diff view for accept/discard, which puts it in the same class as Cursor and Windsurf.** — The agent scaffolds the Next.js app via a terminal command, streams its edits into page.tsx, and then offers accept-all or discard on the diff. ([1:15](https://youtu.be/y3oo7MGo1DA?t=75))
- **Screenshot-as-reference depends on the model. Gemini 2 Flash and a previewed Claude model rejected the image attachment; GPT-4o accepted it.** — The speaker treats the failures as likely preview limitations and does not verify this. ([1:15](https://youtu.be/y3oo7MGo1DA?t=75))
- **Agent mode did not use terminal output as feedback. It ran npm from the parent folder, failed, and then did not pick up the error even when the speaker reported it.** — The speaker contrasts this with Cursor, which reads terminal output and can correct the command. ([2:20](https://youtu.be/y3oo7MGo1DA?t=140))
- **The GPT-4o agent run ignored the screenshot's color scheme. The speaker attributes this to the model choice and to agent mode being experimental.** — Single run, not controlled; the speaker expects Claude Sonnet to do better because it is generally stronger at coding. ([2:20](https://youtu.be/y3oo7MGo1DA?t=140))
- **Copilot Edits mode is now generally available. With Claude 3.5 Sonnet and a text description of the target look, the clone was much closer to the reference.** — The speaker used voice chat, and the reply was read aloud, including code blocks, which he found slow and prefers to avoid. ([3:22](https://youtu.be/y3oo7MGo1DA?t=202))
- **Edit review is weaker than Cursor's. There is a diff view and undo/redo of the last edit, but no reapply or scrubbing back to an earlier snapshot.** — The speaker says he would need to press undo several times to return to an earlier state. ([4:28](https://youtu.be/y3oo7MGo1DA?t=268))
- **Project Padawan is teased as an asynchronous issue-to-PR agent. It was not demonstrated and is described only from the announcement.** — Per the speaker: assign an issue to Copilot, it spins up a secure cloud sandbox, opens a tested PR that accounts for issue/PR discussion and repo custom instructions, assigns a human reviewer, and iterates on review feedback. ([4:28](https://youtu.be/y3oo7MGo1DA?t=268))

## Techniques
- **Agent mode for scaffold-and-run tasks** — In the Copilot Chat box, switch the mode dropdown from edit to Agent, choose a model, and send a prompt. The agent runs terminal commands (e.g. the Next.js create command, then the install), streams its edits, and shows a diff with accept/discard. Check the commands it runs and the folder they run in, because it may start the dev server from the parent folder. *When:* Multi-file scaffolding where the agent needs to run commands. Supervise each terminal step rather than spamming Enter through the confirmations.
- **Screenshot as design reference, with a model check** — Attach the reference screenshot to the prompt. Before prompting, confirm the selected model accepts image input (Gemini 2 Flash and a previewed Claude model rejected it in this video; GPT-4o accepted it). If the output drifts from the image, re-prompt with the key style values in words (colors, layout), as the speaker did. *When:* UI cloning or matching an existing design, where a model without image input will fail silently or ignore the reference.
- **Edits mode with voice input (speaker's caveat)** — Start a voice chat in Copilot Edits and dictate the change. The reply is read aloud, including code, so for ordinary use the speaker prefers the text chat. *When:* Hands-free prompting. Expect slow playback of code if the model's reply includes code.
- **Reviewing edits with diff and undo** — Review the streamed diff and accept or discard per change. Use Undo/Redo last edit to step back one edit at a time. There is no reapply or snapshot list in this version (speaker's observation), so for multi-step changes commit or save a checkpoint yourself before the agent edits. *When:* Any agent edit session. Because revert is one step at a time, keep your own checkpoints.
- **Issue-to-PR flow (Padawan, not shown)** — Per the speaker's description of the announcement, you assign a GitHub issue to Copilot. It runs in a cloud sandbox, opens a PR with tests, takes issue and PR discussion plus repo custom instructions into account, assigns a human reviewer, and works through review comments. Nothing was demonstrated, so treat this as a watch item only. *When:* Watch for when it ships. Do not plan around it from this video alone.

## Numbers
- The speaker is on GitHub Copilot's free tier, which he calls 'very generous'. No quota or price is given. ([0:00](https://youtu.be/y3oo7MGo1DA?t=0))
- Two of three models rejected the screenshot attachment (Gemini 2 Flash and a previewed Claude model). GPT-4o accepted it. ([1:15](https://youtu.be/y3oo7MGo1DA?t=75))
- Project Padawan is described as expected 'this year'. No release date is given. ([0:00](https://youtu.be/y3oo7MGo1DA?t=0))

## Hot takes
- Copilot agent mode is not yet a Cursor-class coding agent: it ignored terminal errors and drifted from the reference design in this run (speaker's view, single run).
- Claude 3.5 Sonnet in Edits mode produced a closer clone than the GPT-4o agent-mode run, which the speaker attributes to model quality rather than the mode itself.
- Voice chat in Copilot reads replies aloud, including code, which the speaker finds slow for real work.
- The headline Project Padawan is only announced and not shown, so the title's framing of a 'game changer' outruns the demo; quality is capped at 2 for hype framing and anecdotal single runs.

## Tools mentioned
GitHub Copilot, VS Code, Copilot Agent mode, Copilot Edits, Project Padawan, Cursor, Windsurf, Devin, Claude 3.5 Sonnet, GPT-4o, Gemini 2 Flash, Next.js

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps Claude Code, and the video shows an agent silently dropping a terminal error that was not fed back into the next turn. That is the feedback gap a checkpoint/resume harness should close. → *Verify that ProsHarness passes failed shell and build output back into the next agent turn, and record command failures as explicit loop state so a resumed run sees them.*

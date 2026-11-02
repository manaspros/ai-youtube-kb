# A Code Editor That Actually Scales

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `kCWwrx51IS4` · [watch](https://youtu.be/kCWwrx51IS4) · **date:** 2026-03-02 · **length:** 5:12 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Zed, Cursor, GitHub, Anthropic
- **topics:** dev-tools, coding-agents, claude-code · **tags:** zed, code-editor, rust, agent-client-protocol, acp, claude, cursor, multiplayer, pair-programming, inline-ai-edit

> A short tour of Zed, a Rust editor pitched against Cursor on large-repo speed and real-time multiplayer. The Claude integration via ACP is the headline, but the evidence for speed is anecdotal.

## Summary
Better Stack presents Zed, a Rust-native code editor, as an alternative to Cursor, centred on two claims: it stays fast on large codebases, and it is multiplayer by design. The headline update is Claude integration through the Agent Client Protocol (ACP). AI is optional: inline edits on a selection and an opt-in Claude Code sidebar. The presenter walks through file search, symbol search and repo-wide search, and says results stay instant on a bigger repo. The collaboration section covers channels with real-time cursors, live edits, GitHub invites and voice chat. The video closes by framing the choice as a solo AI-first editor versus a lighter-AI editor with real-time collaboration. Speed is judged by eye on one large JSON file, with no timings or benchmarks. The Cursor comparison is asserted rather than shown, and the video contains no sponsor segment.

## Key ideas
- **Zed is positioned against Cursor on two weaknesses: lag on large projects and a solo-only workflow.** — The headline update is Claude integration through the Agent Client Protocol (ACP), which the presenter says enables better reasoning, cleaner reviews and custom agents without making the editor heavy. ([0:00](https://youtu.be/kCWwrx51IS4?t=0))
- **AI is opt-in rather than always on.** — The presenter contrasts this with Cursor's AI-first design. The editor is Rust-native with no Electron, and speed on large repos is the main pitch. ([0:53](https://youtu.be/kCWwrx51IS4?t=53))
- **Navigation shortcuts are the basic speed demo on large repos.** — Cmd-P opens file search, Cmd-Shift-O opens symbol search in the sidebar, and Cmd-Shift-F runs repo-wide search. The presenter says results stay instant on a bigger repo, with no timings given. ([1:52](https://youtu.be/kCWwrx51IS4?t=112))
- **AI help is applied inline to a selection and stays out of the way.** — Select code, press Ctrl-Enter and ask for a focused change, such as adding error handling or refactoring a function. The suggestion lands at the cursor, with no persistent chat UI. ([2:44](https://youtu.be/kCWwrx51IS4?t=164))
- **A Claude Code sidebar is available on request via Cmd-Shift-A.** — It is off by default and gives a chat-style panel that the presenter compares to Cursor's. ([2:44](https://youtu.be/kCWwrx51IS4?t=164))
- **Channels bring Slack or Discord-style collaboration into the editor.** — Cmd-Shift-C creates a channel and invites teammates from GitHub. Participants get real-time cursors and avatars, live edits and voice chat, which the presenter uses to argue for pair programming, review and joint debugging. ([3:46](https://youtu.be/kCWwrx51IS4?t=226))
- **The closing trade-off is solo AI-first (Cursor) versus light AI plus real-time collaboration (Zed).** — The presenter suggests Zed suits people who are tired of slow, heavy repos or who work with a team. The verdict is stated as a suggestion, not tested. ([4:47](https://youtu.be/kCWwrx51IS4?t=287))

## Techniques
- **Inline AI edit on a selection** — Highlight a block of code and press Ctrl-Enter. Ask for a focused change, such as adding error handling or refactoring one function. The suggestion is inserted at the cursor position, with no chat panel open. *When:* Small, local edits where you want AI help without a sidebar or pop-ups cluttering the editor.
- **Opt-in Claude Code sidebar** — Keep AI off by default. Turn on the Claude Code sidebar with Cmd-Shift-A when you want a chat-style agent panel. *When:* When you want a conversational agent next to the code, but do not want AI UI running all the time.
- **Live collaboration channel for pairing and review** — Press Cmd-Shift-C to create a channel, invite teammates from GitHub and share the project. Participants see each other's cursors and edits in real time and can use voice chat. *When:* Pair programming, reviewing changes together or debugging with a teammate, without moving to an external call and screen-share tool.
- **Keyboard navigation for large repos** — Cmd-P for file search. Cmd-Shift-O for symbol search, shown in the sidebar. Cmd-Shift-F for repo-wide text search. *When:* Navigating large repos where scrolling and hunting for functions or classes is slow.

## Numbers
- Scale claim: no lag on codebases of 100k+ lines, shown by scrolling a large JSON file. No timings or benchmarks given. ([0:53](https://youtu.be/kCWwrx51IS4?t=53))
- Repo-wide and file search described as instant on a bigger repo. No latency measured. ([1:52](https://youtu.be/kCWwrx51IS4?t=112))

## Hot takes
- The title promises a scaling result, but the only performance evidence is subjective scrolling on one large JSON file. There are no timings, repo sizes or comparisons against Cursor.
- The Claude/ACP integration is the only AI product update described. The rest of the AI section is an inline edit and an optional sidebar toggle.
- The claim that Cursor 'still assumes you are working alone' is asserted without a feature comparison or version numbers.
- Real-time multiplayer with voice is the most distinctive claim, but the video shows only the presenter on screen, not a second participant editing live.
- Quality is capped at 2 because the title is hype-driven and the substance is a shallow feature tour.

## Tools mentioned
Zed, Claude (via Agent Client Protocol, ACP), Claude Code (sidebar in Zed, transcript says 'Cloud Code'), Cursor (comparison only), GitHub (invites)

## Relevance to our work
- **prosharness** (1/3): ACP is the editor-to-agent protocol Zed uses to drive Claude. ProsHarness wraps the Claude Code CLI, so the protocol could matter if the harness is ever to run inside editors as well as the terminal. → *Read the Agent Client Protocol spec and check whether ProsHarness's Claude Code wrapper could expose an ACP interface, so one harness serves both the terminal and Zed.*

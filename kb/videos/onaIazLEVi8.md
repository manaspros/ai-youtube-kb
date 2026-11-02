# The Cursor CLI is Actually Good!?

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `onaIazLEVi8` · [watch](https://youtu.be/onaIazLEVi8) · **date:** 2025-11-02 · **length:** 9:15 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Unnamed Better Stack host · **orgs:** Better Stack, Cursor, Anthropic
- **topics:** coding-agents, claude-code · **tags:** cursor-cli, cursor-agent, claude-code, plan-mode, headless-mode, mcp, vim-keybindings, head-to-head, nextjs, sonnet-4, ide-consistency

> Better Stack's hands-on head-to-head of the Cursor CLI beta against Claude Code on the same Sonnet 4 model: Cursor planned and implemented better, and the host recommends it for language coverage, IDE consistency and single-subscription setups.

## Summary
The host, a daily Claude Code and Cursor IDE user, set out to dismiss the Cursor CLI beta but changed his mind after using it. He lists the shared basics: the same MCP servers and models as the IDE, an auto-run mode, /compress, Vim keybindings, a bang prefix for quick shell commands, chat resume, and a headless mode usable in GitHub Actions. The core test used the same Next.js boilerplate and Claude Sonnet 4 in both tools, with a vague prompt to plan a travel booking app UI without writing code. Cursor produced a far more detailed plan, including wireframes drawn in the terminal, while Claude Code's plan was thin. In the implementation step, Cursor split components into separate files and reused the boilerplate's header and theme switcher, and light and dark mode worked. Claude Code put the whole landing page into one page.tsx and ignored the existing header and design system. Weak spots were that Cursor hung on a long-running npm run dev with no background shell, and that the plan-quality gap is unexplained; the host guesses Cursor adds hidden instructions. He closes with four reasons to try it: planning and implementation quality, every language including headless use, consistency with the IDE, and reuse of an existing Cursor account instead of a second subscription.

## Key ideas
- **Cursor CLI shares MCP servers, models and commands with the Cursor IDE, so the CLI and IDE feel consistent.** — The host says setup picks up the IDE's MCP servers, and model choice uses the same models as the IDE. Auto-run is Cursor's yolo mode for tool calls and file creation. ([0:00](https://youtu.be/onaIazLEVi8?t=0))
- **Feature parity with other CLIs is mostly unsurprising.** — Covers /compress to summarize history, Vim toggle, a shell command shortcut, chat listing and resume, and a headless mode that can run in GitHub Actions for things like review bots. ([1:04](https://youtu.be/onaIazLEVi8?t=64))
- **Cursor's plan output was far more detailed than Claude Code's with the same model.** — Given a vague UI-planning prompt on Sonnet 4, Cursor covered user flows, information architecture, navigation, key screens, design tokens, responsive and accessibility strategy, a roadmap, and terminal wireframes. Claude Code's plan covered only a few screens. ([2:25](https://youtu.be/onaIazLEVi8?t=145))
- **Cursor's implementation was organized into separate component files, and it respected the existing boilerplate.** — The search widget went into a new file of about 153 lines. Cursor reused the boilerplate header and theme switcher, and light and dark mode both worked. Claude Code put the entire page into page.tsx and built a second header instead of reusing the existing one. ([3:30](https://youtu.be/onaIazLEVi8?t=210))
- **Cursor's review mode (Ctrl+R) lets you step through generated files and send follow-ups tied to the file you are viewing.** — Pressing I in review mode sends a follow-up prompt that already references the open file, so you don't have to re-tag it with @. The main gap was that a blocking command such as npm run dev stalled the agent, and the host wants a background-shell mode like Claude Code's. ([4:38](https://youtu.be/onaIazLEVi8?t=278))
- **The plan-quality gap is unexplained, and the host guesses Cursor adds hidden pipeline instructions.** — He ran a single pair of prompts on one project and reports no systematic data. He also notes he already keeps rules in his LLM config to stop inline React components, which Cursor followed without being told. ([5:45](https://youtu.be/onaIazLEVi8?t=345))
- **The case for Cursor CLI is mainly about access and consistency, not raw model quality.** — Four reasons: better planning and implementation in this test, agent quality in any language (for example Java or iOS, where VS Code forks are weaker), the same behavior in CLI and IDE, and working on an existing Cursor account with no second subscription. ([7:54](https://youtu.be/onaIazLEVi8?t=474))

## Techniques
- **Plan-only prompt before implementation** — Start with a vague brief such as 'don't write any code, plan out the UI for X' so the agent produces a structured plan (flows, IA, screens, tokens, roadmap). Then send a separate implementation prompt, such as 'now code the landing page', which uses that plan as context. *When:* Use it for greenfield UI work where you want to review direction before code is written and steer any drift early.
- **Shell command from inside the agent chat** — Prefix a command with an exclamation mark in the Cursor CLI prompt, for example !git status, to run a quick non-interactive shell command without leaving the agent session. *When:* Use it for quick checks like git status while the agent is working, instead of asking the model to run them.
- **Headless Cursor agent in CI** — Run the Cursor agent non-interactively from a script or GitHub Actions workflow, for example a code-review job, following the same pattern the host describes for Claude Code. *When:* Use it when you want an automated agent review or task in CI, and your team already pays for Cursor.
- **Review mode with file-scoped follow-ups** — Press Ctrl+R to open review mode and step through the generated files with the arrow keys. Press I on a file to send a follow-up prompt that automatically refers to that file. *When:* Use it to check many generated files quickly and to correct one file without re-tagging it by hand.
- **Rules file to prevent inline React components** — The host keeps rules in his LLM config that tell the model to put header, hero and similar sections in their own component files. Cursor followed this pattern without the rule, and Claude Code did not. *When:* Use it when the agent keeps putting every section in one page file, and a rules file is your main way to correct that.

## Numbers
- Head-to-head used Claude Sonnet 4 in both tools, one vague planning prompt and one 'now code the landing page' prompt. ([2:25](https://youtu.be/onaIazLEVi8?t=145))
- Cursor's search widget was a new component file of about 153 new lines. ([3:30](https://youtu.be/onaIazLEVi8?t=210))
- Claude Code's plan was reviewed in about five seconds of scrolling, with the sections listed as user search, results, booking flow, accounts and trip management. ([3:30](https://youtu.be/onaIazLEVi8?t=210))
- Claude Code wrote the entire landing page into a single page.tsx file. ([5:45](https://youtu.be/onaIazLEVi8?t=345))
- The landing page was built in two prompts total. ([4:38](https://youtu.be/onaIazLEVi8?t=278))

## Hot takes
- Cursor's plan output beat Claude Code's on the same model, which the host attributes to extra pipeline instructions he could not see. This is a single anecdotal test.
- The CLI is more valuable to teams that already pay for Cursor than as a model or agent advance.
- Cursor's lack of a background shell mode is a real gap compared with Claude Code.
- He calls the Cursor agent's UI second only to OpenCode among the CLIs he has used. He admits that is not a fair criterion.

## Tools mentioned
Cursor CLI (beta), Cursor Agent, Cursor IDE, Claude Code, Claude Sonnet 4, Next.js, Better T-Stack, GitHub Actions, OpenCode (mentioned for UI comparison), Vim, npm

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI with a plan, critique and debate pipeline. This video shows that planning output quality varies a lot between coding agents on the same model, and that long-running blocking commands can stall an agent, which matters for checkpoint and resume design. → *When testing the plan stage, compare Claude Code's plan output with a Cursor CLI plan on the same brief, and check whether ProsHarness detects a blocking dev-server command and needs a timeout or background-process path.*

# Claude Code Tutorial: Full Setup, MCP, and Cursor AI Integration (Claude Squad Guide)

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `u-GGktUnSgg` · [watch](https://youtu.be/u-GGktUnSgg) · **date:** 2025-11-02 · **length:** 8:45 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** unnamed AI LABS host · **orgs:** Anthropic, Cursor, OpenAI, GitHub
- **topics:** claude-code, coding-agents, multi-agent · **tags:** claude-code, cursor, claude-squad, tmux, gh-cli, parallel-agents, ide-integration, usage-limits, max-plan, git

> Tutorial on running Claude Code inside Cursor and installing Claude Squad to run several Claude Code instances in tmux; the IDE link fails on camera and the MCP in the title is never covered.

## Summary
A short AI LABS tutorial covering two ways to run Claude Code beyond a plain terminal. The first is the Claude Code extension in Cursor's integrated terminal, which the speaker says automatically shares selected code and lint/syntax errors with the agent. The second is Claude Squad (invoked as cs), a tmux-based tool that hosts several Claude Code instances in one terminal, shown with separate front-end and back-end sessions driven by a shared API spec. The speaker claims Claude Code gives the raw model's full context where Cursor caps it per model, and that it writes to-do lists for larger prompts. He describes the Max plan at $100 per month with a five-hour reset and calls it unlimited, though he also mentions hourly limits. The Claude Squad IDE-connection check fails on camera, which he dismisses as minor. The install walkthrough covers tmux and gh prerequisites, tmux platform support, and the git-repository requirement. Substance is thin: almost no measurements, a hype framing, and no MCP setup despite the title.

## Key ideas
- **Claude Code runs in Cursor through an extension. The speaker says selected code is shared with the agent automatically, and lint and syntax errors are passed along too. He is unsure about console errors.** — Presented as the main benefit of the IDE mode. Claim is the speaker's own, not tested. ([1:06](https://youtu.be/u-GGktUnSgg?t=66))
- **Running Claude Code in Cursor's terminal gives the raw model's full context. The speaker says Cursor limits context per model to save API cost, so the same model gets less context in Cursor.** — Stated as a major advantage. No figures given. ([2:13](https://youtu.be/u-GGktUnSgg?t=133))
- **For a larger build request, Claude Code writes a to-do list up front. The speaker calls this the main reason to use it, since it structures work without the user prompting for it.** — Demo prompt was a single request to build a small HTML, CSS and JS website. ([2:13](https://youtu.be/u-GGktUnSgg?t=133))
- **Claude Squad runs several Claude Code instances side by side in one terminal. Each new instance is created with n, and each can take a different task.** — Speaker names one session for the front end and another for the back end. ([0:00](https://youtu.be/u-GGktUnSgg?t=0))
- **Parallel agents work from a shared contract. The speaker defines the API with blueprints, then gives one instance the spec for the front end while another handles the back end.** — He says a production app would still need a lot of planning. ([4:58](https://youtu.be/u-GGktUnSgg?t=298))
- **The Claude Squad session failed the IDE connection check with 'no available IDEs have been detected'. The speaker says this only blocks a few secondary features.** — Shown live. He says the multi-agent part is the valuable one. ([3:41](https://youtu.be/u-GGktUnSgg?t=221))
- **Cost is the trade-off for parallel agents. The speaker says running several instances is much more expensive and points to the Max plan as the answer.** — Plan details are in the numbers section. He calls the limits unlimited but also says there is an hourly rate limit. ([4:58](https://youtu.be/u-GGktUnSgg?t=298))
- **Claude Squad only works inside a git repository with at least one commit. For an empty folder, the speaker creates a placeholder file, then initializes git and makes a first commit.** — Exact git commands appear on screen, not in the spoken transcript. ([7:05](https://youtu.be/u-GGktUnSgg?t=425))

## Techniques
- **Install Claude Code and open it in Cursor** — Install Claude Code by copying the install command from the official site and running it in a terminal. If you avoid the terminal, ask Cursor's agent to run the install. Open Cursor's integrated terminal and run the Claude Code command. On first connect it installs a 'Claude Code' extension. Then open the command palette, search 'run Claude Code', and press Enter. A Claude Code terminal opens inside Cursor, and the old terminal can be closed. *When:* When you want Claude Code's agent inside an IDE, especially for users who find a plain terminal intimidating.
- **Check the IDE connection from Claude Code** — Inside a Claude Code session, run the IDE connection check command. The speaker runs it and sees the list of Claude Code commands. The exact command name is shown on screen and not spoken. *When:* To confirm the IDE integration (selection and error sharing) is active. It may fail when Claude Code runs under a multiplexer.
- **Install Claude Squad** — Install the prerequisites first: tmux (macOS and Linux only, no Windows build as of the video) and the GitHub CLI (gh). Then run the automated install script from the Claude Squad GitHub README, which installs the tool. Launch it with the command cs. *When:* When you want several Claude Code instances in one terminal on a Unix-like system.
- **Prepare a repository for Claude Squad** — Run cs only inside a folder with git initialized and at least one commit. For an existing project, run git init and make a first commit. For an empty folder, create a placeholder file named ignore.txt, run git init, commit it, then run cs. The exact git commands are on screen. *When:* Before first use, because Claude Squad and Claude Code need a working tree with a commit to detect.
- **Run parallel sessions for front end and back end** — In Claude Squad, press n to start a new Claude Code instance and give it a session name, such as 'front end session'. Write the API blueprint that defines the endpoints first. Give the front-end instance the spec and have it start building. Press n again for a back-end instance and give it its own task. *When:* When a project splits cleanly into two parts with a defined API boundary, such as a front end and back end that talk over an API.
- **One-shot build prompt that yields a to-do list** — Give Claude Code a single, complete build request, such as 'Make a website in HTML, CSS, and JS for ...'. The speaker says it produces a to-do list before it starts. The speaker's example topic was phishing-related, which is not a reference to copy. *When:* For a multi-part build where you want the agent to plan the work first and show it.

## Numbers
- Claude Max plan costs $100 per month and gives much higher usage limits, described as an unlimited token cap that resets every five hours. ([4:58](https://youtu.be/u-GGktUnSgg?t=298))
- Claude Max limits are hourly rate limits, not a monthly quota as on the older Pro plan. The speaker says Opus is included. ([4:58](https://youtu.be/u-GGktUnSgg?t=298))
- Cursor limits per-model context to save API cost. The speaker says Claude Code gets the raw model's context, but gives no number. ([2:13](https://youtu.be/u-GGktUnSgg?t=133))
- Claude Code shows a real-time token counter while it works. No figures are given. ([3:41](https://youtu.be/u-GGktUnSgg?t=221))
- tmux, a Claude Squad prerequisite, runs on macOS and Linux only, not Windows. ([6:23](https://youtu.be/u-GGktUnSgg?t=383))
- No benchmarks, latencies, or measured costs are given in the video. ([8:28](https://youtu.be/u-GGktUnSgg?t=508))

## Hot takes
- The speaker calls multi-agent use with Claude Squad the most valuable part and treats the failed IDE connection as minor.
- The 'unlimited' Max plan claim is contradicted by his own description of hourly rate limits.
- The title promises MCP setup, but the transcript never covers MCP. Quality is capped at 2 because of this and the hype framing.
- The speaker says the Cursor-to-Claude-Code error sharing covers lint and syntax errors, and implies the feature is new, without evidence.
- Claims like 'amazing', 'crazy' and 'honestly pretty amazing' carry no measured content. He found the tool on X.

## Tools mentioned
Claude Code, Cursor, Claude Code extension for Cursor, Claude Squad (cs), tmux, GitHub CLI (gh), git, GitHub, OpenAI Codex, Claude Opus, Claude Max plan, Claude Pro plan, Claude free plan, ignore.txt (placeholder file)

## Relevance to our work
- **prosharness** (2/3): Claude Squad is a comparable harness around Claude Code CLI that manages several concurrent instances in tmux, which overlaps with ProsHarness's loops and multi-run handling. The API-blueprint-as-shared-contract idea also maps to subagent orchestration. → *Read Claude Squad's source to see how it tracks and isolates several Claude Code sessions, and compare it with ProsHarness's checkpoint/resume model for parallel runs.*

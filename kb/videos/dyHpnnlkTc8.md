# Cooking with Agents in VS Code — Liam Hampton, Microsoft

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `dyHpnnlkTc8` · [watch](https://youtu.be/dyHpnnlkTc8) · **date:** 2026-06-18 · **length:** 17:04 · **format:** demo · **quality:** 2/5 · **depth:** intro
- **speakers:** Liam Hampton · **orgs:** Microsoft, GitHub
- **topics:** coding-agents, multi-agent, context-engineering, sandboxing-execution · **tags:** vs-code, github-copilot, copilot-cli, git-worktree, background-agents, cloud-agents, autopilot, custom-agents, agent-skills, awesome-copilot, mcp, playwright, parallel-agents

> A Microsoft product tour of running local, background (worktree) and cloud coding agents side by side in VS Code, with advice on which mode fits which task.

## Summary
Liam Hampton from Microsoft shows how he runs three kinds of GitHub Copilot agents at once inside VS Code: a local agent he watches closely, a background CLI agent in its own Git worktree, and a cloud agent that runs in GitHub Actions. He argues that one-shot prompts do not work and that the choice of agent should follow how hands-on the developer wants to be. He uses a short recorded demo on a small Python product-store app to write tests, add a front end, and write docs in parallel. He then explains cloud-agent safety (isolated runner, network allowlist, no direct push to main) and shows the shared customization layer (custom instructions, custom agents, prompt files, skills, hooks, MCP) that applies across tools. The talk is mostly product walkthrough, with few measured results; the cost question he raises is not answered.

## Key ideas
- **One-shot prompts do not produce finished apps; agent use needs ongoing human steering** — He says people still expect one prompt to build a whole application or fix everything, and that this is not how it works. He ties this to weak ROI on AI spend and to token cost. ([1:04](https://youtu.be/dyHpnnlkTc8?t=64))
- **Three agent modes are chosen by how hands-on the developer wants to be** — Local agents run in VS Code next to the developer for close, human-in-the-loop work. Background agents use the Copilot CLI in an isolated Git worktree and suit a 50-50 split. Cloud agents run remotely and suit work the developer does not want to touch, such as documentation. ([2:10](https://youtu.be/dyHpnnlkTc8?t=130))
- **A Git worktree is a practical isolation unit for parallel agents** — He describes a worktree as a branch mapped to its own folder inside the workspace. Each background agent gets one, so several agents can edit the same repo without colliding. Running the app from a worktree still hit a port conflict. ([2:10](https://youtu.be/dyHpnnlkTc8?t=130))
- **Route each task to the mode that fits it** — Tests go to a local agent because he wants to understand the code. A front-end UI goes to a background agent. Documentation and open-source hygiene files go to a cloud agent. He ran all three on one repo at the same time. ([3:34](https://youtu.be/dyHpnnlkTc8?t=214))
- **Autopilot removes permission prompts, so a pause gate is needed before the PR** — Autopilot (preview) stops the agent from asking for approval on each tool call. He keeps it on for the work but tells the agent to stop before opening a pull request so he can test locally. He warns that this mode can be dangerous and should not be used casually. ([6:26](https://youtu.be/dyHpnnlkTc8?t=386))
- **Cloud agents are isolated by design** — They run in GitHub Actions in an isolated environment, with network firewall allowlisting and no access to the main branch, so they cannot push straight to main. They get extra context through the GitHub and Playwright MCP servers, which lets them run screenshot-based front-end tests. ([11:31](https://youtu.be/dyHpnnlkTc8?t=691))
- **Customization primitives are shared across agent tools** — Custom instructions, custom agents, prompt files, agent skills (which he calls the newer form of AGENTS.md), hooks and MCP servers all live in one VS Code settings surface. He says the same concepts apply to other AI tools, and that Claude plugins and skills can be managed there too. ([12:52](https://youtu.be/dyHpnnlkTc8?t=772))

## Techniques
- **Worktree-per-background-agent** — Give each background agent its own Git worktree (its own branch and folder) so parallel edits do not clash. Review the result in the worktree folder before merging, and watch for port clashes when running the app. *When:* When you want several agents editing one repo at once and each task is big enough to take a while.
- **Route tasks by hands-on level** — Use a local agent for work you want to understand closely, such as writing tests. Use a background agent for work you want to watch but not drive, such as building a UI. Use a cloud agent for work you can hand off fully, such as docs or repo hygiene files. *When:* When planning a day's agent work across several tasks.
- **Plan first, autopilot second, pause before PR** — Ask the agent for a plan on an issue, approve it, then enable autopilot so it does not ask for each tool call. Tell it to stop before opening the pull request so a human can run and test the change. *When:* For multi-step tasks where you trust the plan but still want a human check before the PR.
- **Task-specific custom agents** — Write a custom agent that carries the instructions for one job, such as how to write unit tests for this codebase, and select it when that job comes up. *When:* When the same kind of task recurs and you want the agent to follow a fixed playbook.
- **Cloud agent with MCP and browser testing** — Give the cloud agent the GitHub MCP server and the Playwright MCP server so it can open pull requests and run front-end checks with screenshots, inside a locked-down network. *When:* For hands-off tasks that need to check a UI, not just code.

## Numbers
- Three agents (local, background, cloud) ran at the same time on a single small Python product-store repo, covering tests, a front end, and docs ([10:15](https://youtu.be/dyHpnnlkTc8?t=615))
- Local agent used Claude Opus 4.6 with medium reasoning; he chose it for speed over depth ([7:48](https://youtu.be/dyHpnnlkTc8?t=468))
- The speaker raised cost as a common question about cloud agents but did not give a figure ([11:31](https://youtu.be/dyHpnnlkTc8?t=691))

## Hot takes
- The cloud agent is a good place to hand off documentation: "I hate documentation."
- Token-saving tricks such as a repo that makes the chatbot talk like a pirate are being promoted as serious cost fixes, and the speaker treats that with doubt.

## Tools mentioned
GitHub Copilot, VS Code, GitHub Copilot CLI, Git worktree, GitHub Actions, GitHub MCP server, Playwright MCP server, Microsoft Learn MCP server, awesome-copilot (open-source repo of agent customizations), Claude Opus 4.6 (used for the local agent)

## Relevance to our work
- **prosharness** (2/3): Worktree-per-agent isolation, a pause gate before the PR, and a cloud agent with a locked-down network all overlap with ProsHarness's checkpoint, approval and loop design. → *Compare ProsHarness's checkpoint/resume with running each long run in its own Git worktree, and check whether a 'stop before PR' gate should be a named, phone-approvable checkpoint.*
- **general** (2/3): A clear routing rule for local, background and cloud agents by how hands-on the developer wants to be, plus the point that skills, hooks and MCP sit in one customization layer. → *Write a one-page rule for when to run Claude Code in the foreground, in a worktree, or as a remote task, based on the hands-on routing here.*

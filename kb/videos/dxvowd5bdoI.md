# Warp CLI: Access the Latest AI Models Anywhere For FREE

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `dxvowd5bdoI` · [watch](https://youtu.be/dxvowd5bdoI) · **date:** 2025-11-02 · **length:** 4:47 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Better Stack presenter (not named in transcript) · **orgs:** Warp, Better Stack, OpenCode
- **topics:** coding-agents, mcp-and-tools, dev-tools · **tags:** warp, warp-cli, agent-profiles, saved-prompts, warp-drive, mcp, headless-agent, terminal, wezterm, context7, gpt-5

> A short walkthrough of Warp CLI, which runs Warp's saved prompts, agent profiles and MCP servers from any terminal, including headless one-shot runs for scripts and CI.

## Summary
The presenter introduces Warp CLI, a beta tool that exposes Warp features (saved prompts, saved workflows, agent profiles, MCP servers) to any terminal through a `warp` command family, with a free tier that includes current models. Single-shot runs are done with `warp agent run` and a prompt; each run creates a new conversation ID. Saved prompts, workflows, notebooks and rules from Warp Drive are invoked by their IDs, which are copied from share links, so the same prompts can run in CI, on remote servers, or from bash scripts. Agent profiles pin a model and permissions (the demo uses a profile forced to GPT-5 for planning and execution), and are selected with a profile ID listed by `warp agent profile list`. MCP servers are listed with `warp mcp list` and attached to a run by ID, with the demo using Context7 and Better Stack's MCP server. The presenter concludes that the CLI suits one-off commands, while longer-running agent work still needs the full Warp terminal app, and says the long IDs are unintuitive and that a terminal UI like OpenCode's would be preferable.

## Key ideas
- **Warp CLI brings Warp features to any terminal** — Saved prompts, saved workflows, agent profiles and MCP servers from Warp can be used from WezTerm or any other terminal. The CLI is in beta, so its docs may change. ([0:00](https://youtu.be/dxvowd5bdoI?t=0))
- **Single-shot runs are one command** — `warp agent run` with a prompt flag starts a new conversation and returns the response. Each run gets a fresh conversation ID, which the presenter says makes it best for one-off commands. ([0:00](https://youtu.be/dxvowd5bdoI?t=0))
- **Saved prompts and workflows run by ID** — The ID is taken from the share link of a saved prompt or workflow in Warp Drive. Workflows take arguments written inside angle brackets in the prompt, and notebooks and rules can run the same way. This makes them usable in CI/CD, on remote servers, or chained in a bash file. ([1:24](https://youtu.be/dxvowd5bdoI?t=84))
- **Agent profiles are the only way to set model and permissions** — The CLI cannot change the model or permissions directly. A profile in Warp settings (AI section) pins them, and the demo uses a default profile plus a GPT-5 profile for planning and execution. ([2:45](https://youtu.be/dxvowd5bdoI?t=165))
- **MCP servers attach to a run by ID** — `warp mcp list` shows servers with IDs. A run can attach one with the MCP flag and a prompt, as in the demo that uses Context7 to write a Next.js client component. ([2:45](https://youtu.be/dxvowd5bdoI?t=165))
- **Presenter's verdict: good for one-shot commands, not long runs** — The presenter says the CLI works well for quick tasks, but longer-running work needs the full Warp terminal. The long IDs are unintuitive, and a terminal UI with a model picker and pay-to-unlock model access, like OpenCode and OpenCode Zen, would be preferable. ([4:07](https://youtu.be/dxvowd5bdoI?t=247))

## Techniques
- **Headless one-shot agent run** — Install Warp CLI, then run `warp agent run --prompt "what model is this"` (flag names as spoken in the video; confirm with `warp agent run --help`). Each call opens a new conversation and prints the response. *When:* Quick single questions or commands from a shell, or any step in a script where you do not need a persistent session.
- **Reuse a saved Warp Drive prompt from the CLI** — In the Warp app, copy the share link of a saved prompt and take the ID from its end. Then run `warp agent run` with the saved-prompt flag and that ID. *When:* When the same prompt is maintained in Warp Drive and should run from a server, CI job or script without retyping it.
- **Run a saved workflow with arguments** — Copy the workflow's ID from the end of its link. Run `warp agent run --prompt` with text that names the workflow inside angle brackets and supplies its arguments, e.g. `<workflow-id> arg1 arg2` in the demo's pattern. *When:* Parameterised repeatable tasks, such as processing a file, that already exist as Warp workflows.
- **Pin model and permissions with an agent profile** — Create a profile in Warp settings under AI (the demo uses one forced to GPT-5). Run `warp agent profile list` to get its ID, then run `warp agent run --profile <id> --prompt "..."`. *When:* When a run needs a fixed model or permission set without changing the default for interactive use.
- **Attach an MCP server to a single run** — Run `warp mcp list` to get the server ID, then run `warp agent run` with the MCP flag, the ID and a prompt. The demo uses Context7 to fetch current Next.js docs for a client component. *When:* When one command needs documentation or tools from an MCP server but the default setup should not include it.
- **Chain prompts in a shell script** — Put several `warp agent run` lines (prompts, workflows, notebooks or rules) in one bash file, as the presenter suggests. *When:* Batch automation of several agent steps on a remote machine or in CI, where each step gets its own conversation ID.

## Numbers
- Video length is 4:47. No benchmarks, prices, token counts or latency figures are given. ([0:00](https://youtu.be/dxvowd5bdoI?t=0))
- Free tier is described as generous and includes some of the latest models, but no quota or price is stated. ([0:00](https://youtu.be/dxvowd5bdoI?t=0))

## Hot takes
- Warp CLI is best for single-shot runs, and longer-running agent work still needs the full Warp terminal app (presenter's view).
- Long opaque IDs for prompts and profiles are unintuitive, and a terminal UI with model access on billing would be better (presenter's view).
- Title says 'For FREE', but the free tier is never quantified, and the video is a short beta-feature tour, so quality is capped at 2.

## Tools mentioned
Warp CLI (warp command, beta), Warp agent profiles, Warp Drive (saved prompts, workflows, notebooks, rules), Warp MCP servers, GPT-5, Context7 MCP server, Better Stack MCP server, WezTerm, Ghostty, iTerm, Next.js, OpenCode, OpenCode Zen

## Relevance to our work
- **agentos** (1/3): Profiles that pin a model per run are a simple routing pattern similar to per-request model choice in a gateway, but this is a single-user CLI feature. → *Note that per-profile model pinning and per-run MCP attachment are worth comparing with how AgentOS routes models and tools per request; no change needed now.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI for long runs, loops and schedules. Warp's non-interactive run-by-profile model and its finding that long runs need a full UI are relevant design contrasts. → *Compare ProsHarness's headless run mode with `warp agent run --profile` for scheduled one-shot runs, and check whether its checkpoint/resume covers the long-running case the presenter says Warp CLI cannot handle.*

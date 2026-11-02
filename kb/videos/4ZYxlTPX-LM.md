# These Factory AI Droids Built My App in 10 Minutes! (Rust + TypeScript!) 👉 Code, Debug & Ship Apps

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `4ZYxlTPX-LM` · [watch](https://youtu.be/4ZYxlTPX-LM) · **date:** 2025-11-02 · **length:** 8:29 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** AI LABS host (unnamed) · **orgs:** Factory, OpenAI, Google, Notion, Atlassian (Jira), Linear, Tauri
- **topics:** coding-agents, software-factory, multi-agent · **tags:** factory, droids, tauri, desktop-app, command-approval, auto-accept, model-switching, openai-api, gemini-2.5-pro, gpt-4

> A hands-on tour of Factory's "droids" (role-specialized coding agents) building a Tauri desktop chat app, covering local bridge setup, command approval, and a model-switch debug. Thin on depth; the title overstates it.

## Summary
The host presents Factory, a coding-agent platform whose agents ("droids") each own one responsibility, and walks through a guided tutorial that builds a native desktop app with Tauri (Rust plus TypeScript). Setup connects the cloud agent to the local machine through a desktop "Factory Bridge" app that is paired with a code, and a checklist lets the user choose which commands run without asking. Before each command runs, the agent shows its risk and waits for accept or reject, or the user can enable auto-accept. The agent builds a counter demo, then offers three app options (LLM chat, code review tool, meeting notes summarizer), and the host picks the chat app, which needs an OpenAI API key and exposes model, temperature, max tokens and system prompt settings. After the first test returns off-topic replies, the host switches to Gemini 2.5 Pro, and the problem goes away; the host suspects the earlier GPT-4 selection but says he is not certain of the cause. The video is an unedited product walkthrough with little explanation of how the droids coordinate internally.

## Key ideas
- **Factory positions its product as a team of specialized agents (droids) instead of one general agent, each handling one part of building software.** — The pitch is that the decomposition mirrors how real software teams work. The host does not show how the droids hand off work or coordinate. ([0:00](https://youtu.be/4ZYxlTPX-LM?t=0))
- **Five droids are listed: tutorial, code, product, reliability and knowledge.** — Code writes code; product covers product-level decisions; reliability covers stability and security; knowledge documents the codebase and fetches external docs. The host does not show how each droid's output is checked. ([1:28](https://youtu.be/4ZYxlTPX-LM?t=88))
- **A hosted agent acts on a local machine through a paired desktop bridge app.** — The user copies a pairing code into the Factory Bridge app, which then lets the agent run commands locally. The user can also connect to a remote workspace instead. ([1:28](https://youtu.be/4ZYxlTPX-LM?t=88))
- **Command execution is gated by a per-command checklist and a risk prompt.** — The checklist sets which commands auto-execute. Before any other command runs, the agent shows its risk and the user accepts or rejects it. Auto-accept removes the prompts entirely. The host calls this precise control, which is the most reusable part of the demo. ([2:54](https://youtu.be/4ZYxlTPX-LM?t=174))
- **Setup and the first build are fast, but the demo app is a starter template.** — The agent detects that Rust is installed, clones a tutorial template, installs dependencies, and runs the app. The result is a native desktop window, not a web app, with a counter demo added as the first feature. ([2:54](https://youtu.be/4ZYxlTPX-LM?t=174))
- **A generated LLM chat app is only as good as its configuration and first-run checks.** — The chat app asks for an OpenAI key, and its settings expose model, temperature, max tokens and system prompt. The first test returns off-topic answers. The host attributes the problem to the model he had picked, GPT-4, and says he is not certain; he did not confirm a root cause. ([6:35](https://youtu.be/4ZYxlTPX-LM?t=395))
- **The fix was a model swap rather than a code change.** — Switching to Gemini 2.5 Pro made the bad responses stop. The host notes that the agent's debugging process showed the app code was not at fault. The video ends before any root cause was confirmed. ([6:35](https://youtu.be/4ZYxlTPX-LM?t=395))

## Techniques
- **Role-split agent team** — Give each agent one responsibility (for example code, product, reliability, documentation) and let them pass work between them, rather than asking one general agent to do everything. *When:* Multi-step builds where a single general agent loses track of scope or quality. Useful as a pattern for designing ProsHarness-style multi-role loops.
- **Paired local bridge for hosted agents** — Run the desktop bridge app on the local machine, paste the one-time pairing code into it, and let the hosted agent run commands there. Remote workspaces are the alternative. *When:* When a cloud-hosted agent must operate on files and tools installed on your own machine.
- **Pre-approved command checklist with per-command risk prompts** — Before the first run, pick which command classes auto-execute from the checklist. Anything not on it shows its risk and waits for accept or reject. Auto-accept is the opt-out for the whole session. *When:* Setting how much autonomy an agent gets on a machine. Keep destructive or networked commands gated and allow routine build commands.
- **Live file-diff preview during agent edits** — Keep the preview pane open next to the list of modified files so changes show up as the agent writes them. *When:* Supervising an agent in real time, especially when the first run is unfamiliar.
- **Model-swap triage for a model-dependent bug** — When a built LLM app gives bad output, change the selected model (the video swaps GPT-4 for Gemini 2.5 Pro), re-run the same prompt, and check whether the bad output stops. This is a quick check, not proof of root cause. *When:* Early testing of an LLM-backed app, to tell a model-specific fault from an app bug before reading code.

## Numbers
- Five droids: tutorial, code, product, reliability, knowledge ([1:28](https://youtu.be/4ZYxlTPX-LM?t=88))
- Three example app options offered after the counter demo: LLM chat app, code review tool, meeting notes summarizer ([5:18](https://youtu.be/4ZYxlTPX-LM?t=318))
- Chat app settings: model, temperature, max tokens and system prompt are configurable ([5:18](https://youtu.be/4ZYxlTPX-LM?t=318))
- Model swap used for debugging: GPT-4 to Gemini 2.5 Pro; host says the bad replies stopped, cause not confirmed ([6:35](https://youtu.be/4ZYxlTPX-LM?t=395))
- Video length 8:29; title claims the app was built in 10 minutes ([0:00](https://youtu.be/4ZYxlTPX-LM?t=0))

## Hot takes
- The title's 'built my app in 10 minutes' framing is a hype claim. The video is an 8.5-minute guided tutorial with a starter template and one follow-up app, and it shows no benchmarks or failure rates.
- The host calls the fix a debug, but the actual change was swapping the model. He says he is not sure why the first model failed, so the claim that the app code was not at fault is unverified.
- The closing pitch asks viewers to sponsor the next video and to use super thanks; no sponsor segment appears inside the content. Quality is capped at 2 for thin substance under a hype title.

## Tools mentioned
Factory Droids, Factory Bridge (desktop app), Tauri, Rust, TypeScript, OpenAI API, GPT-4, Gemini 2.5 Pro, Notion (integration named), Jira (integration named), Linear (integration named)

## Relevance to our work
- **prosharness** (1/3): Factory's per-command checklist and accept/reject risk prompts are a simple, visible version of the approval gating ProsHarness handles with phone-driven approvals. → *Compare Factory's command checklist and auto-accept flow with ProsHarness's phone-approval design. Check whether ProsHarness can pre-approve command classes the same way.*

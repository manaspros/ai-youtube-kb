# AI Coding Finally Fixed, New AI Models, Huge Gemini Deal and More!

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `noxDpgSsops` · [watch](https://youtu.be/noxDpgSsops) · **date:** 2025-12-02 · **length:** 9:11 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** AI LABS host (unnamed) · **orgs:** GitHub, Cursor, Google, OpenAI, Pinterest, Anthropic, 1X, Apple, Apify, Design Arena
- **topics:** models-research, coding-agents, pr-code-review · **tags:** GitHub Agent HQ, Cursor 2.0, Composer, multi-agent orchestration, code review agents, plan mode, Gemini 3 Pro, GPT-5.1, Claude for Financial Services, 1X NEO, Siri, news roundup

> AI LABS' first Context Weekly roundup: GitHub Agent HQ as a multi-agent command center, Cursor 2.0 with its Composer model, and assorted model, product and robotics announcements, mostly relayed from press coverage.

## Summary
This is the first Context Weekly episode from AI LABS, a short news roundup of AI announcements from late 2025. The headline item is GitHub's Agent HQ, announced at GitHub Universe 2025, which the host describes as an orchestrator for agents from Claude, OpenAI and Google, with policy controls and code-quality scoring before merge. Cursor 2.0 is the second major item: a new Composer model with a 200k context window, side-by-side comparison of several models on one task, and a native browser with Chrome DevTools integration. The rest is brief: a sponsored Apify segment, an expected Gemini 3 Pro preview, speculation that anonymous Design Arena models are GPT-5.1, a ChatGPT feature for adding context mid-thinking, Anthropic's financial-services features for Claude, the One X NEO home robot, and reported Apple-Google Gemini deal for Siri. The content is announcement-level with no hands-on testing or benchmarks, and several claims are expected or speculative rather than shipped.

## Key ideas
- **GitHub Agent HQ as a single command center for multiple coding agents** — Agent HQ orchestrates agents from different vendors (Claude, OpenAI, Google) inside GitHub, with enterprise admin controls. It was announced at GitHub Universe 2025 and was slated for release in the coming months, so this is an announcement, not a shipped feature. ([0:00](https://youtu.be/noxDpgSsops?t=0))
- **Agent HQ gates agent output with policies and code-quality scoring** — The pitch is that much AI-generated code is not production quality, so Agent HQ adds code review agents, testing features, and policies with quality scoring so only code that passes reaches production. The host presents this as the main point of the announcement. ([0:55](https://youtu.be/noxDpgSsops?t=55))
- **Plan mode asks clarifying questions before dispatching to agents** — Agent HQ's integrated plan mode asks clarifying questions, defines the steps, and then sends structured instructions to each agent. The speaker frames this as making sure agents know exactly what to do. ([0:55](https://youtu.be/noxDpgSsops?t=55))
- **Mission control to assign, track and control agents from web, IDE, mobile or CLI** — Agent HQ also covers branch management and merge-conflict handling, and dashboard metrics for managers. The host extends the idea to non-code repositories for departments such as marketing, sales and finance, each with its own agents. ([0:55](https://youtu.be/noxDpgSsops?t=55))
- **Cursor 2.0 ships the Composer model and multi-model comparison** — Cursor 2.0 introduces its Composer model with a 200k context window and a chat-style agent layout. Users can run several models on the same prompt and compare answers side by side. Cursor claims Composer is both fast and capable, but no benchmark is shown. ([3:28](https://youtu.be/noxDpgSsops?t=208))
- **Native browser and DevTools inside Cursor for in-loop UI fixes** — Cursor's built-in browser shows the running app next to the editor. You can select a misbehaving element and ask Cursor to change it, and Chrome DevTools integration is available inside the editor. ([3:28](https://youtu.be/noxDpgSsops?t=208))
- **Expected near-term model releases: Gemini 3 Pro preview and GPT-5.1** — The host says Gemini 3 Pro preview is planned for November with a reported 1M-token context, alongside a Nano Banana 2 image model. He also reports anonymous models on Design Arena (Cicada, Caterpillar, Chrysalis, Firefly) that he believes are early GPT-5.1 builds, with Firefly reportedly strong at web development. These are rumors and inferences, not confirmed releases. ([4:31](https://youtu.be/noxDpgSsops?t=271))
- **ChatGPT thinking mode can take mid-run context without a restart** — A user can interrupt ChatGPT's thinking mode partway through a long run, such as deep research, add forgotten context, and let it continue. The host presents this as a fix for restarting long reasoning runs. ([5:50](https://youtu.be/noxDpgSsops?t=350))
- **Anthropic adds financial-services features to Claude** — The host describes Claude working with Excel, PDFs and spreadsheets, pulling data from banking databases, ERP systems and CSV or PDF reports, and producing audit, compliance, risk and forecast outputs. The description is high-level and no workflow is demonstrated. ([6:55](https://youtu.be/noxDpgSsops?t=415))
- **1X NEO home humanoid with a personal memory and pre-orders** — NEO is pitched as a household-chores humanoid with a personal memory bank that recalls past interactions and learns skills over time. Pre-orders are open at $20,000 for early buyers, with deliveries scheduled for 2026. ([7:54](https://youtu.be/noxDpgSsops?t=474))

## Techniques
- **Clarify-then-dispatch planning for multiple agents** — Run a plan step that asks clarifying questions and writes out the steps, then send those steps to each agent as structured instructions. This is how the host describes Agent HQ's plan mode, based on the announcement and not on a demo. *When:* Multi-agent tasks where vague instructions cause agents to diverge, such as several agents editing the same repository.
- **Side-by-side model comparison on one prompt** — Send the same task to several models in one chat view and compare the answers and results directly, as Cursor 2.0's agent layout allows. *When:* Choosing a model for a coding or design task, or checking whether a new model beats the current one on your own work.
- **Select-and-ask UI fix loop in a built-in browser** — Run the app in the editor's browser pane, select the element that is wrong, and ask the agent to change it, using DevTools for inspection. *When:* Front-end iteration where visual correctness matters and you would otherwise switch between editor and browser.
- **Mid-reasoning context injection** — Interrupt a long thinking or research run, add the missing context, and let the model continue without restarting. *When:* Long deep-research or reasoning runs where a key detail was left out of the original prompt.

## Numbers
- Cursor Composer context window: 200k tokens ([3:28](https://youtu.be/noxDpgSsops?t=208))
- Gemini 3 Pro expected context window: 1M tokens (expected, not shipped per the speaker) ([4:31](https://youtu.be/noxDpgSsops?t=271))
- 1X NEO early-buyer price: $20,000, deliveries scheduled for 2026 ([7:54](https://youtu.be/noxDpgSsops?t=474))
- Apple to pay Google about $1B per year for a custom Gemini model for Siri ([7:54](https://youtu.be/noxDpgSsops?t=474))
- Reported Siri model size: about 1 trillion parameters (expected) ([7:54](https://youtu.be/noxDpgSsops?t=474))
- Apify challenge prize pool: $1M total (sponsor segment) ([2:23](https://youtu.be/noxDpgSsops?t=143))
- Pinterest Assistant beta: US users aged 18+, with later rollout to other countries ([5:50](https://youtu.be/noxDpgSsops?t=350))

## Hot takes
- Sponsored Apify segment at 2:23 in a news episode. Quality is capped at 2 for that reason as well as the thin substance.
- Nearly every item is relayed from announcements or rumors. Gemini 3 Pro, GPT-5.1, the Siri model size and the Agent HQ release are all expected or speculative, and the host states some of them as likely facts.
- The GPT-5.1 link to the Design Arena mystery models is the host's inference from naming and performance, not a confirmed attribution.
- Claims about Cursor Composer speed and capability are the vendor's, with no benchmark shown in the video.
- Agent HQ is described as a multi-vendor orchestrator but the video does not explain how it works technically or what it costs.

## Tools mentioned
GitHub Agent HQ, Cursor 2.0, Composer (Cursor model), Chrome DevTools, Gemini 3 Pro (preview, expected), Nano Banana 2 (image model, expected), GPT-5.1 (rumored), Design Arena, ChatGPT, Claude (financial services features), Excel, 1X NEO, Siri, Gemini, Apify

## Relevance to our work
- **agentos** (1/3): Agent HQ's policy and quality-scoring gate before merge is a governance pattern similar to AgentOS's budget and policy pillar, but the video gives only an announcement-level description. → *Read GitHub's Agent HQ documentation once it ships and compare its policy gate with AgentOS's governance layer. Do not rely on this video for the details.*
- **prosharness** (1/3): The clarify-then-structured-instructions plan step is close to ProsHarness's plan stage that precedes critique, so it is a useful comparison point. → *Compare Agent HQ's clarifying-question plan step with ProsHarness's plan stage to see whether ProsHarness should ask clarifying questions before the critique step.*

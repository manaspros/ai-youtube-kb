# OpenAI Agent Builder vs Claude: Who Wins Multi-Agent Workflows? (Complete Comparison)

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `sLiVXlIlSBQ` · [watch](https://youtu.be/sLiVXlIlSBQ) · **date:** 2025-11-02 · **length:** 9:43 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** OpenAI, Anthropic, Zapier, Pipedream, n8n, Speechmatics, Spotify
- **topics:** mcp-and-tools, agent-architecture, product-ux, coding-agents · **tags:** openai-agentkit, agent-builder, chatkit, widgets, guardrails, human-in-the-loop, mcp, vector-store, evals, nextjs, claude-code, agents-md

> A walkthrough of OpenAI's AgentKit (Agent Builder, ChatKit, widgets), with a Speechmatics sponsor segment up front; practical for seeing the visual workflow and ChatKit setup, thin as a head-to-head comparison.

## Summary
The presenter introduces OpenAI's AgentKit release: Agent Builder for visual agent workflows, ChatKit for an embeddable chat UI, and widgets for structured in-chat output. He walks through a demo workflow (start node, guardrails, a JSON-output classifier agent, if/else routing to commerce or personal specialist agents, a file-search node, a human approval node, and a drafting agent that fills an email widget). He covers adding MCP servers from OpenAI connectors, Zapier, or Pipedream, and notes that pass/fail evals and step-by-step preview exist before deployment. He then clones OpenAI's ChatKit starter (Next.js plus backend), shows the Playground for theming, and compares the Widget Builder with having Claude generate a widget. He finishes by embedding the chat as a sidebar or full-screen agent, with the agent running on OpenAI's servers. The "who wins" comparison in the title is not really argued; the Claude parts are UI code generation, not the agent runtime.

## Key ideas
- **AgentKit is three pieces: Agent Builder for workflows, ChatKit for a customizable chat UI you can place anywhere, and widgets as structured UI components rendered inside chat.** — The presenter frames Agent Builder as doing only half the job; the front-end chat surface is the other half. ([0:00](https://youtu.be/sLiVXlIlSBQ?t=0))
- **Workflow shape: start node, then guardrails, then a classifier agent with JSON output, then if/else routing to specialist agents.** — The start node stores the user input in conversation history and exposes it as a text variable. The guardrails node runs moderation and jailbreak detection and ends the workflow on failure. The domain selector agent classifies into commerce or personal, and an if/else sends the message to the matching agent. ([0:58](https://youtu.be/sLiVXlIlSBQ?t=58))
- **Output schemas and variable names can be generated from a natural-language prompt inside the builder.** — The presenter asks the classifier to label input as a vehicle and the builder names the output and variables. He contrasts this with n8n, which he says needs much more manual configuration. ([0:58](https://youtu.be/sLiVXlIlSBQ?t=58))
- **A user approval node adds human-in-the-loop gating before a downstream agent acts.** — The reconciliation proposal is approved or rejected by the user. Only on approval does the workflow continue to the drafting agent, which fills an email widget. ([3:31](https://youtu.be/sLiVXlIlSBQ?t=211))
- **The file-search demo returned made-up data, and real use needs a vector store that costs money.** — He says a real file-search node connects to a vector store, and that uploaded data costs roughly 10 cents per GB per day, so large datasets get expensive. ([0:58](https://youtu.be/sLiVXlIlSBQ?t=58))
- **Widget quality depends heavily on the prompt and on giving a design reference.** — The first widget prompt produced a simple card instead of a food-intake tracker. A clearer second prompt worked better. The Widget Builder reproduced a design reference almost exactly, while the Claude-built attempt was weaker. He says the Claude version was HTML and was not built using the agents.md file. ([6:58](https://youtu.be/sLiVXlIlSBQ?t=418))
- **Widgets are React and follow ChatKit theme changes automatically, so UI edits do not need widget rewrites.** — Because widgets are React components, changes to the AgentKit theme carry through. He presents this as a reason coding agents can keep customizing the UI. ([7:49](https://youtu.be/sLiVXlIlSBQ?t=469))
- **Evals and step-by-step preview are built into the builder, and the agent runs on OpenAI's servers.** — Pass/fail criteria are described in natural language before deployment. The preview runs each node. He says the agent is hosted by OpenAI, so there is no runtime to operate, though he does not show the evals running. ([4:34](https://youtu.be/sLiVXlIlSBQ?t=274))

## Techniques
- **Classifier-then-route agent workflow** — Start node, then guardrails node (select moderation and jailbreak checks from a list), then a classifier agent with JSON output format, then an if/else on the classifier's output field that sends the input to a specialist agent. Reference upstream fields in prompts with double curly braces, for example {{employee_query}}. *When:* Multi-intent front doors where one agent should only handle one category, or when the output must be parseable by downstream nodes.
- **Human approval gate in a workflow** — Insert a user approval node after the proposal step. Approve continues to the drafting agent; reject ends or loops back. *When:* Irreversible or outbound actions such as sending an email or reconciling records, where a person must confirm first.
- **Remote MCP server registration per agent** — In an agent's tools section, add official OpenAI connectors, or add a third-party MCP server (Zapier or Pipedream offer several) by pasting its remote server URL and API key. *When:* Giving one agent access to external SaaS tools without writing a client.
- **ChatKit starter quickstart** — Clone OpenAI's open-source ChatKit repo (Next.js with a backend). Run npm install. Create the env file for API keys (the exact command is not spoken in the video). Set the OpenAI API key and the workflow ID from Agent Builder. Run npm run dev. He opened the project in Cursor. *When:* Getting a working embedded chat UI in front of a published Agent Builder workflow fast.
- **Theme via Playground, then hand off to a coding agent** — In the ChatKit Playground, set accent color, font, greeting, start prompts, and toggles for the model picker and tool menu. Export the code and give it to a coding agent to apply. *When:* Matching the chat to an existing brand before writing custom React.
- **Prompt-to-widget, then pin the format in the agent prompt** — Create a widget in the Widget Builder by prompting it. Copy the widget's default values into the agent prompt so the agent always emits that structure. Give a design reference image when you want a close match. *When:* Making the agent return structured UI cards (for example a meeting-prep summary) rather than plain text.
- **Custom widgets with Claude Code and agents.md** — Point the coding agent at the agents.md file from OpenAI's widget docs as context so generated widgets follow the required structure. The presenter says Claude's first attempt without this file was weaker than the Widget Builder output. *When:* Building widgets in code, when you need more control than the Widget Builder gives.

## Numbers
- Vector store storage costs around 10 cents per GB per day, so large datasets are expensive. ([0:58](https://youtu.be/sLiVXlIlSBQ?t=58))
- Sponsor claim: Speechmatics supports 55+ languages with speaker diarization. ([0:58](https://youtu.be/sLiVXlIlSBQ?t=58))
- Video length is 9:43. ([0:00](https://youtu.be/sLiVXlIlSBQ?t=0))

## Hot takes
- The Speechmatics sponsor segment in the first minute caps quality at 2.
- The title promises a comparison of OpenAI vs Claude for multi-agent workflows, but the video only walks through OpenAI's tooling. Claude appears only as the tool for generating UI code, not as an agent runtime.
- Widget-quality verdict rests on one prompt per tool, and the presenter says the Claude attempt did not use agents.md.
- Evals are described but not run on camera, and the agent runtime is hosted by OpenAI, so the demo does not address vendor lock-in.
- The claim that Agent Builder 'solved a lot of problems of other platforms' is asserted, not demonstrated against a comparison.

## Tools mentioned
OpenAI Agent Builder, OpenAI AgentKit, OpenAI ChatKit, ChatKit Playground, OpenAI Widget Builder, OpenAI vector store / file search, OpenAI guardrails node, ChatGPT apps, Zapier (MCP servers), Pipedream (MCP servers), n8n (comparison only), Next.js, npm, Cursor, Claude / Claude Code, agents.md, Speechmatics (sponsor; speaker diarization), PipeCat (sponsor-mentioned integration)

## Relevance to our work
- **agentos** (1/3): Guardrails node (moderation and jailbreak checks) and workflow-level approval are similar to AgentOS's PII and prompt-injection scan, but this is a hosted OpenAI product with no comparison to AgentOS. → *Compare the guardrail checks in OpenAI's guardrails node against the Govrix Scout PII and prompt-injection scan to see which categories are missing on either side.*
- **prosharness** (1/3): The approval node pauses a workflow until a human approves or rejects, which is close to ProsHarness phone-driven approvals, though the video does not describe a notification channel. → *Compare the approve/reject gating in the approval node with ProsHarness phone-driven approvals to check how a rejection path is handled.*

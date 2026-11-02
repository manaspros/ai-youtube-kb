# A Problem You Never Knew About

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `w3pmfaczpLc` · [watch](https://youtu.be/w3pmfaczpLc) · **date:** 2025-12-02 · **length:** 4:34 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Thesis, Vercel
- **topics:** product-ux, mcp-and-tools · **tags:** generative-ui, c1, thesis, react-sdk, structured-output, tool-calls, sponsored, vercel-ai-sdk, claude-skill

> Sponsored demo of Thesis's C1, a generative UI API that turns LLM output into interactive components (forms, tables, dashboards) via a React SDK. Pitch-level; no evaluation data.

## Summary
The video introduces Thesis's C1, a generative UI API that sits between an LLM and the frontend and turns model output into interactive components such as buttons, forms, tables, charts and dashboards. The speaker argues that hard-coded UI breaks whenever model output changes, and that text chat is the default fallback because it is easy to build. C1 is presented as model-agnostic (the demo mentions GPT-5 and Claude); it returns UI instructions as JSON and the C1 React SDK renders them, handling streaming, error boundaries and state. Tool calls are supported, with API or database results rendered as components. Integration is described as two steps: point the backend at Thesis with an API key and a chosen model, then install the SDK and render the output. The demo runs a Vercel AI SDK project with C1 pre-wired, showing a generated welcome panel and a dashboard, plus form fields whose values are sent back as a prompt on submit. The speaker also built a Claude skill with C1 documentation links, and the video closes with a sponsor offer of up to 5 million free tokens. No latency, cost, accuracy or failure-mode data is shown.

## Key ideas
- **Generative UI as an alternative to text chat: model output becomes interactive components (buttons, forms, tables, dashboards) generated per response.** — The speaker's core claim is that AI apps still answer with plain text while models have improved, and that the real cost is the UI code that must be rewritten whenever output shape or use case changes. ([0:00](https://youtu.be/w3pmfaczpLc?t=0))
- **C1 is middleware between the model and the frontend.** — The backend sends the model response to the C1 API, which decides which UI components to produce (table, form, chart, etc.) and returns them as JSON. The C1 React SDK renders that JSON, handling streaming, error boundaries, state and custom components. ([1:08](https://youtu.be/w3pmfaczpLc?t=68))
- **Tool calls are supported: the model fetches data from APIs or databases and C1 renders the structured results.** — The video states that results from model tool use are automatically rendered with suitable components, but shows no code or example for this path. ([1:08](https://youtu.be/w3pmfaczpLc?t=68))
- **Retrofitting an existing AI app is described as two steps.** — Step one: switch the backend endpoint to Thesis, add the Thesis API key and choose a model (GPT-5 or Claude). Step two: install the C1 SDK and change the app to render the returned components. ([2:13](https://youtu.be/w3pmfaczpLc?t=133))
- **Form fields inside generated UI feed back into the conversation.** — Users fill in fields the model generated; on submit, the values are sent as a prompt alongside the submit button, which makes the next turn structured input rather than free text. ([3:18](https://youtu.be/w3pmfaczpLc?t=198))
- **The speaker wrapped C1 docs in a Claude skill so an agent can build with it.** — The skill contains documentation links the agent fetches when building or integrating C1 into an app. The video does not show the skill's contents or how well it worked. ([3:18](https://youtu.be/w3pmfaczpLc?t=198))

## Techniques
- **Generative UI middleware in front of the LLM** — Backend sends the raw model response to the C1 API; C1 returns a JSON UI description; the frontend renders it with the C1 React SDK, which streams updates. Pick the model behind C1 (GPT-5 or Claude named in the video). *When:* Responses are structured (tables, forms, charts, option lists) and hand-written per-use-case rendering code keeps breaking as output changes.
- **Two-step retrofit of an existing AI app** — 1) Point the backend model endpoint at Thesis, add the Thesis API key, select the model. 2) Install the C1 SDK and update the app to render the returned interactive components instead of raw text. Exact endpoint URL and package name are not shown in the video. *When:* Adding interactive output to a chat app that already calls an LLM, without rewriting the model layer.
- **Form submission as the next prompt** — Let the generated UI include input fields; on submit, bundle the field values with the submit action and send them to the model as the next prompt. *When:* Collecting structured user input (choices, parameters) from a chat interface without building separate forms.
- **Documentation skill for coding agents** — Write a Claude skill that lists the vendor's documentation links so the agent can fetch current API docs when integrating the SDK. *When:* Using a coding agent to integrate a fast-changing SDK whose docs the model may not know.

## Numbers
- Sponsor offer: up to 5 million free tokens on Thesis sign-up via the video's link. This is a promotional offer, not a measured benchmark or price. ([3:18](https://youtu.be/w3pmfaczpLc?t=198))
- Integration described as two steps (endpoint and key swap, then SDK install and render). No latency, token-cost or reliability figures are given anywhere in the video. ([2:13](https://youtu.be/w3pmfaczpLc?t=133))

## Hot takes
- Sponsored segment (sign-up link with a token offer), so quality is capped at 2 per rules.
- Title promises a 'problem you never knew about'; the content is a product pitch with a generic problem statement.
- The only evidence is a single demo output; no evaluation of UI correctness, failure modes, or how it behaves when model output is malformed.
- The claim that C1 works with any LLM is shown only with GPT-5 and Claude mentions, and no alternative model is demonstrated.
- Tool-call rendering is asserted without a worked example.

## Tools mentioned
Thesis C1 (generative UI API), C1 React SDK, Vercel AI SDK (transcribed as 'Versal AI SDK'), GPT-5, Claude, Claude skill (custom, for C1)

## Relevance to our work
- **prosharness** (1/3): ProsHarness has phone-driven approvals; generated approval forms are a possible UI pattern, but this video gives no evidence about reliability or how the generated UI is controlled. → *If the approval flow needs richer input than buttons, prototype one approval screen with a generative UI layer and check whether the output is stable across repeated runs before adopting it.*

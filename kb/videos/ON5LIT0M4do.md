# Feedback Loops are All You Need — Mehedi Hassan, Granola

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `ON5LIT0M4do` · [watch](https://youtu.be/ON5LIT0M4do) · **date:** 2026-05-18 · **length:** 10:11 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Mehdi Hassan · **orgs:** Granola
- **topics:** observability, product-ux, testing-verification · **tags:** feedback-loops, llm-tracing, electron, preview-deploys, web-search, cost-control, product-engineering

> Granola's Mehdi Hassan argues that shipping LLM features needs your own tracing, per-PR web previews, and fast feedback loops, not better one-shot prompts.

## Summary
Mehdi Hassan, a product engineer at Granola (a desktop meeting-notes app), argues that a generic one-shot chatbot fails once real users arrive. Web search is not a single line of code: it adds token cost, bloats context, and can degrade overnight when a provider changes. One prompt also cannot serve every role, such as sales, engineering or HR. Granola therefore built its own tracing tool, saving agent tool calls, reasoning and cost to a database and surfacing them in an internal UI that non-engineers can read. To test variants in parallel, they turned the Electron renderer into a web shell with a PR preview link, so coding agents can run the feature and attach screenshots to the PR. The talk's thesis is that the goal is a tight feedback loop, not a better first attempt. The speaker also says they looked at Tauri, saw no major performance gain, and have not switched.

## Key ideas
- **A generic one-shot chatbot breaks on real use cases** — Once users arrive, the chat fails at to-do lists, slow web search, writing emails in the user's style, and coaching, so molding an LLM to one use case is hard. ([1:51](https://youtu.be/ON5LIT0M4do?t=111))
- **Web search is a product problem, not a single tool line** — Token cost and context growth scale badly, and a provider can degrade overnight with no visibility. The speaker wants control over the search path so user experience does not depend on the labs. ([2:55](https://youtu.be/ON5LIT0M4do?t=175))
- **One prompt cannot serve every role** — Sales, engineering and HR want different summary outputs, so output shape has to be tuned per audience rather than with one general prompt. ([4:01](https://youtu.be/ON5LIT0M4do?t=241))
- **Build your own tracing because LLM behavior is a black box** — Granola saves tool calls, search and reasoning trails, and cost to their own database, wrapped around the AI SDK. The UI is built for product, CX and the founder, not only engineers, so no CloudWatch query is needed to see why something failed. ([4:01](https://youtu.be/ON5LIT0M4do?t=241))
- **Per-PR web previews let agents verify their own UI work** — The Electron renderer runs as a web shell deployed by CI for each PR. A coding agent opens the preview, tests the feature, and uploads a screenshot into the PR, and several feature variants can be tried in parallel. ([6:32](https://youtu.be/ON5LIT0M4do?t=392))
- **Abstract the native layer behind web-standard fallbacks** — IPC calls and React-side APIs such as routing, sessions and the query layer fall back to web standards when running in a browser. This keeps the renderer agnostic of Electron. ([7:44](https://youtu.be/ON5LIT0M4do?t=464))
- **The thesis: optimize the feedback loop, not the first shot** — The aim is a tight back-and-forth with the model, so the shipped feature is the result of trying many variants in practice rather than only seeing a Figma mock. ([8:44](https://youtu.be/ON5LIT0M4do?t=524))

## Techniques
- **Home-built LLM tracing store with an internal UI** — Persist each agent run's tool calls, reasoning, search trails and cost to a database, wrap the AI SDK to capture them, and build a UI with data structured for the questions staff ask. OpenTelemetry and SaaS tools are alternatives the speaker mentions but does not compare. *When:* When you need per-step visibility into agent behavior for non-engineers, and building an internal view is cheaper than a SaaS tool that does not fit.
- **Web-shell preview per PR** — Abstract IPC and platform APIs behind web-standard fallbacks so the front end runs in a browser. CI deploys a preview link on each PR. *When:* When the desktop or Electron app blocks parallel testing of variants and reviewers cannot easily run the build.
- **Agent self-verification with screenshot evidence** — After the PR opens, a coding agent (Cursor, as mentioned) runs the preview, exercises the feature, and uploads a screenshot to the PR for human review. *When:* When you want reviewers to see evidence of UI behavior without running the app locally.
- **Own the web search path** — Build or control web search instead of relying on a provider's built-in tool, so cost and degradation can be managed and debugged. *When:* When search is central to the product and provider changes have hurt user experience.

## Numbers
- Speaker's rough estimate that one chat with web search can cost about 10 pence, which is not feasible at millions of users ([2:55](https://youtu.be/ON5LIT0M4do?t=175))
- Electron desktop app allows only one running instance, which blocked parallel variant testing before the web shell ([6:32](https://youtu.be/ON5LIT0M4do?t=392))
- Tauri was tried and gave no major performance gain, which is the metric the team cares about most (no figures given) ([8:44](https://youtu.be/ON5LIT0M4do?t=524))

## Hot takes
- The answer isn't to one-shot better; the goal is a feedback loop that makes the product feel like magic.
- Web search being a single line of code is what the labs want you to believe.
- Founders reading raw agent loops front to back is a legitimate debugging practice.

## Tools mentioned
Electron, Cursor, AI SDK, CloudWatch, OpenTelemetry, Tauri, Figma

## Relevance to our work
- **agentos** (1/3): Internal trace store plus a non-engineer UI overlaps with the L4 observability layer, but the talk is a product-team anecdote with no benchmarks. → *Sketch a minimal per-tool-call trace table (args, reasoning, cost) for the L4 observability layer and test whether a plain internal view answers debugging questions faster than Prometheus/Grafana alone.*
- **prosharness** (1/3): The harness runs Claude Code on long jobs. Attaching screenshot or test evidence to each checkpoint is a small idea from the talk. → *Have the harness attach a test log or screenshot artifact to each checkpoint so an approval step can review evidence without a rerun.*
- **general** (1/3): Useful as a product-engineering framing: prefer a fast verify loop over a better first prompt, and make variant testing cheap through previews. → *Read the talk's point about per-PR preview links with agent-run tests as a pattern for any agent-written UI change in our own projects.*

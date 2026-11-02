# MCP Apps: Give the Model Data, Give the User a UI — Dustin Mihalik, Indeed

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `lbaXnx0KLA8` · [watch](https://youtu.be/lbaXnx0KLA8) · **date:** 2026-09-18 · **length:** 15:34 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Dustin Mihalik · **orgs:** Indeed, Anthropic, OpenAI
- **topics:** mcp-and-tools, product-ux, context-engineering · **tags:** mcp-apps, render-tool, tool-descriptions, structured-content, separation-of-data-and-ui, update-model-context, indeed, careerscout, claude, chatgpt, apps-sdk

> Dustin Mihalik (Indeed) shares lessons from building MCP Apps for Claude and ChatGPT: model-visible data parity, separate data from rendering, and feeding UI interactions back to the model.

## Summary
Mihalik, who works on AI platform guardrails and gateways at Indeed, argues that an MCP app is more than a UI dropped into a chat. The first problem is branding and links: without tuning, Claude lists jobs as plain text with no links, so Indeed used MCP Apps to add apply buttons and detail modals. The main failure mode is a naive app that renders HTML while calling existing APIs, which leaves the model blind to what the user sees. His fix is to return structured data alongside the UI resource, keep them in sync, and tell the model in the tool description that results appear in the UI. He also reports that user interactions need to go back to the model through the update-model-context method. His top rule is to separate data processing (text search tools the model can call freely) from UI rendering (a render tool that takes IDs), so the model can explore a large result set and then show only a few items. He closes with the advice to design around data first and keep tools small and composable. The talk is short and based on experience across two vendors, and it gives no benchmarks.

## Key ideas
- **Anything shown in the MCP app UI must also be returned to the model as data.** — A naive app that injects HTML and calls existing APIs is a black box, so follow-ups like 'tell me about the first result' fail. Return structured content next to the UI resource URI, and keep the two in sync whenever the API changes. ([3:57](https://youtu.be/lbaXnx0KLA8?t=237))
- **Without tuning, the model re-describes UI output in text, which causes a clash between the app and the model.** — After the app displays results, the model still narrates them again. Steer this with the tool description, for example by saying results are shown as UI components above. ([5:17](https://youtu.be/lbaXnx0KLA8?t=317))
- **User interactions in the app are invisible to the model unless you send them back.** — Clicking a job or opening a details modal leaves the model unaware of which item is selected. Use the update-model-context method to pass state back. Because it takes a single string, append events over time. ([6:39](https://youtu.be/lbaXnx0KLA8?t=399))
- **Separate data processing from UI rendering. This rule overrides the others.** — Keep the search tools as plain text tools that the model can call many times. Add a render tool that takes a list of IDs, so the model can search, filter and then display only the few results it picked. Without this, Claude calls the UI tool once per query and produces many carousels. ([9:27](https://youtu.be/lbaXnx0KLA8?t=567))
- **Designing an MCP app starts with deciding what data the model should see and explore. UI is the result of that.** — Mihalik says this reverses the usual instinct of starting from the UI. Data exposure and model exploration come first, and rendering follows from them. ([13:09](https://youtu.be/lbaXnx0KLA8?t=789))
- **Render tools can accept model-written content, such as a reason for each pick or a highlighted section of a job description.** — This lets the model add commentary inside the UI, which is a richer experience than a fixed render. ([13:09](https://youtu.be/lbaXnx0KLA8?t=789))
- **Use small composable tools, with simple descriptions that say which tool to call first.** — Build two or three search tools and one or two render tools, and keep each description short so the model is not overloaded. The description also tells the model where the render data comes from. ([14:33](https://youtu.be/lbaXnx0KLA8?t=873))

## Techniques
- **Model-visible data parity** — Return structured content alongside the MCP app's UI resource URI, and update both whenever the underlying API changes. *When:* Any MCP app that shows data the model should be able to reason about or act on.
- **Description steering of UI vs text output** — Write into the tool description that results are displayed as UI above, and that the model should summarize briefly instead of repeating the list. *When:* The model narrates or re-tables data that the app already displays.
- **Explore/render split** — Expose plain-text search tools with no UI, plus a render tool that accepts IDs (or full data). The description says which tool supplies the render data and in what format. *When:* The model must filter a large result set and show only a few items, such as job or product search.
- **Interaction feedback via update model context** — Use the update-model-context method to send user actions (selections, opened items, cart changes) to the model as a string, appending events over time. *When:* The user acts inside the app and later questions should refer to what they did.
- **Render tools that take model-generated rationale** — Add optional input fields to the render tool, such as a reason per ID or a highlighted span, and render them in the UI. *When:* You want the model's justifications or highlights inside the app.
- **Small composable tool set** — Use several narrow search tools and one or two render tools with short descriptions, rather than one large tool. *When:* Several data sources or many possible views need to be exposed without overloading the model.

## Numbers
- Claude runs 10 to 15 separate searches for one multi-city job query and then builds a table; with an MCP app it calls the UI tool once instead. ([8:00](https://youtu.be/lbaXnx0KLA8?t=480))
- Example flow: search across many jobs (about 100 candidates), filter them, and render the best 5 through a render-by-ID tool. ([10:27](https://youtu.be/lbaXnx0KLA8?t=627))
- Indeed spent a lot of eval effort to get Claude to link to jobs consistently, and says this was hard to get right ('ridiculous number of hours'). No figure is given. ([1:10](https://youtu.be/lbaXnx0KLA8?t=70))

## Hot takes
- A naive MCP app that injects HTML and calls existing APIs is a black box for the model.
- Data processing and UI rendering should be split into separate tools, and this rule overrides the others.
- Design an MCP app starting from the data the model should explore, not from the UI.
- Tool descriptions are the main control for whether the model narrates the UI or lets it speak for itself.

## Tools mentioned
MCP Apps, Apps SDK (OpenAI), update-model-context method, Claude, ChatGPT, CareerScout (Indeed internal agent)

## Relevance to our work
- **agentos** (1/3): AgentOS exposes tool and agent surfaces, but the talk is about MCP app UIs in third-party chat clients. The only overlap is the principle that any UI output needs a matching data path for the model. → *If AgentOS ever adds a UI for budgets or audit logs, return the same data as structured content and check it against the model's view before shipping.*
- **prosharness** (1/3): Phone-driven approvals are a UI surface over harness state. Keeping approval data and the user's decisions visible to the model matches the talk's rule. → *If approvals move into an MCP app, return the pending approval data as structured content and send each decision back through update-model-context.*

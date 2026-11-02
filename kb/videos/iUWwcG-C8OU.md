# Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `iUWwcG-C8OU` · [watch](https://youtu.be/iUWwcG-C8OU) · **date:** 2026-06-18 · **length:** 19:06 · **format:** demo · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Garrett Galow · **orgs:** WorkOS, Cursor, Anthropic, OpenAI
- **topics:** data-engineering, agent-architecture, context-engineering, enterprise-adoption · **tags:** internal-tools, text-to-sql, self-serve-analytics, widgets, generated-code-artifacts, tool-context-injection, org-connectors, langgraph, convex, snowflake, claude-opus, slack-bot

> WorkOS product lead Garrett Galow demos Studio, an internal agent that answers business questions and turns repeat questions into live widgets. Main lessons: pre-flight checks, runtime tool context, query validation, and keeping the LLM out of widget refresh.

## Summary
Garrett Galow, who runs product at WorkOS, describes Studio, an internal workspace where non-engineers ask business questions in plain language and get answers from Snowflake, Linear and Notion. The agent runs on Claude Opus inside a LangGraph-style loop, reached through a Slack bot or internal dashboard, with state kept in Convex. When a question recurs, the agent builds a "widget": sandbox JavaScript that makes the API and SQL calls and renders a UI, which anyone can rerun without involving the LLM. The talk's practical lessons are to run pre-flight checks and ask clarifying questions before choosing tools, inject tool-specific schema context only when a tool is invoked, layer prompts (base, defaults, org rules, per-tool), and validate that generated queries return data before they are hardcoded. The team skips RAG, runs the same evals in staging and production, and is moving from per-user integrations to org-level connectors with role-based default access. The talk is partly a product showcase, but the design lessons are concrete and reusable.

## Key ideas
- **Business questions create a bottleneck** — Non-technical teams need SQL or an engineer to answer one-off questions, which turns into back-and-forth in Slack. Rigid dashboards need a rebuild for each new question. Studio lets people answer and build tools themselves. ([1:06](https://youtu.be/iUWwcG-C8OU?t=66))
- **Architecture: agent, guidance layer, integration proxy** — Requests come from a Slack bot or internal dashboard, then go through an API to an agent graph that uses Opus. Tools connect through an integration proxy to Snowflake, Linear and Notion. A guidance layer defines how to query the data and what context is needed. State is stored in Convex so sessions persist. ([3:56](https://youtu.be/iUWwcG-C8OU?t=236))
- **Widgets: LLM-written code that is reusable and reliable** — A widget is sandbox code that combines UI, API calls and queries. It is declarative, so refreshing reruns the queries without the LLM. The LLM only runs again when someone asks for a change, so cost is paid per new question, not per view. ([6:25](https://youtu.be/iUWwcG-C8OU?t=385))
- **Sequencing: pre-flight checks, then clarify** — Before acting, the agent checks that tools are connected and that it has enough context. If not, it asks clarifying questions, then works through a checklist to choose tools. ([10:12](https://youtu.be/iUWwcG-C8OU?t=612))
- **Inject tool context at call time, not up front** — Long Snowflake context (schema, how to join teams to resources) is added only when the Snowflake tool is invoked. The speaker argues that preloading all tool context fills the context window. ([10:12](https://youtu.be/iUWwcG-C8OU?t=612))
- **Validate queries before hardcoding them** — Generated SQL can be valid and still return zero rows. The agent runs each query, checks for data, and only then writes it into a widget. Evals run in both staging and production, using the same path. ([11:14](https://youtu.be/iUWwcG-C8OU?t=674))
- **No RAG, and encode domain traps in context** — They call tools directly with a context block and no retrieval database. The context covers join paths and filter columns such as non-deleted or active status, which prevents common mistakes like a bare count-group-by that ignores status. ([13:41](https://youtu.be/iUWwcG-C8OU?t=821))

## Techniques
- **Generated declarative widgets** — The agent writes sandbox JavaScript that makes the same API and query calls to the data tools, with UI on top. The artifact is saved, so refresh runs the code without the LLM. Changes go back through the LLM. *When:* A question recurs and needs a shared, live tool that many people will reuse or refresh.
- **Pre-flight checks and clarifying questions** — Before tool use, check that connectors work and the request has enough context. If not, ask the user. Then pick tools from a checklist. *When:* Agents face ambiguous business questions across several data sources.
- **Runtime tool-context injection** — Keep tool-specific schema and usage guidance out of the base prompt. Attach it when the agent decides to call that tool. *When:* Tool documentation is long, such as a large warehouse schema, and would crowd out the context window if loaded up front.
- **Layered prompts** — Stack a base system prompt, product defaults, org rules, and per-tool context, and keep the layers separate so edits to one tool keep its context. *When:* Several teams or tools share one agent and need different rules.
- **Distrust model priors for product facts** — Tell the model to check primary docs for product-specific facts instead of relying on training data, because the product changes quickly. *When:* The product or APIs change faster than model training data.
- **Execute-and-validate before deploy** — Run each generated query and check for non-empty results. Only then save it into the dashboard or widget. *When:* Generated SQL can be syntactically valid but semantically empty or wrong.
- **Org-level connectors with role-based defaults** — One admin sets up the connection for the org. Access defaults are set by rule (for example read-only), and higher access is granted by app role. This avoids per-user OAuth for every employee. *When:* Many employees need access to the same SaaS data sources and per-user logins are a burden.

## Numbers
- Customer-to-users entity join in Snowflake is about 4 joins deep, which new hires have to copy and paste until the context block covers it ([12:37](https://youtu.be/iUWwcG-C8OU?t=757))
- Hit rate for generated cross-list queries is described as 'very, very high', with no figure given ([13:41](https://youtu.be/iUWwcG-C8OU?t=821))
- Model choice: Opus is kept because the speaker says cheaper models would trade off quality in a way they would not accept. No cost figures are given ([16:29](https://youtu.be/iUWwcG-C8OU?t=989))

## Hot takes
- RAG is not needed when the agent calls tools directly and gets the right context block.
- Generated widgets should be code that runs without the LLM. Paying for an LLM on every view is the wrong design.
- Spend on the best model for question-answering (Opus), because quality matters more than per-question cost.

## Tools mentioned
Snowflake, Linear, Notion, Convex, LangGraph, Claude Opus, Slack bot, Retool, WorkOS Pipes

## Relevance to our work
- **agentos** (1/3): The widget pattern (LLM writes code once, then runs without the LLM) is related to SkillForge's goal of turning telemetry into reusable skills. The talk gives no measured results for this. → *When designing SkillForge output, consider storing each learned skill as deterministic code that is validated against real data before it is saved, rather than as a prompt that reruns the LLM every time.*
- **prosharness** (1/3): The pre-flight step (check connectors and context, ask clarifying questions, then choose tools) and layered prompts are relevant to how ProsHarness starts a run. → *Add a pre-flight stage to ProsHarness runs that checks that the Claude Code CLI, skills and credentials are ready, and asks for clarification if the task is underspecified, before any plan step starts.*

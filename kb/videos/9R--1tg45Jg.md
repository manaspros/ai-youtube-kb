# Build-Time vs. Run-Time: Why Dev Tools Fail in Production — Averi Kitsch & Prerna Kakkar, Google

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `9R--1tg45Jg` · [watch](https://youtu.be/9R--1tg45Jg) · **date:** 2026-09-18 · **length:** 20:26 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Averi Kitsch, Prerna Kakkar · **orgs:** Google, Google Cloud
- **topics:** security-guardrails, mcp-and-tools, data-engineering · **tags:** mcp, mcp-toolbox, database-access, confused-deputy, lethal-trifecta, least-privilege, identity-aware-tools, prepared-statements, text-to-sql, tool-design, read-write-split, zero-trust

> Google's MCP Toolbox team on separating dev-time from production agent tools. Keep credentials, raw SQL and user identity out of agent control, and use predefined, identity-bound, read-only tools.

## Summary
Two Google engineers (MCP Toolbox for Databases and EvalBench) argue that developer-assistant database tools, such as NL-to-SQL and admin/control-plane tools, should not be reused in production agents. They describe the "lethal trifecta" (private data, untrusted content, and an exfiltration path) and the confused-deputy attack that follows when an agent holds broad credentials. Their fix moves connection details into a server-side source config, uses predefined parameterized SQL as custom tools, and splits identity into user, application and agent. User identity is then bound to tools either by the app or by validating a signed token inside the tool. They close with tool-design advice: outcome-level tools, read/write separation, actionable errors and flat inputs. The live demos failed, so the talk rests on slides and claims without demo evidence.

## Key ideas
- **Dev-time and production tools are different categories.** — Build-time tools (NL-to-SQL, admin/control-plane tools that create instances or databases) suit developer assistants and need a human in the loop. A demo of a build-time tool deleted everything because there were no guardrails. Production end-user agents should use deterministic, predefined tools instead. ([4:19](https://youtu.be/9R--1tg45Jg?t=259))
- **The lethal trifecta enables confused-deputy data breaches.** — A breach happens when one agent has private data, untrusted content, and a way to send data back out. The speaker's example: a malicious ticket asks the triage agent to pull salary data and post it back to the ticket. The agent uses its own privileges, so the user never needed access. ([8:32](https://youtu.be/9R--1tg45Jg?t=512))
- **Separate user, application and agent identities.** — The user should only reach the application. The application's workload identity can be broader. The agent should only get the data the end user is allowed to see. This separation is what makes the breach above hard. ([11:11](https://youtu.be/9R--1tg45Jg?t=671))
- **Split tool parameters into agent-controlled and application-controlled.** — Agent parameters are untrusted inputs the model derives. Application parameters are factual constraints, such as user ID or connection details, that the model must not control. Traditional apps had few input fields, so this split was easier before agents. ([11:11](https://youtu.be/9R--1tg45Jg?t=671))
- **Move connection details into a server-side source config and make the source least-privilege.** — In Toolbox, a YAML source holds the host, port and credentials and is injected when the MCP server starts. The agent never sees them. Source-level controls include read-only at the driver level (the most-requested feature), dataset allowlists, and output-size caps to limit blast radius. ([12:35](https://youtu.be/9R--1tg45Jg?t=755))
- **Bind user identity to tools so the agent never sees PII.** — Bounded parameters: the app authenticates the user and binds the value to the tool. Authenticated parameters: the tool receives a signed token (OIDC or JWT), validates it, and extracts claims such as user ID, email and issuer. In both cases the agent cannot change the identity. ([17:25](https://youtu.be/9R--1tg45Jg?t=1045))
- **Design tools around outcomes, not REST endpoints.** — Use custom tools with fixed, parameterized SQL, typed parameters and prepared statements. Give them clear names and descriptions, since those guide the agent. Keep the description free of parameter detail the schema already carries. Separate read and write tools so reads can be auto-approved and writes need confirmation. Return actionable, retryable errors instead of a bare 404, and use flat, simple inputs instead of complex maps. ([14:57](https://youtu.be/9R--1tg45Jg?t=897))

## Techniques
- **Source primitive for connection secrets** — Define DB host, port, credentials and any read-only or dataset limits in a server-side YAML source. Start the MCP server with it so the agent only ever sends a tool call, never a connection string. *When:* Any agent that touches a production database, especially when the model's context could be manipulated by untrusted content.
- **Predefined custom SQL tools** — Write each allowed query once in config with a tool name and description, use prepared statements with typed parameters, and expose only those parameters to the agent. *When:* Production user journeys where the query set is known in advance, such as order cancellation or flight lookup. Use NL-to-SQL only for exploratory or developer use.
- **Read-only enforcement at the driver level** — Remove write tools, and also restrict the database connection to read-only queries so a prompt-injected write cannot pass through. *When:* Any user journey that only needs to read data.
- **Blast-radius limits on sources** — Use dataset allowlists where the database supports them, and cap output size so one agent call cannot pull or overwhelm the database or context. *When:* Agents with access to large or multi-tenant datasets.
- **Bounded and authenticated parameters for identity** — Bounded: the app binds the user ID to the tool after login, and the agent never sees it. Authenticated: the tool validates the incoming signed token and reads the user claims itself. *When:* Any tool that needs PII or user-scoped data, such as booking flights for a specific user.
- **Read/write tool split with approval gates** — Keep read and write as separate tools. Auto-approve reads, and route writes to the user for confirmation. *When:* Any agent with mutating tools, such as cancelling orders or changing bookings.
- **Actionable, retryable tool errors and flat inputs** — Return error messages that say what to fix or retry, rather than a generic HTTP status. Make inputs flat and simple rather than nested maps. *When:* Any tool an agent calls repeatedly. The speaker says this improves reliability.

## Numbers
- MCP Toolbox for Databases has about 15.7K GitHub stars. ([1:16](https://youtu.be/9R--1tg45Jg?t=76))
- 132+ active contributors and support for 40+ databases. ([1:16](https://youtu.be/9R--1tg45Jg?t=76))
- About 20 million tool calls last month across the managed MCP and MCP Toolbox. ([2:37](https://youtu.be/9R--1tg45Jg?t=157))

## Hot takes
- Your database is only as secure as your agent.
- Confused-deputy attacks make agent-held database credentials the main risk; treat the agent as untrusted.
- Build-time developer tools should not be reused as production runtime tools without guardrails.
- Generic HTTP errors are a missed opportunity, since capable agents can act on actionable errors.

## Tools mentioned
MCP Toolbox for Databases, Google Managed MCP, Model Armor, EvalBench, LangChain, Gemini CLI, Claude Code

## Relevance to our work
- **general** (2/3): The tool-design guidance (outcome-level tools, read/write split, actionable errors, flat inputs, identity bound outside the model) applies to any agent tool work. → *Write a short tool-design checklist from this talk (outcome tools, read/write split, actionable errors, flat inputs, identity outside the model) and apply it to the next agent tool added.*
- **agentos** (1/3): The talk's source-level controls (secrets outside the agent, read-only, output caps) apply to any AgentOS tool that touches a database, but AgentOS is a proxy and does not run DB tools directly. → *When designing AgentOS tool/connector configs, keep DB credentials in server-side config and add read-only and output-size caps at the source level.*
- **prosharness** (1/3): ProsHarness already handles credentials with zero tokens. The source-primitive idea of keeping secrets out of agent-visible parameters is a useful check against that design. → *Verify that ProsHarness tool signatures never accept credentials or user identity from the model, and that they are injected server-side.*

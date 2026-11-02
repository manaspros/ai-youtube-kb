# Human-in-the-Loop Automation with n8n — Liam McGarrigle

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `tDArkCqjA-c` · [watch](https://youtu.be/tDArkCqjA-c) · **date:** 2026-05-18 · **length:** 1:19:22 · **format:** workshop · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Liam McGarrigle · **orgs:** n8n
- **topics:** security-guardrails, agent-architecture, mcp-and-tools, context-engineering · **tags:** n8n, human-in-the-loop, approval-gate, tool-calling, tool-descriptions, gmail, google-calendar, openrouter, slack, mcp, sub-agents, workflow-automation, no-code

> Workshop on building a Gmail and Google Calendar agent in n8n, then gating sensitive tool calls behind human approval steps that the model cannot skip.

## Summary
Liam McGarrigle of n8n walks through building a small email and calendar agent in n8n's visual builder. The agent gets Gmail and Calendar nodes as tools, and each tool exposes only the fields the builder declares. Sensitive actions such as sending email or creating events sit behind a human review node that intercepts the tool call before it runs. The model is not told the gate exists in the mechanical sense, so it cannot skip it. Tool names and descriptions are the only per-call context the model sees, so the speaker keeps behavioural rules inside tool descriptions rather than one central system prompt. He also covers memory windows, injecting the current date, and debugging through the execution log. The second half covers extensions: waiting approvals with timeouts, approvals for channels with no buttons, sub-agents as tools, and exposing workflows over MCP. Much of the talk is a product demo, but the approval-gate pattern and its edge cases are concrete.

## Key ideas
- **Put the human gate on the tool, not in the prompt** — The review step sits between the agent and the tool. The model calls the tool, the gate intercepts it, and the tool cannot run until a person approves. The speaker says the model does not need to know the gate exists, and that prompt-only instructions are weaker. ([42:09](https://youtu.be/tDArkCqjA-c?t=2529))
- **Scope tools field by field** — Each tool parameter is declared separately, so the model can only set the fields the builder exposes. The speaker contrasts this with a coding agent given broad API access, where the model can do anything the API allows. The cost is more setup work per field. ([25:54](https://youtu.be/tDArkCqjA-c?t=1554))
- **Tool descriptions are the per-tool prompt** — The node name becomes the tool name and the description is sent with every LLM call. The speaker keeps email style rules in the email tool's description, not in the central system message, so the tool and its rules can be copied between agents. ([28:40](https://youtu.be/tDArkCqjA-c?t=1720))
- **Fix wrong arguments with per-field descriptions** — When the model fills a field wrongly, add a description to that field. Google Calendar's API calls the event title 'summary', so the model wrote a summary of the event. A description saying this is the title fixed it, and the field key can also be renamed. ([36:30](https://youtu.be/tDArkCqjA-c?t=2190))
- **Tell the model a human is reviewing** — Models hold back from acting when they expect an action to go out unreviewed. The speaker adds a line to the tool description saying the message will not send automatically and a human is in the loop, which stops the model from stalling. ([43:20](https://youtu.be/tDArkCqjA-c?t=2600))
- **Approval waits should be durable and visible** — A waiting approval pauses the run as a wait state and resumes after the decision. The execution log records when the wait started and stopped, so approval delays can be measured from the logs. ([1:03:14](https://youtu.be/tDArkCqjA-c?t=3794))
- **Bound the wait with an auto-deny timeout** — Without a limit, approvals nobody answers pile up. The speaker suggests auto-denying after a set time, such as 10 minutes. He was unsure whether waiting executions count against a self-hosted concurrency limit and said he would follow up. ([1:09:15](https://youtu.be/tDArkCqjA-c?t=4155))
- **Approve through a sub-workflow when there are no buttons** — For a phone call or any channel with no buttons, the LLM cannot be allowed to approve itself. The speaker's answer is a separate confirm sub-workflow that asks the person, returns true or false, and branches on an if node, exposed to the agent as a tool. ([1:15:30](https://youtu.be/tDArkCqjA-c?t=4530))
- **Sub-agents as tools, each with its own model** — Specialised agents, such as calendar, email or GitHub, are exposed as tools to a main agent. Each sub-agent can use a different model and has a smaller context, so the main agent's context does not grow with every domain. ([1:17:59](https://youtu.be/tDArkCqjA-c?t=4679))
- **Inject the current time instead of asking the model for it** — LLMs usually do not know today's date, so a query for today's emails can return results from years ago. The speaker passes the current date and time into the prompt with an expression. ([32:23](https://youtu.be/tDArkCqjA-c?t=1943))

## Techniques
- **Approval gate in front of sensitive tools** — Place a human review node on the edge in front of each side-effecting tool, such as send email or create event. Offer approve, decline and optionally a free-text decline. Leave read-only or low-stakes tools, such as archive, ungated. The gate sits in the tool path, so the model cannot skip it. *When:* Any agent that sends messages, writes calendar or CRM records, or takes other irreversible actions on a user's behalf.
- **Free-text decline as feedback** — Instead of a button, the reviewer types a reply. The reply counts as a denial and the agent retries with that reply as context, for example asking for markdown-free output. The speaker notes the model still favoured the tool description over the correction. *When:* Quick corrections in chat, when a reviewer wants the agent to try again rather than abort.
- **Dry runs with dummy data before real accounts** — Test the agent with dummy events and recipients, then decline the gated action so nothing is sent. The execution log shows which tools ran and with what inputs. *When:* Before connecting an agent to a real inbox or calendar, or when changing a tool's prompt or fields.
- **Rules in tool descriptions, not one system prompt** — Put behavioural rules for a tool, such as tone, placeholder bans and approval notes, in that tool's description. Keep the central system prompt for role and general behaviour. Each tool then carries its own rules when copied to another agent. *When:* Multi-tool agents where rules differ per tool and tools are reused across agents.
- **Per-field descriptions for argument mistakes** — When the model fills a field wrongly, add a description to that field saying what it means. Rename the key if the API name is misleading. *When:* A tool gets the wrong value in one field, typically because the upstream API name is confusing.
- **Wait with an auto-deny timeout** — Set the approval wait to expire after a fixed time and deny automatically. This stops unanswered approvals from building up indefinitely. *When:* Any human-in-the-loop flow where the reviewer may not respond, especially in self-hosted setups with concurrency limits.
- **Confirm sub-workflow as a tool** — Wrap the approval in a sub-workflow that asks the person through any channel and returns true or false. The agent calls it as a tool, and an if node branches on the result. The LLM never sets the answer. *When:* Channels with no buttons, such as voice calls or SMS, where the approval must still come from a human.
- **Sub-agent per domain as a tool** — Build each specialised agent as its own workflow with its own model and tools. Expose each one to a parent agent as a tool so the parent's context stays small. *When:* When one agent covers several domains, or when different domains need different models for cost or quality.
- **Date and time injection via expression** — Insert the current date and time into the system prompt or tool input with an expression, so the model does not guess the date. *When:* Any agent that answers questions about schedules, deadlines or recent events.
- **Memory window sizing** — The simple memory window in the demo was 5 messages. The speaker suggests about 50 for chat, since longer windows cost more tokens on every call. A database-backed memory can be used if the chat history must be read outside the agent. *When:* Chat agents where conversation length varies and token cost matters.

## Numbers
- n8n founded in 2019, before ChatGPT, as an integration tool ([9:04](https://youtu.be/tDArkCqjA-c?t=544))
- Latest stable n8n version at the time: 2.14.2 ([4:58](https://youtu.be/tDArkCqjA-c?t=298))
- Demo simple memory window set to 5 messages; speaker suggests about 50 for longer chats, and notes you pay tokens for all past messages ([18:32](https://youtu.be/tDArkCqjA-c?t=1112))
- Example approval wait timeout: auto-deny after 10 minutes ([1:09:15](https://youtu.be/tDArkCqjA-c?t=4155))
- Workshop length about 1 hour 19 minutes including Q&A ([0:00](https://youtu.be/tDArkCqjA-c?t=0))

## Hot takes
- Giving a coding agent direct access to a calendar lets it do whatever it wants, whereas per-field tools limit it to the fields you set.
- Destructive or sensitive actions should always go through a human review step, while low-stakes actions like archiving can stay autonomous.
- Models will avoid sending without asking unless the tool description says a human is in the loop.
- Visual workflow builders are a good fit for agents because you can see what an agent did and fix it, which the speaker calls where the winners will be.

## Tools mentioned
n8n, OpenRouter, Gmail, Google Calendar, Slack, Notion, Postgres, Redis, Claude, Claude Code, Luxon, Swagger

## Relevance to our work
- **agentos** (2/3): Exec-gate guardrails in Crucible need a way to hold a sensitive tool call for a human decision. The talk's interception layer, timeout and free-text deny address that directly. → *Put an approval hold in front of exec-gate-flagged tool calls: the model cannot bypass it, the hold auto-denies after a timeout, and a typed reply counts as a deny with feedback.*
- **prosharness** (2/3): Phone-driven approvals are already a planned feature. The talk shows the gate pattern, timeout behaviour and the open concurrency question directly. → *Model phone approvals as a gate in front of side-effecting tool calls, with a wait timeout that auto-denies, a typed decline that feeds back into the next attempt, and a check on whether paused runs count against limits.*

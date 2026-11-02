# Why Every Claude Code User Needs To Try AgentMail (Not Gmail)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `U3TXAdpmvVk` · [watch](https://youtu.be/U3TXAdpmvVk) · **date:** 2026-04-02 · **length:** 6:18 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Better Stack, AgentMail, Anthropic
- **topics:** mcp-and-tools, claude-code, agent-architecture · **tags:** agentmail, agent-email, agent-inbox, cli-over-mcp, claude-code-loop, claude-sdk, polling-agent, haiku, vendor-demo

> Better Stack walkthrough of AgentMail, an email-inbox API for agents, shown through the CLI in Claude Code and a 30-second polling reply agent built on the Claude SDK. Mostly a demo, with no benchmarks.

## Summary
The presenter introduces AgentMail, an API platform that gives an AI agent its own email address and inbox, with a Python and TypeScript SDK, an MCP server, and a CLI with a skill. Setup is an account, an inbox, and an API key exported as a shell environment variable, after which the CLI and skill work from Claude Code with a natural-language prompt. The demo has the agent send itself a list of matcha spots, sign up for a newsletter and complete the verification, and summarize forwarded emails. The presenter argues that inboxes per agent are cheap and can be created and deleted on demand. For frequent checks he says Claude Code's loop feature is limited to three days, so he builds a small custom agent with the Claude SDK that polls the inbox every 30 seconds, reads unread messages, generates a reply with Haiku, and handles threads. He lists features he did not show (WebSockets for streaming events, pods for per-customer isolation, IMAP/SMTP). The video is a single-vendor walkthrough with no comparisons or measurements, and its core claim, that Gmail is worse for agents, is asserted rather than shown.

## Key ideas
- **Agents need their own email identity; Gmail was built for humans, so an agent's experience there is worse** — AgentMail provides an inbox per agent with send, receive, read and act. The presenter's central claim is that a Gmail account driven through an MCP server is a weaker fit for agents. He does not test that claim against alternatives. ([0:00](https://youtu.be/U3TXAdpmvVk?t=0))
- **Setup is an account, an inbox, an API key in the shell environment, and the CLI plus the agent-mail skill, with no MCP config** — The presenter prefers CLIs over MCP servers for Claude Code. He contrasts this setup favorably with the Google Workspace CLI setup from his previous video. The skill is installed so the prompt does not have to name the tool. ([0:58](https://youtu.be/U3TXAdpmvVk?t=58))
- **Once the CLI and skill are installed, plain-language prompts in Claude Code drive the inbox** — Asking which inboxes exist loads the skill, which runs the CLI. The agent can send mail to the user's personal address, subscribe to newsletters, complete verification, and summarize forwarded mail. ([1:30](https://youtu.be/U3TXAdpmvVk?t=90))
- **Multiple inboxes per agent, created and deleted on demand, are cheap because billing is not per inbox** — Suggested splits are one inbox per agent (Claude Code, Codex, Gemini CLI), per purpose (subscriptions, customer support), or an agent creating an inbox for a task and deleting it afterward. Routing a message from one inbox to another based on its content is also possible. ([2:22](https://youtu.be/U3TXAdpmvVk?t=142))
- **Claude Code's loop feature can poll for mail, but it expires after three days, so frequent polling needs a custom agent** — The presenter used a Claude Code loop to check every minute and summarize new mail, which he calls a reasonable use. For long-running or more frequent polling he says to build a small agent with the Claude SDK. ([3:25](https://youtu.be/U3TXAdpmvVk?t=205))
- **A minimal polling reply agent: poll every 30 seconds, filter unread messages by received time, generate a reply with Haiku, then send it** — The script reads every message in the inbox, checks the unread label, and passes new messages to a generateReply function. That function builds a user prompt, sends it to Haiku with a system prompt, and returns the reply. The code was not walked through in detail. ([3:25](https://youtu.be/U3TXAdpmvVk?t=205))
- **Threads are handled as context: a follow-up reply is answered with the whole thread, not just the newest message** — The agent accepted a second message asking for a joke about cats and answered it after the 30-second wait, using the three-message thread as context. The presenter notes it was a fast demo, so there is no latency or cost measurement. ([4:47](https://youtu.be/U3TXAdpmvVk?t=287))
- **Production features are out of scope for the video: WebSockets for streaming events, pods for per-customer data isolation, and IMAP/SMTP** — The presenter says WebSockets would give near-zero-latency email checks instead of polling. Pods are for products that give AgentMail infrastructure to their own users. IMAP/SMTP support is also mentioned. ([4:47](https://youtu.be/U3TXAdpmvVk?t=287))

## Techniques
- **Give each agent its own inbox via CLI + skill, not an MCP server** — Create an inbox in the AgentMail dashboard, export the API key as a shell environment variable, install the AgentMail CLI and its agent-mail skill, then use natural-language prompts in Claude Code. The video does not show exact commands, flags or the variable name. *When:* Interactive or personal Claude Code use where an agent needs to send, receive or summarize mail. The presenter prefers this to an MCP server, but he gives no token or reliability comparison.
- **Split inboxes by purpose or by agent** — Create separate inboxes for each agent (for example Claude Code, Codex, Gemini CLI) and for each function (subscriptions, support). Create an inbox when a task starts and delete it when it finishes. Route messages between inboxes based on content. *When:* When several agents or workflows need separate sender identities, audit trails or clean-up. The video says inboxes are not billed individually.
- **Poll for mail with a Claude Code loop for short-lived checks** — Use Claude Code's loop feature to check the inbox on an interval (the presenter used one minute) and summarize new messages. The presenter says loops expire after three days. *When:* Short sessions or personal monitoring. For anything that must run longer, move to a custom agent.
- **Custom polling reply agent on the Claude SDK** — Run a script that polls the inbox every 30 seconds from start. For each message, check the unread label and the received time, then pass it to a generateReply function that builds a user prompt and calls Haiku with a fixed system prompt. Send the reply back into the same thread so the next poll includes the full thread. The video does not show the SDK calls. *When:* Auto-responders or triage agents that need a short, predictable loop. The presenter notes that WebSockets would remove the need for polling.

## Numbers
- Agent polls its inbox every 30 seconds from script start ([3:25](https://youtu.be/U3TXAdpmvVk?t=205))
- Claude Code loops are limited to three days (stated by the presenter) ([3:25](https://youtu.be/U3TXAdpmvVk?t=205))
- Inbox at start of demo already held 16 messages ([4:47](https://youtu.be/U3TXAdpmvVk?t=287))
- Thread test: a 3-message thread was processed and answered after the 30-second wait ([4:47](https://youtu.be/U3TXAdpmvVk?t=287))
- Free plan uses an AgentMail-hosted domain; custom domains require a paid plan ([0:58](https://youtu.be/U3TXAdpmvVk?t=58))
- Inboxes are not billed per inbox (qualitative, no price given) ([2:22](https://youtu.be/U3TXAdpmvVk?t=142))

## Hot takes
- Gmail is a poor fit for agents because it was built for humans. Asserted, not tested.
- CLIs are preferred over MCP servers for Claude Code. Stated as preference, with no measured comparison.
- Title says every Claude Code user needs this. The video is a single-vendor demo with no comparison to alternatives.
- The vendor is not disclosed as a sponsor, and the closing plug is for the presenter's own Electron video.

## Tools mentioned
AgentMail (API, dashboard, CLI, skill, MCP server, Python and TypeScript SDKs), Claude Code (loop feature, skills), Claude SDK, Claude Haiku, Google Workspace CLI (mentioned, previous video), Gmail, Codex, Gemini CLI, Electron (transcript says "Electrobon"; desktop app framework, mentioned only)

## Relevance to our work
- **agentos** (1/3): An agent-owned inbox is a new outbound and inbound tool surface. Its send path would need the same PII and prompt-injection scanning AgentOS applies elsewhere. → *If AgentOS ever gives agents mailboxes, route send actions through the proxy's PII and prompt-injection scan and log them in the audit trail.*
- **prosharness** (1/3): ProsHarness has phone-driven approvals and loops. Email is an alternative approval channel, and a polling loop is an alternative to a push channel. → *Compare email (polled, with a three-day loop limit noted in the video) against the current phone approval path for approval requests and replies.*

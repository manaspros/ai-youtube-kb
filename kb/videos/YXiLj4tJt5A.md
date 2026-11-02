# Agent Speedrun — Elizabeth Fuentes Leone & Sandhya Subramani, AWS

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `YXiLj4tJt5A` · [watch](https://youtu.be/YXiLj4tJt5A) · **date:** 2026-10-12 · **length:** 59:55 · **format:** workshop · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Elizabeth Fuentes Leone, Sandhya Subramani · **orgs:** AWS, Strands Agents, Amazon Bedrock, Amazon Bedrock AgentCore
- **topics:** agent-architecture, security-guardrails, skills-self-improvement, mcp-and-tools · **tags:** strands-agents, agentcore, hooks, steering, skills, rate-limiting, guardrails, deployment, observability, bedrock, workshop

> Hands-on AWS workshop: build a Strands customer-service agent with hooks (rate limit, deterministic blocks), lazy-loaded skills, steering guardrails, then deploy to AgentCore Runtime.

## Summary
Two AWS speakers run a hands-on workshop (about 60 minutes) that builds a customer-service agent with Strands Agents, an open-source agent harness. They start with a basic loop of system prompt, model and tools, then inspect the message history and token counts. The middle section adds hooks, which run deterministic Python at lifecycle points, with a per-request rate limiter capping tool calls at three as the worked example. Skills are markdown procedures that the agent loads only when a question needs them, which keeps the system prompt small. Steering adds a "buddy" check, either a rule handler or a small LLM checker, that corrects output format and tone before a reply is sent. The last part deploys the same code to Amazon Bedrock AgentCore Runtime with one entrypoint decorator, and gets memory, sessions and observability from the platform. The talk is mostly a walkthrough with light product pitching, and the code-level patterns are the useful part.

## Key ideas
- **An agent is a loop: the LLM picks tools, tool results ground the answer in a source of truth** — Tools (decorated Python functions) let the agent act on data such as orders and refunds. The speaker says the point is to avoid relying on the model's base knowledge. The agent decides when to call each tool. ([17:36](https://youtu.be/YXiLj4tJt5A?t=1056))
- **A harness lets you swap models without rewriting the system prompt** — The agent is just system prompt + model + tools, so the same boilerplate can run against different models and be compared directly. ([18:39](https://youtu.be/YXiLj4tJt5A?t=1119))
- **Hooks give deterministic control at lifecycle points; prompts are only suggestions** — Hooks can run before invocation, after the LLM call, before a tool call, or after tool execution, and can approve or cancel each step. The speaker contrasts this with prompt instructions, which are probabilistic. ([26:13](https://youtu.be/YXiLj4tJt5A?t=1573))
- **Concrete hook: a per-request tool-call cap of three** — A counter resets on each new user request (BeforeInvocation) and increments on each tool call (BeforeToolCall). When the cap is hit, the tool call is blocked. In the demo the LLM keeps looping after blocks, so ending the turn needs an explicit hook action. ([28:32](https://youtu.be/YXiLj4tJt5A?t=1712))
- **Block sensitive input before the model sees it, to save tokens and avoid leaks** — A deterministic check on the user message (example: card numbers) can stop the request before any model call, so no tokens are spent and the model never receives the data. An after-call hook can also suppress a reply. ([31:08](https://youtu.be/YXiLj4tJt5A?t=1868))
- **Skills: load procedures on demand instead of stuffing the system prompt** — Each procedure (refunds, order tracking, account troubleshooting) is a markdown file exposed through a skills plugin. The agent reads only the relevant one, so input tokens are not spent on unused knowledge. ([35:29](https://youtu.be/YXiLj4tJt5A?t=2129))
- **Steering: a buddy checker corrects output before it is sent** — Steering handlers run at hook-like points and can be rule-based, type-enforcing, or another agent. Examples given: enforce a structured output format, tell the agent to look something up before a refund, or rewrite a message's tone (no overpromising, acknowledge frustration). ([36:37](https://youtu.be/YXiLj4tJt5A?t=2197))
- **Steering rules can be kept in a database, so changing them does not require a code change** — The speaker describes an open-source agent-control library that expresses steering rules, such as limiting bookings to a set number of rooms, and stores them in a database the agent queries at run time. ([44:57](https://youtu.be/YXiLj4tJt5A?t=2697))
- **Deploying to AgentCore Runtime needs one decorator; memory and observability come from the platform** — The only code change is an entrypoint decorator (garbled in the transcript as MPP entry point). Sessions can run from 15 minutes to 8 hours. Observability must be enabled in the console (transaction search) before traces show in CloudWatch. The speaker says IAM policies and infrastructure are generated by the platform via CDK/CloudFormation. ([47:36](https://youtu.be/YXiLj4tJt5A?t=2856))

## Techniques
- **Per-request tool-call rate limiter via hooks** — Register a BeforeInvocation callback that resets a counter to zero and a BeforeToolCall callback that increments it and blocks once it passes max_calls. Expose max_calls as a constructor parameter. *When:* When the model may loop on tools and token spend or tool side effects must be capped hard.
- **Deterministic input filter hook** — Run plain Python on the user message before the model call. If it matches a rule (for example card-number patterns), block it and return a canned response, so no model call is made. *When:* For PII, restricted topics, or any policy that must not depend on the model following a prompt.
- **Skills as on-demand markdown procedures** — Write one markdown file per procedure, register the folder as a skills plugin next to the system prompt, and let the agent pick which skill to load for a given question. *When:* When domain knowledge is large and used only for some questions, to keep the system prompt small.
- **Steering handler (rule or LLM buddy)** — Define a handler with rules in plain language, optionally with a small checker agent. Attach it at points such as after-model or before-tool, and use type enforcement when the output must match a schema. *When:* When output format, tone or required lookups must hold in production and prompt wording is not reliable enough.
- **Externalised steering rules** — Store rules in a database and have the agent fetch them at invocation, so edits take effect without redeploying code. *When:* When rules change often or should be editable by non-engineers.
- **Message-history inspection** — Print agent.messages to see user, assistant and tool-call turns plus token metrics per run, and use multi-turn chat.py variants to test conversational behaviour. *When:* To debug loops, see which tools fired, and measure per-request token cost before adding controls.

## Numbers
- AgentCore Runtime sessions last from 15 minutes up to 8 hours, with short-term memory built into the runtime ([2:42](https://youtu.be/YXiLj4tJt5A?t=162))
- Basic agent with tools and a multi-turn chat loop is under about 60 lines of code ([24:52](https://youtu.be/YXiLj4tJt5A?t=1492))
- Rate limiter demo caps tool calls at 3 per user request; the test drops the cap to 2 to show blocking ([28:32](https://youtu.be/YXiLj4tJt5A?t=1712))
- Workshop enabled for about 250 participants, with the environment open for about two to three more days after the session ([7:57](https://youtu.be/YXiLj4tJt5A?t=477))
- Deployment to AgentCore Runtime takes about one minute in the demo ([55:10](https://youtu.be/YXiLj4tJt5A?t=3310))
- Workshop accounts come with about 20 AWS credits, and AgentCore is described as cheap for small tests ([14:51](https://youtu.be/YXiLj4tJt5A?t=891))

## Hot takes
- A prompt is only a suggestion; a hook is deterministic code and should be used for hard guardrails.
- Blocking sensitive input before the model call saves tokens, and the model never sees the data.
- Skills loaded only when needed are better than putting all knowledge in the system prompt, because unused context is wasted input tokens.
- Steering with a buddy checker is the answer to format and tone drift in production, and removes the need to keep re-prompting.
- On AgentCore, teams no longer need to hand-write IAM policies or infrastructure for the agent runtime.

## Tools mentioned
Strands Agents, Amazon Bedrock AgentCore (Runtime, Memory, Gateway, Observability), Amazon Bedrock, Amazon CloudWatch, AWS CDK / CloudFormation, AWS OpenTelemetry Distro, boto3, agent-control (open-source steering rules library), MCP, A2A, Jupyter / Workshop Studio

## Relevance to our work
- **agentos** (2/3): Hooks are a deterministic pre-model and pre-tool check, the same idea as the L1 budget and PII scan. The talk also shows blocking before the model call saves tokens, which AgentOS could use. → *Compare the placement of the L1 PII/prompt-injection scan with a before-invocation hook design, and test whether blocking sensitive input before the model call saves measurable tokens on a sample of requests.*
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI with loops and approvals. A per-request tool-call cap and a deterministic block hook map directly to its loop-control and approval needs. → *Prototype a pre-tool-call hook in ProsHarness that counts tool calls per request, hard-stops at a configurable cap, and logs each block to the checkpoint.*
- **general** (1/3): Skills-as-markdown loaded on demand is a compact pattern for context engineering, and the steering-with-checker pattern is a cheap-model guardrail. → *Read the Strands hooks and steering docs as a reference design for guardrail APIs before writing our own.*

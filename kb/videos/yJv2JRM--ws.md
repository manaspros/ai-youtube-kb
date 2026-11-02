# I'm Never Vibe Coding Without Next JS Agents Anymore

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `yJv2JRM--ws` · [watch](https://youtu.be/yJv2JRM--ws) · **date:** 2025-11-02 · **length:** 8:41 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Supabase, ShadCN, TweakCN, Stripe, OpenAI
- **topics:** mcp-and-tools, coding-agents, vibe-coding-app-building · **tags:** vibe-coding, nextjs, mcp, claude-code, supabase, stripe, shadcn-ui, tweakcn, prd, payments, auth

> A walkthrough of building a full-stack Next.js agent marketplace with Claude Code and three MCP servers (Supabase, ShadCN, Stripe), driven by a PRD and per-MCP prompts. The reusable parts live in linked resources, not on screen.

## Summary
The speaker wants to turn a coding agent (Claude Code, with Cursor noted as an alternative) into a builder of full Next.js apps with login, roles and payments. He connects three MCP servers in one Claude Code project: Supabase for the backend, the ShadCN MCP for frontend components, and Stripe for payments. Each connection is one command with a personal access token or restricted key, and he checks it with the /mcp command. He brainstorms the app in ChatGPT, turns the result into a PRD, and writes a converter prompt per MCP that rewrites PRD requirements into that MCP's instructions. He builds in one session, in order: backend, then frontend on the running backend, then Stripe. Claude Code turns each prompt into a to-do list. The frontend starts static, a second to-do list wires it to the backend, and Stripe is first set up as a mock and then replaced with real checkout. The video ends with a click-through demo of login, cart, checkout and the Stripe dashboard, with no measurements, failure cases or tests shown.

## Key ideas
- **A coding agent plus MCP servers can build a full-stack Next.js app from prompts alone, with backend, frontend and payments each handled by an MCP.** — The speaker says the agent can handle login, roles and payment processing without manual dashboard configuration, and that the same approach works with any agent, naming Claude Code and Cursor. ([0:00](https://youtu.be/yJv2JRM--ws?t=0))
- **Each hosted-service MCP is connected with one command and checked with /mcp.** — Supabase needs a personal access token from account settings and Stripe needs a restricted API key, both pasted into the command from the video's resources. The /mcp slash command in Claude Code then shows whether each server connected. ([1:12](https://youtu.be/yJv2JRM--ws?t=72))
- **A PRD is the source of truth, and per-MCP converter prompts translate it into each server's instructions.** — The idea is brainstormed in ChatGPT, compiled into a PRD, and then converted into a separate prompt for each MCP so each one gets instructions it can act on. The converter prompts are shared in the description, not shown in the video. ([3:21](https://youtu.be/yJv2JRM--ws?t=201))
- **Build in dependency order in one session, not in parallel.** — Backend (Supabase) comes first, then the frontend built against the running backend, then Stripe. Claude Code makes a to-do list from each prompt and works through it step by step. ([4:02](https://youtu.be/yJv2JRM--ws?t=242))
- **The ShadCN MCP grounds UI generation in real component structure.** — The frontend prompt names shadcn/ui as the library and a TweakCN theme. The ShadCN MCP supplies component context so the agent picks components itself. A slash command with extra MCP usage tips is also included. ([5:05](https://youtu.be/yJv2JRM--ws?t=305))
- **Frontend and backend are integrated in a separate pass after the static UI exists.** — The cart and checkout pages are first only UI with no logic. A second to-do list then connects the frontend to the backend, and the speaker shows login attempts in the Supabase auth panel as evidence the connection works. ([6:15](https://youtu.be/yJv2JRM--ws?t=375))
- **Stripe is verified with a mock before the real checkout replaces it.** — The agent first builds a mock payment setup to confirm the wiring, then swaps in the real Stripe checkout. The speaker checks the Stripe dashboard's customers and transactions to confirm the payment history. ([6:15](https://youtu.be/yJv2JRM--ws?t=375))

## Techniques
- **One-command MCP wiring with a /mcp health check** — Run the MCP add command from the resources and paste the service credential into it: a Supabase personal access token from account settings, or a Stripe restricted API key. Run /mcp in Claude Code to confirm the server is connected. Repeat the same check for every server. *When:* When connecting any hosted service (database, UI library, payments) to a coding agent that should act on it directly.
- **PRD to converter prompts, one per MCP** — Brainstorm the app with an LLM, compile the output into a PRD covering pages, flows, data and payments, then write one converter prompt per MCP that rewrites the relevant PRD requirements into that server's terms. Feed each converter output to the matching MCP. *When:* For a multi-service app where each service has its own tool surface and one undifferentiated prompt would blur them.
- **Dependency-ordered single-session build** — Use one Claude Code chat and do the backend first, then the frontend against the live backend, then payments. Give each stage its own prompt; the agent turns it into a to-do list and completes the items in order. *When:* When later layers depend on earlier ones and parallel agents would have to coordinate shared state.
- **Component-grounded UI with a theme and a usage slash command** — Name the UI library (shadcn/ui) and a theme (a TweakCN theme) in the frontend prompt. Connect the ShadCN MCP so the agent fetches component structure before writing code. Keep a slash command with usage guidance for the MCP. *When:* When generating a UI with a component library and wanting fewer layout or component-usage errors.
- **Static UI first, then a separate wiring pass** — Have the agent build all pages as static UI first, confirm the app runs, then create a second to-do list that connects the frontend to the backend, such as auth and data calls. *When:* When you want to separate layout errors from integration errors and check each layer alone.
- **Mock-then-real payment verification** — Ask the agent for a mock Stripe setup first to confirm the flow works, then replace the mock with real Stripe checkout. Check the Stripe dashboard's customers and transactions to confirm the records. *When:* Before turning on real payments, to separate wiring bugs from integration bugs.

## Numbers
- Three MCP servers are connected to one Claude Code project: Supabase (backend), ShadCN (frontend), and Stripe (payments). ([0:00](https://youtu.be/yJv2JRM--ws?t=0))
- Total runtime is 8:41. The video gives no cost, token, latency, build-time, or success-rate figures. ([0:00](https://youtu.be/yJv2JRM--ws?t=0))
- Each MCP is connected with one command, and the same /mcp check is used for all three. ([1:12](https://youtu.be/yJv2JRM--ws?t=72))

## Hot takes
- The title's "never vibe coding without" framing overstates the case. One demo store is shown, and the video reports no failures, retries, tests, or security review of the auth and payment code.
- The useful details are in external resources (MCP commands, converter prompts, the slash command), not on screen, so the video alone is not reproducible.
- The most transferable habit is the mock-then-real Stripe check, plus building in dependency order rather than in parallel.
- The demo is a click-through of login, cart and checkout. It is not evidence that the generated app is correct, secure, or ready to sell.

## Tools mentioned
Claude Code, Cursor, Next.js, Supabase (MCP server), ShadCN MCP, shadcn/ui, TweakCN, Stripe (MCP server, Stripe checkout), ChatGPT (used for the PRD brainstorm)

## Relevance to our work
- **prosharness** (1/3): Its staged build order (backend, then frontend, then payments) with a to-do list per stage and a mock-before-real check lines up with ProsHarness's checkpoint and plan-driven runs. The credentials are pasted directly into commands, which runs against ProsHarness's zero-token credential handling. → *When designing checkpointed plans, compare its per-stage to-do lists and mock-before-real payment check against how ProsHarness checkpoints a run, and keep credentials out of pasted commands.*

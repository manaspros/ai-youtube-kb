# I Tried TanStack AI... (it's good)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `sdL6bF74t68` · [watch](https://youtu.be/sdL6bF74t68) · **date:** 2026-01-02 · **length:** 7:04 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Better Stack host (unnamed) · **orgs:** TanStack, Vercel, OpenAI, Anthropic, Google, Ollama, OpenRouter, Tavily, Better Stack
- **topics:** dev-tools, mcp-and-tools · **tags:** tanstack-ai, vercel-ai-sdk, streaming, tool-calling, typescript, react, web-search, type-safety, alpha

> Hands-on flyby of TanStack AI (alpha): server-side streaming chat, a typed useChat client hook, and isomorphic tool definitions wired to web search. The speaker finds little that differs from Vercel's AI SDK.

## Summary
The Better Stack host tries TanStack AI, an alpha TypeScript AI SDK that is meant to work alongside an existing stack. It has server support for JavaScript, PHP and Python, client libraries for React, Solid and vanilla JS (Svelte is said to be coming), and provider adapters for OpenAI, Anthropic, Gemini and one more provider. He builds a basic chatbot: a server route calls the core chat function with an OpenAI adapter, the messages, the model and a conversation ID, then turns the chunk stream into an HTTP response. The main selling point he shows is type safety, since the model list and the per-model provider options (such as reasoning effort) are typed, and a wrong option for a model gives a compile error. On the client, the useChat hook returns messages, a send function and a loading flag, and messages are rendered by part type (thinking, text, tool call, tool result). To fix a stale answer about the current F1 champion, he defines a web-search tool with an input schema and description, runs it on the server against Tavily, and passes it in the tools array; the client gets only the definition, for types, and switches on part.name. He says the SDK is young and not production-ready, that it so far looks much like Vercel's AI SDK, and that coding assistants keep generating outdated Vercel AI SDK code for it.

## Key ideas
- **TanStack AI is in alpha and not for production, but it already spans server languages (JS, PHP, Python), client libraries (React, Solid, vanilla JS) and several model providers.** — Speaker stresses the goal of multi-language libraries that fit into an existing stack rather than replacing it. The provider list includes OpenAI, Anthropic and Gemini, plus one more the captions garble. ([0:00](https://youtu.be/sdL6bF74t68?t=0))
- **Server side is one chat call with a provider adapter, then a stream-to-HTTP-response helper.** — Inputs are the adapter, the messages from the POST body, the model and a conversation ID. The model type is inferred from the adapter, so only that provider's models type-check. ([0:00](https://youtu.be/sdL6bF74t68?t=0))
- **Provider options are typed per model, which he says beats the Vercel AI SDK experience.** — Reasoning effort is only accepted by models that support it. Switching to GPT-4o produces a type error, and he found the Vercel SDK's per-model options unclear. ([1:14](https://youtu.be/sdL6bF74t68?t=74))
- **Client useChat hook pairs with a server-sent-events connection to the same endpoint.** — The hook returns messages, a send function and an isLoading flag. Each message has a role and an array of parts: thinking, text, tool call and tool result. ([2:37](https://youtu.be/sdL6bF74t68?t=157))
- **Tool definitions are isomorphic: one definition with input schema and description can be used on the client or the server.** — Definition is shared, but the execute function decides where it runs. Server-side execution receives already-validated parameters. ([3:46](https://youtu.be/sdL6bF74t68?t=226))
- **Tool execution runs on the server for an API-keyed service, and the client gets only the definition, for types.** — Example: the search tool calls Tavily, returns JSON, and is passed in the chat tools array. Client switches on part.name to render tool calls, and a sources panel is built from the results. ([4:49](https://youtu.be/sdL6bF74t68?t=289))
- **Verdict: little is new relative to Vercel's AI SDK, and coding assistants keep writing outdated Vercel code for TanStack.** — Speaker says the Vercel SDK is over two years old, so models trained on it default to its hook and function names. He expects differentiation from future features: client-side tools, approval flows for human-in-the-loop calls, agentic loop management and headless chat UI components. ([5:59](https://youtu.be/sdL6bF74t68?t=359))

## Techniques
- **Typed server chat route with stream response** — On the server, call chat() from the core package with the chosen provider adapter, the request's messages, the model and the conversation ID, plus a tools array. Return the chunk stream as an HTTP response with the library's stream helper. Model and provider-option types come from the adapter. *When:* Adding streaming chat to a TypeScript backend where you want type-checked model options and a provider-swappable adapter.
- **Client useChat hook with server-sent events** — Install the framework client package. In the component, call useChat with a connection built from the server-sent-events helper pointed at the chat endpoint. Use the returned messages, send function and isLoading flag. Render each message's parts by type: thinking, text, tool call, tool result. *When:* Building a React (or Solid or vanilla JS) chat UI that streams from your own endpoint.
- **Shared tool definition for server execution and client typing** — Define the tool once with an input schema (query, max results) and a description the model uses to choose it. Attach the execute function on the server, where it receives validated parameters, and call a web-search API there. On the client, pass only the definition to useChat for types. Use part.name to branch on tool-call parts. *When:* Giving the model a web-search or API tool while keeping API keys on the server and keeping the UI type-safe for tool names.

## Numbers
- Server support in 3 languages (JavaScript, PHP, Python), client libraries for 3 frontends (React, Solid, vanilla JS), and 4 model providers at alpha. ([0:00](https://youtu.be/sdL6bF74t68?t=0))
- Type error appears when GPT-4o is selected with a reasoning option that only GPT-5 accepts. ([1:14](https://youtu.be/sdL6bF74t68?t=74))
- The Vercel AI SDK is over two years old, and coding assistants still produce its code for TanStack prompts. ([5:59](https://youtu.be/sdL6bF74t68?t=359))

## Hot takes
- Speaker sees little that differs from the Vercel AI SDK so far; differentiation depends on future features.
- The Vercel SDK's age means AI coding tools keep generating Vercel code, which he calls the main hurdle for a newer library.
- Typed per-model provider options are the standout feature, and he says the Vercel SDK's options were less clear.
- OpenRouter support would need provider-option types for every model it routes, so it is a lot of types.

## Tools mentioned
TanStack AI (alpha), Vercel AI SDK, OpenAI adapter, Anthropic adapter, Gemini adapter, Ollama (captioned as 'Alarma'), OpenRouter (no adapter yet), React, Solid, Vanilla JS client, Svelte (planned), GPT-5, GPT-4o, Tavily (web search API), Cursor (mentioned as generating outdated Vercel code)

## Relevance to our work
- **agentos** (1/3): AgentOS is a provider-agnostic HTTP proxy, so a client SDK is mostly out of scope. The tool-definition pattern is only relevant if we add a TypeScript web client. → *Skip unless AgentOS gets a TS web client. If it does, reuse the shared tool-definition pattern rather than duplicating schemas.*
- **general** (1/3): The one-definition, server-execute, client-type pattern for tools is a reusable idea for any agent UI that renders tool-call parts. → *When designing tool-call rendering for any agent UI, define each tool once (schema plus description) and branch on tool name in the UI.*

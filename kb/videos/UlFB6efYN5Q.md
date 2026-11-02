# A Song of Types and Agents - Roberto Stagi, Ratel

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `UlFB6efYN5Q` · [watch](https://youtu.be/UlFB6efYN5Q) · **date:** 2026-07-18 · **length:** 14:16 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Roberto Stagi · **orgs:** Ratel, AI Socratic, GitHub, Anthropic, Vercel
- **topics:** agent-architecture, dev-tools, coding-agents · **tags:** typescript, python, language-choice, zod, npm, vercel-ai-sdk, github-octoverse, agent-applications, end-to-end-typing

> Roberto Stagi argues TypeScript is overtaking Python for the agent and application layer, because coding agents default to it, npm is deep, and one Zod schema can type the whole stack; Python keeps training and serving.

## Summary
The speaker argues AI has moved from model training up to the application layer, and that the application layer has been TypeScript's for a long time. Python still owns training, research and GPU serving, which he expects to remain so. GitHub's 2025 data, as he reads it, shows TypeScript passing Python as the top language in August 2025, with the same driver cited as in 2024 (AI). He attributes the shift mainly to coding agents such as Lovable, Claude Code, Cursor and Codex, which became the default way to build apps and generate TypeScript. He gives four reasons to build agents in TypeScript: coding agents should improve on TypeScript as more TypeScript code enters training data, npm covers most needs, one language and one codebase cover the agent loop, tools, backend and UI, and one Zod schema gives end-to-end types. He cites the Vercel AI SDK's growth as evidence, and closes by invoking Jeff Atwood's "any application that can be written in JavaScript will be written in JavaScript" and its TypeScript corollary. His advice is to keep training in Python but build agents and applications in TypeScript. The talk offers little hard evidence beyond download and developer counts, and the speaker runs a context-layer company, so the argument is opinion-led.

## Key ideas
- **AI has moved up the stack from training to the application layer, and the application layer belongs to TypeScript.** — Python still owns training, research and GPU serving. TypeScript now owns the app layer and, the speaker argues, the agentic layer that calls the models. ([2:43](https://youtu.be/UlFB6efYN5Q?t=163))
- **TypeScript passed Python as GitHub's most-used language in August 2025, and GitHub gave the same AI-driven reason as in 2024.** — In 2024 AI pushed Python to the top. In 2025 the same report credited AI for TypeScript. New developers in 2025 reached for TypeScript where earlier ones reached for Python. ([3:42](https://youtu.be/UlFB6efYN5Q?t=222))
- **Coding agents are the driver. They became the default way to build apps, and they build in TypeScript.** — Lovable, Claude Code, Cursor and Codex are named as the established players. Because almost every new app now ships AI features, demand for AI integrations lands on TypeScript. ([5:04](https://youtu.be/UlFB6efYN5Q?t=304))
- **Coding agents should get better at TypeScript over time, because more TypeScript apps feed the training of the next agents.** — This is the speaker's first reason to build agents in TypeScript: deeper native integrations and better output quality are expected to follow. ([7:33](https://youtu.be/UlFB6efYN5Q?t=453))
- **One language and one codebase cut the sync cost between a backend and a frontend.** — A Python agent or backend usually needs a separate FastAPI service and a React app, joined by a contract to maintain. In TypeScript, the agent loop, tools, backend and UI can share one codebase. ([8:56](https://youtu.be/UlFB6efYN5Q?t=536))
- **A single Zod schema can type a value from the model call through the backend to the UI.** — Define the type once and reuse it in the model layer, the backend and the React UI, so one type is checked end to end. The speaker contrasts this with a typing boundary that must be kept in sync in Python stacks. ([9:59](https://youtu.be/UlFB6efYN5Q?t=599))
- **The speaker frames the trend as a prediction: any application that can be written in JavaScript will be written in TypeScript, and so will agentic ones.** — He cites Jeff Atwood's old line about JavaScript and presents TypeScript as its corollary. He expects the gap between Python and TypeScript at the application layer to widen. His advice is to keep training in Python and build agents in TypeScript. ([12:22](https://youtu.be/UlFB6efYN5Q?t=742))

## Techniques
- **Shared Zod schema across the full stack** — Define each data type once as a Zod schema. Reuse it for model output validation, backend handlers and UI forms, so the type is checked end to end without a separate contract to maintain. *When:* A TypeScript stack where an agent, its backend and its UI exchange structured data and drift between separate type definitions is a risk.
- **Single-language monorepo for agent apps** — Keep the agent loop, tool definitions, backend services and UI in one TypeScript codebase, not a Python service plus a separate React app. *When:* A small team building an AI-enabled product where cross-service contract sync costs more than the language benefits.
- **Split by layer: Python for training and serving, TypeScript for the app and agent layer** — Keep model training, research and GPU inference in Python. Build the application and agent orchestration layer in TypeScript on top of model APIs. *When:* You need the Python ML tooling for model work but ship user-facing AI features as a web app.

## Numbers
- Vercel AI SDK weekly downloads rose from 1.6M to 15.1M in one year (about 9-10x). ([10:54](https://youtu.be/UlFB6efYN5Q?t=654))
- GitHub reported about one new developer joining every second in 2025. ([5:04](https://youtu.be/UlFB6efYN5Q?t=304))
- TypeScript passed Python as GitHub's most-used language in August 2025, after Python had topped the ranking in 2024. ([3:42](https://youtu.be/UlFB6efYN5Q?t=222))

## Hot takes
- TypeScript is winning the war for the AI application and agent layer, and Python will keep only training and serving.
- Coding agents defaulting to TypeScript will create a feedback loop that makes TypeScript the default for AI apps.
- Any agentic application will eventually be written in TypeScript, and teams that overlook it will fall behind.

## Tools mentioned
TypeScript, Python, Zod, npm, Vercel AI SDK, FastAPI, React, Claude Code, Cursor, Codex, Lovable

## Relevance to our work
- **agentos** (1/3): AgentOS is Python and Rust infra for the inference and proxy layers, which the talk leaves to Python. A TypeScript client or agent-facing SDK is the only place the argument touches the project. → *If AgentOS gets a TypeScript client SDK, define its request and response types once with Zod and reuse them in the client and any UI, which is the talk's only concrete typing pattern.*

# Vercel made a Model (v0 in Cursor)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `jZB1sXDaOj8` · [watch](https://youtu.be/jZB1sXDaOj8) · **date:** 2025-11-02 · **length:** 6:19 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** Better Stack host (unnamed in transcript) · **orgs:** Vercel, Cursor, Better Stack
- **topics:** vibe-coding-app-building, coding-agents, models-research · **tags:** v0, v0-1.0-md, cursor, nextjs, shadcn, openai-compatible-api, base-url-override, vercel-ai-sdk, model-routing

> Better Stack tries Vercel's new v0-1.0-md model through its API, routes Cursor's OpenAI model slot to it via a base-URL override, and builds a shadcn to-do app from one prompt.

## Summary
Vercel released its own coding model, v0-1.0-md, which the host says is built in-house rather than being prompts or RAG over another provider's model. It is available through an OpenAI-compatible API, is tuned for Next.js and shadcn-style web work, and has a 128k input context, 32k max output, and a 200-messages-per-day beta limit. The host tests it first in the Vercel AI playground, where thinking tokens stream before code. He then wires it into Cursor by pasting a v0 API key and overriding the OpenAI key and base URL, which makes every OpenAI model selection in Cursor hit v0 instead. Using Cursor's agent mode with a single prompt, the model scaffolds a Next.js app, runs shadcn init (which errors on an outdated docs link but self-corrects), and generates the code, taking about 10 minutes in beta. The result runs with some type errors, and the host says it looks better than the v0.dev output, though adding a task is broken. The video is a single hands-on run with no benchmarks.

## Key ideas
- **Vercel released its own model, v0-1.0-md, and the host frames it as an in-house model rather than custom prompts or RAG over another provider's model.** — The host says the model is available via API for use in your own apps or in coding tools like Cursor. Upgraded versions were said to be coming soon. The host's claim that it is built in-house is his reading and is not verified in the video. ([0:00](https://youtu.be/jZB1sXDaOj8?t=0))
- **The API is OpenAI-compatible and framework-aware, with autofix, quick edit and multimodal input.** — Features listed are text and image input, autofix of common coding issues during generation, streamed inline quick edits, and framework-aware completions evaluated on Next.js and Vercel stacks. Limits are a 128k context window, 32k max output, and a 200-messages-per-day beta cap. ([1:22](https://youtu.be/jZB1sXDaOj8?t=82))
- **Access needs a premium or team plan with usage-based billing turned on.** — The host calls the Cursor setup hacky and expects it to improve once the model leaves beta. ([2:29](https://youtu.be/jZB1sXDaOj8?t=149))
- **Cursor can route to the v0 model by overriding the OpenAI key and base URL, which silently replaces every OpenAI model in the picker.** — Once the override is on, selecting any OpenAI model uses v0. The override has to be switched off to use real OpenAI models again. Verification is done by asking the model who it is, and it replies as Vercel's assistant. ([2:29](https://youtu.be/jZB1sXDaOj8?t=149))
- **Given one prompt, the model handled scaffolding, dependency install and component setup with no follow-up fixes, though the output had type errors and one broken feature.** — The agent ran the Next.js scaffold command, hit an outdated shadcn init error that it fixed itself, installed many shadcn components, and wrote the app in one block rather than streaming it. The host had to keep clicking run on tool calls. He says he never asked for a fix. The app ran, but adding a task did not work. ([3:47](https://youtu.be/jZB1sXDaOj8?t=227))
- **The model does not host apps. v0 hosts them and this is only the base model, so you must build your own deployment.** — In the playground the model produced code and setup steps, but no hosted preview. ([0:00](https://youtu.be/jZB1sXDaOj8?t=0))

## Techniques
- **Get a v0 API key for model access** — On v0.dev go to Settings, then API Keys, and create a new key. This requires a premium or team plan with usage-based billing enabled. *When:* Before connecting v0-1.0-md to any OpenAI-compatible client. The host notes the beta is capped at 200 messages per day.
- **Route Cursor to the v0 model via base-URL override** — In Cursor's model settings, paste the v0 API key into the OpenAI API key field, override the OpenAI base URL with the endpoint from the v0 API docs (link in the video description; the URL is not spoken), click Verify, then open agent mode and pick an OpenAI-named model. Confirm with a 'who are you' prompt. *When:* When you want a v0-style coding model in Cursor before native support exists. Remember that every OpenAI model selection now hits v0, so turn the override off to get real OpenAI models back.
- **Single-prompt full-app generation in agent mode** — Give one concrete prompt, e.g. a modern to-do app using shadcn components. Let the agent run the generated scaffold command for a Next.js app, accept the shadcn init step (ignore an outdated docs link if it errors), and click run on each tool call until files and packages are installed. Then run the app and check for type errors. *When:* For fast Next.js and shadcn prototypes where you do not want to scaffold by hand. Expect some type errors and at least one feature to break, and plan a follow-up prompt for those.
- **Compare the same prompt across two surfaces** — Send the same prompt to v0.dev and to Cursor using the v0 model, then compare the generated UI and any broken features. *When:* When judging whether the API route is good enough to replace the hosted v0 product for your work.

## Numbers
- v0-1.0-md has a 128,000-token max context window and 32,000-token max output. ([1:22](https://youtu.be/jZB1sXDaOj8?t=82))
- Beta limit of 200 messages per day. ([1:22](https://youtu.be/jZB1sXDaOj8?t=82))
- Generating the full to-do app took about 10 minutes in beta. The host attributes part of this to load from testers. ([4:47](https://youtu.be/jZB1sXDaOj8?t=287))
- Access requires a premium or team plan with usage-based billing turned on. ([2:29](https://youtu.be/jZB1sXDaOj8?t=149))

## Hot takes
- The host says the output looks better than the v0.dev result he got from the same prompt, while also noting a broken feature.
- Routing via an OpenAI base-URL override is a hack; he expects Vercel to ship a proper integration once out of beta.
- The claim that Vercel built its own model rather than wrapping prompts or RAG around another provider is asserted, not shown.
- The evidence is one hands-on run with no benchmarks, so treat the quality claims as anecdotal.

## Tools mentioned
v0 (v0.dev), v0-1.0-md, Cursor, Next.js, shadcn/ui (spoken as 'ShadCN'), Vercel AI SDK, Vercel AI playground, Three.js (mentioned as a v0 output example), Codex (transcript reads 'codecs'; another coding tool the host names as a target)

## Relevance to our work
- **agentos** (1/3): The base-URL override is the same OpenAI-compatible routing idea AgentOS relies on, and it shows that a model name in the client does not identify the upstream model. → *Add a test that the Govrix proxy passes an unrecognized OpenAI-style model name through unchanged, and that the response records the actual upstream model.*

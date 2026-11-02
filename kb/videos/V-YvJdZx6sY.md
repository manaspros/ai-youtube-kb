# Ship LLM Apps Locally with Dify

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `V-YvJdZx6sY` · [watch](https://youtu.be/V-YvJdZx6sY) · **date:** 2026-02-02 · **length:** 6:14 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Better Stack presenter (not named in transcript) · **orgs:** Dify, LangChain, LlamaIndex, n8n, OpenAI, Google, Vercel, Supabase
- **topics:** agent-architecture, rag-retrieval, dev-tools · **tags:** dify, visual-workflow-builder, low-code-llm, rag, document-extraction, self-hosted, docker, provider-swap, n8n, langchain, speech-to-text, model-provider-config

> Better Stack's short walkthrough of Dify, a self-hosted visual builder for LLM apps (RAG, chained prompts, agents), with a file-summarization demo and a candid list of drawbacks.

## Summary
The presenter introduces Dify as an open-source, Docker-hosted platform with a drag-and-drop canvas for building LLM workflows, not a code library like LangChain or LlamaIndex. He positions it against LangChain (visual and fast to build versus fine-grained code control) and n8n (n8n is general automation with many integrations, while Dify is designed around LLM workflows, RAG and agent patterns). Setup is shown as adding a model provider key under Settings, with other providers installed as plugins. The demo builds a workflow that takes an uploaded file, branches on type, extracts text from CSV or PDF, or transcribes audio, then sends the content to an OpenAI model for summarization. Drawbacks named are a confusing initial setup, occasional bugs, weaker non-AI automation than n8n, and a self-hosting requirement of at least 2 vCPUs and 4 GB RAM. The verdict is hedged: useful for fast MVPs and idea validation by solo devs or small teams, not an automatic default.

## Key ideas
- **Dify is positioned as a platform, not a library: an open-source, self-hosted visual canvas for building LLM apps, competing on speed of building rather than code control.** — The presenter says it does not try to beat LangChain at code. It bundles prompt chaining, RAG, tool calls and agents in one place, and the value is what it saves you from rebuilding. ([0:00](https://youtu.be/V-YvJdZx6sY?t=0))
- **The bundled pieces matter more than any single feature: multi-step logic with conditionals and branches, managed knowledge bases (upload documents, the platform handles chunking, indexing and retrieval), and provider swapping without rewriting app logic.** — He stresses that the combination is the point. Provider swapping is framed as avoiding lock-in to one vendor such as OpenAI. ([0:48](https://youtu.be/V-YvJdZx6sY?t=48))
- **Tradeoff versus LangChain: Dify is visual and needs no Python everywhere, while LangChain gives deeper code control over things like custom memory.** — He frames the choice as speed and visual building against fine-grained control. ([0:48](https://youtu.be/V-YvJdZx6sY?t=48))
- **Dify and n8n look similar (both node-based and free to self-host), but Dify is AI-first with native advanced RAG and agent patterns such as ReAct, while n8n is stronger for general automation with robust triggers and integrations, and its AI features feel bolted on.** — He cites n8n's integration count as at least around 600 apps. This is his subjective assessment, not a benchmark. ([2:11](https://youtu.be/V-YvJdZx6sY?t=131))
- **Setup is key-first: get an API key from the model provider, add it under Settings then Model provider, and install a plugin for other providers such as Google Gemini before choosing the model inside a workflow.** — He shows OpenAI as already configured and says the provider list is long. ([2:11](https://youtu.be/V-YvJdZx6sY?t=131))
- **The demo is a branching file-summarization workflow: a file-input start node splits on file type. CSV or PDF goes through a document extractor, other input is treated as audio and goes through speech-to-text. Both paths then reach an LLM node with a prompt and an output node.** — He ran it on a CSV, which was summarized, and on an MP3 speech recording, which was transcribed and summarized. The video shows no evaluation of output accuracy. ([3:21](https://youtu.be/V-YvJdZx6sY?t=201))
- **Drawbacks: initial setup took longer than expected and was confusing, there were some bugs, it is weaker than n8n for non-AI tasks, and self-hosting needs at least 2 vCPUs and 4 GB RAM.** — His conclusion is that it depends on the problem. It suits solo devs and small teams validating MVPs, and larger setups could save hours of repetitive work. ([4:48](https://youtu.be/V-YvJdZx6sY?t=288))

## Techniques
- **Branch a workflow on input file type** — Start node 'User input' with a file input field. Add a conditional branch: if the file is CSV or PDF, route to a Document extractor node (file as input), then an LLM node linked to the chosen provider, with a prompt that gives the extracted text as context, then output. Otherwise, route to speech-to-text, then an LLM node, then output. Only the node types are named in the video; no exact prompt text or config keys are shown. *When:* Summarizing or analyzing mixed uploads (documents, spreadsheets, audio) without writing an ingestion service.
- **Add a model provider via Settings** — Open Settings, then Model provider. For OpenAI, paste the API key from the OpenAI dashboard. For other providers (example: Google Gemini), install the provider plugin, paste the key, and save. Then pick the model inside each LLM node of a workflow. *When:* Switching or mixing models per workflow node without changing app logic.
- **Run Dify locally with Docker** — Clone the Dify repository from GitHub and start it with Docker. The video says only 'spin it up with Docker' and shows no exact commands. Provision at least 2 vCPUs and 4 GB RAM. *When:* Self-hosting an LLM app builder on your own data.
- **Choose between visual builder and code orchestration** — Pick Dify when speed and visual flows matter and you want native RAG and agent nodes. Pick LangChain when you need custom memory or fine-grained control in code. Pick n8n when the workflow is mostly general integrations and triggers with AI as a side step. *When:* Deciding which orchestration tool fits a new LLM feature, especially for quick MVPs.

## Numbers
- n8n has at least about 600 apps (presenter's estimate, not verified). ([2:11](https://youtu.be/V-YvJdZx6sY?t=131))
- Self-hosting Dify needs at least 2 vCPUs and 4 GB RAM. ([4:48](https://youtu.be/V-YvJdZx6sY?t=288))
- Demo ran on a CSV file, a PDF path through the document extractor, and an MP3 speech recording transcribed by speech-to-text. No timing, token counts or cost figures were given. ([3:21](https://youtu.be/V-YvJdZx6sY?t=201))
- Video length is 6:14. ([0:00](https://youtu.be/V-YvJdZx6sY?t=0))

## Hot takes
- Dify is 'AI first' and n8n's AI features feel bolted on (presenter's opinion, no evidence shown).
- The presenter says Dify is simpler and friendlier than n8n for LLM workflows, but also says setup was confusing and buggy for him. The two claims pull against each other.
- Shallow overview: one demo, no output quality check, no cost data, and no code. Treat the comparisons as impressions.

## Tools mentioned
Dify, LangChain, LlamaIndex, n8n, OpenAI API, Google Gemini, Docker, Vercel, Supabase, ReAct agent pattern

## Relevance to our work
- **agentos** (1/3): Dify's provider-swap and document-to-LLM ingestion flow is a product-level reference point for MemoryMesh's RAG ingestion, though it does not touch the proxy, scheduler or KV-cache pillars. → *Compare MemoryMesh's ingestion path (chunking, indexing, retrieval) against Dify's knowledge-base and document-extractor flow as a feature checklist, not a dependency.*

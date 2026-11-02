# I Replaced Every AI Subscription I Pay For

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `MgHQncHjDhs` · [watch](https://youtu.be/MgHQncHjDhs) · **date:** 2026-09-02 · **length:** 6:40 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Kai Explains host (name not reliable in auto-captions) · **orgs:** OpenAI, Anthropic, Perplexity, Grammarly, Jasper, Midjourney
- **topics:** local-ai, token-cost-efficiency · **tags:** ollama, open-webui, self-hosting, local-llm, privacy, subscription-cost, raspberry-pi, perplexica, searxng, comfyui, stable-diffusion, flux

> Kai Explains argues that a $120/month stack of AI subscriptions can be replaced with self-hosted open-source tools (Ollama, Open WebUI, Perplexica, ComfyUI) running on an old laptop or Raspberry Pi. Mostly motivation; the technical detail is thin.

## Summary
The host says he spent about $120 a month on AI subscriptions (chat, search, image generation, writing assistants) and spent a week replacing them with self-hosted tools on a home machine, such as an old laptop or a Raspberry Pi. The core stack is Ollama as the local model engine with Open WebUI as a ChatGPT-style front end, with small open-weight models like Llama 3.1 8B or Mistral 7B suggested for weaker hardware. He also covers self-hosted AI web search (Perplexica over SearXNG), local image generation with ComfyUI and Stable Diffusion or FLUX, and browser or editor writing assistants pointed at a local Ollama endpoint. He says a local AI coding assistant also runs at home and can be reached across the home network. The video stays at the level of "what to install"; it shows no commands, configs, or benchmarks, and its savings claim (about $1,400 a year) is the host's own arithmetic.

## Key ideas
- **Subscriptions are framed as rented access that providers can throttle, reprice, or downgrade, which motivates running models at home.** — The host spent about $120 a month across several $20 tiers and a rate-limited chat product; the pitch is ownership and control over the model and the prompts. ([0:00](https://youtu.be/MgHQncHjDhs?t=0))
- **Ollama plus Open WebUI is the core local chat stack.** — Ollama downloads and runs open-weight models (Mistral and Qwen named) on the local machine; Open WebUI supplies the chat window with history, dark mode, and multi-model switching. The host presents it as a full replacement for ChatGPT or Claude for everyday use. ([1:15](https://youtu.be/MgHQncHjDhs?t=75))
- **Weak hardware is handled with small models, not bigger hardware.** — On an old laptop or a Raspberry Pi, the host suggests Llama 3.1 8B or Mistral 7B for writing, summarizing, brainstorming, and Q&A, and claims they cover most daily use. No quality comparison is shown. ([2:24](https://youtu.be/MgHQncHjDhs?t=144))
- **Self-hosted AI search replaces Perplexity-style cited search.** — Perplexica, backed by SearXNG for web results and local Ollama models for answers, gives cited web search where queries stay on the host's machine. ([3:38](https://youtu.be/MgHQncHjDhs?t=218))
- **Local image generation replaces hosted Midjourney-style services.** — ComfyUI runs Stable Diffusion-family models, including FLUX, locally; the host presents this as private and unlimited, with no account-ban risk. ([3:38](https://youtu.be/MgHQncHjDhs?t=218))
- **Browser and editor writing assistants can point at the same local model server.** — The host says a browser extension or editor plugin can talk to a local Ollama model for grammar, tone, and rewriting, which replaces Grammarly- and Jasper-style paid tools. He does not name a specific extension. ([4:59](https://youtu.be/MgHQncHjDhs?t=299))
- **A local coding assistant can run on the home network and be reached from other devices.** — The host says his coding assistant runs fully local so code does not leave the home network, and he can reach it from anywhere on that network. No assistant is named and no setup is shown. ([4:59](https://youtu.be/MgHQncHjDhs?t=299))
- **The savings figure is the host's own arithmetic, and the pitch leans on privacy and ownership.** — The host says the setup takes about one afternoon and saves about $1,400 a year, roughly the $120 monthly spend times 12. Electricity is described only as pennies; hardware, setup time, and maintenance are not costed. ([6:15](https://youtu.be/MgHQncHjDhs?t=375))

## Techniques
- **Ollama engine with Open WebUI front end on a home machine** — Install Ollama on an always-on machine (an old laptop or a Raspberry Pi), pull open-weight models such as Mistral, Qwen, or Llama, then run Open WebUI on top for a browser chat with history and model switching. The video shows no commands, ports, or config. *When:* Replacing a paid chat subscription where prompts should stay on local hardware and one interface should serve several models.
- **Small-model fallback for weak hardware** — Use Llama 3.1 8B or Mistral 7B for writing, summarizing, brainstorming, and Q&A on modest hardware instead of the largest models. The host gives no measured quality or speed numbers. *When:* Low-stakes everyday tasks where a small local model is good enough, and the machine cannot run larger models.
- **Self-hosted AI search with cited sources** — Run Perplexica for the answer layer, with SearXNG as the private metasearch backend, and point it at a local model served by Ollama. The video names the components but shows no configuration. *When:* Replacing paid AI search where the query text should not go to a third-party service.
- **Local image generation with ComfyUI** — Run ComfyUI locally with a Stable Diffusion or FLUX checkpoint. No workflow, model file, or hardware requirement is shown. *When:* Generating images without per-image or per-month fees and without hosted usage terms.
- **Local model as backend for editor and browser writing tools** — Install an open-source browser extension or editor plugin and point it at the local Ollama endpoint for grammar, tone, and rewrite suggestions. The host names no specific tool. *When:* Editing text that should not leave the device, in place of paid cloud writing assistants.

## Numbers
- The host spent about $120 a month on AI subscriptions, built up from several $20 tiers (ChatGPT, Claude, Perplexity) plus other tools. ([0:00](https://youtu.be/MgHQncHjDhs?t=0))
- Writing tools cited as costing $30 a month (Grammarly) and $49 a month (Jasper); image tools cited as $10 to $60 a month (Midjourney). ([3:38](https://youtu.be/MgHQncHjDhs?t=218))
- Llama 3.1 8B or Mistral 7B suggested for weaker hardware, with the host claiming they cover about 90% of daily AI use. No measurement is given. ([2:24](https://youtu.be/MgHQncHjDhs?t=144))
- Claimed savings of about $1,400 a year, matching the $120 monthly spend times 12 (rounded). Hardware, setup time, and electricity are not priced beyond calling electricity pennies. ([6:15](https://youtu.be/MgHQncHjDhs?t=375))

## Hot takes
- The video is a stack-listing with no commands, configs, benchmarks, or hardware requirements, so it is not usable as a how-to despite the 'set this up in an afternoon' framing.
- The 90%-of-use claim for 7B and 8B models is asserted without evidence.
- The aside about free-tier API keys for frontier models is a murky suggestion that the host immediately half-retracts; it should not be treated as a recommendation.
- The savings figure ignores the cost of hardware, electricity over time, and maintenance, and treats the subscriptions as equal to what they replace.
- Quality is capped at 2 because the title promises a full replacement while the substance is a tool roundup with no measured results.

## Tools mentioned
Ollama, Open WebUI, Perplexica, SearXNG, ComfyUI, Stable Diffusion, FLUX, Mistral, Qwen, Llama 3.1 8B, Mistral 7B, Raspberry Pi, Grammarly, Jasper

## Relevance to our work
- **agentos** (1/3): The video is a consumer-level self-hosted local model stack (Ollama, Open WebUI). It touches the same local-serving idea as AgentOS's model layer, but gives no technical depth on serving, routing, or budgets. → *Consider a local Ollama endpoint as a cheap fallback or baseline model behind the AgentOS proxy, and measure it against the hosted model on the same tasks before routing any real traffic to it.*
- **general** (1/3): Useful as a reference for which open-source tools (Ollama, Open WebUI, Perplexica, SearXNG, ComfyUI) are common in the local-AI community, but not a source of technique. → *Skim this only if the user asks about self-hosted chat or search stacks; do not treat its claims as evidence.*

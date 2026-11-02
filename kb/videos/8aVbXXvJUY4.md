# An Interaction Is All You Need — Ivan Leo, Google DeepMind

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `8aVbXXvJUY4` · [watch](https://youtu.be/8aVbXXvJUY4) · **date:** 2026-10-04 · **length:** 17:04 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Ivan Leo · **orgs:** Google DeepMind
- **topics:** agent-architecture, sandboxing-execution, security-guardrails, mcp-and-tools · **tags:** interactions-api, managed-agents, server-side-state, interaction-id, environment-id, persistent-sandbox, credential-proxy, steps-data-model, agent-skills, gemini, antigravity

> Google DeepMind's Ivan Leo presents the Interactions API and Managed Agents: server-side state via interaction IDs, persistent sandboxes via environment IDs, and a credential-injecting proxy. Mostly a product walkthrough with a few reusable patterns.

## Summary
Ivan Leo, on the Developer Experience team at Google DeepMind, traces how models moved from single completions to function calling to multi-tool agents, and argues that an agent is mainly a capable model in a loop with an execution environment. He introduces the Interactions API, which keeps conversation context on the server: each response returns an interaction ID that the next turn passes back as previous_interaction_id, so the client does not resend history or manage thought signatures. The talk then covers Managed Agents, a hosted version of Google's agent harness (the one used in AI Studio and the Antigravity app) that runs in a persistent sandbox; the client keeps the environment ID to reattach to the same files and installed packages. Other points include a man-in-the-middle proxy that injects API tokens into outbound calls so the model never sees them, freezing a configured environment as a named agent (up to 1,000 per account, billed only for model tokens), and packaging a local skills folder into .agents so the same skills run locally and in the cloud. Typed output objects (output.type) and a Steps data model replace the older nested outputs array. Most of this is a vendor pitch, and several claims (Gemini-only multimodal steps, pricing, the proxy's security) are the speaker's own assertions rather than evidence.

## Key ideas
- **Agent state can live on the server instead of in the client** — Each response returns an interaction ID. Passing it back as previous_interaction_id keeps the full context, so the client avoids resending history. The speaker says a single stray whitespace in a client-built history once broke a startup's cache, and that dropping thought signatures lowers performance on the newer Gemini models. ([5:48](https://youtu.be/8aVbXXvJUY4?t=348))
- **A managed harness plus a persistent sandbox removes most of the infra work for a coding agent** — Building a coding agent used to mean tuning a harness, finding a sandbox provider, and handling context between runs. The Managed Agent gives a sandbox out of the box with one API call, using the same Antigravity harness that Google uses in its own products. ([9:12](https://youtu.be/8aVbXXvJUY4?t=552))
- **The environment ID is the handle for reattaching to the same sandbox** — If the client keeps the environment ID, later calls reach the same files, installed packages and workspace. Environments can be loaded from GCS buckets, GitHub repos or inline files, and the speaker says the agent needs no persistence logic of its own. ([10:36](https://youtu.be/8aVbXXvJUY4?t=636))
- **Credentials can be injected at a proxy so the model never holds them** — A man-in-the-middle proxy reads each outbound request's headers and swaps in tokens, for example for GitHub API calls. The speaker argues that a prompt-injected model can leak nothing it never saw. This is a claim about the design, and the talk shows no test of it. ([13:29](https://youtu.be/8aVbXXvJUY4?t=809))
- **Working agents can be frozen into named, reusable configurations** — Configure an environment by files and network sources, or by chatting with the agent until it is set up, then save it as a named agent. Up to 1,000 named agents are supported, and the speaker says storage and sandbox are not billed, only model tokens. ([13:29](https://youtu.be/8aVbXXvJUY4?t=809))
- **Local skills can be shipped unchanged to the cloud agent** — A skills folder tuned locally is packaged into .agents and uploaded as a source. The same harness and prompt then run in the cloud, which the speaker presents as a way to move from local iteration to a hosted agent without rewriting. ([12:06](https://youtu.be/8aVbXXvJUY4?t=726))
- **Typed outputs and a Steps data model replace nested response objects** — Each output carries a type discriminator (audio, image, text, function call, thought signature), so parsing does not depend on deeply nested fields. The Steps model replaces the legacy outputs array to support async tool calls and multi-model runs, and built-in tools (Google Search, URL context) can be mixed with custom function tools in one call. ([8:13](https://youtu.be/8aVbXXvJUY4?t=493))

## Techniques
- **Server-side conversation state via interaction ID** — Store the interaction ID returned by each response and pass it as previous_interaction_id on the next turn. Do not resend the whole history, and do not edit or reformat the stored ID. *When:* Multi-turn or chained calls where you want to keep the cache and preserve thought signatures on newer Gemini models.
- **Reattach to a persistent sandbox via environment ID** — Save the environment ID from the first call and pass it on later calls. Installed packages and written files persist across turns without any client-side state management. *When:* Long-running coding or analysis agents that work across several calls on the same repo.
- **Proxy-side credential injection** — Route the agent's outbound traffic through a proxy that adds auth headers per destination (for example, a GitHub token on api.github.com calls), so tokens stay out of the sandbox and the model's context. *When:* Agents that call private APIs and must not be able to leak credentials through prompt injection.
- **Freeze a tuned environment as a named agent** — Iterate by chatting until the sandbox has the right packages and sources, then freeze that configuration as a named agent and call it by name at scale. *When:* Several repeatable agent roles (for example, a data-analyst agent) that need the same setup on every run.
- **Local-to-cloud skill packaging** — Keep skills as folders, test them locally with the CLI, then upload the same folder into .agents as a source for the hosted agent. *When:* When skill quality has been checked locally and you want identical behaviour in the cloud.
- **Strongly typed output parsing** — Branch on output.type (audio, image, text, function call) instead of walking nested response objects. Change modality through the response modality and generation config. *When:* Multimodal pipelines that mix text, image and audio output in one flow.

## Numbers
- A Managed Agent run analyzing a hackathon repository burned over 2 million tokens ([12:06](https://youtu.be/8aVbXXvJUY4?t=726))
- Up to 1,000 named agents per account; storage and sandbox are not billed, only model tokens (vendor claim) ([14:57](https://youtu.be/8aVbXXvJUY4?t=897))
- Deep research agent runs for three minutes or more per task ([4:24](https://youtu.be/8aVbXXvJUY4?t=264))

## Hot takes
- Agents are mostly a capable model in a loop, and as models improve the scaffolding falls away (latest Opus and Fable models just use a bash tool).
- A single stray whitespace in client-built history can break a cache, so server-side state is safer.
- Only Gemini model families can produce these multimodal step pipelines (vendor claim).

## Tools mentioned
Interactions API, Managed Agents, Antigravity agent harness, Gemini API CLI, AI Studio, Google Search tool, URL context tool, GCS, GitHub

## Relevance to our work
- **agentos** (2/3): The credential-injecting proxy overlaps with the L1 Govrix Scout proxy, and the environment-ID sandbox overlaps with the L2C Crucible sandbox design. → *Prototype header-based credential injection in the Govrix Scout proxy: keep provider keys out of the sandbox env, inject them on outbound calls, and test that a prompt-injected model cannot read them.*
- **prosharness** (2/3): Checkpoint/resume of long runs is a core ProsHarness feature. The interaction-ID plus environment-ID pair is a resume handle pattern for reattaching to state. → *Store the provider's session and environment handles with each ProsHarness checkpoint so a resumed run reattaches to the same sandbox and files instead of rebuilding them.*

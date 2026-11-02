# How Secrets Leak Through AI Agents (and How to Stop It) — Venice AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `xn8EsW0wxyc` · [watch](https://youtu.be/xn8EsW0wxyc) · **date:** 2026-10-12 · **length:** 15:22 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Joshua Moe · **orgs:** Venice AI
- **topics:** security-guardrails, agent-architecture, observability, mcp-and-tools · **tags:** secrets management, privacy, prompt injection, credential handling, sandboxing, trusted execution environment, attestation, observability logging, tool calls, vault, handles, hashed identifiers, split-key custody, narrow agent scope, MCP

> Venice AI's developer-relations lead explains how secrets leak through agent architectures (logs, vaults, LLM context, tool calls) and patterns to contain them: hashed IDs, handles, narrow tool scope, and keeping credentials out of the reasoning layer.

## Summary
Joshua Moe, lead developer relations engineer at Venice AI, argues that agent systems leak secrets and personal data in more places than the model itself: logs, vault lookups, tool calls and exfiltration through over-broad tool sets. He first pitches Venice's privacy model (no stored prompts, anonymized requests to third-party providers, TEE-hosted models, encrypted video outputs), then moves to general patterns. The main pattern is to keep credentials in the deterministic runtime rather than the LLM reasoning layer, so the model only requests actions. Other patterns are hashed identifiers, split-key encryption, revocable handles, narrow tool scope to keep context small, and a prompt-injection classification layer in front of the agent. He says sandboxes and VMs help but do not stop egress leaks, so permissions need monitoring and teams should consider owning their own agent runtime. The talk ends by admitting that confidential tool calls remain unsolved, so parts of it are product promotion, but the secrets-flow analysis is useful engineering material.

## Key ideas
- **Credentials should live in the agent runtime, not the LLM reasoning layer.** — In a typical agent, the runtime fetches a secret from a vault, passes it to the model, and the model then makes the tool call. The speaker says this exposes the secret to the model and possibly to training data. He proposes tying the vault to the runtime, which acts as a deterministic execution layer, so the model only requests an action such as logging into a site. ([5:55](https://youtu.be/xn8EsW0wxyc?t=355))
- **Logs are a leak surface by default.** — Metrics, logs and traces are standard observability. Logs are useful for debugging, but they can store prompts, secrets and personal data unless someone is careful about what gets written. ([4:29](https://youtu.be/xn8EsW0wxyc?t=269))
- **Store hashes or handles instead of raw identity data.** — For rate limiting, you can key on a hash of the user footprint rather than the raw identifier. Access to a resource can be expressed as a handle object that can be revoked, so holding the handle is the permission. ([7:03](https://youtu.be/xn8EsW0wxyc?t=423))
- **Over-broad tool sets widen the exfiltration path.** — An MCP server may expose 15 to 20 tools when the agent needs one, and the API key for that tool is then in the agent's reach. A malicious tool call or a bad web destination can then exfiltrate it. Narrowing the tool set limits this and also keeps the context window small, which the speaker says helps performance. ([8:03](https://youtu.be/xn8EsW0wxyc?t=483))
- **Add a classification layer in front of the agent for prompt injection.** — The speaker suggests an LLM-based classifier, or a semantic search layer over vector storage or an in-memory index, to screen inputs before they reach the agent. ([9:22](https://youtu.be/xn8EsW0wxyc?t=562))
- **Sandboxes help but do not cover network egress.** — Firecracker VMs or EC2 inside a VPC improve isolation. If the agent still has internet access, data can leak through external API calls, so the speaker recommends monitoring permissions and, where possible, building your own agent runtime with your own steps, observability and tools. ([12:15](https://youtu.be/xn8EsW0wxyc?t=735))
- **Hardware TEEs give verifiable inference but not yet confidential tool calls.** — Venice returns an attestation with each response that can be checked, so the reasoning step can be proven private. The speaker says that keeping tool calls fully encrypted end to end is still an open problem, given the need for an ergonomic API. ([13:46](https://youtu.be/xn8EsW0wxyc?t=826))

## Techniques
- **Credential-in-runtime, not in-prompt** — Keep vault access in the deterministic agent runtime. The model emits an intent (for example, log in to site X), and the runtime injects the credential when it executes the tool call. The credential never enters the model's context. *When:* Any agent that needs authenticated tool or browser access, such as a browser agent that logs into websites, or a coding harness that calls authenticated APIs.
- **Hashed identifiers for rate limits and tracking** — Store and key on a hash of the user identifier instead of the raw value, so limits and lookups still work without holding personal data. *When:* Rate limiting, abuse tracking or analytics where you need to identify a repeat user but do not need who they are.
- **Split-key custody for stored outputs** — Encrypt stored payloads with a key split into two halves (read and write). Neither the attacker nor a compromised team account can decrypt alone. *When:* Storing generated artifacts or user payloads that must stay private even if the storage or an admin account is compromised. The speaker's example is video-generation results.
- **Revocable handles as capabilities** — Wrap access to a resource (for example, a database pool or a session key) in an object. No handle means no access, and revoking the handle removes access. *When:* Authorization for agent tools, especially where JWTs or session keys are part of the auth model.
- **Narrow tool exposure per agent** — Expose only the one or two tools an agent needs from an MCP server, not the full set of 15 to 20. This reduces the secrets an agent can reach and keeps the context window light. *When:* Any agent wired to an MCP server with many tools, or any time a subagent only needs a subset of capabilities.
- **Prompt-injection classifier in front of the agent** — Run each incoming input through a screening step. Options are an LLM classifier, or a semantic match against a vector store such as Qdrant or LanceDB, or an in-memory index. *When:* Agents that read untrusted content such as web pages, emails or tool output before acting.
- **Own the agent runtime** — Build your own coding harness or agent loop so you control the steps, observability hooks, tools and where credentials live. Do not rely only on a third-party harness. *When:* When you need to enforce privacy or security rules that the model layer cannot enforce, such as where secrets are held or what leaves the network.
- **Verifiable private inference via TEE attestation** — Run the model in a trusted execution environment and check the attestation returned with each response against a verifier. *When:* When you must prove to users or auditors that inference ran in a private process. The speaker notes this covers the reasoning step only, not tool calls.

## Numbers
- Example enterprise customer generating almost 90% of annual revenue, cited to show the cost of a single breach. This is a hypothetical example, not a measured figure. ([1:44](https://youtu.be/xn8EsW0wxyc?t=104))
- An MCP server may expose 15 to 20 tools when the agent needs only one. ([8:03](https://youtu.be/xn8EsW0wxyc?t=483))
- Talk length is 15:22. ([0:00](https://youtu.be/xn8EsW0wxyc?t=0))

## Hot takes
- Some companies claim their systems are private, but they are not.
- Feeding secrets to the LLM reasoning layer means they may end up in training data.
- Sandboxes and VMs are not a cure-all: internet access still allows data exfiltration.
- Teams should build their own agentic runtime to own the execution and reasoning layers.
- Confidential tool calls with end-to-end encryption are still an unsolved problem.

## Tools mentioned
Venice AI, OpenClaw, 1Password, HashiCorp Vault, Firecracker, AWS EC2, VPC, Qdrant, LanceDB, Cursor, Claude Code, MCP, JWT, TEE, Rig

## Relevance to our work
- **agentos** (2/3): The talk's secrets-flow and prompt-injection screening patterns match the L1 Govrix Scout scan and the L2C Crucible exec-gate. It also raises the logging leak issue for the Merkle audit log and telemetry. → *Audit what the proxy writes to logs and the Merkle audit trail: hash user IDs and strip credentials and prompts before they are stored, and check that the audit pipeline never receives raw secrets.*
- **prosharness** (2/3): ProsHarness already has zero-token credential handling, and the talk gives the same argument: keep credentials in the runtime and out of model context. Narrow tool scope and revocable handles also apply to the harness around Claude Code. → *Review ProsHarness credential flows against the runtime-holds-secrets pattern and check whether any credential, or any MCP tool outside the needed subset, can appear in model context.*
- **general** (1/3): Narrow tool scope and keeping context light are general agent practice, and the talk makes the point briefly. The rest is product pitch. → *When wiring an MCP server into an agent, limit it to the tools that the agent's task needs.*

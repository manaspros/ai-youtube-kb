# What if the network was the sandbox? — Remy Guercio, Tailscale

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `BM2JX9hqsVQ` · [watch](https://youtu.be/BM2JX9hqsVQ) · **date:** 2026-06-18 · **length:** 24:29 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Remy Guercio · **orgs:** Tailscale
- **topics:** sandboxing-execution, security-guardrails, governance-compliance, observability · **tags:** tailscale, wireguard, llm-gateway, identity, api-keys, oidc, github-actions, claude-code, budgets, tool-call-logging, tsnet, zero-key-sandbox

> Tailscale's Remy Guercio argues the network layer can act as an agent sandbox: identity-tagged WireGuard connections let an LLM gateway hold the provider key so the sandbox never has one, and every model call and tool call is visible and cuttable there.

## Summary
The speaker breaks a sandbox into two parts, a boundary and a set of permissions/identity, and says agents usually get credentials in one of two ways: a raw API key, or OAuth/OIDC, and both sit inside the sandbox where the agent can reach them. He proposes moving authn/authz to the network: Tailscale runs on WireGuard, and each connection carries the caller's user, groups, or tags, so access can be governed per connection and the receiving side also learns who is calling. On top of this Tailscale built "Aperture," an LLM gateway that holds one provider key and is itself a node on the tailnet; sandboxes such as a GitHub Actions runner get a tag through federated OIDC and need no key at all. A live demo showed per-identity usage, cost and full request/response logs for Claude Code, including that a simple "hello" with Claude Code's initial context cost about 20 cents, and tool calls logged by the gateway rather than the harness. Budgets and quotas apply across providers, webhooks fire on each tool call, and cutting off access is done at the network layer. Q&A covered the choice of the LLM layer over the MCP layer, since code-writing agents bypass MCP, and planned bash-command guardrails. The talk is partly a product pitch, but the architecture points are concrete and reusable.

## Key ideas
- **A sandbox is a boundary plus a set of permissions/identity.** — The speaker frames sandboxing with two basics: a clear in/out boundary and the identity/permissions the agent carries. Without permissions the sandbox has nothing useful inside it. ([0:51](https://youtu.be/BM2JX9hqsVQ?t=51))
- **Giving an agent an API key or OAuth login inside the sandbox leaves credentials where the agent can reach them.** — Raw API keys mean full price and no real authz. The speaker says models are clever with keys, especially in long loops. OAuth/OIDC is cheaper but the login still lives inside the sandbox. ([1:57](https://youtu.be/BM2JX9hqsVQ?t=117))
- **Put identity on the network connection itself.** — On a WireGuard-based tailnet, each connection carries the user, their groups, and tags for non-human callers such as a PR review bot. Access can be denied before a connection is made, and the receiving service also sees who is calling. ([3:47](https://youtu.be/BM2JX9hqsVQ?t=227))
- **A gateway holds one provider key; the sandbox only needs a base URL.** — Aperture stores a single Anthropic, OpenAI, Gemini, Vertex or Bedrock key. The sandbox connects over the tailnet with its tag and holds no key, so it cannot leak or misuse one. Claude Code, Codex and Gemini CLI were all shown working this way. ([5:55](https://youtu.be/BM2JX9hqsVQ?t=355))
- **Full request and response logs at the gateway give visibility a harness cannot.** — The demo showed per-user cost, per-model usage, and full request headers and bodies, including everything Claude Code sends on its first request. The gateway can extract every tool call, and it is not visible from inside the container or the harness. ([7:04](https://youtu.be/BM2JX9hqsVQ?t=424))
- **Cutting access happens at the network layer, not in the agent.** — Revoking the identity or key stops the agent. The speaker says the agent cannot route around it because it never had a key to try elsewhere. ([10:35](https://youtu.be/BM2JX9hqsVQ?t=635))
- **The LLM layer was chosen over the MCP layer because code-writing agents bypass MCP.** — Agents that write and run code or bash mostly skip MCP. The speaker says that at the LLM layer the gateway sees the commands, which is more useful than seeing only MCP calls. Planned guardrails will inspect bash commands. ([22:12](https://youtu.be/BM2JX9hqsVQ?t=1332))
- **Model drift shows up in logs of a fixed prompt over time.** — The speaker reruns a 10-word story prompt in Claude Code and says the topic moved from robots to dogs to cats over weeks. He suggests this as a signal for pipelines that rely on output format. ([17:25](https://youtu.be/BM2JX9hqsVQ?t=1045))

## Techniques
- **Zero-key sandbox behind an identity-aware gateway** — Keep provider keys only in a gateway node. Give each sandbox or CI runner a network identity (tag) and point the agent CLI at the gateway URL. Use federated OIDC from the CI platform to join the network with that tag. *When:* Agents running in CI runners or containers that need model access but must not hold credentials.
- **Per-identity budgets and quotas across providers** — Set spend limits by user, team or tag in the gateway, not per provider key. Combine team and individual limits (union of the two). *When:* Many developers or bots sharing several model providers, where one budget per key is not enough.
- **Per-tool-call webhooks for external policy** — The gateway calls a third-party endpoint for each tool call with the call details. The gateway does not depend on the agent to send them, so the hook always runs. *When:* Auditing or external approval of agent actions that the agent must not be able to skip.
- **Identity-aware internal services with tsnet** — Write a Go program that joins the tailnet with tsnet and reads the caller's identity from each connection. Use that identity in place of OAuth for internal MCP servers or APIs. *When:* Internal tools that should be reachable only by known users or agents, without building an OAuth flow.
- **Policy as code for network identity** — Define access in the ACL policy file, with application capabilities that send extra metadata with the identity. Manage it through GitOps or the API. *When:* Teams that want access rules versioned and reviewed like other infrastructure.

## Numbers
- A simple 'hello' in Claude Code with its initial context cost about 20 cents (the speaker's figure). ([8:17](https://youtu.be/BM2JX9hqsVQ?t=497))
- A PR review bot run on GitHub Actions cost 4 cents and ran three bash commands at once. ([9:16](https://youtu.be/BM2JX9hqsVQ?t=556))
- The dogfood PR review bot's activity over the last 30 days is visible in the gateway. ([9:16](https://youtu.be/BM2JX9hqsVQ?t=556))
- Example budget: $1,000 shared across providers for a team, or $5 per day per person (illustrative, not a benchmark). ([13:27](https://youtu.be/BM2JX9hqsVQ?t=807))
- Model used in the demo: Opus 4.6 with a 1M-token context window. ([11:56](https://youtu.be/BM2JX9hqsVQ?t=716))

## Hot takes
- API keys inside sandboxes are a poor fit for agents because capable models can misuse them over long loops.
- Visibility into agent actions belongs at the LLM/network layer, not in MCP, because code-writing agents mostly skip MCP.
- Transparent network interception of LLM traffic is deliberately not offered, since it breaks in confusing ways; the explicit base URL is the chosen design.

## Tools mentioned
Tailscale, WireGuard, Aperture, tsnet, Claude Code, Codex, Gemini CLI, GitHub Actions, Opus 4.6

## Relevance to our work
- **agentos** (2/3): Govrix Scout is already an LLM proxy with budgets and an audit log. The talk's model of a key-holding gateway plus per-identity budgets and full tool-call capture is close to it, and the zero-key-in-sandbox point is an argument for Crucible-style sandboxes. → *Check whether Govrix keeps provider keys only inside the proxy and identifies callers per request (not per key), and add extraction of tool_use blocks from responses to the audit log.*
- **prosharness** (2/3):  → *Prototype running Claude Code under ProsHarness with ANTHROPIC base URL pointed at a local proxy that holds the key, and record tool_use blocks there for checkpoint audit.*
- **general** (1/3): Relevant to agent-eval and drift monitoring, and to cost awareness for cheap-model pipelines, but the talk does not give methods beyond a single anecdote.

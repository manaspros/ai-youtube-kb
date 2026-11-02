# Agents Need Receipts, Not More Tool Calls - Armanas Povilionis, Alithea Bio

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Fu45geO3zX8` · [watch](https://youtu.be/Fu45geO3zX8) · **date:** 2026-08-18 · **length:** 19:36 · **format:** talk · **quality:** 2/5 · **depth:** practitioner
- **speakers:** Armanas Povilionis · **orgs:** Alithea Bio
- **topics:** security-guardrails, multi-agent, mcp-and-tools · **tags:** froglet, verifiable-receipts, signed-artifacts, agent-marketplace, agent-to-agent-payments, mcp, life-sciences, open-protocol, provenance, docker

> Armanas Povilionis (Alithea Bio) argues that cross-organization agent work needs signed, verifiable receipts, and demos Froglet, an open protocol for agents to discover, buy and verify services.

## Summary
The speaker, from life-sciences firm Alithea Bio, argues that scientific automation is collaborative across organizations, so adding more local tools to agents is not enough. He proposes giving agents budgets and the ability to find, negotiate with and pay external providers, with a verifiable chain of receipts for each step. His solution is Froglet, an open protocol that sits between existing payment rails, agent harnesses and transports rather than replacing them. Every Froglet node is the same software that can act as provider, requester or marketplace, and each node has a key pair so that every artifact in a quote, deal, execution and receipt is signed. Discovery goes through a marketplace, but after a requester picks a service the communication is direct between the two nodes. The live demo ran a trivial two-number addition service from a remote trial node and a local Docker node, with Claude calling it through a Froglet MCP server. The talk makes broad claims, such as bespoke collaboration costing millions and years, and the demo was a toy service, so the evidence is thin and the talk reads closer to a product pitch with a useful framing.

## Key ideas
- **Collaboration across organizations is the real bottleneck, not local tooling** — The speaker's analogy: a cook with better knives is local efficiency, while science is closer to a Michelin restaurant that depends on suppliers and repeatable quality. The gap is aligning a supply chain across siloed data, algorithms and compute, which needs verifiable receipts. ([1:25](https://youtu.be/Fu45geO3zX8?t=85))
- **Give agents budgets, not only tools** — He expects agents to manage their own budgets to discover services, request data, negotiate terms and pay for work across organizational boundaries, and to keep a record of what happened. He describes token budgets per task as a primitive version of this. ([3:34](https://youtu.be/Fu45geO3zX8?t=214))
- **Froglet is a thin interface layer that integrates rather than replaces** — It is an open protocol for discover, transact and receipt. It is meant to plug into different payment rails, agent harnesses, execution environments and transports. Nodes do not need the same software stack, only the same interface. ([5:04](https://youtu.be/Fu45geO3zX8?t=304))
- **One node binary with switchable roles, and signed chains** — A Froglet node can act as provider, requester or marketplace. A marketplace is just a node offering a listing service. Each node generates a key pair, every step is signed, and the chain counts as valid only if no data point was tampered with. ([7:38](https://youtu.be/Fu45geO3zX8?t=458))
- **Marketplace for discovery, direct peer connection for the deal** — Providers publish their services to a marketplace using the same protocol. Requesters query the marketplace for the list, then talk directly to the provider, so quote, deal, execution and receipt happen in one peer-to-peer interaction with no third party in the path. ([8:44](https://youtu.be/Fu45geO3zX8?t=524))
- **An LLM should be the main interface to the protocol** — Froglet is exposed as an MCP server or plugin in agent harnesses. The speaker says the primary human interface should be an LLM that drives usage as provider or requester, which keeps the protocol out of the model's context window. ([9:50](https://youtu.be/Fu45geO3zX8?t=590))

## Techniques
- **Signed per-step receipts for agent transactions** — Give each node a key pair at creation and sign every artifact in the quote, deal, execution and receipt sequence, so the full chain can be checked for tampering. *When:* Multi-party agent work where a result has to be trusted or audited by a party that did not run it.
- **Marketplace as discovery only, direct peer deals** — Providers publish listings to a shared marketplace. Requesters read the list from it, then negotiate and execute directly with the chosen provider. *When:* Discovering external services without routing every request and payment through a central broker.
- **Same node, role chosen at runtime** — One software build can run as provider, requester or marketplace. A single node can hold several roles at once, as shown by the demo node that was both provider and consumer. *When:* Reducing the number of distinct services to deploy in a small network of organizations.
- **Typed payload with schema and deal ID, polled asynchronously** — The requester builds a payload that names the service schema, the target provider and the input, submits it, gets a deal ID, and polls until the result is ready. *When:* Calling remote services whose execution time depends on load, such as a small cloud node.
- **Expose the protocol through MCP and let the LLM drive it** — Ship the node as an MCP server or harness plugin and have the agent perform discovery, invocation and checks via tool calls. The speaker asked Claude to check status, publish a service from a template and invoke it. *When:* When the agent should call external services without putting the protocol details into its context.

## Numbers
- Setting up a sharing and transaction flow costs a few thousand tokens and takes minutes (speaker's claim, not measured) ([10:55](https://youtu.be/Fu45geO3zX8?t=655))
- Bespoke closed-source scientific collaboration can take years and millions before any reusable workflow exists (speaker's claim, not measured) ([5:04](https://youtu.be/Fu45geO3zX8?t=304))
- Remote trial identity token lasts 15 minutes ([11:04](https://youtu.be/Fu45geO3zX8?t=664))
- Demo deal for 7 + 5 returned the correct answer 12 after a polling loop; no latency figures given ([12:05](https://youtu.be/Fu45geO3zX8?t=725))

## Hot takes
- Agents should be given budgets to buy services across organizations, not just better tools.
- Verifiable receipts, not more tool calls, are what make collaborative science with agents possible.
- The primary interface for humans to a protocol like this should be an LLM, not a dashboard.

## Tools mentioned
Froglet, MCP, Claude, Docker, OpenClaw, NemoClaw

## Relevance to our work
- **agentos** (1/3): AgentOS already has a Merkle audit log. Per-execution signed receipts that can be checked by a counterparty is a related idea, though Froglet targets cross-org trust rather than local audit. → *Skim the Froglet receipt format on froglet.dev and compare it with the Merkle audit log design for AgentOS governance.*
- **prosharness** (1/3): Checkpoint and resume of long runs could produce signed, tamper-evident checkpoint records, similar to the receipt chain described. → *Consider whether ProsHarness checkpoints should be hash-chained or signed so a resumed run can be verified.*
- **general** (1/3): The speaker's argument that multi-party agent work needs verifiable provenance is a useful framing, but the talk offers no evaluation and the demo is a toy service. → *Treat as background reading on agent provenance and do not adopt the protocol without an independent check of its signing scheme.*

# Security Firewall for Agents — Ryan Dahl, Deno

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `MkRYPFIMCSA` · [watch](https://youtu.be/MkRYPFIMCSA) · **date:** 2026-08-18 · **length:** 19:06 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Ryan Dahl · **orgs:** Deno, Brex, NVIDIA, Tailscale
- **topics:** security-guardrails, infra-cost-scaling, governance-compliance · **tags:** egress-proxy, agent-security, prompt-injection, credential-injection, policy-as-code, postgres-protocol, human-in-the-loop, llm-as-judge, tailscale, openclaw, claw-patrol, deno-deploy

> Ryan Dahl (Deno) on Claw Patrol, an open-source byte-level egress proxy that gates what production agents send to databases, Kubernetes and SaaS, with rules, credential injection and human or LLM approval.

## Summary
Ryan Dahl describes how Deno runs OpenClaw agents with broad read and write access to Postgres, Kubernetes, ClickHouse, AWS, GitHub and Slack to handle incidents for Deno Deploy. He argues that prompt-level alignment (he cites Opus refusing to delete a users table) is not a security boundary, because support-ticket content can prompt-inject the agent. His position is to treat the agent as untrusted software and gate the network bytes it emits, since subprocesses such as psql speak non-HTTP protocols that HTTP proxies and LLM gateways cannot see. He presents Claw Patrol, an MIT-licensed proxy that parses protocols such as Postgres, applies rules written in HCL (kept in Git, around 1,000 lines), injects credentials so the agent never sees secrets, and can route actions to a Slack approval or an LLM judge. A live demo of a blocked delete is shown in a recorded clip. The talk closes with testing via fixture requests and the view that backstop security is needed even as models improve.

## Key ideas
- **Agents with real production access are a security problem, and alignment is not enough** — Deno gives agents rewrite access to many systems because they resolve incidents well. Speaker says Opus refuses destructive requests, but security cannot rely on that, since support content can prompt-inject the agent. ([2:02](https://youtu.be/MkRYPFIMCSA?t=122))
- **Treat the agent as untrusted software and keep the guard outside it** — Agents run on standalone VMs, so file-level isolation matters less. What matters is network traffic, and the guard cannot live inside the agent because the agent can be manipulated. ([3:29](https://youtu.be/MkRYPFIMCSA?t=209))
- **Every consequential agent action is bytes on the wire** — Actions reach the network through MCP or through subprocesses like psql. Postgres is a non-HTTP protocol, so the guard must understand that protocol to see what is sent. ([4:32](https://youtu.be/MkRYPFIMCSA?t=272))
- **Scoped credentials alone leave holes when systems are composed** — Read-only credentials help, but an agent that can reach one system can tunnel through another (such as an EKS endpoint) to reach a protected database. Speaker says access composition creates holes. ([5:56](https://youtu.be/MkRYPFIMCSA?t=356))
- **Existing guard layers each cover only one slice** — LLM gateways guard only model traffic, HTTP proxies stop at HTTP, credential-injecting proxies hide secrets, and OS sandboxes target syscalls and file paths. None of these covers arbitrary protocols, which is the gap Claw Patrol targets. ([7:22](https://youtu.be/MkRYPFIMCSA?t=442))
- **A byte-level proxy in front of the agent, with rules and credential injection** — Claw Patrol parses each byte, applies protocol-aware rules to decide what leaves the agent, and holds production credentials so the agent process never sees them. The agent is a black box and needs no changes. ([10:13](https://youtu.be/MkRYPFIMCSA?t=613))
- **Verdicts go beyond allow and deny** — Rules can send an action to a Slack approval, to an LLM judge, or to a chain of both. This gives finer control than a simple block list. ([14:03](https://youtu.be/MkRYPFIMCSA?t=843))
- **Reuse existing network identity for the proxy** — The proxy runs as a Tailscale exit node and uses Tailscale identity for dashboard login, with WireGuard for non-Tailscale users. The speaker stresses that the proxy holds production credentials, so it has to be locked down. ([15:28](https://youtu.be/MkRYPFIMCSA?t=928))
- **Test the policy like code, with fixture requests as unit tests** — Each rule file ships with fixture requests that must always be blocked, and the proxy has its own large test suite. Policy changes are reviewed in Git. ([17:48](https://youtu.be/MkRYPFIMCSA?t=1068))

## Techniques
- **Byte-level egress proxy for agents** — Place a proxy between the agent host and the network. Parse the wire protocol (for example Postgres) and apply rules to each action, including ones reached via subprocess or tunnel. *When:* Agents spawn CLI clients such as psql or kubectl, or reach private databases through tunnels, and HTTP-only controls miss those paths.
- **Credential injection at the proxy** — The agent gets a placeholder. The proxy swaps in the real secret as the request leaves, so the agent process never holds the secret. *When:* An agent needs authenticated access but should not be able to leak or reuse credentials.
- **Policy-as-code in HCL with Git review** — Write permissions as a Terraform-style config file, check it into Git, and review each change. Attach fixture requests to rules as unit tests that assert a given request is blocked. *When:* Many services share one permission model and changes need an audit trail and regression tests.
- **Chained verdicts: rule, LLM judge, then human approval** — Let rules decide allow or deny. For ambiguous actions, send them to an LLM judge, then to a Slack approval, with combinations allowed. *When:* Actions are risky but not clearly forbidden, so a human or judge should decide.
- **Network-level placement with existing identity** — Run the proxy as a Tailscale exit node so agents route through it. Use Tailscale identity for dashboard access to avoid a second auth layer. Offer WireGuard for others. *When:* The team already runs a private mesh network and wants no extra login system.

## Numbers
- Rules file is about 1,000 lines of HCL, managed in Git with per-change review ([11:14](https://youtu.be/MkRYPFIMCSA?t=674))
- Agents at Deno already resolve many incidents that previously needed a human SRE in the loop (no figure given) ([2:02](https://youtu.be/MkRYPFIMCSA?t=122))
- Opus repeatedly refused a request to delete the users table in the speaker's tests (qualitative, no count) ([2:02](https://youtu.be/MkRYPFIMCSA?t=122))

## Hot takes
- Security cannot be wishful thinking that the model will obey instructions.
- Agents cannot be trusted to police themselves, including security plugins or changes made inside the agent software.
- We will never be able to fully trust AIs, so backstop security mechanisms will always be needed even as models improve.

## Tools mentioned
OpenClaw, Claw Patrol, Deno Deploy, PostgreSQL, Kubernetes, ClickHouse, AWS (Sigv4), GitHub, Slack, PagerDuty, HCL, Terraform, Tailscale, WireGuard, Agent Vault, HTTP Jail, Crab Trap, NVIDIA OpenShell, LiteLLM, OpenRouter, Claude Opus

## Relevance to our work
- **agentos** (2/3): AgentOS L1 Govrix Scout is an LLM proxy with PII and injection scanning. This talk shows the gap: agent traffic to Postgres, ClickHouse and other non-HTTP protocols is not covered by LLM proxies. → *Scope a Govrix Scout extension that parses Postgres (and later ClickHouse) wire protocol with rule-based denial, and add a fixture-test suite per rule file to validate it.*
- **prosharness** (2/3): ProsHarness already has zero-token credential handling and phone-driven approvals. The talk's credential-injection proxy and Slack or LLM-judge approval chain map directly onto both features. → *Prototype a ProsHarness egress step where the Claude Code subprocess gets placeholder credentials and a local proxy injects real secrets, with approvals routed through the existing phone flow.*
- **general** (1/3): Policy-as-code with fixture tests and chained allow, judge and human verdicts is a reusable pattern for any agent with production access. → *Note the fixture-as-unit-test pattern for policy rules when designing any future permission config.*

# Auth for Agents: Let AI Sign Up for Your Product with auth.md — Michael Grinich, WorkOS

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `nSkmXakJ6eo` · [watch](https://youtu.be/nSkmXakJ6eo) · **date:** 2026-10-12 · **length:** 21:13 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Michael Grinich · **orgs:** WorkOS, Cloudflare, Salesforce, Y Combinator, PostHog
- **topics:** security-guardrails, mcp-and-tools, product-ux · **tags:** auth.md, agent registration, agent identity, ID-JAG, MCP limits, harness engineering, agent sign-up, free tier, human custody, open spec

> WorkOS founder argues agents need their own sign-up step, and proposes auth.md, an open markdown spec that tells an agent how to register for a service without a human clicking through.

## Summary
The speaker, WorkOS founder Michael Grinich, says agents now write most code and run for hours, so the bottleneck is the human's attention. He argues that agents also need to become customers, but sign-up flows are built for humans (CAPTCHAs, email verification, card entry, copy-paste API keys), and MCP solves tools and context but not registration. His proposal is auth.md, a spec in which a service publishes registration instructions: accepted identity proofs, auth flows, scopes, free-tier limits and how a human can claim the account later. He shows a demo where an agent finds a provider that advertises auth.md, sends a signed identity assertion (ID-JAG), receives an API token, and deploys with only approvals from the human. He says payment should come downstream of usage rather than upfront, and that the spec is open even though WorkOS hosts a version. The talk is partly a product pitch, so the design ideas matter more than the claims about the market.

## Key ideas
- **Agents are a new class of consumer, so products should be built for agents as well as humans.** — Speaker says agents can spawn faster than people sign up, and many will choose vendors on a user's behalf (email, deploy, storage). He suggests changing the saying 'make something people want' to also include 'make something agents want'. ([6:07](https://youtu.be/nSkmXakJ6eo?t=367))
- **Sign-up flows are the blocker because they assume a human at every step.** — Login and sign-up pages are hardened against bots (CAPTCHAs, email verification, card entry, copy-paste API keys, dashboards). Agents usually have no email address, so the speaker says registration is the missing primitive. ([7:40](https://youtu.be/nSkmXakJ6eo?t=460))
- **Harness engineering: the model is an engine, and the agent needs a harness around it.** — He lists what an agent needs to run: a safe sandbox, tools, context, a way to check its own work (feedback), and human review. A strong model with a poor harness is not effective. ([3:41](https://youtu.be/nSkmXakJ6eo?t=221))
- **MCP handles tools and context but not registration, and it still needs a human to consent.** — Today a user adds an MCP server and signs in with their own credentials. Speaker wants registration to happen without the human involved, or at least not at first. ([9:12](https://youtu.be/nSkmXakJ6eo?t=552))
- **auth.md is a narrow spec: a markdown file that tells an agent how to register, built on existing auth standards.** — It states what the service does, how to register, which identity proofs are accepted, which auth flows are supported, what scopes exist, and what free-tier limits apply. He deliberately leaves out broader agent identity and permissions. ([10:44](https://youtu.be/nSkmXakJ6eo?t=644))
- **A live demo: the agent discovers auth.md, mints an identity assertion, gets a token, and deploys with only approvals.** — The agent looked for services that advertise auth.md support, picked Cloudflare, sent an ID-JAG signed credential, received an API token, and set up Wrangler and deployment. He says his prompts were only approvals. ([14:18](https://youtu.be/nSkmXakJ6eo?t=858))
- **Monetise later: let agents use the product first, then pay on the provider's own terms.** — He argues for free tiers and downstream payment instead of forcing a credit card at sign-up. The provider sets limits per product, and a human or organisation can claim the account afterwards. ([17:15](https://youtu.be/nSkmXakJ6eo?t=1035))

## Techniques
- **auth.md registration spec** — Publish a markdown file that tells registering agents the sign-up steps, accepted identity proofs, supported auth flows (SSO, email, MFA), scopes, free-tier caps, and how a human later claims the account. Agents discover it when a service advertises support. *When:* You want agents to sign up for your service without a human in the loop, and you want the rules written in one place the agent can read.
- **Identity assertion exchange for agent sign-up** — The agent mints a signed identity assertion (ID-JAG in the talk) that represents the user, sends it to the service's registration endpoint, and receives an ordinary API token. Normal APIs and MCP calls work unchanged after that. *When:* The agent must get API access for a new service and the provider needs to know which user is behind it, but you do not want the user to sign up manually.
- **Risk-scored registration with time-boxed free access** — Assess each registering agent's risk, either from the user identity it brings or from out-of-band verification. Give limited free capacity (the example was a 72-hour deploy window) and widen it after verification or payment. *When:* You want to let good agents in without opening the door to abuse, and to match free limits to what each product costs you.
- **Deferred human claim** — Let the agent create the account first, and let a human or organisation claim custody of it later through the registration flow. *When:* Agents create resources on a user's behalf and the user or company needs to own them afterwards.
- **Approval-only supervision** — Give the agent one clear build request, then approve each step it asks for, without writing a long plan first. *When:* The task is a well-scoped prototype where a running result is more useful than an upfront plan. Speaker's own example, not a measured method.

## Numbers
- Example free-tier window in the demo: a deploy allowed for 72 hours before verification or payment (an example the speaker chose, not a measured figure). ([14:18](https://youtu.be/nSkmXakJ6eo?t=858))
- Automated web traffic has been treated as bad for about 20 to 30 years, which is why CAPTCHAs and bot defences are so strict. ([6:07](https://youtu.be/nSkmXakJ6eo?t=367))

## Hot takes
- MCP is not enough: it connects tools and context but does not solve the registration step.
- CAPTCHAs are effectively dead, and the industry is trying to go backwards by letting browser agents break them.
- Payment should come after agent usage, not at sign-up; forcing a credit card up front is backwards.
- Build for agents at least as much as for people, since agents will choose vendors on users' behalf.
- Markdown files are the future, said half-jokingly about the auth.md format.

## Tools mentioned
auth.md, MCP, ID-JAG, Wrangler, Pi (agent harness), Claude, OpenClaw, x402, Cloudflare

## Relevance to our work
- **general** (2/3): 
- **agentos** (1/3): AgentOS sits in front of agent traffic and enforces budgets and PII scans, but it has no sign-up or registration step. The talk's identity-assertion idea could matter only if budgets are later keyed to a per-agent identity. → *Read the auth.md open spec the speaker mentions and note whether AgentOS budgets could key on a per-agent identity assertion instead of a static API key.*
- **prosharness** (1/3): ProsHarness already gates approvals from a phone and handles credentials. The talk argues the human should approve at steps, not drive each one, which is a weak signal for approval design. → *Compare ProsHarness approval gates with the talk's approve-only flow to see which approval steps could be batched.*

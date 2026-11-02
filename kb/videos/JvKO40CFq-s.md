# Full Workshop: Better Auth — Paola Estefania, Better Auth

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `JvKO40CFq-s` · [watch](https://youtu.be/JvKO40CFq-s) · **date:** 2026-08-18 · **length:** 40:56 · **format:** workshop · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Paola Estefania · **orgs:** Better Auth
- **topics:** security-guardrails, mcp-and-tools, governance-compliance · **tags:** agent identity, capabilities, authorization, OAuth, device flow, revocation, audit logs, OpenAPI, MCP, principal, hire your agent, agent directory

> Paola Estefania (Better Auth) argues agents should get their own identity and scoped capabilities instead of borrowing user credentials, and demos a draft open protocol with approvals, audit logs and revocation.

## Summary
The speaker opens by asking who gives AI agents their personal credentials, and argues that acting as the user is the wrong model; the agent should instead get its own authority, like a hired employee who is not handed the CEO's login. She describes three problems to solve: discovery (how an agent finds what a service can do), scoped authorization (grant specific actions, not broad read or write), and identity (so logs show which agent did what for which user, and so access can be revoked). For discovery she proposes a well-known configuration endpoint for services that adopt the protocol, and until then a directory that converts OpenAPI endpoints into named capabilities that intents are matched against. For identity, each agent gets its own key pair and signs its own tokens, with the host the session runs from also recorded. The live demo connects an email-reader agent through a device-style approval, shows read-only defaults, requires a separate approval to send an email, and revokes the agent so later requests fail. The protocol is the speaker's own open draft from February, so the claims about it are promotional, and the talk is a workshop with audience Q&A rather than measured results.

## Key ideas
- **Give agents their own authority, not your credentials** — Acting with the user's token makes the agent pretend to be the user. The speaker's analogy: a hired worker gets their own access, not the CEO's login. Scope the agent's grants instead. ([2:51](https://youtu.be/JvKO40CFq-s?t=171))
- **Agents need a discovery directory** — Today people wire up each tool by hand. The proposal is a phone-book-style directory where an agent looks up what a service can do and how to call it, without manual setup. ([4:20](https://youtu.be/JvKO40CFq-s?t=260))
- **Grant per action, not broad access** — A Gmail connection that is read-only by default should still allow a specific grant for send or delete. Each tool or action gets a yes, no or always-deny decision. ([6:42](https://youtu.be/JvKO40CFq-s?t=402))
- **Identity makes logs and revocation possible** — If each agent has an identity, logs can answer which agent did what, when, and for which user. Revoking one agent should cut its access without disconnecting the whole user. ([7:50](https://youtu.be/JvKO40CFq-s?t=470))
- **Capabilities are narrower than scopes** — A scope such as read is coarse. A capability names one action, and the user's intent is matched to capabilities. The speaker says constraints such as maximum run time or time windows can also be attached. ([13:20](https://youtu.be/JvKO40CFq-s?t=800))
- **Services without the protocol can be bridged with OpenAPI** — Until services adopt the well-known configuration endpoint, the directory translates their OpenAPI endpoints into capabilities (GET, POST, DELETE and so on). The speaker says this is a stopgap. ([14:41](https://youtu.be/JvKO40CFq-s?t=881))
- **Agent as principal, with its own signed tokens** — Per-agent key pairs let the agent sign its own tokens. Logs then show the agent acting for a user, not hiding behind the user. Revoking the agent alone is not enough: its access tokens must also be deleted. ([16:56](https://youtu.be/JvKO40CFq-s?t=1016))
- **Read by default, approve writes on the fly** — The host grants read capabilities automatically. A send action triggers a separate approval, here shown as an out-of-band approval instead of a redirect. A denied request stays denied. ([28:11](https://youtu.be/JvKO40CFq-s?t=1691))
- **The directory is a matcher, not a data-path proxy** — The speaker says a real proxy would not scale because it sits on the data path. The directory only matches intent to capabilities and returns logs; it does not carry the traffic. ([34:27](https://youtu.be/JvKO40CFq-s?t=2067))

## Techniques
- **Per-agent identity with own key pair** — Each agent gets its own key pair attached to the user it works for. The agent signs its own tokens, and every action is logged with agent ID, user ID and host ID. *When:* When several agents act for one user and you need per-agent audit trails and the ability to revoke one agent alone.
- **Capability grants with default-read policy** — The host auto-grants read-only capabilities. Write or delete capabilities need a separate, explicit approval. Constraints such as time windows or max duration are attached to each grant. Policies can be set per user or per host. *When:* When an agent connects to a sensitive service such as email, calendar or a drive, and you want safe defaults without an approval prompt for every read.
- **Device-flow approval for agents** — Treat the agent as a separate device. It requests a code, the user approves it on another channel, and the agent gets a token. The demo uses an async approval from a second device instead of a browser redirect. *When:* When a headless or local agent needs user consent and cannot open a browser redirect itself.
- **OpenAPI-to-capability translation** — Parse a service's OpenAPI JSON, turn each endpoint into a named capability, and list it in the directory. Map intents from the user's request to those capabilities. *When:* When a service has an OpenAPI spec but does not yet publish agent-specific capability metadata.
- **Full revocation: agent, host and tokens** — Revoke the agent entity, mark the host as unauthorized, and delete outstanding access tokens. Check that a later request fails and a new grant is needed. *When:* When an agent misbehaves and you need to cut its access immediately, including tokens already issued.

## Numbers
- The Gmail directory entry lists about 20 capabilities (spoken as '20 list of capabilities'; approximate). ([14:41](https://youtu.be/JvKO40CFq-s?t=881))
- The protocol draft was first started in February; the speaker says a new draft covering long-lived agents and policies is about to be released. ([20:55](https://youtu.be/JvKO40CFq-s?t=1255))

## Hot takes
- Agents should never be given the user's own credentials; agents should be principals with their own identity.
- Read-only access should be the default for agents, and sends or deletes should always need an explicit approval.
- A proxy is a bad idea for agent authorization because it sits on the data path and does not scale; a directory is enough.

## Tools mentioned
MCP, OAuth, OpenAPI, OIDC, Gmail, Notion, Claude, Cursor

## Relevance to our work
- **agentos** (2/3):  → *Add an agent_id and host_id to every proxied request in the Govrix audit log, separate from the user ID, and add a test that revoking one agent blocks its next call while the user's other agents still work.*
- **prosharness** (2/3): ProsHarness has phone-driven approvals and zero-token credential handling, and this talk covers device-flow approvals, read-by-default grants and token revocation. → *Split ProsHarness approvals into per-capability grants (read by default, write or send needs a phone approval) and check that revoking a run deletes its issued tokens as well as ending the session.*
- **general** (2/3): 

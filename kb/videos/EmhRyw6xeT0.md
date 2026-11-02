# One Login to Rule Them All: Cross-App Access for MCP — Garrett Galow, WorkOS

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `EmhRyw6xeT0` · [watch](https://youtu.be/EmhRyw6xeT0) · **date:** 2026-05-18 · **length:** 23:24 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Garrett Galow · **orgs:** WorkOS, Okta, Figma, Cursor, Anthropic, OpenAI, Microsoft
- **topics:** security-guardrails, mcp-and-tools, enterprise-adoption · **tags:** mcp-auth, oauth, sso, cross-app-access, id-jag, okta, identity, consent-fatigue, scim, revocation, dcr, cimd

> Garrett Galow (WorkOS) explains cross-app access (XAA): the enterprise IdP brokers silent, short-lived MCP tokens so users stop clicking consent screens and IT regains revocation and visibility.

## Summary
Garrett Galow of WorkOS argues that MCP's OAuth setup forces a consent screen for every server, which multiplies into large team-wide friction, while the IT team loses visibility over which MCP servers and clients are used. He points to standing access and refresh tokens that survive offboarding or a compromised laptop unless SCIM is in place. His proposed fix is cross-app access, where the company IdP acts as trust broker: the client exchanges the user's SSO session for an ID-JAG token for a target audience, then trades that for a normal short-lived MCP access token. He walks through a live Claude Code demo where Figma connected with no consent click, and lists the IT, client and server changes needed. He is clear the scheme handles authentication only, with permissions still coming from the target app, and that scopes and some IdPs (Entra, SAML) are not yet covered. The talk is partly a pitch for WorkOS, which runs auth for Cursor and Anthropic, so the claims are the speaker's own.

## Key ideas
- **MCP's OAuth flow forces a consent screen per server, and that cost multiplies across a team.** — Users connect many MCP servers and approve each one. Across dozens of developers this becomes real time lost. The speaker says the root cause is that MCP ignores the single sign-on the company already has. ([1:08](https://youtu.be/EmhRyw6xeT0?t=68))
- **IT has no visibility into which MCP servers, clients and agents are in use.** — MCP connections bypass the IdP, so IT cannot tell which servers a person uses, which clients they run (for example a non-approved agent), or which sensitive data sources (Figma, Notion) those clients can reach. ([3:59](https://youtu.be/EmhRyw6xeT0?t=239))
- **Standing tokens outlive the user's access, which is the real security gap.** — Revoking SSO does not kill the access and refresh tokens already held by MCP clients. Without SCIM, access can last days, weeks or months. The speaker describes his own laptop being compromised and having to hunt for every credential it held. ([4:59](https://youtu.be/EmhRyw6xeT0?t=299))
- **Cross-app access uses the IdP as a trust broker between apps that already trust it.** — The client and the target app both trust the same IdP, so the IdP can issue a credential the target accepts, with no human consent step. The speaker calls this XAA. ([6:13](https://youtu.be/EmhRyw6xeT0?t=373))
- **The flow has four parties and two invisible steps.** — The client (Claude Code) holds the user's ID and refresh tokens from the IdP login. It asks the IdP for an ID-JAG token aimed at the target. The target's auth server checks that token and returns a normal OAuth access token. The final step is the normal MCP call. ([9:47](https://youtu.be/EmhRyw6xeT0?t=587))
- **Short-lived access tokens let revocation work without a human.** — Access tokens last about five minutes. The client re-runs the ID-JAG exchange whenever one expires, as long as the SSO session is alive. If IT locks the Okta session, the next expiry cuts off MCP access. The user logs into the IdP only about once a day or week, per company policy. ([11:46](https://youtu.be/EmhRyw6xeT0?t=706))
- **Adoption needs work on both the client and the MCP server.** — IT adds a managed-connection policy saying which client may request access to which target. The client needs XAA-compatible SSO and a token exchange. The server must accept the JWT bearer grant type, verify the ID-JAG with the IdP, and then issue its normal token. The speaker says WorkOS does this for Cursor and Anthropic. ([13:16](https://youtu.be/EmhRyw6xeT0?t=796))
- **XAA covers authentication, not authorization or scopes.** — The user still gets only the permissions they hold in the target app. Scoped grants are not in the spec yet. Audience URLs (for example the MCP host) are how the IdP maps a target to an app, and the speaker says audience is not a scope mechanism. ([16:06](https://youtu.be/EmhRyw6xeT0?t=966))
- **Ecosystem support is patchy, and clients without DCR must be pre-registered.** — Okta supports XAA for OIDC connections today, with SAML promised. Microsoft Entra does not yet support it. Some clients lack dynamic client registration, so they must be registered in advance. The speaker presents CIMD as the successor, a metadata document that defines clients up front. ([22:40](https://youtu.be/EmhRyw6xeT0?t=1360))

## Techniques
- **Cross-app access via ID-JAG token exchange** — The client keeps the user's IdP refresh or ID token. It asks the IdP for an identity JWT authorization grant (ID-JAG) tied to the target audience. It then sends that grant to the target's auth server, which validates it with the IdP and returns a standard access token. *When:* Many users connect to SSO-managed MCP servers and you want silent, centrally revocable access without per-tool consent screens.
- **IdP-side allow-list for app-to-app access** — The admin declares in the IdP's managed-connections portal which client app may request access to which target app. Users still need membership in both apps. *When:* You want to control which agents or clients can reach which tools, and have that policy live in the IdP rather than in each MCP config.
- **Short-lived access tokens with silent re-mint** — Keep access tokens around five minutes. When one expires, repeat the ID-JAG exchange while the SSO session is valid. Revocation at the IdP then takes effect at the next expiry. *When:* You need fast revocation for agent or MCP access and do not want to depend on SCIM.
- **Audience URL as the routing key** — Identify each target by an audience URL (for example the MCP server host). Map that audience to the app in the IdP, so the client asks for an audience and the IdP answers with the matching app. *When:* One IdP fronts several MCP servers and you need to route token requests without per-app client config.
- **Server-side ID-JAG acceptance** — Advertise the JWT bearer grant type, accept ID-JAG tokens, verify each one against the IdP, then issue the normal access token. *When:* You run an MCP server that enterprise customers will call from SSO-managed clients.

## Numbers
- Users connect a half dozen to a dozen MCP servers, each with its own consent screen, and this repeats across dozens of team members. ([1:08](https://youtu.be/EmhRyw6xeT0?t=68))
- Standing access from MCP tokens can last days, weeks or months after offboarding when SCIM is not used. ([4:59](https://youtu.be/EmhRyw6xeT0?t=299))
- Access tokens for most apps are around five minutes, and the user re-logs into the IdP only about once a day or once a week, depending on IT policy. ([11:46](https://youtu.be/EmhRyw6xeT0?t=706))
- Okta supports XAA for OIDC connections only today. SAML is promised, and Microsoft Entra does not yet support it. ([18:44](https://youtu.be/EmhRyw6xeT0?t=1124))
- CIMD, the successor to DCR, is described by the speaker as about three months old, with little ecosystem support yet. ([22:40](https://youtu.be/EmhRyw6xeT0?t=1360))

## Hot takes
- MCP's consent screens on top of consent screens are a symptom of OAuth's two-systems-don't-trust model, which SSO has already moved past.
- Standing access tokens that survive revocation are a bigger security risk than the consent-click annoyance.
- Claude is very good at explaining specs, so it is a good way to learn the ID-JAG spec without reading the IETF text.

## Tools mentioned
MCP, Claude Code, Cursor, Okta, Figma, WorkOS, Microsoft Entra, SCIM, CIMD, DCR, OAuth, OIDC, SAML, ID-JAG

## Relevance to our work
- **general** (2/3): 
- **agentos** (1/3): AgentOS's L1 proxy holds budgets and PII scanning, but has no per-user identity layer for MCP tools; this talk only touches on it. → *Note the ID-JAG flow as reference if AgentOS ever needs per-user auth on MCP tool calls. No code change now.*
- **prosharness** (1/3): ProsHarness keeps credentials out of tokens (zero-token handling), and the talk argues standing refresh tokens are the main leak risk. The talk does not change the harness design. → *Check whether ProsHarness's stored Claude Code and MCP credentials can be revoked centrally, or whether they are standing tokens that outlive a session.*

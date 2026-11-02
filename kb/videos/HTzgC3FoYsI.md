# Let Anyone at Your Company Ship Internal Apps with AI — Garrett Galow, WorkOS

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `HTzgC3FoYsI` · [watch](https://youtu.be/HTzgC3FoYsI) · **date:** 2026-10-09 · **length:** 17:13 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Garrett Galow · **orgs:** WorkOS, Cloudflare, Okta, Doppler, Webflow, Lovable, Snowflake
- **topics:** vibe-coding-app-building, enterprise-adoption, governance-compliance · **tags:** internal-apps, non-engineers, secure-by-default, sso, cloudflare-workers, cli-scaffolding, shared-skills, app-registry, hackathon, secrets-management, audit-logs, claude-code

> WorkOS's Garrett Galow on a CLI, a Cloudflare-based platform and SSO-by-default that let non-engineers build and ship internal apps; 37% of about 60 apps had no engineer commits.

## Summary
Garrett Galow (WorkOS product team) explains that building an app got cheap with AI coding tools, but shipping it internally still required engineers for hosting, auth, secrets and provisioning. The story starts with an account executive whose Lovable prototype her CEO could not open, which led to two engineers rebuilding it. WorkOS responded with a "WoW" CLI that prepares a laptop (git, Node, GitHub, Doppler), creates a repo from a template and deploys it, plus a shared skills repo and company-wide one-day "Claude days" hackathons that pair non-engineers at the keyboard with engineers as consultants. The underlying platform, Atlas, runs on Cloudflare Workers with D1 and KV, puts every app behind Okta SSO by default, auto-hosts under a shared workers domain, logs all requests and keeps secrets in Doppler. He reports about 278 registered apps, over 3 million requests a week, and 37% of roughly 60 maintained apps built with no engineer commits. The talk closes with gaps (group/role permissions, data connectors, Slack install) and a sales pitch for the platform.

## Key ideas
- **Building got cheap but shipping did not** — The bottleneck moved from writing the app to hosting, auth, secrets and provisioning. A non-engineer's prototype stalled at access, so engineers had to rebuild it. ([1:41](https://youtu.be/HTzgC3FoYsI?t=101))
- **Two hard requirements: build without asking infra, and share by link** — Anyone should be able to build and deploy without infra provisioning or security approval for standard apps. Colleagues should open a shared link in Slack behind login, with no extra red tape. ([3:12](https://youtu.be/HTzgC3FoYsI?t=192))
- **A pre-flight CLI removes setup friction for non-engineers** — The WoW CLI checks for git, Node, GitHub login and Doppler, creates a repo from a template in the enterprise GitHub, and deploys a Node app in one command. It is pushed to every laptop through MDM on day one. ([4:38](https://youtu.be/HTzgC3FoYsI?t=278))
- **Hackathons pair non-engineers with engineers to get feedback** — Company-wide one-day Claude days pair teams so the non-engineer drives and the engineer only unblocks. The events generated the feedback loop that showed what worked. ([4:38](https://youtu.be/HTzgC3FoYsI?t=278))
- **Atlas: infra invisible, secure by default, discoverable** — Three principles: the deploy target can change (Cloudflare today, Vercel or AWS later) without users noticing; every app sits behind Okta SSO by default because many hold PII; every app is listed in a catalog and shareable by link. ([11:00](https://youtu.be/HTzgC3FoYsI?t=660))
- **Shared skills repo that anyone can push to and fetch from** — Employees publish useful skills so others can discover and pull them to build apps or run workflows. ([6:11](https://youtu.be/HTzgC3FoYsI?t=371))
- **Registry and audit by default** — Every push is logged to an internal registry. All traffic is logged and auditable, and secrets go into Doppler rather than repos. Token-based auth is an opt-in path for APIs and Slack bots. ([8:28](https://youtu.be/HTzgC3FoYsI?t=508))
- **Success metric is apps built with zero engineer commits** — Of about 60 maintained apps, 37% were built with no engineer in any commit. He treats this as proof that engineers are no longer needed to migrate or maintain tools for sales and marketing. ([14:13](https://youtu.be/HTzgC3FoYsI?t=853))

## Techniques
- **Pre-flight local setup CLI with template scaffolding** — One create command checks git, runtime, git-host login and secrets tooling on the laptop, creates a repo from a standard template, pushes it and runs a deploy step so the app is live locally and remotely. *When:* Onboarding people who are not engineers onto a standard stack, so that agent-built projects start from a known-good configuration.
- **SSO gate on every deployed app by default** — All apps under the shared domain require the corporate identity provider login. Token-based auth is added as an explicit opt-in for APIs and bots, and every request is logged. *When:* Internal tools that touch sensitive data where per-app security review would block non-engineers.
- **Platform abstraction over deploy target** — Hide the compute target behind the platform layer. Provide per-app storage (D1 databases, KV) and secrets through the platform so builders do not provision them. *When:* You want non-expert builders to ship without knowing the infrastructure, and may need to switch providers later.
- **Pair non-engineer driver with engineer consultant in timed hackathons** — A one-day event pairs a non-engineer at the keyboard with an engineer who only unblocks. Use the output to collect feedback on the tooling. *When:* Early stage of an internal platform, to find out where non-experts get stuck with agent tools.
- **Push-to-register catalog with shared skills** — Each pushed app is recorded in an internal registry with usage counts. Skills are published to a shared repo that others fetch and discover. *When:* Building a company-wide catalog of agents, skills and tools that people can find without asking.

## Numbers
- 278 apps pushed to the internal registry; 21 with a deployment today ([8:28](https://youtu.be/HTzgC3FoYsI?t=508))
- About 3.3 million requests over the last week across internal apps ([8:28](https://youtu.be/HTzgC3FoYsI?t=508))
- 60 apps on custom branded domains ([8:28](https://youtu.be/HTzgC3FoYsI?t=508))
- About 60 apps deployed, maintained or used regularly; over 3 million requests a week (about 14:13 restated) ([16:13](https://youtu.be/HTzgC3FoYsI?t=973))
- 37% of the ~60 active apps were built with no engineer in any commit ([14:13](https://youtu.be/HTzgC3FoYsI?t=853))
- Problem history: idea about 6 to 8 months before the talk, Lovable prototype blocked on access ([0:12](https://youtu.be/HTzgC3FoYsI?t=12))

## Hot takes
- Once building is cheap, the real bottleneck is shipping: hosting, auth, secrets and provisioning.
- Secure-by-default (SSO on every app) can remove the need for per-app security approval for standard internal tools.
- Measure success by the share of apps with no engineer commits, not by how many apps exist.
- Presenting the platform as a sales pitch: the talk ends with an offer to sell Atlas to other companies.

## Tools mentioned
Claude Code, Codex, Lovable, Cloudflare Workers, Cloudflare D1, Cloudflare KV, Doppler, Okta, GitHub, Webflow, Slack, Node.js, Snowflake, MDM, Vercel, AWS

## Relevance to our work
- **agentos** (1/3): Secure-by-default SSO gate plus per-request audit logs on every deployed app is a governance pattern similar to the L1 proxy audit trail, but it is an SSO and hosting approach rather than a model proxy. → *Read the approach as a reference for AgentOS governance: a default identity gate and audit trail on every agent-built app, without changing code yet.*
- **prosharness** (1/3): A shared skills repo with push and fetch commands is a distribution model for skills that ProsHarness ranks, but the talk gives no ranking or evaluation details. → *Look at a push and fetch skills repo as a distribution option for ProsHarness skill ranking, if skill sharing across users comes up.*

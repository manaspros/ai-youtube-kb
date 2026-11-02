# Stop Building Login Systems… Use This Instead (Authentik)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `LVuspKy4P2w` · [watch](https://youtu.be/LVuspKy4P2w) · **date:** 2026-05-02 · **length:** 5:35 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Authentik, Keycloak, Authelia, Okta, Auth0
- **topics:** security-guardrails, dev-tools · **tags:** self-hosted, sso, oauth, oidc, mfa, passkeys, identity-provider, docker-compose, kubernetes, authentik, homelab

> Short walkthrough of Authentik, a self-hosted open-source identity provider for SSO, OAuth login and MFA across your own apps, with a Docker Compose quick start and a take on its costs versus Keycloak, Authelia, Okta and Auth0.

## Summary
The speaker argues that per-service logins and patchwork auth become painful in self-hosted stacks, and proposes Authentik as one identity provider for SSO, MFA and user management. The demo starts a fresh server with a single Docker Compose command, creates an OAuth2 provider and app in the admin UI, points a dummy app at it, and logs in with a user created in the UI. The speaker positions Authentik between heavyweight Keycloak and lightweight Authelia, and against Okta and Auth0, which he calls polished but costly at scale. Customization uses a visual flow builder and Python policies rather than XML or SAML config. Downsides he names are a learning curve, roughly 2 GB of RAM, a single point of failure without high availability, and a paid tier for large scale. The video is brief and promotional in tone, and the demo covers only OAuth login, not the MFA or passkey features the intro promises.

## Key ideas
- **Self-hosted identity provider to replace scattered per-app auth** — Authentik is pitched as one login system for every app: SSO, MFA, user management and access control in one place, instead of each service handling auth on its own or stitching tools together. ([0:00](https://youtu.be/LVuspKy4P2w?t=0))
- **Quick start is one Docker Compose command plus the admin UI** — On a fresh server, a single docker compose up brings Authentik up. From the admin UI you create an app and attach an OAuth provider, which the speaker says takes under 30 seconds. ([0:53](https://youtu.be/LVuspKy4P2w?t=53))
- **Customization through flow stages and Python policies, not XML/SAML config** — Login logic is built as visual flow stages, and Python policies cover cases that config cannot. The speaker presents this as the main difference from enterprise IdPs. ([0:53](https://youtu.be/LVuspKy4P2w?t=53))
- **Demo is an OAuth login for a dummy app in about 90 seconds** — A test app gets a redirect URL (localhost), the client ID and secret from Authentik, and a user created in the UI. Logging in as that user, not the admin, is the proof of concept. ([2:11](https://youtu.be/LVuspKy4P2w?t=131))
- **Positioning: between Keycloak, Authelia and Okta/Auth0** — Keycloak is called powerful but legacy-heavy, Authelia lightweight but outgrown quickly, and Okta/Auth0 polished but paid per user. Authentik sits in the middle with full identity management and a visual flow builder, though a paid tier applies at scale. ([2:11](https://youtu.be/LVuspKy4P2w?t=131))
- **Costs and trade-offs: RAM, learning curve, single point of failure** — The speaker cites roughly 2 GB of RAM, a confusing first install, and a single point of failure unless high availability is set up. He says it is heavier than ultra-lightweight tools. ([3:37](https://youtu.be/LVuspKy4P2w?t=217))
- **Best fit is self-hosted stacks that need SSO and MFA everywhere** — He recommends it for homelabs, internal tools, SaaS and on-prem apps, and for custom auth logic. It is a poor fit for minimal setup or very large scale, where he suggests paid providers. ([4:35](https://youtu.be/LVuspKy4P2w?t=275))

## Techniques
- **Stand up Authentik with Docker Compose** — On a fresh server, run docker compose up for the Authentik stack. The video does not show the compose file, its name or the image tag, so check the Authentik docs for those details. *When:* Trying a self-hosted identity provider on one box, such as a homelab or internal tools host.
- **Register an app with OAuth2/OIDC in the admin UI** — In the admin UI, create an application and attach an OAuth provider. In the consuming app, set the redirect URL (localhost for testing), then paste the client ID and client secret from Authentik. Create a test user in the UI and log in as that user. *When:* Adding central login to an existing self-hosted app without building a custom login page or password store.
- **Model login logic as flow stages plus Python policies** — Compose login behavior from the visual flow builder (stages), then add Python policy code where configuration options run out. The speaker does not show a policy example. *When:* Login rules need to go beyond standard SSO and MFA settings, such as custom access checks.
- **Weigh Authentik against other self-hosted IdPs by RAM, ops load and scale** — The speaker's comparison: Keycloak is heavy and enterprise-oriented, Authelia is light but limited for growth, and Authentik is mid-weight at roughly 2 GB RAM. Add high availability to avoid a single point of failure. *When:* Choosing an identity provider for a self-hosted stack and deciding whether to run it in HA.

## Numbers
- Adding an OAuth provider to an app in the admin UI takes under 30 seconds (speaker's claim) ([0:53](https://youtu.be/LVuspKy4P2w?t=53))
- The full demo, from Docker Compose up to a working login on a dummy app, took about 90 seconds ([2:11](https://youtu.be/LVuspKy4P2w?t=131))
- Authentik needs around 2 GB of RAM (speaker's estimate) ([3:37](https://youtu.be/LVuspKy4P2w?t=217))

## Hot takes
- The intro promises SSO, MFA and passkeys, but the demo only shows OAuth login with a test user. No MFA or passkey setup is shown.
- Calls Okta and Auth0 costly at scale and Authentik's paid tier a fair trade-off, but gives no pricing figures.
- Frames Authentik as the balanced middle option without comparing it hands-on to Keycloak or Authelia; the comparison is unsourced opinion.

## Tools mentioned
Authentik, Docker Compose, Kubernetes, OAuth2/OIDC, Keycloak, Authelia, Okta, Auth0

## Relevance to our work
- **agentos** (1/3): AgentOS's proxy layer (L1 Govrix Scout) and any admin or dashboard UIs may need a central login. Authentik is a self-hosted candidate, but this is a generic SSO tool, not an agent-specific auth model. → *Compare Authentik against the current auth plan for AgentOS's admin and observability UIs before building custom login; keep per-agent API keys separate from human SSO.*
- **general** (1/3): Useful as a reference point for self-hosted SSO and MFA in homelab or internal tools, but a light intro with no security depth. → *Read the Authentik docs on OIDC provider setup and flow stages before adopting it for any internal service.*

# The Last Authentication Library You'll Ever Need...

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `hFtufpaMcLM` · [watch](https://youtu.be/hFtufpaMcLM) · **date:** 2025-11-02 · **length:** 11:43 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Unnamed Better Stack presenter · **orgs:** Better Stack, Stripe, Polar, GitHub
- **topics:** security-guardrails, dev-tools · **tags:** authentication, betterauth, typescript, nextjs, drizzle, postgres, oauth, server-actions, api-keys, session-management

> Better Stack walkthrough of BetterAuth, an open-source TypeScript auth framework: an overview of its frameworks, databases, auth methods and plugins, then a live Next.js + Drizzle + Postgres setup for email/password and GitHub login.

## Summary
Better Stack presents BetterAuth, an open-source TypeScript authentication framework, and claims it is the most comprehensive option for TypeScript. The presenter says it works across frameworks (Astro, Remix, Next, TanStack Start, Hono, Express, Expo) and databases (MySQL, SQLite, Postgres, MS SQL, and others through Kysely dialects). Built-in methods include email/password, many social providers, a generic OAuth plugin for any OAuth2 or OpenID Connect provider, and SSO/OIDC for enterprise. Plugins cover 2FA, phone number, magic link, email OTP, passkeys, one-tap, admin user management, API keys, organizations, JWT and multi-session, plus Stripe and Polar integrations. The core of the video is a live build of a Next.js app with Drizzle and Postgres: install the package, generate the auth schema with the CLI command from the install guide, create the auth instance, and mount one catch-all route handler. Email sign-up and login run as server actions wrapped in a Zod validator, with the nextCookies plugin so cookies are set. The dashboard checks the session on the server and redirects to login when there is none, while sign-out and GitHub sign-in run from a client component. The presenter says copying the docs took about three minutes and needed two manual changes, and the video does not compare BetterAuth against alternatives.

## Key ideas
- **Framework and database breadth is the main pitch** — BetterAuth runs in Astro, Remix, Next, TanStack Start, Hono, Express and Expo, and reaches many SQL databases through Kysely dialects. The presenter's point is that it works in almost any TypeScript stack. ([0:00](https://youtu.be/hFtufpaMcLM?t=0))
- **Built-in auth surface is wide, with a generic OAuth escape hatch** — Email/password, many social providers, and a generic OAuth2/OIDC plugin for providers not on the list. SSO and OIDC are included for enterprise use. ([1:23](https://youtu.be/hFtufpaMcLM?t=83))
- **Plugins extend it to authorization and billing** — Admin (create, ban users), API keys (create, hand out, verify), organizations, and third-party Stripe and Polar integrations that create customers at signup and handle subscription lifecycle events. ([1:23](https://youtu.be/hFtufpaMcLM?t=83))
- **Schema generation from the CLI removes hand-written auth tables** — The install guide's schema command detects the ORM and generates user, session, account and verification tables. The presenter had to move the generated file into their Drizzle schema folder and pass the schema to the Drizzle adapter explicitly, which may not be needed in other setups. ([4:49](https://youtu.be/hFtufpaMcLM?t=289))
- **One catch-all route handler serves all auth endpoints** — A single route.ts with GET and POST handlers hands requests to BetterAuth's Next.js handler, so the endpoints (sign-in, sign-up, callbacks) come from the library instead of being written per route. Server code calls auth.api, and client code calls a separate auth client. ([5:50](https://youtu.be/hFtufpaMcLM?t=350))
- **Server actions need the nextCookies plugin** — Without the plugin, cookies set during a server action do not reach the browser. The presenter adds it to the config and says it works automatically after that. ([5:50](https://youtu.be/hFtufpaMcLM?t=350))
- **Route protection is a server-side session check** — The dashboard server component fetches the session with the Next.js request headers, redirects to /login if none exists, and passes the user to the sidebar. ([9:36](https://youtu.be/hFtufpaMcLM?t=576))
- **Social login is one client call plus a callback URL** — The button calls the auth client's social sign-in with the provider name. The first attempt landed on localhost:3000 until the callback URL was set to /dashboard. ([10:40](https://youtu.be/hFtufpaMcLM?t=640))

## Techniques
- **Minimal BetterAuth config for email/password plus GitHub** — Install the package and set environment variables. Create the auth instance with a Drizzle adapter (passing the generated schema tables), emailAndPassword enabled: true, and socialProviders.github with clientId and clientSecret read from environment variables. Export the auth object for server use and a separate auth client for client components. *When:* Starting a new TypeScript web app that needs password login and one OAuth provider, with Drizzle as the ORM.
- **Generate the auth schema with the CLI, then push with Drizzle** — Run the schema generation command from step 5 of the install guide. Accept the file path prompt and save it in the Drizzle schema folder. Push the generated tables with Drizzle. Tables created: user, session, account, verification. *When:* Adding BetterAuth to an existing Drizzle project so its tables match the ORM setup without writing them by hand.
- **Mount a single catch-all auth route** — Create one route.ts with a catch-all segment. Export GET and POST handlers from BetterAuth's Next.js handler, passing the auth config. *When:* Wiring BetterAuth into a Next.js App Router app so its built-in endpoints work without writing sign-in or sign-up routes.
- **Enable the nextCookies plugin for server actions** — Add the nextCookies plugin to the BetterAuth config so cookies set during server actions reach the browser. *When:* Any Next.js app that calls BetterAuth from server actions (form submits) rather than client fetch calls.
- **Email sign-up and login from a server action** — Wrap the action in a Zod-validating helper that returns either validated data or an error. Inside, call the BetterAuth server API with the sign-up call (body: email, password, name) or the sign-in call (body: email, password), then redirect to /dashboard. Forms use a server-action state hook tied to the action. *When:* Building credential forms in Next.js where validation happens before the auth call.
- **Protect a server-component page by session** — In the server component, fetch the session with auth.api's get-session call, passing the Next.js request headers. If there is no session, redirect to /login. Otherwise read the user fields (id, name, email) and pass them to the UI. *When:* Gating dashboard or account pages in Next.js App Router with BetterAuth.
- **Sign out and social sign-in from a client component** — Sign out by calling the auth client's sign-out with fetch options; on success redirect to /login. Start GitHub login with the auth client's social sign-in, passing provider: github and callbackURL: /dashboard. *When:* Adding logout and OAuth buttons to client-rendered UI.

## Numbers
- Setting up BetterAuth by copying the install guide took about 3 minutes. ([3:40](https://youtu.be/hFtufpaMcLM?t=220))
- The schema generated by the CLI has four tables: user, session, account, verification. ([4:49](https://youtu.be/hFtufpaMcLM?t=289))
- Presenter says covering all features in depth would take about 12 hours (rhetorical; no benchmark). ([0:00](https://youtu.be/hFtufpaMcLM?t=0))
- No latency, cost, adoption or benchmark figures are given. ([0:00](https://youtu.be/hFtufpaMcLM?t=0))

## Hot takes
- Presenter calls it the best auth library they have come across, based on one copy-the-docs setup and no comparison with alternatives such as Auth.js or Clerk.
- The docs-copy demo hid two manual fixes (moving the schema file, passing the schema to the adapter). Those suggest that the docs may not match real project layouts.
- The 12-hour claim is rhetorical. The video covers only email/password and GitHub login in working code; the plugins are listed, not demonstrated.
- No sponsorship is stated (the presenter says they have no affiliation), so the quality cap for sponsored content does not apply.

## Tools mentioned
BetterAuth, Next.js, Drizzle ORM, Postgres, Docker, shadcn/ui, Zod, GitHub OAuth, Kysely, Hono, Express, Expo, Astro, Remix, TanStack Start, React Native, Stripe plugin, Polar plugin, nextCookies plugin

## Relevance to our work
- **agentos** (1/3):  → *Read BetterAuth's API-key plugin docs and compare its create, hand-out and verify flow against how AgentOS's gateway issues and checks keys, in case it is reusable for a future admin UI.*

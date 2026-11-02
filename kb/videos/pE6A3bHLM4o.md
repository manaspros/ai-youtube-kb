# 1 in 9 Apps Ship Supabase Keys: Here’s How It Happens

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `pE6A3bHLM4o` · [watch](https://youtu.be/pE6A3bHLM4o) · **date:** 2026-02-02 · **length:** 4:16 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Supabase
- **topics:** security-guardrails, dev-tools · **tags:** supabase, secrets, env-vars, next.js, vite, sveltekit, row-level-security, secret-scanning, client-bundle, key-rotation

> Public-prefixed env vars (NEXT_PUBLIC_, VITE_, PUBLIC_) ship into the client bundle, so a private Supabase key behind one leaks to every visitor; the fix is server-side calls, bundle checks and CI guardrails.

## Summary
A short Better Stack explainer on how private Supabase keys end up in front-end JavaScript. It cites a report that scanned about 20,000 indie apps and found one in nine exposing Supabase credentials in client code. The speaker explains that build tools inline any variable with a public prefix (Next.js, Vite, SvelteKit) into the client bundle, and that anon/publishable keys are meant to be public while service-role/secret keys bypass row-level security. A demo builds a small Next.js CRUD app with a private key behind NEXT_PUBLIC_, then finds it by searching the compiled bundle. The fix is to have the browser call its own server-side API, which holds the private key, then rebuild and confirm the key is gone. Guardrails proposed are CI secret scanning, a PR rule treating public-prefixed variables as public, and key rotation on any suspicion of exposure.

## Key ideas
- **A public-prefixed env var is a shipping label, not a safety label** — NEXT_PUBLIC_ (Next.js), VITE_ (Vite) and PUBLIC_ (SvelteKit) tell the build tool to inline the value into the client JavaScript bundle, so any visitor can download it. ([0:00](https://youtu.be/pE6A3bHLM4o?t=0))
- **Supabase keys split into public and private classes** — The anon/publishable key is designed to be visible. The service-role/secret key bypasses row-level security, so if it reaches the browser, RLS policies stop mattering. ([0:00](https://youtu.be/pE6A3bHLM4o?t=0))
- **The leak is an accident, not a hack** — The speaker's point is that the affected apps were not breached; the credentials were simply in the public JS that the app serves, readable by anyone who opens DevTools. ([0:00](https://youtu.be/pE6A3bHLM4o?t=0))
- **Reproduction: one private key behind a public prefix is enough** — Demo: a Next.js CRUD app linked to Supabase, a private key placed behind NEXT_PUBLIC_, a production build, then a search of the compiled bundle that finds both the URL and the key. ([1:29](https://youtu.be/pE6A3bHLM4o?t=89))
- **Fix by moving privileged calls to the server** — The browser calls the app's own API route or server function; that server-side code holds the private key and calls Supabase. Rebuild and search the bundle again to confirm the key is gone. ([2:30](https://youtu.be/pE6A3bHLM4o?t=150))
- **Fixing the key is not the whole job** — Also enable RLS on user-facing tables, verify the policies do what you think, and test them, since the speaker says this step is often skipped. ([2:30](https://youtu.be/pE6A3bHLM4o?t=150))
- **Guardrails stop the regression during a rushed release** — Add secret scanning in CI so builds fail when a key appears where it should not, add a PR rule that treats public-prefixed variables as public by default, and rotate keys on any hint of exposure rather than waiting. ([3:54](https://youtu.be/pE6A3bHLM4o?t=234))

## Techniques
- **Audit the shipped build for secrets** — Build the app the way you ship it (the speaker runs npm run build), then search the output for Supabase, JWT, service, secret, and anything token-shaped. The video shows searching the compiled JS in Chrome DevTools; it does not name a build output directory. Treat any private-looking hit as compromised: rotate it and move the logic server-side. *When:* Before each release, and after adding or renaming any env var that uses a public prefix.
- **Proxy privileged calls through your own server** — Keep the service-role or secret key out of client code. The browser calls an app-owned API route or server function; that server code holds the private key and calls Supabase. Rebuild and confirm the key is absent from the bundle. *When:* Any operation that needs a private Supabase key (admin writes, RLS-bypassing reads) from a browser-facing app.
- **Enable and test RLS on user-facing tables** — Turn on row-level security for every user-facing table and check that each policy does what it is meant to do by testing it, not just reading it. *When:* Alongside any Supabase key change, since RLS is the backstop for the public anon key.
- **Review rule for public-prefixed variables** — In PR review, treat anything named NEXT_PUBLIC_, VITE_ or PUBLIC_ as public by default and question any secret placed behind those prefixes. *When:* Any PR that adds or changes environment variables in a front-end project.
- **CI secret scanning as a build gate** — Run a secret scanner in the pipeline so the build fails when a key appears in a place it should not. The video names no specific scanner. *When:* Every build pipeline that ships a browser bundle.
- **Rotate on suspicion** — If there is even a slight hint that a key was exposed, rotate it instead of waiting to see whether it is abused. *When:* Any private key found in a bundle, log, or repo.

## Numbers
- Report scanned about 20,000 indie apps; one in nine exposed Supabase credentials in front-end code ([0:00](https://youtu.be/pE6A3bHLM4o?t=0))
- Demo video length is about 4 minutes 16 seconds (the whole video) ([0:00](https://youtu.be/pE6A3bHLM4o?t=0))

## Hot takes
- The one-in-nine figure is attributed only to an unnamed report from 'this month'; the video gives no methodology, and the speaker never names the source.
- The core message is simple and correct: if a key is in the bundle, it is public. The video is thin on specifics beyond that (no CI tool named, no RLS policy examples).

## Tools mentioned
Supabase, Next.js, Vite, SvelteKit, Chrome DevTools, npm

## Relevance to our work
- **general** (2/3): Common failure mode for any team shipping a browser app with a backend service key, and cheap to guard against. → *Add a secret-scanning step to CI and a grep of the production build output for private-key patterns before release.*
- **agentos** (1/3): AgentOS has a security-guardrails pillar (L1 PII/prompt-injection scan, L2C exec-gate). This video is about secret placement in client bundles, which is adjacent but not core. → *If AgentOS ever ships a browser-side UI, add a CI step that fails the build when provider or service keys appear in the built JS.*
- **prosharness** (1/3): ProsHarness emphasises zero-token credential handling. The video's rule that private keys stay server-side fits that principle. → *Apply the bundle-grep check to any browser-facing ProsHarness UI so credentials are not inlined into client assets.*

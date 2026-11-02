# HUGE Next.js Authorization Bypass... Are You Safe? (9.1 CVSS)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `D_Tt39FEIiU` · [watch](https://youtu.be/D_Tt39FEIiU) · **date:** 2025-11-02 · **length:** 6:24 · **format:** news · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Better Stack host (not named in transcript) · **orgs:** Vercel, Netlify, Cloudflare, Replit
- **topics:** security-guardrails, dev-tools · **tags:** nextjs, cve, authorization-bypass, middleware, waf, self-hosting, web-security

> Walkthrough of the Next.js 15.2.2 middleware authorization bypass (CVSS 9.1): a client-sent internal subrequest header skips middleware, what it exposes, how it was patched, and edge mitigations.

## Summary
The host demonstrates a critical (CVSS 9.1) authorization bypass in Next.js middleware. Apps that gate routes only in middleware can be bypassed by sending the internal x-middleware-subrequest header with the middleware name repeated five times. The root cause is a recursion guard that counts matching entries in that header, so five entries hit the max-depth check and the request returns early, skipping middleware. Impact is limited in the demo: API routes that check auth themselves still reject the request, but pages that rely on middleware alone for UI gating and unprotected API routes are exposed. The fix landed in 15.2.3 (with backports to 14, and reportedly 13 and 12), and the patch strips the header unless it carries a server-generated random ID. Mitigations for teams that cannot upgrade are blocking the header at the edge or a WAF; the host says Vercel and Netlify already block it and Cloudflare offers a managed rule. The second half covers the public drama over Vercel's CVE messaging and CEO spats, which the host largely frames as noise compared with the basic lesson to check auth in every API route.

## Key ideas
- **The vulnerability is a CVSS 9.1 authorization bypass in Next.js middleware, which the host calls possibly the largest in Next.js history.** — Anyone whose only route protection is a middleware auth check may be exposed. The host's view is that the real-world impact is narrower than the rating suggests. ([0:00](https://youtu.be/D_Tt39FEIiU?t=0))
- **Sending the internal x-middleware-subrequest header with the middleware name repeated five times, colon-separated, skips the middleware entirely.** — The demo app redirected unauthenticated users to login. With the header set, the protected route loaded directly. ([1:07](https://youtu.be/D_Tt39FEIiU?t=67))
- **Impact is bounded by how the app does auth. API routes that re-check auth still fail because the bypassed request carries no auth details, but layout and any unprotected API data are visible.** — The host says a simple paywall that only gates the UI is affected, and that an API with no auth check is bad practice regardless. ([2:28](https://youtu.be/D_Tt39FEIiU?t=148))
- **Root cause: a recursion guard in the middleware runner (sandbox code) counts matching entries in the subrequest header, and five entries reach the max-depth limit, so the code returns early.** — The header was meant to stop middleware from recursing into itself on nested fetches. The reduce over the split header array is where the bypass happens. ([3:51](https://youtu.be/D_Tt39FEIiU?t=231))
- **The fix is in 15.2.3, with backports to 14 and reportedly 13 and 12. The patch generates a random server-only ID and strips the subrequest header when the ID is missing.** — Hosts already blocking the header include Vercel and Netlify. Cloudflare offers a managed firewall rule, or you can write your own edge rule. ([5:14](https://youtu.be/D_Tt39FEIiU?t=314))
- **Public response was contentious: Vercel's advisory included a line about Vercel customers being protected, which critics called marketing. The host reports the vendor CEOs' back-and-forth without taking a side.** — The host's takeaway is that an auth check in each API route would have contained the bug. ([5:14](https://youtu.be/D_Tt39FEIiU?t=314))

## Techniques
- **Re-check auth in every data-bearing route** — Do not rely on middleware alone. Each API route or server handler that returns protected data verifies the session or token itself, so a skipped middleware cannot expose data. *When:* Any Next.js app that uses middleware for authentication, especially one with API routes or paywalls.
- **Strip the internal subrequest header at the edge until patched** — Block or drop the x-middleware-subrequest header from external requests at the WAF, load balancer or reverse proxy, as the host describes Cloudflare's managed rule doing, or write a custom rule. *When:* Self-hosted Next.js that cannot upgrade to the patched release immediately.
- **Check the vulnerable and patched source at the release tags** — Open the Next.js repo at the vulnerable version (15.2.2 in the video) and the patched version (15.2.3), then inspect the sandbox run function and the linked fix PR to see exactly what changed. *When:* Assessing a CVE's real impact on your app, rather than relying on the headline severity.

## Numbers
- CVSS severity score 9.1 out of 10 (critical). ([0:00](https://youtu.be/D_Tt39FEIiU?t=0))
- Vulnerable version shown as 15.2.2; patched in 15.2.3. ([2:28](https://youtu.be/D_Tt39FEIiU?t=148))
- The bypass header value repeats the middleware name five times, so the recursion depth counts to five and hits the max-depth limit. ([1:07](https://youtu.be/D_Tt39FEIiU?t=67))
- Fix in 15.2.3, with patches for 14 and, per the host, backports to 13 and 12. ([3:51](https://youtu.be/D_Tt39FEIiU?t=231))

## Hot takes
- The host calls the bug a bit silly and says the severity is inflated, since the bypass exposes mostly page layout and unprotected API routes, which were already bad practice.
- Vercel's advisory line about its customers being protected was criticized as marketing. The host relays this criticism and the Replit and Cloudflare CEO spats but does not endorse either side.
- Anyone with an API route that returns data without its own auth check was already exposed. Middleware-only auth is not a sufficient control.

## Tools mentioned
Next.js 15.2.2 (vulnerable), Next.js 15.2.3 (patched), Next.js 14 (patched line), Vercel, Netlify, Cloudflare (managed firewall rule), Replit (named in the public discussion), GitHub (source and PR review), Chrome (password warning)

## Relevance to our work
- **agentos** (1/3): The Govrix Scout proxy makes budget and PII policy decisions. Any client-controllable header that changes whether those checks run would be a bypass of the same shape. → *Check whether any Scout header can skip budget, PII or prompt-injection scanning, and add a test that sends it from an untrusted client.*

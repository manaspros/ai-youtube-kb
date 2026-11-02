# Yeah it’s over for NextJS... 13 NEW vulnerabilities

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `mYdx6hZG9qo` · [watch](https://youtu.be/mYdx6hZG9qo) · **date:** 2026-06-02 · **length:** 16:03 · **format:** news · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Vercel (Next.js), Meta (React), TanStack, Astro, Cloudflare, Vinext
- **topics:** security-guardrails, dev-tools · **tags:** nextjs, react-server-components, cve, security, middleware, ssrf, cache-poisoning, xss, denial-of-service, self-hosting

> Better Stack walks through five of the 13 React and Next.js CVEs in one security release (middleware bypass, RSC denial of service, SSRF, cache poisoning, script XSS) and argues for moving off Next.js.

## Summary
The presenter covers a Next.js and React security release that fixed 13 CVEs, six of them rated high severity. He reproduces five of them on a sample app: a Pages Router i18n middleware bypass that exposed server-side props through the data route, a denial-of-service in React Server Components deserialization, a server-side request forgery in the self-hosted proxy path, a cache poisoning issue where RSC payloads were cached as HTML, and an XSS in before-interactive script props. For each, he explains the root cause and the upstream fix, which is mostly a guard or a change in algorithm. He stresses that middleware alone is not real auth and that a hand-rolled serialization protocol is hard to get right. The video ends with his opinion that Next.js has had too many hurdles, and that he has moved to TanStack Start, Astro for content sites, and Cloudflare. He says he could not reproduce every CVE, and that he is biased toward TanStack.

## Key ideas
- **A single Next.js and React security release fixed 13 CVEs, six rated high severity. The only remediation is to upgrade to the patched Next.js versions.** — Covers DoS, middleware bypass, XSS and more. The presenter says TanStack Start is not affected, which he admits is a bias he holds. ([0:00](https://youtu.be/mYdx6hZG9qo?t=0))
- **Middleware bypass in the Pages Router with i18n: the matcher covered the English and French locale variants of a protected page but not the base path, so the base path was unprotected.** — Rated 7.5. The presenter argues middleware bypasses sound worse than they are, since Next.js does not recommend relying on middleware alone for protection. ([0:39](https://youtu.be/mYdx6hZG9qo?t=39))
- **Server-side props for protected pages were reachable through the data JSON route, which the middleware did not cover for the base locale.** — The build ID needed to build that route is visible in the page's embedded data. The fix is to enforce auth in the data-fetching code, not only in middleware. ([2:36](https://youtu.be/mYdx6hZG9qo?t=156))
- **Denial of service in the React Server Components (Flight) deserializer: for each reference it rescanned every key in the payload, which is O(k times n).** — The presenter's crafted payload (about 200k keys and 1000 references) causes roughly 200 million string comparisons. A single request raised response time from 0.02 s to about 6 s. The fix uses a forward-only cursor over the key list, bringing the work to about n plus k (around 201k operations). ([3:36](https://youtu.be/mYdx6hZG9qo?t=216))
- **Server-side request forgery in self-hosted Next.js (rated 8.6, the highest in the set): a crafted websocket-upgrade request got the framework to proxy to an arbitrary internal address.** — The root cause is that resolveRoutes returned the attacker-supplied request target as the proxy destination. The fix adds a finished flag and a status-code guard so only valid rewrite or proxy routes are forwarded. The presenter says the issue affects self-hosted and third-party deployments, though the transcript is unclear on the exact exclusion. ([8:22](https://youtu.be/mYdx6hZG9qo?t=502))
- **Cache poisoning (rated 5.4): the RSC detection check looked only for a .rsc suffix, so an RSC request with a query string was cached as HTML and later served to normal users.** — Fix: ignore the query string when deciding whether a response is RSC payload. ([10:38](https://youtu.be/mYdx6hZG9qo?t=638))
- **XSS (rated 6.1) in next/script with strategy beforeInteractive when a prop takes untrusted input: the framework serializes props with JSON.stringify inside a script tag, which does not escape the closing script delimiter.** — Untrusted query parameter data can close the script element and run arbitrary script. The presenter notes that this is a realistic route to session cookie theft. ([13:09](https://youtu.be/mYdx6hZG9qo?t=789))
- **Presenter's conclusion: hand-rolled wire protocols and serialization are hard to get right, and Next.js has had repeated hurdles, so he has moved to TanStack Start, Astro for content sites, and Cloudflare.** — This is opinion, not an argument supported by data. He also questions whether server components have been useful. ([15:28](https://youtu.be/mYdx6hZG9qo?t=928))

## Techniques
- **Enforce auth in the data loader, not only in middleware** — Check the session inside getServerSideProps or the equivalent data function for any page that returns sensitive props. Treat middleware as a convenience layer. The presenter cites Next.js guidance that middleware should not be the only protection. *When:* Any page with sensitive server-rendered data, especially when i18n or multiple locales are enabled.
- **Regression-test matcher and data-route coverage** — After changing middleware matchers or enabling i18n, confirm that every locale variant and the base path, including the data routes under /_next/data/<buildId>/, return a redirect or 401 for unauthenticated requests. *When:* Whenever middleware matchers, i18n config, or routing changes.
- **Load-test server action endpoints with large or repetitive payloads** — Send payloads with many keys and repeated references to server action endpoints, and track p95 latency and event-loop blocking. A regression shows up as a sharp latency jump from a single request. *When:* Before exposing RSC or server action endpoints to untrusted traffic, and as a gate on framework upgrades.
- **Make CDN cache keys match the content-type routing logic** — Decide whether a response is RSC payload or HTML using the same normalized URL the cache uses, with query strings stripped. Vary on the RSC header where the framework supports it, and test by warming the cache with an RSC-style request, then requesting HTML. *When:* Any CDN or cache in front of a framework that serves both HTML and RSC payloads from the same path.
- **Keep untrusted input out of inline script props** — Do not pass request-derived values into next/script props, especially with beforeInteractive. Pass values through data attributes or fetch them client-side, and escape <, >, and / when serializing into a script tag. *When:* Any inline script or head script that receives user-controlled data.
- **Limit what the app server can reach internally** — Assume a request-forgery bug can make the web server reach internal services. Use egress rules, separate network policy for databases and Redis, and authenticate internal services, not just network-level firewalling. *When:* Self-hosted Next.js or any web tier that sits next to internal services.
- **Patch to the fixed Next.js release** — Upgrade to the patched version listed in the vendor security advisory. The presenter says this is the only resolution for the 13 CVEs. *When:* Immediately, for any app on an affected Next.js or React Server DOM version.

## Numbers
- 13 CVEs in the release, six rated high severity ([0:00](https://youtu.be/mYdx6hZG9qo?t=0))
- Middleware and proxy bypass CVE rated 7.5 out of 10 ([0:39](https://youtu.be/mYdx6hZG9qo?t=39))
- Denial-of-service CVE rated 7.5. Normal response 0.02 s, about 6 s after one exploit request ([3:36](https://youtu.be/mYdx6hZG9qo?t=216))
- Deserializer example: 6 keys became 12 keys passed over in a small case ([4:42](https://youtu.be/mYdx6hZG9qo?t=282))
- Stress example: 199,999 random keys plus 1000 references caused about 200 million string comparisons (before the fix) ([5:55](https://youtu.be/mYdx6hZG9qo?t=355))
- After the cursor fix, the same example needs about 201,000 operations (n plus k) ([7:00](https://youtu.be/mYdx6hZG9qo?t=420))
- Server-side request forgery rated 8.6 out of 10, the highest in the release ([8:22](https://youtu.be/mYdx6hZG9qo?t=502))
- Cache poisoning rated 5.4 out of 10 ([10:38](https://youtu.be/mYdx6hZG9qo?t=638))
- Cross-site scripting rated 6.1 out of 10 ([11:55](https://youtu.be/mYdx6hZG9qo?t=715))

## Hot takes
- The title ("it's over for NextJS") is hype. The evidence is five reproductions out of 13 CVEs, and the framing that Next.js is in decline is the presenter's opinion.
- The presenter says middleware bypasses are less serious than they sound, since middleware should not be the only protection. This is a useful correction to a common pattern.
- He admits he is biased toward TanStack, and his claim that TanStack Start is unaffected is not backed by a demonstration in the video.
- He suggests running Claude Mythos over the React and Next.js codebase, without evidence it would find more issues.
- His claim that hand-rolled serialization protocols are inherently hard to get right is a plausible argument but not measured here.

## Tools mentioned
Next.js (Pages Router, i18n, middleware/proxy, getServerSideProps, next/script beforeInteractive), React Server Components and the React Flight serialization protocol (react-server-dom), TanStack Start, Astro, Vinext, Cloudflare, Python http.server (used as the internal target in the SSRF demo), curl, Browser devtools (Network tab, inspect element), Claude Mythos (suggested by the presenter for auditing the React and Next.js codebase)

## Relevance to our work
- **agentos** (1/3): The Next.js-specific CVEs don't apply to AgentOS, but the classes (a proxy trusting the request target, a cache key that ignores query strings, auth enforced in only one layer) do apply to the Rust proxy in Govrix Scout. → *Add regression tests to the Govrix Scout proxy that an absolute-URL request target or an upgrade header cannot cause an upstream proxy to a non-configured host, and that the cache key normalizes the query string the same way the routing decision does.*

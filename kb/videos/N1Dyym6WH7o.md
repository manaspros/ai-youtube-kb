# It Happened Again... 2 New React CVE's

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `N1Dyym6WH7o` · [watch](https://youtu.be/N1Dyym6WH7o) · **date:** 2026-01-02 · **length:** 5:27 · **format:** news · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, React, Vercel
- **topics:** security-guardrails, dev-tools · **tags:** react, next.js, react-server-components, server-actions, cve, denial-of-service, deserialization, source-code-leak, dependency-patching, secrets-management

> Better Stack walks through two new React and Next.js vulnerabilities disclosed after the React Server Components RCE the week before: a high-severity denial of service and a medium-severity leak of server action source code, both triggered by a single crafted POST, with the earlier patch not covering them.

## Summary
The video covers two follow-up vulnerabilities in React Server Components and Next.js, found after the remote code execution disclosed the previous week. The first is a denial of service (CVSS 7.5, high) that the presenter reproduces on a Next.js app with no custom code and no server actions, showing the server stop serving pages after one request. The root cause is in how the React Flight Protocol resolves chunked payloads: references between chunks can form a cycle, so deserialization never finishes. The first patch was incomplete, so a second CVE and a second patch followed, which adds a hard cap on resolution cycles. The second issue (CVSS 5.3, medium) requires an app that uses a server action; a crafted payload gets a server function reference resolved into an argument, and the function's source is then returned because function-to-string conversion exposes code, including any secrets hard-coded in it. The fix overrides toString for server references so it returns a placeholder. The presenter's advice is to upgrade React and Next.js right away, keep secrets in environment variables, and note that the React team expects follow-on bugs near a major disclosure as researchers probe adjacent code for bypasses. The content is a short advisory-style walkthrough with one live demo per bug and no sponsorship; it names the mechanism but does not publish the exact payloads, and it gives no CVE identifiers in the transcript.

## Key ideas
- **Two new React/Next.js vulnerabilities follow the React Server Components RCE from the prior week. Both are triggered by a simple POST, and the earlier patch does not fix them, so upgrading React and Next.js is the immediate action.** — The presenter says the earlier patch does not cover either bug and tells viewers to upgrade Next.js or React now. ([0:00](https://youtu.be/N1Dyym6WH7o?t=0))
- **The denial-of-service bug (CVSS 7.5, high) hangs the server on one request, even for an app with no custom code and no server actions.** — In the demo, the request connection time climbs to about 20 seconds, and afterward the site returns nothing to normal GET requests. The demo app is on Next.js 16 (transcript says '16.08'). ([0:00](https://youtu.be/N1Dyym6WH7o?t=0))
- **Root cause of the DoS is cyclic reference resolution in the React Flight Protocol. Chunk references can point back to each other, so deserialization loops forever.** — Flight payloads use chunk references (the dollar-sign notation) that resolve to a final object. A reference cycle between two chunks keeps the request stuck and blocks further processing. ([1:01](https://youtu.be/N1Dyym6WH7o?t=61))
- **The first patch was incomplete, which led to a second CVE and second patch. The second patch adds a hard cap on resolution cycles.** — The first patch tracks references already visited and returns them by ID rather than re-exploring. The second patch adds a hard-coded cycle limit of 1000, after which resolution errors out. The presenter calls the first patch more complicated. ([1:01](https://youtu.be/N1Dyym6WH7o?t=61))
- **The source-code leak (CVSS 5.3, medium) needs an app that uses a server action. A crafted payload makes a server function reference resolve into an argument, and the function's source text comes back.** — Function-to-string conversion returns the function's source code, and the demo shows the source leaking through a template literal. Medium severity reflects that it leaks source but needs a server action, and that secrets should not be hard-coded in source anyway. ([2:28](https://youtu.be/N1Dyym6WH7o?t=148))
- **The fix for the leak overrides toString on server references so it returns a fixed placeholder instead of the function source.** — The overridden method, named server reference toString in the presenter's words, returns a constant string in place of the code. The presenter says the leak scope is limited. ([3:27](https://youtu.be/N1Dyym6WH7o?t=207))
- **Expect more CVEs after a big disclosure. Researchers scrutinize the affected code and its neighbors while hunting for bypasses of the original fix.** — The presenter cites a React team note saying extra vulnerabilities are common after a major bug and hopes these two are the last high-severity ones. ([4:39](https://youtu.be/N1Dyym6WH7o?t=279))

## Techniques
- **Verify the patched version before trusting an earlier fix** — Check the vendor advisory for every CVE in the family, not just the first. Confirm the installed React and Next.js versions cover both the DoS and the source-leak CVEs. The second patch here was required because the first was incomplete. *When:* Any time a framework has a serious RCE or deserialization bug, because follow-up CVEs often land in adjacent code within days.
- **Test a staging deployment for hang-on-request behavior** — After upgrading, send a request to a non-production instance and check whether connection time stays bounded and normal GET requests still return the page. The presenter measures time to connect and whether the page loads after the request. *When:* To confirm a DoS-class patch is effective, as an upgrade regression check on any server-rendered React or Next.js service.
- **Keep secrets out of server action source** — Read secrets from environment variables instead of constants in server action files. The presenter's point: a source leak then exposes code but not credentials. *When:* Any server action or server-side function that touches credentials, API keys, or database connection strings.
- **Treat neighbors of a fixed bug as suspect** — After a major disclosure in a serialization or deserialization layer, review adjacent code paths in your stack for similar patterns, and watch advisories for follow-up CVEs. *When:* Right after a large framework CVE, when deciding how much to audit and when to re-check patch status.

## Numbers
- Connection time to the demo server rose to about 20 seconds after one crafted POST, then the site stopped responding. ([0:00](https://youtu.be/N1Dyym6WH7o?t=0))
- Denial-of-service CVE severity is 7.5 (high). ([0:00](https://youtu.be/N1Dyym6WH7o?t=0))
- The DoS patch sets a hard-coded cycle limit of 1000 before resolution errors out. ([1:01](https://youtu.be/N1Dyym6WH7o?t=61))
- Source-leak CVE severity is 5.3 (medium). ([3:27](https://youtu.be/N1Dyym6WH7o?t=207))
- Demo app is on Next.js '16.08' per the transcript, with no custom code changes and no server actions. ([0:00](https://youtu.be/N1Dyym6WH7o?t=0))

## Hot takes
- Hype title and 'make sure you upgrade immediately' framing, but the content is substantive: the mechanism is explained and each bug has a live demo.
- The presenter calls the DoS 'the most severe' and notes that the first patch failed, so it is worth re-checking that an upgrade actually includes the second fix.
- The presenter argues the source leak is less severe than the DoS (5.3 vs 7.5) because it needs a server action and because secrets should live in environment variables, not in code.
- A React team note warns that more CVEs tend to follow a major disclosure, so this is likely not the last one.

## Tools mentioned
React, Next.js, React Server Components, React Flight Protocol, Server Actions, GitHub Security Advisories

## Relevance to our work
- **agentos** (1/3): AgentOS is a self-hosted infra project, so framework CVEs in any web UI or dashboard it runs are a supply-chain concern, but the transcript has no agent-specific content. → *If any self-hosted AgentOS UI uses Next.js or React server components, check it against the patched versions and add a regression check that a single crafted request does not hang the server.*

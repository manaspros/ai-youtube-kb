# React’s Worst Vulnerability Ever (RCE Exploit Explained)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `iV48tEiHFDY` · [watch](https://youtu.be/iV48tEiHFDY) · **date:** 2026-01-02 · **length:** 7:31 · **format:** news · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Vercel, Cloudflare, AWS
- **topics:** security-guardrails, dev-tools · **tags:** react-server-components, rce, cve, prototype-pollution, deserialization, nextjs, patching, waf, react-flight-protocol

> Explainer on the critical unauthenticated RCE in React Server Components (React2Shell, CVSS 10) affecting React and Next.js servers. Main takeaway: upgrade now, since WAF rules are not a full fix.

## Summary
The video walks through a critical unauthenticated remote code execution flaw in React Server Components, which the speaker says affects any site running the Next.js server or the React server package, even without server actions. Two CVEs were issued: one for the React server package (CVSS 10) and one for the Next.js server, which depends on it. The speaker says hosting providers such as Vercel and Cloudflare deployed WAF rules, but people have reported bypasses, so upgrading is the real fix. AWS reportedly saw threat groups quickly trying to exploit it. The root cause is in the React Flight Protocol deserializer, which resolves references between chunks by walking paths on attacker-controlled input without checking that each key is an own property of the object. That lets a request reach inherited JavaScript internals. The official fix adds a hasOwnProperty check and throws on inherited keys. The speaker demonstrates the impact on a local Next.js build, where the server ran a shell command it should not have. He deliberately stays at the level of the mechanism and does not give a payload.

## Key ideas
- **Critical unauthenticated RCE in React Server Components, scored CVSS 10. The speaker says upgrade React and Next.js immediately.** — Affects any app running the Next.js server or the React server package. Server actions do not need to be in use to be exposed. Provider WAF rules are described as partial, with bypasses reported. ([0:00](https://youtu.be/iV48tEiHFDY?t=0))
- **Active exploitation was already happening.** — The speaker says AWS reported threat groups rapidly trying to exploit the flaw at the time of the video. ([0:00](https://youtu.be/iV48tEiHFDY?t=0))
- **Two CVEs: one for the React server package and one for the Next.js server, which depends on it.** — The bug was credited to Lachlan Davidson, who published a write-up and proofs of concept. The speaker names the issue React2Shell. ([1:08](https://youtu.be/iV48tEiHFDY?t=68))
- **Root cause is in the React Flight Protocol deserializer.** — Server components send chunks as form data with reference notation. The deserializer resolves references by walking paths taken from the incoming payload, so untrusted input decides which properties are read. ([2:14](https://youtu.be/iV48tEiHFDY?t=134))
- **The missing check is an own-property test before dereferencing each path segment.** — Without it, the path walk can reach inherited JavaScript internals such as the object prototype. A missing key that should have returned an error instead exposes the prototype chain. ([3:16](https://youtu.be/iV48tEiHFDY?t=196))
- **The official fix is a hasOwnProperty guard that throws on inherited keys.** — Keys that are not own properties of the object are rejected with an invalid reference error before any access happens. ([4:23](https://youtu.be/iV48tEiHFDY?t=263))
- **Impact is full server-side code execution, not just a crash.** — The speaker shows a demo where a POST to a local production Next.js server runs a shell command and prints the contents of a file on the host. He says the attacker can do anything the server process can do, and he omits the payload internals. ([6:47](https://youtu.be/iV48tEiHFDY?t=407))

## Techniques
- **Patch React and Next.js before anything else** — Upgrade the React server package and the Next.js server to fixed versions. Check the advisory for the exact patched version, because the captions for the vulnerable Next.js version are ambiguous (spoken as '16.06'). Do not treat provider WAF rules as a substitute for upgrading. *When:* Any app that uses React Server Components or the Next.js server, including the default create-next-app setup.
- **Guard property lookups in any deserializer or path resolver** — Before reading each path segment from an object, check that the key is an own property (for example with Object.prototype.hasOwnProperty.call) and throw otherwise. This is the fix the video describes for the Flight deserializer. *When:* Writing or reviewing code that resolves dotted or bracketed paths, reference strings or chunk references taken from request bodies, or custom serializers that accept untrusted input.
- **Audit for dynamic path traversal on untrusted input** — Search the codebase for code that splits strings on separators such as ':' or '.' and then indexes objects with the resulting keys, especially where the input comes from a request body or form data. Confirm each lookup has an own-property check or uses a Map or an allowlist of keys. *When:* Security review of a Node or Next.js service, or after a framework advisory that involves deserialization.

## Numbers
- CVSS score of 10 for the React server package CVE; a second CVE covers the Next.js server. ([0:00](https://youtu.be/iV48tEiHFDY?t=0))
- The vulnerable Next.js version is spoken as '16.06' in the captions, the latest vulnerable release when the video was made. Verify the exact version against the advisory. ([0:00](https://youtu.be/iV48tEiHFDY?t=0))
- Two CVEs in total: one for the React server package, one for the Next.js server. ([1:08](https://youtu.be/iV48tEiHFDY?t=68))

## Hot takes
- Upgrade now. WAF rules from hosting providers are not enough, per the speaker.
- The 'worst vulnerability ever' title is hype, but the mechanism explanation (missing own-property check leading to prototype access) is accurate and useful for code review.
- Mostly a news or vulnerability explainer. There is no sponsor segment, and the speaker deliberately omits the payload. Practical content is limited to patching and the fix pattern, so quality is capped around 3.

## Tools mentioned
React, React Server Components, React Flight Protocol, Next.js, Node.js, Cloudflare WAF, AWS

## Relevance to our work
- **agentos** (1/3):  → *If any AgentOS dashboard or admin UI uses Next.js or React Server Components, confirm it runs a patched version. Also grep the Node services for dynamic path lookups on request bodies.*

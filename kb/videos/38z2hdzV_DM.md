# Is This WordPress's Worst Hack In History?

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `38z2hdzV_DM` · [watch](https://youtu.be/38z2hdzV_DM) · **date:** 2026-08-02 · **length:** 5:04 · **format:** news · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** WordPress
- **topics:** security-guardrails, dev-tools · **tags:** wordpress, sql-injection, rest-api, batch-endpoint, validation-desync, privilege-escalation, web-shell, vulnerability, ai-assisted-exploitation

> Better Stack walks through a WordPress REST API batch-endpoint bug (6.9.x and 7.0.x) that chains a validation desync into unauthenticated SQL injection, admin account creation and a malicious plugin upload.

## Summary
The host demos a public proof-of-concept against a stock local WordPress install, where a check script returns HTTP 207 to confirm the site is vulnerable. The chain starts at the unauthenticated batch/v1 endpoint, which takes nested requests that are supposed to be validated and permission-checked individually. A bug left two parallel arrays (validation and matches) out of sync when one sub-request had an invalid path, so the same index read mismatched results. The PoC uses that desync to smuggle GET requests past a method allow-list, reaching a function that interpolates an author parameter into SQL without escaping. The first five steps are pre-auth; the sixth, uploading a plugin, is ordinary behaviour for an admin. The host shows a SQL read, creates an admin, uploads a web-shell plugin, deletes the admin, and logs in with a persistent backdoor account. The affected versions are stated as 6.9.0 to 6.9.4 and 7.0.0 to 7.0.1 (captions read "6.90 to 6.94" and "7.00 to 7.01"), fixed in 7.0.2. The host argues that AI made the chain findable in about 10 hours and that automated scanners will soon exploit such bugs within days.

## Key ideas
- **A batch endpoint is only as safe as its per-request checks. Here the outer batch request was validated as a POST, and its nested requests were dispatched without that same method check.** — The outer batch/v1 request was validated, but nested requests inside a v2 posts request body bypassed the method allow-list, which let GET requests through. ([1:30](https://youtu.be/38z2hdzV_DM?t=90))
- **Parallel arrays that must stay in sync are a fragile design. A validation update on one branch but not the other let a single index read mismatched results.** — The batch handler kept validation and matches arrays in parallel. When a sub-request had an invalid path, only validation was updated, so the same index pointed at different requests in each array. ([0:00](https://youtu.be/38z2hdzV_DM?t=0))
- **Internal dispatch that skips escaping turns a routing mismatch into SQL injection. The author-exclude parameter ended up in a SQL string as raw text.** — The desync caused a GET to a non-existent post to be dispatched to a get-items handler, where an author-exclude field was mapped to an author-not-in clause and interpolated into SQL unescaped. ([1:30](https://youtu.be/38z2hdzV_DM?t=90))
- **Individually harmless steps chain into full takeover. Only the first five steps are unauthenticated, and step six (plugin upload) is normal admin behaviour.** — The chain creates an admin through the v2 users endpoint, then uploads a plugin as that admin. The host notes the stock install is what is vulnerable, with no malicious plugin needed to start. ([1:30](https://youtu.be/38z2hdzV_DM?t=90))
- **The host frames the speed of exploitation as the real risk. He argues that automated scanners could find and chain bugs like this within days, and cites a Reddit user whose site was compromised two days after disclosure.** — These are the host's own claims, not measured results. The 10-hour and weeks-to-months comparisons are unsourced in the video. ([3:50](https://youtu.be/38z2hdzV_DM?t=230))

## Techniques
- **Check batch endpoint nested requests against the same allow-list** — Re-run method and permission validation for every sub-request in a batch or nested request body, not only the outer request. Keep validation and dispatch results keyed to the same request object, not parallel arrays. *When:* Designing any batch, bulk, or multiplexed API. Relevant to a gateway that accepts batched agent or tool calls.
- **Escape or parameterize values reaching SQL on internal dispatch paths** — Do not assume an internally routed call is trusted. Use parameterized queries for every field that can arrive via a nested or re-dispatched request. *When:* Any handler reachable through several routes or internal re-dispatch.
- **Patch and check your WordPress version** — Upgrade to 7.0.2 or later. The host gives the affected ranges as 6.9.0 to 6.9.4 and 7.0.0 to 7.0.1 (captions read 6.90 to 6.94 and 7.00 to 7.01). Check for unexpected admin accounts and plugins that were not installed by you. *When:* Running WordPress 6.9.x or 7.0.x. The video does not show detection or cleanup steps beyond the upgrade.

## Numbers
- WordPress runs over 44% of the world's websites (host's figure). ([0:00](https://youtu.be/38z2hdzV_DM?t=0))
- The check script returns HTTP 207 when the target is vulnerable. ([0:00](https://youtu.be/38z2hdzV_DM?t=0))
- Affected versions as captioned: 6.90 to 6.94 and 7.00 to 7.01. Fixed in 7.0.2. ([0:00](https://youtu.be/38z2hdzV_DM?t=0))
- Host says a human researcher would need weeks or months, and the chain could not have been found in 10 hours without AI (unsourced). ([3:50](https://youtu.be/38z2hdzV_DM?t=230))
- A Reddit user reports their site was compromised two days after the bug was disclosed (anecdote). ([3:50](https://youtu.be/38z2hdzV_DM?t=230))

## Hot takes
- The title 'Worst Hack In History' is hype. The content is a 5-minute PoC demo of one bug, with no CVE number, no timeline and no before-and-after evidence.
- The claim that AI made this chain findable in about 10 hours, and that a human would need weeks or months, is unsourced in the video.
- The 44% figure is a host-quoted statistic with no source given in the video.

## Tools mentioned
WordPress, WordPress REST API (batch/v1, wp/v2 posts, wp/v2 users), A public proof-of-concept repo (the video does not name it; the link is in the description)

## Relevance to our work
- **agentos** (1/3): Security review of a proxy that must apply policy consistently to nested requests. The video itself is not about agents. → *Add a test case to the L1 proxy suite that sends a nested or batched payload carrying a disallowed method, and confirm it is blocked.*

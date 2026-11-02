# The Internet Is Full of Zombies and Nobody Is Talking About It

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `3yR45A3EGOU` · [watch](https://youtu.be/3yR45A3EGOU) · **date:** 2026-02-02 · **length:** 5:12 · **format:** other · **quality:** 2/5 · **depth:** intro
- **speakers:** Andrus · **orgs:** Better Stack, Cloudflare
- **topics:** infra-cost-scaling · **tags:** bgp, routing, networking, incident-analysis, byoip, cloudflare, reliability, make-before-break

> Explains BGP "zombie" routes that stay in some routers' tables after withdrawal, citing Cloudflare's observations and their make-before-break fix. Networking background, not AI.

## Summary
The video explains BGP zombies, outdated routes that some networks keep using after the originating network has withdrawn them. Withdrawal is normal when networks move traffic between data centers or take servers offline, but some routers fall back to a less specific route slowly and keep stale entries, so traffic loops, detours, or dead-ends and users see hangs or timeouts. The speaker cites Cloudflare's measurements that zombies lasted 6 to 11 minutes in large networks, with IPv4 zombies lasting longer than IPv6. Routes self-heal because BGP timers expire stale entries and ongoing neighbor updates eventually confirm the withdrawal. Cloudflare found the problem while handling BYOIP (bring your own IP) customers, where a temporary advertisement was withdrawn and some providers kept the old path. Their fix was to announce the same route from a stable location first, let routers converge on the new path, and only then withdraw the old announcement. The content is accurate at a high level but shallow, a secondhand summary of a Cloudflare blog post the speaker does not link in the transcript.

## Key ideas
- **A BGP zombie is a route that was withdrawn by its origin but still exists in other networks' routing tables, so traffic keeps flowing down a dead path.** — Withdrawal is routine (moving traffic between data centers, maintenance), but some routers keep believing the old route, causing loops, long detours, or dead-ends. ([1:09](https://youtu.be/3yR45A3EGOU?t=69))
- **The root cause is the fallback search after a more specific route disappears: routers look for a less specific route, and during that window some fail to clear the old entry.** — Speaker's explanation of why routers lag in updating the global map; the mechanism is described briefly. ([2:11](https://youtu.be/3yR45A3EGOU?t=131))
- **Zombies self-heal, but only after a delay: route timers delete stale entries, and ongoing BGP updates from neighbors eventually inform routers of the withdrawal.** — Cloudflare observed zombies lasting 6 to 11 minutes in large networks, with IPv4 zombies lasting longer than IPv6. ([2:11](https://youtu.be/3yR45A3EGOU?t=131))
- **Cloudflare discovered the behavior while handling BYOIP customers, where it temporarily advertises a customer's IP space and then withdraws it.** — Some providers kept using the old route long after the withdrawal, sending traffic into Cloudflare's network on unexpected and inefficient paths. ([3:03](https://youtu.be/3yR45A3EGOU?t=183))
- **The fix is to announce the same route from a stable location before withdrawing the old announcement, so routers move to the new path cleanly.** — This avoids the fallback surge that creates zombies. Cloudflare also tuned internal systems so future transitions go more smoothly. ([3:03](https://youtu.be/3yR45A3EGOU?t=183))
- **From a user's view, a zombie shows up as a hanging or timing-out page or a brief app connection failure, which is often short but sometimes very visible.** — The speaker frames this as usually resolved before users notice, with occasional visible effects. ([1:09](https://youtu.be/3yR45A3EGOU?t=69))

## Techniques
- **Make-before-break route handoff** — When moving traffic off a route or endpoint, first announce the same route from a stable, long-lived location so the rest of the system converges on the new path, and only then withdraw the old announcement. Withdrawing first lets laggard routers fall back to a stale path. *When:* Migrating traffic between locations or endpoints where some consumers update slower than others, such as BYOIP handoffs, failovers, or cutovers in a multi-site system.
- **Rely on TTL-style expiry as a backstop for stale state** — Route entries carry timers and are deleted if no fresh update arrives; ongoing gossip eventually removes stale entries even when a withdrawal is missed. *When:* Designing distributed caches, registries, or routing tables where a missed removal message must not persist forever. Expiry bounds how long stale state can survive.

## Numbers
- Cloudflare observed BGP zombies lasting 6 to 11 minutes in large networks. ([2:11](https://youtu.be/3yR45A3EGOU?t=131))
- IPv4 zombies tended to survive longer than IPv6 zombies (no figures given). ([2:11](https://youtu.be/3yR45A3EGOU?t=131))

## Hot takes
- Off-topic for an AI engineering KB: this is networking, with no AI or agent content.
- Thin on substance: a roughly 5-minute summary of a Cloudflare blog post the speaker does not link in the transcript. Treat the mechanism as a simplification.
- Clickbait-ish framing ("Full of Zombies and Nobody Is Talking About It") for a well-known operational phenomenon.

## Tools mentioned
BGP (Border Gateway Protocol)

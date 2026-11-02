# Astro is Joining Cloudflare (Here's Why)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `vpbNP4loCiE` · [watch](https://youtu.be/vpbNP4loCiE) · **date:** 2026-02-02 · **length:** 4:57 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** Better Stack host (unnamed) · **orgs:** Astro, Cloudflare, Vercel, Google, Microsoft, OpenAI, Wix, Webflow, Stainless, Tailwind, Bun, Hono, TanStack
- **topics:** dev-tools, vibe-coding-app-building · **tags:** astro, cloudflare, web-framework, open-source-funding, acquisition, islands-architecture, ssr, static-html, astro-6

> Astro, the MIT-licensed framework for content-driven sites, is joining Cloudflare. The team says it stays open source, multi-host and governed the same way, and the host sees the move as a funding fix for Astro.

## Summary
The host reports that Astro, an open source web framework for content sites like blogs, docs and e-commerce, is joining Cloudflare, and that the whole Astro team moves to Cloudflare full-time. Per the founder's announcement as relayed, Astro stays open source and actively maintained, keeps supporting non-Cloudflare deployment targets, and keeps its open governance and roadmap. The host's explanation for the deal is that Astro is MIT-licensed but backed by a VC-funded company, and paid hosted add-ons (database, storage, analytics) never caught on, so the company needed a new home for maintenance costs. He argues Cloudflare is a natural fit because both want a fast web (infrastructure and framework sides), Cloudflare already sponsored and used Astro, and Cloudflare has sponsored Hono and TanStack without locking them in. He also points to AI-era tools like Webflow Cloud, Wix Vibe and Stainless that already pair Astro with Cloudflare. The video closes by noting Astro 6 is in beta. Most of the content restates a blog post; the revenue and strategy points are the host's inference, not sourced figures.

## Key ideas
- **Astro is joining Cloudflare, and the whole team moves over full-time; the host frames it as one more framework being absorbed by a platform vendor (Cloudflare has Astro, Vercel has Next.js, Google has Angular, Microsoft has Blazor).** — The host opens with the consolidation framing and says the news looks good for Astro on balance. ([0:00](https://youtu.be/vpbNP4loCiE?t=0))
- **Announced commitments: Astro stays open source and actively maintained, keeps supporting deployment targets other than Cloudflare, and keeps its open governance and public roadmap.** — The host reads these as the key promises from the founder's blog post and contrasts them with the lock-in concern around Next.js and Vercel. ([1:16](https://youtu.be/vpbNP4loCiE?t=76))
- **Astro's core design: render on the server, send static HTML with the least JavaScript, and add interactive islands only where needed. It can still use React, Vue, Svelte or Solid components.** — The host explains the main selling point as fast content sites, citing Google, OpenAI and Cloudflare as users for blogs, marketing pages and docs. ([0:00](https://youtu.be/vpbNP4loCiE?t=0))
- **The business reason: Astro is MIT-licensed but backed by a VC-funded company. Its plan to sit at the center of a platform with paid hosted primitives (database, storage, analytics) fell flat with users.** — The host ties this to similar open-source-vs-company stories (Tailwind, Bun). Astro downloads have doubled each year and are near a million per week, but the host assumes revenue did not keep pace (inference, not a sourced figure). ([2:10](https://youtu.be/vpbNP4loCiE?t=130))
- **Why Cloudflare: both companies were after a fast web from different sides, infrastructure (Cloudflare) and framework (Astro). Cloudflare was already a longtime sponsor and used Astro for its docs, Workers landing page and marketing sites.** — The host also cites Cloudflare's track record of sponsoring projects like Hono and TanStack without locking them to its platform as evidence the openness promises are credible. ([3:12](https://youtu.be/vpbNP4loCiE?t=192))
- **AI-era demand: Webflow Cloud, Wix Vibe and Stainless already run on Cloudflare and Astro together, which the host reads as a sign the pairing fits both companies.** — This is the only concrete adoption evidence in the video, and it comes from the Cloudflare blog post as the host reports it. ([3:12](https://youtu.be/vpbNP4loCiE?t=192))
- **Astro 6 is in beta.** — The host says a dedicated video will follow. No release details are given. ([4:21](https://youtu.be/vpbNP4loCiE?t=261))

## Techniques
- **Server-rendered static HTML with islands** — Render the page on the server and send plain HTML with minimal JavaScript. Add interactive components as isolated islands (React, Vue, Svelte or Solid) instead of hydrating the whole page. The host describes this as Astro's main performance approach, with no code shown. *When:* Content-driven sites where initial load speed matters more than client-side app state: blogs, documentation, marketing pages, e-commerce catalogs.

## Numbers
- Astro downloads roughly double each year and are now nearly 1 million per week (host's figure, as stated in the video). ([2:10](https://youtu.be/vpbNP4loCiE?t=130))
- Astro 6 has reached beta. ([4:21](https://youtu.be/vpbNP4loCiE?t=261))

## Hot takes
- The host calls this good news for Astro because the funding problem is solved, but no revenue or financial figures are given to back that up.
- The 'everybody gets a framework' framing treats platform consolidation as a trend rather than analysing what changes for users.
- Cloudflare's openness record (Hono, TanStack) is presented as strong precedent, based on sponsorships rather than any stated contract terms.
- The host says Vercel 'does try and deny' lock-in concerns about Next.js, which is an opinion, not evidence from the announcement.

## Tools mentioned
Astro (6 in beta), Cloudflare (Workers), Next.js, Nuxt, Svelte, Angular, Blazor, React, Vue, Solid, Hono, TanStack, Webflow Cloud, Wix Vibe, Stainless, Tailwind, Bun, Vercel

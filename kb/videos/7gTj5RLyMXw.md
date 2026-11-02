# This Framework DESTROYS Next.js With 7x Faster Performance!

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `7gTj5RLyMXw` · [watch](https://youtu.be/7gTj5RLyMXw) · **date:** 2025-11-02 · **length:** 5:03 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed Better Stack presenter · **orgs:** Better Stack, Vercel, DigitalOcean
- **topics:** dev-tools, infra-cost-scaling · **tags:** fastify, nextjs, react, ssr, vite, benchmarking, autocannon, vercel, load-testing, web-framework

> Better Stack benchmarks Fastify with React (Vite SSR) against Next.js and finds a 5x gap on a local hello-page test, but only about 4% on a realistic to-do app once Vercel hosting is included. The "7x" headline comes from one maintainer benchmark.

## Summary
The presenter argues that Fastify with React, a Vite-based server-side rendering setup, can outperform Next.js, and cites a Fastify maintainer's benchmark where Next.js managed 49 requests per second against 347 for React with Fastify. He then runs his own AutoCannon load tests on an M1 MacBook: a simple SSR page reached 271 requests per second against 51 for Next.js. A to-do app with hooks, with Next.js on Vercel and Fastify on a DigitalOcean droplet, came out nearly even, at 468 versus 488 requests per second. He notes that Next.js was measured warm and that its cold start was slower, that the local run is not a Linux server, and that Fastify on Vercel was harder to set up. His conclusion is to choose Fastify with React if you are not on Vercel or want more server control, and that the Vercel case is less clear. The video shows no sponsor and no repo name in the transcript, and the numbers quoted in the intro do not match the later tests.

## Key ideas
- **Headline claim: Fastify with React is up to 7x faster than Next.js, based on a Fastify maintainer's benchmark (Next.js 49 req/s vs React+Fastify 347 req/s).** — The presenter takes these numbers from a third-party article. He does not rerun that benchmark himself, and the title's 7x comes from this single source. ([0:00](https://youtu.be/7gTj5RLyMXw?t=0))
- **Fastify React is a React SSR renderer for Fastify, built on Vite. Its focus is server rendering and client hydration, not the full feature set of Next.js.** — The presenter calls the narrower scope a good thing. He says the project tried React Server Components but dropped them because of thin documentation and friction with Webpack and Vite ESM imports. ([1:14](https://youtu.be/7gTj5RLyMXw?t=74))
- **On the simple local test, Fastify with React handled about 5.3x the requests of Next.js.** — AutoCannon, 10-second run, M1 MacBook Pro with 16 GB RAM: Fastify 3,000 requests in 10 s, average 271.2 req/s; Next.js 520 requests in 10 s, average 51 req/s. He says a Linux server would likely give different numbers. ([2:39](https://youtu.be/7gTj5RLyMXw?t=159))
- **On a realistic to-do app with hooks, the gap almost disappears.** — Next.js on Vercel averaged 467 req/s and Fastify on a DigitalOcean droplet averaged 487.8 req/s, both at 5,000 requests in 10 s. The two runs were on different hosts, so this compares hosting as well as framework. ([3:59](https://youtu.be/7gTj5RLyMXw?t=239))
- **Next.js was measured on a warm start. Its cold start handled only about 4K requests, and the presenter says Fastify on Vercel was not straightforward to deploy.** — Vercel is the case where he suggests Next.js is the less painful choice. The recommendation is to pick Fastify with React if you self-host, run locally, or want more server control. ([3:59](https://youtu.be/7gTj5RLyMXw?t=239))

## Techniques
- **Fastify + Vite SSR wiring for React** — The Fastify server file calls the Fastify-Vite setup and listens on port 3000. The Vite config includes the Vite React plugin and the Fastify-React plugin. The HTML shell has a mount element that the client JS hydrates. Exact commands and file names beyond these are not shown in the video; the repo is referenced but not named. *When:* Self-hosted React SSR on Node when you want Fastify's low overhead and control over the server, and do not need Next.js routing or React Server Components.
- **Confirm SSR before benchmarking** — Run the app in production mode and view the page source. The markup should already contain the rendered HTML, not an empty root div, before any load test is run. *When:* Before benchmarking any SSR framework, so you do not measure a client-only render by mistake.
- **AutoCannon 10-second load test** — Open a second tab and run AutoCannon against the page URL. The default duration is 10 seconds. Read the total request count and the average req/s from the output. Repeat against each app on the same settings. *When:* A quick single-endpoint throughput comparison. It is a crude method: one run, no stated warmup, and no latency percentiles.
- **Separate warm and cold start numbers** — Record warm-start throughput and cold-start throughput separately. The presenter measured Next.js warm (about 5K requests in 10 s) and cold (about 4K requests). *When:* Serverless or managed hosts, where cold starts can change the result a lot. Report both numbers, not just the warm one.

## Numbers
- Intro: about 1,000 requests per 10 s for the Fastify app vs about 400 for Next.js on the same app. These figures are not reconciled with the later tests. ([0:00](https://youtu.be/7gTj5RLyMXw?t=0))
- Maintainer's benchmark (cited, not rerun): Next.js 49 req/s vs React with Fastify 347 req/s, about 7x. ([0:00](https://youtu.be/7gTj5RLyMXw?t=0))
- Local simple SSR page, M1 MacBook Pro 16 GB, AutoCannon 10 s: Fastify 3,000 requests, average 271.2 req/s. Next.js 520 requests, average 51 req/s. Ratio about 5.3x. ([2:39](https://youtu.be/7gTj5RLyMXw?t=159))
- To-do app with hooks, AutoCannon 10 s: Next.js on Vercel 5,000 requests, average 467 req/s (warm). Fastify on DigitalOcean 5,000 requests, average 487.8 req/s. Gap about 4%. ([3:59](https://youtu.be/7gTj5RLyMXw?t=239))
- Next.js cold start on Vercel: about 4K requests in 10 s (presenter's figure, single run). ([3:59](https://youtu.be/7gTj5RLyMXw?t=239))

## Hot takes
- The title's 7x and DESTROYS claims come from one maintainer benchmark. The presenter's own tests show about 5.3x on a hello-page SSR test and about 4% on a realistic app, which is the honest result, but the headline does not reflect it.
- The realistic comparison pits Next.js on Vercel against Fastify on DigitalOcean. That is a comparison of hosts, not frameworks. The 4% gap is also within what a single 10-second run can vary.
- The intro numbers (about 1,000 vs 400 requests, 49 vs 347 req/s) do not match the later figures (3,000 vs 520, 51 vs 271). The presenter does not explain the difference.
- The local M1 test is labelled by the presenter as not representative of a Linux production server. The benchmark method has no warmup, no repeats, and no latency percentiles.
- The claim that React Server Components were dropped for lack of docs and Webpack or Vite friction is the presenter's account of the project's decision. It is not verified in the video.
- Quality is capped at 2: the title is hype, the benchmarks are single runs on different hosts, and the actionable part is short. Transcript caption errors ('cell' for Vercel, 'via coded' for vibe-coded) are not material.

## Tools mentioned
Fastify, Fastify React (fastify-react renderer), Vite, React, Next.js, AutoCannon, Vercel, DigitalOcean, Webpack, React Server Components (discussed, not adopted by Fastify React), Nuxt, Vue, useRootContext (hook name as transcribed), useServerAction (hook name as transcribed)

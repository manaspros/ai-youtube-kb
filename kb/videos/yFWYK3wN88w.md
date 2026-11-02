# Lightpanda: The 64MB Browser That is 60x FASTER than Chrome

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `yFWYK3wN88w` · [watch](https://youtu.be/yFWYK3wN88w) · **date:** 2026-05-02 · **length:** 5:35 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Better Stack, Lightpanda, Vercel, OpenClaw
- **topics:** voice-multimodal, mcp-and-tools · **tags:** lightpanda, headless-browser, web-fetch, browser-agents, puppeteer, chrome-devtools-protocol, memory-footprint, claude-sdk, benchmark

> Better Stack tests Lightpanda, a Zig-built headless browser that speaks CDP, against headless Chrome in a Claude SDK web-fetch agent: far less memory and faster at scale, but it fails on the Airbnb single-page app.

## Summary
The video introduces Lightpanda, a headless browser written in Zig for AI agents that exposes the Chrome DevTools Protocol so Puppeteer or Playwright can drive it. It does not render pixels and lacks some common web APIs. The host runs three tests: a single Wikipedia page (Lightpanda 344 ms vs Chrome 392 ms), 100 Wikipedia pages (about 18 s vs about 30 s, sometimes 60 s for Chrome), and a Claude SDK agent with a custom WebFetch tool that fetches three MDN pages. In the agent test, Lightpanda's fetch was roughly twice as fast and browser memory was 66 MB vs 829 MB, while wall time was the same. Lightpanda failed to extract Airbnb listings because it runs JavaScript only at the language level (V8) and does not render single-page apps. The host's verdict is that Lightpanda suits web search and fetch inside custom agents, while Chrome is still needed for JS-heavy SPAs. The sample is one run per setup, and the host's "never use Chrome again" line overstates the evidence.

## Key ideas
- **Lightpanda is a headless browser built for agents from the ground up in Zig, with no WebKit or Chromium. It exposes the Chrome DevTools Protocol, so Puppeteer or Playwright can connect to it.** — The host claims up to 9x faster and 16x less memory than headless Chrome. These are vendor figures relayed in the intro, not measured by the host. ([0:00](https://youtu.be/yFWYK3wN88w?t=0))
- **The design trade-off is that Lightpanda renders no pixels and omits some common web APIs (the captions name Service Workers and IndexedDB, among others). The host asks why agent tools such as OpenClaw and Vercel's agent browser use it anyway.** — The answer the video builds toward is that agents mostly need fetched content, not a visual page, so the missing features matter less for that job. ([0:00](https://youtu.be/yFWYK3wN88w?t=0))
- **On a single static page the speed gap is small: Lightpanda took 344 ms against Chrome's 392 ms for the Wikipedia references links.** — The gap grows with volume. Across 100 Wikipedia pages Lightpanda finished in about 18 s against roughly 30 s for Chrome, and Chrome sometimes took 60 s. ([0:55](https://youtu.be/yFWYK3wN88w?t=55))
- **In an agent loop the main difference is memory. Three MDN fetches through a Claude SDK agent gave Lightpanda a browser footprint of 66 MB against 829 MB for Chrome, with a fetch time about 2x faster. Wall time was the same.** — Agent memory was slightly lower with Lightpanda, but the host says the browser engine would not change that number much. ([3:40](https://youtu.be/yFWYK3wN88w?t=220))
- **Lightpanda fails on single-page applications. It could not extract listings from an Airbnb search in Tokyo, while Chrome did. The host attributes this to its JavaScript support being language-level only (V8 runs async/await, closures and promises, but not full SPA rendering).** — The host says this may change in future releases and is not sure it will. ([3:40](https://youtu.be/yFWYK3wN88w?t=220))
- **The host's verdict: Lightpanda is a strong addition to a custom agent that needs web search or web fetching, but Chrome remains necessary for complex SPAs.** — The video does not describe a routing scheme. The implied pattern is to use Lightpanda for fetch-only pages and fall back to Chrome for SPAs. ([4:59](https://youtu.be/yFWYK3wN88w?t=299))
- **The comparison was made fair by disabling Chrome's default caching, because Lightpanda has much less caching. The host also ran everything locally, although Lightpanda offers an MCP server and a cloud service.** — Disabling Chrome's caching is a method worth copying for any headless-browser benchmark. Without it the memory and timing numbers would not be comparable. ([1:55](https://youtu.be/yFWYK3wN88w?t=115))

## Techniques
- **Lightpanda as a CDP fetch backend** — Start the Lightpanda server with `lightpanda serve` (captioned as LightPanda serve; the port flag is not shown) and connect Puppeteer to that port before the agent runs. The connect call is not shown either. The same CDP client code works against Chrome, so the backend can be swapped. *When:* Web search, scraping or fetch tools in a custom agent, on static or server-rendered pages, where memory per run and throughput matter more than full rendering.
- **Custom WebFetch tool in a Claude SDK agent loop** — Define one WebFetch tool that takes URLs and a prompt, fetches the pages through the browser, and returns the content to Claude. The agentic loop checks which tool was called with an if statement. Add metrics around the loop: fetch time, wall time, browser memory computed from the browser process, and agent memory. *When:* Building a custom agent that needs web access, when you want per-run metrics to compare browser engines.
- **Fair headless-browser benchmark** — Before measuring Chrome, clear its default caching (the host notes Lightpanda has far less caching). Run the same scripts against both engines and time them, and measure browser memory per run. The host runs each setup once and reports a 60 s outlier for Chrome, so repeat runs before drawing conclusions. *When:* Any comparison of headless engines where caching differences would skew timing or memory.
- **Route by page type (implied by the verdict)** — Use Lightpanda for server-rendered or static pages such as Wikipedia and MDN. Send SPA targets such as Airbnb to Chrome. The video does not implement this, so it is the host's conclusion applied as a pattern, not a demonstrated technique. *When:* Agents that browse varied sites and need both low memory and SPA support.

## Numbers
- Vendor claim relayed in intro: up to 9x faster and 16x less memory than headless Chrome. Not measured by the host. ([0:00](https://youtu.be/yFWYK3wN88w?t=0))
- Single Wikipedia references page: Lightpanda 344 ms vs Chrome 392 ms. ([0:55](https://youtu.be/yFWYK3wN88w?t=55))
- 100 Wikipedia pages: Lightpanda about 18 s vs Chrome about 30 s, and up to 60 s in some runs. ([2:16](https://youtu.be/yFWYK3wN88w?t=136))
- Agent test with 3 MDN fetches: Lightpanda fetch time about 2x faster than Chrome, wall time the same. ([3:40](https://youtu.be/yFWYK3wN88w?t=220))
- Browser memory in the agent test: Lightpanda 66 MB vs Chrome 829 MB. The host says Chrome is more than 10x larger. ([3:40](https://youtu.be/yFWYK3wN88w?t=220))
- Host says Lightpanda is up to 21x smaller than Chrome. This conflicts with the same segment's figures (829/66 is about 12.6x) and should be treated as unreliable. ([3:40](https://youtu.be/yFWYK3wN88w?t=220))

## Hot takes
- Honestly, you should never use Chrome ever again for headless browsing. This is overstated: the video rests on single runs and its own Airbnb test contradicts it.
- Only one run per setup is shown and Chrome varied from 30 s to 60 s, so the timing gaps are not established with any confidence.
- The '21 times smaller' claim conflicts with the 829 MB vs 66 MB figures shown in the same segment (about 12.6x).
- The 'quick rebrand' and funding speculation is not supported by anything in the video.
- The SPA failure is the most useful finding in the video. It limits the verdict more than the speed numbers support the recommendation.

## Tools mentioned
Lightpanda, Chrome (headless), Puppeteer, Playwright, Claude SDK, Chrome DevTools Protocol, OpenClaw, Vercel agent browser, Chrome MCP server (referenced as a related video)

## Relevance to our work
- **agentos** (1/3): AgentOS exposes an agent-facing tool layer and budgets memory on a single RTX 5090. A lighter browser backend could matter if AgentOS ever ships a web-fetch tool, but the video shows nothing on that layer. → *If AgentOS adds a browsing or web-fetch tool, benchmark Lightpanda against headless Chrome on memory per run and on SPA failure rate, using the caching-disabled method from the video.*

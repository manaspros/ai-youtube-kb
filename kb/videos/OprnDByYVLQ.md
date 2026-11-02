# Browser Use + Claude Code Is INSANE (Free + Open Source + Real Browser)

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `OprnDByYVLQ` · [watch](https://youtu.be/OprnDByYVLQ) · **date:** 2026-08-02 · **length:** 6:45 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Channel host (Kai Explains; name not stated in transcript) · **orgs:** Anthropic, Microsoft, Google, Cloudflare
- **topics:** voice-multimodal, security-guardrails, token-cost-efficiency · **tags:** browser-agents, browser-use, computer-use, prompt-injection, accessibility-tree, dom-menu, cloudflare-bot-detection, token-cost, human-in-the-loop, sandboxing

> Browser Use plus Claude Code: the browser part is old, the new part is a model choosing actions from a numbered text menu of page elements. The menu makes it useful, and the same open page makes prompt injection a real risk when the browser is logged in.

## Summary
The host argues that browser automation is decades old (Selenium, Playwright, Puppeteer), so the new part is a language model choosing what to click from a plain-English goal. He contrasts the screenshot-and-coordinates approach (roughly Anthropic's computer use) with a text menu of numbered interactive elements, which he calls cheaper and more reliable. He then lists how real websites break the demo: cookie banners, Cloudflare checks, captchas, login and 2FA walls, infinite scroll, iframes, shadow DOM, and a menu that goes stale while the model is thinking. He points out that token cost compounds because each step rereads the menu, often for 10 to 40 steps per task. The main warning is prompt injection: a model driving a logged-in browser can be told by hidden page text to act on the user's behalf. His mitigations are throwaway accounts, a sandbox or VM, read-only low-stakes tasks first, a human gate on purchases and sends, and a step cap. The video shows no code, commands, or benchmarks.

## Key ideas
- **Browser automation is old; the new part is the model** — Selenium dates to about 2004 and Playwright and Puppeteer are established. The only new piece is a language model picking the element to act on from a plain-English goal on a page it has never seen. ([0:00](https://youtu.be/OprnDByYVLQ?t=0))
- **Screenshot-plus-coordinates is the naive approach and it is slow and expensive** — The approach sends a screenshot, asks where to click, gets pixel coordinates back, and repeats. He says it is roughly Anthropic's computer use approach. Images cost many tokens and pixel guessing is fragile. ([1:26](https://youtu.be/OprnDByYVLQ?t=86))
- **A numbered text menu of page elements is the core idea** — Turning the page into a short numbered list of interactive elements gives the model text it can order from. He calls it small, cheap, and reliable, and says it runs on a real browser with real JavaScript and cookies. ([1:26](https://youtu.be/OprnDByYVLQ?t=86))
- **Real websites break the happy path** — Cookie banners, Cloudflare checks, captchas, login and 2FA walls, infinite scroll, iframes, and shadow DOM all get in the way. The menu can go stale while the model thinks, so a stored element number may point at a different button by the time it clicks. ([2:47](https://youtu.be/OprnDByYVLQ?t=167))
- **Token cost compounds across steps** — An agent rereads the menu after every action, often 10, 20, or 40 times per task. A heavy page can have hundreds of interactive elements, so the free library still burns metered model tokens. ([2:47](https://youtu.be/OprnDByYVLQ?t=167))
- **Prompt injection is the real danger with a logged-in browser** — The model reads page content as context and cannot reliably separate instructions from text written by a stranger. Hidden text, alt attributes, or off-screen comments can tell it to act, and a logged-in session makes the damage larger. ([4:08](https://youtu.be/OprnDByYVLQ?t=248))
- **Use it like a loaded tool: sandbox, low stakes, human gates, step caps** — Run it on throwaway accounts inside a sandbox or fresh VM, start with read-only low-stakes jobs, require a human to confirm purchases, sends, and deletes, cap the number of steps, and keep it away from bank accounts. ([5:36](https://youtu.be/OprnDByYVLQ?t=336))

## Techniques
- **Numbered interactive-element menu for browser agents** — Extract the page's interactive elements (links, buttons, inputs) from the live DOM and give each a stable index. Send the model that text list plus the goal, have it return an index and an action, execute on a real browser, then re-read the menu. The speaker describes this approach but shows no code. *When:* When you want cheap, text-based, reliable element selection instead of screenshot pixel coordinates, especially on pages the agent has not seen before.
- **Untrusted-page threat model for browser agents** — Treat everything the page renders, including hidden text, alt attributes, and comments, as attacker-controlled input. Do not give the agent a logged-in session for anything that matters. Use a throwaway account, a sandbox or fresh VM, and no access to money or data you care about. *When:* Before pointing any browser agent at a site the user is logged into, or at any site that could contain adversarial content.
- **Staged rollout for browser agents: read-only first** — Start with read-only, low-stakes tasks such as scraping, research, or filling forms on sites you do not care about. Add write actions only after that works. *When:* When first deploying a browser agent, before it has any path to purchases, sends, or deletes.
- **Human gate on destructive browser actions and a step cap** — Pause for a human to confirm any purchase, send, delete, or final confirm click. Cap the number of agent steps per task so a loop cannot run dozens of rounds unattended. *When:* For any long-running or unattended browser agent run, especially one that can spend money or change data.

## Numbers
- Browser automation with Selenium dates to roughly 2004 ([0:00](https://youtu.be/OprnDByYVLQ?t=0))
- Agent loops reread the page menu each step, often 10, 20, or 40 times for one task ([2:47](https://youtu.be/OprnDByYVLQ?t=167))
- Heavy pages can have hundreds of interactive elements in the menu ([2:47](https://youtu.be/OprnDByYVLQ?t=167))
- Speaker estimate, unsourced: the happy path is about 5% of the real web ([2:47](https://youtu.be/OprnDByYVLQ?t=167))
- Browser Use library is MIT licensed (speaker's statement) ([2:47](https://youtu.be/OprnDByYVLQ?t=167))

## Hot takes
- The browser part of Browser Use plus Claude Code is the oldest and most boring part of the stack; the novelty is the LLM choosing actions from a text menu.
- The library is free, but the model tokens are metered, and each agent step rereads the page.
- Prompt injection through a logged-in browser is a bigger risk than the demo shows, and the speaker says Anthropic warns about it in its computer use docs.
- The clean demo web is not representative; the happy path is a small share of real sites (speaker's own unsourced estimate).

## Tools mentioned
Browser Use, Claude Code, Claude, Anthropic computer use, Selenium, Playwright, Puppeteer, Google Flights, Cloudflare (bot check)

## Relevance to our work
- **agentos** (2/3): The L1 proxy scans for prompt injection and PII, and L2C Crucible handles sandboxed execution. A browser agent with logged-in sessions is a concrete injection-through-tool-output case that these pieces should cover. → *Add a test corpus of hidden-text and alt-text injection payloads (white-on-white, aria-label, off-screen elements) and check whether the L1 prompt-injection scan catches them when they arrive as tool or page results.*
- **prosharness** (2/3): ProsHarness has phone-driven approvals and loops. The speaker's main safety recommendation is a human gate on destructive actions plus a step cap, which maps directly onto that design. → *Route browser or tool actions tagged as purchase, send, or delete through the existing phone approval flow, and add a hard max-step cap to long-running loops.*

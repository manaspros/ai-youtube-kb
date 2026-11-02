# How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `V_5bn4q-vAI` · [watch](https://youtu.be/V_5bn4q-vAI) · **date:** 2026-09-18 · **length:** 16:27 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Christopher Burns · **orgs:** Inth, C15T, LeadType, Mintlify, Vercel, Cloudflare, Y Combinator, Stripe
- **topics:** context-engineering, mcp-and-tools, product-ux, coding-agents · **tags:** llms.txt, llms-full.txt, AGENTS.md, markdown twins, content negotiation, web MCP, node_modules docs, agent discovery, docs as context, token efficiency, agent readiness, LeadType, Next.js

> Christopher Burns (Inth) on making LLMs recommend and correctly use his open-source cookie-banner library by shipping agent-friendly docs: hand-written llms.txt, markdown twins, web MCP, and grep-able docs inside node_modules.

## Summary
The speaker maintains C15T, an open-source cookie banner library, and says AI assistants now drive its largest share of inbound signups. He argues that developer tools should optimise for agents: coding agents often never visit the docs site and instead read the installed package in node_modules. His stack, wrapped in a tool called LeadType that runs over .mdx files, includes a hand-written llms.txt, a markdown twin of every page advertised by a header, several ways to reach that markdown, and an agents.md file that tells agents to grep bundled docs. He also mentions a web MCP that exposes search, get-pages and ask-docs tools, and agent-readiness scoring sites that he treats as volatile. The talk is practitioner-level with some self-promotion, and the numbers are self-reported with no method given.

## Key ideas
- **Developer tools are now discovered through LLM recommendations** — After the library's onboarding form showed spikes in 'how did you hear about us' from April 13, AI assistants (Claude, ChatGPT, Codex, Gemini) became the number one inbound source. Installation has moved from humans following a wizard to agents being given a prompt. ([1:09](https://youtu.be/V_5bn4q-vAI?t=69))
- **A hand-written llms.txt beats a generated one** — The speaker's testing found that about 40 carefully written lines beat a 1,000-line generated index, which he calls noise. The index should be a curated map of the docs that agents can navigate. ([5:30](https://youtu.be/V_5bn4q-vAI?t=330))
- **Serve a markdown twin of every page and advertise it** — Each docs page gets a .md version, and a link header tells agents that a markdown alternative exists. Agents can then skip HTML, which is expensive in tokens. He says the adoption of this header is uneven across agents. ([6:57](https://youtu.be/V_5bn4q-vAI?t=417))
- **Offer markdown through more than one access path** — Agents differ in what they can send, so the same markdown is reachable by appending .md, by an Accept: text/markdown redirect in the framework config, and by a ?mode=agent query parameter. ([8:16](https://youtu.be/V_5bn4q-vAI?t=496))
- **Expose the docs through a web MCP** — Agents cannot ask a website questions, so the tool exposes search-docs, get-pages and ask-docs tools over MCP. He describes this as early, but he considers it the most important future direction. ([9:26](https://youtu.be/V_5bn4q-vAI?t=566))
- **Coding agents read node_modules, not your website** — For libraries, agents mostly read the repo and installed package source, and their training data is often stale. Shipping the bundled markdown inside the package, with an agents.md that says to grep it, gave him a claimed saving of about half the tokens compared with web search, and it works without skills. ([10:20](https://youtu.be/V_5bn4q-vAI?t=620))
- **Agent-readiness scores are volatile, so keep iterating** — He points to external checkers (a Cloudflare tool and a newer one called Aura AI). His own site scored 59 and had been much higher three weeks before, so he treats the score as a moving target rather than a goal. ([12:40](https://youtu.be/V_5bn4q-vAI?t=760))
- **If you can only do one thing, do markdown per page plus llms.txt** — In Q&A, for a general website he recommends a .md for every page first, then llms.txt and llms-full.txt. He says many CMSs cannot produce this, but he still recommends it, and he built his own CMS for this purpose. ([14:05](https://youtu.be/V_5bn4q-vAI?t=845))

## Techniques
- **Hand-curated llms.txt index** — Write a short (about 40 lines) llms.txt by hand that maps the most important pages and what each is for, rather than auto-generating a long index. Add llms-full.txt as the full-content version. *When:* Documentation sites with hundreds of pages, where agents need to find the right page quickly and a noisy index wastes tokens.
- **Markdown twin per page with discovery header** — Build a .md version of each page from the .mdx source with a build step (LeadType generate). Advertise it with a link/alternate header on the HTML page. *When:* Any docs or marketing site that agents visit, especially when the HTML is large and token cost matters.
- **Three ways to reach markdown** — Serve the same markdown at a .md URL suffix, behind a redirect that honours Accept: text/markdown, and behind a ?mode=agent query parameter for agents that cannot set headers. *When:* When you do not know which headers or request shapes the agents you care about will send.
- **Bundle docs in the package with an agents.md pointer** — Ship the markdown docs inside the published npm package, and add an agents.md that tells agents to read or grep these files for any question, then verify the bundled docs match the code. *When:* A library whose API changes often, where agents would otherwise search the web or rely on stale training data. Works with or without an extra skill.
- **Web MCP for docs** — Expose docs search, page retrieval and an ask-docs endpoint as MCP tools on the site so agents can query it directly. *When:* When agents need to ask targeted questions of a large docs set, rather than fetch whole pages.
- **Agent-readiness checks as a loop** — Run external agent-readiness checkers against the site, then change the markdown, llms.txt or headers and re-check. *When:* When you want a measurable target for how agent-friendly your docs are, while accepting that the scoring rules change.

## Numbers
- C15T had about 1.2k downloads when the speaker first presented it at NextConf; now close to 2 million (speaker's figure). ([1:09](https://youtu.be/V_5bn4q-vAI?t=69))
- About 3 million npm downloads, with roughly 45% month-on-month growth (transcript reads '4.5, 45%', so the first figure is uncertain). ([1:09](https://youtu.be/V_5bn4q-vAI?t=69))
- About 2.8k websites in production use, including Mintlify, Zed and others. ([1:09](https://youtu.be/V_5bn4q-vAI?t=69))
- Since April 13 the AI assistants (Claude, ChatGPT, Codex, Gemini) became the number one inbound source on the onboarding form (speaker's figure). ([1:09](https://youtu.be/V_5bn4q-vAI?t=69))
- A hand-written llms.txt of about 40 lines beat a 1,000-line generated one in the speaker's testing. ([5:30](https://youtu.be/V_5bn4q-vAI?t=330))
- Bundling docs in node_modules with an agents.md pointer gave almost 50% token savings versus agents searching the web, across several models (method not described). ([10:20](https://youtu.be/V_5bn4q-vAI?t=620))
- The speaker's site scored 59 on Aura AI's agent-readiness test, down from a much higher score about three weeks earlier. ([12:40](https://youtu.be/V_5bn4q-vAI?t=760))

## Hot takes
- Coding agents almost never visit your website; they read the installed package in node_modules, so ship the docs there.
- Write llms.txt by hand. A generated 1,000-line index is noise, and 40 good lines beat it.
- Even a CMS-driven site should provide a markdown file for every page, because agents now visit more pages than humans do.
- The 'how did you hear about us' form is now a measurement tool for how much AI assistants are recommending you.

## Tools mentioned
LeadType, llms.txt, llms-full.txt, AGENTS.md, Next.js, Aura AI, Cloudflare agent-readiness checker, MCP

## Relevance to our work
- **prosharness** (1/3): ProsHarness drives Claude Code runs, and the talk's point about agents reading bundled docs instead of searching the web could cut search tokens in those runs, but the talk is about public docs rather than harness internals. → *Check whether ProsHarness's own docs and skill references could be bundled as grep-able markdown with an AGENTS.md pointer, and measure the token difference on one long run.*

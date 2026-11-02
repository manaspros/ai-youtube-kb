# 500 people vibe-coded for 30 days. I was one of them. - Sanja Grbic, Automattic

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `UcYoMg-8-L8` · [watch](https://youtu.be/UcYoMg-8-L8) · **date:** 2026-07-18 · **length:** 17:49 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Sanja Grbic · **orgs:** Automattic
- **topics:** enterprise-adoption, vibe-coding-app-building, product-ux, coding-agents · **tags:** radical-speed-month, vibe-coding, product-designers, design-engineering, prototype-first, pairing, claude-code, figma, enablement, large-org-adoption, design-system, woocommerce, jetpack

> Automattic's 30-day "Radical Speed Month" experiment, in which about 500 people in paired teams shipped roughly 794 projects, and how the speaker moved from designer to design engineer by prototyping in code before Figma.

## Summary
Sanja Grbic, a product designer at Automattic (about 1,400 people, fully distributed), describes Radical Speed Month. Roughly a third of the company (about 500 people) paused roadmap work for 30 days, worked in two-person teams with full autonomy, and shipped real projects, around 794 in total. AI use was optional but widely used. The speaker walks through three projects: a board game session manager built in two hours during an enablement course, a design system status tracker built largely alone over about 2.5 weeks, and an iOS chat app for WooCommerce merchants built in six days with another designer. She reports that her process shifted from Figma-first to prototype-first in code, that engineers' most valuable role was enabling others, and she closes with org-level advice: give people access, find champions, make room for experiments, and give them agency. The talk is an experience report with few hard metrics.

## Key ideas
- **A time-boxed, company-wide experiment can unlock AI-driven shipping faster than top-down tool rollout.** — Automattic paused roadmap work for 30 days, paired people up, gave them full autonomy and asked them to ship something real. AI use was optional, but about 500 people (a third of the company) took part and shipped around 794 projects. Staging the rollout in rounds made it manageable. ([0:01](https://youtu.be/UcYoMg-8-L8?t=1))
- **Company-wide enablement came before the experiment and made it possible.** — Each employee took a two-week role-specific immersive AI course. Ops built a dev environment that a non-engineer could spin up. An internal Context MCP server gave AI tools access to the company's documented knowledge. Coding contributions were encouraged as coding tools improved. ([2:42](https://youtu.be/UcYoMg-8-L8?t=162))
- **The most valuable engineer contribution in a mixed-skill team may be enabling others rather than writing more code.** — In a two-hour board game app build with two designers, a product lead and an engineer, the engineer set up the GitHub project and taught Git basics. The speaker says the impact of enabling others can exceed the impact of doing more engineering personally, and that engineers will need to become enablers and teachers as non-engineers begin to commit code. ([7:52](https://youtu.be/UcYoMg-8-L8?t=472))
- **Designers can move from handing off mockups to owning a working product end to end.** — The design system status tracker pulled links from GitHub, Storybook and Figma, sorted them by status and tagged them with library names, with live component previews. The speaker built the full proof of concept alone. It went from a prototype in about a week to an internal and a public-facing deployment after about another week and a half, which she describes as the move from designer to design engineer. ([9:10](https://youtu.be/UcYoMg-8-L8?t=550))
- **Prototype in code first, then use Figma only for visual finishing.** — Normally the team would work in Figma to high fidelity first. In the WooCommerce iOS chat project they started in a Claude Code project folder where chats and ideas were saved as files, built the working prototype, and only then returned to Figma for a mood board and UI fine-tuning. The speaker says this sped up both collaboration and the build, and she has kept the practice. ([14:42](https://youtu.be/UcYoMg-8-L8?t=882))
- **The speaker's caveat: this worked because of the experiment's freedom, and large organizations need guardrails.** — Her process fit within existing onboarding, security and system constraints. She argues teams can get the same result by providing access to the tools, finding champions, creating space for experiments, and giving people agency to break habits. ([16:08](https://youtu.be/UcYoMg-8-L8?t=968))

## Techniques
- **Time-boxed paired ship sprint** — Pause normal roadmap work for a fixed period (here 30 days). Pair people up with mixed skills, give them full autonomy, require a real shipped outcome, and roll the program out in stages so it stays manageable. *When:* To break habits in a large org and see what AI tools can ship when people have agency and no roadmap pressure.
- **Prototype-in-code before design tool** — Start the exploration as a Claude Code project folder, keep chats and ideas recorded as files, build a working prototype, then go back to Figma only for mood boards and visual polish. *When:* For new products where a working prototype answers feasibility and feel questions faster than high-fidelity mockups.
- **Shared file-based exploration log** — Record chats, ideas and decisions in a project folder that the coding agent and collaborators both work from, instead of keeping them in separate chats. *When:* When two or more people shape a product with an agent and need shared context for collaboration and later build steps.
- **Aggregating scattered sources into a status tracker** — Have the tool pull links from repos, Storybook and Figma, then sort by status and tag by library. Show live component previews rather than static screenshots. *When:* When information about a large, fast-changing design system or set of components is spread across tools and needs to be surfaced to both humans and AI tools.
- **Engineer as enabler in mixed-skill pairs** — The engineer sets up the repo and teaches Git and basic commands. Everyone commits code. Pairs share an understanding of how to use the tools together. *When:* When designers, product people or ops staff start contributing code in a team that has engineers.

## Numbers
- Company size is about 1,400 people, fully distributed and asynchronous. ([0:01](https://youtu.be/UcYoMg-8-L8?t=1))
- About a third of the company (around 500 people) took part in the first round. ([3:45](https://youtu.be/UcYoMg-8-L8?t=225))
- The first round started around 794 projects in 30 days. ([3:45](https://youtu.be/UcYoMg-8-L8?t=225))
- Role-specific AI enablement course per employee lasted two weeks. ([2:42](https://youtu.be/UcYoMg-8-L8?t=162))
- Board game session app built in two hours. ([6:27](https://youtu.be/UcYoMg-8-L8?t=387))
- Design system status tracker: about 2.5 weeks total, with the prototype built in about a week, then about 1.5 weeks to rebuild for hosting and deployment. ([11:53](https://youtu.be/UcYoMg-8-L8?t=713))
- WooCommerce iOS chat proof of concept built in six days by a pair of designers. ([13:14](https://youtu.be/UcYoMg-8-L8?t=794))

## Hot takes
- An engineer's biggest impact may come from enabling others, not from doing more engineering.
- Prototyping in code before Figma can shift a designer's process within about 30 days.
- Designers can become design engineers when they own the full path from idea to deployed product.
- Enablement and agency, not tool rollouts, are what unlock AI-driven speed in large organizations.

## Tools mentioned
Claude Code, Figma, Storybook, GitHub, Nano Banana, Context MCP server, WordPress.com, Jetpack, WooCommerce

## Relevance to our work
- **prosharness** (1/3): Keeping shared chats and ideas as files in a Claude Code project folder, and building prototypes before polish, is close to ProsHarness's checkpoint and resume model. The talk only describes it in passing. → *Read the next Claude Code workflow notes to decide whether the handoff between exploration and build should be a file-based log that ProsHarness checkpoints.*

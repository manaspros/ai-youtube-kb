# Content Is Code - Matt Palmer, Conductor

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `yv6xovSsB1U` · [watch](https://youtu.be/yv6xovSsB1U) · **date:** 2026-08-18 · **length:** 10:53 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Matt Palmer · **orgs:** Conductor, Replit, Anthropic, OpenAI
- **topics:** product-ux, context-engineering, coding-agents · **tags:** content-engineering, code-as-communication, remotion, react, typescript, changelogs, design-tokens, docs, devrel, product-tour-video, structure-over-taste

> Matt Palmer (Conductor) argues code is becoming the medium for technical content, so docs, changelogs and product videos should be generated from a structured source of truth.

## Summary
Matt Palmer, who leads developer experience at Conductor, argues that code is now the fastest way to make technical content such as docs, changelogs, emails, product tours and videos. He splits content history into three eras: handcrafted content, expensive code where engineering was the bottleneck, and today's cheap code. He says the scarce resource is now structure (clean PRs, tagged changes, design tokens, internal docs and skills), not taste, and that AI rewards this kind of conscientiousness. He shows a product tour for Conductor built with React and Remotion that recreates the product surface, and admits it is still buggy. His closing prediction is that 2026 was the year of the creative technologist and 2027 will be the year of the content engineer, with declarative content pipelines. The talk is mostly opinion and framing; it gives few measurements and little implementation detail.

## Key ideas
- **Code is becoming the way technical content is produced** — Docs, changelogs, emails, marketing and video can all be generated from code. Before AI, only professional engineers wrote code for content, so content was a low priority. ([0:00](https://youtu.be/yv6xovSsB1U?t=0))
- **Content has moved through three eras** — Era 1 was handcrafted content, limited by time, money and skill. Era 2 had code, but engineers were expensive and the bottleneck. Era 3 is today, where code is cheap and AI tools can produce assets. ([2:51](https://youtu.be/yv6xovSsB1U?t=171))
- **Changelogs are a diff problem** — An accurate changelog needs an accurate diff of the product. Without it, someone has to read through PRs by hand to work out what shipped. Good PR tagging and descriptions make this possible. ([1:25](https://youtu.be/yv6xovSsB1U?t=85))
- **Structure is the expensive part now, not taste** — Maintaining a structured codebase, consistent brand guidelines, design tokens kept apart from app code, clean merges, PR tags and up-to-date internal docs are the hard work. Most organizations do not do these well. ([5:49](https://youtu.be/yv6xovSsB1U?t=349))
- **AI output quality follows conscientiousness** — Generic output (what he calls purple-gradient slop) comes from missing structure. Careful, meticulous work with clear expectations matters more than raw technical skill, and agents need docs and skills to succeed. ([7:10](https://youtu.be/yv6xovSsB1U?t=430))
- **Make the codebase the source of truth for content** — If content is generated from code, the code has to be structured. Organizational discipline in software creation is what allows content to be produced from it. ([8:35](https://youtu.be/yv6xovSsB1U?t=515))
- **Prediction: 2027 is the year of the content engineer** — He expects declarative, robust content pipelines that produce walkthroughs, documentation, screenshots and product updates from code. He calls 2026 the year of the creative technologist. ([9:57](https://youtu.be/yv6xovSsB1U?t=597))

## Techniques
- **Generate product tour videos with React and Remotion** — Recreate the product surface as React components, then use Remotion scenes to walk through a sample user flow. The result is code, so it can be re-rendered when the product changes. He says it is buggy and the flows are not finished yet. *When:* When you need a product walkthrough or demo video that must be kept up to date as the product changes.
- **Derive changelogs and product updates from the diff** — Use an accurate diff or well-tagged PRs as the input, then summarize them for users. Emails and product updates follow from the changelog. *When:* When changelogs are late or incomplete, or someone has to comb through PRs by hand to find what shipped.
- **Keep design tokens separate from app code** — Store brand values in their own layer, apart from front-end and back-end code, so that generated assets and UI stay consistent with brand guidelines. *When:* When agents or generated content produce off-brand or inconsistent visuals.
- **Write internal docs and skills for agents** — Document how the team does things and encode it as skills. Agents without this documentation cannot solve structural problems such as tagging or merge hygiene. *When:* When agents keep producing work that is generic or does not follow the team's conventions.

## Hot takes
- Structure is the expensive thing now, not taste.
- AI rewards conscientiousness and organizational excellence more than raw technical skill.
- Most organizations do not merge clean PRs or tag them properly, and that undermines generated content.
- 2027 will be the year of the content engineer.

## Tools mentioned
React, TypeScript, Remotion, CSS, HTML, Claude

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps Claude Code, and its output quality depends on how well its context and skills are structured. The talk makes that point in general terms only. → *Audit the CLAUDE.md and skill docs that ProsHarness passes to Claude Code for missing structure and conventions.*

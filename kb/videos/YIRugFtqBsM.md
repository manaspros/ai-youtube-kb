# Tailwind is Dying... (this is bad!)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `YIRugFtqBsM` · [watch](https://youtu.be/YIRugFtqBsM) · **date:** 2026-02-02 · **length:** 8:18 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** Better Stack host (unnamed) · **orgs:** Better Stack, Tailwind CSS
- **topics:** dev-tools, vibe-coding-app-building, product-ux · **tags:** open-source-sustainability, llms-txt, documentation, tailwind-css, tailwind-plus, ai-traffic, maintainer-funding, vibe-coding

> A Better Stack commentary on a Tailwind CSS maintainer's refusal to review an LLMs.txt PR, arguing AI is eroding docs traffic and the paid products that fund open source.

## Summary
The video covers a GitHub PR, opened 18 Nov 2025, that asked Tailwind CSS to add an LLMs.txt endpoint serving LLM-optimized docs. The PR sat unreviewed until the maintainer replied that he had more pressing business problems. He tied the reply to layoffs (team cut from four engineers to one) and to a collapse in revenue, with docs traffic down about 40% since early 2023 while npm downloads grew sharply. The host explains the model: Tailwind is free, but Tailwind Plus (paid components and templates) funds maintenance, and docs visits are the funnel to those sales. AI answers now replace docs visits, so the funnel shrinks even as usage explodes. The host calls LLMs.txt good for package users but says it does not fix the monetization problem, and he doubts major LLM providers use it. He closes by suggesting ShadCN's free component model may also be pulling buyers away from Tailwind Plus.

## Key ideas
- **The story starts with an unreviewed PR to add an LLMs.txt endpoint for LLM-optimized Tailwind docs.** — The PR was opened 18 Nov 2025 and went unreviewed. The maintainer's eventual reply cited more pressing business problems, and the host's framing is that the reply was widely read as a sympathetic but worrying response. ([0:00](https://youtu.be/YIRugFtqBsM?t=0))
- **Tailwind's funding model depends on paid Tailwind Plus products, and docs visits are the top of that funnel.** — The library is free, but Tailwind Plus (components, templates, UI kits) pays for maintenance. The host compares this to Laravel, Sidekiq, Elastic and Redis, which also run companies around open-source cores (his examples, not verified). ([1:10](https://youtu.be/YIRugFtqBsM?t=70))
- **AI assistants are removing the traffic that open-source companies monetize through docs.** — The maintainer's reply says docs are the only way people discover commercial products. Vibe coders ask an LLM to implement things instead of reading docs, so fewer people see Tailwind Plus. ([2:33](https://youtu.be/YIRugFtqBsM?t=153))
- **Usage and business health are diverging: npm downloads rose while docs traffic and revenue fell.** — The host quotes the maintainer on layoffs and on docs traffic down about 40% from early 2023. He also cites npm downloads of about 6M at the start of last year and 32M at the end. Per the maintainer, revenue is down close to 80%, which the host presents as the real issue. ([4:52](https://youtu.be/YIRugFtqBsM?t=292))
- **LLMs.txt helps package users but does not connect ease of use to the maintainers' income.** — The host says the feature benefits developers using the package, but with no link between Tailwind being easier to use and its sustainability, a better LLM experience does not fund the project. He calls the risk abandonware if maintainers cannot be paid. ([4:52](https://youtu.be/YIRugFtqBsM?t=292))
- **The host doubts LLMs.txt will matter because LLMs already scrape docs and major providers reportedly ignore the convention.** — He says models were probably trained on Tailwind docs and many public examples, so they can already write common UI blocks. He also says he has heard LLMs.txt is not a standard and that Anthropic and OpenAI do not use it. He did not verify either claim. ([7:13](https://youtu.be/YIRugFtqBsM?t=433))

## Techniques
- **Publish an LLM-optimized docs endpoint (LLMs.txt)** — Serve a machine-readable version of the docs at an LLMs.txt endpoint, as proposed in the Tailwind PR. The video does not show an implementation, and the host says the convention is not yet a standard that major providers use. *When:* When your library or product has a large public docs site that LLM coding assistants read, and you want cleaner context for them. Do not expect it to drive traffic or revenue on its own.
- **Tie docs funnel to paid products, and track docs traffic against usage** — The open-core pattern in the video: free library, paid companion products (components, templates), and docs as the discovery path. The lesson is to watch docs traffic alongside downloads, since the two can diverge when AI answers questions directly. *When:* When you maintain an open-source library that funds itself through a commercial add-on and you see usage growth without matching revenue.

## Numbers
- The LLMs.txt PR to Tailwind docs was opened on 18 Nov 2025. ([0:00](https://youtu.be/YIRugFtqBsM?t=0))
- Team went from four engineers to one, with three laid off, per the maintainer's comment (about 75% of the engineering team). ([2:33](https://youtu.be/YIRugFtqBsM?t=153))
- Docs traffic is down about 40% from early 2023, while Tailwind is more popular than ever. ([2:33](https://youtu.be/YIRugFtqBsM?t=153))
- npm downloads were about 6M at the start of last year and about 32M at the end. ([2:33](https://youtu.be/YIRugFtqBsM?t=153))
- Maintainer says revenue is down close to 80% (as quoted in the video). ([4:52](https://youtu.be/YIRugFtqBsM?t=292))
- Host's own rough attribution: 80-90% of the decline is AI's fault. This is a speculative estimate, not data. ([7:13](https://youtu.be/YIRugFtqBsM?t=433))

## Hot takes
- Title says Tailwind is dying, but the substance is a maintainer's revenue and staffing problem, not evidence the library is failing (cap quality at 2 for hype title and thin analysis).
- Host claims major LLM providers do not use LLMs.txt. He did not verify this.
- Host attributes 80-90% of the decline to AI without data.
- ShadCN's free, open-source component model may be pulling buyers away from Tailwind Plus. The host offers this as speculation.
- Speculation about a Tailwind pivot (for example a design-focused vibe-coding product) is the host's idea, not something the maintainers said.

## Tools mentioned
Tailwind CSS, Tailwind Plus, Tailwind v4, LLMs.txt, npm, ShadCN, Laravel, Sidekiq, Elastic, Redis, Anthropic, OpenAI

## Relevance to our work
- **general** (1/3): Useful background on how AI usage shifts can hurt open-source maintainer funding, which matters for choosing which dependencies to support. → *Check whether any open-source dependencies used in our projects have sponsorship pages, and sponsor the ones we rely on heavily.*

# The Missing Layer: Design Taste in AI Agents — Hassan El Mghari, Together AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `7GMKdpLsxwU` · [watch](https://youtu.be/7GMKdpLsxwU) · **date:** 2026-09-18 · **length:** 14:10 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Hassan El Mghari · **orgs:** Together AI, Cursor
- **topics:** vibe-coding-app-building, product-ux, context-engineering, coding-agents · **tags:** design-taste, ai-slop, frontend, agents-md, skills, model-tiering, screenshots-as-context, vibe-coding, hallmark

> Hassan El Mghari (Together AI) on getting AI-built UIs out of "AI slop": codify the tells as anti-patterns, feed in references, iterate with a cheaper model.

## Summary
The speaker, who leads developer experience at Together AI and says he is not a designer, has built about 10 AI apps a year and argues that UI polish is what made his apps reach large audiences. He says vibe-coded AI apps share recognizable tells (purple gradients, italic headers, scroll-to-explore, all-caps spaced pills, gradient logos, emojis), and that a little extra UI effort gives a real edge. His first tool is Hallmark, a design skill that lists these "slop gates" as things the model should avoid and adds a library of visual themes as inspiration; he reports about 10,000 users in roughly six weeks. His second line of advice is process: give agents screenshots and references, keep a persistent agents.md of do/avoid rules, write longer and more specific prompts (often dictated as voice notes), and send one or two features per prompt. He recommends building the base with a strong model such as Codex or Claude Code, then iterating with a smaller, faster open model such as GLM 5.2, which he says is close in design quality at a fraction of the cost and latency. He closes by saying one-shot output is only a starting point to iterate on.

## Key ideas
- **Small UI effort is a competitive edge** — He says that spending an extra 10-20% of effort on the UI, after the functionality works, can clearly separate an app from generic AI output. He credits design and UX as the main reason his apps got users. ([0:08](https://youtu.be/7GMKdpLsxwU?t=8))
- **Make the AI tells explicit** — Most AI-built sites share a list of 20-30 recognizable patterns. He says that naming them lets you ban them in the prompt or in a skill, because many people can see that a site looks AI-made but cannot say why. ([3:34](https://youtu.be/7GMKdpLsxwU?t=214))
- **Codify anti-patterns and themes in a design skill** — Hallmark has two parts: a list of slop patterns the model must avoid, and a set of themes that the model uses as starting inspiration. He says that strong inspiration leads to much better output. ([3:34](https://youtu.be/7GMKdpLsxwU?t=214))
- **Use a cheaper model for iteration** — He builds the base with a frontier coding agent and then iterates with a smaller open model. In a blind comparison, GLM 5.2 and Opus 4.8 landing pages were hard to tell apart, and the smaller model was faster and much cheaper. ([7:13](https://youtu.be/7GMKdpLsxwU?t=433))
- **Persistent preferences go in agents.md** — Each time a logo or layout comes out badly, he adds a rule to an agents.md file, for example what to avoid and how to do the logo. Over time this file captures his taste so he does not have to correct it again. ([9:31](https://youtu.be/7GMKdpLsxwU?t=571))
- **References and screenshots matter most** — He keeps an inspiration vault of sites and apps he likes and pastes screenshots into the prompt, saying the output is much better. He calls this the single most important tip. ([10:31](https://youtu.be/7GMKdpLsxwU?t=631))
- **Longer prompts, one or two features at a time** — His prompts are often two to three paragraphs, dictated as voice notes, and each one covers one or two features. He queues follow-up feature messages behind the first big prompt. ([11:38](https://youtu.be/7GMKdpLsxwU?t=698))
- **One-shot output is a base, not a finished product** — He says the main gains come from several rounds of feedback and iteration, not from accepting the first result. ([12:52](https://youtu.be/7GMKdpLsxwU?t=772))

## Techniques
- **Slop-gate anti-pattern list in a design skill** — Write the recognizable AI-design tells (gradients, italic headers, emoji use, all-caps pills, and so on) as explicit things the model must not do, and load that list as a skill or rules file before generating UI. *When:* Any time an agent builds a landing page or front end and the output needs to look intentional rather than generic.
- **Theme library as inspiration** — Keep a set of named visual themes and feed them into the design skill, so the model picks from concrete options instead of defaulting to its own style. *When:* When the agent keeps producing the same default look across projects.
- **Screenshot inspiration vault** — Save screenshots of sites and apps you like, then paste several into the prompt and describe the mix you want (for example, part of one app plus part of another). *When:* Before starting any new UI, so the agent has concrete visual references instead of only text.
- **Two-tier model routing for UI work** — Use a strong coding agent to make the first version. Then do the many small revision rounds with a cheaper, faster open model that is close enough in quality. *When:* When iteration speed and cost matter more than the first-shot quality, and the cheap model is good enough on the task.
- **agents.md as a taste log** — After each bad output, add a concrete avoid or do rule to the project's agents.md, so the same mistake is not made again. *When:* Across a long series of projects or features where your preferences repeat.
- **Batched feature prompting** — Send one long, specific prompt for the app shell with screenshots, then queue separate short prompts for one or two features each. *When:* Building a multi-feature app with a coding agent that can work through a queue of messages.

## Numbers
- About 10 apps built per year for the last five years; some reached millions of users (his claim) ([0:08](https://youtu.be/7GMKdpLsxwU?t=8))
- Logo creator app used by about 85,000 people ([1:33](https://youtu.be/7GMKdpLsxwU?t=93))
- Subtitle generator app used by about 8,000 people ([1:33](https://youtu.be/7GMKdpLsxwU?t=93))
- Hallmark design skill launched about 1.5 months earlier and has over 10,000 users ([5:01](https://youtu.be/7GMKdpLsxwU?t=301))
- In one comparison, the larger model cost about 5x as much and was noticeably slower than GLM 5.2 for similar output ([7:13](https://youtu.be/7GMKdpLsxwU?t=433))

## Hot takes
- Vibe-coded AI apps mostly look the same, and people can spot them within a second or two.
- A cheaper open model like GLM 5.2 is good enough for design iteration, even when a frontier model made the base.
- References and screenshots matter more than any other prompting tip for UI quality.
- Accepting a one-shot AI app as final is the main mistake people make.

## Tools mentioned
Codex, Claude Code, Cursor, Hallmark, agents.md, GLM 5.2, Opus 4.8, Composer 2.5, Together AI

## Relevance to our work
- **prosharness** (1/3): The agents.md taste log and the cheap-model iteration tier are relevant to how ProsHarness runs Claude Code sessions, but the talk is only about UI design. → *Add a short do and avoid section to the ProsHarness agents.md, built from the corrections made during a run, and check whether a smaller model can handle the revision steps in the plan-critique loop.*
- **general** (1/3):  → *When an agent builds a registry or dashboard page, give it two or three reference screenshots and a short slop-pattern list in its context file before the first prompt.*

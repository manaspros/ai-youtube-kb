# Imagination Engineering: "Live in the future and then build what's missing."

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Z2Erdirpudo` · [watch](https://youtu.be/Z2Erdirpudo) · **date:** 2026-07-18 · **length:** 16:04 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed YC design lead (name not stated in transcript) · **orgs:** Y Combinator, Conductor
- **topics:** product-ux, vibe-coding-app-building, context-engineering · **tags:** software-on-demand, thinking-in-public, personal-tools, voice-md, design-system, agent-readable-docs, claude-opus-4.8, fable-5, conductor, slack, imagination-engineering

> A YC design lead shows "software on demand" built from a week of public stream-of-consciousness Slack posts, plus a one-morning personal tool, and argues idea generation is the new bottleneck.

## Summary
The speaker, who leads design at Y Combinator, argues that once models make building easy, the scarce skill is generating ideas worth building. He describes "thinking in public": for a week he posted unfiltered brain dumps to a Slack channel, then asked Opus 4.8 to aggregate them into a personal website covering his interests, tools, books, and quotes. The site also got a stack dashboard, a design system that updates when components change, a voice.md distilled from his public writing, and a completeness checklist. He then built a "Shape of Minds" explorer in one morning that compares historical thinkers across dimensions such as routines, obsessions, and worldview, and used the model to pull out highlights. Smaller personal tools followed: a Slack emoji search, a componentized design language, an agent-readable glossary markdown, and short digest reports for commutes. He closes by pointing to cloud workspaces where agents can be launched from the road, and he frames the whole thing as an open experiment with no benchmarks or metrics.

## Key ideas
- **The new bottleneck is generating crazy, non-obvious ideas, because models will make it easy to build almost anything.** — The speaker thinks the valuable skill now is stretching the mind to invent things that seem impossible today, not execution. He frames the talk around this. ([0:08](https://youtu.be/Z2Erdirpudo?t=8))
- **Think in public: share a running stream of consciousness with trusted people, the way Paul Graham's essays shared his thinking.** — He copied a colleague's Slack channel of raw thoughts and started his own for a week. The raw dumps became the input for everything that follows. ([3:34](https://youtu.be/Z2Erdirpudo?t=214))
- **Aggregate a brain dump into a personalised site in one generation step.** — The model picked up his interests, quotes, projects, tools, and books from the dumps. The site let him adjust background, typography, width, dark mode, and translation, which he calls a future of design made of sliders. ([4:38](https://youtu.be/Z2Erdirpudo?t=278))
- **Have the model distil your public writing into a voice file and a design-language file.** — He asked for a voice.md built from his tweets and other writing, and a design-language file that updates when he creates or changes a component. ([8:05](https://youtu.be/Z2Erdirpudo?t=485))
- **Build a small personal tool in one morning and let the model handle the work.** — The Shape of Minds explorer, comparing historical thinkers across dimensions with hover details, was started at 10 a.m. with a model that could not yet use the newest release. The highlights were generated about 20 minutes before the talk, so he had not read them yet. ([9:05](https://youtu.be/Z2Erdirpudo?t=545))
- **Software on demand: any stream of consciousness can become a tool if you ask an agent to build it.** — Examples include a search for Slack emoji, an emoji picker that copies on click, and a glossary markdown of the site meant to be read by agents more cheaply than scraping the page. ([11:35](https://youtu.be/Z2Erdirpudo?t=695))
- **Use models as a personal tutor: ask for short reports on topics you want to learn, then read them on the go.** — Topics included the 10 principles of good design and Renaissance patronage. He wants to launch agents from his phone while travelling, using cloud workspaces. ([13:04](https://youtu.be/Z2Erdirpudo?t=784))

## Techniques
- **Public thought log as agent input** — Post unfiltered stream-of-consciousness notes to a shared channel every day, then feed the accumulated log to a model to synthesise into artifacts such as a site, profile, or tool. *When:* When you want a model to pick up your interests and taste without writing a formal spec.
- **Distil a voice file from public writing** — Have the model read everything you have published (posts, tweets, writing) and write a voice.md describing tone and what makes the writing distinctive. *When:* When you want consistent first-person writing or a style guide that agents can reuse.
- **Self-updating design language** — Keep the design system as a document that the model rewrites whenever a component changes, so the doc does not drift from the code. *When:* When one person builds many small UIs and wants consistency without manual upkeep.
- **Agent-readable glossary markdown** — Write a compact markdown glossary of everything a page displays, and point agents at it instead of having them read the rendered page. *When:* When agents need project facts cheaply and the source page is large or visual.
- **Checklist-driven completeness** — Ask the model to list everything a project needs before launch (for example, social preview image) and track progress against that list. *When:* When a personal or side project has many small launch steps that are easy to forget.
- **Timeboxing with a timer** — Start a timer at the beginning of a build session to set a hard limit on the work. *When:* When you have a deadline and want to limit scope.

## Numbers
- Stream-of-consciousness logging ran for about one week before the website was generated. ([0:08](https://youtu.be/Z2Erdirpudo?t=8))
- The Shape of Minds tool was started at 10 a.m. and was built in one morning, with highlights generated about 20 minutes before the talk. ([9:05](https://youtu.be/Z2Erdirpudo?t=545))
- A personal timer was set when work began to cap the build session; he had five minutes left when presenting the last items. ([11:35](https://youtu.be/Z2Erdirpudo?t=695))
- The talk runs 16:04 in total; no benchmarks, costs, latencies, or adoption metrics are given. ([16:04](https://youtu.be/Z2Erdirpudo?t=964))

## Hot takes
- The new bottleneck is coming up with crazy ideas, not building.
- The future of design will be mostly sliders.
- Models with this capability feel like AGI.
- Whatever stream of consciousness you have, you should just ask an agent to build it.
- Thinking in public may be as valuable as building in public.

## Tools mentioned
Claude / Claude Code, Opus 4.8, Fable 5, Conductor, Slack, Paper (design tool), ChatGPT (used to make the header image)

## Relevance to our work
- **general** (2/3): Shows several patterns for keeping personal context current for agents (voice file, self-updating design doc, stream-of-consciousness log). These are directly relevant to context engineering. → *Try a self-updating voice.md or project-context file generated from a raw notes log, and measure whether it improves agent output consistency.*
- **agentos** (1/3): The agent-readable glossary markdown idea is a cheap way to give agents project facts without scraping a page. Only loosely related to AgentOS's context needs. → *Consider a compact glossary markdown for AgentOS's docs as a cheaper context source for agents, then compare its token cost against reading the full docs.*
- **prosharness** (1/3): Launching agents from a phone while travelling matches ProsHarness's phone-driven approvals, but the talk gives no mechanism to reuse. → *Read the cloud-workspace part (around 14:34) only if a concrete phone-to-agent launch pattern is being designed for ProsHarness.*

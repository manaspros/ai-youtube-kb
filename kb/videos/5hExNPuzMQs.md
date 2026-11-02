# Remix is DROPPING React (and I'm excited)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `5hExNPuzMQs` · [watch](https://youtu.be/5hExNPuzMQs) · **date:** 2025-11-02 · **length:** 4:33 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Remix, React Router, Preact
- **topics:** dev-tools · **tags:** remix, react-router, preact, react, web-frameworks, model-first-development, web-standards, zero-dependencies

> Short news recap: Remix v3 is being rebuilt without React on a forked Preact, with AI-first, web-API-first, runtime-only, zero-dependency principles, and no upgrade path from React Router v7 or Remix v2.

## Summary
The video announces that Remix v3 will drop React and build on a fork of Preact, a roughly 3KB React-compatible library. The speaker explains the history first: Remix began as a paid framework around $250 before going open source, focused on SSR and progressive enhancement, then became a thin wrapper over React Router and was merged into React Router v7. Remix v3 is presented as a clean break with no upgrade path from React Router or Remix v2, which only shares the name. The announced principles are model-first development (optimizing for AI-assisted building and AI-powered apps), web-platform APIs over framework abstractions, no build steps or bundler magic, and zero dependencies so the team controls its own roadmap. The speaker is enthusiastic about the AI-native bet but says nobody yet knows what model-first development looks like. The piece is a four-and-a-half-minute recap with no code, no timeline beyond the framing, and no link to the primary announcement.

## Key ideas
- **Remix v3 will drop React and be built on a fork of Preact rather than React.** — Preact is described as a roughly 3KB alternative with the same modern API. The team forks it instead of depending on it as a package. ([1:19](https://youtu.be/5hExNPuzMQs?t=79))
- **Remix was merged into React Router v7, which freed the team to start a new project.** — Remix v2 had become a thin wrapper over React Router, so the two projects were duplicating work. The merge into v7 is what gave the Remix team room to rebuild. ([1:19](https://youtu.be/5hExNPuzMQs?t=79))
- **Remix v3 is a clean break with no upgrade path from React Router or Remix v2.** — The speaker's version graph runs RR v5, v6, then Remix v1 and v2 on top of v6, RR v7 absorbing Remix v2, and Remix v3 as a separate project that only shares the name. ([3:22](https://youtu.be/5hExNPuzMQs?t=202))
- **Model-first development is the first stated principle: optimize for AI and LLMs, both for building apps and for apps that use AI.** — The speaker finds the bet interesting but says nobody yet knows what model-first development looks like, and that most current AI work just bolts AI onto old patterns. ([1:19](https://youtu.be/5hExNPuzMQs?t=79))
- **The other stated principles are web-API-first, runtime-first, and zero dependencies.** — Web-API-first means using platform APIs instead of framework-specific abstractions. Runtime-first means no build steps or bundler magic, with everything working without pre-processing. Zero dependencies means control over the roadmap, which is why Preact is forked rather than imported. ([2:25](https://youtu.be/5hExNPuzMQs?t=145))
- **Remix's history: started as a paid framework (around $250) and then went free and open source, with a focus on SSR and progressive enhancement.** — The speaker frames it as an answer to common React app problems: client-only rendering, poor bundle size, neglect of web fundamentals, and request waterfalls and race conditions. ([0:00](https://youtu.be/5hExNPuzMQs?t=0))

## Techniques
- **Own a small runtime by forking it instead of depending on it** — Fork the upstream library's source into the project instead of consuming it as a versioned package, so the roadmap is not set by someone else. The speaker cites Preact (about 3KB, same API as React) as the base for Remix v3. *When:* When upstream roadmap or breaking changes threaten a long-lived framework, and the base library is small enough to maintain.
- **Build on web platform APIs instead of framework-specific abstractions** — Use standard web APIs (fetch, Request/Response, forms, and so on) directly instead of learning framework-specific equivalents. The speaker presents this as the Remix team's long-standing stance. *When:* When designing a framework or app layer that should stay portable and keep its learning curve low. Stated by the speaker as a principle, not demonstrated.

## Numbers
- Remix's original paid license cost around $250 before it was made free and open source. ([0:00](https://youtu.be/5hExNPuzMQs?t=0))
- Preact is described as a roughly 3KB alternative to React with the same modern API. ([1:19](https://youtu.be/5hExNPuzMQs?t=79))

## Hot takes
- The title says Remix is dropping React, but the speaker's enthusiasm ("I'm excited") outpaces the evidence: the video gives no technical detail, no code, and no link to the primary announcement.
- The speaker questions whether keeping the Remix name is confusing, and says Remix v3 is effectively a new framework that shares a name.
- Model-first development is presented as a bet the speaker finds fascinating, but the speaker admits no one knows yet what it means in practice.
- The video's own framing is that this is a clean break with no upgrade path, which reduces its relevance to anyone running React Router v7 or Remix v2 apps today.

## Tools mentioned
Remix, React Router, React, Preact, Next.js

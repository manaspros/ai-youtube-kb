# The Next Game Engine Won't Have a Manual — Arturo Nunez, Nereu

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `VBCDhRrvlYo` · [watch](https://youtu.be/VBCDhRrvlYo) · **date:** 2026-09-18 · **length:** 19:33 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Arturo Nunez · **orgs:** Nereu, Unity, MongoDB, Unreal
- **topics:** vibe-coding-app-building, agent-architecture, product-ux, context-engineering · **tags:** game-engine, entity-component-system, asset-tagging, natural-language-authoring, level-of-detail-context, vision-model-tagging, closed-alpha, claude-code

> Arturo Nunez (ex-Unity, MongoDB) pitches Nereu, a tag-driven, describe-it-to-build game engine where an AI assistant (Bibi) edits scenes via an Asset Tag System, so creators never touch engine vocabulary or code.

## Summary
The speaker argues that game engines should move from component and parameter setup toward describing intent in game-design language. In Nereu, every asset is an entity with tags (ECS-style), and systems query those tags to drive behavior. An LLM assistant named Bibi reads the available tags and tools, then adds or removes tags based on a natural-language request. Context is assembled from the scene, the asset library and the game genre, and it is trimmed with a level-of-detail idea so nearby objects get more detail. Assets were tagged by a vision model across roughly 6,000 to 7,000 models. The talk is an early-stage product demo and vision talk, with no benchmarks or measured results. The speaker says the tool is in closed alpha and built iteratively with Claude Code. The main open problem he names is that the LLM still needs to be guided by the vocabulary of the engine, otherwise it reinvents the same code each time.

## Key ideas
- **Describe intent, not implementation** — The speaker wants creators to describe a game in game-design language (for example 'move with WASD', 'double jump', 'when you collect a coin, increase the score') rather than set up meshes, renderers, colliders and sliders. ([5:18](https://youtu.be/VBCDhRrvlYo?t=318))
- **Every asset is an entity with tags, and systems act on tags** — Nereu borrows entity-component-system and data-oriented design. Assets carry tags, and systems query all entities with a given tag set (for example vehicle plus drivable) and act on them. Any object can get a behavior just by receiving a tag. ([9:14](https://youtu.be/VBCDhRrvlYo?t=554))
- **The LLM edits a scene only through a fixed set of tools** — The assistant knows the available tools and tags, and it applies changes by adding or removing tags. The engine has no scripting layer by design. Behavior logic is JavaScript that runs in the browser, and power users can extend it. ([10:36](https://youtu.be/VBCDhRrvlYo?t=636))
- **Context is limited with level-of-detail** — Rather than sending the full scene, the context is built like level-of-detail rendering. Objects near the user or the current selection get full tag and setting detail, and distant ones are reduced to a bare mention of their position. The context refreshes as the user edits. ([15:05](https://youtu.be/VBCDhRrvlYo?t=905))
- **Vision models are used to label a large asset library** — With about 6,000 to 7,000 assets, typing descriptions by hand was not realistic. The speaker took screenshots of each asset, ran a vision model on them, and generated descriptions from the screenshots and file names. ([14:07](https://youtu.be/VBCDhRrvlYo?t=847))
- **Genre and mood must be decomposed into engine parameters** — A request such as 'a scary platformer' has to be mapped onto lighting and post-processing settings as well as the tags. The speaker calls this the hardest part of the composing. ([11:38](https://youtu.be/VBCDhRrvlYo?t=698))
- **Build the engine with the coding agent and prune features** — The speaker discusses features with domain experts and then builds them with Claude. He removes settings that users do not use, and each new tool is added to the assistant's tool definitions as it is built. ([12:43](https://youtu.be/VBCDhRrvlYo?t=763))

## Techniques
- **Entity tags as an intent layer over ECS** — Describe assets with tags such as character, animated, drivable, and let systems query the tag sets and run the behavior. Keep the tag vocabulary small and documented so an LLM can compose it. *When:* When many domain objects need to share behaviors, and users should author by describing them, not by configuring components.
- **LLM-as-editor with a tool-only interface** — The assistant gets the current scene summary, the available tools, and the asset library. It applies changes only through tool calls (add or remove tags), so every change is structured and reversible. *When:* When an agent edits a domain structure that a non-expert user has to be able to trust and understand.
- **Level-of-detail context assembly** — Give full information for nearby or selected items and a coarse summary for distant ones. Re-derive the context as the user moves around and edits. *When:* When a scene or project is too big to send in full and the context window is the bottleneck.
- **Vision-model asset captioning** — Render each 3D asset to a screenshot, run a vision model on it, and combine the description with the asset name and file to create searchable metadata. *When:* When a large library of unlabeled assets must be searched or matched by natural-language description.
- **Domain expert in the loop while building with a coding agent** — Talk to domain experts about a feature, bring their input into a planning session with the coding assistant, build it, and then remove features that users do not use. *When:* When building a tool that needs domain judgment and needs to stay simple as it grows.

## Numbers
- About 6,000 to 7,000 assets in the library were labeled with a vision model. ([14:07](https://youtu.be/VBCDhRrvlYo?t=847))
- A scene in the demo had about 100 assets, most of them grass that could be ignored. ([15:05](https://youtu.be/VBCDhRrvlYo?t=905))
- The speaker worked at Unity for almost 10 years. ([3:58](https://youtu.be/VBCDhRrvlYo?t=238))
- The tool is in closed alpha, with a waitlist. No users or adoption numbers are given. ([16:58](https://youtu.be/VBCDhRrvlYo?t=1018))

## Hot takes
- The next game engine should have no manual, and the context should be game design rather than the engine's vocabulary.
- Most game-engine complexity (sliders, boilerplate components) is avoidable and should be hidden behind tags.
- World models will be a separate medium from traditional games, and real-time 60fps at 4K is still far off.

## Tools mentioned
Claude Code, Unity, Unreal, vision model

## Relevance to our work
- **general** (2/3): Concrete context-assembly ideas (level-of-detail context, refresh on edit) and a practitioner account of building a tool with Claude Code and pruning features. → *Try a level-of-detail context builder for large inputs: full detail for the active item and a summary for the rest, refreshed on each turn.*
- **prosharness** (1/3): Its tag-based intent layer and LLM-as-editor with a tool-only interface loosely resemble harness tool design, but the talk offers no harness mechanics. → *Optional: keep the constraint that the LLM can change state only through a small, documented set of tools, and check that ProsHarness's own tool surface follows it.*

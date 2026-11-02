# HTML Is All Agents Need — James Russo, HeyGen

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Cz4v1WHVyZc` · [watch](https://youtu.be/Cz4v1WHVyZc) · **date:** 2026-08-18 · **length:** 15:13 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** James Russo · **orgs:** HeyGen
- **topics:** voice-multimodal, context-engineering, skills-self-improvement, product-ux · **tags:** html-as-output-format, video-generation, deterministic-rendering, headless-browser, agent-skills, thin-wrapper, evals, launch-videos, open-source

> HeyGen's Hyperframes turns agent-written HTML into deterministic MP4 video by freezing the browser clock and seeking frame by frame; the thinnest HTML wrapper beat heavier DSLs.

## Summary
James Russo (co-creator and tech lead of Hyperframes at HeyGen) argues that HTML, CSS and JavaScript are the native language of LLMs, so agents should author video in HTML instead of a custom DSL or JSON format. HeyGen tried several wrappers around HTML with bigger system prompts, extra context and skills, and found the thinnest one (plain HTML plus a few data attributes for timing) worked best. The hard part was rendering: browsers load assets asynchronously, so Hyperframes freezes the page clock, seeks to each frame, waits for everything to load, screenshots, and encodes the result. Preview and final render use the same browser output. Skills focus on video taste and motion craft rather than teaching HTML syntax, and evals are used to raise the quality floor of single-shot output. Good results still need a storyboard, iterative frame-by-frame work, and a human last-mile edit in the open-source studio. Speaker's own caveat: models are still weak at creative work, and the team is building a code-to-video benchmark with LLM labs.

## Key ideas
- **HTML/CSS/JS is the model's native language; custom DSLs and JSON force it to learn a second language.** — Speaker compares a new DSL to asking Shakespeare to write a poem in Japanese: few-shot examples don't close the gap. Letting agents write HTML gives better output. ([1:37](https://youtu.be/Cz4v1WHVyZc?t=97))
- **Thinnest wrapper won.** — HeyGen tried many wrappers with larger system prompts, more context and skills. The best was plain HTML with a few data attributes for timing and metadata. Their reasoning: if a small model (Gemini 3 Flash) can author it, larger models and coding agents can too. ([5:27](https://youtu.be/Cz4v1WHVyZc?t=327))
- **Creative DSLs and frameworks cost controllability and creativity.** — After Effects and Premiere are the quality benchmark but are not agent-friendly. Lottie and Rive are editable only in limited ways. Remotion-style frameworks needed teaching the framework and many examples, which the speaker says took away creativity. ([4:01](https://youtu.be/Cz4v1WHVyZc?t=241))
- **Browsers are async by design, so video needs a deterministic render path.** — Fonts, images and video can load late and change the page. A video frame needs every asset ready, so the render path must wait for them. ([6:53](https://youtu.be/Cz4v1WHVyZc?t=413))
- **Deterministic rendering: freeze the clock, seek frame by frame, wait for load, screenshot, encode.** — The same browser pixels seen in preview become the video frames. Anything renderable in a browser (Three.js, WebGL/WebGPU, SVG, shaders, Lottie, charts) can go into a video. ([7:52](https://youtu.be/Cz4v1WHVyZc?t=472))
- **Skills should teach taste, not the language.** — Because agents already know HTML, HeyGen's skills cover video and motion craft. Other frameworks' skills mostly explain how to write that framework's syntax. ([8:55](https://youtu.be/Cz4v1WHVyZc?t=535))
- **Evals raise the floor, but great output still takes human craft.** — Single-shot website-to-video output is decent after eval-driven skill work. Great output comes from storyboarding, frame-by-frame motion work, and a human last-mile edit in the open-source studio with keyframes. ([9:57](https://youtu.be/Cz4v1WHVyZc?t=597))

## Techniques
- **Thin HTML as the agent output format** — Have the agent write plain HTML/CSS/JS with only a few data attributes for timing and metadata. Avoid a custom DSL, JSON schema or heavy wrapper prompts. *When:* When agents must produce a structured visual artifact and you want the model writing in its native language.
- **Deterministic frame-by-frame browser rendering** — Freeze the page clock, seek to each frame timestamp, wait until fonts, images and media are loaded, capture a screenshot, and encode the frames to MP4. *When:* When you need reproducible output from async web content, such as video, image sequences or snapshot tests.
- **Single render path for preview and output** — Use the same DOM and browser rendering for the live preview and the final export, so what the author sees is what gets encoded. *When:* When a WYSIWYG preview must match the final artifact exactly.
- **Taste-focused skills instead of syntax skills** — Write skill content about motion principles, design judgment and quality criteria, and leave out how to write the base language, which the model already knows. *When:* When the base language is well known to the model and the skill is meant to improve output quality, not API accuracy.
- **Small model as a format canary** — Test whether a small, cheap model can author valid output in a candidate format. If it can, expect larger models to do it too. *When:* When choosing an output format or DSL for agent-generated artifacts.
- **Storyboard, iterate, then human last-mile edit** — Plan the narrative and each frame first, then have the agent add motion one frame or keyframe at a time, then finish in an editor a human can drive. *When:* When output quality needs creative control and humans must stay in the loop.
- **Website-to-asset single-shot skill** — Point the agent at a URL, have it pull assets and branding, then generate a draft from design tokens plus a few example motion patterns. *When:* When generating branded first drafts from an existing web presence.

## Numbers
- Over 1.3 million videos rendered by open-source Hyperframes users in the last 90 days ([12:09](https://youtu.be/Cz4v1WHVyZc?t=729))
- 267,000 creators have tried Hyperframes ([12:09](https://youtu.be/Cz4v1WHVyZc?t=729))
- About 15,000 videos rendered per day with the open-source framework ([12:09](https://youtu.be/Cz4v1WHVyZc?t=729))
- About 32,000 GitHub stars ([12:09](https://youtu.be/Cz4v1WHVyZc?t=729))
- Team has worked on this approach for over a year; Hyperframes was released a couple of months before the talk ([2:40](https://youtu.be/Cz4v1WHVyZc?t=160))
- Gemini 3 Flash was the small-model design partner for testing whether formats are workable ([5:27](https://youtu.be/Cz4v1WHVyZc?t=327))

## Hot takes
- The thinnest wrapper ultimately won; bigger prompts, extra context and skills on top of wrappers did not help.
- Let's not fight the model: let agents write in HTML, their native language, rather than teaching them a framework.
- After Effects and Premiere give the best creative output but are not agent-friendly.
- Skills should teach taste, not framework syntax.

## Tools mentioned
Hyperframes, HTML/CSS/JS, Three.js, WebGL, WebGPU, Lottie, Rive, Remotion (transcribed as "Promotion"), After Effects, Premiere Pro, Gemini 3 Flash, Claude Code, Codex, Cursor

## Relevance to our work
- **agentos** (1/3): SkillForge's open question is how to score skill-worthiness. The talk's finding that skills which teach judgment beat syntax-heavy skills is a testable idea for that scoring. → *Run a SkillForge ablation: same task with a minimal taste-only skill vs a syntax-heavy skill, and score both on success rate and token cost, to test the skill-worthiness signal.*
- **prosharness** (1/3): ProsHarness works with Claude Code skills and skill ranking. The talk argues that syntax-heavy skill content adds little when the model already knows the base language. → *Audit ProsHarness skill files for content that restates tool syntax the model already knows, then A/B the trimmed skill against the current one on a fixed task set before rewriting any skill.*
- **general** (1/3): Shows that a thin HTML output format beat heavier DSL wrappers for agent-authored visuals, a context-engineering data point. → *Read the Hyperframes repo and its skills to compare how they keep the skill small against our own skill files.*

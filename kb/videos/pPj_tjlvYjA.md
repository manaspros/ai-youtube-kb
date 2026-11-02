# Building an Agentic Video Editor for Mass Consumer — Ekaterina Deyneka, Reelful

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `pPj_tjlvYjA` · [watch](https://youtu.be/pPj_tjlvYjA) · **date:** 2026-09-18 · **length:** 12:45 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Ekaterina Deyneka · **orgs:** Reelful, a16z speedrun
- **topics:** sandboxing-execution, product-ux, testing-verification, voice-multimodal · **tags:** agentic video editing, Remotion, sandbox per job, plan approval gate, verification layer, skills as craft, mobile-first, directional templates, consumer AI

> Reelful's founder shows how an agentic video editor turns real footage into a clip: media understanding, a user-approved plan, a sandboxed agent with skills, Remotion rendering, and a verification loop.

## Summary
Ekaterina Deyneka, founder and CEO of Reelful, says video editing is tedious and still mostly manual, and that agents could handle most of the pipeline. She compares agentic video editing to agentic app building: both use a prompt UI, a remote sandbox with an agent, tools and skills, and both return a result (a rendered video instead of an app preview). She argues that editing real footage is harder than generating from a blank canvas, because the agent must pick moments, cut messy material, and still deliver a polished clip. The pipeline runs media understanding and transcription first, then a creative plan the user can approve, change or regenerate, and only then a sandbox where the agent works. Remotion (video as React code) is the rendering layer, and a verification step checks that the composition is valid and renders, so the agent can iterate on errors. For mass consumers, Reelful is mobile-first, offers directional templates so users need no prompt, and provides a manual editor for small tweaks. The talk closes with a beta call and a note on a16z speedrun funding, and gives no benchmarks.

## Key ideas
- **Agentic video editing has the same infrastructure shape as an agentic app builder.** — Both have a prompt UI, a remote sandbox with an agent, tools and skills. The output differs: a rendered video instead of an app preview. ([2:32](https://youtu.be/pPj_tjlvYjA?t=152))
- **Editing real footage is a harder agent problem than generating from scratch.** — With a blank canvas the agent can do anything. With user footage it must choose the best moments, omit weak ones, organize the rest, and hide that the result is AI-edited. ([3:30](https://youtu.be/pPj_tjlvYjA?t=210))
- **Show a creative plan and get user approval before spending on execution.** — The pipeline does media understanding and transcription first, then a plan the user can approve, change or regenerate. The sandbox starts only after approval. ([4:49](https://youtu.be/pPj_tjlvYjA?t=289))
- **Encode editing taste as skills.** — Skills hold cut rules for picking moments, font pairing guidance, and B-roll generation. Sub-processes handle music, voiceover, sound and photo animation. ([6:06](https://youtu.be/pPj_tjlvYjA?t=366))
- **Use a code-based render target so agents can write the output.** — Remotion treats video as React code, and agents are good at writing code. The composition is a file that lists assets, tracks and their order. ([7:18](https://youtu.be/pPj_tjlvYjA?t=438))
- **Add a verification layer that the agent must pass before delivery.** — The layer checks that the composition is clean, well-defined and renders. If not, the agent reiterates on the composition. ([7:18](https://youtu.be/pPj_tjlvYjA?t=438))
- **Hide the agent workflow behind consumer UX.** — Mobile-first use, directional templates (speak-to-camera, B-roll, voiceover) that work with no prompt, and a manual timeline editor for small fixes like removing a second or correcting a caption word. ([8:33](https://youtu.be/pPj_tjlvYjA?t=513))

## Techniques
- **Sandbox per approved job** — Spin up a remote machine with the agent, its skills and tools only after the user approves the plan. The sandbox does the composition and rendering work. *When:* Multi-step agent jobs where execution is expensive and the user should steer the direction first.
- **Plan approval gate** — Generate a creative plan from media understanding. Let the user approve, edit or regenerate it before any execution starts. *When:* Creative or generative pipelines where a wrong direction wastes compute or user trust.
- **Skills as encoded craft** — Package domain taste as skills: cut rules, font pairings, B-roll generation rules. The agent loads them in the sandbox. *When:* Domains where quality depends on expert judgment rather than a single API call.
- **Code-defined render target** — Express the output as code (Remotion React compositions) so the agent writes it and the renderer compiles it. *When:* Agent output that must be rendered or built deterministically from assets.
- **Verification-then-reiterate loop** — Before delivery, check the composition is valid and renders. On failure, return the error to the agent to fix and retry. *When:* Any agent-written artifact that can fail to build or render.
- **Directional templates plus manual editor fallback** — Offer preset editing modes so users need no prompt. Let them fix small issues in a conventional timeline editor after the agent pass. *When:* Consumer products where prompting is a barrier and agent output needs small corrections.

## Hot takes
- Editing real footage is a harder agent problem than generating from a blank canvas.
- Consumer users should not need to know that a complex agentic workflow runs behind the app.

## Tools mentioned
Remotion, React

## Relevance to our work
- **prosharness** (2/3): Plan approval before sandbox execution maps to ProsHarness's plan step and phone-driven approvals. → *Add an explicit user approval gate after the plan stage and before the first costly execution step, reusing the phone-driven approval flow.*
- **agentos** (1/3): Sandboxed render jobs with an error-feedback verification loop match the Crucible exec-gate pattern, but the talk gives no metrics or code. → *In Crucible, test one job type where the agent output must compile or render, and feed the build error back to the agent for a retry; consider SkillForge output as per-domain skill files.*

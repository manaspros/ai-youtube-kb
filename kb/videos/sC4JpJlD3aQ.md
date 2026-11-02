# I Didn't Expect This From OpenAI's IDE

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `sC4JpJlD3aQ` · [watch](https://youtu.be/sC4JpJlD3aQ) · **date:** 2026-03-02 · **length:** 7:36 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** OpenAI, Tripo 3D, Canva, Aceternity UI
- **topics:** coding-agents, multi-agent, vibe-coding-app-building, skills-self-improvement · **tags:** codex, tripo-3d, image-to-3d, glb, nextjs, gsap, aceternity-ui, react-three-fiber, git-worktrees, subagents, skill-creator, landing-page

> A 7-minute build log: turning a car photo into a 3D hero section for a Next.js landing page with Tripo 3D, OpenAI's Codex app, GSAP and Aceternity UI, with parallel Codex subagents in git worktrees.

## Summary
The speaker builds a landing page with a 3D car in the hero section. They remove the photo background (Canva's remover, with a free alternative mentioned), generate a 3D model in Tripo 3D, and export it as GLB because it bundles textures and materials in one web-native file. They then build the site in the Codex app (macOS only), which has a built-in skill creator. Codex generates a skill for the 3D animation, but the install step times out in the agent environment, so dependencies are written to package.json and fixed locally after version mismatches. The page is split into four isolated feature tasks run by parallel Codex agents in separate git worktrees, then merged without conflicts. The speaker installs GSAP by hand, asks Codex to add scroll-triggered animations while leaving the hero untouched, swaps in Aceternity UI components, and corrects off-theme gradients and missing hover effects with screenshots and follow-up prompts. A post-processing layer adds a glow to the model after several retries. This is a practical, honest walkthrough with little reusable code, and the Codex free-quota pitch is promotional.

## Key ideas
- **Remove the photo background before image-to-3D generation** — The speaker says background/foreground separation is hard for image-to-3D tools and a bad generation wastes credits, so the background was stripped first (Canva's background remover, with a free alternative mentioned). ([0:00](https://youtu.be/sC4JpJlD3aQ?t=0))
- **Export the 3D model as GLB** — GLB keeps textures and materials in one file and is a native web format that works easily with web libraries. The model was exported at 4K after picking the better of two generations. ([1:14](https://youtu.be/sC4JpJlD3aQ?t=74))
- **Codex ships a built-in skill creator** — Unlike other agents, where you install an open-source skill creator, Codex had one plus common ready-made skills. The speaker described the animation and libraries, answered its questions, and it generated a skill with scripts, references, assets and a YAML file of trigger prompts. ([2:38](https://youtu.be/sC4JpJlD3aQ?t=158))
- **Agent sandboxes can time out on installs** — Codex could not finish dependency installation because of a command timeout, so the speaker had it write the dependencies into package.json. Running the install locally then failed on library version mismatches, which took repeated debugging. ([2:38](https://youtu.be/sC4JpJlD3aQ?t=158))
- **Split work into isolated subtasks run by parallel agents in worktrees** — A slow single Codex run was broken into four feature tasks, each with objectives, requirements and constraints. Each agent worked in its own git worktree to avoid conflicts on the same landing page. The outputs were merged cleanly and the work was faster. ([4:05](https://youtu.be/sC4JpJlD3aQ?t=245))
- **Install the animation library yourself and fence off finished work** — GSAP was installed by hand in the terminal to avoid the agent's install timeout. The prompt told Codex not to touch the hero section, which was already working, and it added scroll-triggered animations to the other sections. ([4:54](https://youtu.be/sC4JpJlD3aQ?t=294))
- **Fix visual regressions with screenshots and name the exact behavior you want** — Aceternity components came in with off-theme gradients, which were fixed by sending a screenshot. They were also static, so the speaker asked for the variants with built-in hover-tilt micro-interactions. ([4:54](https://youtu.be/sC4JpJlD3aQ?t=294))
- **Post-processing effects can need several prompt rounds** — A post-processing package for React Three Fiber (called 'Post Processing' in the transcript) was used for gamma correction and a subtle glow. The first attempt had no visible effect, and the speaker repeated the prompt until the glow appeared on the 3D model. ([6:18](https://youtu.be/sC4JpJlD3aQ?t=378))

## Techniques
- **Pre-clean the image for image-to-3D** — Remove the subject's background (Canva background remover, or a free alternative) before uploading to Tripo 3D as the reference image. Check the model from all angles, generate once or twice, and export only the best one (the free plan allows 15 exports). *When:* Generating a 3D asset from a photo with a busy background, when credits or export quotas are limited.
- **GLB asset in a Next.js public folder** — Export the model as GLB (textures and materials in one file). Create a fresh Next.js app and place the .glb in public/ so it can be loaded by URL. *When:* Shipping a 3D model on a web page where one self-contained, web-native file is easiest to load.
- **Generate a project skill with the agent's skill creator** — In Codex, describe the behavior, the libraries to use, and any constraints. Answer its questions and let it run its skill-creator scripts. Expect the output in a scripts/, references/ and assets/ layout with a YAML file of trigger prompts. Move it into the agent's expected folder (here .agent/, since Codex put it in the root). *When:* Capturing a repeatable procedure, such as building a particular 3D animation, as a skill the agent can invoke later.
- **Work around agent install timeouts** — If the agent's environment times out on an install, have it write the dependencies into package.json, then run the install yourself and fix version mismatches by iterating on the errors with the agent. *When:* Agent sandboxes that time out on npm install, leaving the dependency list unresolved.
- **Parallel subagents in separate git worktrees** — Split the feature into independent tasks. Give each one objectives, requirements and constraints. Run each agent in its own git worktree, not the main branch. Merge the outputs afterward. The speaker used Codex's multi-agent feature with four tasks. *When:* Many independent features that touch the same codebase and would otherwise conflict or run slowly on one agent.
- **Scope the agent with explicit do-not-touch constraints** — In the prompt, name the section that is finished and forbid changes to it (here, the hero section). Specify where and how to add the new behavior (for example, scroll-triggered GSAP animations). Feed error messages back verbatim. *When:* Adding a layer, such as animation, to a page where part of the UI is already correct.
- **Fix visual drift with screenshots and named variants** — When the agent's output breaks the theme (such as gradients), send a screenshot and say what is wrong. When components are static, ask for the library's specific variant (for example, hover-tilt) by name. *When:* Swapping in a component library whose default look or interaction does not match the app.

## Numbers
- About 300 Tripo credits on sign-in, described as enough for around 10 generations ([0:00](https://youtu.be/sC4JpJlD3aQ?t=0))
- Model generation took about 1 minute ([1:14](https://youtu.be/sC4JpJlD3aQ?t=74))
- Tripo free plan allows 15 exports; the speaker generated two attempts and exported one at 4K ([1:14](https://youtu.be/sC4JpJlD3aQ?t=74))
- Work split into four parallel subtasks; the speaker says the merged result was significantly faster than Codex alone, with no timing given ([4:05](https://youtu.be/sC4JpJlD3aQ?t=245))

## Hot takes
- The speaker says Codex's built-in skill creator sets it apart from other agents, which need an open-source skill creator installed separately.
- The Codex free-plan quota is pitched as a reason to use it now ('the best time'). That is a time-limited vendor promotion, not a lasting capability.
- Parallel worktree subtasks are presented as the fix for slow single-agent runs, but the speaker gives no timing comparison.
- The opening includes a plug for the channel's paid community (AI LABS Pro). It is self-promotion, not a sponsor segment.

## Tools mentioned
Codex app (OpenAI), Tripo 3D, Canva background remover, Next.js, GSAP, Aceternity UI, React Three Fiber, post-processing package for React Three Fiber (named 'Post Processing' in the transcript), npm, GLB (file format), Antigravity (agent manager, compared in passing), Claude Code (mentioned as the previous agent used)

## Relevance to our work
- **prosharness** (1/3): Sketches a multi-agent pattern (scoped subtasks with objectives, requirements and constraints, run in separate git worktrees, then merged) that ProsHarness's Claude Code harness could use for long runs. Same sandbox install-timeout issue applies. → *Check how ProsHarness fans out work: give each subtask its own git worktree plus an explicit objectives/requirements/constraints block, then merge. Also make sure dependency installs are run outside the agent sandbox.*

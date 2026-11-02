# Why Smart Developers Use Kimi For Design

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `zx9xhp7wB9M` · [watch](https://youtu.be/zx9xhp7wB9M) · **date:** 2026-10-02 · **length:** 6:37 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Claude, OpenAI, Google, Design Arena
- **topics:** vibe-coding-app-building, models-research · **tags:** design-generation, model-comparison, kimi, claude, astra, frontend-design, 3d-modelling, game-dev, component-library, cost, model-routing

> Better Stack runs one informal side-by-side test of Kimi, Claude and an OpenAI model (Astra) across five design and game tasks, finds each model wins different rounds, and spends $6 on Kimi.

## Summary
The speaker tests a claim that Kimi sits at the top of Design Arena, comparing Kimi against Claude and an OpenAI model (named Astra in the transcript) on five prompts: a landing page, a 3D floating island, a component library, a mobile app, and a jumping robot game with generated assets. Each round is judged by eye, with a point awarded to the winner, a point to everyone on a tie, and no points when all results are poor. Kimi wins the landing page, Astra wins the 3D scene, the component libraries are scored as a three-way tie, the mobile app earns no points, and Claude wins the game. The speaker's conclusion is that no model dominates, that each has domain strengths (Kimi for web design, Claude for interactive demos and games, OpenAI for 3D), and that the best results may come from switching models per task. The only cost figure given is $6 for all five Kimi demos; the Astra and Fable runs were on a subscription, so their cost is unknown. The evidence is a single run per model with no prompts, seeds or rubric shown, and the final winner is never stated.

## Key ideas
- **Test of a 'Kimi tops Design Arena' claim using five prompts: landing page, 3D island, component library, mobile app and a game with generated assets.** — Each model gets the same brief per round, and the speaker scores them by eye. The Design Arena ranking itself is not checked in the video. ([0:00](https://youtu.be/zx9xhp7wB9M?t=0))
- **Landing page for a Postgres job queue: Kimi wins the round.** — Claude gets credit for an animated queue graphic but a odd font choice. OpenAI's version has better typography but static, weaker graphics. Kimi is judged most balanced and close to deployable, with an npm install block and a call to action. ([0:00](https://youtu.be/zx9xhp7wB9M?t=0))
- **3D floating island with a day/night cycle: Astra (OpenAI) wins, Kimi is worst.** — Claude's trees are blocky and the waterfall clips. Astra's composition and softer day/night lighting are judged best, though its waterfall also clips. Kimi's model is the blockiest and has the worst clipping, so the speaker says Kimi does not hold up for 3D. ([2:28](https://youtu.be/zx9xhp7wB9M?t=148))
- **Component libraries (Cairn from Claude, Forma from OpenAI, Meridian from Kimi) are scored as a three-way tie.** — The speaker says the buttons, inputs, focus states, checkboxes and radios all look good and that taste would decide. Each lab gets one point. ([3:39](https://youtu.be/zx9xhp7wB9M?t=219))
- **Mobile coffee-rating app: every model is generic, so no points are awarded.** — The speaker says a one-shot prompt is unlikely to produce a good mobile design and that it probably needs many refinement prompts. OpenAI and Kimi are described as similarly blocky, and Claude's is called very ugly. ([3:39](https://youtu.be/zx9xhp7wB9M?t=219))
- **Robot jumping game with generated assets: Claude wins, OpenAI's walk animation runs backwards.** — Claude's version has a blinking eye, a walk cycle, flame and smoke effects. OpenAI's flame is basic and its walk animation moves the wrong way. Kimi is in the middle, with feet moving the right way and an eye that follows the mouse. ([5:00](https://youtu.be/zx9xhp7wB9M?t=300))
- **The speaker's takeaway is to switch models per task, not pick one.** — Kimi is strongest at web design, Claude at interactive demos and games, and OpenAI at 3D. Counting the points in the video, each lab ends with two points (Kimi: landing page and components; Astra: 3D and components; Claude: game and components). The speaker never states an overall winner. ([6:12](https://youtu.be/zx9xhp7wB9M?t=372))
- **The only cost datapoint: Kimi ran all five demos for $6, while the Astra and Fable runs used a subscription, so their cost is unknown.** — The speaker's cost claim is a single run on one account, so it is not a benchmark of cost per task. ([6:12](https://youtu.be/zx9xhp7wB9M?t=372))

## Techniques
- **Same-brief, side-by-side model bake-off** — Send one identical brief to each candidate model for each task type (landing page, 3D scene, component library, mobile UI, game with assets). Render or run each output, then judge them against one another in rounds. *When:* Before committing a design or UI workflow to one model. It is a cheap way to find which model suits which kind of task.
- **Per-task model routing** — Pick a model per task type based on the bake-off results: Kimi for landing pages and web design, Claude for interactive demos and games, OpenAI for 3D scenes. Switch between providers instead of using one for everything. *When:* When your tool or gateway can route requests by task type. The speaker's routing choice rests on one set of demos, so verify it on your own tasks.
- **Round scoring with a tie rule** — Award a point to the best output in each round, a point to every output on a tie, and no points when all are poor. Total the points at the end, so a poor round does not force a winner. *When:* When judging generated outputs by eye and you want a simple, explicit outcome per round.
- **Visual checks for generated 3D and animation output** — Toggle scene states (for example day and night) and look for clipping, blocky geometry, lighting harshness, and animation direction problems such as feet moving backwards or effects running off screen. *When:* When you judge generated 3D scenes, sprites or animations. These checks catch the failures the speaker found, which a static screenshot would miss.
- **Plan for iterative refinement on generic UI** — For broad UI requests such as a mobile app, expect generic one-shot output and budget several refinement prompts instead of a single generation. *When:* When the first output is generic and a single prompt is unlikely to reach a production-quality design.

## Numbers
- Five demos in the comparison: web design, 3D modelling, UI components, mobile app design and game dev. ([0:00](https://youtu.be/zx9xhp7wB9M?t=0))
- Kimi cost $6 to run all five demos. Astra and Fable were run through a subscription, so their cost is not known. ([6:12](https://youtu.be/zx9xhp7wB9M?t=372))
- Points tally from the video's round results, counted by me, not stated by the speaker: Kimi 2, Astra 2, Claude 2, mobile app round 0. ([6:12](https://youtu.be/zx9xhp7wB9M?t=372))

## Hot takes
- The title ('Why Smart Developers Use Kimi For Design') and the Design Arena framing overstate the result. Kimi wins one round outright and loses the 3D round, and the speaker never names an overall winner.
- The method is one run per model, judged by eye, with no prompts, seeds or rubric shown, so the round results are anecdotal.
- The speaker says a one-shot mobile app is unlikely to be good enough and needs many refinement prompts, which undercuts the 'production ready with a little steering' claim at the start.
- The only cost figure is for Kimi, and the other two runs were on a subscription, so no cost comparison is possible.

## Tools mentioned
Kimi (Kimi K3 mentioned as a separate follow-up video), Claude, Astra (OpenAI model, as named in the transcript), Fable, Design Arena (leaderboard the speaker cites), Postgres (the product in the landing-page demo), npm (install block shown on the landing page)

## Relevance to our work
- **agentos** (1/3): Per-task model choice is loosely related to the strategy routing in the Rust proxy. This video offers only anecdotal evidence and one cheap-run cost figure. → *If routing rules are ever set per task type, use a small same-brief bake-off like this to choose candidate models, and measure it with our own evals rather than trusting this video.*

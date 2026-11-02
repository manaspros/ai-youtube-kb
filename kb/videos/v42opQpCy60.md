# Design at the Speed of Adjectives — Paul Bakaus, Renaissance Geek, Inc.

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `v42opQpCy60` · [watch](https://youtu.be/v42opQpCy60) · **date:** 2026-09-18 · **length:** 15:59 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Paul Bakaus · **orgs:** Renaissance Geek, Inc.
- **topics:** vibe-coding-app-building, product-ux, coding-agents, context-engineering · **tags:** design, impeccable, skills, adjectives-as-commands, human-in-the-loop, frontend, taste, workflow-mapping

> Paul Bakaus on steering coding agents toward good design with a skill (Impeccable) that maps vague design adjectives like "bolder" to project-specific meanings, keeping humans in the loop instead of one-shotting.

## Summary
Paul Bakaus presents Impeccable, a design skill that works across coding harnesses (Claude Code, Copilot, Cursor, Codex) and turns the agent into a more careful designer. He argues that design and engineering roles are blurring and that the old handoff process is breaking down. He says direct manipulation (Figma-style pixel work) is too low-level, while fully agentic prompting produces generic "slop" that is a moving target, and he calls the middle ground the missing control level. His core claim is that design cannot be one-shotted: it needs context, audience and emotional territory, and several rounds of iteration. The tool gives the agent a shared vocabulary of verbs and adjectives (bolder, quieter, distill, harden, polish, overdrive), each defined in a loaded file in terms of the project's design system (hierarchy, scale, decisive type) rather than generic tricks like gradients. He maps the design workflow into stages (shaping, crafting, iterating, hardening, polishing, cleanup) and places the commands at injection points. He says he will not build an automatic mode, and ends with the view that taste can be amplified but not lab-grown.

## Key ideas
- **Design sits between two bad extremes: pixel-level manipulation is too low a level of control, and fully agentic one-prompt generation gives generic output. The useful control level is in between.** — Paul says direct manipulation of padding and margins is too low for most work. Pure agentic prompting yields bland, same-looking pages, which he calls 'Claude Beige' and 'algorithmic Uniqlo'. He says the missing piece is the right level of control, and where to put the human in the loop. ([4:42](https://youtu.be/v42opQpCy60?t=282))
- **You cannot one-shot design. Good design needs context (audience, goal, emotional territory, what it should never feel like) and multiple rounds of iteration.** — He lists the questions to answer first: what is the emotional territory, what should this never feel like, what is the reference, who is the audience. A design director would not accept a brief with none of these. Stakeholders and users also add opinions, so design is messy and iterative. ([6:38](https://youtu.be/v42opQpCy60?t=398))
- **Adjectives like 'bolder' are compressed instructions. The skill defines what they mean in the project's design system so the agent does not invent its own meaning.** — Without a definition, 'make it bolder' makes the model invent colors or gradients. The loaded file defines bolder as hierarchy, scale and decisive type, which keeps the design system intact. A test in the file: if you show someone your work and say you made it bolder and they believe you, you failed. ([10:12](https://youtu.be/v42opQpCy60?t=612))
- **An adjective with nothing behind it is just a nicer prompt. Verbs and adjectives only steer the agent once they are tied to explicit meaning.** — Words like bolder have many meanings in training data, so the team has to spell out what they mean in the context. He explicitly rejects a fully automatic mode, arguing the point is steering toward a result the user wants, not one-shotting design. ([13:42](https://youtu.be/v42opQpCy60?t=822))
- **Map the real workflow first, then place the tools at the injection points. Design is non-linear, has several stages and several people, and the commands are attached to those stages.** — His stages are initialization and shaping, crafting and iterating, hardening and polishing, then bringing the work back into the design system with cleanup. Each stage gets its own set of verbs and adjectives. ([11:43](https://youtu.be/v42opQpCy60?t=703))
- **Ship experimental commands and let the community decide. He shipped 'overdrive' as a half-joke, kept it because people embraced it, and uses it to push visuals further.** — The overdrive command produced an over-the-top shader in his own library, which he says was not one-shotted. He keeps unsure commands in circulation and keeps the ones that stick with users. ([12:42](https://youtu.be/v42opQpCy60?t=762))

## Techniques
- **Project-defined verb and adjective commands** — Create named commands (bolder, quieter, distill, polish, harden) and attach a file with the project-specific meaning of each, loaded when the command is invoked. Define the meaning in terms of the project's own system (hierarchy, scale, type), and say what it must not do. *When:* When you repeatedly steer a coding agent with vague design or quality words and get inconsistent results across runs or people.
- **Self-check against a stated failure test** — Put a concrete test in the instructions, such as 'show someone your work and say you did this; if they believe you, you failed'. The agent is then asked to check its own output against it and often flags its own weak work. *When:* When the agent tends to claim success on subjective or hard-to-verify output.
- **Pre-brief questions before generation** — Before generating, have the agent or the human answer the questions: emotional territory, what it should never feel like, reference, audience. Use the answers as context for every later step. *When:* At the start of any UI or design task where the agent would otherwise fill the gaps with defaults.
- **Workflow-stage command mapping** — Write the target user's full workflow as stages, then attach a command or tool to each stage instead of one general prompt. Stages in his case: shape, craft, iterate, harden, polish, clean up. *When:* When building a skill or tool for a multi-stage process that several people touch, and a single prompt does not cover it.
- **Community-tested experimental commands** — Ship a command you are unsure about, watch how people use it, and keep it if it sticks. *When:* When extending a skill library and you cannot predict which commands users will value.

## Numbers
- Comparison demo: same project, same prompt (make the workflow section bolder), GPT 5.5 extra high, with and without Impeccable. He says the difference is slight and leaves the judgment to the audience. ([1:09](https://youtu.be/v42opQpCy60?t=69))
- He has built tools for more than 20 years. ([11:43](https://youtu.be/v42opQpCy60?t=703))
- AI can't yet replace humans for the last 5 to 20 percent of work to get from good to great, by his estimate. ([11:43](https://youtu.be/v42opQpCy60?t=703))
- Users ask for an automatic mode at least once a week; he refuses it. ([13:42](https://youtu.be/v42opQpCy60?t=822))
- Talk length is 15:59. ([0:08](https://youtu.be/v42opQpCy60?t=8))

## Hot takes
- You cannot one-shot design, and maybe never will. [6:38]
- Taste can be amplified but cannot be lab-grown; it is contextual and cultural. [14:47]
- There is no auto mode, and there never will be. [13:42]
- Pure agentic design now produces the same look everywhere ('Claude Beige'), so it is slop even without the purple gradients. [5:39]
- The role of designer and engineer is blurring, and the waterfall handoff is collapsing. [2:42]

## Tools mentioned
Impeccable, Claude Code, GitHub Copilot, Cursor, Codex, Figma, Webflow, Claude Design, Radiant Shaders

## Relevance to our work
- **general** (2/3): Useful context-engineering pattern: vague instruction words need project-specific definitions and a self-check test. This applies to CLAUDE.md and skill files in general. → *Audit CLAUDE.md and skill files for vague directives (for example 'be careful' or 'clean this up') and replace each with a definition plus a pass/fail test the agent can check against.*
- **prosharness** (1/3): The talk's idea of named, project-defined commands with explicit meanings is close to how ProsHarness steers Claude Code runs, but the talk does not cover checkpointing, critique or approvals. → *When adding a new ProsHarness command or phase, write its meaning in a project file the agent loads, so the agent does not improvise its own interpretation.*

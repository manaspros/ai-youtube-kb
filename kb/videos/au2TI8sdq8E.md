# Google Just Fixed AI Design By Releasing This

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `au2TI8sdq8E` · [watch](https://youtu.be/au2TI8sdq8E) · **date:** 2026-10-19 · **length:** 13:47 · **format:** tutorial · **quality:** 3/5 · **depth:** practitioner
- **speakers:** AI LABS host · **orgs:** Google, AI LABS, Whisperflow
- **topics:** coding-agents, context-engineering, skills-self-improvement, testing-verification · **tags:** stitch, google-stitch, design-md, claude-code-skills, visual-review, scrollytelling, brief-md, design-to-code, mcp-vs-cli

> Google's Stitch design tool now has a terminal CLI, so Claude Code can drive it through a brief-to-design-to-site workflow with review and story-review skills; the video is a tutorial-style walkthrough with a sponsor segment.

## Summary
The speaker (AI LABS) shows how Claude Code can use Google's new Stitch CLI to produce a website design. Setup is installing the Stitch CLI, logging in, and installing the Stitch skill plus a scrollytelling skill into the project's .claude folder. Claude then interviews the user to write brief.md, prompts Stitch for several design versions (8 in their case), and downloads the chosen designs as webpages with images and fonts to build the site. A Stitch review skill then compares the built site against the design and takes screenshots at several screen sizes, because the first build broke on phones. Finally a story-review skill judges pacing, animation count and copy against brief.md, and the team fixes the findings it ranks worst first. The CLI is pitched as cheaper in tokens than an MCP server because tools load only when needed. Quality is a tutorial with reasonable process detail but no measured results.

## Key ideas
- **Stitch now ships a CLI, which lets agents use it without the Google Cloud setup the MCP needed.** — The speaker says the CLI loads only when needed, unlike MCP, which stays in context, so it uses fewer tokens. This is the speaker's claim, with no measurement shown. ([1:19](https://youtu.be/au2TI8sdq8E?t=79))
- **Skills must be installed into the .claude folder, or Claude will not load them.** — The install command places the Stitch skill in a different folder unless .claude is named explicitly. Once it is in .claude, the skill's guides cover design.md and a design-word list. ([2:43](https://youtu.be/au2TI8sdq8E?t=163))
- **Write the site idea into brief.md before prompting any designs.** — Claude interviews the user until it has no questions left, offering options for each one, then writes brief.md with a summary and a step-by-step story. Every Stitch prompt is built from this file, which keeps the designs consistent since Stitch's style shifts between generations. ([5:26](https://youtu.be/au2TI8sdq8E?t=326))
- **Claude prompts Stitch in a loop: it generates several versions, checks each one, and re-prompts when it finds a problem.** — The run produced 8 versions. The Stitch designs are static images with no scroll animation, which the speaker says is deliberate because motion is added later in Claude Code. ([6:46](https://youtu.be/au2TI8sdq8E?t=406))
- **A design review is needed because the built site looked fine on desktop but broke on phones.** — Stitch designed for a desktop screen only. The team had Claude create a review skill that compares the site against the Stitch design and screenshots several screen sizes. It produces a report sorted worst first, and the team asked Claude to fix the issues. ([9:25](https://youtu.be/au2TI8sdq8E?t=565))
- **A separate story-review skill checks whether the animated site is good, not just whether it matches the design.** — It checks story flow, whether each animation serves the story, scroll speed and copy quality, judged against brief.md with a demand to reach award-site standard. The stars effect was too busy at fast scroll and was cut back. The review found the stars too heavy and the team cut them back. ([11:55](https://youtu.be/au2TI8sdq8E?t=715))
- **Animation effects were added with the scrollytelling skill, including sideways horizontal movement in one section.** — Effects shown are a start-up shake, streaking stars while scrolling, a chapter marker and a horizontal timeline inside a vertically scrolling page. The speaker notes that responsive review earlier meant these also worked at phone and tablet sizes. ([10:52](https://youtu.be/au2TI8sdq8E?t=652))

## Techniques
- **Stitch CLI install with the skill in .claude** — Install the Stitch CLI with the command from the Stitch site, run its login command (browser Google sign-in), then run the Stitch skill install command and make sure the target is the project's .claude folder. The scrollytelling skill goes into the same .claude folder. Exact commands are not shown in the transcript. *When:* Before building any design-driven site with Claude Code. Use the CLI rather than the MCP when setup cost or context tokens matter.
- **brief.md interview before any design generation** — Ask Claude to interview you about the site and keep asking until it has nothing left to ask, offering a few options per question. Have it write brief.md with a short summary and then the story step by step, plus every other detail that shapes the site. Use brief.md as the single source for every Stitch prompt. *When:* Whenever several generated designs must share one story and voice, since the generator's style drifts between outputs.
- **Loop of generate, check, and re-prompt in Stitch** — Ask Claude to prompt Stitch from brief.md and request several design variants. Claude creates a Stitch project, sends the brief as the description, requests versions, checks each one, and re-prompts when it finds a problem. Preview each in Stitch on desktop and phone views. *When:* For the design phase, when you want several candidates to choose from and expect a slow run.
- **Build from Stitch via download of HTML, images and fonts** — Ask Claude Code to build the chosen design into the project. The Stitch tool hands over each design as a webpage plus a screenshot, and Claude downloads the design with its images and fonts before building the site. *When:* After design selection, to turn the Stitch output into real project files.
- **Two-stage review: design fidelity, then story quality** — Stage 1 is a Stitch review skill: compare the built site with the Stitch design and take screenshots at several screen sizes, then report problems worst first. Reference the skill in CLAUDE.md so the review knows the project. Stage 2 is a story-review skill: judge story flow, whether each animation serves the story, scroll speed and copy against brief.md, with a sorted problem list. Fix in order from the top of each report. *When:* Run stage 1 right after the static build, before adding motion, and stage 2 after animations, since agents tend to over-animate.

## Numbers
- Stitch's CLI loads tools only when needed, which the speaker says uses fewer tokens than an MCP that stays in context. ([1:19](https://youtu.be/au2TI8sdq8E?t=79))
- The design run produced 8 Stitch versions. ([6:46](https://youtu.be/au2TI8sdq8E?t=406))

## Hot takes
- A CLI is cheaper than MCP in tokens because MCP servers stay in context, which the speaker asserts without a measured comparison.
- Agents over-add animations, and the speaker says too many are hard on the eyes, so a separate story-review pass is needed.
- The Stitch-to-code path is judged a review problem, not a generation problem: the desktop-only design needs phone verification.
- Sponsor segment for Whisperflow (about 1 minute) and the video links to a paid community.

## Tools mentioned
Stitch (Google), Stitch CLI, Claude Code, Stitch skill, scrollytelling skill, design.md, brief.md, Whisperflow (sponsor)

## Relevance to our work
- **prosharness** (1/3): The brief-first interview, the generate-check-reprompt loop, and the two-stage review are general patterns that could fit ProsHarness plan and critique steps. → *Consider whether a brief.md-style spec interview before long runs fits ProsHarness plan stage; compare with its plan, critique and debate flow.*

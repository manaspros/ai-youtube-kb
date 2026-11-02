# Perception Agents — Antje Barth, Amazon AGI Lab

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `2JX6JYyQG4Y` · [watch](https://youtu.be/2JX6JYyQG4Y) · **date:** 2026-08-18 · **length:** 21:45 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Antje Barth · **orgs:** Amazon AGI Lab, Amazon
- **topics:** voice-multimodal, testing-verification, coding-agents · **tags:** computer-use, perception-agents, verification, shared-context, annotation, design-review, browser-agents, open-source, reliability

> Amazon AGI Lab's Antje Barth argues computer-use agents need shared screen context and self-verification, then demos open-source annotation and design-spec checking tools for UI work.

## Summary
Antje Barth of Amazon AGI Lab says agents can now click and drive browsers, but end-to-end knowledge work that spans several apps still fails, and a 60 to 80 percent success rate is not trustworthy. She contrasts coding, which became reliable because code can be run and tested, with messy knowledge work that has no unit test. Her proposed fix is a "perception agent" that works from the rendered screen in a perceive, plan, act loop, and that reacts while the human works instead of waiting for turn-based prompts. She gives three reasons for it: it can check its own output, it needs no API, and pointing at a UI is a less lossy input than long text. The team has open-sourced two pieces, an annotation Chrome extension and a verification tool that checks the UI against a design-rules file and walks user flows. In a short live experiment, a meeting transcript from a wearable device was turned into a summary, sent to the agent with one click, and checked automatically against the design rules. The talk is early-stage framing with a demo and an open call for feedback, not benchmark results.

## Key ideas
- **Clicking and tool calls are largely solved, but real work spans the seams between apps** — Her example is onboarding a new hire across about five systems (accounts, Slack, intros, laptop). Each step is doable alone, but no single agent step covers the whole job. ([0:08](https://youtu.be/2JX6JYyQG4Y?t=8))
- **Reliability, not capability, is now the bottleneck** — She says end-to-end success of 60 to 80 percent sounds fine but is not enough, since one failure in four (such as deleting a database) ends trust. She says the bar is 'in the nines'. ([2:38](https://youtu.be/2JX6JYyQG4Y?t=158))
- **Coding became trustworthy because code is verifiable** — Code can be run, tested and checked. Most knowledge work (did the report land, is the design on brand) has no unit test, so verification hits a wall exactly where much of the work lives. ([4:15](https://youtu.be/2JX6JYyQG4Y?t=255))
- **Humans handle messy work through shared context, not a bigger brain** — Two colleagues looking at the same screen solve a problem in minutes. She argues the agent is missing that shared view more than raw intelligence. ([7:34](https://youtu.be/2JX6JYyQG4Y?t=454))
- **Proposed loop is perceive, plan, act, borrowed from robotics, but on the rendered screen** — The agent should read what is actually rendered (layout, state, what just changed), not scrape the code behind the page. ([9:08](https://youtu.be/2JX6JYyQG4Y?t=548))
- **Current agents are turn-based and should become reactive** — Today's flow is prompt, wait, review, re-prompt. She wants an agent that comments and helps while the user is still working. ([10:09](https://youtu.be/2JX6JYyQG4Y?t=609))
- **Three reasons for perception agents** — They close the loop by checking their own output, they need no API or backend access because they work on pixels and structure, and pointing at a UI is a more precise, less lossy input than a long text description. ([11:11](https://youtu.be/2JX6JYyQG4Y?t=671))
- **Verification is a separate, open-sourced piece** — Design rules (colors, components, layout) go into a design file. The agent turns them into checks, runs a visual check and a user-flow walkthrough, and writes a report of passes and failures. The human then decides whether to fix the output or change the rules. ([15:54](https://youtu.be/2JX6JYyQG4Y?t=954))
- **A meeting transcript can feed the agent directly** — In a live test, a wearable transcription device captured a design discussion, a summary and insights were produced, one Apply button sent them to the agent, and verification started at once. The approved color scheme passed, and the report would have flagged violations otherwise. ([17:24](https://youtu.be/2JX6JYyQG4Y?t=1044))

## Techniques
- **Element pointing as agent input** — A Chrome extension lets the user hover and select an element on a live page, then add a note such as 'double the font size'. The tool records the element's location, style and the feedback, and produces a summary the coding agent can act on. *When:* UI change requests on a running web app, where describing the change in prose is long and lossy.
- **Design-rules verification from a spec file** — Write colors, components and layout rules in a design markdown file. The agent turns them into checks, runs a visual pass, walks user flows (add or delete a task, like a real user), and writes a pass/fail report for human review. *When:* UI work with no unit tests, where brand or layout drift must be caught before a human clicks through the app.
- **Meeting transcript to agent to verification pipeline** — Capture a live design discussion with a wearable transcriber, generate a structured summary and insight list, push the chosen items to the agent with one action, then run verification automatically against the design rules. *When:* Design reviews where decisions should turn into code changes without retyping them.
- **Perceive, plan, act, then re-check the screen** — The agent reads the rendered screen (not DOM or code), plans, acts, and re-reads the screen to confirm the result instead of firing actions and hoping they worked. *When:* Computer or browser automation where each step needs confirmation before the next one.

## Numbers
- Gut-check end-to-end success rate of agent workflows, estimated at 60 to 80 percent by the speaker ([2:38](https://youtu.be/2JX6JYyQG4Y?t=158))
- A one-in-four failure rate is described as unacceptable for trust, with the target 'in the nines' ([2:38](https://youtu.be/2JX6JYyQG4Y?t=158))
- Example onboarding workflow touches about five different systems ([1:34](https://youtu.be/2JX6JYyQG4Y?t=94))
- Two open-source pieces released: annotation and verification ([13:26](https://youtu.be/2JX6JYyQG4Y?t=806))

## Hot takes
- Coding got reliable first only because code is verifiable; most knowledge work has no unit test, and that is the wide-open frontier.
- A one-in-four failure rate on end-to-end workflows ends trust in an agent, even if each step works alone.
- The missing piece is shared context (both parties looking at the same screen), not a bigger model.
- Agents should react in real time while the human works, instead of the prompt, wait, review, re-prompt loop.

## Tools mentioned
Chrome extension (annotation tool), design rules markdown file (design.md), wearable transcription device, Amazon AGI Lab open-source perception agent harness (GitHub)

## Relevance to our work
- **prosharness** (1/3): A rules-file check the agent runs against its own output could work as a done-check for ProsHarness runs that touch a UI, though the talk gives no evidence it fits CLI-only work. → *Read the open-source verification piece and test whether a rules-file check on rendered output fits as a completion gate for UI-touching ProsHarness runs.*

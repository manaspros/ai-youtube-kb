# Build with Perception Agents — Emile Baizel & Shruti Arora, Amazon AGI Lab

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `ZGzthw4BZiA` · [watch](https://youtu.be/ZGzthw4BZiA) · **date:** 2026-10-12 · **length:** 55:43 · **format:** workshop · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Emil Baizel, Shruti Arora, Giovanni · **orgs:** Amazon AGI Lab, AWS, Amazon
- **topics:** voice-multimodal, testing-verification, coding-agents, mcp-and-tools · **tags:** perception-agents, computer-use, browser-agents, visual-verification, gherkin, nova-act, chrome-extension, visual-annotation, agent-bridge, design-feedback-loop, workshop, aws

> Amazon AGI Lab hands-on workshop on Nova Act's open-sourced perception primitives: point-and-annotate a live page into JSON, run Gherkin-based visual verification, and wire both to a coding agent.

## Summary
Emil Baizel (Amazon AGI Lab solutions lead) introduces the lab, which builds knowledge-work agents that perceive, reason and act on screens, and its shipped product Amazon Nova Act, a browser-automation AWS service with an MCP server and skill. Shruti Arora runs the hands-on part: a role-play where a front-end engineer gets design feedback and wants a coding agent to apply it and then verify the result. The two open-sourced primitives are a Chrome-extension visual annotator, which is deterministic and exports JSON plus a prompt, and a visual verification skill, which crawls the site once to generate Gherkin user flows and checks design specs in a browser. The workshop's solution requires an agent bridge: the extension needs a localhost host permission in manifest.json and an "apply changes" button injected into content.js so the annotations reach Claude Code or Kiro. Attendees then ran a timed challenge (15 minutes for the easy path, 30 to 35 for the medium one). Several audience members demoed extensions: a wearable voice-capture pipeline, a Jam MCP idea for feeding console and network logs into the loop, and a GTD-style capture inbox. The talk is mostly a product walkthrough, but the bridge and verification-loop mechanics are concrete.

## Key ideas
- **Reliability is the bar for agents** — A customer quote is used to argue that an agent that works 50% of the time does not work at all, because people either skip it or spend their time debugging it. The lab says it trains in simulated RL environments built from real knowledge-work use cases. ([2:58](https://youtu.be/ZGzthw4BZiA?t=178))
- **Perception is the missing half of computer use** — Computer use means acting on a screen. The speaker argues agents should also understand what is on screen the way a human would, and that they should work on screens with no API behind them. Feedback can then be given by pointing and describing a change instead of writing long descriptions of the screen. ([5:49](https://youtu.be/ZGzthw4BZiA?t=349))
- **Annotation capture is deterministic, not model-driven** — The visual annotator lets a person click, draw or pin on any web page, then exports a JSON file of the changes plus a prompt for a coding agent. The speaker stresses that this step does no inference and is not tied to any model. ([7:01](https://youtu.be/ZGzthw4BZiA?t=421))
- **Verification flows can be generated from a crawl** — On the first run, the verification tool does a one-level surface crawl of the site, then writes user flows in Gherkin syntax. It checks these flows and design specs (colors, font size, user flow) in a browser and produces a report. ([14:04](https://youtu.be/ZGzthw4BZiA?t=844))
- **The feedback loop is the product** — The speaker describes a design-review cycle that took about a week and may shrink to a few days. The aim is to send collected feedback straight to an agent, leave it running, and only step in to review the changes and the verification report. ([12:37](https://youtu.be/ZGzthw4BZiA?t=757))
- **An agent bridge is needed to connect the extension to the coding agent** — The extension has no built-in path to a coding agent. The workshop fix is two edits: a localhost host permission in manifest.json, and an apply-changes button plus a verification trigger injected into content.js. A bridge receives the request and opens the agent with the annotations. The speaker says it was tested with Claude Code and Kiro, and that Cursor or Codex would need the bridge changed. ([25:33](https://youtu.be/ZGzthw4BZiA?t=1533))
- **Run logs expose what the model saw and decided** — Nova Act logs show what the model was reasoning about and which part of the screen it was deciding on. After the change, the verification run starts automatically and writes a report to the repo. ([29:32](https://youtu.be/ZGzthw4BZiA?t=1772))
- **Non-keyboard input works as a source for the same loop** — A presenter feeds a wearable's transcript through a CLI, a bridge and the perception agent, so spoken design changes (title color, emoji) get applied to the page. The speaker says a live run was dropped because of slow Wi-Fi, and that a preloaded test account was used instead. ([32:53](https://youtu.be/ZGzthw4BZiA?t=1973))

## Techniques
- **Deterministic visual annotation to JSON** — Capture feedback on a live page (draw, pick an element, or drop a pin), export a JSON of changes plus a prompt, and hand both to a coding agent. No model runs in the capture step. *When:* Non-technical reviewers or designers need to give feedback on a running site without writing a long description, and you want the capture step to be repeatable.
- **Gherkin user flows auto-generated from a surface crawl** — On the first run, crawl the site one level deep, write the discovered links and content as Gherkin scenarios, then replay those scenarios in a browser and report the results. Design specs are checked alongside. *When:* You want visual or flow regression coverage on a site without hand-writing end-to-end tests, and the site can be crawled from its entry page.
- **Browser extension to coding agent bridge** — Add a localhost host permission to the extension manifest, inject an apply-changes button into the content script, and have a small local bridge pass the annotation JSON to the coding CLI and then trigger verification. *When:* A browser extension must trigger edits in a local coding agent, and you accept a local bridge that edits the agent's entry point.
- **Automatic verification after every agent change** — Chain the change step to a verification run, so the agent's edit is always followed by a browser replay and a report, and keep the logs that show the model's per-step decisions. *When:* You need proof that a coding agent's UI change actually works before a human reviews it.
- **Voice or wearable transcript as an annotation source** — Pull a conversation summary through a device CLI, pass the design-related utterances through a bridge, and apply the resulting changes through the same perception agent loop. *When:* Design decisions are made in meetings and should flow into the codebase without someone retyping them.

## Numbers
- Customer quote: an agent that works 50% of the time effectively does not work at all ([2:58](https://youtu.be/ZGzthw4BZiA?t=178))
- Nova Act has four primary adopted use cases: form filling, search and extract, shopping, and QA ([2:58](https://youtu.be/ZGzthw4BZiA?t=178))
- Speaker's rough estimate: a front-end build from design takes 4 to 5 weeks, and a review pass that took about a week may drop to a few days, or a few hours, with coding agents ([9:59](https://youtu.be/ZGzthw4BZiA?t=599))
- Setup for the workshop takes about 5 to 7 minutes ([21:22](https://youtu.be/ZGzthw4BZiA?t=1282))
- Challenge time budget: about 15 minutes for the easy path, 30 to 35 minutes for the medium path ([22:21](https://youtu.be/ZGzthw4BZiA?t=1341))
- Prizes: a device for each of the top three ideas, plus a crowd favorite; a device for a demo on stage ([17:01](https://youtu.be/ZGzthw4BZiA?t=1021))

## Hot takes
- Agents should understand a screen the way a human does, and should not be used as a blind surface to click on.
- The visual annotation step has nothing to do with inference; it is purely deterministic and only outputs JSON.
- Agents do not need APIs for knowledge work, because much of that work is done by humans on screens without APIs.

## Tools mentioned
Amazon Nova Act, Nova Act SDK, Nova Act MCP server, Visual Annotator (Chrome extension), Visual verification skill, Claude Code, Kiro, Gherkin, Chrome, uv / uvx, Jam MCP, Atlassian MCP, BCLI (wearable CLI)

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps Claude Code runs; the annotation-to-agent bridge and an automatic verification step after each change are the same pattern as a harness-driven loop. → *Read the open-sourced visual verification skill and compare its Gherkin-generation step against how ProsHarness decides a run is done.*
- **general** (1/3): Practical example of a deterministic capture step plus a model step, and of verification run logs that show per-step reasoning. → *Note the pattern: deterministic JSON capture of feedback, then a separate agent step, then a verification report, when designing review loops for coding agents.*

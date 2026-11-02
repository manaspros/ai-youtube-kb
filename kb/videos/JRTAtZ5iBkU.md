# HTML is All You Need (for Agents to Make Graphics) - Amol Kapoor, Nori

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `JRTAtZ5iBkU` · [watch](https://youtu.be/JRTAtZ5iBkU) · **date:** 2026-07-18 · **length:** 7:00 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Amol Kapoor · **orgs:** Nori Agentic (Nori)
- **topics:** product-ux, vibe-coding-app-building, coding-agents · **tags:** html-as-medium, agent-generated-slides, svg-vs-html, visual-artifacts, pelican-benchmark, render-to-pdf, nori

> Amol Kapoor (Nori) argues agents fail at graphics because of the medium, not the model, and that HTML is a better authoring format than canvas tools or SVG for slides, docs and video.

## Summary
Amol Kapoor, CEO of Nori Agentic, argues that coding agents can do far more than write code, and that agents look bad at visual work because they are given the wrong medium. Canvas tools like PowerPoint, Figma and Canva are built for human eyes and hands, and an agent working through them produces overlapping, misaligned output. He uses Simon Willison's pelican-on-a-bicycle SVG test as an example, and says SVG is a wall of coordinates that is hard for a model to reason about. HTML instead gives the model semantic structure (headings, grids, charts) that the browser turns into pixels, so the model never has to place coordinates. He says the editing format is arbitrary: you can author in HTML and render to PDF or another format later. Nori uses this approach for board decks, sales decks, docs and videos, and he presents it as a way to build decks from raw data such as call transcripts and emails. The talk is short and ends with a plug for the Nori product, so most of its value is the framing rather than measured results.

## Key ideas
- **Coding agents can do much more than write code, but you have to think like an agent to get them to do it.** — The speaker says calling them coding agents is weak marketing and that the real skill is framing the task in the model's terms. ([0:06](https://youtu.be/JRTAtZ5iBkU?t=6))
- **Canvas-based tools (PowerPoint, Slides, Figma, Canva) are built for humans, so agents using them produce bad output.** — Click, drag and snap-to-grid suit human spatial perception. The underlying data is in an application-only format, and agent output comes out with overlaps, unreadable text and no alignment. ([1:09](https://youtu.be/JRTAtZ5iBkU?t=69))
- **Failures on visual tasks come from the medium, not the model's spatial reasoning.** — He says an SVG is a wall of numbers that no person could write by hand either. Models should be given tools that match how they think: language, tokens and structure. ([2:33](https://youtu.be/JRTAtZ5iBkU?t=153))
- **HTML lets the model reason in structure, so it never has to place a coordinate.** — Tags like heading, chart and grid carry meaning, and the browser handles layout, fonts and motion. Models have seen huge amounts of HTML, so they handle it well. ([4:02](https://youtu.be/JRTAtZ5iBkU?t=242))
- **The editing format can be arbitrary: author in HTML and render to PDF or other formats later.** — He separates the deck (what the audience sees) from the tool used to make it, and says nobody in the audience cares how the presentation was produced. ([4:02](https://youtu.be/JRTAtZ5iBkU?t=242))
- **A good-looking deck is worth little without the content, so feed the agent real data.** — He says the agent should get access to call transcripts and emails so it can build the deck end to end. He describes building board decks on his phone during a commute. ([5:27](https://youtu.be/JRTAtZ5iBkU?t=327))

## Techniques
- **HTML as the agent's authoring format for visual artifacts** — Have the agent write slides, docs and video as HTML/CSS (divs, headings, grids, charts), then theme and edit the source directly. Render to PDF or another format at the end. *When:* Any time the output is a visual artifact (slide deck, doc, explainer video) and the agent is producing it, instead of driving a GUI canvas or writing SVG by hand.
- **Pick the format the model is strongest in, separate from the delivery format** — Choose the editing format by how well the model handles it, then convert to the delivery format (PDF, PPTX, video) as a final step. *When:* When a tool's native format is opaque to agents (binary, canvas-based, or app-only) and the audience only sees the rendered result.
- **Ground the artifact in source data, not in the layout** — Give the agent direct access to the raw inputs (call transcripts, emails, docs) so it fills the layout with real content. He treats the design as the easy part. *When:* When building decks or reports that must reflect real company data, such as board or sales decks.
- **Avoid screenshot-and-replace loops and canvas-driving tools for agents** — He contrasts these with HTML: Figma MCPs, PowerPoint CLIs and screenshot-replace loops all make the agent act like a human at a canvas. *When:* When choosing a toolchain for agent-produced graphics. Treat these as a weaker default.

## Numbers
- The world puts about 34,000 human-years a day into making slide decks (speaker's figure, unsourced). ([0:06](https://youtu.be/JRTAtZ5iBkU?t=6))
- A 10-hour deck should take about 25 minutes once formatting, branding and moving objects are removed (speaker's estimate). ([1:09](https://youtu.be/JRTAtZ5iBkU?t=69))
- Video length is 7:00. ([0:00](https://youtu.be/JRTAtZ5iBkU?t=0))

## Hot takes
- Calling them coding agents is bad marketing; they can do almost anything.
- Agents are not bad at spatial reasoning; the canvas medium is what fails.
- PowerPoint is just a tool; the deck is the presentation mode, and the editing format is arbitrary.
- Plain text is usually the wrong choice when you are trying to make something useful.
- Stop thinking like a user; think like the model.

## Tools mentioned
HTML, CSS, SVG, Figma MCP, PowerPoint CLI, PDF export, Nori Sessions

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps Claude Code and could produce HTML status reports or slides from agent runs. The talk's main claim is about artifact generation, not harness design. → *When a ProsHarness run needs a shareable report, try having the agent write it as HTML and render to PDF instead of driving a GUI tool or hand-writing SVG.*
- **general** (1/3): Relevant to the recurring interest in how agents should be given the right representation. Most of the talk is a product pitch with little evidence. → *Read the Simon Willison pelican-on-bicycle SVG test and try the same prompt on a current model to check the medium claim against your own tests.*

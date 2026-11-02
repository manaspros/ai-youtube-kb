# One Designer + AI. Hundreds of Deliverables. — Vincent Wendy, AI Engineer

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `O1FN4awNEtM` · [watch](https://youtu.be/O1FN4awNEtM) · **date:** 2026-09-18 · **length:** 16:48 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Vincent Wendy · **orgs:** AI Engineer
- **topics:** product-ux, context-engineering, testing-verification · **tags:** design-system, figma, design-tokens, spec-sheet, automation, visual-qa, devin, exception-handling, single-designer, conference-ops, face-matching, png-export

> A solo designer at AI Engineer uses agents (Devin, GPT, Figma) to produce hundreds of conference deliverables by fixing design tokens first, automating data-driven outputs, and checking results with an agent.

## Summary
Vincent Wendy, senior creative designer at AI Engineer, describes how one designer with a team of about 12 to 15 people produced the design for the conference (about 7,000 attendees, 140+ sponsors, 300+ speakers, 600+ sessions). His stated answer to the scale problem is five steps: set up a foundation (design system with colors, type scale, and components), build reusable design from it, automate workflows, validate output, and remove friction between design and engineering. He argues that LLMs invent random font sizes unless the design tokens are written down, so he defines desktop and mobile type scales for the agent to follow. Concrete uses include room schedules and speaker cards generated from data and exported to PNG, a Figma spec-sheet plugin that gives the agent annotated spacing, sizes and colors, and an agent that checks the sponsor logo banner for missing logos. He also uses an agent for exceptions, such as adding an edit button to the schedule tool when a change came in. The talk is mostly a practitioner experience report with few hard numbers, and the speaker frames it as non-technical.

## Key ideas
- **Scale problem: a very small team has to produce every deliverable (signage, stickers, landing pages, speaker graphics), and one missed sponsor logo or wrong schedule is a visible failure.** — Expected attendance rose from 6,000 to 7,000, with 140+ sponsors, 300+ speakers and 600+ sessions handled by about one designer and a team of 12 to 15. ([1:40](https://youtu.be/O1FN4awNEtM?t=100))
- **Five-part method: foundation first, reusable design, automated workflows, validated output, and removing friction.** — The speaker treats the design system as the base everything else is built from. Atomic design (small pieces combined into deliverables) is the mental model he uses. ([3:44](https://youtu.be/O1FN4awNEtM?t=224))
- **Define the design tokens before asking an LLM to produce anything, because models otherwise pick random font sizes and colors.** — He writes separate desktop and mobile type scales and a fixed color set so that generated output stays on-brand. Once the website's tokens are set, emails, flyers and documents can be built from the same definitions. ([6:17](https://youtu.be/O1FN4awNEtM?t=377))
- **Data-driven generation replaces manual layout work for repetitive assets like room schedules and speaker cards.** — A schedule that used to be built by hand in Figma is now requested from the agent with a room and a time, then exported to PNG for the screens. Speaker cards come from one template applied to 300+ speakers, with a landscape variant when a headshot exists. ([8:26](https://youtu.be/O1FN4awNEtM?t=506))
- **Pixel-accurate handoff comes from giving the agent a spec sheet, not just a mockup, since designers' layer names are unreliable.** — A free Figma plugin annotates the frame with spacing, font size and colors as a PDF, and the agent reads that along with the design. The speaker says the agent can handle unnamed layers like Frame 3 and Frame 4. ([10:35](https://youtu.be/O1FN4awNEtM?t=635))
- **An agent can serve as a QA check on large visual assets by comparing the output against a known list.** — The speaker asked the agent to find missing sponsor logos on the lobby banner and t-shirt artwork. He reports 100% accuracy on his own test, and he treats the agent plus a human reviewer as a two-step QA process. ([12:36](https://youtu.be/O1FN4awNEtM?t=756))
- **Real work is exception handling. Instead of redoing an asset by hand, ask the agent to add the missing feature, such as an edit button for schedule changes.** — The schedule tool had no edit button, so a late schedule change was handled by asking the agent to add one, then exporting again. ([14:41](https://youtu.be/O1FN4awNEtM?t=881))
- **Design for the user journey, not the designer's view. The speaker imagines an attendee walking from registration through wayfinding and QR codes, then fixes the gaps he finds.** — Thinking small and listing every failure mode in advance is his recommended way to make automation pay off. ([14:41](https://youtu.be/O1FN4awNEtM?t=881))

## Techniques
- **Tokens-first design system for agents** — Write the color palette, the type scale for each breakpoint, and the component set as an explicit spec the agent reads before generating anything. Keep the agent from inventing values. *When:* Before any agent-produced design or front-end work, and especially when many deliverables must match one brand.
- **Annotated spec sheet as handoff** — Export the design with spacing, font size and color annotations (via a Figma plugin) as a PDF, and send it to the coding agent together with the design file or MCP connection. Layer names do not need to be clean. *When:* When a coding agent must match a design pixel for pixel and the design file is messy.
- **Single data source to many assets** — Keep records like speakers or room schedules in one data source. Generate each card or schedule through a template, then export PNG for signage or the web. *When:* When hundreds of near-identical outputs change often.
- **Agent as checklist QA on visual output** — Give the agent the list of required items (such as sponsor logos) and ask it to find what is missing in the rendered graphic. A human checks the result afterward. *When:* For completeness checks on large graphics where a human would miss an item.
- **Vision-based photo matching** — Ask the agent whether two photos show the same person, then use the match to pull a speaker's photos from a large library. *When:* When you need to find the right photo for each person in a large image collection.
- **Raster first, then vectorize** — When the model cannot produce a usable vector image (the speaker's pelican-on-a-bicycle test), request a PNG and trace it into a vector in Figma. *When:* When a vector illustration is needed and the model's SVG output is poor.

## Numbers
- Expected attendees grew from 6,000 to 7,000. ([1:40](https://youtu.be/O1FN4awNEtM?t=100))
- 140+ sponsors, 300+ speakers, 600+ sessions, handled by one designer and a team of about 12 to 15 people. ([1:40](https://youtu.be/O1FN4awNEtM?t=100))
- 300+ speakers each need a speaker card, which is why the card is generated from data instead of built one by one. ([8:26](https://youtu.be/O1FN4awNEtM?t=506))
- The agent's missing-logo check reached 100% accuracy on the speaker's own test. The test size is not stated. ([12:36](https://youtu.be/O1FN4awNEtM?t=756))

## Hot takes
- Tools are no longer the problem; having a real problem is the advantage.
- An LLM's output is only usable if the design tokens are defined beforehand.
- The real job for a designer with agents is handling exceptions, not making the first version.

## Tools mentioned
Devin, GPT, Figma, MCP, Slack, PNG export, Figma spec-sheet plugin

## Relevance to our work
- **prosharness** (1/3): The talk's check-the-output step (agent compares a rendered result to a required list before it is accepted) is a loose match for ProsHarness's verification of long runs. No agent-harness architecture is discussed. → *Consider a short checklist step at the end of a ProsHarness run in which the agent verifies its output against a required-items list before the run is marked done.*
- **general** (1/3): Practical reminder that a spec-token file is what keeps agent-generated UI consistent, and that agent output should be checked against a list. → *Keep a single tokens or spec file in any repo where a coding agent generates UI, and read it before generating.*

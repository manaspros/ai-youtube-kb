# The Windsurf vs Cursor rivalry just reached a turning point

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `gejEvBWbgHA` · [watch](https://youtu.be/gejEvBWbgHA) · **date:** 2025-11-02 · **length:** 6:01 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** unnamed AI LABS host · **orgs:** Windsurf, Cursor, Anthropic, OpenAI, DeepSeek
- **topics:** coding-agents, vibe-coding-app-building, product-ux · **tags:** windsurf, cascade, cursor, front-end, select-to-edit, tab-to-import, linter, mcp, deepseek-v3, claude-3.7, gpt-4.5

> Windsurf feature tour: select a live page element in the preview, describe the change to Cascade, and it edits the code. Also covers Tab to Import, linter integration, suggested actions, built-in MCP docs and admin model controls. Mostly unmeasured demos.

## Summary
An unnamed AI LABS host demos the latest Windsurf update, centred on a new select-element feature for web previews. He selects a hero text element, asks Cascade to change its colour, restarts the dev server and confirms the change. He repeats the flow for a testimonial section (adding card animations) and a Get Started button (adding a pop-up), noting that Cascade fixed its own errors along the way. The rest of the video is a quick list of smaller updates: Tab to Import, built-in linter integration, suggested actions, built-in MCP documentation, drag-and-drop file references in Cascade, and admin control over models. The host argues Windsurf is now better than Cursor for front-end work, but he does not run a side-by-side comparison. There are no timings, success rates or cost figures beyond a claim about unlimited DeepSeek V3 usage.

## Key ideas
- **Select-to-edit on live previews** — A web page is previewed inside Windsurf; the user selects an element, and Cascade receives it as context. The host says it identifies the target without a text description, so he asks for the change in plain words instead of locating the element with a screenshot. ([0:00](https://youtu.be/gejEvBWbgHA?t=0))
- **Restart the dev server to verify edits** — After accepting Cascade's changes, the host restarts the dev server to check the result. The colour change on the hero text is confirmed this way. ([0:00](https://youtu.be/gejEvBWbgHA?t=0))
- **Section-level selection for larger edits** — Selecting a whole testimonial section and asking for card animations produced working CSS-style animations after one prompt. The host accepted them after reviewing them in the preview. ([1:13](https://youtu.be/gejEvBWbgHA?t=73))
- **Agent fixes its own errors during the run** — The host reports errors during the animation change and says Windsurf fixed them itself. He gives no detail on the error types or how often this happens. ([1:13](https://youtu.be/gejEvBWbgHA?t=73))
- **Screenshot-based debugging is the old workflow** — The host contrasts select-to-edit with his earlier Cursor and Windsurf work, where he had to screenshot errors and make the tool guess which element to fix. ([2:39](https://youtu.be/gejEvBWbgHA?t=159))
- **Tab to Import adds missing imports while typing** — Building on earlier Tab autocomplete, Super Complete and Tab to Jump, Tab to Import adds the import line for a dependency as the user writes it. ([3:45](https://youtu.be/gejEvBWbgHA?t=225))
- **Linter feedback goes to Cascade directly** — Cascade now has built-in linter integration, so linter errors can be handed to the agent without the user asking. The host notes Cursor already offered this. ([3:45](https://youtu.be/gejEvBWbgHA?t=225))
- **Suggested actions after a request** — After a specific request, Cascade proposes related changes based on the workflow it has seen. The host describes this as a flow-state editor that remembers the user's workflow. ([3:45](https://youtu.be/gejEvBWbgHA?t=225))
- **Admin model control for teams** — An admin control lets an organisation restrict which models are available. The host mentions it only briefly, with no detail on how it is set or enforced. ([5:02](https://youtu.be/gejEvBWbgHA?t=302))

## Techniques
- **Select-and-describe UI edits** — Open the page being developed in the Windsurf preview, use the select tool on the target element (it is attached to Cascade), describe the change in plain words (for example, make this text white for contrast), let Cascade apply it, accept the edits, then restart the dev server to check the result. *When:* Visual front-end tweaks where pointing at the element is faster than describing its selector or file location.
- **Batch section edits for animations** — Select a whole section (for example, a testimonial block) and ask for an effect across its child cards, then accept the diff and verify in the preview. *When:* Adding one behaviour to a group of elements at once, such as hover or entrance animations.
- **Let the agent fix its own build errors** — Keep the agent in the loop when the change fails: the host did not paste errors back in, and Windsurf reportedly fixed them itself. Check the result after the fix in the preview. *When:* Small UI changes where a failed build is cheap to retry. Not tested on larger or riskier changes in the video.
- **Drag files into the agent instead of referencing them** — Drag a file into the Cascade panel instead of typing an @-reference. The file is attached as context. *When:* Adding a few known files to context during a session.

## Numbers
- DeepSeek V3 is offered unlimited in Windsurf, and the host says it uses no credits. No pricing or limit is shown. ([2:39](https://youtu.be/gejEvBWbgHA?t=159))
- Three front-end edits (colour change, card animations, pop-up) each applied from one prompt in the demo. The video gives no timings, retry counts or success rate. ([0:00-2:39](https://youtu.be/gejEvBWbgHA?t=0))

## Hot takes
- The title says the rivalry 'reached a turning point' and the host calls Windsurf 'superior to cursor' and 'the go-to choice for front-end developers'. The video runs no comparison to support this.
- Select-to-edit is presented as a 'game changer' with no measured speed-up. The examples are three small, cosmetic UI changes on one demo page.
- The 'unlimited DeepSeek V3' point is a plan-specific promotion, not a feature that lasts. The host does not say how long it applies.

## Tools mentioned
Windsurf, Cascade, Cursor, Claude 3.7 (thinking mode, as named by the host), GPT-4.5 (as named by the host), DeepSeek V3, MCP

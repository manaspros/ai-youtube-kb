# Complete Guide to ChatGPT’s Canvas Update  New Tools & Features You Need

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `-ajtoeyu4go` · [watch](https://youtu.be/-ajtoeyu4go) · **date:** 2024-11-02 · **length:** 11:03 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** OpenAI
- **topics:** coding-agents, product-ux · **tags:** chatgpt, canvas, code-editing, inline-edits, auto-comments, logging, port-to-language, version-history, reading-level, writing-assistant

> A roughly 11-minute walkthrough of ChatGPT Canvas, the side-by-side editor for code and writing, covering inline edits, auto-comments, logging, port-to-language, and version navigation. Little hard data; mostly a UI tour.

## Summary
The video is a feature tour of ChatGPT Canvas (November 2024), a side-by-side editor where the chat sits on the left and generated code or prose sits on the right. The presenter says it is available to paid Teams and Plus users and is selected via a "GPT-4 with Canvas" entry in the model dropdown. For writing, the tour covers inline editing, adjusting length and reading level (graduate and middle-school examples), grammar polish, Suggest Edits, and adding emojis. For code, it covers review, inline changes instead of regenerating the whole answer, auto-added comments, "logs" that insert print statements, bug fixing, and porting code to another language (a Pygame game ported to C++/SFML). A Pygame Mario-style game needed several follow-up prompts before it worked, which the presenter presents as the main advantage of editing in place. Version arrows at the top right let the user step between earlier generated versions. The speaker mentions charts and benchmarks comparing Canvas efficiency but never shows any figures.

## Key ideas
- **Canvas puts generated content in a side panel next to the chat, so edits happen in the document or code instead of as a new full response.** — Chat stays on the left and code or text appears on the right. The presenter contrasts this with earlier workflows where any tweak produced a fresh answer from scratch. ([0:00](https://youtu.be/-ajtoeyu4go?t=0))
- **Canvas is enabled by picking a special model entry rather than a separate app mode.** — On the Plus plan the user picks the GPT-4 with Canvas option from the model dropdown at the top left. The presenter says it is for paid Teams and Plus users. ([0:00](https://youtu.be/-ajtoeyu4go?t=0))
- **For writing, the main features are inline editing, reading-level changes, polish, and emojis.** — Users can edit text directly, change length or reading level (graduate and middle-school examples were shown), run a polish pass for grammar and flow, and add emojis. Suggest Edits highlights changes that the user accepts with Apply. ([1:19](https://youtu.be/-ajtoeyu4go?t=79))
- **For code, Canvas edits in the editor: review, comments, logging, bug fixes, and language porting.** — Changes appear as edits in the editor rather than a new reply. The presenter also highlights automatic comments, debug logs, and a port-to-language action that creates a separate file. ([2:48](https://youtu.be/-ajtoeyu4go?t=168))
- **The demo needed several iterative prompts before the game worked, and the presenter credits the in-editor workflow for making that quick.** — The first Pygame Mario-style game ran but did not behave as expected. The presenter then fixed it through several prompts inside Canvas, which the video frames as collaborative editing. ([4:36](https://youtu.be/-ajtoeyu4go?t=276))
- **The logs feature inserts print statements throughout the code so runtime flow and errors are easier to trace.** — The presenter describes this as error logging: the print statements show the flow of execution and point to where an error happens. The port feature is shown converting the Python game to C++ using SFML. ([5:38](https://youtu.be/-ajtoeyu4go?t=338))
- **Version arrows at the top right let users step back through earlier Canvas generations of the same document.** — The presenter says the arrows let the user move between earlier versions and restore a current or previous one, as a guard against bad edits. ([6:59](https://youtu.be/-ajtoeyu4go?t=419))

## Techniques
- **Iterate in place with Canvas instead of re-prompting** — Generate the artifact in Canvas, then ask for targeted changes; the model edits the document or code in the editor. Use the version arrows (top right) to roll back a bad iteration. *When:* Multi-round edits to a single code file or long document where regenerating the full answer loses context or quality.
- **Canvas editor actions for code: review, comments, logs, port** — Open the code in Canvas and use the editor actions: Review code, Add comments, Add logs (inserts print statements), Fix bugs, and Port to language (pick a target such as C++; output goes to a separate file). *When:* Quickly documenting, debugging, or translating a script. The presenter shows this for a Python game.
- **Canvas writing actions: Suggest Edits, reading level, polish, emojis** — Select a passage and use Suggest Edits, then Apply the suggestions you accept. Use the reading-level control for grade levels (the demo goes from graduate to middle school). Use the polish action for a final grammar and flow pass. *When:* Revising drafts for audience or readability, or cleaning up a document before sharing.

## Numbers
- No benchmark figures are stated. The presenter says charts show Canvas is more efficient than earlier options, but no values are given in the transcript. ([2:48](https://youtu.be/-ajtoeyu4go?t=168))
- The Pygame demo needed several follow-up prompts before it ran as expected. No count is given. ([4:36](https://youtu.be/-ajtoeyu4go?t=276))
- Video length is 11:03; the feature tour is the bulk of it. ([0:00](https://youtu.be/-ajtoeyu4go?t=0))

## Hot takes
- The title promises a complete guide, but this is a short UI tour of a 2024 ChatGPT feature with no measurements.
- The efficiency claim rests on charts that the video never shows, so it is unverified.
- The presenter says the emoji feature added 'maybe a bit too many', which undercuts the feature's value.

## Tools mentioned
ChatGPT, ChatGPT Canvas, GPT-4 (with Canvas), Python, Pygame, VS Code, C++, SFML

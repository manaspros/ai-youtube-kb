# Add this Chrome Extension to 10X your productivity

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `j8KcvLrZ9uU` · [watch](https://youtu.be/j8KcvLrZ9uU) · **date:** 2025-11-02 · **length:** 8:25 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed host (AI LABS channel) · **orgs:** MindStudio
- **topics:** agent-architecture, product-ux · **tags:** browser-agent, chrome-extension, no-code-agent-builder, visual-workflow, mindstudio, agent-marketplace, word-lookup-agent, publishing-agents

> A walkthrough of MindStudio's Chrome extension for running prebuilt browser agents and building a simple word-lookup agent with its visual block builder. Mostly a product tour with a hype title and thin technical depth.

## Summary
The host installs MindStudio's Chrome extension, which adds a side menu of prebuilt agents that act on the current web page. He runs a YouTube-to-X-thread agent on one of his videos, which finishes in roughly 2-3 minutes and sends a notification when done. He then runs a competitor-analysis agent on a MacBook Pro product page, which pulls the specs and returns strengths and weaknesses. He dismisses the developer agents (such as an API cheat-sheet generator) as unnecessary next to AI IDEs like Cursor and Windsurf. The second half builds a "Word Query" agent: a browser-extension trigger supplies the selected text and URL, a user-input block collects an optional question, and a generate-text block with a conditional prompt either defines the word or answers the question. He publishes it after a workaround for a bug where an end-session setting still returned JSON. The video has no sponsor segment, but the title oversells what is a short product tour.

## Key ideas
- **The extension is a side-panel launcher for prebuilt agents that operate on the page you are viewing.** — After installing from the Chrome Web Store (works on Chromium browsers, including Arc), the host pins the extension and opens a side menu of agents. Some are free and some are labeled paid. ([0:00](https://youtu.be/j8KcvLrZ9uU?t=0))
- **Long-running agents notify you on completion instead of making you wait.** — The YouTube-to-X-thread agent takes about 2-3 minutes; a notification fires when it finishes. The host says this replaces writing a thread by hand or generating one from a script. ([3:16](https://youtu.be/j8KcvLrZ9uU?t=196))
- **Page-reading agents can produce useful competitor analysis from structured spec pages.** — On a MacBook Pro product page, the competitor agent read the listed specs and returned competitors with strengths and weaknesses. The host calls it accurate and useful, which rests on one demo. ([4:29](https://youtu.be/j8KcvLrZ9uU?t=269))
- **The host sees little value in developer-facing agents now that AI IDEs write code directly.** — He finds the API cheat-sheet agent promising for understanding code but says tools like Cursor and Windsurf make it largely redundant. This is a personal opinion, not a measured result. ([1:35](https://youtu.be/j8KcvLrZ9uU?t=95))
- **Custom agents are built as visual block graphs with a start block, input blocks, generate-text blocks and an output behavior.** — The start block set to browser-extension supplies launch variables (URL and user selection). A user-input block collects a question, and a generate-text block references variables in double curly brackets inside a conditional prompt. ([5:31](https://youtu.be/j8KcvLrZ9uU?t=331))
- **Output and session settings in the builder are not fully reliable yet.** — Setting output behavior to end session still returned a JSON output in the host's test. He removed the end block as a temporary fix, which means the agent never formally ends, though he could still return to it. ([7:01](https://youtu.be/j8KcvLrZ9uU?t=421))
- **Agents are published from the builder and show up under the Build tab's Published and Drafts sections.** — The host opens the menu, goes to Build, expands Published and Drafts, and creates a new agent from Create a New Agent. Publish makes it live. ([5:31](https://youtu.be/j8KcvLrZ9uU?t=331))

## Techniques
- **Install and pin the MindStudio extension** — Open the MindStudio site, click the link to the Chrome Web Store, add the extension, pin it to the toolbar, then click it to open the side menu. Log in with Google. Run agents from the menu and pin favorites. *When:* When you want quick access to prebuilt page-level agents (summaries, social posts, competitor analysis) without pasting page content into a chatbot.
- **Build a selection-driven lookup agent in the visual builder** — 1) Build tab > Published/Drafts > Create a New Agent. 2) Click the Start block and set the trigger to Browser extension to get the URL and user-selection variables. 3) Add a User input block with variable name user_question and label 'question'. 4) Add a Generate text block. 5) In its prompt, reference the selection with double curly brackets, then write a conditional: if user_question is empty, return the meaning of the selected text; otherwise answer the question about it. 6) Choose the model (free options named: Claude 3.5 Haiku, GPT 4.0 Mini). 7) Set output behavior to Display result. 8) Publish. *When:* When you want a reusable in-browser helper that defines or explains whatever text you select, with an optional follow-up question.
- **Workaround for end-session returning JSON** — If output behavior is set to end session and the agent still returns a JSON blob, delete the End block. The agent then stops returning JSON but never formally ends (you can return to it). The host says a proper fix is still to come. *When:* Only as a stopgap for the reported bug in this version; verify the behavior in your own build before relying on it.

## Numbers
- Some agents take about 2-3 minutes to run (YouTube-to-X-thread agent). ([3:16](https://youtu.be/j8KcvLrZ9uU?t=196))
- Free models offered in the builder: Claude 3.5 Haiku and GPT 4.0 Mini. ([7:01](https://youtu.be/j8KcvLrZ9uU?t=421))
- Video length is 8:25; the demos are short and no benchmark, cost or latency data is given. ([0:00](https://youtu.be/j8KcvLrZ9uU?t=0))

## Hot takes
- Developer agents such as the API cheat-sheet generator are not very useful now that AI IDEs (Cursor, Windsurf) write the code.
- Many agents in the store are free and the paid ones are labeled; the host says the free image-generation agents are a good value.
- Title ('10X your productivity') is hype; the video shows a product tour and one simple custom agent with no measured productivity gain.

## Tools mentioned
MindStudio (Chrome extension and agent builder), Chrome Web Store, Arc browser, Claude 3.5 Haiku (free model in builder), GPT 4.0 Mini (free model in builder), ChatGPT (mentioned as the manual alternative), Cursor (mentioned), Windsurf (mentioned)

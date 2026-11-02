# Figma MCP Tutorial: The Best Way to Clone a Front-End

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `FJBLhd23f80` · [watch](https://youtu.be/FJBLhd23f80) · **date:** 2025-11-02 · **length:** 5:18 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Figma, Cursor
- **topics:** mcp-and-tools, coding-agents, vibe-coding-app-building · **tags:** figma, figma-mcp, mcp, sse, cursor, design-to-code, html-css, personal-access-token, get-node, pnpm, npx

> A 5-minute tutorial on connecting an open-source Figma MCP server to Cursor, then having the agent generate HTML/CSS from a Figma page link instead of a screenshot.

## Summary
The narrator sets up an open-source Figma MCP server (attributed to "glips") and wires it into Cursor, then uses it to generate an HTML/CSS clone of a Figma page. Setup is clone the repo, run pnpm install, create a read-only Figma personal access token, start the server with npx, and add it to Cursor as an SSE server. The server exposes Get File and Get Node tools. The agent first picked Get File, which fetches the whole file, so the narrator had to force it to use Get Node for a single page. Get Node returned detailed layout data, including sizes, colors and material effects such as a glass look, which the narrator argues a screenshot cannot provide. The output had a few minor placement bugs, which the narrator suggests fixing by supplying both a screenshot and the Figma link. The video is a short practitioner walkthrough with no benchmarks or comparison against a screenshot-only baseline, and its headline claims are untested.

## Key ideas
- **An open-source Figma MCP server lets an agent read a Figma page directly and generate front-end code from a Figma link, with no screenshot needed.** — The narrator presents the result as a near one-to-one clone of a full page. The claim rests on one demo. ([0:00](https://youtu.be/FJBLhd23f80?t=0))
- **Setup is a clone, pnpm install, then running the server with a Figma token. The server runs over SSE, so Cursor must be configured with type SSE and the URL printed in the terminal.** — The terminal prints a message like 'new sse connection has been established' when the server is up. In Cursor the connection status turns green when it is active. ([0:00](https://youtu.be/FJBLhd23f80?t=0))
- **The Figma personal access token only needs read-only access to file content, and it is shown only once.** — Create it under the Figma account settings, Security tab, personal access tokens. ([1:22](https://youtu.be/FJBLhd23f80?t=82))
- **Cursor's MCP configuration moved during recording. The MCP servers entry is now a dedicated 'MCP Services' section rather than under Features.** — The narrator notes the rest of the configuration is unchanged. ([2:44](https://youtu.be/FJBLhd23f80?t=164))
- **The agent did not pick the right tool on its own. It chose Get File, which pulls the whole file, instead of Get Node, which targets one node.** — The narrator blames unclear tool descriptions and forced the agent to use Get Node. This is the main practical gotcha in the video. ([2:44](https://youtu.be/FJBLhd23f80?t=164))
- **Scoped input works best. Right-click a section in Figma, choose copy/paste as, copy the link to the selection, and give that link to the agent.** — Node data includes sizes, colors and material properties such as whether a panel is solid or glass-like. The narrator says a screenshot cannot provide this. ([2:44](https://youtu.be/FJBLhd23f80?t=164))
- **Output is close but imperfect. Small errors such as an arrow or search icon placement remain.** — The narrator suggests adding a screenshot alongside the Figma link to correct mismatches, rather than fixing each element by hand. ([4:10](https://youtu.be/FJBLhd23f80?t=250))

## Techniques
- **Run a Figma MCP server over SSE and attach it to Cursor** — git clone the MCP repo, run pnpm install (pnpm must be installed), create a Figma personal access token with read-only file-content permission, then start the server with npx using the token as the Figma API key. Copy the SSE URL from the terminal output. In Cursor, add a new MCP server, name it, set type to SSE (not command), paste the URL, and wait for the status to turn green. *When:* When you want a coding agent to read Figma designs directly rather than through screenshots.
- **Copy a link to a Figma selection and hand it to the agent** — In Figma, right-click the section, choose Copy/paste as, then Copy link to selection. Paste the link into the agent prompt and ask it to implement the design in the target stack (the demo used HTML and CSS). *When:* When you only need one section or page converted, so the agent fetches a single node instead of the whole file.
- **Force the agent to the node tool when it picks the wrong one** — If the agent calls Get File for a single-page task, instruct it explicitly to use the Get Node tool. The narrator's exact wording is not shown in the video. *When:* When tool descriptions are not specific enough and the agent over-fetches with the whole-file tool.
- **Combine the Figma link with a screenshot for corrections** — Give the agent both the screenshot and the Figma link, then ask it to fix the mismatches, instead of correcting each element by hand. *When:* When the first generated output has small layout errors such as misplaced icons.

## Numbers
- Video length is 5:18. ([0:00](https://youtu.be/FJBLhd23f80?t=0))
- The Figma token needs only read-only access to file content, and the Figma MCP server exposes two tools used in the demo: Get File and Get Node. ([1:22](https://youtu.be/FJBLhd23f80?t=82))
- The demo covered one full Figma page, with the agent generating HTML/CSS that had a few minor placement bugs (an arrow and a search icon). ([4:10](https://youtu.be/FJBLhd23f80?t=250))

## Hot takes
- The headline claims of a 'perfect one-to-one clone' and that 'you can't recreate this with just a screenshot' are not tested against a screenshot-only baseline. The video shows one demo only.
- Title and intro are hype-leaning, but the content is a usable setup walkthrough, so quality is not capped at 2.
- The agent choosing Get File over Get Node is a real tool-description problem that the narrator attributes to unclear tool descriptions. It was not measured, only observed once.

## Tools mentioned
Figma MCP server (glips, open source, run via npx and pnpm), Figma API / personal access tokens, Cursor (MCP client), pnpm, npx, git, HTML/CSS (generation target)

## Relevance to our work
- **prosharness** (1/3): Shows an agent choosing a broad MCP tool over a narrow one until forced, which is a tool-selection problem a harness wrapping Claude Code with MCP tools would face. → *When wiring MCP servers into ProsHarness runs, check that tool descriptions steer the agent to the narrow tool, and test the agent's tool choice on one representative task.*

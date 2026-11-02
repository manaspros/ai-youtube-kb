# This MCP Setup is the Best Way to Add 3D Models to Your Frontend

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `srsst0L51RE` · [watch](https://youtu.be/srsst0L51RE) · **date:** 2025-11-02 · **length:** 6:27 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Sketchfab
- **topics:** mcp-and-tools, coding-agents, vibe-coding-app-building · **tags:** mcp, sketchfab, cursor, windsurf, claude-desktop, threejs, 3d-models, landing-page, tutorial

> Short tutorial on connecting the Sketchfab MCP server to Cursor so an agent can search, download and place a 3D model into a Three.js landing page from one prompt.

## Summary
The creator installs a community Sketchfab MCP server from the mcp.so listing (git clone, npm install, build) and wires it into Cursor through an mcp.json entry that needs a Sketchfab API token and the absolute path to the built index.js. He then prompts Cursor to build a drone landing page with a 3D hero model in Three.js, and the agent calls the server's search, model-details and download tools in turn. The first model it picked looked poor, so he asked the agent to remove it and find a top-rated model with a preview link, which he checked in the browser. Windsurf's preview feature is recommended for model selection, but he could not test the MCP setup there. The video closes with a passing claim that Claude 3.7 is among the best tools for 3D game generation, which is not demonstrated. Overall this is a setup walkthrough with a single demo, not an evaluation.

## Key ideas
- **A single prompt in Cursor can add a 3D model to a web page when a Sketchfab MCP server is connected.** — The demo landing page's hero model was produced by one prompt; the agent used the Sketchfab MCP tools to find and download the model and then implemented it. ([0:00](https://youtu.be/srsst0L51RE?t=0))
- **Cursor's MCP setup now takes a JSON config block instead of a pasted command.** — Earlier Cursor versions required a specific command to be pasted. Now the server is added by editing the mcp.json file with a config entry containing a flag (left unchanged), the API key, and the path to index.js. ([1:20](https://youtu.be/srsst0L51RE?t=80))
- **The server exposes a search, model-details, download flow with no visual preview.** — The agent called search, then model details, then download. The speaker notes that the flow does not show candidates, so picking a model in Cursor means manually opening each link in a browser. Windsurf's preview feature is suggested as a better fit for this. ([2:52](https://youtu.be/srsst0L51RE?t=172))
- **Iterating on the model choice is done by re-prompting the agent.** — The first model looked basic and did not match the site, so he asked the server to remove it, find a top-rated replacement, and return a preview link. He checked the link and the final page used the new model. ([4:25](https://youtu.be/srsst0L51RE?t=265))
- **The speaker's broader claim that Claude 3.7 is among the best for 3D games is asserted, not shown.** — No game was built in the video. The Three.js game use case is mentioned only as a possibility. ([5:49](https://youtu.be/srsst0L51RE?t=349))

## Techniques
- **Install the Sketchfab MCP server from source** — git clone the repo listed on the mcp.so page, cd into it, run npm install, then run the build step (spoken as 'npm build', likely npm run build), and start it as an MCP stdio server. *When:* Use when you want an agent to fetch Sketchfab models for web or game work.
- **Get a Sketchfab API token** — Log in to Sketchfab, open Settings, go to the Password and API section, and copy the API token. *When:* Required by the MCP server config before any search or download call works.
- **Get the absolute path to the built server entry point** — In the project root, cd into build/ and run the real-path command on index.js (speaker does not name it; realpath is the usual command on Linux). Copy the printed path. *When:* The MCP client config needs an absolute path to build/index.js.
- **Register the server in Cursor via mcp.json** — Open Cursor's mcp.json from the tools/MCP settings and add the server entry from the mcp.so page. Leave the flag unchanged, replace the API key placeholder with the token, and replace the path placeholder with the absolute index.js path. Claude Desktop and Windsurf take the same configuration block. *When:* Use to make the Sketchfab tools available to Cursor, Windsurf or Claude Desktop.
- **Prompt for a 3D hero section and iterate on the model** — Prompt: a sleek, modern landing page with a hero section that uses a 3D model rendered with Three.js. If the result looks weak, ask the agent to remove the model, search for a top-rated one, verify it, and return a preview link to open in the browser. *When:* Use for landing pages or simple web 3D where the model's look matters.

## Numbers
- The agent used three MCP tool calls in order: search, model details, download. ([2:52](https://youtu.be/srsst0L51RE?t=172))
- The video is 6:27 long. ([0:00](https://youtu.be/srsst0L51RE?t=0))

## Hot takes
- Windsurf is recommended over Cursor for MCP-driven model selection because of its preview feature, though the speaker did not test the MCP server in Windsurf.
- Claude 3.7 is called one of the best tools for generating 3D games, with no evidence shown.
- The server's flow of search, details, download with no preview is described as tedious in Cursor.

## Tools mentioned
Sketchfab MCP server (community server listed on mcp.so), Sketchfab, Cursor, Windsurf, Claude Desktop, Three.js (3JS), git, npm, Claude 3.7 (mentioned for 3D game generation)

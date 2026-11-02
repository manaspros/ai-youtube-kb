# I Built an MCP Server with a Single Prompt!

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `yLAmw4oL-6A` · [watch](https://youtu.be/yLAmw4oL-6A) · **date:** 2025-11-02 · **length:** 7:30 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed AI LABS host · **orgs:** AI LABS, OpenWeather, Figma, Cursor, Windsurf
- **topics:** mcp-and-tools, coding-agents · **tags:** mcp, mcp-server-generation, prompt-to-tool, sse, cursor, claude-desktop, figma-mcp, openweather, test-before-deploy, mcp-json

> A walkthrough of a hosted prompt-to-MCP-server generator, shown building a weather server and a Figma server, with practical lessons on testing before deploy and wiring the result into Cursor.

## Summary
The host shows an unnamed platform that generates SSE-based MCP servers from a plain-language prompt, and says it built the Figma MCP server this way. The generator asks clarifying questions first (API key, how credentials are passed, what data to access, output format), then builds tools iteratively. The first weather-server attempt returned nothing when tested, so he asked for the raw API call with his key to try in a browser. He also had to tell the generator about OpenWeather free-plan limits. Chaining follow-up prompts degraded results until he reissued the original full prompt, which worked. Generated code can be exported and handed to Cursor to run locally, and the deployed server cannot be edited afterward. Wiring it into Cursor means copying the deploy config into mcp.json, renaming the server key and keeping the url key. The Figma server was split into separate file-data and node-data tools after a first attempt produced only one. The video is a product walkthrough with thin evaluation and no shown code.

## Key ideas
- **A hosted platform turns a plain-language prompt into a working SSE-based MCP server without hand-written code, and the host says the Figma MCP server was made this way.** — The generator produces the tool definitions and code, and the host claims no coding was needed. The platform is never named in the transcript. ([0:00](https://youtu.be/yLAmw4oL-6A?t=0))
- **The generator interviews you before building.** — It asks whether you have an API key, how credentials should reach the server (per prompt or as environment variables), what data to access, and other specs. It then builds step by step. The UI has a modify mode for code and a chat mode for questions about the server. ([0:00](https://youtu.be/yLAmw4oL-6A?t=0))
- **Testing is the weak point, so ask for the raw API call and run it yourself.** — When asked to test, the generated server returned nothing. Requesting the exact API request with the key included let him paste it into a browser and confirm the service worked. He calls testing essential because a deployed server cannot be modified. ([1:22](https://youtu.be/yLAmw4oL-6A?t=82))
- **Tell the generator the service's real plan limits.** — His OpenWeather key was on the free plan and the generated tools called restricted features. After he said what the free tier allowed, the tool adjusted. ([1:22](https://youtu.be/yLAmw4oL-6A?t=82))
- **Chained follow-up prompts can degrade output, so reissue the original full prompt.** — After several patch-style prompts, the generator stopped returning correct API calls. Going back to the original complete prompt produced the correct current-weather call. He reports two or three failed prompts before that. ([2:48](https://youtu.be/yLAmw4oL-6A?t=168))
- **Generated tools can be exported and run locally.** — The generated code is viewable, and Cursor can replicate the tools in your own codebase so they run locally instead of on the hosted server. Once deployed, the hosted server cannot be changed, so fixes mean regenerating it. ([2:48](https://youtu.be/yLAmw4oL-6A?t=168))
- **The Figma server was made more usable by splitting one tool into two.** — The first attempt produced a single tool for file or node data. He asked for separate tools for file data and node data, and the result was a get-node-data tool that returned element details, including RGB colors, from a Figma link. ([5:33](https://youtu.be/yLAmw4oL-6A?t=333))

## Techniques
- **Prompt-to-MCP generation with env-var credentials** — State the service and what it should return, and say the API key is already set as an environment variable so it is not repeated in each prompt. Give the output format explicitly (he asked for degrees). Answer the generator's clarifying questions (key present, credential passing, which data to access, formatting). For a file-based source, specify whether to return default data for no selection, or the full file when asked. *When:* Starting any hosted MCP generator where credentials are needed and you want to avoid pasting secrets into prompts.
- **Test the raw API call before deploying** — Ask the generator for the exact HTTP request for the service with your key included. Run it in a browser or client yourself to confirm the response. Only then export or deploy the tool, because a deployed server cannot be edited. *When:* Before deploying any generated MCP server, especially when the generator's own test returns nothing.
- **Declare the plan limits up front** — When the API key is on a free or restricted tier, tell the generator which endpoints or features are allowed so it does not generate tools that call blocked features. *When:* Integrating any third-party API whose key has limited access.
- **Recover from drift by restarting from the original prompt** — When follow-up patches stop working, paste the complete original specification again instead of stacking more corrections, then re-test the raw call. *When:* The generator's outputs regress after several iterative prompts.
- **Wire a hosted MCP server into Cursor** — Copy the configuration shown after deployment. In Cursor, open Settings, go to the MCP section, and edit mcp.json. Extract the inner server entry from the copied block, rename its key to the server name you want, make sure the url key is present, and save. The server becomes available automatically. The video shows Claude Desktop and Windsurf config options too. *When:* After deploying a generated MCP server and wanting to use it from Cursor.
- **Split tools by data type** — If one generated tool covers several data shapes (for example file versus node), ask for separate tools for each so the model can choose the right call. *When:* A generated tool surface mixes unrelated operations and the agent picks the wrong one.
- **Export and run locally** — View the generated code and ask Cursor to recreate the tools in your own repo to run them locally instead of on the hosted server. *When:* You need control over the server, or the hosted deployment is too limited to modify.

## Numbers
- Video length is 7:30. ([0:00](https://youtu.be/yLAmw4oL-6A?t=0))
- Two or three more prompts failed before reverting to the original prompt, which then returned the correct weather API call. ([2:48](https://youtu.be/yLAmw4oL-6A?t=168))
- Two MCP servers were built in the demo: a weather server and a Figma server, which first produced one tool and was split into two. ([1:22](https://youtu.be/yLAmw4oL-6A?t=82))

## Hot takes
- Claims no code was written, yet the demo shows many iterations and manual test steps, so the no-code framing overstates the process.
- The platform is unnamed and the video is a product walkthrough with no code shown, which reads as promotional.
- Says the deployed server cannot be modified, which is a serious lock-in and iteration cost that the video mentions but does not evaluate.
- Credentials are handled via env vars and then pasted into generated code, with no discussion of how secrets are stored or who can see the hosted server.
- The host admits the tool still has bugs and will improve over time.

## Tools mentioned
MCP (Model Context Protocol), SSE-based MCP servers, Figma MCP server (get Figma node data tool), OpenWeather API, Cursor, Claude Desktop, Windsurf, mcp.json

## Relevance to our work
- **prosharness** (1/3): Keeping secrets out of prompts via env vars matches ProsHarness's zero-token credential handling, and the no-edit-after-deploy trap bears on checkpoint and rollback design. → *Check that generated or harness-created tools read credentials from environment variables, not prompt text, and plan for a redeploy path since hosted tools cannot be edited in place.*

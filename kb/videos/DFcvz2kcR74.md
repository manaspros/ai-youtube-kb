# How I Turned Claude Into a Design Tool with Pencil.dev

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `DFcvz2kcR74` · [watch](https://youtu.be/DFcvz2kcR74) · **date:** 2026-03-02 · **length:** 6:45 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed Better Stack host · **orgs:** Better Stack, Pencil (pencil.dev), Figma, Sketch, Unsplash, Tailwind Plus
- **topics:** vibe-coding-app-building, coding-agents, mcp-and-tools · **tags:** pencil, design-tool, mcp, claude-code, figma-import, ui-kit, design-to-code, vibe-design

> Walkthrough of Pencil, a free agent-driven design tool that Claude Code can drive over MCP to build dashboards and a bakery website, then code them. Shows a workable loop, with no benchmarks.

## Summary
The presenter demos Pencil, an agent-driven design tool that runs locally in an IDE or as a standalone app, with a Figma-like canvas, components, UI kits and CSS variables. He drives it from Claude Code in the terminal through the Pencil MCP server, so his skills and MCP servers are available, and the agent builds a rover-management dashboard on the canvas in real time. He then starts from a blank frame, applies a style guide, and prompts for a bohemian French bakery website with Unsplash images, which produces three pages after a few follow-up questions. He fixes text and padding by direct manipulation, then asks Claude to code the designs into a working site, which he judges as closely matching the designs. He notes Pencil files are plain JSON, which makes them easy for agents to read, and that the tool is free for now but venture-backed. Known issues he reports are an unresponsive build chat, a generating overlay that sometimes stays until save or restart, and slowness on some actions. This is a single-person product demo with no measurements, so treat it as a workflow idea rather than evidence of quality.

## Key ideas
- **Pencil is an agent-driven design tool that can run inside your IDE or as a standalone app, and it works like Figma for editing agent output.** — Features mentioned are components, UI kits, CSS variables and a free price for now. The presenter argues that designers may want to tweak or get sign-off on a design before any code is written. ([0:00](https://youtu.be/DFcvz2kcR74?t=0))
- **Driving Pencil from Claude Code in the terminal lets the agent reuse your existing skills and MCP servers during design.** — The prompt from Pencil's first file is pasted into Claude Code with an instruction to use the Pencil MCP server. The agent calls the Pencil batch design tool and the canvas updates live. The presenter then edits the result by hand (padding change on one element). ([1:19](https://youtu.be/DFcvz2kcR74?t=79))
- **Blank-canvas generation works when you set a frame size, apply a style guide, and let the agent ask clarifying questions before it designs.** — He sets a frame wider than 800 px (about 1024) and taller, selects the frame, applies the style guide, and prompts for a bakery site. A superpowers skill asks follow-up questions, and the agent proposes a wider frame than he drew. It produces three pages. ([2:40](https://youtu.be/DFcvz2kcR74?t=160))
- **Designs made this way can be turned into code page by page, and the presenter says the output matched the designs closely.** — He asks Claude to code the designs into a functioning site and checks each page against the designs: home, story and menu. He notes it added a background that was not in the designs. Because the design is AI-generated, he says he can connect the site to a database or other MCP tools afterward. ([4:06](https://youtu.be/DFcvz2kcR74?t=246))
- **Text in the design can be fixed by direct manipulation (double-click to edit, drag to move), so small AI design errors need no re-prompt.** — The presenter drags a text block to a new position and edits its wording on the canvas, then regards the issue as fixed. ([4:06](https://youtu.be/DFcvz2kcR74?t=246))
- **Pencil files are plain JSON, which the presenter credits as the reason agents can read and translate them into code.** — Figma designs can be imported via File > Import from Figma. He also says the team plans custom UI kit import, such as kits from Tailwind Plus. ([5:15](https://youtu.be/DFcvz2kcR74?t=315))
- **Current limitations are an unresponsive build chat, a generating overlay that sometimes persists until save or restart, and slowness on some actions.** — He calls these small problems the team is likely already working on. He also flags that the tool is free only for now because it is venture-backed. ([5:15](https://youtu.be/DFcvz2kcR74?t=315))

## Techniques
- **Drive a design tool from Claude Code via its MCP server** — Open the prompt in Pencil's first file (step three), copy it, paste it into a Claude Code session, and add an instruction to use the Pencil MCP server. Watch the canvas update as the agent uses the Pencil batch design tool to add layout, navigation and components. Keeps your own skills and MCP servers in the loop. *When:* You want agent-generated UI iterated visually before any code is written, and your skills or MCP servers should apply to the design work.
- **Build a UI from a UI kit** — Pick a kit in Pencil (the presenter uses Lunaris and mentions others such as Halo, Nitro and a kit captioned as 'Sha Tien'). Prompt the agent to build a dashboard from the kit's existing components. Use the theming panel to switch to dark mode, change the accent colour (such as yellow buttons) or change the background. *When:* You need a consistent component set quickly, such as an admin dashboard, and want a theme change without re-prompting.
- **Blank-canvas site generation with a style guide** — Choose File > New. Set the frame width above 800, for example 1024, and make the height longer. Select the frame, have Claude use the style guide, then prompt for the site (for example a bohemian French bakery with Unsplash images). Answer the clarifying questions from the superpowers skill. Review the pages it produces. *When:* You are starting from nothing and want a multi-page marketing site design before coding it.
- **Fix AI design output by direct manipulation** — Select an element and change its padding in the properties panel, or double-click text to edit its wording or drag it into place. Then continue prompting for the rest. *When:* The agent output is nearly right and only small spacing or copy fixes are needed. Re-prompting the whole design would be slower.
- **Hand designs to the agent for implementation** — After the design is done, ask Claude to code the designs into a working site. Compare each page with the designs (the presenter checks the home page, the story page and the menu). Add real data sources or MCP tools afterwards. *When:* You want to go from a design to a functioning site in one loop and check fidelity page by page.
- **Import existing Figma designs** — In Pencil, use File > Import from Figma to bring existing Figma designs in, then edit them with the agent. *When:* Designs already exist in Figma and you want to continue in Pencil.

## Numbers
- Pencil is completely free to use at the time of recording, and the presenter says this will not last because the company is venture-backed. ([0:00](https://youtu.be/DFcvz2kcR74?t=0))
- A suggested frame width of 1024 (the frame must be above 800), with the frame made taller. ([2:40](https://youtu.be/DFcvz2kcR74?t=160))
- The agent produced three website pages from one prompt, after a few clarifying questions. ([2:40](https://youtu.be/DFcvz2kcR74?t=160))
- The video is 6:45 long, and the presenter sped up the generation part. ([2:40](https://youtu.be/DFcvz2kcR74?t=160))
- No benchmarks, latency, token counts or adoption figures are given. Quality claims are qualitative only. ([4:06](https://youtu.be/DFcvz2kcR74?t=246))

## Hot takes
- The presenter says AI design output looks impressive enough that he would not assume it came from AI if he saw it on a website.
- The presenter believes Pencil is easier to set up than the Figma and Sketch MCP tools, based only on what he saw online. He says he did not try those tools.
- The free price will not last because the tool is venture-backed. This is speculation, not something he verified.

## Tools mentioned
Pencil (pencil.dev), Pencil MCP server, Pencil batch design tool, Claude Code, Figma, Figma MCP tool, Sketch, Sketch MCP tool, Lunaris UI kit, Halo UI kit, Nitro UI kit, Unsplash, superpowers skill, Claude Canvas, Tailwind Plus

## Relevance to our work
- **prosharness** (1/3): Shows Claude Code driving an external design tool through MCP, which ProsHarness' Claude Code wrapper could use in a long-running loop. The video does not discuss checkpointing or approvals. → *Check whether Pencil's MCP server works in a ProsHarness-run Claude Code session. Only do this if UI generation becomes a ProsHarness workload.*

# Github #1 Trending Skill's Author Just Fixed Claude's Design Problem

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `Ow_z94c3wKk` · [watch](https://youtu.be/Ow_z94c3wKk) · **date:** 2026-10-02 · **length:** 12:35 · **format:** review · **quality:** 2/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** AI LABS, Manid (sponsor)
- **topics:** mcp-and-tools, coding-agents, vibe-coding-app-building · **tags:** inspo, mcp, design, design-md, ui-skills, frontend, reference-retrieval, claude-code, sponsored, tutorial

> Walkthrough of Inspo, a free MCP server of 832 captured sites with per-site design.md files that lets coding agents pull real references before designing. Sponsored segment; tested on one demo page.

## Summary
The video argues that AI-generated sites look generic because models default to the most common patterns in their training data, and that markdown design-skill instructions cannot show how components fit together. It presents Inspo, an MCP server with 832 captured sites (2,320 page screenshots, desktop and mobile), component references, and a design.md per site listing exact colors, fonts and measurements. The Recommend tool returns the most common layout among the top matches, up to five examples, component references, a palette and up to three screenshots. The host installed it in user scope and tested it on a demo fashion landing page, where the agent expanded the prompt with style keywords, studied about 24 sites, offered three directions, and combined parts of several references instead of copying one. Animations were added separately through a UI Skills MCP server. Failure cases were wrong-industry references for a coffee prompt, and pop-ups covering screenshots that led the agent to invent that section. A sponsor segment (Manid) sits in the middle.

## Key ideas
- **Generic AI design is a training-frequency effect** — Models learn the patterns that appear most often and treat them as safe, so without design direction they reproduce a recognizable house style (for example purple/blue on white, or warm orange and cream). ([0:00](https://youtu.be/Ow_z94c3wKk?t=0))
- **Markdown design instructions do not show how a whole page fits together** — Existing design skills tell the model fonts and layout in text and sometimes reference sites, but the model still cannot see how components interact on a full page. ([2:43](https://youtu.be/Ow_z94c3wKk?t=163))
- **Inspo gives the agent real captured sites plus structured design data** — It is an MCP server over 832 sites and 2,320 page screenshots, with component references and a design.md per site (exact palette, fonts, text sizes, spacing) so the agent does not have to infer styles from images. ([2:43](https://youtu.be/Ow_z94c3wKk?t=163))
- **Recommend picks the layout that recurs among the closest matches** — The search finds the nearest captured pages, takes the layout that appears most often among the top results, and returns up to five examples with components, a suggested palette and up to three screenshots. ([4:06](https://youtu.be/Ow_z94c3wKk?t=246))
- **Fewer references studied in depth is a deliberate context-budget choice** — Inspo tells the agent to study only a few references in detail and stop searching once it has enough, because each extra search adds results to the context and makes the style choice less certain. ([5:34](https://youtu.be/Ow_z94c3wKk?t=334))
- **Ask for design directions before the build so you can redirect early** — The host asked the agent for a few styles before building, so they could stop and change direction before the full site existed. The agent offered three directions and built only after a choice. ([8:29](https://youtu.be/Ow_z94c3wKk?t=509))
- **Synthesis, not copying, was verified by checking the cited sources** — The host asked which sites the agent had referenced, opened the links, and found that the hero came from one site, the buttons from another and the product layout from a third, with no exact copy. ([8:29](https://youtu.be/Ow_z94c3wKk?t=509))
- **Inspo does not cover animation; a separate skill library does** — Animations were added with the UI Skills MCP, which searches a library of skills from several authors and loaded an animation skill and a scroll-animation skill. ([9:57](https://youtu.be/Ow_z94c3wKk?t=597))
- **Known failure modes: wrong-industry references and occluded screenshots** — A coffee-subscription prompt returned health and business references until a food and beverage industry filter was applied. Pop-ups covered parts of some screenshots, and the agent filled the hidden part with its own guess. ([11:24](https://youtu.be/Ow_z94c3wKk?t=684))

## Techniques
- **Pre-build style menu** — In the prompt, ask the agent to propose a few visual directions (with descriptions) and wait for a choice before it builds the full page. Use this as a checkpoint to catch drift toward a wrong style. *When:* Any agent-driven UI build where the style is not fully specified, so a redirect costs less than a rebuild.
- **Reference provenance check** — After the build, ask the agent to list every site it referenced, open the links, and compare which section came from which source. Confirm the design combines patterns rather than copying one site. *When:* When you want evidence that a reference-driven design was synthesized and not copied.
- **Filter-scoped reference search** — State the industry, page layout and light/dark theme in the prompt or choose them in Inspo's filters so the reference search is narrowed. Check that the returned references match the site type; if not, re-run with the industry filter set. *When:* When the prompt is vague or the first search returns off-topic references.
- **Cap reference study depth** — Tell the agent to study only a few references in detail and stop searching once it has enough material, instead of pulling in many results. *When:* When retrieved examples risk overloading context and making the agent indecisive about style.
- **Install Inspo in user scope** — Copy the install command from the Inspo website and run it in a terminal. The installer detects installed coding agents and asks whether to add Inspo to all of them. Answering no cancels the whole install, so for one agent re-run the command with a client flag naming that agent (flag name not shown in the video). Restart the agent and run the mcp command to confirm Inspo's 15 tools are listed. Install is user scope, so it is available in every folder. *When:* Setting up Inspo for Claude Code or another coding agent on a personal machine.
- **Split design and animation into separate MCP lookups** — Use Inspo for layout, palette and components, then ask the agent to find an animation skill through the UI Skills MCP and apply it on top. *When:* When a generated site is static and needs motion added after the visual design is settled.

## Numbers
- Inspo corpus: 832 sites, 2,320 captured pages as images, with desktop and mobile screenshots ([2:43](https://youtu.be/Ow_z94c3wKk?t=163))
- Recommend returns up to five example layouts, component references, a palette and up to three screenshots ([4:06](https://youtu.be/Ow_z94c3wKk?t=246))
- Inspo exposes 15 MCP tools after install ([7:01](https://youtu.be/Ow_z94c3wKk?t=421))
- Agent studied about 24 sites for the demo fashion landing page and offered three design directions ([8:29](https://youtu.be/Ow_z94c3wKk?t=509))
- Wrong-reference problem seen on 2 occasions in testing; coffee prompt got health and business references until the food and beverage filter was applied ([11:24](https://youtu.be/Ow_z94c3wKk?t=684))
- Sponsor claims (unverified): 1,900 additional tools behind one key; Stripe bought OpenRouter for $7 billion ([5:34](https://youtu.be/Ow_z94c3wKk?t=334))

## Hot takes
- Sponsored segment (Manid) at about 5:34; per the rule, quality is capped at 2. Sponsor figures (1,900 tools, $7B acquisition) are unverified.
- Title overstates the evidence: the whole test is one demo fashion landing page, and the host says results 'worked well most of the time' with no quantified comparison against other design skills.
- The host's own caveats are the most useful part: wrong-industry references on 2 occasions and pop-up occlusion of screenshots, which made the agent improvise hidden sections.
- The claim that the Inspo author is 'the same person behind Hallmark' is not substantiated in the video.

## Tools mentioned
Inspo (MCP server, free, no account or API key), UI Skills MCP server, Emil Kowalski animation skill, Mengto scroll animation skill (name as transcribed), Hallmark design skill (name as transcribed), AI Labs Pro design system (community resource), Claude Code, Manid (sponsor, agent tools API gateway)

## Relevance to our work
- **agentos** (1/3): The reference-retrieval pattern (search, pick the common structure, cap how many results enter context) is a small, relevant idea for retrieval budgets in MemoryMesh; it is not a direct build change. → *When designing MemoryMesh retrieval, cap the number of hits returned per tool call and stop once enough evidence is found, measuring the effect on answer quality.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI; an MCP-backed reference lookup plus a pre-build checkpoint and a provenance check is a reusable pattern for harness-driven UI work, and the install-scope notes apply to MCP setup. → *Consider a checkpoint step in ProsHarness plans where the agent proposes options and waits for approval before a large build, and log which references an agent cites.*

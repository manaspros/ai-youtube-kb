# Claude Code Just Killed Every Shopify Agency Ever

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `x2pRavsHdls` · [watch](https://youtu.be/x2pRavsHdls) · **date:** 2026-06-02 · **length:** 10:25 · **format:** tutorial · **quality:** 2/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Shopify, Anthropic, Google, Willow Voice
- **topics:** coding-agents, claude-code, vibe-coding-app-building, context-engineering · **tags:** shopify, shopify-cli, shopify-mcp, claude-md, skills, hooks, settings-json, gemini-cli, image-generation, html-prototyping, admin-api, storefront, sponsored, paywalled-guide

> A walkthrough for building and syncing a Shopify storefront with Claude Code, using the Shopify CLI, AI toolkit MCP, HTML prototype skill, Gemini image skill and settings.json hooks. Quality is capped by a sponsor segment and a thin, hype-titled setup guide.

## Summary
The presenter sets up a Shopify store end to end with Claude Code. The steps are: create a Shopify Partner account as a development sandbox, scaffold a React and TypeScript app with the Shopify CLI, and install the Shopify AI toolkit MCP and its plugin. The project gets a CLAUDE.md, a Gemini-CLI image generation skill, and a "prototype" skill that writes an HTML preview before any change touches the app. Hooks in settings.json act as guardrails, for example blocking pushes to the app without approval. The design is prototyped in HTML, then implemented in the development app and synced to the live store through the CLI and MCP. Admin API auth needs extra scopes before products can be added, and a payment plan is needed before the store is public. The video is mostly a sequence of steps with few measurements. A sponsor read sits at about 4:17, and the full setup guide and skills are behind a paid tier.

## Key ideas
- **A Shopify Partner account is the development sandbox. It exposes test tools such as fake payments and test users, and the app can later move to a merchant account once it is ready to sell.** — Sign up for a Partner account first. Build and test in the dev store, then add payment integrations and move to a merchant account for real sales. ([0:00](https://youtu.be/x2pRavsHdls?t=0))
- **The Shopify CLI is the bridge between the local app and the cloud store. The MCP alone only supplies API docs and validation, and it cannot push changes to a running store.** — Install the CLI from the docs. Pick the React app template and TypeScript. The CLI then handles deploy and sync, so the MCP is for knowledge and checks, not for publishing. ([1:27](https://youtu.be/x2pRavsHdls?t=87))
- **Skills and CLAUDE.md shape the output. A prototype skill writes an HTML preview before any change reaches the app, and an image skill replaces the SVG placeholders Claude generates by default.** — The presenter says CLAUDE.md holds their usual best practices (a separate video covers it). The prototype skill runs in two phases, preview then apply. The image skill calls Gemini CLI and relies on that CLI's own auth, so no separate API key is needed. ([2:49](https://youtu.be/x2pRavsHdls?t=169))
- **Hooks in settings.json act as guardrails. A pre-tool-use hook can stop Claude from pushing changes to the live app without approval.** — Hooks are configured in the project's .claude settings.json. The presenter says any number can be added. ([4:17](https://youtu.be/x2pRavsHdls?t=257))
- **HTML prototyping is much cheaper than iterating in the real app. The presenter says the full implementation pass costs a lot of time and tokens, so design changes should be settled in the HTML preview first.** — The first HTML draft had placeholder image sections. Claude then launched several Gemini CLI processes in parallel in YOLO mode, so no permission prompt blocked them. The images were generated to match the UI style. ([5:21](https://youtu.be/x2pRavsHdls?t=321))
- **The design is implemented in the development app, then synced to the live store with the CLI and MCP. Products need the Admin API and extra scopes, and the store stays password-gated until a plan is selected.** — Re-run the CLI auth command with added scopes to write products and publications. Without a plan, visitors need a password to see the store. ([8:16](https://youtu.be/x2pRavsHdls?t=496))

## Techniques
- **Two-phase skill: HTML preview, then apply** — Write a skill whose workflow is (1) render the requested design change as a standalone HTML file the user can preview, then (2) apply the approved change to the app. The skill.md holds both phases. The presenter's prototype skill works this way. *When:* Any UI change where re-implementing in the real app is slow and costly to iterate on.
- **Image generation through a CLI skill** — A skill tells the agent to call the Gemini CLI with a prompt and to save output to a fixed directory. The presenter uses Gemini CLI's own auth, so no API key is needed. Batch several generations by launching multiple CLI processes from bash, in YOLO mode so no permission prompt blocks them. *When:* Replacing placeholder images on a generated site. Note the security tradeoff of YOLO mode (see hot_takes).
- **Pre-tool-use hook as an approval gate** — Configure hooks in the project's settings.json. A pre-tool-use script can block actions such as pushing changes to the live app until the user approves. *When:* Any agent that can publish or deploy. Keep the publish step behind a hook, not only a prompt.
- **Shopify project bootstrap** — Partner account, then Shopify CLI install from the docs, select the React app template and TypeScript, let it install dependencies, run the dev app. Install the Shopify AI toolkit MCP with the Claude command from the docs, then the plugin with its install commands, then the reload-plugins command. Write CLAUDE.md before prompting for the first design. *When:* Starting a new Shopify storefront driven by Claude Code.
- **Admin API auth with incremental scopes** — Run the Shopify CLI auth command with the auth link. The browser opens and authorizes. For product writes, re-run the auth command with the extra scopes (write products, read and write publications). Then ask Claude to add products through the CLI and MCP. *When:* Once the theme is live and product data needs to go in. Request only the scopes the step needs, and re-authenticate when a step needs more.

## Numbers
- Sponsor claims from Willow Voice (not verified): 3x more accurate than built-in dictation, more than 100,000 daily users, SOC2 certified, HIPAA compliant, zero data retention. ([4:17](https://youtu.be/x2pRavsHdls?t=257))
- No benchmarks, token counts or timings are given. The presenter says that iterating design in the real app 'would have wasted a lot of time and tokens' and that HTML prototyping is 'much faster and easier', but these are not measured. ([6:49](https://youtu.be/x2pRavsHdls?t=409))

## Hot takes
- The title says Claude Code 'killed every Shopify agency', but the video only demos one solo store setup. It makes no comparison with agency work.
- Sponsored segment (Willow Voice) at about 4:17. Quality is capped at 2 under the rules.
- The image-generation step runs Gemini CLI in YOLO mode, which removes the permission prompts. The video presents this as a convenience and does not discuss the risk, which matters when hooks are the guardrail.
- The setup guide and the skills are gated behind an 'AI Labs Pro' paid tier. The free video shows the workflow without the artifacts needed to reproduce it.
- The claim that HTML prototyping saves time and tokens is asserted, not measured.

## Tools mentioned
Shopify Partner account, Shopify CLI (React app template, TypeScript), Shopify AI toolkit (MCP), Shopify plugin (agents and skills), Shopify Admin API, Claude Code, CLAUDE.md, Gemini CLI (image generation), settings.json hooks, Willow Voice (sponsor segment, not a tool used in the setup)

## Relevance to our work
- **prosharness** (1/3): Hooks in settings.json used as an approval guardrail (pre-tool-use blocks a push until the user approves) match the ProsHarness approval pattern. The presenter's YOLO-mode subagents bypass that gate, which ProsHarness should avoid. → *Compare the pre-tool-use approval hook with ProsHarness's phone-driven approval flow. Check that spawned subagents inherit the same gate and do not run in a bypass-permissions mode.*

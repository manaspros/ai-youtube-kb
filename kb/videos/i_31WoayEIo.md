# AI Coding with Cursor & Claude: Build Apps That People Keep Using in 5 Simple Steps

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `i_31WoayEIo` · [watch](https://youtu.be/i_31WoayEIo) · **date:** 2025-11-02 · **length:** 12:13 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Anthropic (Claude), OpenAI (ChatGPT), Google (Gemini CLI, Google Fonts), Lovable, Windsurf, bolt.new
- **topics:** vibe-coding-app-building, context-engineering, product-ux, mcp-and-tools · **tags:** cursor, claude, chatgpt, context7, mcp, swiftui, ios, html-prototype, ux-md, colorscheme-md, conversion-md, animations-guide, google-fonts, color-palette, app-icon, context-engineering, fresh-chat-per-task, todo-list-agent

> Tutorial on building a photo-cleaner iOS app with Cursor and Claude: user journey saved in a markdown file, HTML prototype, palette, fonts, icon, Swift port and animations guided by Context7 docs.

## Summary
The host builds a swipe-to-clean photo app as a walkthrough of an AI-assisted workflow. He gets a user journey from Claude or ChatGPT, saves it to ux.md because Cursor forgets across chats, and has Cursor build a clickable HTML prototype first since HTML is faster to change than iOS code. He then layers in a color palette (colorscheme.md), a Google Font, and an app icon made with the ChatGPT image model. The HTML is ported to SwiftUI using conversion.md, with the Context7 MCP supplying framework docs. Animations are specified visually first, written as full implementations in an animations guide, and added one screen per fresh chat. He closes by saying a polished app takes about a month with AI rather than about six months, while the app is still visibly janky. The video is practical but light on code, and its retention and psychology framing is not really followed through.

## Key ideas
- **Execution and UX matter more than the app idea itself, since clones can win users with a better experience.** — The host argues that many photo-cleaner apps are on the App Store with poor UX, and that a better execution can win users from the same idea. ([1:03](https://youtu.be/i_31WoayEIo?t=63))
- **Cursor has no memory across chats, so important context must be written to files and re-referenced.** — He calls this context engineering and saves the user journey, palette, conversion rules and animation specs as markdown files in the project. ([2:10](https://youtu.be/i_31WoayEIo?t=130))
- **Build a clickable HTML prototype before any native code, because layout and design edits are much easier in HTML.** — He has Cursor build the flow from ux.md in HTML first, then converts it to a Swift app once the structure is settled. ([2:10](https://youtu.be/i_31WoayEIo?t=130))
- **Get the design system right in one pass: remove colors and emojis, identify UI elements, then map a palette to them and save the mapping.** — The palette mapping is stored in colorscheme.md so it is not forgotten. Fonts come from Google Fonts embed code and icons from the ChatGPT image model, both checked against the palette. ([4:23](https://youtu.be/i_31WoayEIo?t=263))
- **Use Context7 MCP to pull current framework docs before the port and before each fix, rather than letting the model guess the framework APIs.** — The host says Context7 uses vector search over docs for many frameworks and languages. It supplies the HTML-to-Swift conversion rules and the SwiftUI animation patterns, and he says it helps most when fixing errors. ([6:35](https://youtu.be/i_31WoayEIo?t=395))
- **Start a new chat for each discrete task, such as the conversion, because a fresh context performs better.** — Cursor's to-do list breaks the conversion into 15 items, edits files one by one, runs the app, and fixes errors it sees on its own. ([7:36](https://youtu.be/i_31WoayEIo?t=456))
- **For animations, describe the look visually first, then have the agent write a complete implementation per screen, and only then apply it.** — The host says Cursor does not know how to write polished SwiftUI animations unaided. He describes each screen's animation without timing or direction, stores full implementations in an animations guide, and does one screen per chat. ([8:46](https://youtu.be/i_31WoayEIo?t=526))
- **For bugs, capture a screenshot, send it to the agent, and tell it to consult Context7 again.** — He says doing one screen at a time avoids the model forgetting or breaking earlier work, and he admits the result is still janky with overlapping views and jitter. ([10:14](https://youtu.be/i_31WoayEIo?t=614))

## Techniques
- **Persistent context files in the repo** — Keep ux.md (user journey, pasted from Claude or ChatGPT), colorscheme.md (element-to-color mapping), conversion.md (HTML-to-Swift rules) and an animations guide file. Reference them in each new chat so the agent recovers the plan. *When:* Any multi-session build in Cursor, since its chats do not persist memory.
- **Specify the user journey first, then build an HTML prototype** — Ask Claude or ChatGPT (free tier is enough) to describe the app and its user journey, and read it for changes. Save it to ux.md, then have Cursor build the flow in HTML according to that file. *When:* Early product exploration, when UI structure will change often and native iteration is slow.
- **Palette-from-elements prompt sequence** — 1) Tell Cursor to remove all existing colors and emojis. 2) Have it list UI elements such as cards and buttons. 3) Have it map a palette onto those elements and save the mapping to colorscheme.md. 4) Generate a palette on a color-palette site by pressing space to cycle, export the CSS, and paste it to Cursor. 5) Have it apply the scheme to the HTML. *When:* When the prototype needs a consistent visual system before porting.
- **Google Fonts embed into the HTML prototype** — On fonts.google.com, pick a font, click Get font, choose the HTML tab, copy the embed code, and paste it into the prototype's HTML head. *When:* Quick typography change in a web prototype.
- **App icon via ChatGPT image model with palette constraint** — Describe a cartoonish icon for the app name (a leaf) for an iOS app, then add the color palette to the follow-up prompt so the icon matches the UI colors. *When:* Producing an icon without a designer, once a palette exists.
- **Context7 MCP for framework docs** — Add the Context7 MCP server to Cursor. Tell the agent to use Context7 when converting HTML to Swift, implementing animations and fixing errors, so it pulls the current framework documentation instead of guessing. *When:* Native or framework work where the model's built-in API knowledge is unreliable, such as SwiftUI animations.
- **Fresh chat per task plus Cursor to-do list** — Open a new Cursor chat for each major task. Ask the agent to write a to-do list (the example was 15 items) and work through the files one by one, then run the app and let it fix errors. *When:* Multi-file refactors or ports, where a clean context improves results.
- **Two-stage animation pipeline** — Stage 1: ask Claude for a visual description of each screen's animation, with no timing or direction. Stage 2: in Cursor, have the agent convert each description into a complete implementation in the animations guide, then have it add that exact implementation to the app. Repeat per screen in a new chat. *When:* Adding polish to a native app where the model should not invent animation timing on the fly.
- **Screenshot-driven bug fixing** — When a screen looks wrong, capture a screenshot of the simulator, send it to Cursor, and tell it to use Context7 MCP to find the correct implementation before editing. *When:* Visual bugs such as overlapping views or jitter in a native app.

## Numbers
- Build time for a polished product: about a month with AI, versus about six months before. Anecdotal, from the host's own experience. ([10:14](https://youtu.be/i_31WoayEIo?t=614))
- Cursor to-do list for the HTML-to-Swift conversion has 15 items. ([7:36](https://youtu.be/i_31WoayEIo?t=456))
- Hackathon from July 22 to July 28; top 5 submissions get featured in a video. Promotional, not a benchmark. ([3:23](https://youtu.be/i_31WoayEIo?t=203))
- Opening claim: successful apps get opened about 10 times a day by users. Rhetorical, not measured. ([0:00](https://youtu.be/i_31WoayEIo?t=0))

## Hot takes
- The title promises apps people keep using and the intro promises user-psychology and habit formation, but the body covers only build workflow, prototyping and visual polish. No retention mechanics are discussed.
- Claim that Cursor does not know how to implement SwiftUI animations unaided, and that Context7 fixes this. This is an unverified anecdote with no before-and-after comparison shown.
- The one-month-versus-six-months timeline is a single creator's anecdote, and the app shown is admittedly still janky.
- Hype-leaning framing: 'ideas don't matter' and 'competitive edge' are asserted without evidence. The video also includes hackathon and subscribe plugs, though it is not sponsored.
- Tool choice rests on the host's opinion that Cursor is best for beginners, with no comparison shown.

## Tools mentioned
Cursor, Windsurf, Lovable, bolt.new, Claude Code, Gemini CLI, Claude, ChatGPT, ChatGPT image model (called ChatGPT 4 image model in the video), Context7 MCP, Google Fonts, HTML, Swift, SwiftUI, iOS simulator, a color-palette generator site (name not spoken; link in the description)

## Relevance to our work
- **prosharness** (1/3): Manual version of ProsHarness's checkpoint/resume idea: persist plan and context to markdown files and start a fresh session per subtask, then pass the file as context. Only a passing parallel. → *Compare the ux.md / colorscheme.md / conversion.md file-based context pattern with how ProsHarness checkpoints long Claude Code runs, and check whether the plan files it writes are reusable across fresh sessions.*

# I Tried Building an Expo App in 360 Seconds… Here’s What Happened

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `Dmgu7jE2toM` · [watch](https://youtu.be/Dmgu7jE2toM) · **date:** 2025-11-02 · **length:** 6:02 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Tempolabs, Cursor, Expo, Google, OpenAI, Supabase, Stripe
- **topics:** vibe-coding-app-building, coding-agents, context-engineering · **tags:** expo, react-native, prd, mermaid, cursor, tempolabs, spec-first, docs-sync, gemini-2.5-pro, mobile-app, storyboard, next.js, supabase, stripe

> Walkthrough of a two-tool flow for Expo mobile apps: Tempolabs generates the PRD, user flow and wireframes, then Cursor takes over the code via a synced docs folder. Single-project demo with no measurements.

## Summary
The speaker builds a simple Expo mood-tracker app using Tempolabs for planning and Cursor for coding. Tempolabs turns a requirements prompt into a PRD, a Mermaid user-flow diagram and linked storyboard wireframes, and it can be edited by asking its agent. A Tempolabs extension in Cursor connects the two editors, and a docs folder with the PRD and diagram syncs both ways so Cursor's agent can read it as context. The app is then built in Cursor with Gemini 2.5 Pro from that PRD, with a few UI bugs; the dark-mode bug was fixed by Tempolabs's agent after Cursor failed to fix it. The speaker notes the pinch gesture jittered on desktop but was smooth in Expo Go on a phone, and mentions Tempolabs can also scaffold Next.js SaaS apps with Supabase and Stripe. The video makes strong claims about cutting planning and iteration time to near zero, and the title's 360 seconds is never measured on screen.

## Key ideas
- **Use a builder tool first to generate the spec: Tempolabs turns a detailed requirements prompt into a PRD and a user flow before any code is written.** — The speaker gives only functional requirements, not technical details, and selects the Expo framework. The PRD is generated first, then a user flow. The speaker argues Tempolabs is stronger at planning and design for React-based apps because it specializes in them. ([0:00](https://youtu.be/Dmgu7jE2toM?t=0))
- **The user flow is a Mermaid diagram that doubles as a living spec, editable by asking the agent.** — It lists every route and interaction, including animations, and drives the generated storyboard wireframes, which are split into components. The speaker says the agent can edit the diagram on request. ([1:12](https://youtu.be/Dmgu7jE2toM?t=72))
- **Local editing bridges the builder and the IDE: a Tempolabs extension in Cursor opens the project in the editor.** — The speaker installs the extension, chooses the editor, and allows the connection, which opens a new editor window connected over SSH with the app already imported. ([2:39](https://youtu.be/Dmgu7jE2toM?t=159))
- **Keep the PRD and Mermaid diagram in a docs folder inside the repo so the coding agent has the full context.** — The speaker pastes the PRD and diagram into a markdown file. The docs folder syncs both ways between Cursor and Tempolabs. The speaker says Cursor can format the file, or ChatGPT can do it. ([3:40](https://youtu.be/Dmgu7jE2toM?t=220))
- **Use a different agent for stubborn UI bugs. Cursor with Gemini 2.5 Pro built the app, but the dark-mode bug stayed until Tempolabs's own agent fixed it.** — The speaker says Gemini 2.5 Pro caused few issues. One dark-mode section did not adapt to the theme change, and a Cursor fix attempt failed. Prompting Tempolabs's agent resolved it. Remaining bugs were small UI issues. ([3:40](https://youtu.be/Dmgu7jE2toM?t=220))
- **Test on a real device. The pinch gesture jittered in the desktop preview but was smooth in Expo Go on a phone.** — The speaker loaded the app on a phone with the Expo Go app. This is a single observation, not a systematic test, but it shows the desktop preview can mislead on gesture behavior. ([4:20](https://youtu.be/Dmgu7jE2toM?t=260))
- **The same tool can scaffold full Next.js SaaS apps with auth, database and payments preconfigured.** — The speaker names Supabase and Stripe as the built-in integrations and points to a separate video on setting up a SaaS with Tempolabs. ([5:06](https://youtu.be/Dmgu7jE2toM?t=306))

## Techniques
- **PRD and user flow from a requirements prompt** — In Tempolabs, describe the app's functional requirements only (no tech details), select the Expo framework, and let it generate the PRD first, then the user flow (Mermaid diagram) and storyboard wireframes linked to the flow. Edit the flow by asking the agent in plain language. *When:* Starting a new mobile or React app where you want a spec and screen map before coding, for a solo builder or a designer handing off to a developer.
- **Connect the builder to the IDE via the Tempolabs extension** — In Tempolabs, open the 'local editing' icon and follow its prompt. In Cursor's Extensions tab, search for 'Tempolabs' and install it. Choose the target editor (Cursor), allow the connection, and the project opens in a new editor window via SSH. *When:* When you want to keep the AI-generated structure from the builder but refine code locally in your own editor and agent.
- **Commit the spec into the repo as context for the coding agent** — Create a docs folder in the project. Put a PRD markdown file in it with the full PRD text and the Mermaid user-flow diagram. Ask the coding agent to format it, or have another LLM format it. The docs folder syncs back to Tempolabs both ways. *When:* Before asking a coding agent to implement a multi-screen app, so it reads the requirements and routes instead of guessing them from a short prompt.
- **Route stubborn bugs to the agent that made the code** — When the local coding agent fails to fix a UI bug after a second try, switch to the builder's own agent in Tempolabs with the bug description and let it fix it there. *When:* When an AI-generated codebase is split between two agents and one agent keeps failing on the same bug (speaker's dark-mode example).
- **Verify gestures on a device, not the desktop preview** — Load the Expo app on a phone with the Expo Go app and test the interaction there. The speaker's pinch gesture jittered in the desktop view but was smooth on the phone. *When:* Any Expo app where touch interaction matters, since desktop previews may not reproduce gesture behavior.

## Hot takes
- The title says '360 seconds' but the video never times the build; the only timing claim is the speaker's remark that the flow saves 'near zero' planning and iteration time, which is unmeasured.
- Single project and single anecdote: one mood-tracker app, one model (Gemini 2.5 Pro), no comparison with Windsurf or Cursor alone despite naming them.
- The claim that Tempolabs is 'really solid' for React tasks rests on one bug fix, with no failure rate or cost given.
- Ends with a donation call-to-action; the video is a product walkthrough and is not labeled as sponsored.

## Tools mentioned
Tempolabs, Cursor, Expo, Expo Go, Gemini 2.5 Pro, ChatGPT, Mermaid, Windsurf, Next.js, Supabase, Stripe, SSH

## Relevance to our work
- **prosharness** (1/3): Plan-first workflow (PRD + user flow in a docs/ file read by the coding agent) is a light match for ProsHarness's plan step, but the video offers no harness, checkpoint or review mechanism. → *Compare how ProsHarness's plan step writes its spec to disk against this PRD-in-docs/ pattern, and check whether the coding agent is pointed at that file.*

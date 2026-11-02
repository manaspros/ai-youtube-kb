# 3 Ways to Build ACTUALLY Beautiful Websites Using Cursor AI

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `djDZHAi75dk` · [watch](https://youtu.be/djDZHAi75dk) · **date:** 2025-11-02 · **length:** 9:51 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Cursor, TweakCN, shadcn/ui, React Bits, Aceternity UI, Google Fonts
- **topics:** vibe-coding-app-building, product-ux · **tags:** cursor, ui-design, design-tokens, shadcn-ui, tweakcn, react-bits, framer-motion, nextjs, google-fonts, responsive-layout, animation, typography, prompting

> Three Cursor workflows for less generic AI-built sites: clone a reference design via an extracted design JSON, theme shadcn/ui with TweakCN, and drop in React Bits components, plus font and layout prompting tips.

## Summary
The speaker argues that AI-generated websites look generic because people prompt with vague requests like "make it beautiful." He presents three methods: (1) ask another AI to turn a reference design into a JSON design system and hand that file to Cursor; (2) customize a shadcn/ui theme on TweakCN (colors, fonts, shadows, light and dark modes) and paste the generated CSS into index.css; (3) copy animated components from React Bits into a Next.js landing page and have Cursor integrate them, including the framer-motion dependency. He then covers three prompting habits: be specific about animations rather than asking for "animated," pick fonts from Google Fonts and pass the embed code to Cursor, and specify exact layouts such as a bento grid that collapses to one column on mobile. Most of the advice is generic prompt-engineering guidance, and the concrete parts are mostly demonstrated on his own examples without showing the JSON schema or full prompts.

## Key ideas
- **Vague prompts like 'make it beautiful' produce the same generic AI-site look; specific design inputs are the fix.** — The speaker's framing is that the problem is how the AI is prompted, not the model itself. ([0:00](https://youtu.be/djDZHAi75dk?t=0))
- **Method 1: clone an existing design by having another AI extract its visual properties into a JSON design system, then give that JSON to Cursor.** — In the test, the prompt asked for an HTML/CSS/JS educational dashboard following design.json and did not mention design. The speaker says the result matched the target closely, but the JSON format itself is not shown. ([1:16](https://youtu.be/djDZHAi75dk?t=76))
- **Method 2: build a custom shadcn/ui theme on TweakCN and feed its generated code into the project.** — He adjusts primary, accent, base and card colors, fonts, and shadows, checks dashboard and mail previews in light and dark mode, then copies the code tab into index.css and asks Cursor to build from it. ([2:17](https://youtu.be/djDZHAi75dk?t=137))
- **Method 3: copy premium animated components from React Bits and have Cursor integrate them into a specific section.** — He picked a tilting 3D card for a six-section Next.js landing page. The prompt named the target section, told Cursor to use the component as the card, and asked it to install the framer-motion prerequisite. ([3:27](https://youtu.be/djDZHAi75dk?t=207))
- **Integrating complex components brings side effects that need a follow-up prompt.** — The tinted card's original code included a background image, and Cursor added a stock placeholder image. He had to ask Cursor to remove it. ([5:39](https://youtu.be/djDZHAi75dk?t=339))
- **Animation restraint: don't animate everything, and name the exact effect you want.** — He suggests asking the AI how to prompt for a specific 3D effect or subtle micro-interaction rather than asking for generic 'animated' output. ([6:51](https://youtu.be/djDZHAi75dk?t=411))
- **Font choice from Google Fonts is a cheap, high-impact change; pass the embed code to the agent.** — He chose a font on Google Fonts, copied the embed code, and asked Cursor to import it and apply it to the hero heading. ([8:05](https://youtu.be/djDZHAi75dk?t=485))
- **Specify the exact layout instead of asking for 'responsive.'** — He asked for a bento grid that becomes a single column on mobile, put the spec in a file, and showed the result in both desktop and mobile views. ([8:05](https://youtu.be/djDZHAi75dk?t=485))

## Techniques
- **Reference design to JSON design system, then build from it** — 1) Give Claude or ChatGPT a reference design and ask it to produce a JSON design system capturing style and structure, leaving the AI some latitude for other details. 2) Save the output as design.json. 3) In Cursor, ask for the app (the demo used HTML, CSS and JavaScript) and say to follow design.json, without restating design in the prompt. The JSON schema and full prompts are not shown in the video. *When:* You have a reference site or screenshot you want to match closely and do not want the agent to invent styling.
- **TweakCN theme to shadcn/ui project** — 1) On tweakcn.com, adjust primary, accent, base and card colors, fonts, and shadow. 2) Check the dashboard and mail previews in light and dark mode. 3) Open the code tab, copy the CSS, paste it into index.css in the project. 4) Ask Cursor to build the project from that file. *When:* You want an original, consistent shadcn/ui look without designing every token by hand, and you use shadcn components.
- **Drop a copied component into a named section** — 1) Copy the component's code from React Bits (optionally customize it first). 2) Note its prerequisites (here, framer-motion). 3) Prompt the agent with the target section by name, the instruction to use this component as that section's card, the dependency to install, and the pasted code. 4) Test hover and interaction, then fix side effects with a follow-up prompt (the demo removed an unwanted stock background image). *When:* A page is functional but visually plain, and you want polished interactive pieces without writing them from scratch.
- **Font via embed code** — On Google Fonts, pick a font, click Get font, copy the embed code, and give it to the agent with the instruction to import the font and apply it to a specific element (here, the hero heading). *When:* You want a quick typography upgrade that matches the project's tone.
- **Spec the layout explicitly and keep it in a file** — Describe the exact layout and its breakpoints (e.g., bento grid on desktop, single column on mobile) instead of asking for 'responsive.' Store the spec in a file so the output is reproducible and easy to re-check in desktop and mobile views. *When:* Layouts need to behave predictably across screen sizes and you don't want the agent guessing the breakpoints.
- **Animation restraint** — Ask for specific effects (a named 3D tilt, a subtle micro-interaction) on specific sections, and avoid blanket requests to animate everything. *When:* You want motion that adds polish rather than distraction.

## Numbers
- Landing page built as a Next.js app with six sections, created by Cursor from one prompt. ([4:22](https://youtu.be/djDZHAi75dk?t=262))
- The speaker says 50 people joined his first channel-membership tier immediately. This is a channel promotion, not a technical result. ([5:39](https://youtu.be/djDZHAi75dk?t=339))

## Hot takes
- The title promises 'actually beautiful' sites, but quality is judged only by the speaker's own before-and-after demos, with no comparison or rubric.
- The design-JSON method, the core of method 1, is shown without the JSON format or the exact prompts, so it is hard to reproduce from the video.
- Most of the advice ('be specific', 'don't overdo animations') is generic prompt-engineering guidance rather than a technique that is specific to Cursor or to design.
- The channel-membership plug is non-sponsored self-promotion; it does not affect the quality cap.

## Tools mentioned
Cursor, Claude, ChatGPT, TweakCN, shadcn/ui, React Bits, Aceternity UI, Google Fonts, Next.js, framer-motion, React, HTML, CSS, JavaScript, index.css

## Relevance to our work
- **agentos** (1/3): AgentOS may need an operator console or dashboards, and this video's design-token-JSON approach would only matter if the UI is built with a coding agent. The rest of the content (landing pages, shadcn themes, animated components) does not map to the AgentOS roadmap. → *If an AgentOS dashboard or console is built with a coding agent, pin a design-token JSON (or shadcn theme CSS) in the repo's CLAUDE.md and reference it in every UI prompt.*

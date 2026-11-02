# TikTok built an IDE to rival Cursor - Trae AI

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `OKmwTv0BHwE` · [watch](https://youtu.be/OKmwTv0BHwE) · **date:** 2025-11-02 · **length:** 8:07 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** ByteDance, TikTok, Cursor, Windsurf, Anthropic, OpenAI, JetBrains, DeepSeek
- **topics:** coding-agents, dev-tools · **tags:** trae, bytedance, vs-code-fork, ai-ide, cursor-alternative, builder-mode, agent-mode, inline-edit, tab-completion, nextjs, tailwind, claude-3.5-sonnet, gpt-4o, screenshot-to-code

> Hands-on first look at Trae, ByteDance's free VS Code-based AI IDE with an agent "builder" mode, inline edit and tab completion; the host finds it not yet compelling enough to replace Cursor.

## Summary
The host installs Trae, a VS Code fork from ByteDance (macOS only at recording time), and notes it feels close to stock VS Code, with existing VS Code and Cursor settings importable and a web view built into the editor. Two models are free to use at recording time, Claude 3.5 Sonnet and GPT-4o, with no pricing shown. In beta "builder" (agent) mode, a prompt for a Next.js and Tailwind landing page produced a plan, ran the create-next-app command via a run button that opens the terminal, and wrote page.tsx, but agent output appeared only after completion rather than streaming. Attaching a busy Twitter screenshot produced a generic Twitter clone with mock data, which the host attributes to a bias in training data. Accepted agent changes cannot be reapplied or rolled back the way Cursor allows. The inline edit (Cmd+I) streams line by line in a side-by-side diff the host finds cramped, and tab completion works. The host concludes that none of the features are compelling enough to leave Cursor and raises concerns about the parent company given the US TikTok ban.

## Key ideas
- **Trae is a free, stock-looking VS Code fork from ByteDance; existing VS Code and Cursor settings can be imported during setup, and VS Code extensions carry over.** — Setup offers theme choice and config import from VS Code or Cursor; login is required for AI features via GitHub or Google. The host says it looks and feels almost identical to stock VS Code, with a modern skin and some commenters compared it to JetBrains Fleet, which the host has not used. ([0:00](https://youtu.be/OKmwTv0BHwE?t=0))
- **The AI features are gated behind a beta 'builder' mode, which is the agent counterpart to Cursor's and Windsurf's agents.** — Two models are selectable and free for now: Claude 3.5 Sonnet and GPT-4o. The host expects pricing later and says Claude is usually expensive, so the free access is probably promotional. ([1:07](https://youtu.be/OKmwTv0BHwE?t=67))
- **Builder mode can run shell commands and the output pops into the real terminal; a built-in web view can open the dev server inside the editor.** — A prompt for a Next.js and Tailwind landing page led the agent to propose create-next-app, which the user runs from a button. The host calls out the pop-out terminal as a fix relative to Windsurf, and the dev server prompt offers a web view inside the editor. ([2:12](https://youtu.be/OKmwTv0BHwE?t=132))
- **Agent mode does not stream its edits. The user waits for the full change set, then accepts all at once.** — The host contrasts this with Cursor, where edits stream into the file. After completion, the changes are accepted with an accept-all button. ([3:27](https://youtu.be/OKmwTv0BHwE?t=207))
- **A screenshot of a busy page produced a generic clone with mock data, and the host blames the prompt and the screenshot.** — The host says the screenshot was hard to copy and should have been split into sections, and the prompt was too vague. Their guess is that training data full of Twitter clones pulls the output toward the generic version. ([4:24](https://youtu.be/OKmwTv0BHwE?t=264))
- **Accepted agent changes cannot be reapplied or rolled back later, which the host says Cursor handles better.** — After accepting, the only option is to review; if the code changes afterward, the review button no longer works as a rollback. ([4:24](https://youtu.be/OKmwTv0BHwE?t=264))
- **The inline edit (Cmd+I) streams its change line by line, and the diff is side-by-side, which the host finds cramped on a small screen.** — The host prefers Cursor's stacked diff. Tab completion works as expected, completing a filter expression. ([5:46](https://youtu.be/OKmwTv0BHwE?t=346))
- **The host wants an automatic model router, because Trae's marketing says each task goes to the most suitable agent but the user still picks the model.** — The host says that picking a model per task will get harder as models multiply and that a tool choosing for you would be better. Trae's website describes a collaboration of humans and agents, which the host reads as a pitch. ([6:xx](https://youtu.be/OKmwTv0BHwE?t=0))

## Techniques
- **Scaffold a project from a builder-mode prompt** — Open the editor in an empty folder, open the builder pane, and describe the app (here: a Next.js and Tailwind landing page with a hero section). Let the agent propose shell steps, click run to execute them in the integrated terminal, then review and click accept all. Use the web view or an external browser to check the dev server. *When:* Bootstrapping a small frontend project from a single prompt, when you are happy to accept the whole diff at once.
- **Attach context to builder mode** — Add a few lines, a file, or a folder as context in the builder pane before prompting. The host says this works like Cursor's context attachment. *When:* Giving an agent the existing code it should edit or copy patterns from, instead of relying on the prompt alone.
- **Screenshot-to-UI with split inputs** — Upload a screenshot in builder mode and ask for a new route (here /demo) with mock data. For busy screenshots, split the design into several smaller images or sections and give a more specific prompt than a generic one. *When:* Prototyping a page from a design. The host's test shows a simple screenshot and a detailed prompt are needed to avoid a generic clone.
- **Inline edit for scoped changes** — Select code and press Cmd+I (the host says command I, not command K) to open the inline prompt, for example to add a draft boolean to data. Changes stream line by line; review the diff, then accept all. *When:* Making a local change to a single function or block without an agent loop.

## Numbers
- Two models are available free in Trae at recording time: Claude 3.5 Sonnet and GPT-4o. The host expects pricing later. ([1:07](https://youtu.be/OKmwTv0BHwE?t=67))
- The video runs 8:07 and covers a single hands-on session with no benchmarks, latency, or cost data. ([0:00](https://youtu.be/OKmwTv0BHwE?t=0))
- At recording time Trae was macOS-only. ([0:00](https://youtu.be/OKmwTv0BHwE?t=0))

## Hot takes
- The host says none of Trae's features are compelling enough to switch from Cursor.
- Concern about the parent company, given the US TikTok ban.
- The host thinks the best improvement would be automatic model routing, so users do not have to pick a model per task.
- The title says it rivals Cursor, but the video is a first-impression walkthrough with no comparison data, so quality is capped at 2.

## Tools mentioned
Trae (ByteDance AI IDE), VS Code, Cursor, Windsurf, Claude 3.5 Sonnet, GPT-4o, Next.js, Tailwind CSS, create-next-app, JetBrains Fleet, DeepSeek

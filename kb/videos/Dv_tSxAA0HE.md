# How to Make Cursor CODE What You ACTUALLY Want.....

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `Dv_tSxAA0HE` · [watch](https://youtu.be/Dv_tSxAA0HE) · **date:** 2025-11-02 · **length:** 6:02 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** AI LABS host (unnamed in transcript) · **orgs:** Cursor, Supabase
- **topics:** coding-agents, context-engineering · **tags:** cursor, cursor-rules, project-rules, globs, notepads, cursor-docs, web-search, prompt-reuse, mcp

> A short Cursor feature tour: scoped project rules that replace the deprecated .cursorrules file, plus reusable prompts in Notepads, @web search, and custom doc indexing.

## Summary
The host walks through Cursor's newer rules system. Global user rules in Cursor Settings apply to every project, while project rules are per-project files with a description and globs that decide when they are pulled into context, which he says replaces the older single .cursorrules file. He suggests reusing community rule files from cursor.directory and Supabase's example prompts. Notepads hold reusable prompts that can be referenced in Composer. In chat, @web searches the web and returns sources, and custom docs can be added by pasting a docs URL so Cursor indexes them. He briefly mentions generating images through an MCP tool in a demo he found on X. The video is a UI tour with few measurements and no quantified productivity claims.

## Key ideas
- **Cursor's project rules are presented as the new way to scope instructions, replacing the old single .cursorrules file, which he says is deprecated.** — The old file tried to handle the whole repo at once. Per-project rules let frontend (Next.js/TypeScript) and backend (Python) instructions differ. ([0:00](https://youtu.be/Dv_tSxAA0HE?t=0))
- **User-level AI rules in Cursor Settings apply to every project opened in Cursor.** — His example global rule tells the model to give code directly and not make excuses, which he says helped a lot with an earlier habit. ([0:00](https://youtu.be/Dv_tSxAA0HE?t=0))
- **A project rule has a name, a description that says when it applies, globs that name file types to trigger it, and a body of instructions.** — Matching files cause the rule to be included automatically, so prompts reference the right file types without manual attaching. He created a 'python rules' rule as the example. ([1:27](https://youtu.be/Dv_tSxAA0HE?t=87))
- **Community rule files can be reused: cursor.directory lists rules per framework and language, and Supabase's GitHub examples/prompts folder contains ready-made prompts with description and globs already filled in.** — The example he gives is a database-migration prompt. The workflow is to copy the file or prompt and paste it into a rule. ([2:48](https://youtu.be/Dv_tSxAA0HE?t=168))
- **Notepads store reusable prompts and custom docs, and Composer can reference a note with @ to run it.** — He creates a note, renames it, and types a prompt into it, then references it in Composer with @ and runs it. ([2:48](https://youtu.be/Dv_tSxAA0HE?t=168))
- **@web in chat searches the web and returns the sources it used, mainly official documentation, which he demonstrated with the latest Next.js release notes.** — Pre-indexed docs such as Tailwind are available by name. If a doc is missing, as with n8n in his example, you can paste its docs URL and Cursor indexes it in settings, then you can reference it in chat. ([4:12](https://youtu.be/Dv_tSxAA0HE?t=252))
- **He says image generation is possible in Cursor through an MCP tool, shown in a demo he found on X, and defers MCP to a later video.** — He does not show the setup, so this is an unverified pointer rather than a tested technique. ([4:12](https://youtu.be/Dv_tSxAA0HE?t=252))

## Techniques
- **Global user rules for all projects** — Open Cursor Settings, scroll to the AI rules section, and put behavior rules there (his example: give the code directly and do not make excuses). They apply to every project opened in Cursor. *When:* For personal style or behavior preferences that should hold in every repo.
- **Scoped project rules with description and globs** — In Cursor Settings, find the project rules section and click add a new rule. Name it (e.g. 'python rules'). Fill in: description (when the rule should apply), globs (file patterns that trigger it, e.g. Python files), and the instruction body. The file is markdown, but plain text also works, per the host. *When:* When a monorepo or a project has separate frontend and backend stacks that need different conventions, so each set of instructions is only loaded for the matching files.
- **Reuse community rule files** — Browse cursor.directory by framework or language, read the descriptions, and copy a rule file into a new project rule. Supabase's example prompts are in its GitHub repo under examples/prompts and already include description and globs fields. *When:* When starting a new stack and you want tested starting instructions instead of writing them from scratch.
- **Reusable prompts in Notepads** — Open the Notepads panel, create a note, rename it (his example: 'prompt one'), and type the prompt. In Composer, reference the note with @ followed by its name and ask it to run the prompt. *When:* For prompts you run repeatedly, such as a standard task description or a checklist.
- **Web search and custom docs in chat** — Type @web followed by a question to get a web search with cited sources. For a framework that is not pre-indexed, paste its docs URL when adding custom docs, confirm, and wait for indexing in settings. Then reference the docs in chat. *When:* When a model needs current or unfamiliar library docs, such as a new framework version or a tool without built-in docs.

## Hot takes
- The title promises the model will code what you actually want, but the video is a feature tour. It offers no measurements of the productivity gains it claims at 0:00.
- The claim that scoped per-language rules avoid confusion compared with one big rules file is asserted, not tested.
- The MCP image-generation item at 4:12 is an unverified demo the host saw on X. It is a pointer, not a tutorial.

## Tools mentioned
Cursor, Cursor Composer, cursor.directory, Supabase (examples/prompts repo), Next.js, TypeScript, Python, Tailwind, n8n, MCP (Model Context Protocol)

## Relevance to our work
- **prosharness** (1/3): Scoped instructions keyed to file globs are a context-engineering pattern that could inform how ProsHarness splits Claude Code guidance by area, but this is a Cursor feature tour with little depth. → *Compare the glob-scoped project rules pattern with how ProsHarness currently loads CLAUDE.md and skills, and consider whether per-area instruction files would reduce context for the Claude Code CLI harness.*
- **general** (1/3): Confirms that per-file-type scoped rules are becoming a standard way to manage coding-agent instructions across editors. → *Read the Cursor rules documentation if we need a reference for how glob-scoped instructions are matched.*

# Claude 3.7 Sonnet is INSANE + Claude Code? (Best Coding Model)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `6KGH47rdeBs` · [watch](https://youtu.be/6KGH47rdeBs) · **date:** 2025-11-02 · **length:** 5:17 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Anthropic, Cursor, Google, DeepSeek
- **topics:** claude-code, coding-agents, models-research · **tags:** claude-3.7-sonnet, claude-code, extended-thinking, thinking-budget, swe-bench, tau-bench, custom-scaffolding, agentic-coding, pricing, permissions

> Walkthrough of Claude 3.7 Sonnet's hybrid extended-thinking mode, its published benchmarks, and the Claude Code research preview, shown on a single demo project.

## Summary
The presenter covers the Claude 3.7 Sonnet launch: a hybrid reasoning model where extended thinking gives the same model more time rather than switching to a different model. He tests extended thinking in the chat UI on one Monty Hall prompt and notes that the API lets you cap the thinking budget. He then reads the vendor's benchmark claims (SWE-bench and TAU-bench) and notes that API pricing did not change. The second half is a Claude Code demo on a Next.js Hacker News clone: he installs the CLI, asks it to explain the project, approves file-edit and npm-command prompts, has it add a submit page, and asks it to commit. The presenter admits a single prompt proves little and leans on vendor-published numbers, so the video is mostly a release recap with a shallow hands-on demo.

## Key ideas
- **Hybrid reasoning means extended thinking is the same model given more time and effort, not a separate reasoning model or strategy.** — The presenter calls 3.7 Sonnet the first hybrid reasoning model on the market and says extended mode simply lets the same model think longer, with the thought process visible. ([0:00](https://youtu.be/6KGH47rdeBs?t=0))
- **Thinking budget is controllable through the API, trading speed, cost and quality.** — You can cap the number of thinking tokens, up to the 128,000 output-token limit, so the same model can be tuned for latency or depth per request. ([1:15](https://youtu.be/6KGH47rdeBs?t=75))
- **The model was tuned away from competition math toward real-world business tasks.** — The launch post says it was optimized less for math and CS competition problems and more for tasks that reflect how businesses use LLMs. ([1:15](https://youtu.be/6KGH47rdeBs?t=75))
- **SWE-bench gains depend heavily on the scaffolding around the model.** — The base score is 62.3% and 70.3% with custom scaffolding. The scaffold gave the model a planning tool, a bash tool and a file-editing tool, while external code handled file retrieval and test validation. ([1:15](https://youtu.be/6KGH47rdeBs?t=75))
- **Extended thinking improves the agentic benchmarks further, but the presenter says a single prompt proves nothing.** — He cites TAU-bench as best-in-class and says extended thinking helps most on coding and math, but he is relying on the vendor's published numbers rather than his own tests. ([2:35](https://youtu.be/6KGH47rdeBs?t=155))
- **Claude Code launched as a terminal agent that reads the repo, asks permission per action, and can commit its own work.** — After installing it and running it in a project folder, the agent explored the code, answered questions about the project, edited a page and ran npm, with approval prompts for each category. It then wrote a git commit with a generated message. ([2:35](https://youtu.be/6KGH47rdeBs?t=155))
- **Permission prompts can be granted per tool class with a do-not-ask-again option.** — The presenter approved editing page.tsx with a yes-and-don't-ask-again choice, then did the same for running npm commands. Later steps then ran without prompts. ([3:55](https://youtu.be/6KGH47rdeBs?t=235))
- **The stated purpose of Claude Code is to learn how developers use Claude for coding in order to guide future model training.** — The presenter's reading of Anthropic's framing is that Claude Code is a research preview aimed at improving models from real usage data, not just a competitor to AI IDEs like Cursor. ([3:55](https://youtu.be/6KGH47rdeBs?t=235))

## Techniques
- **Toggle extended thinking in the chat UI** — In the claude.ai model selector, choose Extended instead of Normal. Extended is positioned for math and coding. The thinking stream is visible and can be expanded or collapsed. *When:* Use for hard math or coding prompts where you want to inspect the reasoning. Normal is fine for everyday requests.
- **Set a thinking budget on API calls** — Cap the thinking tokens per request, with the total output limit up to 128,000 tokens. The video does not show the parameter name or code, so check the API docs for the exact field. *When:* Use when you need to trade latency and cost against answer quality on a per-request basis.
- **Quick-start Claude Code on an existing project** — Install the CLI through npm, cd into the project folder, and run the claude command. Then ask it a plain question such as explain this project. It explores the files and answers from what it read. The exact npm package name is not shown in the video. *When:* Use to orient an agent on an unfamiliar repo before asking it to change anything.
- **Approve Claude Code actions with scoped trust** — When it asks to edit a file or run a command, approve with the yes and do-not-ask-again option for that action class. Each category is then trusted for the rest of the session. *When:* Use for a trusted repo where you want fewer interruptions while keeping a review step for new kinds of action.
- **Have Claude Code create the commit** — After the task finishes, ask it to commit the changes with git. It writes a commit message and description that summarize the work. *When:* Use as a final step to leave a reviewable commit that describes what the agent did.
- **Custom scaffolding for SWE-bench-style agents** — Give the model a small set of tools (a planning tool, a bash tool and a file-editing tool). External code handles file retrieval and test validation so the model focuses on reasoning and edits. *When:* Use when building your own coding agent loop and wanting to know how much of a benchmark score comes from scaffolding rather than the model.

## Numbers
- API pricing stayed at $3 per million input tokens and $15 per million output tokens ([2:35](https://youtu.be/6KGH47rdeBs?t=155))
- Extended thinking output is capped at a 128,000-token output limit, and the thinking budget can be set below that ([1:15](https://youtu.be/6KGH47rdeBs?t=75))
- SWE-bench score of 62.3% base, rising to 70.3% with custom scaffolding ([1:15](https://youtu.be/6KGH47rdeBs?t=75))
- Thinking time on a single Monty Hall prompt was about 19 seconds ([1:15](https://youtu.be/6KGH47rdeBs?t=75))
- Claude Code took about a minute of thinking before creating the submit page ([3:55](https://youtu.be/6KGH47rdeBs?t=235))

## Hot takes
- The title says INSANE, but the evidence is a single prompt and vendor-published benchmarks that the presenter did not reproduce.
- The presenter says a single prompt cannot judge model quality, then draws conclusions from one Monty Hall answer.
- The presenter is disappointed that pricing did not drop while Gemini and DeepSeek are much cheaper.

## Tools mentioned
Claude 3.7 Sonnet, Claude Code, Cursor, Gemini, DeepSeek, Next.js, TypeScript, Tailwind CSS, npm, git, SWE-bench, TAU-bench

## Relevance to our work
- **agentos** (1/3): Per-request thinking-token budgets are a cost and latency knob that could sit in a routing layer, but the video only covers the chat UI and a one-line API claim.
- **prosharness** (1/3): Claude Code's per-action approval prompts with a do-not-ask-again option are the same surface ProsHarness wraps for phone-driven approvals. → *Compare Claude Code's per-action approval and do-not-ask-again scoping against the phone-approval flow, and confirm which permission classes the harness can pre-approve safely.*

# You're Prompting Opus 5.5 Wrong (Anthropic's Guide to Mastering Opus 5.5)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `5TNXByrtHc4` · [watch](https://youtu.be/5TNXByrtHc4) · **date:** 2026-10-12 · **length:** 6:55 · **format:** tutorial · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Better Stack presenter (unnamed) · **orgs:** Anthropic, Better Stack, OpenAI
- **topics:** claude-code, context-engineering, multi-agent · **tags:** opus-5.5, prompting, claude-md, subagents, tasks-md, long-running-agents, code-review, safeguards, model-switching, fast-mode

> Better Stack walkthrough of Anthropic's Opus 5.5 prompting guide: state the finish line up front, drop "think carefully" lines, steer with CLAUDE.md stop rules, split audits across subagents, track tasks in a file, and handle safeguard flags.

## Summary
The video summarizes Anthropic's guide to prompting Opus 5.5 for long-running work. The core advice is to give the whole task in one message, state what "done" means, and let the model run without staged hand-holding. It recommends deleting "think carefully" or "think step by step" lines because the model already decides how much to think, and it says specific banned-style lists work better than vague "avoid generic design" instructions. For steering, it suggests typing follow-ups mid-run (they are read after the current step) rather than interrupting, and adding a CLAUDE.md rule like "keep going unless you need me, or it's destructive" to reduce unwanted stops. For big audits or migrations it suggests sub-agents with evidence checks, plus a tasks.md file that survives context summarization. It ends runs with blocked-on-me, changed and found headings, and suggests a review pass limited to merge-blocking issues. The video also covers Opus 5.5 safeguard flags that can switch models, with advice to rephrase, state the work is on your own codebase, avoid asking for internal reasoning, and start a new thread after a flag. The presenter partially disagrees on using the same model for review and prefers a different model as reviewer. Content is mostly practitioner tips drawn from a vendor guide, with little independent data.

## Key ideas
- **State the whole task and the finish line in one message, then let it run** — Opus 5.5 is tested on long coding tasks and needs little oversight. Done should be explicit, e.g. every endpoint uses the new client, the old one is deleted, and all tests pass. Adding 'only stop if a test fails for a reason you can't explain' helps it self-recover. ([0:00](https://youtu.be/5TNXByrtHc4?t=0))
- **Delete 'think carefully' and 'think step by step' from prompts and skills** — Opus 5.5 always thinks first and sizes its own thinking. Anthropic reported that removing these lines made replies start sooner with no clear quality drop. Specific finish lines help; vague thinking nudges do little. ([0:50](https://youtu.be/5TNXByrtHc4?t=50))
- **Ban specific design defaults instead of saying 'avoid a generic look'** — Without design direction the model falls back to a few default styles, and 'avoid generic' just swaps one template for another. Naming styles to ban works better, e.g. numbered sections, monospace labels, pill-shaped buttons. ([0:50](https://youtu.be/5TNXByrtHc4?t=50))
- **Type follow-ups mid-run instead of interrupting** — Stopping a run to add something restarts it, which costs more. In Claude Code, typing a follow-up queues it to be read once the current step finishes, without stopping the run. ([2:13](https://youtu.be/5TNXByrtHc4?t=133))
- **Use CLAUDE.md to set when to stop versus keep going** — Opus 5.5 sometimes stops to report progress when it should continue. A rule like 'keep going unless you need me, or unless it's something destructive' reduces full stops while keeping the stops you want. ([2:13](https://youtu.be/5TNXByrtHc4?t=133))
- **Split large audits and migrations across sub-agents, then check each result** — Sub-agents keep each context smaller. The guide has the model verify each sub-agent's evidence before accepting it, which gives a multi-step review. ([2:13](https://youtu.be/5TNXByrtHc4?t=133))
- **Keep a tasks.md file for long runs** — Context summarization can drop original tasks and detail from older turns. A file on disk survives that and lets both the user and the model see what is done and what is left. ([3:29](https://youtu.be/5TNXByrtHc4?t=209))
- **End runs with 'blocked on me / changed / found' and use a merge-blocker-only review** — The final summary should list what the model needs from you first. For review, the guide suggests a pass on the diff listing only problems that would block a merge, each with file, line, why it is wrong, and how to show it fails. One early tester said Opus 5.5 at low effort caught more bugs than Opus 5 at high effort, with fewer false alarms. ([3:29](https://youtu.be/5TNXByrtHc4?t=209))
- **Safeguard flags can silently move you to an older model** — Opus 5.5 is the first Opus with Fable-level bio and cyber safeguards, which can flag legitimate work such as finding vulnerabilities in your own code. Options: Esc twice to edit the last message, reword to sound less suspicious, and state that the work is on your own codebase. Prompts about showing internal reasoning are a known flag trigger. Settings can make Claude ask before switching models. ([4:45](https://youtu.be/5TNXByrtHc4?t=285))
- **Start a new thread after a flag instead of continuing** — The flagged message stays in context, so switching back to Opus 5.5 in the same thread can get flagged again. ([5:49](https://youtu.be/5TNXByrtHc4?t=349))

## Techniques
- **One-message task with explicit finish line** — Give the full task in a single prompt. State what done means as observable conditions (e.g. all endpoints migrated, old client deleted, all tests pass). Optionally add: only stop if a test fails for a reason you cannot explain. *When:* Long-running coding tasks such as migrations or large refactors, where you want the agent to finish without staged check-ins.
- **Remove thinking-nudge lines** — Search your prompts, CLAUDE.md and skills for 'think carefully' / 'think step by step' and delete them. The model decides its own thinking budget. *When:* Prompts and skills written for older models that needed explicit reasoning prompts.
- **Ban specific styles for design** — List concrete styles to avoid (e.g. numbered sections, monospace labels, pill-shaped buttons) rather than writing 'avoid generic design'. *When:* Generating UI or frontend pages where the default output looks templated.
- **Queue follow-ups during a run** — In Claude Code, type the follow-up while the run is active. It is read after the current step ends and the run is not restarted. *When:* You remember something to add mid-run and do not want to restart work.
- **CLAUDE.md stop-rule** — Add a rule such as: keep going unless you need me, or unless it is something destructive. *When:* Opus 5.5 stops to report status mid-task when you want it to proceed.
- **Sub-agent split with evidence check** — For an audit or migration across a large codebase, ask the model to split work across sub-agents and verify each sub-agent's evidence before accepting it. *When:* Large sweeps where a single context would be too big or where you want a second check on claims.
- **tasks.md progress file** — Ask Claude to keep its task list in a file such as tasks.md, updated as it works. *When:* Long runs that may exceed the context window and get summarized.
- **Structured end-of-run summary** — Add a CLAUDE.md rule to end every run with three headings: blocked on me, changed, found. *When:* Long runs, so the actionable items come first.
- **Merge-blocker diff review** — Have the model review a diff before a human does. Report only problems that would block a merge, each with file, line, why it is wrong, and how to reproduce the failure. *When:* Pre-merge review of agent-written changes.
- **Cross-model review** — Have a different model from the implementer do the review and pass its notes back. The presenter uses an OpenAI model for review and feeds the notes to Opus. *When:* When you want less correlated review results than a same-model reviewer gives.
- **Recover from safeguard flags** — Press Esc twice to edit the last message. Reword to sound less suspicious, and state that the work is on your own codebase. Avoid asking for internal reasoning. Start a new thread if the flagged message is still in context. *When:* Opus 5.5 flags legitimate work such as vulnerability analysis of your own code.
- **Answer quickly prompt** — Add a phrase like 'answer quickly' or 'answer directly' to the prompt. The presenter prefers this over the paid fast mode, which uses extra usage. *When:* Simple questions where you want a short reply and not a long run.

## Numbers
- Anthropic's example migration done-criteria: every endpoint uses the new client, the old client is deleted, all tests pass ([0:50](https://youtu.be/5TNXByrtHc4?t=50))
- A tester reports Opus 5.5 at lowest effort caught more bugs than Opus 5 at high effort, with fewer false alarms ([3:29](https://youtu.be/5TNXByrtHc4?t=209))
- Removing thinking-nudge lines made replies start sooner with no clear drop in quality, per Anthropic's testing ([0:50](https://youtu.be/5TNXByrtHc4?t=50))

## Hot takes
- Deleting 'think carefully' lines from prompts and skills, since Opus 5.5 already decides its own thinking budget.
- Banning named design tropes (numbered sections, monospace labels, pill buttons) works better than asking to avoid a generic look.
- Use a different model from the implementer for code review, since same-model reviews give less unique results; the presenter partly disagrees with the guide here.
- Opus 5.5 safeguards can flag legitimate own-codebase security work, and rewording plus a new thread is the practical workaround.

## Tools mentioned
Claude Code, Claude Opus 5.5, CLAUDE.md, tasks.md, OpenAI model (named Astra in transcript)

## Relevance to our work
- **prosharness** (3/3): ProsHarness wraps the Claude Code CLI for long runs, so the finish-line rule, tasks.md checkpointing, end-of-run summary format, and stop-vs-continue CLAUDE.md rule apply directly. → *Add a finish-line field and a blocked-on-me / changed / found summary block to ProsHarness run prompts, and write a tasks.md checkpoint file alongside each run for resume.*
- **agentos** (1/3): Prompting guidance for long-running agents and subagent splits is loosely relevant to AgentOS's agent workflows, but nothing here changes the infra. → *Read the Anthropic Opus 5.5 prompting guide and check whether any of the stop-rule or finish-line patterns apply to AgentOS's internal agent prompts.*

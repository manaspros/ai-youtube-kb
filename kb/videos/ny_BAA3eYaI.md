# Claude Ralph - The Bizarre Anthropic Plugin That Every Developer Is Missing

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `ny_BAA3eYaI` · [watch](https://youtu.be/ny_BAA3eYaI) · **date:** 2026-01-02 · **length:** 4:25 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Better Stack host (not named in transcript) · **orgs:** Anthropic, Better Stack, RepoMirror, Y Combinator (YC hackathon)
- **topics:** claude-code, coding-agents, agent-architecture, token-cost-efficiency · **tags:** ralph, ralph-wiggum, stop-hook, completion-promise, max-iterations, agent-loop, claude-code-plugin, autonomous-agents, cost-control, bun-test, beads, typescript-migration

> Walkthrough of the Ralph Wiggum Claude Code plugin, which re-runs the same prompt through a stop hook until a completion promise appears, with a max-iterations cap as a cost guard.

## Summary
The video explains the "Ralph" technique, a bash loop that feeds an agent the same prompt repeatedly until a clear completion signal appears. Anthropic's Claude Code plugin implements the idea with a /ralph slash command, a state file, and the Claude Code stop hook instead of a bash loop. The presenter demos converting a Python audio-delay script to TypeScript, with the prompt file telling the agent to write and run passing tests. He stresses a max-iterations flag to avoid runaway cost on expensive models like Opus. The claimed results (a $300 MVP, six repos shipped overnight, a new language) are anecdotes repeated from a talk and a hackathon, not measurements from the video. Practical limits are clear completion criteria, incremental steps, and no use for tasks that need human judgment. The video is short (4:25) and light on detail, but the mechanism and guardrails are concrete.

## Key ideas
- **Ralph is an infinite loop that re-sends the same prompt to a coding agent until the task is done** — Originated with Geoffrey Huntley (transcript spells it Jeffrey). The loop is a bash while-loop: give the agent a prompt, wait for the response, send the identical prompt again. It works only if the task has clear completion criteria and a completion signal, so it can run overnight. ([0:00](https://youtu.be/ny_BAA3eYaI?t=0))
- **The Anthropic plugin replaces the bash loop with a stop hook and a state file** — Starting /ralph writes a state file holding the prompt, the completion promise (e.g. 'complete' or 'done') and an optional max-iteration count. Each time Claude Code finishes a turn, the stop hook reads the state file and the latest output. If the completion promise is missing, it re-triggers the same prompt, and Claude revisits its own previous code. ([1:15](https://youtu.be/ny_BAA3eYaI?t=75))
- **Headline results cited are anecdotes from a talk and a hackathon** — An engineer reportedly delivered, reviewed and tested an MVP with many agents for under $300, versus about $50,000 quoted for a contractor. A RepoMirror team reportedly shipped six repos overnight at a YC hackathon, including a Python-to-TypeScript rewrite of browser-use. Someone also reportedly built a new programming language in under three months. The video presents these without measuring them. ([1:15](https://youtu.be/ny_BAA3eYaI?t=75))
- **Demo: Python-to-TypeScript migration gated by tests written into a prompt file** — The presenter's prompt.md asks the agent to write passing tests. The completion promise is 'done'. The result was a TypeScript version of an audio-delay script, with tests run via bun test. The prompt file doubles as the spec the loop re-reads each iteration. ([2:23](https://youtu.be/ny_BAA3eYaI?t=143))
- **Max iterations is the cost guard for expensive models** — Ralph re-runs the prompt every time the stop hook fires, so cost grows with iterations. The max-iterations setting increments on each hook trigger and stops the loop at the chosen number. The presenter says this matters most with API pricing and models like Opus. The video does not measure the actual cost of the demo run. ([3:44](https://youtu.be/ny_BAA3eYaI?t=224))
- **Ralph works only for tasks with testable completion criteria, not for judgment calls** — Vague goals like 'make it good' or 'make it pretty' will not terminate cleanly. Complex work should be split into incremental steps. Tasks needing human judgment should be avoided. The presenter suggests pairing Ralph with beads to keep incremental steps on track, but does not demo this. ([3:44](https://youtu.be/ny_BAA3eYaI?t=224))

## Techniques
- **Ralph-style re-prompt loop (manual)** — Write one prompt that states the task, testable completion criteria, and a completion signal such as the word 'done'. Run the agent, check whether the signal appeared, and if not, resend the identical prompt. Let the agent read its own prior output and code on each pass. *When:* Long, well-specified, mechanically verifiable tasks such as ports or migrations with a test suite, especially overnight runs where the agent tends to give up early.
- **Ralph Claude Code plugin with stop hook** — Invoke the /ralph slash command with the task prompt, a completion promise (for example 'done' or 'complete'), and a max-iterations value. The plugin stores this in a state file. The Claude Code stop hook checks the state file and last output on each stop, and re-triggers the prompt unless the completion promise is present or the iteration cap is reached. The video does not show exact flag names. *When:* Interactive Claude Code sessions where you want the agent to keep going until a test or completion condition is met, without a separate bash process.
- **Iteration cap as a spend limit** — Always set the max-iterations value before running Ralph on a metered or expensive model. Choose the number from a rough per-iteration cost estimate multiplied by your budget. *When:* API-priced usage or expensive models like Opus, where an unbounded loop could produce a large bill.
- **Tests in the prompt file as the completion gate** — Keep the task in a prompt.md file. Include an instruction to write tests and run them until they pass, and make the completion promise appear only after the tests pass. The demo used bun test for a TypeScript port. *When:* Code migrations or rewrites where 'done' should mean verified behavior rather than the agent claiming it is finished.
- **Decompose before looping** — Break a large goal into small, ordered, individually checkable steps before starting the loop. The presenter suggests tracking these with beads. *When:* Any task bigger than one clear deliverable, so each loop iteration has a reachable, testable goal.

## Numbers
- Engineer reportedly delivered an MVP (build, review, test with many agents) for under $300 ([1:15](https://youtu.be/ny_BAA3eYaI?t=75))
- Quoted contractor cost for the same MVP: about $50,000 ([1:15](https://youtu.be/ny_BAA3eYaI?t=75))
- RepoMirror team reportedly shipped six repos overnight at a YC hackathon ([1:15](https://youtu.be/ny_BAA3eYaI?t=75))
- A new programming language reportedly built from scratch in under three months ([1:15](https://youtu.be/ny_BAA3eYaI?t=75))
- Video length 4:25; demo is shown in fast-forward, so no timing or cost is measured ([2:23](https://youtu.be/ny_BAA3eYaI?t=143))

## Hot takes
- The title's 'every developer is missing' framing oversells a short walkthrough. The substance is the stop-hook gate, the completion promise, and the iteration cap.
- The $300 vs $50,000 and overnight-shipping claims are secondhand anecdotes, not verified results, and the video does not measure the demo's own cost.
- The presenter's view that Ralph should not be used for judgment-based tasks is the most useful caveat in the video.

## Tools mentioned
Claude Code, Ralph Wiggum plugin (Anthropic Claude Code plugin, /ralph command), Claude Code stop hook, AMP (agent named as a comparison; no details given), bun test (Bun test runner), beads (suggested pairing, not demonstrated), TypeScript, Python

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI and already handles loops and schedules. Ralph's stop-hook re-prompt with a completion-promise gate and an iteration cap is a close pattern to compare against. → *Compare ProsHarness loop design with Ralph's stop-hook and state-file approach, and evaluate adding a completion-promise check plus max-iteration cap before any re-prompt of a Claude Code run.*
- **agentos** (1/3): A per-loop iteration cap is a simple budget primitive. It is adjacent to AgentOS L1 budgets but does not change the design. → *Consider whether AgentOS Scout budgets should cap retry or loop iterations per run, and compare that to the Ralph max-iterations approach.*

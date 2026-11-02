# Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `ZpK5PWX2YRM` · [watch](https://youtu.be/ZpK5PWX2YRM) · **date:** 2026-07-18 · **length:** 21:35 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Alex Volkov · **orgs:** ThursdAI, Weights & Biases, CoreWeave, OpenAI, Anthropic, GitHub, METR, Google
- **topics:** pr-code-review, testing-verification, coding-agents, software-factory · **tags:** code-review, human-in-the-loop, risk-based-review, agent-generated-code, loops, verification, writer-reviewer-separation, decomposition, review-bottleneck, z-l-continuum, claude-code, codex, pi, openclaw

> Alex Volkov on the "Z/L continuum" for how much agent-written code engineers should read in 2026: route review effort by the proof a change needs, not by a blanket rule.

## Summary
Alex Volkov (ThursdAI) frames the 2026 debate about reading agent-written code as a continuum between two AI Engineer EU talks: Ryan Lopopolo (OpenAI), who says code is free and the prompts and guardrails matter, and Mario Zechner (creator of Pi), who says read every line of critical code. He corrects his own framing: the continuum is about the task, not the person, so one engineer may need different proof for different changes. He cites 2026 survey data showing output rising faster than review quality (more incidents and bugs per PR, more PRs merged without review), and an Anthropic essay saying human review has become the bottleneck. His proposed routing table sends auth, money movement, permissions and irreversible data changes to a human reading every line, while other changes get lighter proof. Other advice: split work into small reviewable PRs, keep the writer separate from the inspector and test author, and turn repeated review findings into docs and lint rules. He ends with loops (scheduled self-verifying agent runs) and warns that a builder grading its own work does not remove the review. The talk is mostly opinion and anecdote, with a few useful frames and some stats whose sources are not clearly named.

## Key ideas
- **The useful question is what proof a specific change needs, not whether to read code in general.** — The speaker says 'should I still read code in 2026?' is the wrong question. The better one is 'what proof does this specific change need?' Review effort should follow the risk of the change. ([14:04](https://youtu.be/ZpK5PWX2YRM?t=844))
- **The continuum is about the task, not the person.** — His correction: the same engineer can go Lopopolo-style on low-stakes code and Zechner-style on critical code. Different tasks need different proof. ([11:06](https://youtu.be/ZpK5PWX2YRM?t=666))
- **Route review by risk. Critical paths get a human reading every line.** — Auth, money movement, permissions and irreversible data should be read line by line by a person. Other code can be lighter, with checks chosen to match the risk. Agents can help point to which code is critical in a large repo. ([14:04](https://youtu.be/ZpK5PWX2YRM?t=844))
- **Output has outrun review, and quality is paying for it.** — He cites 2026 survey data: more code deleted per PR, more PRs merged with no review, many more incidents per PR, and more bugs per developer. He also points to Anthropic's own status page as an example that speed does not guarantee stability. ([8:28](https://youtu.be/ZpK5PWX2YRM?t=508))
- **Fix a repeated mistake once in the system, not once per PR.** — Humans are bad at catching the same mistake again and again. A reviewer should record the finding once, in docs, a linter, or a reviewer rule, so the system catches it next time. The point is to inspect the system, not every line. ([15:27](https://youtu.be/ZpK5PWX2YRM?t=927))
- **The agent that writes the code should not be the one that checks it.** — If the same agent writes the code, writes the tests and judges the output, it is like grading your own exam. Keep the writer, the reviewer and the test author separate. ([14:04](https://youtu.be/ZpK5PWX2YRM?t=844))
- **Loops are scheduled agents that verify themselves, and self-verification does not remove review.** — A loop finds a task, writes a prompt, runs a plan, verifies the result, and retries if it fails. But if the builder is also the grader, the review step has only moved. Automation raises the stakes on where human judgment goes. ([19:21](https://youtu.be/ZpK5PWX2YRM?t=1161))

## Techniques
- **Risk-tiered review routing** — Sort every change into a tier. Auth, money movement, permissions and irreversible data changes get a human line-by-line read. Other changes get proof suited to their risk, such as tests, traces, evals or shadow mode. *When:* When agent output volume is too high to read everything, but some code paths can still cause serious harm.
- **Decompose into atomic PRs with agents** — Ask an agent to split a large change into small, reviewable PRs before review starts. Each piece should be small enough to read properly. *When:* When a PR is too long and reviewers start to skim.
- **Separate writer, inspector and test author** — Do not let one agent write the code, review it and write its tests. Use a different agent or a fresh context for the inspection and the tests. *When:* Any time agent-written code is checked by the same agent that wrote it.
- **Turn review findings into system rules** — When a reviewer catches a repeated mistake, record it once as documentation, a lint rule or a reviewer instruction so the system catches it in future runs. *When:* When the same class of bug keeps reappearing in agent PRs.
- **Ask the agent where the critical code is** — In a large repo, ask an agent to point out critical primitives or code areas, and use its answer to decide where human reading should go. *When:* When you need to decide what to read carefully in a codebase you do not fully know.
- **Loops with verification and retry** — Run scheduled agent jobs that discover a task, plan it, execute it, verify the result and retry on failure. The speaker says the verification must come from something other than the builder. *When:* For recurring, well-defined maintenance work where success can be checked automatically.

## Numbers
- METR: models first completed tasks that would take engineers over 16 hours, and the trend has risen since. ([1:12](https://youtu.be/ZpK5PWX2YRM?t=72))
- Anthropic: about 80% of its code is now AI-written (a stat the speaker says is a few months old); Boris Cherny's code is 100% AI-written. ([2:11](https://youtu.be/ZpK5PWX2YRM?t=131))
- GitHub is on track for about 14 billion commits in 2026, against about 1 billion in all of 2025 (14x). ([2:11](https://youtu.be/ZpK5PWX2YRM?t=131))
- Survey of 22,000 engineers (April 2026, cited as the 'acceleration whiplash' study): +861% code deleted per PR. ([8:28](https://youtu.be/ZpK5PWX2YRM?t=508))
- Anthropic says it ships about 8x more code per quarter than in 2025. ([8:28](https://youtu.be/ZpK5PWX2YRM?t=508))
- Same study: 31% increase in PRs merged with no review, human or agent. ([9:50](https://youtu.be/ZpK5PWX2YRM?t=590))
- Same study: 242% increase in incidents per PR. ([9:50](https://youtu.be/ZpK5PWX2YRM?t=590))
- Bugs per developer are up about 6x compared with 2025. ([9:50](https://youtu.be/ZpK5PWX2YRM?t=590))
- AI Engineer World's Fair: about 7,000 attendees, 36 tracks, roughly 3x last year's size. ([2:11](https://youtu.be/ZpK5PWX2YRM?t=131))

## Hot takes
- Code is cheap, but attention is not. The bottleneck has moved to human judgment and review.
- The review layer moves over time: from reading outputs, to directing tasks, to inspecting loops. Capability growth does not remove the need for proof.
- A builder grading its own loop output has not removed review, only moved it.
- Not every line in 2026 needs your eyes. Every system still needs your judgment.

## Tools mentioned
Claude Code, Codex, OpenClaw, Pi, Antigravity, Grok Code

## Relevance to our work
- **prosharness** (2/3): ProsHarness already runs plan, critique (Codex) and debate, and has loops and phone approvals. The talk's advice to split writer from verifier and to route critical changes to a human fits that design, but it adds no new mechanism. → *Add a risk tier to the ProsHarness plan step: changes touching auth, money, permissions or irreversible data always go to the phone-approval gate, and other changes proceed after an independent verifier pass. Check that the verifier never shares context with the builder.*
- **general** (2/3): Turning repeated review findings into docs, lint rules and reviewer instructions connects to the context-engineering interest in CLAUDE.md and AGENTS.md. It also gives a way to measure review quality over time. → *Track repeated review findings in one list for a repo, and convert the top recurring ones into CLAUDE.md rules or lint checks. Count how often each one recurs.*
- **agentos** (1/3): The talk's loop and verification points are general engineering advice, not infrastructure. The only overlap is the idea that self-verifying loops need an outside check. → *When designing AgentOS SkillForge or EvolveCraft loops, require verification from a separate evaluator and not from the agent that produced the change.*

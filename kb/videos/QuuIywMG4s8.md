# Evals Are Broken, Use Them Anyway — Ara Khan, Cline

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `QuuIywMG4s8` · [watch](https://youtu.be/QuuIywMG4s8) · **date:** 2026-06-18 · **length:** 19:04 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Ara Khan · **orgs:** Cline, Stanford University, Laude Institute, OpenAI, Harbor, Daytona, Modal, Epoch AI
- **topics:** evals, testing-verification, coding-agents · **tags:** evals, terminal-bench, hill-climbing, vibe-check, harness-testing, failure-triage, coding-agent, benchmark-saturation, swe-bench

> Ara Khan (Cline) argues most people misuse evals, either trusting vendor leaderboards or dismissing evals for vibes, and shows how to build a Terminal-Bench-style agent eval and hill-climb on it alongside a vibe check.

## Summary
Ara Khan of Cline argues that most people are wrong about evals in one of two directions: they treat leaderboard numbers as fact, or they dismiss evals in favour of vibes. He gives three levels of eval use (use others' evals, use evals to improve your own agent, build your own) and says he will cover only the first two. His heuristics are to distrust vendor-reported numbers, let new models sit for a couple of weeks before switching, and prefer recent, precise evals because older ones like SWE-bench Verified no longer track frontier coding work. Cline built its own coding evals from opted-in user sessions, but found agent tasks hard to grade because the agent takes many steps and the end state matters. They adopted Terminal-Bench (89 tasks run through Harbor in isolated parallel VMs) and used a loop of run, triage failing traces with an agent, fix small levers, and re-run. A low score can come from the model, the harness, or a badly posed task, and fixes fall into obvious bugs, nuanced per-model prompting, and overfitting, which is the danger zone. The talk closes by saying to hill-climb on a benchmark while also passing a vibe check on the product.

## Key ideas
- **Two ways to be wrong about evals: trusting objective leaderboard numbers as truth, or dismissing evals and judging only by vibes.** — The speaker says vendor-reported numbers are approximations that often don't hold up in real use. Pure taste is also not enough. The right stance is in between. ([1:04](https://youtu.be/QuuIywMG4s8?t=64))
- **Use evals in three stages: borrow others' evals, use evals to improve your own agent, then build your own. The talk only covers the first two.** — Stage one is reading public evals with judgment. Stage two is hill-climbing your own agent on a suite. Stage three, building domain-specific evals, is left out for time. ([1:04](https://youtu.be/QuuIywMG4s8?t=64))
- **Let new models sit for a couple of weeks before switching to them.** — Frontier models change every few months. Waiting lets early problems surface, so the speaker's advice is to adopt once a model has held up, not to chase the cutting edge. ([3:57](https://youtu.be/QuuIywMG4s8?t=237))
- **Old standard benchmarks saturate or stop measuring what matters, so look for newer, precise evals.** — The speaker cites an OpenAI post saying SWE-bench Verified no longer measures frontier coding capability. He says it contains toy problems that do not reflect real software engineering. ([5:20](https://youtu.be/QuuIywMG4s8?t=320))
- **Agent evals are hard to grade because the agent takes many steps, so the end state has to be checked, not one answer.** — A single-turn question has a short, checkable answer. An agent that installs packages, reads docs, runs scripts and tests has a huge space of paths. The team had to check whether the task worked and whether it broke anything else. ([9:15](https://youtu.be/QuuIywMG4s8?t=555))
- **Build a dataset from real usage and clean it by hand, then use an existing benchmark as a standard to compare against.** — Cline paid opted-in users and mined their coding sessions for realistic problems. They then cleaned those tasks manually so they were solvable. They also used Terminal-Bench as an outside standard. ([7:57](https://youtu.be/QuuIywMG4s8?t=477))
- **Each eval task runs in its own isolated machine in parallel, so total run time equals the slowest task.** — Harbor sets up a standard Linux box per task, with the repo and agent installed, and runs all tasks at once. Runs take minutes, and some tasks take 30 to 40 minutes. ([10:15](https://youtu.be/QuuIywMG4s8?t=615))
- **A failing score is a triage problem: test the model, the harness and the task separately.** — A strong model can hide a weak harness, and a good harness can hide a weak model. Some tasks may also be unfair. The speaker says to check which of these caused a failure before changing anything. ([12:47](https://youtu.be/QuuIywMG4s8?t=767))
- **Improvements come in three zones: obvious bugs, nuanced per-model prompting, and overfitting.** — Zone one is bugs and rate limits. Zone two is tuning prompts and thinking settings per model family, since techniques that work for one family may fail for another. Zone three is gaming the score, which the speaker warns against. ([14:54](https://youtu.be/QuuIywMG4s8?t=894))

## Techniques
- **Failure-trace triage loop** — Run the full eval suite and record the score. Pass the failing tasks' full traces (every LLM call) to another agent, which groups failures by cause (e.g. a test was never run, a file-read tool was broken). Then pick the small fixes that recover the most failures. *When:* After each eval run, when you have many failures and need to decide what to change next.
- **Isolated parallel eval runs** — Define each task as a standard Linux environment with the repo, your agent CLI and fixed CPU/RAM/timeouts. Run all tasks in parallel on cloud sandboxes or containers (Harbor with a sandbox provider is the example given). *When:* When a benchmark has many independent tasks and sequential runs would be too slow, or when you need repeatable environments.
- **Hill-climb with a vibe check** — Improve the harness against the eval score, but only keep changes that also feel good in daily use with the actual product and model. Do not rely on either signal alone. *When:* When tuning a coding agent or harness over many iterations.
- **Sort fixes into three zones** — Fix obvious bugs first (caching bugs, rate limits). Then make model-specific nuanced changes (prompt style, thinking budget) and check each model family separately. Treat large score jumps from gaming the benchmark as suspect. *When:* When deciding which harness changes are real improvements and which are overfitting.
- **Delayed model adoption** — Wait a couple of weeks after a new model release, see whether it holds up in the community and your own tests, then switch. *When:* When deciding whether to move your agent to a newly released model.
- **Check the task itself** — Before trusting a score, confirm the tasks are sane, realistic and solvable. Hand-clean any data taken from user sessions. *When:* When building or adopting an eval suite, before drawing conclusions from it.

## Numbers
- Terminal-Bench suite has 89 coding tasks (race conditions, database issues, infra debugging). ([10:15](https://youtu.be/QuuIywMG4s8?t=615))
- Some Terminal-Bench tasks take 30 to 40 minutes each, and a full run is parallelised so total time is set by the slowest task. ([10:15](https://youtu.be/QuuIywMG4s8?t=615))
- Cline's internal harness score started at about 43% before fixes to container CPU/memory, timeouts and thinking behaviour. ([14:54](https://youtu.be/QuuIywMG4s8?t=894))
- Speaker's example triage: 50 failures out of 89 tasks in one run, which are then grouped by cause. ([12:47](https://youtu.be/QuuIywMG4s8?t=767))
- Frontier models change roughly every couple of months (Epoch index cited). ([3:57](https://youtu.be/QuuIywMG4s8?t=237))

## Hot takes
- Don't believe model vendors' eval numbers; they are approximations.
- Most AI researchers and engineers dismiss evals and treat them as an approximation, not a ground truth.
- SWE-bench Verified is no longer a useful measure of frontier coding ability.
- Wait a couple of weeks after a model release before switching to it.
- Overfitting an eval to get a high score and then posting it is the danger zone, and he advises against it.

## Tools mentioned
Terminal-Bench, Harbor, SWE-bench Verified, Claude Code, Codex, Daytona, Docker, Modal

## Relevance to our work
- **agentos** (2/3): AgentOS has RAGAS evals for retrieval, but no end-to-end task suite for agent behaviour. The talk's model of isolated task runs, end-state grading and trace triage fits the agent-side evals AgentOS lacks. → *Sketch a small Terminal-Bench-style task suite for one AgentOS flow (for example a Crucible exec task). Grade end state, not single replies, and record per-task traces for triage.*
- **prosharness** (2/3): ProsHarness wraps Claude Code CLI. The talk's point that a score reflects the model, the harness and the task at once maps directly onto testing ProsHarness changes. → *Build a fixed task set and run it with raw Claude Code and with ProsHarness, so harness changes (checkpoint, plan/critique loop) are measured separately from model changes. Read the Terminal-Bench / Harbor setup first.*
- **general** (2/3): Practical, concrete advice on evals for coding agents, including failure triage, parallel isolated runs and the guard against overfitting. It applies to any agent work the team does. → *Read the Terminal-Bench task format and the Harbor runner docs before writing any new agent eval, and copy the triage-by-agent step into the eval loop.*

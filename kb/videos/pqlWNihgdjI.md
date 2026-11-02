# From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `pqlWNihgdjI` · [watch](https://youtu.be/pqlWNihgdjI) · **date:** 2026-09-18 · **length:** 20:57 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Clare Liguori · **orgs:** AWS, Amazon
- **topics:** enterprise-adoption, coding-agents, context-engineering, testing-verification · **tags:** frontier-development, kiro, productivity, steering-files, spec-driven, shift-left-testing, mock-services, agent-habits, org-change, decision-bottleneck, burnout, deployment-velocity

> Amazon's frontier-dev habits from AWS's Clare Liguori: teams that changed how they worked (context files, self-validating agents, spec-first, local tests) hit a 4.5x median in deployment velocity; tool-only teams got under 3x.

## Summary
Clare Liguori (AWS, works on Kiro) argues that Amazon's large productivity gains from coding agents come from changing how engineers work, not from the tools alone. She describes "frontier developers" who write 1-2% of code by hand, run agents for hours, and keep several agents busy in parallel. Pilots are cited: a six-person Bedrock team rebuilt an inference data plane in 76 days, a Prime Video sprint cut a 90-week estimate to 24, and a 50-team Amazon Stores pilot found that teams who changed their habits reached a median 4.5x deployment-velocity gain while the rest stayed under 3x. She stresses that the first two examples were unusually expert or heavily prepared teams, so they do not generalise by themselves. She lays out five habits: invest in agent context, slow down to speed up, feed agents rather than babysit them, make intent explicit, and shift testing left with fast local feedback. She also flags risks: burnout from parallel agents, review load on early-career engineers, leaders who expect speed too early, and decision-making that becomes the new bottleneck. The talk is a practitioner account from a team with a vendor stake in Kiro, and the metrics are internal and unverified.

## Key ideas
- **Step-change gains come from changing the way of working, not from the tool** — In an Amazon Stores pilot of 50 ordinary teams, about half got under 3x and the others a median 4.5x (sometimes over 10x) on deployment velocity. ~90% of the teams used Kiro, so the split was about how they worked, not which tools they had. ([5:00](https://youtu.be/pqlWNihgdjI?t=300))
- **Frontier developers write very little code by hand and keep agents running** — Frontier developers hand-write about 1-2% of their code, let agents run for hours unattended, and run several agents in parallel to keep their backlog moving. The speaker says she personally felt only 10-20% gains from earlier phases (inline completion, chat, vibe coding). ([1:22](https://youtu.be/pqlWNihgdjI?t=82))
- **Showcase results came from expert or heavily prepared teams, so they do not transfer by default** — The Bedrock Mantle team (six people, 76 days, estimated at 30 people over 18 months) was made of top distributed-systems and LLM engineers. The Prime Video sprint had six engineers with no on-call duty, and a senior engineer had spent three weeks writing small, detailed tasks beforehand. ([2:33](https://youtu.be/pqlWNihgdjI?t=153))
- **Habit 1: agent context must be written down, and pruned as models improve** — Tacit knowledge that usually lives in Slack, mentors, reviews and standups has to go into skills and steering files. Each time the agent does something the engineer would not, the fix is a context-file rule. Older models needed many 'do not' lines (Sonnet 3.7); newer ones need fewer, so each rule should be re-checked for bloat. ([8:26](https://youtu.be/pqlWNihgdjI?t=506))
- **Habit 2: productivity dips at first, so slow down to speed up** — Nearly every interviewed team got slower when it adopted the new way of working. They first improved the codebase: better error messages, new MCP servers, restructured code so agents can navigate it, and in some cases a move to typed languages (TypeScript, Rust) that give the agent compiler feedback. ([9:42](https://youtu.be/pqlWNihgdjI?t=582))
- **Habit 3: feed agents what to build and how to check it, instead of babysitting** — Babysitting means waiting 30-60 seconds for each reply, which blocks parallel work. Feeding means giving the agent the goal and the self-check bar (it must compile, pass tests, reach coverage), so it returns only when the bar is met. The next step is to put that in steering so it happens without a prompt. ([11:44](https://youtu.be/pqlWNihgdjI?t=704))
- **Habit 4: make intent explicit with a spec before code** — Vibe coding often means many rounds of rework when the intent was wrong. Amazon teams write a spec first, and Kiro can generate it. Iterating on a spec document is much cheaper than iterating on code spread across a codebase. ([13:00](https://youtu.be/pqlWNihgdjI?t=780))
- **Habit 5: shift testing left and give agents a fast local feedback loop** — Linters, unit, integration, performance and security tests now have enough ROI to invest in. Teams also replace live cloud services with deterministic local mocks, so the agent gets many more loops per hour. The speaker says fast feedback is what lets agents run for hours and correct themselves. ([13:57](https://youtu.be/pqlWNihgdjI?t=837))
- **The new bottleneck is decisions and launch reviews, not writing code** — Code that used to take 9-12 months to build now takes 1-2 months, so the time spent deciding to build and approving the launch dominates. The speaker says frontier teams often spend more time on decisions than on code, and advises making fast, easily reversible decisions. ([18:12](https://youtu.be/pqlWNihgdjI?t=1092))

## Techniques
- **Living steering/skills file with a rule per agent mistake** — Each time the agent misses something, add the missing rule to the steering or skills file. Re-audit the file after every model upgrade and delete rules the new model no longer needs. *When:* Brownfield codebases where team knowledge is tacit and models change often.
- **Self-validating agent loop** — Put the build, lint, test and coverage commands, plus a clear pass bar, in the task or steering. The agent iterates on its own and returns to the human only when the bar is met. *When:* Any long or unattended agent run, so the human reviews only finished work.
- **Spec-first iteration** — Have the agent write a spec or design doc, review and iterate on that document with the human, and only then generate code. *When:* Ambiguous or complex features where wrong intent is costly to fix in code.
- **Local deterministic mock services** — Replace live cloud dependencies with local mocks that return fixed responses, so tests and agent loops run on the laptop with no network calls. *When:* Integration-heavy systems where agents need fast feedback and cannot wait on shared services.
- **Agent-friendly language and error design** — Move to typed languages with strong compiler errors where possible, and improve tool and error messages so the model can see what failed. *When:* Legacy code where agents guess because the language gives no compile-time signal.
- **Deployment velocity as the productivity metric** — Measure how fast changes reach customers, not commit counts, and compare teams on that basis. *When:* Evaluating whether agent tooling actually speeds up delivery.
- **Decision-speed audit** — Find where launch and build decisions wait longest, and shorten the approval path for reversible decisions. *When:* After coding speeds up and review or approval becomes the slowest step.

## Numbers
- Median productivity gain of 4.5x (sometimes over 10x) for Amazon pilot teams, measured as deployment velocity to production ([1:22](https://youtu.be/pqlWNihgdjI?t=82))
- Teams that changed their way of working reached 4.5x median; teams that only sprinkled tools on top stayed under 3x (50-team Amazon Stores pilot, roughly 90% using Kiro) ([5:00](https://youtu.be/pqlWNihgdjI?t=300))
- Speaker's own felt productivity from earlier AI phases was about 10-20% ([0:12](https://youtu.be/pqlWNihgdjI?t=12))
- Frontier developers hand-write about 1-2% of the code they produce ([1:22](https://youtu.be/pqlWNihgdjI?t=82))
- Bedrock Mantle team: six people, built a new inference data plane in 76 days with Kiro; estimate had been 30 people over 18 months; the talk cites up to 20x improvement ([2:33](https://youtu.be/pqlWNihgdjI?t=153))
- Prime Video 10-day sprint with six engineers cut the project delivery estimate from 90 weeks to 24 weeks ([3:50](https://youtu.be/pqlWNihgdjI?t=230))
- Amazon plans to scale the approach from about 50 pilot teams to the next 2,000 teams in 2026 ([18:12](https://youtu.be/pqlWNihgdjI?t=1092))
- Product builds used to take 9-12 months; with agents, code takes 1-2 months, so decision and launch-review time becomes the critical path ([18:12](https://youtu.be/pqlWNihgdjI?t=1092))

## Hot takes
- Teams that just add AI tools get under 3x; the 4.5x comes from changing how the team works.
- Rolling out frontier practices to every team at once is a mistake; slow down to speed up.
- Decision-making and launch approval, not coding, are now the main bottleneck.
- Early-career engineers struggle more with reviewing AI output than with writing it.
- Showcase results like the 76-day rebuild came from unusually expert teams and do not generalise by default.

## Tools mentioned
Kiro, MCP servers, Bedrock, TypeScript, Rust

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code with checkpoint/resume, plan-critique-debate and loops. The talk's self-validating loop, steering-file audits and spec-first habit map directly onto those parts. → *Add a per-task done gate in ProsHarness that runs build, lint and tests and returns to the human only when they pass, and record which steering rules each run used so they can be pruned after model upgrades.*
- **general** (1/3): Useful as a checklist for adopting coding agents in any team, and it reframes productivity around deployment velocity instead of commits. → *Measure any agent-tooling claim by deployment velocity (changes reaching users) rather than commit count, and compare teams with the same metric.*

# AI passed every benchmark… then failed at real work

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `7s2IIIP47GM` · [watch](https://youtu.be/7s2IIIP47GM) · **date:** 2026-07-02 · **length:** 5:03 · **format:** other · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** MIT, Cursor, GitHub Copilot, Google (Gemini CLI), Anthropic (Claude Code)
- **topics:** evals, coding-agents, enterprise-adoption · **tags:** benchmarks-vs-real-work, silent-failures, human-in-the-loop, ai-roi, hype-critique, opinion

> Opinion piece arguing AI coding tools look strong on benchmarks but fail on open-ended, underspecified real work, and that failures are quiet. Recommends measuring shipped outcomes and keeping humans on costly decisions.

## Summary
The host argues that AI tools score well on benchmarks but underperform on real engineering work, which is open-ended, under-documented and full of conflicting requirements. He cites a 2025 MIT report, as he describes it, of more than 300 enterprises that spent over $30B on AI, with 95% reporting no measurable revenue or ROI impact. He claims benchmarks are closed problems with clean code, known answers and no ambiguity, while real work is the opposite. He says coding tools (Claude Code, Copilot, Gemini CLI) handle perfect specs well but break on spec gaps and integration with existing systems. The main risk he describes is silent failure: output that compiles, passes the linter and looks correct but does the wrong thing at scale, and only surfaces in production. He closes with three recommendations: measure tools by whether work shipped and worked, keep humans in the loop where errors are expensive (co-pilot, not captain), and stop using leaderboard scores as purchasing criteria. The video offers no new data of its own and rests almost entirely on one secondhand statistic.

## Key ideas
- **Hype framing and a cited ROI failure rate** — Opens with sweeping vendor claims, then cites a 2025 MIT report (as the host describes it): 300+ enterprises, over $30B spent on AI, 95% with zero measurable revenue or ROI impact. Secondhand, not checked in the video. ([0:00](https://youtu.be/7s2IIIP47GM?t=0))
- **Benchmarks are closed problems; real work is open-ended** — Benchmarks give a clear problem, a clean codebase and a known correct answer. Real work has half-documented legacy code, stale requirements, conflicting threads and missed deadlines. The gap between benchmark and real performance is large, per the host. ([1:14](https://youtu.be/7s2IIIP47GM?t=74))
- **Coding tools fail on spec gaps and real integrations** — Claude Code is strong given a perfect spec but falls apart when specs have gaps, which the host says is every human-written spec. Copilot autocompletes confidently but often wrongly. Gemini CLI builds working apps from scratch that break when they meet real systems. ([2:32](https://youtu.be/7s2IIIP47GM?t=152))
- **The core risk is silent failure** — AI-written code can compile, pass the linter and look correct while doing the wrong thing at scale. Standard PR review often misses this, so teams may not see the failure until production. ([2:32](https://youtu.be/7s2IIIP47GM?t=152))
- **Three recommendations** — (1) Judge tools by whether work shipped and worked, not demo impressiveness. (2) Keep humans in the loop wherever being wrong is expensive: AI as co-pilot, not captain. (3) Stop treating leaderboard scores as purchasing criteria, since they reflect controlled tests, not your codebase. ([3:52](https://youtu.be/7s2IIIP47GM?t=232))

## Techniques
- **Outcome-based tool evaluation** — Measure AI tools on whether the change shipped and behaved correctly in production, not on demo quality or leaderboard scores. The host gives no concrete metric or setup. *When:* Choosing or justifying a coding-agent tool, or assessing whether an AI rollout is paying off.
- **Human gating by cost of error** — Keep humans as approvers on steps where a wrong result is expensive, and let the AI run freely elsewhere. The host frames this as co-pilot, not captain. *When:* Deciding which agent actions need review before they run, such as production changes, data writes or spending.
- **Evaluate on your own codebase and problems** — Treat public benchmark results as a weak signal and test tools on your own repos and realistic, under-specified tasks. The host argues this is the only test that predicts real performance. *When:* Before adopting a tool or model for a team's actual work.

## Numbers
- MIT 2025 report, as cited: 300+ enterprises, over $30B spent on AI, 95% reported zero measurable revenue or ROI impact. Secondhand figure, not verified in the video. ([0:00](https://youtu.be/7s2IIIP47GM?t=0))
- Cursor scores 87% on an unnamed "software engineering benchmark" (speaker's figure, not sourced). ([1:14](https://youtu.be/7s2IIIP47GM?t=74))

## Hot takes
- The benchmark-vs-reality framing is a fair critique, but the video offers no new data. Its evidence is one secondhand MIT statistic and anecdotes.
- The claim that AI tools 'fail quietly' is asserted with no concrete example or failure rate.
- The title and opening ('97% on the Trust Me Bro benchmarks') are hype-driven. Content is opinion with thin substance, so quality is capped at 2.

## Tools mentioned
Claude Code (transcript says "Clawed code"), GitHub Copilot, Gemini CLI, Cursor

## Relevance to our work
- **agentos** (1/3): The benchmark-vs-real-work argument supports prove-it-with-correctness-checks, but the video gives no method. → *Build eval tasks from messy, under-specified real repo work rather than clean benchmark-style problems, and score outcomes on whether the change works.*
- **prosharness** (1/3): Human approval on expensive-to-be-wrong steps matches ProsHarness's phone-driven approvals. → *Route only high-cost actions (e.g. production writes, large spend) to the phone-approval path and let low-risk steps run unattended.*

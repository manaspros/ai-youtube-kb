# Why Humans Can't Keep Up With AI-Written Code - Tariq Shaukat, Sonar

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `LQW_Wvqhp04` · [watch](https://youtu.be/LQW_Wvqhp04) · **date:** 2026-10-30 · **length:** 16:35 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Tariq Shaukat · **orgs:** Sonar, Toyota, Meter, PayPal, Meta, Microsoft
- **topics:** software-factory, testing-verification, evals, governance-compliance · **tags:** software factory, code confidence, guide rails vs guard rails, independent verification, LLM-as-judge reliability, error compounding, codebase navigation tokens, cognitive surrender, evidence and compliance, deterministic + agentic verification, SonarQube, Sonar Vortex

> Vendor talk arguing AI-generated code makes volume cheap but confidence scarce, so software factories need intent, guide rails, independent verification and evidence, with LLM judges treated as unreliable.

## Summary
Tariq Shaukat, CEO of Sonar, opens with the Toyota Production System analogy: quality first, fix the system, design for building, solve problems as they occur, and let anyone stop the line. He argues modern software practices (Agile, Kanban, CI, SRE error budgets) descend from that thinking, but agentic coding breaks it. He cites a recent study of asynchronous agents showing about 2,450% more lines of code and 240% more commits but only about 30% more releases, so output scales and shipping does not. He lists five limits: human-in-the-loop does not scale (humans agree with AI even when it is wrong), agents degrade on large codebases, errors compound over long tasks, LLMs are unreliable judges, and exploit time is near zero. His "code confidence formula" multiplies four factors (clear intent, guide rails, independent verification, evidence), so a zero in any one zeroes confidence. He presents vendor results for Sonar's own products (Sonar Vortex for intent and guide rails, SonarQube for verification) and closes with a pitch to visit the booth.

## Key ideas
- **Manufacturing analogy: quality over volume, fix the system not symptoms, design for buildability, solve problems as they occur, and empower anyone to stop the line. Modern practices (Agile, Kanban, CI, SRE error budgets) come from the same Toyota lineage.** — Speaker argues agentic software factories should be built on these lean principles, not on volume-first output. ([1:33](https://youtu.be/LQW_Wvqhp04?t=93))
- **Code volume is now cheap, but shipping has not scaled with it. A cited study of asynchronous agents shows about 2,450% more lines of code and 240% more commits, yet only about 30% more releases.** — The gap between producing code and shipping it is the core problem. Speaker's own survey: 5% of developers say they run agentic software factories, 34% expect to within a year. ([3:02](https://youtu.be/LQW_Wvqhp04?t=182))
- **Human-in-the-loop does not scale in the agentic era. He cites a study where humans agreed with AI when it was right 93% of the time, and agreed about 4 in 5 times when it was wrong (he calls this cognitive surrender).** — Speaker says most companies he talks to give 'humans in the loop' as their AI governance answer, and he rejects it as the control. ([5:26](https://youtu.be/LQW_Wvqhp04?t=326))
- **Agents degrade on large codebases. In one code-translation study, accuracy was about 91% at 10k lines and collapsed by 50k. Token use to finish the same task varied 30x across codebases because agents spend tokens learning the structure.** — Speaker's analogy: starting a trip from a random point; a bad starting position costs far more time and money. ([6:52](https://youtu.be/LQW_Wvqhp04?t=412))
- **Errors compound over long tasks. Per-step accuracy of 95% gives about 36% success at 20 steps. The Meter study's 16-hour task horizon is measured at 50% accuracy; the curve flattens sharply at 80%.** — Speaker: a 16-hour horizon at 50% accuracy says little about reliability for a real multi-step run. ([7:49](https://youtu.be/LQW_Wvqhp04?t=469))
- **LLMs are unreliable judges. Across identical replications, 7% to 17% of verdicts changed (PayPal AI lab). Under a simple 'are you sure?' challenge, verdicts flipped 7% to 34% (Meta study), depending on model.** — Speaker's implication: a single LLM judge pass is not a gate. Verification must be independent and deterministic where possible. ([9:15](https://youtu.be/LQW_Wvqhp04?t=555))
- **Code confidence formula: confidence = intent x guide rails x independent verification x evidence (multiplicative). If any factor is zero, confidence is zero.** — Guide rails (nudges that keep an agent on the road) are preferred to guard rails (which stop it after it leaves the road). Evidence must be consistent, auditable and repeatable. ([10:14](https://youtu.be/LQW_Wvqhp04?t=614))
- **Verification should mix deterministic and agentic methods: use CPUs when they suffice, GPUs only when needed. Verification is treated as a first-class part of the factory, not a final step.** — Speaker says Sonar started as a verification company and views the problem through that lens. ([13:03](https://youtu.be/LQW_Wvqhp04?t=783))
- **Evidence is what makes the outcome defensible to executives, boards and auditors. He lists compliance frames such as IT general controls and MISRA as examples of evidence requirements.** — The talk closes on: abundant code, scarce confidence. Factories should deliver confidence, not just output. ([14:29](https://youtu.be/LQW_Wvqhp04?t=869))

## Techniques
- **Code confidence formula as a factory checklist** — Treat the factory as four multiplied factors: (1) explicit intent written down before the agent starts, (2) guide rails that nudge the agent during the run, (3) independent verification, not the same agent checking itself, (4) auditable evidence. Audit each factor; a missing one drives overall confidence to zero. *When:* Designing or reviewing an agentic pipeline that must be defensible to non-engineers (execs, auditors, customers).
- **Guide rails over guard rails** — Inject small, continuous nudges into the agent loop (intent, codebase map, verification feedback) that keep it on track, instead of only blocking bad outputs after the fact. Speaker's claim: putting the map near the answer cuts token burn because the agent does not re-learn the codebase structure. *When:* Long-running agent tasks on large codebases where exploration tokens dominate cost.
- **Deterministic plus agentic verification mix** — Run cheap deterministic checks (static analysis, rules) first on CPUs, reserve GPU or LLM-based agentic review for what needs semantic judgment, and combine both into one verification stage. *When:* Gating agent-written PRs or commits before merge.
- **Measure judge stability before trusting an LLM judge** — Run the same judgment twice on identical input and count flips; then challenge the verdict with a neutral 'are you sure?' and count flips again. The talk cites flip rates of 7% to 34% as the range to expect, so judge stability should be measured per model and per task, not assumed. *When:* Before using an LLM as a pass/fail gate, eval grader or plan critic.
- **Model per-step reliability to pick task length** — Multiply per-step accuracy across the number of steps (0.95^20 is about 0.36) to estimate end-to-end success, then either shorten the task, add verification between steps, or raise per-step accuracy. *When:* Planning how long one unattended agent run should be before a checkpoint or review.

## Numbers
- Lines of code written up 2,450% after implementing asynchronous agents (cited study) ([3:02](https://youtu.be/LQW_Wvqhp04?t=182))
- Commits up 240%, but releases up only 30% (same study) ([5:26](https://youtu.be/LQW_Wvqhp04?t=326))
- Survey (Sonar State of Code, preview): 5% of developers run agentic software factories; 34% expect to within a year; 39% in financial services ([3:02](https://youtu.be/LQW_Wvqhp04?t=182))
- Code translation accuracy about 91% at 10,000 lines, collapsing by 50,000 lines ([6:52](https://youtu.be/LQW_Wvqhp04?t=412))
- Token usage to complete the same task varies about 30x across large codebases ([6:52](https://youtu.be/LQW_Wvqhp04?t=412))
- Meter: Claude Mythos preview completes tasks humans take 16 hours at 50% accuracy; curve flattens at 80% ([7:49](https://youtu.be/LQW_Wvqhp04?t=469))
- 95% per-step accuracy over 20 steps gives about 36% end-to-end accuracy ([7:49](https://youtu.be/LQW_Wvqhp04?t=469))
- Humans agree with AI when it is right 93% of the time and about 4 in 5 times when it is wrong ([5:26](https://youtu.be/LQW_Wvqhp04?t=326))
- PayPal AI lab: 7% to 17% of verdicts change across identical replications ([9:15](https://youtu.be/LQW_Wvqhp04?t=555))
- Meta study: 7% to 34% of verdicts flip when the LLM is challenged, depending on model ([9:15](https://youtu.be/LQW_Wvqhp04?t=555))
- Sonar Vortex customers: 36% token cost reduction and 92% reduction in issues in commits (vendor-reported) ([13:03](https://youtu.be/LQW_Wvqhp04?t=783))
- SonarQube users over 1,000 customers: 81% more likely to see a positive impact on code security, 34% on time to market, 76% on outage frequency (vendor survey) ([14:29](https://youtu.be/LQW_Wvqhp04?t=869))

## Hot takes
- Abundant code, scarce confidence: the bottleneck moves from writing code to proving it is safe to ship.
- Human-in-the-loop is not a governance strategy at agentic scale; the speaker says humans rubber-stamp AI output.
- A single LLM judge is not a reliable gate; verdicts flip on replication and on challenge.
- Guide rails (steering during the run) beat guard rails (blocking after the fact) for long agent tasks.
- Vendor-sourced caveat: the product results (36%, 92%, 81%, 34%, 76%) come from Sonar and its own customer survey, and the close is a booth pitch. Quality capped at 3 for that reason; the cited third-party studies carry more weight than the product claims.

## Tools mentioned
SonarQube, Sonar Vortex, Claude Mythos preview (named as the model in the Meter study, version as stated in talk)

## Relevance to our work
- **agentos** (2/3): Crucible exec-gate guardrails and RAGAS evals are LLM-judge based; the talk's judge-flip data and per-step compounding math apply directly to AgentOS eval and guardrail design. → *Measure verdict flip rate for each LLM-judge eval (repeat the same input, then challenge it) before trusting RAGAS or any exec-gate LLM check as a pass/fail gate.*
- **prosharness** (2/3): ProsHarness runs plan, then critique (Codex), then debate, and the talk warns that LLM critiques are unstable. Independent verification and guide rails map to the checkpoint and loop design. → *Test the plan-critique loop for verdict stability: run the same critique twice and challenge it; if verdicts flip, add a deterministic check before a plan is approved.*

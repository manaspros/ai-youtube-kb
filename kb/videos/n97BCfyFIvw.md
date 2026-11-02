# "The engineer of the future is the person who chooses what is worth doing." — Addy Osmani, Anthropic

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `n97BCfyFIvw` · [watch](https://youtu.be/n97BCfyFIvw) · **date:** 2026-07-18 · **length:** 18:26 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Addy Osmani · **orgs:** Anthropic, Sonar, Wharton
- **topics:** software-factory, governance-compliance, pr-code-review, product-ux · **tags:** human-in-the-loop, accountability, verification-bottleneck, cognitive-debt, taste, inner-loop-outer-loop, software-factory, career

> Addy Osmani argues engineers are defined by owning the verdict on agent work: choosing what is worth doing, backing it with evidence, and accepting accountability. Keep humans at the highest-leverage checkpoint.

## Summary
Osmani, speaking for Anthropic, argues that the engineer's job shifts from producing code to choosing what is worth doing and owning the verdict on agent output. He separates quality (which produces evidence) from verdict (which assigns responsibility) and answerability (which lets someone stand behind it). He describes a progression from harness engineering to loop engineering to software factories, where humans still make the production decisions. The main bottleneck he names is verification: teams have distrust of AI code without the bandwidth to verify it. He frames the operating boundary as an inner loop (agents investigate, implement, test and report) and an outer loop (humans decide, verify, approve and own). He closes with the rule "explain it or don't ship it" and an argument that cheaper building expands latent demand, moving the bottleneck to whether something should exist.

## Key ideas
- **The engineer's scarce skill is choosing what is worth doing and owning the verdict on agent work.** — Quality produces evidence, a verdict assigns responsibility, and answerability is what lets someone stand behind the verdict. The talk proposes engineering modes (prototype, build, sweep, grow, maintain) as a way to ask which part of the system a person owns. ([0:08](https://youtu.be/n97BCfyFIvw?t=8))
- **Harness engineering and loop engineering turned agents into delegable infrastructure, but humans still make the production decisions.** — The coding agent is the model plus harness (context, tools, file system, Git). Loop engineering adds prompting, checking, remembering and deciding next steps. Software factories are built from these loops, and the win is moving human judgment to the highest-leverage checkpoint. ([2:33](https://youtu.be/n97BCfyFIvw?t=153))
- **Verification is the bottleneck: the problem is distrust without bandwidth.** — He cites a survey where most engineers do not fully trust AI code, but only about half always verify before committing. Making generation cheaper does not make review cheaper, so verification needs to be cheaper, clearer and harder to skip. ([3:48](https://youtu.be/n97BCfyFIvw?t=228))
- **Organizations need answers to governance questions that current tooling rarely gives.** — Did a model touch this file? What constraints guided the work? What evidence was produced, what risk was accepted, and who owned the result? ([5:10](https://youtu.be/n97BCfyFIvw?t=310))
- **Judgment has a decay rate. Edges (speed, recall, verification) decay with each model release, but a signature (credibility, the name on the work) lasts longer.** — He uses alpha for the gap between what a person can do and what current models can do, and decay for how fast that gap closes. He argues the strategic question is what only a human can be answerable for, not what agents can do. ([6:37](https://youtu.be/n97BCfyFIvw?t=397))
- **Delegation depth is the main risk: long-horizon agent runs need a control system, not a final glance.** — A 30-second run is an interaction. An hour- or day-long run is a work stream. Running many in parallel requires review designed as a control system. ([9:26](https://youtu.be/n97BCfyFIvw?t=566))
- **Orchestration tax: more agents running does not add more human bandwidth, so attention must be designed.** — Each loop creates more decisions to route, merge, verify and integrate. The fix is not necessarily fewer agents but deliberately choosing where to enter, what to acquire and what to reuse. ([12:14](https://youtu.be/n97BCfyFIvw?t=734))
- **The boundary is evidence and responsibility, not whether a human reads every line. The rule is: explain it or don't ship it.** — Agent output should come back as evidence (diffs, tests, logs, rationale, traces, screenshots). Someone must be able to defend the change, similar to an owners file for code areas. The agent can follow a runbook but cannot inherit consequences. ([13:41](https://youtu.be/n97BCfyFIvw?t=821))
- **Lowering the cost of building creates latent demand, so the bottleneck moves from can we build this to should this exist.** — He points to past abstractions (higher-level languages, frameworks, cloud, low code) that increased software demand instead of reducing it. ([17:25](https://youtu.be/n97BCfyFIvw?t=1045))

## Techniques
- **Inner loop / outer loop split** — Let agents run the inner execution loop (investigate, implement, test, report). Keep the outer loop (decide whether work is worth doing, verify evidence, approve, redirect, own what reaches production) with humans. *When:* When running agents on production changes, especially in parallel, and deciding where human sign-off sits.
- **Evidence bundle as the review unit** — Require each agent run to return diffs, test results, logs, rationale, traces, trajectories or screenshots, as the work requires. Review the evidence, not only the final diff. *When:* Any agent-produced PR or task output that a human must accept or reject.
- **Explain-it-or-don't-ship gate with named owners** — Before merging agent-written changes, check that a named owner can explain the change, its evidence and its risks. Map ownership to architecture areas, similar to an owners file. *When:* Merge decisions on agent-written code in shared or large codebases.
- **Review as a control system for long runs** — Treat hour- or day-long agent tasks as work streams with checkpoints and escalation points, not single end-of-run reviews. Cap delegation depth so the team keeps understanding of the system. *When:* Long-horizon or many parallel agent runs where the human can lose track.
- **Move verification into the harness** — Put verification into evals, static checks and model critique inside the harness so it runs without a human having to remember it. He presents this as the way verification gets cheaper. *When:* When review load outgrows reviewer bandwidth.
- **Clean code for agents as well as humans** — Keep repos clean and readable. He cites a Sonar study where clean and messy repos had similar pass rates, but clean repos used fewer tokens and caused fewer revisits. *When:* When planning maintainability work that also reduces agent token cost and rework.

## Numbers
- A Sonar 2026 survey: AI-assisted code is no longer marginal and is increasingly a large part of codebases. ([2:33](https://youtu.be/n97BCfyFIvw?t=153))
- Sonar: clean and messy repos had roughly the same pass rates, but clean repos used fewer tokens and caused fewer revisits. ([3:48](https://youtu.be/n97BCfyFIvw?t=228))
- Sonar: about 96% of engineers do not fully trust AI code, but only about half always verify before committing. ([3:48](https://youtu.be/n97BCfyFIvw?t=228))
- Wharton study: when the AI was wrong, 73% of people still believed they had picked the right answer and felt more sure. The transcript says 'picked the wrong answer', which is probably an auto-caption error. The stated figure is the core point. ([10:50](https://youtu.be/n97BCfyFIvw?t=650))
- Run length framing: a 30-second run feels like an interaction, while an hour- or day-long run is a work stream. ([9:26](https://youtu.be/n97BCfyFIvw?t=566))

## Hot takes
- Taste can become a magic word for whatever part of the work we don't want to explain yet.
- Accountability is not what remains after agents get good. It is what lets the rest of the system scale.
- More AI agents running does not mean there is more of you available. Cognitive bandwidth does not parallelize.
- The failure mode is not using AI but borrowed confidence.
- The bottleneck moves from can we build this to should this exist, and can we answer for it.

## Tools mentioned
Git

## Relevance to our work
- **prosharness** (2/3): ProsHarness already has checkpoints and phone-driven approvals. The talk's point that approvals need evidence and a named owner (not only yes or no) applies directly to that flow. → *Extend the checkpoint approval record with the evidence bundle shown, the risk accepted and the approver's identity, so each approval answers who accepted what and why.*
- **agentos** (1/3): The audit log is Merkle-based and records what happened. The talk argues the record should also show who owns the outcome and what evidence supported it. → *Consider adding an owner or accountable-principal field to audit entries, separate from the agent identity that performed the action.*
- **general** (1/3): The inner/outer loop split and the explain-it-or-don't-ship rule are reusable design rules for any agent pipeline. → *Use one human approval gate after agent execution as the default design for any new agent workflow, and record the evidence it reviews.*

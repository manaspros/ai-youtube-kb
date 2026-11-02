# Act, Confirm, or Stop? Smarter behavior for AI assistants, wearables & robots — Amit Desai, Roku

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Zd5b40Jbp_k` · [watch](https://youtu.be/Zd5b40Jbp_k) · **date:** 2026-09-18 · **length:** 20:25 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Amit Desai · **orgs:** Roku, Alexa (Amazon)
- **topics:** voice-multimodal, product-ux, evals · **tags:** voice-ux, confidence-thresholds, act-confirm-stop, user-cost-function, decision-thresholds, embodied-ai, conversational-behavior

> Voice assistant satisfaction can rise without better accuracy: gate act/confirm/stop on calibrated confidence and pick thresholds by minimizing a user-cost function ("ouch").

## Summary
Amit Desai (Roku, former Alexa voice SME) argues that voice AI teams only tune one knob, accuracy, and that a second knob, system behavior under uncertainty, is underused. He uses a smart-speaker music example with 1,000 labeled requests at 79% accuracy. Choosing a single confidence threshold for "act or stop" by gut feel is worse than an optimized threshold, because wrong actions and unnecessary stops have different user costs. He models user cost as extra seconds to recover (wrong song 10s, stop 4s) and calls the metric "ouch." Adding a confirm behavior creates a three-band policy (stop, confirm, act) with two thresholds, found by optimization over a heat map, and the cost falls further (2.1 to 1.9 to 1.27 to about 1.26 per turn). The same approach should transfer to TV and to embodied or digital agents, but the cost values must be re-set per modality, since visual choices or state-losing actions change the trade-off.

## Key ideas
- **Two levers for user satisfaction: accuracy, and system decisions under uncertainty (stop, confirm, act). The second lever is orthogonal to accuracy and under-used.** — Accuracy held fixed at 79%, and the system's behavior alone changes the outcome. The speaker frames this as the premise for the talk. ([1:08](https://youtu.be/Zd5b40Jbp_k?t=68))
- **Gut-feel confidence thresholds produce bad outcomes; optimize the threshold against a cost function instead.** — Any single threshold trades off stopping (bad) against wrong actions (bad). A 65% threshold guess gave about 1.9 cost per turn, and the optimized threshold at 43% gave about 1.27. ([6:01](https://youtu.be/Zd5b40Jbp_k?t=361))
- **Outcomes are not equally bad. Quantify each one as extra seconds to recover to success.** — Unit costs used: wrong song about 10 seconds (hear it, interrupt, re-request), stop about 4 seconds (re-speak). The speaker calls the combined metric 'outcome user cost heuristic,' or 'ouch.' ([8:56](https://youtu.be/Zd5b40Jbp_k?t=536))
- **Adding a confirm behavior turns the policy into three bands and two thresholds (T1 and T2).** — Confirm-yes costs about 2 seconds and confirm-no about 6 seconds. The optimum reported is T1 about 41 and T2 about 49, found from a 2D heat map. Accuracy is unchanged throughout. ([13:00](https://youtu.be/Zd5b40Jbp_k?t=780))
- **The cost values are assumptions, and the optimum moves when they change. Set them per surface and per modality.** — If a wrong action is valued at 20 instead of 10, the optimal thresholds shift. On a TV with visible choices, confirm is cheaper; if launching a channel exits the current state, a wrong act costs much more. ([15:25](https://youtu.be/Zd5b40Jbp_k?t=925))
- **The method is meant to be real-time and learned in production, not a fixed offline table. The principle carries over to other surfaces and embodied or digital agents.** — The smart-speaker grid is a simplified example. The speaker expects real systems to use a learned decision model, and says the same reasoning applies to physical or digital actions like sending email or placing a call. ([16:42](https://youtu.be/Zd5b40Jbp_k?t=1002))

## Techniques
- **Outcome user-cost minimization for act/confirm/stop** — Label a sample of requests with the outcome of each possible system behavior. Give each bad outcome a cost in seconds of user recovery (wrong act, stop, confirm-yes, confirm-no). Plot confidence distributions for correct and wrong hypotheses, then choose thresholds that minimize total cost divided by turns. *When:* A voice or agent system gives a calibrated confidence score and can choose between acting, asking to confirm, or declining, and where the wrong-action and stop costs differ.
- **Two-threshold three-band policy with grid search** — Define T1 (below it: stop) and T2 (above it: act), with confirm in between. Sweep both thresholds over a grid, compute total cost for each pair, and read the minimum from a heat map. The speaker used an AI coding assistant to build the interactive graph. *When:* When adding a confirmation step, which makes the decision space two-dimensional and makes guessed thresholds unreliable.
- **Sensitivity check on unit costs** — Change the assumed cost of the most expensive outcome (for example, wrong act from 10 to 20) and recompute the optimal thresholds before committing to a policy. *When:* Before shipping a threshold policy, since the cost values are heuristic and drive the optimum.

## Numbers
- Accuracy on 1,000 labeled spoken requests: 79% correct, 21% wrong song ([3:34](https://youtu.be/Zd5b40Jbp_k?t=214))
- Always-act baseline cost: 2.1 user-cost points per turn (2100 total over 1,000 requests) ([10:19](https://youtu.be/Zd5b40Jbp_k?t=619))
- Single threshold guessed at 65%: about 1.9 per turn ([10:19](https://youtu.be/Zd5b40Jbp_k?t=619))
- Single threshold optimized at 43%: about 1.27 per turn, with accuracy unchanged ([11:38](https://youtu.be/Zd5b40Jbp_k?t=698))
- Unit costs: wrong song about 10 seconds, stop about 4 seconds, confirm-yes about 2 seconds, confirm-no about 6 seconds ([8:56](https://youtu.be/Zd5b40Jbp_k?t=536))
- Three-band optimum: T1 about 41, T2 about 49, total cost about 1.26 per turn. The transcript's written figure reads '1464,' which looks like a garbled 1.264; treat as uncertain ([15:25](https://youtu.be/Zd5b40Jbp_k?t=925))

## Hot takes
- Accuracy is not the only lever. Behavior under uncertainty can do as much for user satisfaction as squeezing out more accuracy.
- Gut-feel confidence thresholds are measurably worse than thresholds optimized against a user-cost function.
- Embodied and digital agents that take real actions will make accuracy alone an insufficient path to acceptable UX.

## Tools mentioned
Interactive threshold-sweep graph built with a coding assistant (no specific library named)

## Relevance to our work
- **agentos** (1/3): Crucible's exec-gate guardrails and any agent that takes actions could use a confidence-banded act/confirm/stop policy, though the talk covers voice only. → *Prototype a three-band gate (auto-run, ask for confirmation, refuse) on Crucible exec-gate decisions, with a per-action-type cost table, and tune the thresholds on logged decisions.*
- **prosharness** (1/3): ProsHarness has phone-driven approvals, and this talk gives a way to decide when to ask for approval versus proceed. → *Consider using a cost-weighted approval threshold for ProsHarness phone approvals, so low-risk steps auto-proceed and only costly-to-undo steps wait for a human.*
- **general** (1/3): Recurring interest in evals for agents. The talk proposes a cost-weighted metric as a better target than raw accuracy. → *When evaluating agent decisions, report expected user or recovery cost (weighted by outcome type) alongside accuracy, and keep the cost table versioned.*

# Stop Burning Tokens: Why self-improvement needs domain expertise first - Annabell Schäfer, Langfuse

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `eAXxdtNlK04` · [watch](https://youtu.be/eAXxdtNlK04) · **date:** 2026-08-18 · **length:** 17:39 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Annabell Schäfer · **orgs:** Langfuse
- **topics:** evals, context-engineering, observability · **tags:** self-improvement loop, prompt optimization, target function, LLM-as-judge, high-signal evaluators, domain expertise, validation split, error clustering, GPT-5 Nano, Claude Opus, Langfuse

> Langfuse's Annabell Schäfer shows that a clear-cut yes/no target function (single-label paper classification) lets an optimizer loop improve a small model's prompt, and argues teams need domain experts and high-signal evaluators before auto-improvement pays off.

## Summary
The talk argues that agent self-improvement only works when the target function is clear, and that most AI applications lack one because LLM-as-judge scores on vague 0-1 or 1-10 scales give low, inconsistent signal. As a test, the speaker ran an optimization loop on single-label classification of research papers (GPT-5 Nano as the agent, Claude Opus 4.8 via Claude Code as the optimizer) using 200 fit, 100 validate and 300 test items. The loop did error analysis on the fit set, proposed prompt changes, and kept only those that improved validation, with stops at 15 runs or 92% accuracy. Accuracy rose from a baseline of about 68% to roughly 83%, and held near 80% on the unseen test set. The biggest single gain (about 10 points) came from the first iteration, driven by a clear error pattern in the confusion data. The speaker's recommended path is to work with domain experts to define concrete yes/no quality criteria, review production data by hand, and use validation sets and escape hatches so loops do not burn tokens. The talk is a practitioner-level method talk with one concrete experiment, and it is honest about its limits, such as label subjectivity in the ground truth.

## Key ideas
- **Self-improvement loops need a clear target function, and most AI apps do not have one.** — Coding has a natural target (does it compile). Domains like healthcare or compliance have targets that are incomplete and hard to state, so teams that invest in defining what 'good' means improve faster and can ship with more confidence. ([1:19](https://youtu.be/eAXxdtNlK04?t=79))
- **A single-label classification task was used as a clean test bed for the loop.** — Right or wrong is unambiguous, so accuracy gives a clear signal. The speaker used it to see what an optimizer does with a plain target. ([2:28](https://youtu.be/eAXxdtNlK04?t=148))
- **Loop design: fit, validate and test splits, with an optimizer that only accepts changes that generalize.** — The optimizer analyses errors on the fit set and proposes a prompt change for the biggest error cluster. A change is kept only if validation improves. The test set is held out and the agent is not given its link. ([3:50](https://youtu.be/eAXxdtNlK04?t=230))
- **The first iteration produced most of the gain.** — Accuracy went from about 68% to about 78% in one step, driven by a clear error pattern (answer sink, with the most-confused label pair). The later steps added only small gains, so the speaker suggests stopping early once a strong signal has been used. ([10:01](https://youtu.be/eAXxdtNlK04?t=601))
- **The optimizer's prompt edits were structural, not stylistic.** — It added a general classification approach, rules for choosing between similar labels, guidance on preferring specific over broad labels, and examples of frequently confused item pairs. The speaker had expected label descriptions. ([8:54](https://youtu.be/eAXxdtNlK04?t=534))
- **Replace vague 0-1 or 1-10 judge scores with specific yes/no criteria.** — Metrics like correctness or helpfulness are low-signal and inconsistent unless each score level is defined. Better checks are binary and specific, such as whether a claim appears in the retrieved context, whether a brand name is spelled correctly, or which known failure mode occurred. ([11:26](https://youtu.be/eAXxdtNlK04?t=686))
- **Working with domain experts and reviewing production data by hand is the foundation.** — Experts should be asked to create example outputs and explain why decisions are made. Human review of production traces catches failure modes before customers do and shows when scope shifts. ([15:15](https://youtu.be/eAXxdtNlK04?t=915))
- **Treat evaluation as a system that generalizes, and add escape hatches.** — Use validation splits to check for overfitting, give loops clear instructions and a stopping rule, and avoid letting an agent run for hours against a wall while burning tokens. ([16:30](https://youtu.be/eAXxdtNlK04?t=990))

## Techniques
- **Fit / validate / test split for prompt optimization** — Run the baseline prompt on the fit and validate sets and score per item. Optimizer analyses fit-set errors and clusters, proposes one prompt change for the largest error category, and keeps it only if validation improves. Test set stays hidden until a stopping rule is met (here 15 runs or 92% accuracy). *When:* Any automated prompt-tuning loop where overfitting to the training data is a risk and a labelled dataset exists.
- **Error clustering to drive hypotheses** — Group the errors by label, count the most-confused label pairs, and look at the underlying inputs for patterns. Feed these clusters to the optimizer, which turns each into one targeted hypothesis. *When:* Classification or extraction tasks where failures fall into a few dominant confusion patterns.
- **Binary, criterion-specific judges instead of Likert-style scores** — Define each quality criterion as a yes/no check tied to the application (for example, is a claim supported by the retrieved context, is a brand name spelled correctly) or as a named failure-mode category, and avoid unanchored 0-10 scores. *When:* Building LLM-as-judge evaluators meant to feed an automatic improvement loop.
- **Task markdown as the loop spec** — A markdown file describes each loop step, the datasets (the test-set path is withheld) and the stopping criteria. The optimizer reads it and runs the loop, with a reference prompting guide as context. *When:* Running a coding agent (here Claude Code) as an unattended optimizer over a fixed eval setup.

## Numbers
- Baseline accuracy of the flat-label-list prompt on the fit/validate sets is about 68%. ([6:21](https://youtu.be/eAXxdtNlK04?t=381))
- Accuracy reached about 83% on the validation set on the fourth iteration, then plateaued at around 80%. ([6:21](https://youtu.be/eAXxdtNlK04?t=381))
- The first iteration gained about 10 points (68% to about 78%), driven by 64 errors in the dominant patterns. ([10:01](https://youtu.be/eAXxdtNlK04?t=601))
- Generalization to the 300-item held-out test set reached about 80%. ([7:30](https://youtu.be/eAXxdtNlK04?t=450))
- Dataset sizes are 200 fit, 100 validate and 300 test items, with a stopping rule of 15 runs or 92% accuracy. ([3:50](https://youtu.be/eAXxdtNlK04?t=230))
- The optimizer model was Claude Opus 4.8 run through Claude Code, and the agent was GPT-5 Nano. ([3:50](https://youtu.be/eAXxdtNlK04?t=230))

## Hot takes
- Most LLM-as-judge metrics such as correctness or helpfulness are low-signal for auto-improvement unless each score level is defined.
- The first iteration of an auto-optimization loop often delivers most of the gain, so teams may stop there once a clear error pattern is found.

## Tools mentioned
Langfuse, Claude Code, GPT-5 Nano, Claude Opus 4.8

## Relevance to our work
- **agentos** (2/3): L2D SkillForge needs a success signal and skill-worthiness scoring. The talk's point that a binary target and a validation split are needed before a loop can learn from telemetry applies directly to that open question. → *Define binary, criterion-specific success checks for SkillForge's mined skills and hold out a validation split before any auto-tuning loop is allowed to change skills.*
- **prosharness** (2/3): ProsHarness runs long Claude Code loops with checkpoint/resume and needs stopping rules. The talk's escape-hatch and validation-gate pattern fits its plan → critique loop. → *Add a validation gate and an explicit stop criterion (run cap or target metric) to the ProsHarness loop, so a change is kept only if it improves a held-out check.*
- **general** (2/3): Recurring interest in evals for agents and cheap-model (Haiku) pipelines. The experiment (small model plus frontier optimizer, with fit/validate/test) is a clear template for that. → *Read the Langfuse talk's approach to replacing 0-10 judge scores with binary criteria, and apply it to the next Haiku pipeline's eval set.*

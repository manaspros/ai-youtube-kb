# Build AI Systems for Discernment, Not Approval - Angel Ortmann Lee, Duolingo

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `CDqzWpwkSls` · [watch](https://youtu.be/CDqzWpwkSls) · **date:** 2026-07-18 · **length:** 25:53 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Angel Ortmann Lee · **orgs:** Duolingo
- **topics:** product-ux, evals, governance-compliance · **tags:** human-in-the-loop, automation-bias, interaction-design, labeling-signals, review-gates, proctoring, trust-calibration, coding-agent-ux

> Duolingo shows skilled reviewers accepted half of fake AI cheating flags; guidelines demanding independent evidence raised rejections 21%. Design human-in-the-loop interactions for discernment, not approval.

## Summary
Angel Ortmann Lee (Duolingo) argues that human-in-the-loop AI often fails because the human rubber-stamps the model. The team ran a case study on the Duolingo English Test, feeding historical clean sessions to human proctors with a fake AI copy-typing signal. Despite scoring above 90% on accuracy calibration, proctors accepted about half of the fake flags. The team concluded the problem was the interaction design, not the model (about 1% false positive rate) or the people. Changing the proctor guideline to call the AI signal a preliminary alert and to require independent video evidence before upholding a flag raised rejection rates by 21%. The talk then generalises to other flags, tutoring UIs and coding agents, and proposes principles: engineer the reasoning, match friction to stakes, treat every interaction as a label, and collect explicit feedback. The speaker frames the human-AI loop as a flywheel that produces either honest labels or confident false ones.

## Key ideas
- **Automation bias shows up even in skilled reviewers** — Proctors with over 90% calibration accuracy accepted about 50% of fake AI signals on known-clean sessions. The speaker reads this as deferring to the AI without checking the evidence. A Wharton study cited earlier found 80% of people accepted wrong AI answers. ([5:42](https://youtu.be/CDqzWpwkSls?t=342))
- **The fix was the interaction, not the model or the people** — The model had about 1% false positives and the reviewers were skilled, so the team changed the reviewer guideline. They told reviewers the AI signal is only a preliminary alert and that they must find independent video evidence before upholding a flag. No model or UI change was needed. ([6:39](https://youtu.be/CDqzWpwkSls?t=399))
- **Bundled yes/no questions corrupt labels** — A headphone-detection prompt packed two questions into one yes/no: did the model see headphones, and should this person be flagged? A person with a hearing aid gives a true detection but should not be flagged, so a 'no' poisons the training signal. Splitting the question gave more and cleaner data. ([12:04](https://youtu.be/CDqzWpwkSls?t=724))
- **Rubber-stamping creates a vicious cycle** — If the interaction does not force deliberation, the model looks more confident, reviewers defer more, and the approval is logged as ground truth. The speaker contrasts this with a virtuous cycle in which forced independent judgment produces honest positive and negative labels. ([11:00](https://youtu.be/CDqzWpwkSls?t=660))
- **Every interaction is already a label, but only if the diff is captured** — Accept and reject alone is a weak signal, and it skews toward accept. When a human edits or overrides the AI output, that diff is the real signal. Recording only a yes lets false signals pollute the dataset. ([21:30](https://youtu.be/CDqzWpwkSls?t=1290))
- **Match friction to stakes and make the output structured** — High-stakes review should have deliberate friction and gates. Low-stakes chat should be seamless. Structured inputs and outputs (forms, tables, inline markup, surfaced assumptions) give targeted, reviewable interactions instead of walls of text. ([20:14](https://youtu.be/CDqzWpwkSls?t=1214))

## Techniques
- **Calibration test with planted false signals** — Take sessions or cases known to be clean from history, show them to reviewers in the normal workflow with a fake AI flag, and measure how often reviewers uphold it. Use it to find automation bias before it reaches real users. *When:* Before trusting human review of an AI classifier in a high-stakes setting, or when judging whether reviewers rubber-stamp.
- **Reframe the AI output as a preliminary alert** — Change the review guideline so the model output is a lead, and the human must cite independent evidence before accepting it. This is a prompt or policy change, not a model change. *When:* When the human is deferring to a model's flags and you need honest true and false labels.
- **Split compound questions into separate signals** — Where one prompt asks both 'was X detected' and 'should we act on X', ask two questions. Store the detection and the decision separately so each is a clean label. *When:* When a yes/no review step mixes perception with policy judgment.
- **Inline anchored feedback instead of a long essay** — Mark up the user's text in place, with colour-coded spans (good, awkward, wrong), short feedback on hover, and accept-in-line actions. Each suggestion stays tied to its exact span. *When:* For tutoring or writing-feedback UIs where the output should match how a human teacher marks a document.
- **Surface assumptions and trade-offs for sign-off in agent plans** — Have the coding agent state its assumptions and design trade-offs early, ask for sign-off, and split work into small reviewable PRs with a written spec, instead of one large diff or a per-edit prompt. *When:* For long-running coding-agent tasks where late corrections are expensive.
- **Capture the edit diff as the training signal** — Log what the human changed or overrode from the AI output, not only the accept or reject. Treat the diff as the label for the next eval or fine-tune. *When:* When designing data collection for an agent or assistant that a human reviews.
- **Log the questions users ask as a trust signal** — Track follow-up and explanation requests and their sentiment. Frequent 'why' questions can indicate low trust or a wrong output. *When:* When you want a cheap proxy for user confidence in an AI feature.

## Numbers
- Wharton study: 80% of participants accepted AI answers even when wrong (cognitive surrender) ([2:17](https://youtu.be/CDqzWpwkSls?t=137))
- In that study, performance rose 25 percentage points when the AI was right and fell 15 points when it was wrong ([2:17](https://youtu.be/CDqzWpwkSls?t=137))
- Duolingo English Test is used by about 6,000 programs worldwide ([3:31](https://youtu.be/CDqzWpwkSls?t=211))
- Proctors scored above 90% on accuracy calibration yet accepted about 50% of fake copy-typing flags on clean historical sessions ([5:42](https://youtu.be/CDqzWpwkSls?t=342))
- The copy-typing model has a stated 1% false positive rate ([6:39](https://youtu.be/CDqzWpwkSls?t=399))
- Changing the proctor guideline raised rejection rates by 21%; the speaker says the majority of previously accepted sessions were now judged okay (the exact 71 figure is ambiguous in the transcript) ([7:49](https://youtu.be/CDqzWpwkSls?t=469))

## Hot takes
- The human in the loop is often not thinking. Accepting an AI flag is a coin flip for skilled people, and the interface causes it.
- Sometimes the fix is not a better model or more oversight. It is engineering the interaction.
- Binary accept/reject labels carry little information and skew toward accept, so most agent telemetry is noise unless the edit diff is captured.
- Friction is your friend where stakes are high. Seamless UX is right only for low-stakes chat.

## Relevance to our work
- **agentos** (2/3): The talk's point that accept/reject is a weak signal and the edit diff is the real label bears on SkillForge's open question about the success signal for mining agent telemetry. It does not change the proxy or infra design. → *For SkillForge, log the diff between the agent's output and the human's final version as a candidate success signal, and compare it against plain accept/reject before settling the skill-worthiness score.*
- **prosharness** (2/3): ProsHarness's plan -> critique -> approval flow and phone-driven approvals are the kind of human gate the talk critiques. Surfacing assumptions and trade-offs for sign-off, and capturing plan edits, would make those approvals more than rubber stamps. → *Change the plan approval step to list the plan's assumptions and trade-offs explicitly and record which lines the human edited or rejected, instead of storing a plain approve/deny.*
- **general** (1/3): Recurring interest in entity resolution and data quality with LLMs: the planted-false-signal test is a direct way to check whether human reviewers of ER match decisions are rubber-stamping model output. → *Run a planted-false-match calibration on past ER review data to measure how often reviewers accept wrong model matches before trusting reviewed labels.*

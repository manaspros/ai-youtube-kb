# Build Evals That Actually Matter - Nick Ung & Akshay Sharma, Lyft

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `3z2uT5aDx_Y` · [watch](https://youtu.be/3z2uT5aDx_Y) · **date:** 2026-08-18 · **length:** 37:45 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Nick Ung, Akshay Sharma · **orgs:** Lyft
- **topics:** evals, observability, enterprise-adoption · **tags:** customer-support-agent, llm-as-judge, user-simulator, offline-eval, online-eval, annotation-queue, precision-recall, confidence-intervals, eval-harness, criteria-drift, error-analysis, langgraph, langsmith, langfuse, deepeval

> Lyft's customer-support agent team on building offline simulation evals, calibrating LLM judges on hand labels, and closing the loop from error analysis to agent changes.

## Summary
Nick Ung and Akshay Sharma from Lyft describe the eval pipeline for their multi-agent customer-support agent, split into offline evals before launch and online evals on production traces. Offline evals run simulated multi-turn conversations between the agent and an LLM user, graded by an LLM judge plus deterministic code assertions. Their first simulator was too polite, which inflated pass rates to about 90%, so they fine-tuned the user model on real Lyft user messages and added personas, which lowered scores as intended. They argue judges should be binary, task-based pass/fail rubrics tied to business outcomes, not generic metrics like helpfulness. Judges should be treated as classifiers: hand-label about 100 examples, split them into train, dev and test sets, and report precision and recall. Criteria evolve as the team reads data, and small score gaps on about 50 traces need confidence intervals before they mean anything. The loop is continuous error analysis on traces, with annotation queues for domain experts, and the next step is a config-driven eval harness that runs locally, pre-commit and in CI.

## Key ideas
- **Run offline multi-turn simulated conversations as a launch gate for agents.** — Before shipping, the agent is run against a synthetic dataset representative of production traffic. A user LLM plays the customer, and an LLM judge grades each conversation. Live users are not used as test data. ([3:58](https://youtu.be/3z2uT5aDx_Y?t=238))
- **A judge score only matters if it gates a decision.** — Speaker's first pitfall: judges that produce scores nobody uses for launch or regression gating are noise. Regression gates must have clear owners who act on the results. ([5:17](https://youtu.be/3z2uT5aDx_Y?t=317))
- **Simulated users that are too polite make evals look falsely good.** — The first offline run gave 90%+ accuracy. Simulated users were patient and verbose, while real Lyft users are impatient and frustrated. The team judged the high score as too good to be true. ([13:49](https://youtu.be/3z2uT5aDx_Y?t=829))
- **Calibrate the user simulator on real user messages and personas, and expect scores to drop.** — They fine-tuned the user LLM on real Lyft user verbatims and defined personas such as bypasser, refund seeker and AI skeptic. Lower scores after this change are the goal, because a too-easy eval gives no production signal. ([15:15](https://youtu.be/3z2uT5aDx_Y?t=915))
- **Generic judge metrics are not actionable; use binary task success or failure tied to business outcomes.** — Pre-built DeepEval-style scores such as helpfulness at 0.5 give no next step. Each metric defines explicit pass and fail criteria for a task. Example: the agent escalates too soon, or tries too many times to educate the user. ([17:41](https://youtu.be/3z2uT5aDx_Y?t=1061))
- **Treat the LLM judge as a classifier and validate it against hand labels.** — Hand-label about 100 examples as pass or fail, then split them into train (few-shot examples for the prompt), dev (prompt iteration) and test (final check). Report precision and recall. The split informs the prompt; no model weights are trained. ([21:33](https://youtu.be/3z2uT5aDx_Y?t=1293))
- **Evaluation criteria drift, so validate the validators continuously.** — Criteria are discovered by reading data and grading outputs, and the team's sense of quality changes as they see more examples. Criteria and judges should be co-developed with the agent rather than fixed up front. ([23:00](https://youtu.be/3z2uT5aDx_Y?t=1380))
- **Report confidence intervals and use paired designs, because small gaps are noise.** — An 84% vs 88% gap on 50 traces is not evidence of a real difference. Bigger gains or paired comparisons need fewer samples. Reserve the heavier statistics for numbers that gate a ship decision or go to leadership. ([24:09](https://youtu.be/3z2uT5aDx_Y?t=1449))
- **Error analysis on raw traces is a recurring loop, not a one-off audit.** — Look at traces, name failure modes, keep only metrics that change a decision, re-create the eval, and repeat on a regular cadence such as weekly or biweekly. Ignoring the data is the root anti-pattern. ([27:13](https://youtu.be/3z2uT5aDx_Y?t=1633))
- **Close the loop through model, context or harness changes.** — Model learning means post-training. Context learning changes what the agent sees, such as documents, memories and outputs. Harness learning changes control flow, routing, retries and schemas. Error analysis guides which of these to change. ([30:08](https://youtu.be/3z2uT5aDx_Y?t=1808))

## Techniques
- **Simulated multi-turn offline eval** — Define the user intent, world state and persona for each case. A user LLM runs a full conversation with the agent graph. Grade with an LLM judge plus deterministic code checks, such as whether the agent's tool calls match an expected outcome (e.g. a concession was granted). *When:* Pre-launch testing of multi-turn, user-facing agents, especially customer support.
- **Mixed eval dataset from production samples plus mutations** — Do not ask an LLM to generate 50 test queries. Sample real production conversations, then mutate criteria to cover golden paths and edge cases. *When:* Building an offline eval set that should resemble real traffic.
- **User simulator realism calibration** — Fine-tune the simulated user model on real user messages. Add personas that match real behavior, such as impatient or skeptical users, then check that scores fall. *When:* Simulated users are too cooperative and the eval pass rate looks suspiciously high.
- **Binary task-outcome rubric per metric** — Each judge checks one task with explicit success and failure criteria. Map each failure to a business outcome. Drop generic metrics that do not change a decision. *When:* Designing LLM judges that someone must act on.
- **Judge calibration as a classifier** — Hand-label about 100 traces pass or fail. Split into train (few-shot prompt examples), dev (prompt iteration) and test (final check, to detect overfitting). Report precision and recall against the human labels. *When:* Before trusting any LLM judge score for a gate.
- **Confidence intervals and paired comparisons** — Attach a confidence interval to every alignment rate reported. Compare two evaluators on the same traces (paired design) so a small gap can be tested. *When:* Comparing judges or agent versions with modest sample sizes.
- **Annotation queue for domain experts** — Show traces in a simple labelling UI so domain experts never read raw JSON. Labels feed eval datasets and judge calibration. The speaker mentions LangSmith and Langfuse for tracing. *When:* Getting expert labels at scale for error analysis and judge validation.
- **Config-driven eval harness** — Store eval suites as YAML built from primitives: task, dataset, persona, LM adapter, evaluator. Support parallel runs for thousands of cases. Run the same config locally, at pre-commit and in CI as a regression or acceptance test. *When:* The eval suite has grown past ad-hoc notebooks and needs to be shared across contributors.

## Numbers
- First offline simulation run reported about 90%+ accuracy, which the team judged too good to be true. ([13:49](https://youtu.be/3z2uT5aDx_Y?t=829))
- Judge calibration uses about 100 hand-labelled examples split into train, dev and test sets. ([21:33](https://youtu.be/3z2uT5aDx_Y?t=1293))
- Example: 84% vs 88% alignment on only 50 traces is too small a gap to call real without statistics. ([25:49](https://youtu.be/3z2uT5aDx_Y?t=1549))
- Error-analysis review cadence suggested as weekly or biweekly. ([28:35](https://youtu.be/3z2uT5aDx_Y?t=1715))
- The eval suite is expected to reach thousands, or tens of thousands, of examples, which requires parallel runs. ([34:01](https://youtu.be/3z2uT5aDx_Y?t=2041))

## Hot takes
- Frontier-model user simulators are trained to be helpful, so an eval built on them is too easy. A very high offline pass rate is a warning sign.
- Pre-built judge metrics such as helpfulness or conciseness are not actionable. Use them as a baseline only.
- A judge score that gates nothing is noise, and LLM judges must be validated against human labels like any classifier.

## Tools mentioned
LangSmith, Langfuse, DeepEval, LangGraph, tau-bench (transcribed as CowBench, from Sierra)

## Relevance to our work
- **agentos** (2/3): AgentOS has RAGAS evals and an agent-facing proxy, and this talk gives a concrete method for calibrating judges and running simulated multi-turn evals. → *Add a judge-calibration step to AgentOS evals: hand-label about 100 traces, split train/dev/test, report precision and recall with confidence intervals, and only let judges gate releases after they pass.*
- **prosharness** (1/3): ProsHarness runs plan and critique loops, and binary pass/fail checks calibrated on labels may be more useful than free-form scores. → *Try binary pass/fail acceptance checks for ProsHarness checkpoints, calibrated on about 100 labelled runs before they gate a loop.*

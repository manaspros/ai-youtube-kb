# Parameter Golf with AutoResearch — Vayum Arora, Zhengyao Jiang, Dixing Xu & Dhruv Srikanth, Weco AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `7RFJRDYroic` · [watch](https://youtu.be/7RFJRDYroic) · **date:** 2026-10-12 · **length:** 34:13 · **format:** workshop · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Vayum Arora, Zhengyao Jiang, Dixing Xu, Dhruv Srikanth · **orgs:** Weco AI, OpenAI, Modal, Shopify
- **topics:** evals, software-factory, agent-architecture, context-engineering · **tags:** autoresearch, parameter-golf, eval-design, reward-hacking, tree-search, steerability, time-budget, hidden-validation-set, weco, modal

> Hands-on workshop on autoresearch loops, where an agent edits code, a fixed eval scores each attempt, and only improvements are kept. Covers eval design, bounded runs, steerability and the Parameter Golf results.

## Summary
The talk is a workshop from Weco AI on autoresearch: a loop where a language model changes code, runs a replayable eval, keeps changes that raise the score and discards the rest. The speakers explain the OpenAI Parameter Golf challenge (16 MB artifact, 10-minute training, bits-per-byte scored) and how their agent Aden placed as the top contributor. They then describe the anatomy of a run: the editable source file, a fast, cheap, low-noise eval that outputs one scalar, the metric direction, the step count, hard time bounds on the eval, and a guidance markdown file. They stress that agents reward-hack weak evals, and that a tree of attempts with per-node diffs plus the ability to inject ideas mid-run makes the loop usable. The second half is a live demo and a Flappy-Bird-style controller contest scored across four hidden worlds. Much of the content is a product walkthrough for Weco's dashboard, so the reusable part is the design checklist rather than the tool.

## Key ideas
- **Autoresearch is a keep-or-discard loop over code, driven by a replayable eval** — The agent is given code and an eval script, tries ideas, keeps the ones that raise the score, and drops the rest. The speakers say the pattern spread quickly from model training to backend work, prompt and agent tuning, inference speed, and CI/CD. ([0:12](https://youtu.be/7RFJRDYroic?t=12))
- **The agent multiplies your setup, so a weak eval burns tokens** — A normal coding agent is steered step by step. An autoresearch loop runs on its own, so the quality of the eval and the setup matter far more. Pointing it at the right eval lets it search widely; otherwise the run spends tokens for little gain. ([1:47](https://youtu.be/7RFJRDYroic?t=107))
- **Eval design is the most important part of the setup** — The eval should output a single scalar, run fast, cost little, and have low noise. A fast, cheap eval lets you run more steps under the same budget, and low noise lets both the agent and the human trust the hill-climbing. ([11:10](https://youtu.be/7RFJRDYroic?t=670))
- **Agents reward-hack the eval, so harden it** — Agents look for holes in the eval protocol and benchmark. The speaker says the eval should be made as robust as possible before the loop starts. ([12:34](https://youtu.be/7RFJRDYroic?t=754))
- **Bound every eval run in time, and budget the split** — Loops can stall, hardware can fail, and bad code can hang the system. The MiniPG setup allowed 210 seconds: 60 for training, 60 for testing on unseen text, and 90 as a buffer for GPU spin-up and overhead. ([15:02](https://youtu.be/7RFJRDYroic?t=902))
- **Write domain knowledge into a guidance file that steers the search** — The guidance is a markdown file with hard constraints and ideas that seem to work, such as compression, quantization methods, or weight sharing across blocks. This is how a team's prior knowledge enters the loop from the start. ([15:48](https://youtu.be/7RFJRDYroic?t=948))
- **Production-grade needs tree structure, observability and steerability** — Structure means a tree of attempts so ideas compound. Observability means opening any node to read the exact diff behind its score. Steerability means injecting your own idea in plain English mid-run, or budgeting compute per branch when the loop is stuck. ([17:16](https://youtu.be/7RFJRDYroic?t=1036))
- **Human steering picked up an outside idea and produced the largest jump** — Aden's score plateaued for five days (April 15 to 19) across attention, compression and stack changes. A community member shared a tokenizer idea; within eight hours the system fused it with its own work and made the biggest jump in weeks. The speakers present this as the reason steerability matters. ([19:17](https://youtu.be/7RFJRDYroic?t=1157))
- **Use a held-out or hidden eval, and fold multi-objective goals into one scalar** — In the contest, the leaderboard runs on a hidden validation set, so local scores do not match. For several objectives, the speakers suggest either weighting them into one metric or holding one as a constraint, such as model size in Parameter Golf or precision in fraud detection. ([25:12](https://youtu.be/7RFJRDYroic?t=1512))

## Techniques
- **Fixed-budget eval contract** — Give the agent one eval command that prints a single scalar. Set the metric direction (minimise or maximise) and a per-run time limit split across train, test and overhead. Keep the eval cheap and low-noise so more steps fit the budget. *When:* Before starting any autoresearch or automated hill-climbing loop, and for any agent task with a measurable score.
- **Tree-of-attempts search with per-node diffs** — Store each attempt as a node linked to its parent, with its score and code diff. Let the agent branch from high-scoring nodes and prune weak ones. Review the diff of any node when the metric moves. *When:* When a long run produces hundreds of experiments and you need to see what caused each change, or to build on earlier winners.
- **Guidance file as the steering channel** — Put hard constraints, known-good ideas, and known dead ends in one markdown file that the agent reads at start. Mid-run, inject new ideas in plain language to open a new branch. *When:* When you have domain knowledge the agent lacks, or when the loop stalls on one direction.
- **Hidden validation set for contests and benchmarks** — Score the final submission on data the agent never sees. Average across several conditions (the four Flappy worlds) so that a solution overfitted to one condition loses. *When:* When the agent can overfit the public eval, or when the score has to be trusted as a generalisation measure.
- **Constrained single-metric optimisation** — Turn several goals into one metric by weighting them, or keep one as a hard constraint (for example model size under 16 MB) and optimise the other. *When:* When the task has more than one objective and the loop accepts only one scalar.
- **Bridged session for direct steering** — Attach a coding-agent session to the dashboard so that the tree, the metric and the agent's chat are visible together. Use this to redirect the search while it runs. *When:* When you need to watch the search and correct its direction in real time.

## Numbers
- Parameter Golf ran 44 days with 1,016 researchers, 2,048 PRs, and about 250k GPU compute (as stated by the speaker), $1M in compute credits, and 47 merged records from 31 contributors ([5:45](https://youtu.be/7RFJRDYroic?t=345))
- Aden landed 7 merged leaderboard records, twice the next best human, and was cited or built on by 435 downstream participants ([7:11](https://youtu.be/7RFJRDYroic?t=431))
- Aden used 4% of community GPU compute, produced 15% of merged records, and was 3.7x more cost-effective than the field average ([7:11](https://youtu.be/7RFJRDYroic?t=431))
- On OpenAI's MLE-bench, Aid scored about 4x the medal rate of the next best agent ([4:12](https://youtu.be/7RFJRDYroic?t=252))
- Eval time budget: 210 seconds total, split as 60 s training, 60 s test on unseen text, and 90 s overhead for GPU spin-up ([15:02](https://youtu.be/7RFJRDYroic?t=902))
- MiniPG runs used 20 steps as the default; the Flappy contest allowed about 50 steps in 30 minutes, with unlimited steps until end of day ([13:45](https://youtu.be/7RFJRDYroic?t=825))
- Plateau for five days (April 15 to 19) before a community tokenizer idea was picked up within eight hours ([19:17](https://youtu.be/7RFJRDYroic?t=1157))
- Flappy controller is scored as the average over four worlds (normal, moving gap, wind, variable), on a hidden validation set ([30:04](https://youtu.be/7RFJRDYroic?t=1804))

## Hot takes
- Autoresearch is a bigger multiplier on your setup than a normal coding agent, so a poor eval wastes tokens.
- Agents love to reward-hack, so the eval has to be hardened before the loop starts.
- Steerability, meaning a human injecting ideas mid-run, is what makes real breakthroughs happen in autoresearch.

## Tools mentioned
Weco, Modal, Claude Code, Opus 4.8, OpenAI MLE-bench

## Relevance to our work
- **agentos** (2/3): AgentOS has InferCraft and MemoryMesh tuning loops with a single benchmark metric and a fixed budget. The talk's eval contract and per-attempt diff tree apply directly, though the target is code search, not infra. → *Write an eval contract for one InferCraft or MemoryMesh benchmark: single scalar, time budget split across phases, and a hidden holdout set. Log each attempt as a node with its config diff.*
- **prosharness** (2/3): ProsHarness runs long checkpointed agent loops. The talk's time-bounded runs, per-attempt tree log, and mid-run steering are patterns the harness could use. → *Add a per-iteration time cap and a tree-style attempt log with diffs to the ProsHarness loop runner, and allow idea injection while a loop is running.*
- **general** (2/3): The ER autoresearch harness uses the same loop pattern. The talk's advice on eval noise, reward hacking and hidden holdouts applies directly to that work. → *Audit the ER autoresearch eval for reward-hacking holes and check that a hidden holdout is never visible to the agent. Compare the eval's noise against its improvement margin before the next run.*

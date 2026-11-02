# How Autoresearch is changing ML research — Zhengyao Jiang, Weco

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `iCj_ATyThvc` · [watch](https://youtu.be/iCj_ATyThvc) · **date:** 2026-07-18 · **length:** 16:16 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Zhengyao Jiang · **orgs:** Weco, OpenAI, UCL
- **topics:** evals, software-factory, models-research · **tags:** autoresearch, parameter-golf, AIDE, eval-design, data-leakage, reward-hacking, pr-based-collaboration, quantization, code-abstraction, human-ai-collaboration

> Weco's Zhengyao Jiang on AIDE, an autoresearch agent whose PRs won OpenAI's ParameterGolf and got reused by others; humans design the eval and code abstraction while the agent executes.

## Summary
Zhengyao Jiang (CEO of Weco) presents AIDE, a multi-agent autoresearch system that reads papers and public PRs, runs experiments, and submits a PR only after it passes a quality gate. In OpenAI's ParameterGolf challenge (about 1,000 participants, 2,000 submissions, 47 accepted), AIDE placed seven leaderboard records, more than twice the best human's three. He argues the useful metric is whether the community merges and builds on the work, and reports AIDE's PRs had the highest reuse (H-index 10 vs 7 for the next human). Most of AIDE's record ideas came from human papers and community notes that others had dropped, so its main strength is execution. He compares autoresearch to model training: the code abstraction acts as architecture that constrains the search, and the eval acts as the loss function and data. A fraud-detection example shows a loose API let test data leak into training, and a strict API brought leakage to zero. He closes by saying that designing the hill for the agent to climb is becoming a key skill for AI engineers. The figures are self-reported by his company and come from a single competition.

## Key ideas
- **Judge autoresearch by whether humans merge and build on its work, not only by the score it climbs.** — AIDE publishes results as PRs behind a quality gate. Reuse by other participants (H-index over PRs: 10 vs the next human's 7) is the success signal he prefers. ([1:10](https://youtu.be/iCj_ATyThvc?t=70))
- **AIDE is a multi-agent, self-improving loop that reads papers and PRs, runs experiments, and submits only gated findings.** — The gate is the single quality signal. In the 22-day ParameterGolf run it set seven records, each stamped by OpenAI review. ([2:09](https://youtu.be/iCj_ATyThvc?t=129))
- **Most useful ideas come from humans, and the agent's edge is implementing them.** — Most record ideas came from papers and community notes, including ideas a human had dropped because of implementation difficulty. Only a small share were original to the agent. ([5:44](https://youtu.be/iCj_ATyThvc?t=344))
- **Ideas combine with synergy: an architecture idea plus a community tokenizer change gave a jump neither gave alone.** — Gated attention from a Qwen paper broke the 16MB size limit. Adding quantization fixed the size, but the score barely moved. Combining it with a tokenizer improvement from another contributor produced a leaderboard record after about five days. ([6:46](https://youtu.be/iCj_ATyThvc?t=406))
- **Execution is the bottleneck; humans supply the beliefs and ideas, and the agent supplies many executions.** — He says what moves the frontier is usually a belief about existing ideas plus many good executions, and the agent is fast at searching large combination spaces. ([8:51](https://youtu.be/iCj_ATyThvc?t=531))
- **Treat the eval as the loss function and the code abstraction as the architecture.** — The abstraction sets what the agent can explore and biases where the search goes. The eval sets what it optimizes. Competition design and eval design carry the leverage, and a bad design can make community effort useless. ([10:52](https://youtu.be/iCj_ATyThvc?t=652))
- **A loose API lets the agent leak test data into training. A strict API that separates them removes the leak.** — In a fraud-detection preprocessing task, one function handled both train and test data. The score looked great, but test information leaked into training. A stricter API that stopped test data from reaching training brought the leakage rate to zero. He notes that a determined agent can still reward-hack. ([12:55](https://youtu.be/iCj_ATyThvc?t=775))

## Techniques
- **Publish-gated agent output** — Let the agent open PRs only after its findings pass a quality check, so reviewers see a high signal-to-noise stream. Measure impact by reuse, such as an H-index over PRs. *When:* When an autonomous agent's output will be read or merged by other people, and a raw leaderboard score is not enough.
- **Strict eval API that separates held-out data** — Put train and test data behind separate functions, and make it impossible for test data to reach the training path. Check for leakage afterward. *When:* Before running any autonomous optimization loop where the agent can see the score, such as a preprocessing or model search.
- **Recombine community ideas with the agent's own changes** — Collect ideas from papers and other participants, including ones that were abandoned. Have the agent implement each one and test combinations, since pairs can have synergy that neither has alone. *When:* When a search is stuck on a plateau, or when the constraint is execution rather than ideas.
- **Constraint-driven follow-up move** — When a change breaks a hard constraint, such as a size limit, add a simple fix such as quantization, then re-measure the combined result. *When:* When the agent's search runs into a fixed budget such as file size, memory, or compute.

## Numbers
- ParameterGolf: about 1,000 participants, 2,000 submissions, 47 passed OpenAI review onto the leaderboard, 7 of them from AIDE (best human: 3 records). ([0:08](https://youtu.be/iCj_ATyThvc?t=8))
- Run length about 22 days, roughly 1,300 experiments on a single H100 node. ([3:11](https://youtu.be/iCj_ATyThvc?t=191))
- H-index over PRs: AIDE 10, next human 7 (community reuse). ([3:11](https://youtu.be/iCj_ATyThvc?t=191))
- AIDE used at most 4% of the competition's total compute and made about 15% of the leaderboard records. ([4:39](https://youtu.be/iCj_ATyThvc?t=279))
- 28% of AIDE's submissions made the leaderboard, about six times the community average hit rate. ([4:39](https://youtu.be/iCj_ATyThvc?t=279))
- Size limit in the example is 16 MB; the gated-attention idea initially broke it. ([6:46](https://youtu.be/iCj_ATyThvc?t=406))
- Fraud-detection example: a stricter API reduced the data leakage rate to zero. ([14:22](https://youtu.be/iCj_ATyThvc?t=862))

## Hot takes
- Execution, not ideas, is the bottleneck for frontier progress, so humans should focus on designing the eval and abstraction.
- Designing the hill for an agent to climb (eval, abstraction, competition design) is becoming an important AI engineering skill.
- Community reuse of PRs, not benchmark scores alone, should be the success metric for autonomous research agents.

## Tools mentioned
AIDE (Weco's autoresearch agent), H100 GPU node, Quantization, Qwen gated attention (paper idea)

## Relevance to our work
- **agentos** (2/3): The SkillForge open question asks what success signal to use for skill-worthiness. The talk offers downstream reuse (others building on and merging the work) as a measurable signal. → *In SkillForge, test downstream reuse (how often other agents or users build on a skill) as a candidate skill-worthiness signal against the current success-signal options.*
- **general** (2/3): The eval-as-loss-function and abstraction-as-architecture framing, with the leakage example, applies to any autonomous optimization loop and matches the recurring interest in evals for agents. → *Before running any autonomous optimization loop, write the eval behind a strict API that keeps held-out data out of the agent's path, then check the winning run for leakage or reward hacking.*
- **prosharness** (1/3): ProsHarness runs long Claude Code loops with checkpoints. The talk's strict-separation eval lesson could apply to acceptance checks in those loops. → *When writing ProsHarness loop acceptance checks, keep held-out checks out of the agent's reach and look for leakage, following the strict-API example at 12:55.*

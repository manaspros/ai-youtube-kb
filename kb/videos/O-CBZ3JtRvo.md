# Training Frontier Models to Out-Think Hackers — Uri Rolls, Arithmetic & Thom Wolf, Hugging Face

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `O-CBZ3JtRvo` · [watch](https://youtu.be/O-CBZ3JtRvo) · **date:** 2026-08-18 · **length:** 17:28 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Uri Rolls, Thom Wolf · **orgs:** Arithmetic, Hugging Face
- **topics:** security-guardrails, evals, training-finetuning-rl, models-research · **tags:** cybersecurity, benchmark, access-control, zero-day, black-box-eval, partial-credit, open-source-models, post-training, exploit-chain, Mask Off

> Uri Rolls and Thom Wolf present Arithmetic's "Mask Off" benchmark: black-box access-control exploit chains built from real zero-days, graded per step, to test whether models can make logic leaps.

## Summary
The speakers argue cybersecurity is a wide, under-explored field for AI and that open-source models should be part of the defense. Their first benchmark, Mask Off, focuses on access control because it is the first door into most targets and is driven by logic flaws rather than simple code bugs. Each task is a black-box environment (for example Keycloak, Vault and a broker) built from a zero-day the team found themselves, with no internet or source access, and a solve script exists for every task. Every step of the exploit chain has a deterministic grader, plus a final binary pass/fail check on whether an underprivileged user gained a forbidden capability. In a demo, models wandered through the system and reached the right check but failed to make the logical leap of changing the admin's own identity. Per the speaker, the benchmark is very hard: one solve at K1, and only one public model (GPT-5.5) solves it at higher K, though the captions for that remark are garbled. The team measures depth via partial graders, runs evals through an internal orchestrator called Bach, and spends its days reading traces to find failure modes. The closing argument is that speed will decide attack versus defense, so specialized open models on specialized hardware should be trained and offered to companies rather than relying on two closed vendors.

## Key ideas
- **Cyber evals should target access control first** — Access control is the first door into any target, and its flaws are logic breaks between checks spread across big systems, not single bugs. The speaker says these have long topped the OWASP list (captions read 'OS list'). ([7:38](https://youtu.be/O-CBZ3JtRvo?t=458))
- **Use black-box environments built from real zero-days the team found** — Tasks use zero-days the team found and disclosed in widely used open-source software. The model gets no source code or internet, only basic tooling, so it cannot have memorised the bug. ([8:51](https://youtu.be/O-CBZ3JtRvo?t=531))
- **Grade every step, not just the final result** — Each step of the discovery and exploit chain has a deterministic grader, so the eval can say how deep the model got. A final binary check asks whether an underprivileged user did something they were not allowed to do. ([8:51](https://youtu.be/O-CBZ3JtRvo?t=531))
- **The hard part is the logic leap, not the search** — In the demo, models reached the right check and captured the needed information, but never made the leap of changing the admin's own permissions and name to bypass it. Successful models reason across the whole system state. ([10:15](https://youtu.be/O-CBZ3JtRvo?t=615))
- **Human researchers must create out-of-distribution task data** — The team's data comes from human vulnerability researchers who find their own zero-days, because synthetic data is unlikely to contain these new patterns. Each task also ships with a solve script. ([7:38](https://youtu.be/O-CBZ3JtRvo?t=458))
- **Speed, not just capability, decides attack versus defense** — Defenders must see and block an attack as it starts. The speaker argues for specialized, fast models on specialized hardware, trained on open models and offered to any company that needs protection. ([15:08](https://youtu.be/O-CBZ3JtRvo?t=908))

## Techniques
- **Black-box exploit-chain environments from self-found zero-days** — Build a multi-service environment around a real vulnerability you found and disclosed. Give the model only basic tools, with no source code and no internet, and a solve script per task to prove it is solvable. *When:* Benchmarking whether an agent can reason across an unfamiliar system rather than pattern-match known code.
- **Per-step deterministic graders with partial credit** — Attach a verifiable check to each stage of the chain (discovery, then exploitation) and report the furthest stage reached, alongside the binary final pass. *When:* Long multi-step tasks where pass/fail hides real progress and you need to see where the agent stalls.
- **Trace review as the main eval loop** — Read the full traces of each model run to find the specific failure modes, then design environments that isolate them. The speaker says this is most of the team's daily work. *When:* Improving an agent benchmark over time, when aggregate scores do not explain failures.
- **Orchestrator for running evals** — An internal orchestrator (Bach) runs the benchmark and shows results per environment and per step, so model performance can be tracked over time. *When:* Running many environments and models repeatedly and tracking performance across versions.

## Numbers
- Models score about 1-2% on the generic ARC-style interactive world-model benchmark the speaker mentions ([1:35](https://youtu.be/O-CBZ3JtRvo?t=95))
- The exploit chain in the demo task is about 16 steps long ([10:15](https://youtu.be/O-CBZ3JtRvo?t=615))
- At K1 the benchmark has one solve; the speaker says only one public model (GPT-5.5) solves it at higher K ([11:14](https://youtu.be/O-CBZ3JtRvo?t=674))
- An agent run on the hard task FaultLine ran for over three hours without solving it ([13:46](https://youtu.be/O-CBZ3JtRvo?t=826))
- The speaker says access-control vulnerabilities created a roughly $30 billion industry ([7:38](https://youtu.be/O-CBZ3JtRvo?t=458))

## Hot takes
- Defenders can keep up with AI-driven attackers if models get much better at cyber, through high-quality evals and data.
- Open-source models are part of the cyber solution, not a risk to be avoided.
- Relying on two closed-model companies to solve cyber defense is a mistake; speed-specialised open models should be trained and shared.
- Cyber is a game of speed, so specialised models on specialised hardware matter more than general frontier models.

## Tools mentioned
Bach (Arithmetic's internal eval orchestrator)

## Relevance to our work
- **agentos** (1/3): AgentOS has a sandboxed exec layer and exec-gate guardrails (Crucible). Step-level grading of an agent's multi-step attack chain is a relevant eval pattern for that guardrail work. → *Add per-step partial graders to any multi-step agent eval in Crucible, so the report shows how far an agent got before failing, not only pass/fail.*
- **prosharness** (1/3): ProsHarness checkpoints long agent runs. Per-step deterministic checks could serve as checkpoint gates that record how far a run got. → *Consider deterministic per-step checks as checkpoint gates for long ProsHarness runs, so a resumed run restarts from the last verified step.*
- **general** (1/3): Matches the recurring interest in evals for agents. The talk's main lesson is to grade each step of a long chain and read traces, not just score the final output. → *Read the Mask Off benchmark write-up if one is published, and compare its step-graded design with our own agent eval design.*

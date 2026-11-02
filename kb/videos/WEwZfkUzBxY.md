# OpenAI's GPT 6 Astra Is Near "AGI" Level?

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `WEwZfkUzBxY` · [watch](https://youtu.be/WEwZfkUzBxY) · **date:** 2026-09-02 · **length:** 13:55 · **format:** news · **quality:** 3/5 · **depth:** intro
- **speakers:** Kai Explains host (name not stated in transcript) · **orgs:** OpenAI, Anthropic, Google DeepMind, Erdős Problems database (Thomas Bloom)
- **topics:** models-research, evals · **tags:** formal-verification, lean-4, math-ai, openai-astra, erdos-problems, benchmarks, agi-debate, verification-fidelity

> Kai Explains weighs OpenAI's claim that its unreleased Astra model solved 10 open math problems, what Lean verification does and doesn't prove, and why this is not yet evidence of AGI.

## Summary
The video covers OpenAI's August 1 post claiming an internal model (called Astra, not yet public) solved 10 open math problems across eight fields, including a 27-year-old question about sofic groups. OpenAI published the proofs as Lean 4 files on GitHub, and the host stresses that the Lean compiler, not marketing, is what checks them, with zero `sorry` placeholders. He then names the key limit: Lean only checks that the proof follows from the formal statement, so a weakened formalization would still compile. He contrasts this with Thomas Bloom's endorsement and with Bloom's earlier call-out of OpenAI's October 2025 GPT-5 Erdős claims. The cost figure (about $2,000) excludes failed searches, and a mathematician at Anthropic reportedly reproduced 5 of 10 proofs within a day with a public model, offering either corroboration or evidence that the ceiling is lower than advertised. Counterweights include Terence Tao's sealed set of live problems, which AI models failed, and the Riemann Bench climb from about 6% to the 60s and 70s in months. The host's conclusion: the evidence shows strong search over defined problems, not open-ended choice of problems, so it is not proof of AGI.

## Key ideas
- **OpenAI claims an unreleased internal model (Astra) solved 10 open math problems across eight fields, announced in an August 1 post.** — Results include the first non-sofic group construction (a question open since Gromov's 1999 introduction of sofic groups), a disproof of a 1980 rigidity conjecture (caption reads 'Kahn'), the first sphere-packing improvement in high dimensions since 1978, and three Erdős problems. ([0:00](https://youtu.be/WEwZfkUzBxY?t=0))
- **The proofs are published in Lean 4 under an open license, so the check is mechanical rather than reputational.** — Anyone can build the repo and see whether Lean accepts it. The host reports zero `sorry` placeholders across all 10 proofs, meaning no step was skipped. ([2:40](https://youtu.be/WEwZfkUzBxY?t=160))
- **Lean verifies the proof, not the question. Formalization fidelity remains a human judgment.** — If the formal statement is accidentally weaker than the original conjecture, Lean can produce a flawless proof of the wrong thing. Whether the 10 formalizations match the originals still needs working mathematicians. ([4:06](https://youtu.be/WEwZfkUzBxY?t=246))
- **Thomas Bloom's endorsement carries weight because he previously called out OpenAI.** — In October 2025, OpenAI (via Kevin Weil) claimed GPT-5 solved 10 open Erdős problems. Bloom found it had located existing literature solutions and called it a dramatic misrepresentation. This time he called the August results big news. ([5:27](https://youtu.be/WEwZfkUzBxY?t=327))
- **The $2,000 compute figure is incomplete: it covers only successful runs.** — Noam Brown noted that failed search attempts were excluded, and their cost was not disclosed. The human contribution to final write-ups was also not quantified. ([6:51](https://youtu.be/WEwZfkUzBxY?t=411))
- **A public model reportedly reproduced 5 of the 10 proofs within a day, which cuts both ways.** — An Anthropic mathematician used a generic prompt with internet access off. The host reads this as strong outside corroboration, and also as evidence that the ceiling may be lower than the announcement suggests, with several systems reaching a similar threshold. ([8:10](https://youtu.be/WEwZfkUzBxY?t=490))
- **Tao's sealed test of live research problems is the counterpoint: current AI failed every one.** — Terence Tao and colleagues used 10 unsolved problems from their own work under a fixed window. Single AI prompts failed all of them. The host reads this as the gap between searching a defined space and choosing a direction. ([9:26](https://youtu.be/WEwZfkUzBxY?t=566))
- **The key distinction is between solving a well-defined hard problem and deciding which problems are worth solving.** — The first capability has strong evidence. The second, open-ended selection, has much weaker evidence, because humans chose, formalized, and wrote up the problems. The host argues the AGI question shifts to whether AI can select its own targets. ([11:48](https://youtu.be/WEwZfkUzBxY?t=708))

## Techniques
- **Check formal proofs for sorry placeholders and compile them** — Build the published Lean 4 repository and grep for `sorry`. A compiling proof with zero `sorry` means no gaps. The compiler verifies every step, so no trust in the author is needed. *When:* Evaluating any AI claim to have proved a result, when a formal artifact is published.
- **Audit the formal statement against the original problem** — Compare each Lean theorem statement to the original conjecture's wording, checking for weakened hypotheses or a changed scope. Compilation alone does not establish that the right problem was proved. *When:* Whenever a formal proof is used as evidence, since a fidelity error passes the checker silently.
- **Corroborate with an independent model under constraints** — Give a different model a generic prompt with internet access disabled and see whether it reproduces the same results. Overlap across independent systems is evidence that the underlying result is real. Partial overlap also gives a rough lower bound on difficulty. *When:* Assessing a headline result from one lab, particularly when the result is verifiable.
- **Report total cost including failed attempts** — Count the search or retry spend across all attempts, not just the successful run. The host argues the successful-run cost understates the real cost of discovery. *When:* Interpreting efficiency or cost claims for search-heavy agent runs.
- **Separate solving-defined-problems from choosing-problems in evaluation** — Design evals in two tiers: well-specified targets (search and proof success) and open-ended tasks where the agent must pick the target. Do not let high scores on tier one imply tier two. *When:* Designing evals or benchmarks for research-style or autonomous agents.

## Numbers
- OpenAI claims 10 solved open problems across 8 fields, from an internal model called Astra. ([0:00](https://youtu.be/WEwZfkUzBxY?t=0))
- One problem had been open for 27 years (the sofic group question, introduced in 1999). ([0:00-1:16](https://youtu.be/WEwZfkUzBxY?t=0))
- The first sphere-packing improvement in high dimensions since 1978. ([1:16](https://youtu.be/WEwZfkUzBxY?t=76))
- The Erdős unit distance conjecture, open since 1946, was disproved by an internal OpenAI model in May. ([5:27](https://youtu.be/WEwZfkUzBxY?t=327))
- Compute cost for the 10 proofs was about $2,000 at current API rates. It excludes failed runs, and the total is undisclosed. ([6:51](https://youtu.be/WEwZfkUzBxY?t=411))
- A public model reproduced 5 of 10 proofs within 24 hours. ([8:10](https://youtu.be/WEwZfkUzBxY?t=490))
- Tao and colleagues' sealed set of 10 live research problems: AI models failed all of them. ([9:26](https://youtu.be/WEwZfkUzBxY?t=566))
- Riemann Bench: 25 new problems. Best score at launch about 6% (none reached 10%). By mid-year, top scores in the 60s and 70s. ([10:22](https://youtu.be/WEwZfkUzBxY?t=622))

## Hot takes
- The verification story (Lean, zero sorry) is strong, but Lean cannot check that the formal statement matches the original problem, so the Astra result is not fully established yet.
- Solving a hard, well-defined problem is not the same as deciding which problem is worth solving. The AGI question depends on the second capability, where evidence is weaker.
- The video says 'I wouldn't call this proof of AGI. I'd call it AI moving from solving problems to participating in research.'
- A public model reaching half the results in a day could mean the ceiling is lower than OpenAI's framing, or that several systems are reaching the same threshold at once.

## Tools mentioned
Lean 4 (formal proof checker, with public GitHub repo of proofs), Astra (OpenAI internal model, unreleased, per the video), GPT-5 (cited for the October 2025 Erdős claim), Fable (named in the video as Anthropic's publicly available model; the name may be a caption error for Claude, which the host did not confirm), Riemann Bench (25 newly written research-level math problems), Erdős Problems database

## Relevance to our work
- **agentos** (1/3): The Lean point, that a checker passes a weakened formal statement, is relevant to correctness and RAGAS-style evals: a green check does not prove the spec was right. → *When designing AgentOS correctness checks, record how each check's spec maps to the original requirement, and test that mapping separately from the checker's pass/fail.*
- **prosharness** (1/3): Independent verification of an agent's 'done' claim, with a checker separate from the author, parallels ProsHarness's plan, critique, and debate steps. The talk gives no concrete harness design. → *Consider a separate verifier pass for long agent runs before marking them complete, as an extension of the plan to critique step.*

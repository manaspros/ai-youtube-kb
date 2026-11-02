# Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers — Varun Pant, AWS

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `lRa9sPaMyy4` · [watch](https://youtu.be/lRa9sPaMyy4) · **date:** 2026-09-18 · **length:** 10:07 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Varun Pant · **orgs:** AWS
- **topics:** testing-verification, coding-agents, context-engineering · **tags:** formal-verification, lean, spec-driven-development, differential-testing, smt-solvers, verus, aeneas, rust, cedar, strata, z3

> Varun Pant (AWS) argues that formal verification in Lean, Verus and similar tools can prove code correct for all inputs, which tests and LLM judges cannot, and that humans should own the specification while agents write code and proofs.

## Summary
The speaker says coding agents now produce far more code than humans can review, and that tests, LLM-as-judge and human review cannot show correctness for all inputs. Formal verification gives a mathematical proof against a written specification, so a passing proof holds for every input. His workflow is spec-driven: a human writes or checks the specification (possibly auto-formalised by AI from natural language), the agent implements it, and a prover checks the implementation against the spec. He introduces Lean as both a programming language and a proof assistant with a small trusted kernel, and explains proof search as a chess-like tree of tactics with backtracking. Three examples follow: an AI-translated zlib in Lean with a 32,000-line proof, Cedar (AWS authorization policy language) with a Lean spec checked against Rust by nightly differential testing, and Verus/Aeneas for Rust using pre- and post-conditions and solvers such as Z3. He closes by presenting Strata, a work-in-progress intermediate representation that lowers any language to a common core dispatched to Lean, SMT solvers or model checkers.

## Key ideas
- **Tests, LLM-as-judge and human review are not enough for agent-written code** — Tests check only some inputs, LLM judges are probabilistic, and human review does not scale to agent speed. Formal verification is the only one of these that can state correctness for all inputs. ([0:08](https://youtu.be/lRa9sPaMyy4?t=8))
- **Humans own the spec, machines own the code and the proof** — The specification is the upstream artifact that everything else depends on. It is either written formally or auto-formalised from natural language, then validated by a human or by testing it on sample inputs. The agent implements from it and the prover checks the match. ([1:16](https://youtu.be/lRa9sPaMyy4?t=76))
- **Lean puts definitions and proofs in one language with a small trusted kernel** — There is no translation layer between code and proof. Proofs can be exported and re-checked independently, and only the small kernel has to be trusted. Anyone can write an independent kernel, and kernels exist in C++, Rust and Lean. ([2:20](https://youtu.be/lRa9sPaMyy4?t=140))
- **Proof search is a game tree of tactics** — The speaker compares tactics to chess moves on an interactive board. The prover tries a tactic, backtracks when a goal cannot be proved, and tries another branch until the theorem is closed. The kernel then checks the result, and a wrong proof is rejected immediately. ([3:23](https://youtu.be/lRa9sPaMyy4?t=203))
- **AI can verify a whole real library by decomposing it into lemmas** — An AI turned a natural-language spec of zlib decompression into a formal spec, wrote the Lean code, generated helper lemmas as subgoals, proved each one with tactics and assembled the final theorem. The human checks the formal spec, not the proof steps. ([4:23](https://youtu.be/lRa9sPaMyy4?t=263))
- **Keep a formal spec next to production Rust and test them against each other** — Cedar's production code runs in Rust while its functional specification is written in Lean. Differential random testing runs both on the same inputs, and the speaker says about 100 million such tests run nightly. No version ships until they agree. ([5:48](https://youtu.be/lRa9sPaMyy4?t=348))
- **Solvers act as calculators that answer satisfiable or unsatisfiable** — Verus uses annotations (requires and ensures) that the Z3 solver checks statically. They are erased at runtime, so they behave like ghost code. Aeneas translates Rust's mid-level IR into Lean for proving. ([6:49](https://youtu.be/lRa9sPaMyy4?t=409))
- **Lower every language into one shared core IR and dispatch it to many engines** — Strata lets you define a dialect for a language and lower it to Strata Core, which is written in Lean. From there the same program can go to the Lean prover, an SMT solver or a model checker. The speaker says this is still work in progress. ([8:42](https://youtu.be/lRa9sPaMyy4?t=522))

## Techniques
- **Spec-first verified agent coding** — Write what correct means as a specification (in Lean, or in natural language that AI auto-formalises). Validate the spec by human review or by testing it on some inputs. Let the coding agent implement it, then have a formal verifier prove the implementation meets the spec. *When:* Critical code where a wrong answer is costly, and where the agent writes most of the code, so the human needs a checkable point of control.
- **Spec model plus differential random testing** — Keep a functional spec (for example in Lean) alongside production code (for example in Rust). Run both on the same random inputs each night and block releases until their outputs match. *When:* The production code is too big to verify in full but has a clear reference model, as with Cedar's authorization engine.
- **Lemma decomposition for AI proofs** — Ask the AI to split a theorem into helper lemmas (subgoals), prove each one with tactics, then combine them into the final theorem. The kernel checks the final result. *When:* Large proofs, such as the 32,000-line zlib example, where one proof attempt is too large to handle at once.
- **In-code pre- and post-conditions checked by a solver** — Add requires and ensures annotations next to the Rust code. The verifier checks them with a solver such as Z3 at build time and erases them at runtime. *When:* Rust code where you want static guarantees without runtime cost and with less proof work than an interactive prover needs.
- **Intermediate-representation dialect to many backends** — Define a dialect for each source language, lower it to a shared core IR, then send that core to whichever engine fits: an interactive prover, an SMT solver or a model checker. *When:* Several languages or many programs need verification with one toolchain (Strata is the example).

## Numbers
- Builders generate hundreds and thousands of PRs every week (speaker's framing of the problem) ([0:08](https://youtu.be/lRa9sPaMyy4?t=8))
- AI converted zlib to Lean over about a week, with a 32,000-line proof checked by the kernel ([4:23](https://youtu.be/lRa9sPaMyy4?t=263))
- Cedar runs about 100 million differential random tests nightly; no version ships until they pass ([5:48](https://youtu.be/lRa9sPaMyy4?t=348))
- Video length 10:07 ([0:00](https://youtu.be/lRa9sPaMyy4?t=0))

## Hot takes
- Tests only check some inputs, LLM-as-judge is probabilistic and human review cannot match agent speed, so formal proof is the only way to say code is correct for all inputs.
- Humans should own the specification and machines should own the code and the proof.
- The goal is software that is probably correct in a provable sense, not just probably correct.

## Tools mentioned
Lean, Lean 4 browser playground, Kiro (transcript shows 'Kero', likely the AWS agentic IDE), Verus, Z3, Aeneas, Strata / Strata Core, Cedar, SMT solvers, model checkers, ArenaLang (kernel registry)

## Relevance to our work
- **general** (2/3): The core idea, that a human owns a validated spec and the agent implements against it with an automatic check, applies to any agent-written code. The formal tooling is heavy, but the workflow is portable. → *Pick one critical module, write its invariants as property tests (or pre/post-condition asserts) before the agent implements it, and check whether the agent's code passes them.*
- **agentos** (1/3): L1 policy checks and L2C exec-gate guardrails are rules that could be written as formal properties, but the talk does not address runtime agent policy. → *Read the Cedar differential-testing section and consider whether one exec-gate rule could be written as a spec and checked against its implementation with random inputs.*
- **prosharness** (1/3): ProsHarness has a plan step followed by a critique step. The talk's human-validates-the-spec-before-implementation idea is close to that, but its checks are formal. → *Consider adding a spec-validation checkpoint before the implementation step of a long run, with a check that is lighter than full proof.*

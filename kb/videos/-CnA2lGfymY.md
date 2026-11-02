# "I've never seen anything scarier than an LLM with tool calls." — Erik Meijer aka @HeadinTheBox

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `-CnA2lGfymY` · [watch](https://youtu.be/-CnA2lGfymY) · **date:** 2026-07-18 · **length:** 21:13 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Erik Meijer · **orgs:** Leibniz Labs, OpenAI, Anthropic
- **topics:** security-guardrails, testing-verification, agent-architecture · **tags:** formal-verification, lean, dafny, free-monad, tool-calls, lethal-trifecta, proof-carrying-code, taint-analysis, plan-execution-split, agent-safety

> Erik Meijer shows how to make agent tool calls provably safe by turning the plan into a program that can be type-checked, taint-analysed and proven before anything runs.

## Summary
Meijer frames tool calls as the point where LLM safety stops being a philosophical question and becomes a real risk, because the model's output can now have side effects on files, money and databases. He argues that alignment and LLM-as-judge checks cannot formally guarantee safety. He then walks through a Lean/Dafny-style example: the model should not run the agentic loop directly, but should return a plan as data, which a separate executor runs only after a check. He says the plan should be a program in a small effect language (a free monad idea), so that data-flow analysis and type checking can run on it without executing it. He ends with proof-carrying code, where the model returns a program plus a proof that a checker validates, and he concludes that agents should be treated as dangerous until proven safe, and that languages should be designed for machines to write and check rather than for humans. The talk is a conceptual tutorial with jokes and no product pitch, and it gives no measured results or working implementation details.

## Key ideas
- **Tool calls change the risk. Adding tools turns a pure text function into one with side effects, so the danger is what the model does, not what it says.** — Speaker compares the LLM signature to a Lean IO type. Once the model can act on files, money or databases, a safe-looking answer does not protect the user from an unsafe run. ([10:47](https://youtu.be/-CnA2lGfymY?t=647))
- **Air-gap the agentic loop from the agent. The model should produce a plan as data, and a separate executor runs it only after a check.** — Speaker calls this pushing the IO to the right. The plan can be inspected before any side effect happens. ([14:52](https://youtu.be/-CnA2lGfymY?t=892))
- **The plan should be a program, not an opaque action. A program can be analysed, but a black-box IO value cannot be reasoned about.** — Speaker says Lean treats IO A as a black box. Representing the computation as an expression tree (a free monad in his terms) lets the checker walk it for type errors and data flow. ([17:18](https://youtu.be/-CnA2lGfymY?t=1038))
- **Taint analysis on the plan can address the lethal trifecta: private data, untrusted content and tools together.** — Speaker credits Simon Willison's lethal trifecta framing and says that analysis over the program can flag flows from untrusted input into dangerous operations. ([15:51](https://youtu.be/-CnA2lGfymY?t=951))
- **Proof-carrying output: the model returns the program together with a proof of safety, and a checker validates the proof instead of trusting the model.** — Speaker says the technique dates to academic work in the 1990s and that he is borrowing it. He demos a simple inductive interpreter and inductive proof that models can generate. ([18:40](https://youtu.be/-CnA2lGfymY?t=1120))
- **Design languages for machines. Models write these languages and checkers consume them, so human readability matters less than checkability.** — Speaker's closing rule is that agents are dangerous until proven safe, and that a human-facing language is not needed if a machine generates, checks and proves it. ([19:38](https://youtu.be/-CnA2lGfymY?t=1178))

## Techniques
- **Plan as data, execute after check** — Have the model emit a structured plan (an expression tree or a DSL program) instead of performing tool calls in its loop. A separate interpreter runs the plan only after the checks pass. *When:* Any agent with side-effecting tools where a human or deterministic gate should see the actions before they run.
- **Taint or data-flow analysis over the plan** — Walk the plan's expression tree and mark values that come from untrusted sources (retrieved content, tool output, user text). Reject plans where those values reach write, exec or send operations, or where private data flows out with tools. *When:* Agents that read private data and untrusted content and also have tools, the lethal trifecta setup.
- **Proof-carrying generation** — Ask the model to return the program plus a machine-checkable proof of a property such as safety. A checker verifies the proof independently of the model. *When:* High-stakes actions where the safety property can be written as a formal spec. Speaker notes that free-form properties like 'the answer is safe' cannot be specified this way.
- **Effects as data (free monad style)** — Model side effects as constructors of a data type, with one interpreter for real execution and another for analysis, linting or dry-runs. *When:* When you need to inspect or simulate what an agent would do before doing it.

## Numbers
- ChatGPT-style chat interface launched on November 30, 2022, described as the first time people could speak to their computer. ([3:51](https://youtu.be/-CnA2lGfymY?t=231))
- OpenAI added tool call support to GPT-4 in June 2023, and other vendors copied the API shape, which the speaker calls minimum differentiation. ([10:47](https://youtu.be/-CnA2lGfymY?t=647))
- Speaker says there are at least 100 startups in the exhibition hall using LLMs as judges for safety. ([9:27](https://youtu.be/-CnA2lGfymY?t=567))
- Talk length is 21 minutes 13 seconds, billed as a 20-minute tutorial. No benchmarks or measured results are given. ([0:08](https://youtu.be/-CnA2lGfymY?t=8))

## Hot takes
- An LLM with tool calls is scarier than anything else in AI, and tool calls are like handing the model a loaded gun.
- Safety that can only be stated as 'the answer is safe' cannot be formally specified, so LLM-as-judge is a weak substitute.
- Prompt injection is a bigger problem than SQL injection because LLMs do not separate code from text.
- Agents should be treated as dangerous until proven safe.
- Languages should stop being designed for humans, since models write them and checkers consume them.

## Tools mentioned
Lean, Dafny, Isabelle, PVS, TLA+, Claude Code

## Relevance to our work
- **agentos** (2/3): Crucible exec-gate guardrails need a way to decide what an agent may run. Plan-as-data plus taint checks over the plan is a concrete pattern for that gate. → *Prototype a Crucible exec-gate that takes the agent's proposed tool calls as a structured list, then rejects any plan where a value from retrieved or tool-output content reaches a write or exec tool, before the executor runs.*
- **prosharness** (2/3): ProsHarness already runs plan, then critique, then debate before execution. The talk's split between a plan that is data and an executor that runs it after checks fits that flow. → *Make the plan step emit a machine-readable list of tool actions with a tag for each (reads private data, reads untrusted content, side effect), and add a deterministic check that blocks any plan containing all three before the Claude Code run starts.*

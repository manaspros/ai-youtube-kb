# How to Test AI Agents When No Benchmark Exists — Nathanael Weill, Air Canada

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `c_SPW__jF9w` · [watch](https://youtu.be/c_SPW__jF9w) · **date:** 2026-10-22 · **length:** 19:50 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Nathanael Weill · **orgs:** Air Canada
- **topics:** evals, rag-retrieval, enterprise-adoption · **tags:** evaluation-without-benchmark, synthetic-test-generation, known-answer-tests, rag-eval, llm-as-judge-avoidance, invariance-testing, contract-analysis, bm25, chunking, embedding-model, test-sets, expert-in-the-loop

> Air Canada's data science team explains how they built evaluation sets with no public benchmark: generate test cases from known answers, grade them with code, and avoid LLM-as-judge.

## Summary
Nathanael Weill, who works on data science at Air Canada, describes how his team evaluated agents for narrow business tasks where no public benchmark exists and domain experts have limited time. His RAG story from a telecom Q&A project is the core lesson: generate a question from a known source page, then check whether the agent retrieves and answers from that page, which turned one expert evaluation a week into dozens a day. The team says removing complexity helped more than published techniques, which often broke other things. For the Air Canada supplier-contract analysis agent, they generate known-answer tests by planting rule violations, removing clauses from signed contracts, and filling expert templates with values, and they add invariance checks such as renaming a supplier or reordering clauses. Where possible they grade with code instead of LLM judges, because judge noise was about as large as the agent's own noise. Expert feedback is used to write better tests and prompts rather than to patch outputs, and the speaker says passing the tests is a starting point, not a go/no-go.

## Key ideas
- **If you cannot grade the agent, you cannot improve it. The speaker's core rule from a 2024 RAG project, carried into a 2026 contract agent.** — They had no test set and no access to experts for grading, so the team judged five chatbot answers side by side in weekly meetings. Expert opinions disagreed, and the budget allowed one trial a week. ([0:08](https://youtu.be/c_SPW__jF9w?t=8))
- **Reverse the eval: start from a source page, generate a question from it, then check that the agent finds the answer. This is the 'answer first' pattern.** — An LLM writes a question about a page that is already known. The agent must retrieve and answer it, and code compares the result against the source page. This turned one evaluation a week into dozens a day, and accuracy rose across weeks. ([5:45](https://youtu.be/c_SPW__jF9w?t=345))
- **Complexity often breaks more than it fixes. Tuning basics (embedding model, chunking, BM25 alpha) gave more value than published advanced techniques.** — The team tried techniques from papers. They did not improve their system, and each added layer broke something that had worked before. Removing layers helped. ([3:43](https://youtu.be/c_SPW__jF9w?t=223))
- **For the contract agent, a diff of an original contract against the signed version is the ideal test, but it is not available because the company keeps only the latest version.** — The agent has four steps: spot clauses in a contract, find supporting documents for an amendment, write the amendment, and classify whether to keep it. Without version pairs, the team planted known problems instead. ([9:45](https://youtu.be/c_SPW__jF9w?t=585))
- **Plant rule violations in generated contracts to make labelled tests. The team wrote 275 tests with known answers, and the agent missed most clauses that had been removed.** — Each rule, such as a $1M cap, becomes a generated clause that either breaks or follows it. The removed-clause test, which mixes in clean contracts to measure false flags, showed the strongest gap. ([12:19](https://youtu.be/c_SPW__jF9w?t=739))
- **Invariance checks catch inconsistency. Output should not change when irrelevant fields change, and each check is graded by code.** — The team renames a supplier or changes its address, reorders clauses, and reruns the same contract. The flag count should stay the same. Code checks these results, and none of them need an LLM judge. ([14:51](https://youtu.be/c_SPW__jF9w?t=891))
- **Avoid LLM-as-judge where possible. Exact-match and code graders are fast, but judge noise was as large as the agent's own noise.** — Finding the right judge harness was described as almost as hard as solving the original problem. Fact-checking and similar padding were tried, but the team did not find one that worked for this project. Feedback cycles moved from about four weeks of expert review to a five-minute script run. ([16:19](https://youtu.be/c_SPW__jF9w?t=979))
- **Use expert feedback to improve the tests and prompts, not to hand-patch agent outputs. Passing the tests is a starting point, not a go/no-go.** — Each loop produces better tests, better prompts, and better ideas for removing clauses. Some designs had to change because they could not be evaluated, and the team accepted slightly different designs that could be. ([18:47](https://youtu.be/c_SPW__jF9w?t=1127))

## Techniques
- **Answer-first synthetic eval for retrieval QA** — Pick a source page or document. Have an LLM write a question whose answer is on that page. Run the agent on the question. Check in code whether the agent retrieved the source and answered consistently with it. Keep the set as a regression suite. *When:* A RAG or QA system over a corpus where no labelled Q&A set exists and experts are scarce.
- **Plant-the-defect known-answer tests** — Write the business rules as explicit checks, such as a $1M cap. Generate inputs that either violate a rule or comply with it, so each input has a known expected output. Mix in clean inputs to measure false flags. Count how many planted defects the agent catches. *When:* The domain rules are known or can be written down, but no labelled examples exist.
- **Remove-a-clause mutation test** — Take a signed, compliant document. Delete one clause. Expect the agent to flag the missing clause. Run the same test on clean documents to measure false positives. *When:* You have compliant examples and want to test whether the agent notices omissions, not only bad text.
- **Template fill-in combinatorics** — Take the expert-maintained templates with blank fields. For each blank, define an array of candidate values, some of which break a rule. Generate combinations. Compute the expected label from the chosen values in code. *When:* Experts already use templates, so the generation work is mostly reused.
- **Invariance tests** — Change irrelevant input features, such as the supplier name, the address or clause order. Rerun the same input several times. Assert that the key outputs, such as flag counts, are unchanged. Use code to compare results. *When:* The output should depend only on the substance of the input, not on incidental fields or run-to-run randomness.
- **Trajectory checks for tool-using agents** — Define the expected sequence of endpoints for a task. Generate a scenario with an LLM. Run the agent and inspect its trace against the expected sequence. *When:* The agent must call a fixed set of APIs in a required order.
- **Prefer code graders over LLM-as-judge** — Where the expected answer can be computed, compare it with exact match or code. Use an LLM judge only when no code check is possible, and measure its noise against the agent's noise first. *When:* Any eval where a deterministic check exists, which the speaker treats as the default.
- **Strip complexity before adding techniques** — Remove layers from the pipeline and tune the basics first: embedding model, chunking and the BM25 alpha weight. Add a technique only when the eval shows it helps. *When:* A pipeline has grown complex, and each change breaks something else.

## Numbers
- Telecom Q&A corpus of about 10,000 vendor and engineering documents. ([1:11](https://youtu.be/c_SPW__jF9w?t=71))
- Before the change, the team could run one expert-graded trial per week (budget of one trial a week). ([4:43](https://youtu.be/c_SPW__jF9w?t=283))
- Eval throughput went from one evaluation a week to dozens a day with the answer-first pattern. ([6:45](https://youtu.be/c_SPW__jF9w?t=405))
- The planted-defect suite had 275 generated tests with known answers. The agent missed most of the removed clauses. ([13:20](https://youtu.be/c_SPW__jF9w?t=800))
- Expert feedback cycle was about four weeks, versus a five-minute script run for the generated tests. ([16:19](https://youtu.be/c_SPW__jF9w?t=979))
- The speaker's rule of thumb: if the right document is found, the answer is right about 90% of the time, so retrieval is the main challenge. ([3:43](https://youtu.be/c_SPW__jF9w?t=223))
- Competition: two external teams and one internal team built systems for the same task in sequence. The speaker says his team's system worked and was used, though he does not know exactly why. ([2:12](https://youtu.be/c_SPW__jF9w?t=132))

## Hot takes
- If you cannot grade the agent, you cannot make it better.
- Complexity often breaks more than it fixes; basic retrieval tuning mattered more than published techniques.
- LLM-as-judge noise was as large as the agent's own noise, so it is a hard tool to get right.
- Passing your own generated tests is a starting point, not a go/no-go for shipping.

## Tools mentioned
BM25, LLM-as-judge, Text-to-SQL (mentioned as an example pattern)

## Relevance to our work
- **agentos** (2/3): MemoryMesh is hybrid BM25 plus pgvector retrieval with RAGAS evals. The answer-first generated question set and the warning against LLM-as-judge fit directly. → *Build a generated question set from MemoryMesh knowledge-bucket documents, where each question has a known source chunk, and use it as a regression suite for BM25/pgvector weight and chunking changes.*
- **prosharness** (2/3): ProsHarness plans, critiques and ranks skills. Known-answer and plant-the-defect tests fit testing whether plan critique and skill ranking catch deliberately planted flaws. → *Create a set of plans with deliberately planted flaws and check whether the critique step (and skill ranking) flags them, with code-based grading rather than an LLM judge.*

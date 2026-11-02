# Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `HEFSExa0xl0` · [watch](https://youtu.be/HEFSExa0xl0) · **date:** 2026-07-18 · **length:** 19:09 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Nuno Campos · **orgs:** Witan Labs
- **topics:** agent-architecture, mcp-and-tools, testing-verification, evals · **tags:** spreadsheets, REPL, code-mode, persistent-state, verification-loop, formula-engine, render-engine, golden-spreadsheet-eval, LLM-as-judge, domain-knowledge-prompts, trace-review, tool-consolidation

> Witan Labs on lifting coding agents' spreadsheet accuracy from about 50% to 92% by replacing 15 tools with one persistent-state REPL, plus a formula engine and render engine as the verification loop.

## Summary
Nuno Campos of Witan Labs describes four months spent making coding agents as good at spreadsheets as they are at general code, measured on an internal financial-analysis benchmark that went from about 50% to 92%. Early attempts failed: a rigid three-agent edit pipeline, and many spreadsheet representations (SQL, XML) that did not work alone. CSV/TSV views and an HTML-style layout idea were useful only as parts of a larger solution. The biggest gain came from replacing roughly 15 tools with a single persistent-state Node.js REPL, where each old tool became a JavaScript function the agent composes in one call, with the spreadsheet logic implemented in C#. Accuracy then rose to 74% from the REPL alone, and further gains came from fuzzy search, formula dependency tracing, prompt changes and bug fixes. The speaker stresses a verification loop built on a high-fidelity formula engine and a renderer that shows the sheet as an image, and notes that low-fidelity engines hurt results. For evaluation, the team began with LLM-as-judge and moved to deterministic golden-spreadsheet input/output checks where possible. The talk closes with the advice to read traces, since infrastructure bugs often look like model reasoning failures.

## Key ideas
- **Many sequential or parallel tool calls mean you have built a bad scripting language; give the agent a real one.** — Before the REPL, agents needed 10-15 tool calls to explore a sheet, often timing out. Parallel tool calls did not help because results could not be combined. One code call that composes the steps fixed this. ([16:43](https://youtu.be/HEFSExa0xl0?t=1003))
- **Replacing about 15 tools with one persistent-state REPL was the largest single gain.** — Each old tool became a JavaScript function callable inside one REPL call. Persistent state means variables survive between calls, so the agent builds on earlier work. Accuracy went from about 50% to 74% from this change alone. ([4:55](https://youtu.be/HEFSExa0xl0?t=295))
- **Adding a capability is a type-definitions change, not a new tool.** — New methods, such as formula dependency exploration, are added to the REPL and described in a TypeScript type definitions file placed in the prompt. The tool schema stays the same size. ([7:45](https://youtu.be/HEFSExa0xl0?t=465))
- **A verification loop is the durable part, and it only works if the engines are high fidelity.** — A formula engine recalculates results and a render engine turns a range into an image with formatting. An engine that implements only about 50% of Excel formulas makes results worse, because the agent trusts formulas that then fail or give wrong values. ([10:11](https://youtu.be/HEFSExa0xl0?t=611))
- **Representations that look good in theory often fail; the useful ones were pieces of a larger system.** — SQL and XML (the on-disk format of Excel) did not work as standalone representations. CSV/TSV views were used often but were not enough alone, and an HTML-like layout idea led to the render engine. ([2:34](https://youtu.be/HEFSExa0xl0?t=154))
- **Prefer deterministic evals, and check traces because infrastructure bugs look like model failures.** — LLM-as-judge scores can shift because the judge changed, not the agent. Golden spreadsheets used as black boxes (same inputs, compare outputs) were more trustworthy where they applied. Retries that look like model stupidity were often tool failures. ([14:11](https://youtu.be/HEFSExa0xl0?t=851))

## Techniques
- **Single persistent-state REPL instead of many tools** — Expose each former tool as a function inside one JavaScript REPL tool. Keep state across calls. Give the model a TypeScript type-definitions file to learn the available methods. Keep the scripting language separate from the implementation language (here, C# behind the REPL). *When:* When an agent needs many tool calls that depend on each other, or when tool schemas keep growing as capabilities are added.
- **Verification loop with domain engines** — Build or reuse a formula calculator and a renderer that shows a range with formatting as an image. The agent edits, checks the result, and fixes the formula or formatting when the check fails. *When:* When the domain has no existing compiler, linter or tests to close the feedback loop, and the engine must be high fidelity.
- **Golden-spreadsheet black-box evaluation** — Take a reference file with known inputs and outputs. Put the same inputs into the agent-produced file and compare outputs. Use LLM-as-judge only where no deterministic check is possible. *When:* When you need evals whose scores do not drift because the grader changed.
- **Domain-knowledge reminders in the prompt** — Add short notes that point the model to the concepts that matter for the task (such as ARR or net revenue). Frame them as directing attention rather than teaching. Keep them portable across interface designs. *When:* When the model knows the concepts but needs help choosing the right one for a specific task.
- **Trace review for plumbing bugs** — Read agent traces to tell model mistakes from bugs in tools, skills or prompts. Fix the plumbing when the model is following a bad example or retrying a failing tool. *When:* When an agent looks unreliable or repeats the same action, before tuning the model or the prompt.

## Numbers
- Accuracy on an internal financial-analysis benchmark went from about 50% to 92% over four months. ([0:00](https://youtu.be/HEFSExa0xl0?t=0))
- Accuracy was 74% after the REPL change, before later changes brought it to 92%. ([7:45](https://youtu.be/HEFSExa0xl0?t=465))
- About 15 separate tools were replaced by one REPL tool. ([4:55](https://youtu.be/HEFSExa0xl0?t=295))
- Before the REPL, an agent often needed 10-15 tool calls to explore a spreadsheet, and tasks often hit the 5-minute timeout. After the change, timeouts were reportedly zero. ([9:12](https://youtu.be/HEFSExa0xl0?t=552))
- REPL scripts were shorter than the pure code-mode scripts, which often ran about 50 lines. ([6:19](https://youtu.be/HEFSExa0xl0?t=379))
- The team saw four or five model releases during the work. ([11:23](https://youtu.be/HEFSExa0xl0?t=683))

## Hot takes
- If an agent makes many sequential tool calls, you have invented a bad scripting language, so give it a real one.
- Infrastructure bugs in agents often look like reasoning failures, so check the traces before blaming the model.
- An incomplete formula engine is worse than none, because the agent trusts formulas that then fail.

## Tools mentioned
Node.js REPL, JavaScript, TypeScript type definitions, C#, LLM-as-judge, Witan Labs internal formula engine, Witan Labs internal render engine

## Relevance to our work
- **agentos** (1/3): Crucible is the sandboxed code-execution layer, and the talk's persistent-state REPL pattern is a code-execution design choice that could fit it. → *Read the REPL-vs-separate-tools argument and consider whether one persistent-state code-execution tool in Crucible would replace some tools in the agent surface.*
- **prosharness** (1/3): ProsHarness wraps Claude Code, and the talk's lesson about verification loops and trace review applies to checkpointed agent runs. → *When adding eval checks to a ProsHarness run, prefer deterministic golden checks over LLM-as-judge where the output allows it, and log traces to find plumbing bugs.*
- **general** (1/3): Shows the same pattern of replacing a tool sprawl with one code interface and a verification loop, which applies across coding agents. → *Read the talk's eval section on golden-output comparisons before designing evals for any agent that edits structured files.*

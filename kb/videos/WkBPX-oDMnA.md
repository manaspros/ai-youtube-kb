# Understanding is the new bottleneck — Geoffrey Litt, Notion

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `WkBPX-oDMnA` · [watch](https://youtu.be/WkBPX-oDMnA) · **date:** 2026-07-18 · **length:** 19:33 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Geoffrey Litt · **orgs:** Notion
- **topics:** coding-agents, testing-verification, product-ux, skills-self-improvement · **tags:** code-comprehension, explainer-docs, comprehension-quiz, cognitive-debt, micro-worlds, shared-understanding, literate-diffs, ExplainDiff, Claude Code, Notion, education-inspired, human-in-the-loop

> Geoffrey Litt (Notion) argues humans must still understand agent-written code to stay creative participants, not only to verify it, and shows explainer docs, comprehension quizzes, agent-built micro-worlds and shared spaces for doing so.

## Summary
Litt opens with a poll and a hot take that people still need to understand how code works, even as agents write very large PRs that are hard to keep up with. He argues the usual reason, verification, is shrinking in value as agents get better at checking themselves. The deeper reason is that understanding is what lets you take part in the next loop and generate the next idea, and he names the risk of accumulating "cognitive debt" when understanding degrades. He borrows from education and presents three techniques: explainer docs for each change (background first, intuition before details, interactive figures, literate diffs), micro-worlds (agent-built debuggers and step-through simulations), and shared spaces where humans and agents discuss work together. He also describes a quiz at the end of each explainer that he must pass before sending code to teammates, which he calls a "speed regulator" that keeps understanding in step with correctness. He closes by tying this to Alan Kay's vision of computers as a way to level up people, and says the goal is to put humans more deeply in loops, not take them out.

## Key ideas
- **Verification is not the main reason to understand agent code** — Agents are getting better at checking their own work, so the human role in correctness checks is shrinking. The stronger reason is understanding to participate: understanding gives you the concepts to make the next idea in the next loop. ([2:13](https://youtu.be/WkBPX-oDMnA?t=133))
- **Cognitive debt is the cost of losing understanding** — Like technical debt, you can move fast for a while, but when your understanding degrades you end up unable to follow or participate. He credits Margaret Storey for the term and Simon Willison for writing about it. ([4:22](https://youtu.be/WkBPX-oDMnA?t=262))
- **Use education methods to stay in the loop** — He frames the question as one education has studied for a long time and draws three techniques from it: explanations, micro-worlds, and shared spaces. ([5:42](https://youtu.be/WkBPX-oDMnA?t=342))
- **An explainer should teach, not just list the diff** — His ExplainDiff skill starts with background, then gives intuition before details, adds interactive figures where useful, and walks through code as a literate diff with prose before each file. The raw diff is the weakest version. ([6:46](https://youtu.be/WkBPX-oDMnA?t=406))
- **A quiz at the end acts as a speed regulator** — Each explainer ends with five medium-difficulty questions. His rule is not to send code to teammates until he passes the quiz on what the agent wrote. He says it has caught gaps in his own understanding many times. ([10:22](https://youtu.be/WkBPX-oDMnA?t=622))
- **Micro-worlds build a feel for the system** — He had Claude build a timeline debugger for a Prolog interpreter so he could scrub through execution and see state at each step. A step-by-step migration game for his website gave him a clearer sense of file changes than a generated script did. ([12:28](https://youtu.be/WkBPX-oDMnA?t=748))
- **Shared spaces build collective understanding** — Multiplayer threads let humans and agents work in one visible conversation instead of separate private ones. Documents with comments let a team discuss an agent's plan in place. ([15:32](https://youtu.be/WkBPX-oDMnA?t=932))

## Techniques
- **Explainer doc per agent change (ExplainDiff-style skill)** — Have the agent write an explainer for each change: background on the system first, then the intent of the change in plain terms, then interactive figures where they help, then a literate walk through the code in order with prose before each file. Output as HTML or Markdown, kept in a shared doc so teammates can comment. *When:* When an agent produces a change large enough that reading the raw diff would not show why it was made, and when a teammate needs to review it.
- **Comprehension quiz gate before sharing code** — Append a short quiz (he uses five medium-difficulty questions) to each explainer. Set a personal rule: do not send the code for review until you can answer the quiz without re-reading. Cites Andy Matuschak and Michael Nielsen's interactive essay with spaced-repetition questions as the model. *When:* When reading feels done but the reader may have skimmed; use it as a self-check before handing code to others.
- **Intuition-first, literate ordering** — Start explanations with the goal in one or two sentences and concrete examples, then details. Order code by the story, not by file path. He compares this to how good math teachers explain. *When:* When writing any explanation of code, especially for a reader who does not yet know the subsystem.
- **Agent-built micro-world debugger** — Ask the agent to build a small UI around the system you want to understand, for example a timeline that steps through the interpreter and shows state at each step, with a comment feature to leave notes on specific steps. *When:* When a bug or internal mechanism is hard to reason about from code alone, or when you want a feel for the machine beyond fixing one bug.
- **Step-through simulation for a migration** — Instead of a script that runs silently, have the agent build a UI that shows old and new states side by side, advances one step per click, prints each command, and shows file trees changing. The user clicks through and sees each change happen. *When:* For one-off or risky migrations where the user needs to see what each step does before trusting the result.
- **Shared threads and commentable docs with agents** — Put agent conversations and plans in a shared workspace where several people and agents can see the same thread, and let teammates comment on a plan in context. He says Notion now lets Claude and Cursor run inside its workspace. *When:* When a team needs to align on a plan or design that an agent produced, and private one-to-one agent chats are slowing down shared understanding.

## Numbers
- Agents are landing PRs of around 50,000 lines, which makes review hard to keep up with ([1:13](https://youtu.be/WkBPX-oDMnA?t=73))
- Each explainer ends with a 5-question, medium-difficulty quiz; the speaker's rule is not to share code until he passes it ([10:22](https://youtu.be/WkBPX-oDMnA?t=622))
- Notion launched HTML blocks in pages that morning, which he used for an interactive rock-drawing simulation ([13:29](https://youtu.be/WkBPX-oDMnA?t=809))
- Notion launched the ability to bring coding agents (Claude and Cursor) into Notion the week before the talk ([15:32](https://youtu.be/WkBPX-oDMnA?t=932))
- Alan Kay's essay A Personal Computer for Children of All Ages is described as roughly 50 years old ([17:06](https://youtu.be/WkBPX-oDMnA?t=1026))

## Hot takes
- Understanding how code works still matters, and the main reason is participation in the next creative loop, not correctness checks.
- Books don't work: reading something does not mean you understood it, so comprehension needs an active check such as a quiz.
- The raw code diff is the weakest possible explanation of an agent's change.
- Interactivity in explanations can be a crutch or slop, and should be used only where it adds understanding that static pictures cannot.

## Tools mentioned
Claude Code, Claude, Cursor, Notion, Notion HTML blocks

## Relevance to our work
- **prosharness** (2/3): ProsHarness runs long Claude Code jobs and has phone-driven approvals. An explainer and a comprehension quiz before an approval is a concrete gate that fits that approval flow. The timeline-debugger micro-world idea could also help with checkpoint review. → *Prototype a run summary (background, intent, step-by-step changes) generated at each checkpoint, with a short comprehension question the approver must answer before the run continues.*
- **agentos** (1/3): Talk is about how humans understand agent-written code. SkillForge turns telemetry into reusable skills, and an explainer-plus-quiz step could be a review gate for those skills, but the talk does not address skill mining or governance. → *Read the ExplainDiff idea as a possible review step for SkillForge-generated skills: a short explainer and a quiz before a skill is accepted. Low priority, no build work now.*

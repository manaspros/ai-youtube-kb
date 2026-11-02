# MIT just proved how ChatGPT impacts our brains

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `y9WkrRhFF0s` · [watch](https://youtu.be/y9WkrRhFF0s) · **date:** 2025-11-02 · **length:** 6:31 · **format:** other · **quality:** 2/5 · **depth:** intro
- **speakers:** Better Stack host (unnamed in transcript) · **orgs:** MIT, OpenAI, Google, Better Stack
- **topics:** models-research, evals · **tags:** cognitive-debt, learning-vs-delegation, ChatGPT, EEG, MIT-study, research-commentary, essay-writing

> Better Stack walks through the MIT "Your Brain on ChatGPT" essay study: AI-assisted writers showed weaker brain connectivity, poorer recall and lower ownership, with the effect persisting after the AI was removed. Small, text-only, single-task evidence.

## Summary
The host summarizes an MIT study (Your Brain on ChatGPT, on cognitive debt from AI assistants in essay writing) rather than reading the 206-page paper. Participants were split into an LLM group (ChatGPT), a search-engine group and a brain-only group, ran three essay sessions with EEG recording, and in a fourth session the groups were swapped. The reported findings are weaker neural connectivity in the LLM group, which persisted after switching to unaided writing, and very poor recall of the participant's own essay text (83.3% of LLM participants could not give a correct quote versus 11.1% in the other two groups). The LLM group also reported low ownership of their essays and produced essays that were more homogeneous, lower effort and that the host says were scored below the brain-only group at all levels. The host lists the study's limits: 54 participants (18 in the swap group), one educational essay task, text-only interaction, and possibly no transfer to programming. The host's takeaway is to use AI deliberately and learn from it rather than copy and paste, and notes the paper's FAQ asks writers to avoid words like "dumb" or "harm".

## Key ideas
- **Study design: three groups (LLM/ChatGPT, search engine, brain-only) over three sessions, then a fourth session where the groups are swapped** — EEG, NLP analysis, participant interviews, and scoring by human teachers plus an AI judge. Essay prompts were drawn from SAT-style topics such as loyalty and happiness. ([0:00](https://youtu.be/y9WkrRhFF0s?t=0))
- **Neural connectivity scales down with external support** — Per the host's reading of the paper, brain-only writers had the widest networks, search-engine writers were intermediate, and LLM users had the weakest coupling. ([1:10](https://youtu.be/y9WkrRhFF0s?t=70))
- **The effect persists after the AI is removed (cognitive debt)** — In the swap session, former LLM users who wrote unaided showed weaker connectivity and under-engagement of alpha and beta networks. Former brain-only users who then used an LLM showed higher recall and wider re-engagement. ([2:30](https://youtu.be/y9WkrRhFF0s?t=150))
- **LLM users could not recall or claim their own text** — 83.3% of LLM participants failed to give a correct quotation from their essay minutes after writing it, versus 11.1% in the search and brain-only groups. Reported ownership of the essays was low. The host suggests searching forces you to find and absorb the quote. ([2:30](https://youtu.be/y9WkrRhFF0s?t=150))
- **Essay quality and homogeneity** — LLM-group essays were lower quality than brain-only essays at all levels, even after the switch. Essays were homogeneous, with shared locations and dates, and in session 3 were mostly copy-paste and close to ChatGPT's default answer for the bare prompt. ([3:53](https://youtu.be/y9WkrRhFF0s?t=233))
- **Limits the host stresses** — Only 54 participants (18 in the swap group), an educational essay task, text-only interaction (no audio), and results that may not generalize to programming. The host says the study confirms saved effort costs memory and critical thinking, but argues this is not a reason to avoid AI. ([4:57](https://youtu.be/y9WkrRhFF0s?t=297))
- **Wording caution from the paper's FAQ** — The FAQ asks readers not to describe the findings as making people stupid, dumb, or harmed or damaged. The host reads this as a caveat about overclaiming. ([6:09](https://youtu.be/y9WkrRhFF0s?t=369))

## Techniques
- **Crossover study with a swap session** — Assign participants to tool conditions (LLM, search, none) across several sessions, then swap conditions in a final session. Compare each group's residual performance and neural or behavioural signal against people who never used the tool. *When:* Measuring whether an AI assist leaves lasting effects on skill or memory after it is removed, rather than only measuring in-the-moment output quality.
- **Post-task recall probe** — Right after a participant finishes an output, ask them to quote or explain specific parts of it. Score the result as a direct measure of whether they engaged with the content. *When:* Checking whether a user actually understands or owns AI-generated work, as a complement to output-quality scoring.
- **Multi-signal output scoring** — Combine human expert grading, an AI judge, and automatic text analysis (homogeneity across outputs, distance from the default model answer for the same prompt) instead of relying on one judge. *When:* Evaluating open-ended writing or generation where one grader is unreliable, or where you need to detect copy-paste behaviour or convergence on one answer.
- **Deliberate AI use for learning** — Read and rework model output instead of pasting it, so the final text is the user's own. *When:* When the goal is to learn the material or to own the result, as opposed to only getting an artifact quickly.

## Numbers
- Study size: 54 participants, with 18 in the session-4 swap group ([4:57](https://youtu.be/y9WkrRhFF0s?t=297))
- 83.3% of LLM-group participants failed to give a correct quotation from their own essay, versus 11.1% in the search-engine and brain-only groups ([2:30](https://youtu.be/y9WkrRhFF0s?t=150))
- Four sessions in total with three groups; the paper itself is 206 pages ([0:00](https://youtu.be/y9WkrRhFF0s?t=0))

## Hot takes
- The title "MIT just proved how ChatGPT impacts our brains" overstates the evidence. The study is 54 people on one essay task, and the host notes it may not transfer to programming or audio.
- The host's own summary is a secondhand reading of the paper, and the video is mostly comedy and commentary, not practitioner analysis.
- The 'cognitive debt' framing is a strong interpretation of EEG connectivity and recall differences, presented as a finding about long-term effects.

## Tools mentioned
ChatGPT, Google search (search-engine condition), EEG (neural recording used in the study), NLP analysis (used in the study)

## Relevance to our work
- **agentos** (1/3): Only weakly relevant. The study is about human learning and recall after AI use, not agent infrastructure, but it argues for measuring user ownership or comprehension of AI output, which could matter for skill-mining or review workflows. → *Do not cite this study as design evidence; if a human-in-the-loop approval or review feature is ever built, consider the post-task recall probe as a cheap check that a reviewer understood an output.*

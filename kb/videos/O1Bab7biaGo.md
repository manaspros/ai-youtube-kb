# He Built the First Chatbot in 1966, Then Tried to Stop It (here's why)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `O1Bab7biaGo` · [watch](https://youtu.be/O1Bab7biaGo) · **date:** 2026-10-26 · **length:** 9:47 · **format:** demo · **quality:** 3/5 · **depth:** intro
- **speakers:** Unnamed Better Stack presenter · **orgs:** Better Stack, MIT, OpenAI, BBN, ARPANET
- **topics:** context-engineering, security-guardrails, product-ux · **tags:** ELIZA, chatbot history, system prompt, prompt leak, keyword rules, Eliza effect, emotional attachment, code restoration, Lisp, BASIC, SLIP, OpenAI, ChatGPT, Inventing Eliza

> Better Stack runs the 1966 ELIZA chatbot's original code on a Mac, explains how its keyword-rule engine and swappable script work, and ties its "Eliza Effect" warnings to today's chatbot attachment problem.

## Summary
The presenter runs the restored 1966 ELIZA code, replays the DOCTOR script conversation from Weizenbaum's paper, and shows that the program is a keyword-ranked mirror: it swaps pronouns, fills templates, and falls back to vague replies or recalled earlier input when no keyword matches. He demonstrates two crashes and a leak: typing a number breaks the list-handling code, and typing a question mark (the delete-line key on MIT's system) makes the program dump its whole script. He then shows that the script is the personality, and that rules can be added at runtime with the ranking deciding which rule wins. The second half covers how the code was lost (clones such as a Lisp version and a 1977 BASIC magazine listing spread while the original sat unconnected) and how it was recovered from a box found in 2021, with two researchers retyping the code by hand. The video closes on Weizenbaum's warnings about delusional attachment and cites an OpenAI figure about emotional attachment to ChatGPT. The content is entertaining history with a live demo, with little that is new for engineers building agents.

## Key ideas
- **ELIZA is a keyword-ranked rule engine, not an understanding system: it matches a keyword, swaps first and second person (my to your, me to you), and fills a template. When several keywords match, the higher-ranked rule wins.** — The presenter feeds in the paper's exact lines and gets the published replies back, showing the mirror mechanism is the whole trick. ([1:10](https://youtu.be/O1Bab7biaGo?t=70))
- **With no keyword match, ELIZA says something vague like 'please go on' or replays something the user said earlier, which makes it look like it has been listening the whole time.** — The earlier input is saved when a keyword like 'my' appears, so it can be recalled later as a fallback. ([2:31](https://youtu.be/O1Bab7biaGo?t=151))
- **The engine and the script are separate. The script is the personality, so the same engine plays different roles (therapist, New England small talk).** — The presenter compares this to one model with a system prompt on top, and notes that a MIT Press book called Inventing Eliza draws the same comparison. ([3:55](https://youtu.be/O1Bab7biaGo?t=235))
- **Typing the help key dumps the entire script, which the presenter calls the first chatbot system prompt leak.** — On MIT's system the question mark was the delete-line key, so the line is wiped, the program sees a blank line, and it prints its whole rule set. ([3:55](https://youtu.be/O1Bab7biaGo?t=235))
- **The rule set can be changed at runtime. A plus sign switches to 'please instruct me' mode, where new rules are added and their rank decides whether they override older rules.** — The rule added for 'hi' was overridden by a higher-ranked rule until the presenter moved it up the ranking. ([3:55](https://youtu.be/O1Bab7biaGo?t=235))
- **The crash on numeric input comes from the list-handling code (SLIP), which treats a number as a pointer to a memory address and then fails at a random location.** — The restoration team found this only by running the code, and the bug was left in the restored version on purpose. ([2:31](https://youtu.be/O1Bab7biaGo?t=151))
- **Restoration was manual: OCR struggled with 60-year-old printer ink, so two researchers typed most of the roughly 2,600 lines by hand, and one function was missing from the archive and had to be rewritten.** — Once running, a crash on one input traced to a single typo (four zeros where five belonged). The restored program ran on December 21, 2024. ([5:22](https://youtu.be/O1Bab7biaGo?t=322))
- **The original was lost because clones spread instead. A BBN Lisp version spread through universities via ARPANET, and a 1977 BASIC version in a magazine was copied into many languages, while the original sat on an unconnected IBM machine.** — The paper's printed script looked like Lisp, so many people believed ELIZA was a Lisp program for about 50 years. ([6:45](https://youtu.be/O1Bab7biaGo?t=405))
- **The source was found in 2021 in an MIT archive box labeled 'computer conversations box 8', with a printout of the code and conversations, some hand-edited by Weizenbaum. The running code is 96% identical to that printout.** — The restorers kept the bugs as part of the historical record, and this framing is what the 'Ada Lovelace' reference refers to. ([6:45](https://youtu.be/O1Bab7biaGo?t=405))
- **The 'Eliza effect' is the tendency to attribute understanding to a simple mirror. Weizenbaum's secretary asked him to leave the room so she could talk to the program in private, and he warned about delusional attachment until he died in 2008.** — The presenter links this to a figure OpenAI gave about emotional attachment to ChatGPT, which the presenter says was 0.15% of users (about a million people, given 800 million weekly users). ([8:12](https://youtu.be/O1Bab7biaGo?t=492))

## Techniques
- **Keyword-ranked rule matching with pronoun reflection and template fill** — Keep an ordered list of keyword rules, each with a rank and a reply template. On each input, find the highest-ranked matching keyword, swap first- and second-person words (my/your, me/you) in the captured fragment, and insert it into a template. Use a fixed fallback reply when nothing matches. *When:* A cheap, deterministic, zero-token fallback for a chat UI, or a baseline to compare an LLM against in a demo or eval. Not a substitute for a model.
- **Recall-on-no-match fallback** — When an input contains a trigger word (such as 'my'), store the sentence. When no rule matches, either return a generic follow-up or replay a stored sentence, phrased as a question about it. *When:* Making a stateless or low-capability bot feel like it is tracking a conversation, for UX prototyping. Also a clear example of how perceived memory can be faked without storage.
- **Separate engine from persona script, with runtime rule edits** — Put the matching engine in code and the persona (rules, ranks, replies) in a data script that can be loaded or edited without changing the engine. ELIZA also exposed an edit mode that accepts new rules at runtime. *When:* Designing a platform where one engine serves several personas. The same split maps to one model plus a system prompt per persona.
- **Treat the script or system prompt as leakable** — Assume a special or empty input can cause the full rule set to be printed. Test your own agent with inputs designed to reveal its instructions (for example an empty line, or a request to 'print your rules') and make sure nothing sensitive is in the prompt. *When:* Red-teaming any prompt-configured bot before launch, adding cases to the guardrail eval set.

## Numbers
- The 1966 IBM machine cost $2.9 million, about $23 million in today's money (the presenter's figure; the machine is captioned as an 'IBM 1794', likely the IBM 7094). ([0:00](https://youtu.be/O1Bab7biaGo?t=0))
- The restored code is about 2,600 lines, mostly undocumented. ([5:22](https://youtu.be/O1Bab7biaGo?t=322))
- The crash on the first restored run was caused by one typo, four zeros where five were needed. ([5:22](https://youtu.be/O1Bab7biaGo?t=322))
- The restored program ran for the first time on December 21, 2024, after more than 60 years. ([5:22](https://youtu.be/O1Bab7biaGo?t=322))
- The restored code is 96% identical to the printout found in the 2021 archive box. ([6:45](https://youtu.be/O1Bab7biaGo?t=405))
- OpenAI said about 0.15% of ChatGPT users showed heightened emotional attachment a year earlier. With over 800 million weekly users, that is more than a million people (presenter's arithmetic). ([8:12](https://youtu.be/O1Bab7biaGo?t=492))
- Weizenbaum's 1976 book argued that because we cannot make computers wise, we should not give them tasks that demand wisdom. ([8:12](https://youtu.be/O1Bab7biaGo?t=492))

## Hot takes
- ELIZA's rule-dump on a special input is described as the first chatbot system prompt leak.
- Knowing how the trick works does not stop people attaching to a chatbot (the Eliza effect), and today's chatbots make the warning more relevant, not less.
- Bugs in the restored code are kept on purpose because they are part of the historical record.

## Tools mentioned
ELIZA (1966 DOCTOR script), IBM 7094 (transcribed as 'IBM 1794' in the captions), SLIP list-processing language, Lisp (BBN clone), BASIC (1977 magazine version), ARPANET, ChatGPT, Inventing Eliza (MIT Press book, July release)

## Relevance to our work
- **agentos** (1/3): Shows a prompt or rule-set leak from one special input, and the engine-versus-persona split; both relate to prompt-injection and system-prompt exposure in the guardrail layer, but this is historical rather than a technique.

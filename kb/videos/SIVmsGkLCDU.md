# Why AI Loves Em Dashes

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `SIVmsGkLCDU` · [watch](https://youtu.be/SIVmsGkLCDU) · **date:** 2026-09-02 · **length:** 13:28 · **format:** other · **quality:** 3/5 · **depth:** intro
- **speakers:** Kai (narrator, Kai Explains) · **orgs:** OpenAI, Anthropic, Google, Medium
- **topics:** models-research, data-engineering · **tags:** em-dash, ai-writing-style, pretraining-data, rlhf, tokenizer, ai-text-detection, model-collapse, punctuation

> Debunks the token-efficiency, RLHF-demographics and Medium theories for AI's em-dash habit; argues older print-book pretraining data fits the timeline. Opinion-led, with thin sourcing.

## Summary
The narrator notices that his own writing has picked up the em-dash habit from heavy AI use, then sets out to explain why AI models overuse em dashes. He cites a measurement of em-dash rates per word for humans, Moby Dick, and several models, with Claude Opus at about 12 per 1,000 words and GPT-4o below the human baseline. He tests and rejects four popular explanations: token efficiency, training-data mirroring, RLHF raters in Africa, and Medium's auto-conversion of hyphens. His preferred explanation is a shift in pretraining data toward older, public-domain print books, where em-dash use was much higher, and he says the habit then gets reinforced by RLHF, single-pass generation, synthetic-data loops and human imitation. He ends by arguing that em dashes should not be treated as an AI-detection signal and that he will keep using them.

## Key ideas
- **The narrator absorbed the em-dash habit from heavy AI use and only noticed when a colleague asked whether AI had written his text.** — Frames the whole video around how AI style leaks into human writing, not only the reverse. ([0:00](https://youtu.be/SIVmsGkLCDU?t=0))
- **Measured em-dash rates: modern humans use about 0.25 to 0.275% of words, Moby Dick about 0.79%, and models vary widely.** — Moby Dick has 1,712 em dashes in about 216,000 words. Claude Opus is reported near 12 per 1,000 words, GPT-4o below the human baseline, and Gemini about twice the human rate. The speaker says the spread across models is the key finding. ([1:18](https://youtu.be/SIVmsGkLCDU?t=78))
- **The scatter across models argues against a shared training corpus as the sole cause.** — If pretraining data alone drove the habit, models trained on similar data should cluster at similar rates. They do not, which points to post-training differences. ([2:37](https://youtu.be/SIVmsGkLCDU?t=157))
- **Token efficiency does not explain the habit once surrounding spaces are counted.** — The em dash beats only the most verbose alternative by about one token and ties a comma. Efficiency may reinforce the habit but cannot explain a roughly 10x jump between GPT-3.5 and GPT-4. ([3:54](https://youtu.be/SIVmsGkLCDU?t=234))
- **Mirroring the training data and RLHF rater demographics both fail the evidence.** — Mirroring would produce the human baseline, not a much higher rate. Nigerian English text has em dashes at 0.022% of words, below the global baseline, although words like delve show the demographic pattern. ([5:16](https://youtu.be/SIVmsGkLCDU?t=316))
- **Medium's hyphen-to-em-dash conversion explains the character choice, not the usage pattern.** — The real question is why models use em dashes as parenthetical breaks and punchy connectors far more than humans do, which hyphen conversion does not account for. ([5:16](https://youtu.be/SIVmsGkLCDU?t=316))
- **Best-fit explanation: pretraining shifted toward older print books, which were full of em dashes.** — The timeline runs from GPT-3.5 in late 2022 to GPT-4 in 2024, and the speaker ties the shift to labs seeking higher-quality, public-domain and digitized older books. Em-dash use peaked around 1860, and court filings are cited for Anthropic starting this process in early 2024. ([6:35](https://youtu.be/SIVmsGkLCDU?t=395))
- **Four forces keep the habit alive: RLHF rewards polished-looking prose, single-pass generation cannot self-edit, synthetic data loops amplify quirks, and humans are picking the habit up.** — A cited study reports that human scientific abstracts more than doubled em-dash use between 2021 and 2025. The speaker frames the synthetic-data loop as an early form of model collapse. ([9:11](https://youtu.be/SIVmsGkLCDU?t=551))
- **Em dashes are now used as an AI-detection signal, which the speaker rejects because the mark predates AI.** — Dickinson and New Yorker writers used them heavily. Some writers avoid em dashes to avoid being flagged, while others keep them. ([10:37](https://youtu.be/SIVmsGkLCDU?t=637))
- **A reported late-2025 ChatGPT episode shows the habit resists instruction.** — After a public promise to respect custom instructions against em dashes, screenshots reportedly show the model apologizing for an em dash in the same reply. The speaker treats this as evidence of how deep the habit runs. ([11:55](https://youtu.be/SIVmsGkLCDU?t=715))

## Techniques
- **Per-word punctuation rate against a human baseline** — Count a punctuation mark (em dash) per 1,000 words in a text, then compare with a human baseline (about 0.25 to 0.275% of words) and with older literary corpora such as Moby Dick (about 0.79%). Use the same counter on every text so the numbers are comparable. *When:* When you want a cheap, language-level style metric for generated prose, for example in a prose-quality or style eval. The speaker's own figures are second-hand and unsourced, so verify before relying on them.
- **Check token cost in context, not in isolation** — Compare alternatives (em dash, comma, wordy phrase) inside real sentences with their surrounding spaces, then count tokens with the target tokenizer. Do not compare a bare symbol against the most verbose option. *When:* Before accepting a claim that a formatting choice is token-efficient, or when reasoning about why a model prefers one punctuation form over another.
- **Do not use one punctuation mark as an AI-text detector** — Treat em-dash density as a weak signal. Human writers such as Dickinson and New Yorker journalists use them heavily, so a high rate alone does not show machine authorship. *When:* When designing a heuristic to flag AI-written text, such as a review or moderation check. Combine it with other signals or drop it.

## Numbers
- Modern human baseline for em-dash usage is about 0.25 to 0.275% of words in general English writing ([1:18](https://youtu.be/SIVmsGkLCDU?t=78))
- Moby Dick (about 216,000 words) has 1,712 em dashes, about 0.79% of words, roughly 3x the modern human rate ([1:18](https://youtu.be/SIVmsGkLCDU?t=78))
- Claude Opus is reported at nearly 12 em dashes per 1,000 words, about 4.5x the modern human rate and about 1.5x Moby Dick ([1:18](https://youtu.be/SIVmsGkLCDU?t=78))
- GPT-4o is reported below the human baseline and Gemini at about twice the human rate in the same test ([1:18](https://youtu.be/SIVmsGkLCDU?t=78))
- In tokenizer comparison, a bare em dash is one token and a wordy alternative is three tokens. Once surrounding spaces are included, the em dash saves at most one token and ties a comma ([3:54](https://youtu.be/SIVmsGkLCDU?t=234))
- GPT-4 used roughly 10x more em dashes than GPT-3.5 (speaker's figure) ([6:35](https://youtu.be/SIVmsGkLCDU?t=395))
- Nigerian English text has em dashes at 0.022% of words, below the global English baseline ([5:16](https://youtu.be/SIVmsGkLCDU?t=316))
- Em-dash usage in English peaked around 1860, about 30% above today's elevated usage ([7:53](https://youtu.be/SIVmsGkLCDU?t=473))
- A cited study reports human writers more than doubled em-dash use in scientific abstracts between 2021 and 2025 ([10:37](https://youtu.be/SIVmsGkLCDU?t=637))

## Hot takes
- The token-efficiency explanation falls apart once surrounding spaces are counted, so it cannot explain the habit's origin.
- Em-dash density is a poor AI-detection signal because the mark predates AI and is used heavily by human writers.
- Claude Opus, not GPT-4o (the model the meme is named after), has the highest reported em-dash rate in the cited test.
- The print-book pretraining explanation is the speaker's inference from timing and the punctuation history, not a confirmed cause. The numbers come from unnamed third parties (Someone measured, someone pulled data) with no sources given.

## Tools mentioned
ChatGPT, GPT-3.5, GPT-4, GPT-4o, Claude Opus, Gemini, Medium

## Relevance to our work
- **agentos** (1/3):  → *If we add a prose-quality eval, track punctuation or stock-phrase rates per 1,000 words against a human baseline. Low priority.*

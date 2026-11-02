# Ending AI Slop — Thais Castello Branco, Taste Labs

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `lCBf9slCanI` · [watch](https://youtu.be/lCBf9slCanI) · **date:** 2026-08-18 · **length:** 16:30 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Thais Castello Branco · **orgs:** Taste Labs, Reducto
- **topics:** evals, training-finetuning-rl, data-engineering · **tags:** subjective-domains, llm-as-judge, verifiability, brand-adherence, mode-collapse, preference-data, rl-environments, expert-data-qa, task-decomposition

> Taste Labs founder argues subjective domains like design and writing can be made verifiable by decomposing quality into checkable parts, routing each part to the right judge, and using quality expert data.

## Summary
Thais Castello Branco, founder of Taste Labs, opens by saying the company's mission is to end "AI slop" by understanding subjective domains such as design, creative writing, and personality. She argues that coding and math look easy for models because code is verifiable, which is a property of the domain rather than the model, and that subjective work needs a different approach. Her main method is to decompose a fuzzy target, using brand as the example (colors, typography, motion, texture), into codified parts that can be checked, which turns "make something great" into "make something on brand." She warns that LLM-as-judge has reward hacking and hallucination problems, so each component should be routed to a deterministic check, an LLM judge, or human preference data. She also says that averaging preferences and sampling the most likely output collapses to the mean, so she uses a large community of expert designers and per-person preference modeling to keep the distribution diverse. For data quality, she recommends strict expert selection, scoring how specific an expert's commentary is, linking comments to the exact code component, and treating expert disagreement on style as signal but disagreement on objective criteria as a defect. Her closing advice is quality over quantity. The talk is conceptual, with few hard numbers, and it describes the company's practice rather than published results.

## Key ideas
- **Capability follows measurability** — Code is easy for models partly because code itself decomposes, executes and verifies. Design and writing lack that, so progress depends on making their quality measurable. ([2:27](https://youtu.be/lCBf9slCanI?t=147))
- **Brand turns a fuzzy goal into a checkable spec** — 'Great design' is hard to grade, but 'on brand' can be split into colors, typography, motion, animation and texture, and each part can be verified against. ([4:53](https://youtu.be/lCBf9slCanI?t=293))
- **LLM-as-judge is not a reliable grader on its own** — The speaker reports reward hacking and hallucination patterns in LLM judges. Designing the task so it has a clear ground truth is the hardest part of building the environment. ([5:55](https://youtu.be/lCBf9slCanI?t=355))
- **Route each component to the right method** — Components near objective ones (alignment, vision) suit environments or programmatic checks. Style and creativity suit human judgment and preference data. Her main takeaway is to decide the method per sub-problem. ([9:22](https://youtu.be/lCBf9slCanI?t=562))
- **Collapse to the mean is a data and eval failure** — The most likely output is not the best one in subjective work. Greatness sits in the tails, so the system has to break patterns on purpose and keep the distribution wide. ([7:13](https://youtu.be/lCBf9slCanI?t=433))
- **Preferences are plural, so do not average them** — Pooling preference data from unknown raters pushes results toward the mean. Modeling a per-person preference vector and matching it to the data keeps the disagreement intact. ([10:48](https://youtu.be/lCBf9slCanI?t=648))
- **Disagreement is a signal only in the right place** — Experts disagreeing on alignment (an objective property) points to bad data. Disagreeing on style or aesthetics shows real taste distinctions. Consensus should be used on purpose, not everywhere. ([14:21](https://youtu.be/lCBf9slCanI?t=861))
- **Expert commentary quality can be measured** — Specific language is a proxy for rich, high-signal labels. Tying a comment to the exact code component it refers to reduces noise, since models struggle to connect code to visuals. ([12:02](https://youtu.be/lCBf9slCanI?t=722))

## Techniques
- **Decompose fuzzy quality into codified components** — Break a subjective target (for example brand) into named, checkable elements such as colors, typography, motion and texture. Grade each element with its own method rather than one holistic score. *When:* A generation task has a subjective goal but also has parts that can be specified or checked, such as UI or style guides.
- **Per-component routing of grading method** — For each sub-criterion, pick deterministic check, LLM judge, or human preference data based on how objective it is. Move criteria toward verification by codifying them. *When:* Building an eval or RL environment where some criteria are objective and others depend on taste.
- **Ground-truth rules instead of similarity to a reference** — Grade a new output against the codified spec rather than only against an original example, so novel but valid outputs are not penalized. *When:* The agent should create something new that still follows the rules of a reference, such as a new page in an existing brand.
- **Diverse expert pool with strict selection to counter mode collapse** — Use a large group of domain experts across styles and media, select them strictly, and deliberately force the output distribution to stay wide instead of converging on the average. *When:* Collecting human data for creative or subjective domains where averaging erases good minority styles.
- **Specificity and code-linkage QA on expert labels** — Score expert comments for specificity and tie each comment to the exact code element it describes. Use these as filters for data quality. *When:* Collecting expert critiques of generated UI or code where vague feedback is noisy training data.
- **Disagreement triage in expert consensus** — Check whether disagreeing experts are split on an objective criterion (a data defect) or on a stylistic one (valid signal). Keep the second kind as distinct preference signal. *When:* Running human QA or consensus voting on expert labels.

## Numbers
- Taste Labs came out of stealth a few weeks before the talk. ([0:12](https://youtu.be/lCBf9slCanI?t=12))
- Community of over 1,000 experts across different mediums and styles, used to force a wide output distribution and avoid mode collapse. ([8:18](https://youtu.be/lCBf9slCanI?t=498))
- No benchmark or cost results are given. The talk describes practice, not measured outcomes. ([15:34](https://youtu.be/lCBf9slCanI?t=934))

## Hot takes
- Models are good at code and math mainly because those domains are verifiable, not because the models are special.
- Averaging preferences from unknown raters produces slop; the optimal answer is not the average of what people like.
- LLM-as-judge is the wrong tool for checking brand adherence, and human judgment still beats it on subjective work.
- Quality over quantity: a small set of high-taste, deeply specific expert data beats a large noisy set.

## Relevance to our work
- **agentos** (1/3): AgentOS has RAGAS evals in L2A. The talk's point that judges need decomposed, checkable criteria applies to any judged output, but nothing here is about the proxy, memory or serving layers. → *When adding LLM-judge evals to MemoryMesh or other AgentOS layers, split each rubric into checkable criteria and check which ones a deterministic test can cover before using a judge.*
- **general** (1/3): Expert-label QA is relevant to the entity-resolution labeling work, where annotator disagreement needs triage. The talk's split between objective-criterion disagreement (a defect) and stylistic disagreement (a signal) is the transferable idea. → *In labeling or review of entity-resolution pairs, split annotator disagreement by criterion. Disagreement on objective match rules flags bad labels, while disagreement on borderline judgment calls is worth keeping as signal.*

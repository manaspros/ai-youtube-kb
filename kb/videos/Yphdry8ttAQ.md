# Trading Desks to Clinical Trials: Parallels in Applied Vertical AI — Ayush Bhardwaj, Allos AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Yphdry8ttAQ` · [watch](https://youtu.be/Yphdry8ttAQ) · **date:** 2026-09-18 · **length:** 20:02 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Ayush Bhardwaj · **orgs:** Allos AI
- **topics:** product-ux, evals, data-engineering, enterprise-adoption · **tags:** vertical-ai, domain-experts, error-analysis, llm-as-judge, proprietary-data, learning-loop, ai-in-the-loop, pharma, finance, rlhf, rubrics-as-reward

> A seven-step recipe for building vertical AI (finance, pharma) where domain experts in a learning loop, not LLM-as-judge, drive quality and proprietary data is the moat.

## Summary
Ayush Bhardwaj, who has done applied AI at a hedge fund and now at Allos AI (a pharma tech startup), argues that vertical AI products in finance, pharma and legal follow a similar build process. He lays out a seven-step recipe: formulate a narrow problem, identify proprietary data, model the task as a sequence of steps a person would take, set up observability, iterate with domain experts as users, climb the ladder of post-training only when cheaper methods run out, and ship once the loop shows real value. His main claim is that LLM-as-judge fails in domains without verifiable answer keys, so the domain expert has to judge outputs. He also says current deployments are mostly AI-in-the-loop rather than human-in-the-loop, and that models and infra are commodities while domain data and expertise are what differentiate a product. The talk is practitioner-level with a few anecdotes and no code or benchmarks beyond a few cited statistics, and the speaker is candid that the recipe is a simplification.

## Key ideas
- **Narrow the job, then build many agents** — Pick one very specific sub-task (a market, an industry, a ranking criterion) instead of asking one agent to do everything. The speaker notes that building more agents carries no penalty. ([3:45](https://youtu.be/Yphdry8ttAQ?t=225))
- **Proprietary data is the moat** — Public data (broker reports, preprints, papers) is shared by everyone, so the differentiator is data your organization already holds or can curate. Examples given: trade theses (what traded and why it worked) in finance, and failed experiments in pharma. An LLM workflow can turn years of unstructured internal data into structured data quickly. ([5:10](https://youtu.be/Yphdry8ttAQ?t=310))
- **LLM-as-judge does not work where there are no answer keys** — The speaker says he first tried LLM-as-judge and calls it a mistake. Verifiable rewards work for math and code because outputs can be checked (e.g. does it compile). In finance and pharma no such check exists, and errors compound across steps. ([9:07](https://youtu.be/Yphdry8ttAQ?t=547))
- **The data gap is structural, not an oversight** — Pharma firms are legally required to disclose clinical trials, yet about 30% never do. Funds above a holding threshold must file positions publicly each quarter. The data that would teach models the field is therefore scarce and gated, and cannot be bought from frontier labs. ([10:01](https://youtu.be/Yphdry8ttAQ?t=601))
- **Hire the domain expert as the first user and build a learning loop** — The expert curates sources, refines prompts, and decomposes how they reason through a problem. Each new user adds queries, data, and feedback, and the loop generates its own dataset of what works and what does not. ([12:40](https://youtu.be/Yphdry8ttAQ?t=760))
- **Climb the post-training ladder only as needed, starting with error analysis** — Options in rough order of cost: supervised fine-tuning, RLHF (human preferences train a reward model), rubrics-as-reward (a human writes a rubric and the AI grades itself, with an echo-chamber risk), and error analysis on logs. Error analysis on existing observability traces is the cheapest and highest-ROI step because it touches no weights. Fine-tuning must then be repeated with each new base model. ([13:54](https://youtu.be/Yphdry8ttAQ?t=834))
- **AI-in-the-loop, not human-in-the-loop, for now** — In finance and pharma the expert still makes the final call, and the AI narrows options (e.g. five candidate trade theses or drug candidates). The speaker expects this to hold for a long time because models still lack causal reasoning and mostly do pattern matching. ([17:44](https://youtu.be/Yphdry8ttAQ?t=1064))
- **Models and infra are commodities; domain expertise is the product** — Anyone can buy the same model or infra subscription. The durable advantage is the domain data and expertise that the learning loop accumulates. ([18:54](https://youtu.be/Yphdry8ttAQ?t=1134))

## Techniques
- **Narrow task decomposition** — Break the business process into steps and give each agent one pointed question. Do not ask one agent for an open-ended output like top market picks. *When:* Early in building any agent, before writing prompts or choosing data sources.
- **LLM workflow for unstructured-to-structured data curation** — Run an LLM pipeline over years of internal unstructured records to extract structured fields such as trade rationale or experiment outcome. The speaker says this can run overnight. *When:* When the organization holds proprietary but messy documents and needs a clean corpus for prompts or training.
- **Observability traces as the first improvement loop** — Trace every step of the agent, read the logs, and categorize where the output goes wrong. Fix prompts or data based on those error categories before touching model weights. *When:* Once the agent runs end to end and before any fine-tuning or RLHF spend.
- **Domain expert as user in a learning loop** — Hire or embed the person who will buy the product. Have them run queries, judge outputs, decompose their reasoning into prompt steps, and curate sources. Their feedback becomes the training and eval signal. *When:* When no automated judge can verify outputs, as in regulated or niche domains.
- **Post-training ladder** — Go through error analysis, then supervised fine-tuning, then rubrics-as-reward, then RLHF. Move up only when the cheaper step stops improving results. *When:* After the loop shows which failure modes remain. Plan for re-tuning when the base model changes.
- **AI-in-the-loop reduction of expert time** — Have the model generate a short list of candidates, and let the expert choose and make the final decision. *When:* When decisions carry high stakes and need causal judgement that the model cannot reliably supply.

## Numbers
- Institutional managers holding over $100 million in qualifying U.S. equities must publicly file long holdings every quarter (speaker's description of the disclosure rule). ([10:01](https://youtu.be/Yphdry8ttAQ?t=601))
- About 30% of clinical-trial sponsors (nearly one third of firms) never disclose trial results as legally required, per the speaker. ([10:01](https://youtu.be/Yphdry8ttAQ?t=601))
- In 2026 the FDA publicly reminded about 2,000 sponsors to release unfavorable trial results (speaker's recollection, stated approximately). ([10:01](https://youtu.be/Yphdry8ttAQ?t=601))
- Stanford AI Index figure cited: roughly 80% to 89% of enterprise AI agents never reach production. The speaker disputes this framing and says they do reach production but fail to justify their cost. ([15:14](https://youtu.be/Yphdry8ttAQ?t=914))
- Illustrative expert cost of a trader at about $100 per hour, used to explain why experts are expensive to annotate. ([11:16](https://youtu.be/Yphdry8ttAQ?t=676))

## Hot takes
- Asking whether agents are in production is the wrong question; the right one is whether they make or save money end to end.
- LLM-as-judge is a really stupid mistake in domains without answer keys.
- Human-in-the-loop is not yet the norm in finance and pharma; it is AI-in-the-loop, and that will last a long time.
- Model, infra and ecosystem are commodities; the moat is domain data and expertise that nobody can sell you.
- The data that would make vertical models good is gated, so frontier labs do not have it.

## Relevance to our work
- **general** (2/3): Error analysis on logs plus domain-expert labeling is a cheap eval method, relevant to the entity-resolution work where automated judges are weak on niche matching rules. → *Before tuning the ER matcher further, run a structured error-analysis pass over logged false matches and false non-matches, tagged by failure category, with a domain reviewer.*
- **agentos** (1/3): L4 observability and L2D SkillForge both mine agent traces; the talk's error-analysis-before-tuning ordering is a useful framing but nothing in it changes the build. → *When designing SkillForge's skill-worthiness scoring, first hand-tag a sample of failed traces into failure categories before choosing a success signal.*

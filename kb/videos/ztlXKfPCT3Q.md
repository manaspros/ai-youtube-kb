# You’re Not Thinking Big Enough: Rebuilding Food Systems with AI Agents — Cody Menefee, Firecrawl

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `ztlXKfPCT3Q` · [watch](https://youtu.be/ztlXKfPCT3Q) · **date:** 2026-09-27 · **length:** 18:26 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Cody Menefee · **orgs:** Firecrawl, Halter, NoFence, Planet, Pasture Bird, Lincoln University of Missouri
- **topics:** context-engineering, data-engineering · **tags:** agriculture, livestock, rotational-grazing, firecrawl, openpasture, web-scraping, knowledge-base, human-in-the-loop, gps-collars, satellite-imagery, iot

> Firecrawl growth engineer Cody Menefee argues LLM agents could help automate rotational grazing for livestock, with the LLM suggesting moves and a human confirming, plus a recruiting pitch for Firecrawl.

## Summary
Cody Menefee of Firecrawl's growth team uses his livestock background to argue that AI engineers should pick bigger physical-world problems, not another MCP server for another SaaS product. He explains rotational grazing: cattle are moved to fresh paddocks every day, which takes constant labor, and farmers decide where to move them by looking at the grass. He proposes replacing that judgment with an LLM that reasons over GPS positions, drought data, grass height and past grazing across the farm. He reviews sensing options (drones, satellites, trail cameras with a measuring reference) and says the blockers are a knowledge base, a visualization layer and open software for GPS collars. He stresses that the LLM should propose and a human should confirm or deny, since the problem has no single right answer. The talk ends with a call for open collar APIs and a hiring pitch for Firecrawl. Most of the content is anecdote and advocacy; the technical patterns are light.

## Key ideas
- **Labor is the bottleneck for pasture-based livestock.** — Rotational grazing means moving fences, water and animals every day, so few farms do it. The speaker says the way to get more animals on grass is to automate that labor. ([5:01](https://youtu.be/ztlXKfPCT3Q?t=301))
- **The hard part is the decision, not the fence.** — Where to move the herd depends on drought, rainfall, how much a paddock has been grazed, and grass height. Today farmers make this call by looking at the pasture. The speaker frames replacing that visual judgment as the core problem. ([7:16](https://youtu.be/ztlXKfPCT3Q?t=436))
- **Some problems have no deterministic answer.** — The speaker argues engineers should not force LLMs into deterministic roles. Grazing is a multivariate problem with a best guess, not a single correct paddock, so the LLM should reason over the data and suggest, while a human confirms or denies. ([15:37](https://youtu.be/ztlXKfPCT3Q?t=937))
- **Context packaging is the main job.** — He says the first problem is giving agents the context they need: gathering data from many sources, packaging it, and presenting it so an LLM can reason over it. ([16:41](https://youtu.be/ztlXKfPCT3Q?t=1001))
- **The knowledge is locked in YouTube videos and papers.** — Farmers' know-how on when and how to move animals lives in videos. The speaker uses Firecrawl to scrape those videos and research papers into an open repository, OpenPasture, to build a knowledge base for the LLM. ([11:37](https://youtu.be/ztlXKfPCT3Q?t=697))
- **Hardware lock-in blocks the software layer.** — GPS collar companies such as Halter and NoFence require their own collars, so customers cannot plug in their own software. He asks for open APIs so the software can compete on quality. ([17:34](https://youtu.be/ztlXKfPCT3Q?t=1054))
- **Sensing options each have trade-offs.** — Drone orthomosaic maps give good detail but face pilot training, line-of-sight rules and an autonomy approval gap. Satellites are frequent but too high to see what farmers need. A trail camera pointed at a measuring reference can track grass height. ([8:16](https://youtu.be/ztlXKfPCT3Q?t=496))

## Techniques
- **Human-confirmed LLM suggestions over multivariate data** — Feed the LLM several inputs (animal GPS, past positions, drought, grass height across the farm) and ask for a recommendation. A person accepts or rejects it. The speaker treats the human as the final check. *When:* Use when a decision depends on many interacting inputs and no single correct answer exists, so the model proposes and a person decides.
- **Knowledge base from scattered web sources** — Scrape YouTube videos and research papers with Firecrawl, then store the material in an open repository that others can read. *When:* Use when expert knowledge is spread across videos and papers and needs to be gathered before an agent can use it.
- **Context gathering and packaging for LLM reasoning** — Collect data from several sources, normalize and bundle it, then present it in a form the model can reason over, instead of passing raw inputs. *When:* Use when an agent's output quality depends on combining data from many systems.
- **Fixed reference object for remote measurement** — Place a trail camera beside a known measuring object so the camera sees the object and the grass together. Grass height is then read relative to that reference. *When:* Use when a remote sensor needs a repeatable, scale-stable reading without a human in the field.
- **Model the decision at several levels** — The speaker says decisions must be framed at the animal, herd, paddock, farm and ecosystem levels, and that these levels feed back into each other. *When:* Use when a single agent decision affects several linked scopes and optimizing one level can hurt another.

## Numbers
- Speaker's figure: about 97% of cattle are finished on feedlots and about 3% are raised on pasture. The talk gives no source. ([5:01](https://youtu.be/ztlXKfPCT3Q?t=301))
- Speaker says Planet images the whole globe every day at about 1 m resolution, but satellites fly too high to show what farmers need. ([8:16](https://youtu.be/ztlXKfPCT3Q?t=496))
- Speaker says Halter, a GPS collar company, received investment from Peter Thiel at a roughly $2 billion valuation, as reported in the news. ([6:00](https://youtu.be/ztlXKfPCT3Q?t=360))

## Hot takes
- Engineers who push to make LLMs deterministic are missing a whole class of problems that have no deterministic answer, such as grazing rotation.
- Most AI conference talks build software for software builders. The bigger opportunity is in physical-world problems.
- GPS collar makers that lock their software to their hardware are a barrier. Open APIs would let software compete on quality.

## Tools mentioned
Firecrawl, OpenPasture, Halter, NoFence, Planet satellite imagery, trail camera

## Relevance to our work
- **prosharness** (1/3): The speaker's framing of an LLM that proposes and a human that confirms or denies matches ProsHarness's phone-driven approval gates, but the talk gives no mechanism. → *Compare the 15:37 'LLM proposes, human confirms or denies' pattern against ProsHarness's phone approval flow to see whether any checkpoint should be framed as a proposal for review.*
- **general** (1/3): The talk's main point is that LLM reasoning over combined context needs that context packaged first. This matches the context-engineering interest, but the talk gives little technical detail. → *Read the 16:41 segment on packaging multi-source data for LLM reasoning when designing context inputs for any multi-source agent.*

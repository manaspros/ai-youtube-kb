# AI Agents Cut 3-Day Portfolio Builds to Minutes — Jack McDonald, Apollo & Michael Manapat, Rowspace

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `BOWYujhIQuo` · [watch](https://youtu.be/BOWYujhIQuo) · **date:** 2026-10-17 · **length:** 18:57 · **format:** interview · **quality:** 2/5 · **depth:** intro
- **speakers:** Michael Manapat, Jack McDonald · **orgs:** Rowspace, Apollo, Reddington Ridge Capital
- **topics:** data-engineering, enterprise-adoption, product-ux · **tags:** financial-services, CLO, portfolio-construction, data-reconciliation, golden-source, embedded-engineering, human-in-the-loop, customer-case-study, structured-credit

> Customer case study: Rowspace agents and an embedded team cut Apollo's portfolio builds from days to minutes and weekly trade recaps from hours to a one-minute report, with trust earned through per-field source validation.

## Summary
Michael Manapat (co-founder of Rowspace) and Jack McDonald (COO of Reddington Ridge Capital, an Apollo structured-credit/CLO manager with about $50B AUM) describe using AI agents to do data engineering on fragmented financial data. The first example is CLO portfolio construction: PMs used to spend two to three days in Excel building portfolios of 200 to 400 credit names, and now a near-complete portfolio is built in minutes from live documents, trade/compliance systems and pricing, with PMs refining the last 10 percent. The second example is a weekly trade-settlement recap that took two to three people many hours and is now a repeatable one-minute report that the team only QAs daily. On trust, the speakers say general LLMs lack the firm's own data, so trust comes from Rowspace staff sitting with PM and finance teams to define calculations and decide which of many conflicting sources is the golden source for each data point. McDonald argues finance is still very early in AI adoption, with the most value in automating routine middle and back-office work, and that AI-driven process and information advantages will compound in private markets. The closing advice is that unusual-looking internal workflows usually exist for a reason, so spending time on site with domain teams is worth it. The talk is also a partly promotional joint session, with a closing hiring pitch from both companies.

## Key ideas
- **Agents are used to do the data-engineering work of pulling and reconciling fragmented data from many systems so decision-makers get it faster.** — Rowspace positions itself as an AI-driven layer that gathers data from document libraries, trade and compliance systems, and pricing feeds for PMs and traders. ([0:01](https://youtu.be/BOWYujhIQuo?t=1))
- **Generic LLMs are useful for research but not for decisions, because they lack the firm's own data.** — The speaker says Claude or ChatGPT give general information, while trust in production comes from owning the firm's data and a platform that is validated against it. ([7:09](https://youtu.be/BOWYujhIQuo?t=429))
- **Trust is built by per-field source arbitration, not by model output alone.** — One fact can come from 20 sources with only one correct, so the vendor team works with PM and finance staff to decide which source overrides the others and to agree on the calculations. ([8:14](https://youtu.be/BOWYujhIQuo?t=494))
- **Portfolio construction moves from days to minutes, and humans finish the last 10 percent.** — The AI builds a portfolio of 200 to 400 names from live documents and data to about 80 to 90 percent complete, then the PM applies judgment to make it theirs. ([4:25](https://youtu.be/BOWYujhIQuo?t=265))
- **A manual recurring report becomes a repeatable automated one, and the team shifts to daily QA.** — The weekly trade and settlement recap, previously assembled by hand from bank statements by two to three people over many hours, was rebuilt as a visualization that now runs in about a minute. ([5:31](https://youtu.be/BOWYujhIQuo?t=331))
- **Embedded, on-site work with domain teams is the main lever for success.** — McDonald says Rowspace was ahead of its roadmap because staff sat with the client team almost daily to learn its workflows. ([17:39](https://youtu.be/BOWYujhIQuo?t=1059))
- **Finance is still early in AI adoption, and the near-term value is in routine middle and back-office tasks.** — The speaker expects fewer junior support roles over time and sees the gain as freeing capacity for more complex projects. ([12:05](https://youtu.be/BOWYujhIQuo?t=725))
- **In actively traded markets, a strong process and accurate information are the basis of AI advantage, and private markets are catching up.** — The speaker expects better information and trusted data to compound into a durable competitive edge over time. ([14:19](https://youtu.be/BOWYujhIQuo?t=859))

## Techniques
- **Embedded discovery with domain teams** — Vendor engineers sit with PM, finance and operations teams most days, learn the actual calculations and workflows, and identify the golden source of truth before building. *When:* Complex domains with many conflicting data sources and undocumented workflows.
- **Per-field source precedence** — For each data point, define which upstream system wins when sources conflict, validate it with the business owners, and aggregate using that rule. *When:* Reconciling many systems that disagree about the same fact, such as trades, positions or prices.
- **Agent draft then human refinement** — The agent builds the bulk of a judgment-heavy artifact, such as a portfolio, to about 80 to 90 percent, and the expert finishes the last part. *When:* Tasks where the expert's judgment matters but most of the work is mechanical data gathering.
- **Automate recurring reports, keep human QA** — Turn a manually assembled weekly report into a repeatable pipeline with a visual output, then have staff check the output daily rather than build it by hand. *When:* Recurring reports that are high-effort, rules-based and need to be accurate.

## Numbers
- Manages about $50B in assets as a captive CLO and structured-credit manager. ([1:06](https://youtu.be/BOWYujhIQuo?t=66))
- Thousands of data points arrive daily, with around 1,000-name loan pools. ([2:12](https://youtu.be/BOWYujhIQuo?t=132))
- Portfolio of 200 to 400 single credit names: 2 to 3 days of manual Excel work before, now minutes. ([4:25](https://youtu.be/BOWYujhIQuo?t=265))
- Portfolio is built to about 80 to 90 percent completion by the system, with PMs refining the last 10 percent. ([4:59](https://youtu.be/BOWYujhIQuo?t=299))
- Weekly trade recap: 2 to 3 people spending many hours per week, now a repeatable report in about one minute. ([5:31](https://youtu.be/BOWYujhIQuo?t=331))
- Investor base of over 400 global investors. ([15:59](https://youtu.be/BOWYujhIQuo?t=959))

## Hot takes
- General-purpose LLMs are not a substitute for a firm's own validated data when making trading or portfolio decisions.
- Finance is still very early in AI adoption, and back-office automation is the main near-term value.
- Vendor staff sitting on site with the client daily matters more than a product roadmap for success.

## Relevance to our work
- **agentos** (1/3): The per-field golden-source precedence idea is relevant to MemoryMesh conflict resolution and provenance, but the talk gives no architecture detail. → *Check how MemoryMesh picks a winning fact when two memories conflict, and consider storing a per-field source-precedence rule alongside provenance.*
- **prosharness** (1/3): The agent-draft-then-human-finishes pattern is close to ProsHarness's plan and approval flow, but the talk is not about coding agents. → *Consider making the plan step pause for the user to finish or edit the last part of a plan before execution, not just approve or reject it.*

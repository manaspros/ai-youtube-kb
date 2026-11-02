# Proving Alpha: How a Hedge Fund Measures AI's ROI - Hari Kumar, Contour Asset Management

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `ZMZlAn6Pyfg` · [watch](https://youtu.be/ZMZlAn6Pyfg) · **date:** 2026-10-24 · **length:** 18:24 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Hari Kumar · **orgs:** Contour Asset Management, AlphaSense, Yipit, Rogo, Hebbia, Bloomberg
- **topics:** governance-compliance, enterprise-adoption, evals, mcp-and-tools · **tags:** roi-measurement, ab-testing, analyst-workflows, cost-per-useful-insight, alt-data, mcp-connectors, finance, hedge-fund, ops-consolidation, idea-tracking

> A hedge-fund head of AI explains how Contour measures AI ROI: live A/B tests of analyst workflows, process metrics over slow P&L, cost per useful insight, and connector-maintenance time counted as a cost.

## Summary
Hari Kumar, head of AI at Contour Asset Management (a roughly $6B fundamental long/short fund with about 15-20 people, mostly TMT), describes his mandate to show AI impact across research, trading, ops, compliance and finance. The main method is live A/B testing: for each analyst's coverage name, the team records the pre-AI research workflow across one three-month earnings cycle, then reruns it with each new tool added and compares data sources and conclusions. He argues P&L is too slow and noisy to show short-term ROI in a fundamental shop, so the team tracks process metrics instead, including analyst time per name and a "cost per useful insight" metric tied to later outcomes. Beyond research, he describes agents that resurface dropped ideas and watch timing, alt-data feeds connected through MCP or APIs, and an effort to consolidate fragmented ops and compliance tools into one internal platform. He also argues that time spent fixing broken model calls and connectors belongs in the ROI equation. The talk is intentionally high-level and shares no measured results.

## Key ideas
- **Measure AI impact with live A/B tests of real analyst workflows** — For one name, the team records the full pre-AI research process across one three-month earnings cycle. Each new tool (expert-call assistant, agent-run consumer survey) is then added in turn and the two runs are compared on data sources and conclusions. Analysts across about 10 covering analysts run this in parallel. ([2:33](https://youtu.be/ZMZlAn6Pyfg?t=153))
- **Process metrics stand in for P&L, which is too slow to show short-term ROI** — Fundamental ideas take months to play out, so a three-month window is already long. The speaker tracks whether the process itself improves (survey work, model updates) and whether people's work actually changes rather than adding friction. ([5:22](https://youtu.be/ZMZlAn6Pyfg?t=322))
- **Agents should keep ideas alive and watch timing** — Ideas get dropped when a PM deprioritizes them, then resurface too late. Agents that scan an analyst's notes against market data can flag an idea that has become interesting again, even if it was only worked on for a day. ([7:53](https://youtu.be/ZMZlAn6Pyfg?t=473))
- **Alt-data is only valuable when combined, which MCP and APIs make possible** — Credit-card panel data (Yipit is the example) is siloed on its own. Feeding it through an MCP or API connector into agents that also read expert-call transcripts lets the system relate the two sources. ([8:50](https://youtu.be/ZMZlAn6Pyfg?t=530))
- **Consolidate fragmented ops and compliance workflows into one tool** — Ops tasks such as order reconciliation and vendor tracking are spread across Bloomberg, the order management system and vendor tools. The goal is one internal tool so ops and compliance are not dependent on piecemeal external products. ([11:44](https://youtu.be/ZMZlAn6Pyfg?t=704))
- **Count the time spent on cost per useful insight** — The team tracks analyst time spent per name per day, the insights it produced, which tools were used, and where those ideas eventually landed in P&L. The resulting metric is cost per useful insight. ([10:18](https://youtu.be/ZMZlAn6Pyfg?t=618))
- **Count the time lost to fixing connectors as an ROI cost** — Model calls break and connectors fail every few days. Someone has to fix them, and that time is taken away from insight work. The speaker says this cost should be netted against the value of the tool and is shrinking over time, but it is still tracked. ([16:46](https://youtu.be/ZMZlAn6Pyfg?t=1006))
- **Build an in-house layer on top of vendor subscriptions** — Analysts already use AlphaSense, Rogo and Hebbia-type tools. The plan is an internal platform that pulls them into one place, learns each analyst's model patterns, and raises the value of existing subscriptions through their APIs and MCP servers. ([14:23](https://youtu.be/ZMZlAn6Pyfg?t=863))

## Techniques
- **Live A/B workflow capture** — Pick one coverage name and one earnings cycle. Record the analyst's full process without LLMs first, then rerun it with each tool added in sequence (expert-call tooling, agent-run surveys). Compare the data sources used and the conclusions reached, and log time spent at each step. *When:* Rolling out AI tools into an existing research process where the baseline is an experienced analyst's work and the outcome only shows up over months.
- **Agent-synthesized vs analyst-synthesized expert calls** — Run the expert call through an agent, then compare two variants: the analyst synthesizes the agent's notes, or the agent synthesizes and the analyst reviews the conclusions. Measure how long each takes to get the same information and which one reaches better conclusions. *When:* Evaluating how much of the synthesis step to delegate to an agent.
- **Cost per useful insight** — Log analyst time per name per day and the insights produced, tag each insight with the tools used, and later join each insight to its P&L outcome. Divide the total cost of time and tools by the number of insights that were judged useful. *When:* You need an attribution metric in a domain where P&L takes months to show up.
- **Idea-resurfacing agent** — Store every note an analyst writes, even short sessions. Periodically check the stored ideas against current market data, and notify the PM and trader when an old idea crosses an interest threshold. *When:* Analysts generate more ideas than the team has time to act on, and timing matters.
- **Alt-data via MCP or API connectors into agents** — Expose vendor datasets (credit-card panels, spend data) through an MCP server or API, and give the agent both those feeds and internal notes or transcripts, so it can relate the two sources. *When:* Vendor data is valuable only when joined with other internal sources.
- **Connector-maintenance time as an ROI line item** — Track the engineer or analyst hours spent fixing broken model calls and connectors, and subtract that time from the value the tool delivers. *When:* Measuring ROI for any tool that depends on external APIs that break regularly.

## Numbers
- Fund size: about $6B AUM with roughly 15-20 people, mostly invests in TMT ([0:08](https://youtu.be/ZMZlAn6Pyfg?t=8))
- About 10 analysts, with each covering up to 30-40 names at smaller funds ([2:33](https://youtu.be/ZMZlAn6Pyfg?t=153))
- A3 three-month earnings-to-earnings cycle used as the A/B test window ([2:33](https://youtu.be/ZMZlAn6Pyfg?t=153))
- Measurement horizons: some ideas take 3 months, others 6-12 months to show up in the stock price ([5:22](https://youtu.be/ZMZlAn6Pyfg?t=322))

## Hot takes
- The talk is deliberately vague, and it shares no measured ROI results, deltas or costs, so the method is a proposal rather than evidence.
- The 'cost per useful insight' metric is named but never defined, and the talk does not say how 'useful' is judged.
- Counting connector and model-call breakage time as an ROI cost is a point most AI ROI frameworks omit, and it is the most transferable idea in the talk.

## Tools mentioned
AlphaSense, Yipit, Rogo, Hebbia, Bloomberg, MCP, APIs (vendor data)

## Relevance to our work
- **agentos** (1/3): Its budget, observability and Locust-based measurement layers could carry a per-task 'cost per useful output' metric, but the talk gives no technical method for it. → *Consider adding a cost-per-accepted-output metric to the L4 Prometheus/Grafana dashboards, joining token spend to a human accept/reject signal.*
- **prosharness** (1/3): The A/B capture of a workflow with and without a tool maps onto comparing ProsHarness configurations (for example plan-critique on or off) across checkpointed runs. → *Log per-run human intervention time and outcome for each harness config, so the same with-vs-without comparison can be made on real runs.*

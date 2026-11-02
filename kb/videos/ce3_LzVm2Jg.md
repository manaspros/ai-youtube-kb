# I Let AI Argue About a Stock

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `ce3_LzVm2Jg` · [watch](https://youtu.be/ce3_LzVm2Jg) · **date:** 2026-01-02 · **length:** 5:06 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** Better Stack presenter (unnamed in transcript) · **orgs:** Better Stack
- **topics:** multi-agent, agent-architecture, dev-tools · **tags:** trading-agents, langgraph, multi-agent-debate, financial-agents, cli, openai, alpha-vantage, yahoo-finance, non-determinism, token-cost

> Better Stack demo of Trading Agents, an open-source Python multi-agent project that simulates a trading firm with LLM analyst agents and a bull/bear debate; a quick CLI walkthrough with cost and non-determinism caveats.

## Summary
The video introduces Trading Agents, an open-source Python project that spins up a team of LLM agents (fundamentals, sentiment, news, technical analysts, plus bullish and bearish debaters) to produce a buy/sell recommendation for a stock. The presenter runs the CLI on Hilton (HLT), setting up the repo in under two minutes with a Conda env, requirements, and OpenAI and Alpha Vantage keys. The stack is LangGraph for the multi-agent flow, with Yahoo Finance and Alpha Vantage as data sources. He notes the project can be pointed at Anthropic or Google models and that the debate rounds are configurable, trading cost for depth. The main caveats are that repeated runs give different results, API spend adds up, and external data rate limits apply. He frames it as a sandbox for learning multi-agent systems, not financial advice. Quality is modest: a light walkthrough with no benchmarks or measured results.

## Key ideas
- **Trading Agents is a multi-agent simulation of a trading firm, where each agent has a specialized role and they do not always agree.** — Roles include fundamentals analyst, sentiment analyst (social media), news watcher, and technical analyst, plus bullish and bearish agents that debate. The presenter stresses that the team behaves like a real team rather than one model answering. ([0:00](https://youtu.be/ce3_LzVm2Jg?t=0))
- **The stack is LangGraph for orchestrating the agent flow, with Yahoo Finance and Alpha Vantage as data sources.** — The presenter describes it as modular and geared to stocks. He says crypto could be squeezed in but ETFs are not supported. ([1:06](https://youtu.be/ce3_LzVm2Jg?t=66))
- **Setup is fast: clone, Conda env, install requirements, add API keys.** — He says it took under two minutes. OpenAI is not required, since Anthropic, Google, or other providers can be used. ([1:06](https://youtu.be/ce3_LzVm2Jg?t=66))
- **The CLI asks for a ticker, a date, which analyst groups to enable, research depth, the LLM provider, and which models to use for quick and deep thinking.** — In the demo he picks HLT, enables all analysts, and then the run unfolds with fundamentals, sentiment, news, and technical (RSI, MACD) steps before the debate. ([2:05](https://youtu.be/ce3_LzVm2Jg?t=125))
- **The bull/bear debate is the key mechanism: instead of one answer, the final output is a buy/sell recommendation with reasoning.** — The bullish agent argues the upside, the bearish agent calls out risk, and the final conclusion cites the gathered data. ([2:05](https://youtu.be/ce3_LzVm2Jg?t=125))
- **Debate rounds are configurable and trade depth for cost.** — Changing the default config in the main Python file, for example to a deeper model or more debate rounds, produces deeper analysis but calls the API much more often. ([2:05](https://youtu.be/ce3_LzVm2Jg?t=125))
- **Output is non-deterministic: the same run can produce different recommendations.** — The presenter reruns the same ticker and date and gets a different result, and he flags it as a con. ([3:24](https://youtu.be/ce3_LzVm2Jg?t=204))
- **Cons called out: token spend, inconsistent results, external data rate limits, stock-only focus, and not production-hardened.** — He says it is not something he would bet money on. He calls it a sandbox for learning and risk-free backtesting. ([3:24](https://youtu.be/ce3_LzVm2Jg?t=204))

## Techniques
- **Role-specialized analyst agents plus adversarial bull/bear debate** — Create separate agents for fundamentals, sentiment, news, and technicals. Feed their reports into a bullish and a bearish agent that debate for N rounds, then have a final agent recommend buy or sell with reasoning. Round count is a config value. *When:* When you want a structured multi-perspective decision and are willing to pay for extra calls to get depth.
- **Scripted run instead of CLI** — Skip the CLI and invoke the main Python script with a ticker and a date. Adjust the default config in the main file to change the model or number of debate rounds. *When:* When you want to automate or batch runs rather than run interactively.
- **Model-agnostic setup** — Set provider keys for OpenAI, Anthropic, or Google as needed. The presenter notes the project is not tied to OpenAI. *When:* When you want to control cost or try other models.

## Numbers
- Setup took under two minutes (clone, Conda env, requirements, two API keys). ([1:06](https://youtu.be/ce3_LzVm2Jg?t=66))
- Debate rounds are configurable; more rounds means deeper analysis but many more API calls and higher cost. No figures given. ([2:05](https://youtu.be/ce3_LzVm2Jg?t=125))

## Hot takes
- He says the project could end up inside everyday trading apps and quant tools, but also says it is not hardened for production.
- He calls the results non-deterministic, which makes them unreliable as a basis for decisions.
- He says it is a learning sandbox and not financial advice.

## Tools mentioned
Trading Agents (open source Python project, multi-agent trading simulation), LangGraph, OpenAI API, Alpha Vantage API, Yahoo Finance, Anthropic API, Google models, Conda, Python 3

## Relevance to our work
- **agentos** (1/3): Multi-agent role debate with LangGraph is a useful reference for AgentOS orchestration, but the video is a light walkthrough. → *Look at the Trading Agents repo's LangGraph graph to compare its debate-round control flow with our multi-agent design.*
- **prosharness** (1/3): The bull/bear plus final-decision pattern is a plan→critique→decide shape close to ProsHarness's plan→critique→debate flow. → *Compare the debate-then-decide pattern with ProsHarness's plan→critique→debate step to see if round count and stop criteria are worth borrowing.*

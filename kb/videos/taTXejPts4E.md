# How Crypto Is Secretly Taking Over Banking with @SarahBensonCodes  | Better Stack Podcast Ep. 8

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `taTXejPts4E` · [watch](https://youtu.be/taTXejPts4E) · **date:** 2026-01-02 · **length:** 52:07 · **format:** interview · **quality:** 2/5 · **depth:** intro
- **speakers:** Richard, James, Sarah Benson · **orgs:** Better Stack, Amber Data, Gelato Network, Tiger Data, Thirdweb, Polymarket, Canton Network, Ethereum, Citibank
- **topics:** dev-tools, mcp-and-tools, enterprise-adoption · **tags:** web3, crypto, smart-contracts, solidity, tokenized-rwa, prediction-markets, mcp, due-diligence, podcast

> Better Stack podcast with Sarah Benson (Amber Data) on crypto vs Web3, tokenized real-world assets and smart-contract basics. Mostly opinion, with a short note on exposing data to LLMs via MCP.

## Summary
Hosts Richard and James interview Sarah Benson, a software engineer at Amber Data, about how crypto and Web3 relate and where the industry is heading. The conversation covers the three layers of blockchain development (chain core, smart contracts, dApp front ends), with Solidity and Rust for contracts and React, TypeScript and ethers.js or web3.js for front ends. It explains smart contracts and oracles at a beginner level and recommends Thirdweb's audited templates as a starting point. Sarah argues that consumer Web3 use cases are weak while institutional finance is moving on-chain, citing private permissioned chains and tokenized real-world assets. She describes Amber Data shifting from REST APIs toward MCP servers and semantic tagging so trader-owned LLMs can query on-chain data. The back half is mostly off-topic chat (Polymarket, pump.fun, Chicago), and there is a partnership plug for Tiger Data, so the technical substance is thin.

## Key ideas
- **Blockchain development has three layers: core chain (very hard for beginners), smart contracts (Solidity or Rust), and dApp front ends (React and TypeScript plus ethers.js or web3.js).** — The smart contract is compared to a back end or API layer that dApps call. Security is flagged as essential, especially for AI-written contracts with Solidity gotchas. ([3:45](https://youtu.be/taTXejPts4E?t=225))
- **Smart contracts cannot read off-chain data by themselves, so oracles such as price feeds are needed to bring that data on-chain.** — Oracles are described as connectors that let a contract use off-chain asset prices in its calculations, for example in DeFi pricing such as TWAP and VWAP. ([7:36](https://youtu.be/taTXejPts4E?t=456))
- **Sarah's view is that consumer Web3 (NFTs, metaverse, physical tags) is unlikely to see mass adoption, while finance is moving on-chain quickly.** — She expects finance to move almost entirely on-chain in the coming years, mostly out of sight of end users. Gaming is the one consumer area she sees potential in. ([9:40](https://youtu.be/taTXejPts4E?t=580))
- **Private or permissioned chains let institutions transact on chain without public transparency.** — The Canton Network is named as a current example. Any party can create its own chain, and the data can stay private to it. ([11:50](https://youtu.be/taTXejPts4E?t=710))
- **Tokenized real-world assets (RWAs) and tokenized collateral are her biggest prediction. Assets like gold get 24/7 tradable tokens, and collateral keeps earning yield while a deal settles.** — The argument is capital efficiency for banks and funds: deals close faster and money stays productive. This is a prediction from a practitioner, not evidence. ([13:14](https://youtu.be/taTXejPts4E?t=794))
- **Amber Data's work is shifting from serving data through a plain API to MCP servers and semantic tagging, so trader-owned LLMs can query historical on-chain data in natural language.** — Tagging and semantic modelling are described as making the data crawlable by LLMs. This is the most directly reusable idea for our data and registry work. ([33:09](https://youtu.be/taTXejPts4E?t=1989))
- **The speaker sees the future of Web3 as AI agents, data pipelines, privacy, governance and interoperability working together, not NFTs and tokens.** — She also notes that AI-driven 24/7 automated on-chain trading makes agent-driven trading more plausible. ([30:46](https://youtu.be/taTXejPts4E?t=1846))
- **Prediction markets such as Polymarket are presented as a better forecasting signal than polls, because participants put real money behind their beliefs.** — Her examples are election outcomes and bets on model release timing. She claims it beat polls, but gives no data to back that up. ([28:06](https://youtu.be/taTXejPts4E?t=1686))
- **Her due-diligence heuristics for a Web3 project are transparency about founders, team and cap table, named reputable backers, and whether trusted creators follow it.** — She says code review rarely reveals an obvious scam, so she weights the human signals more heavily. ([41:52](https://youtu.be/taTXejPts4E?t=2512))
- **Content advice: full-build tutorials need heavy scripting so no step feels like a jump, and topics should track the industry (DAO tutorials were popular in 2020 and are not now).** — She mentions a Tiger Data (TimescaleDB) partnership build tutorial that ingests crypto trade data and runs AI analysis, which is a sponsored-style plug. ([40:34](https://youtu.be/taTXejPts4E?t=2434))

## Techniques
- **Start a smart contract from an audited template** — Pick a template on Thirdweb (all listed as audited), read it to see the contract pattern, add it to the Thirdweb platform, one-click deploy to a testnet, then deploy to mainnet only when ready. *When:* Learning how contracts are structured, or prototyping a contract quickly without writing one from scratch. Use with a testnet first.
- **Expose analytics data to agent LLMs via MCP plus semantic tags** — Wrap the dataset in an MCP server so an LLM can call it, and add tagging and semantic modelling metadata so the data is discoverable and crawlable by LLMs. The speaker gives no implementation details. *When:* Users (here, traders with their own LLMs) need natural-language queries over structured historical data, and a plain REST API is not enough.
- **Private permissioned chain for institutional settlement** — Run a private chain (the speaker names Canton Network as an example) instead of a public one, so transactions and data stay closed to outsiders. *When:* Institutions need on-chain settlement or collateral movement but cannot expose their transactions publicly.
- **Vet a Web3 project before trusting it** — Check that founders and team are named, that the cap table and backers are disclosed, and which trusted creators follow the project on X. Treat code review as a weak signal, since obvious backdoors are rare. *When:* Evaluating an unknown crypto or Web3 project, for example before partnering or integrating with it.
- **Full-build tutorial structure** — Script each point heavily before filming, make every step explicit so no jump is unexplained, and mix in vlog-style footage for conferences. *When:* Making technical tutorials on dense topics where viewers get lost at unexplained steps.

## Numbers
- Bitcoin stabilized above 100k for a while, then dropped to roughly the 80k range over the last week or two (hearsay, unsourced). ([29:22](https://youtu.be/taTXejPts4E?t=1762))
- Anecdote: about 96% of people on a Polymarket market said 'no' and about 4% 'yes' on whether Jesus returns. No source is given. ([29:22](https://youtu.be/taTXejPts4E?t=1762))
- An 11-year-old's pump.fun token was rug-pulled at roughly 32,000 (currency unspecified). Anecdote only. ([25:42](https://youtu.be/taTXejPts4E?t=1542))

## Hot takes
- Web3 consumer apps (NFTs, metaverse, gaming) are unlikely to see mass adoption; finance is the real on-chain story [9:40].
- Tokenized real-world assets are the biggest near-term opportunity, especially tokenized collateral [11:50].
- Prediction markets beat polls as a predictor because real money is at stake [28:06].
- Crypto is not dead; it has matured and is becoming infrastructure underneath everyday systems [47:04].
- Sponsored-style partnership plug (Tiger Data) appears in the content advice segment [40:34]. The episode is mostly opinion, so quality is capped at 2.

## Tools mentioned
Solidity, Rust, Forge (Foundry), Hardhat, React, TypeScript, web3.js, ethers.js, Thirdweb, Polymarket, pump.fun, Canton Network, Ethereum (EVM), MCP (Model Context Protocol), TimescaleDB, Snowflake, X (Twitter)

## Relevance to our work
- **agentos** (1/3): The MCP-plus-semantic-tagging pattern for exposing data to agents touches the knowledge-bucket and retrieval surface, but only as a passing remark. → *Skim how the speaker describes semantic tagging for LLM-crawlable data, and compare it with how MemoryMesh buckets expose metadata to agents.*

# How Web Data Infrastructure Powers the Next Generation of AI — Patricija Žemaitytė, Oxylabs

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `1UmZHb_E_SM` · [watch](https://youtu.be/1UmZHb_E_SM) · **date:** 2026-08-18 · **length:** 19:03 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Patricija Žemaitytė · **orgs:** Oxylabs
- **topics:** infra-cost-scaling, rag-retrieval, data-engineering · **tags:** web-data, scraping, proxies, serp-api, latency, load-testing, observability, grounding, video-data, product-iteration

> Oxylabs' product manager on how public web data infrastructure feeds AI systems: how a video API, a sub-second SERP API and a 60k-rps scraper grew out of repeated client requests, latency cuts and load tests.

## Summary
The speaker, a product manager at Oxylabs (a web intelligence and proxy provider), argues that AI models need live, structured web data, and that the infrastructure to collect it is the hard part. She tells three stories. First, a two-week request for a video API for AI training (at least 5 PB per month) grew through repeated client requests into a full video API suite (downloader, transcripts, subtitles, search, metadata) in about three months. Second, a sub-second search API built for AI grounding first failed to ship because the old scraper took about 4 seconds; the team dropped ads, widgets and layouts and focused on organic results and news. It reached about 650 ms P90 in under two weeks, but was blocked during a client call, so browser rendering had to be added, and the team then hunted seconds across every stage until it averaged 550 ms. Third, scaling a scraper from about 10k to 60k requests per second in under two months revealed that synthetic load tests were not enough, that telemetry becomes part of the load, and that the team should scale gradually and rely on production traffic. The talk closes with the claim that the lasting value is adaptation, not any single product.

## Key ideas
- **Models need live data, and the infrastructure that collects public web data at scale is the real bottleneck** — Training alone is not enough. Models need fresh, live retrieval, and the speaker's company sells the layer that reaches the open web, handles bot defenses and delivers structured data into pipelines and agents. ([0:08](https://youtu.be/1UmZHb_E_SM?t=8))
- **A one-off feature request grew into a product family by iterating on what the client actually needed** — A video downloader request turned into transcript, subtitle, language search and metadata support. The client bought the team's ability to adapt, not the first version. Roughly three months to a full video API suite. ([2:24](https://youtu.be/1UmZHb_E_SM?t=144))
- **SERP data's role changed from analytics to grounding for AI systems, which pushed the latency requirement to sub-second** — Search results now feed retrieval pipelines and grounded answers. A 2024 sub-second attempt on a roughly 4 s baseline was shelved because the market was not ready. ([6:38](https://youtu.be/1UmZHb_E_SM?t=398))
- **Low latency came from narrowing the output to what AI systems use, not from speeding up the old scraper** — The general scraper collects ads, widgets, rich results and AI overviews. The fast search API keeps organic results, top stories and news, and drops the heavy layout. The team calls this a redesign, not an optimization. ([8:05](https://youtu.be/1UmZHb_E_SM?t=485))
- **Browsers are needed to get past blocking, and they bring latency back, so latency has to be hunted stage by stage** — The first version hit about 650 ms P90, then got blocked on a live client call. The fix relied on browsers, which are slow. The team reviewed layouts, parsers, sessions and proxies and cut a second or more at each step, reaching 550 ms average. ([9:26](https://youtu.be/1UmZHb_E_SM?t=566))
- **At scale, the end-to-end job is the unit of load, and telemetry becomes part of that load** — A scraping job includes routing, rendering, proxy handling, browser execution, parsing, retries and delivery. Adding about 2,000 servers did not fix it alone. Logs and metrics became costly at 20k rps. ([12:59](https://youtu.be/1UmZHb_E_SM?t=779))
- **Synthetic load tests miss problems that organic-like traffic reveals, so scale gradually and use production traffic as the final test** — The team hit a wall around 20,000 rps in a load test and could not tell whether the system could go further. They concluded that realistic traffic is the hard part, and that production traffic is the real test. ([14:14](https://youtu.be/1UmZHb_E_SM?t=854))

## Techniques
- **Iterate from client requests into an internal library** — Treat each new client ask (transcripts, subtitles, metadata) as a small adaptation. Glue the pieces into one internal library until the one-off becomes a product family. *When:* Early product work where the client does not yet know the exact spec and deadlines are short.
- **Narrow the response to what the AI consumer needs** — Drop ads, widgets, rich results and layout parsing, and return only organic results, top stories and news. This removes most of the per-request work. *When:* A fast API is needed for an LLM or agent, where the consumer does not need the full page.
- **Stage-by-stage latency audit** — Walk the whole pipeline (layout, parser, sessions, proxies, browser) and cut a fraction of a second at each stage. Measure every stage, not just the total. *When:* A system is far from its latency target and no single breakthrough is available.
- **Realistic load testing with gradual ramp-up** — Replay organic-like traffic rather than only synthetic load. Raise the load in steps, watch telemetry cost, and treat production traffic as the final test. *When:* Scaling a distributed system where synthetic load does not match real client usage.
- **Account for observability as load** — Plan logs and metrics volume as part of capacity, because at high request rates collecting and processing telemetry is itself expensive. *When:* Capacity planning at tens of thousands of requests per second.

## Numbers
- Video API demand: at least 5 PB per month, with a two-week deadline; suite built in about 3 months ([2:24](https://youtu.be/1UmZHb_E_SM?t=144))
- Earlier SERP scraper average latency about 4 seconds, which the 2024 sub-second attempt had to beat ([6:38](https://youtu.be/1UmZHb_E_SM?t=398))
- First fast search version reached about 650 ms P90 in under two weeks ([9:26](https://youtu.be/1UmZHb_E_SM?t=566))
- Fast search API average latency now 550 ms ([10:49](https://youtu.be/1UmZHb_E_SM?t=649))
- Daily requests grew from about 400 million to almost 6 billion ([10:49](https://youtu.be/1UmZHb_E_SM?t=649))
- Scale demand rose from about 10,000 rps to 60,000 rps in under two months, with about 2,000 extra servers added ([12:59](https://youtu.be/1UmZHb_E_SM?t=779))
- Load test hit a wall at about 20,000 rps ([14:14](https://youtu.be/1UmZHb_E_SM?t=854))
- Next internal target (project 150) is about 100,000 rps ([15:37](https://youtu.be/1UmZHb_E_SM?t=937))

## Hot takes
- The next generation of AI will be powered by better infrastructure around the models, not by better models.
- Innovation is the ability to keep adapting fast enough that changing requirements become new infrastructure.
- In the AI era speed is not just performance; it decides which products can exist at all.
- Scale is never a finish line; each target reached reveals the next one.

## Tools mentioned
Oxylabs Fast Search API, headless browsers, proxy network

## Relevance to our work
- **agentos** (1/3): AgentOS's retrieval and grounding layers could face the same latency problem when an agent pulls live web data; the talk's stage-level budget is a useful lens, but it is not a direct change. → *When designing MemoryMesh live retrieval, define a per-stage latency budget and keep only the fields the model actually uses, before adding a faster backend.*
- **general** (1/3): The talk makes a general point that web data acquisition is a separate infrastructure layer with its own reliability and latency problems, not an afterthought of the model. → *Read the Oxylabs-style architecture (routing, rendering, retries, delivery) when designing any agent that depends on live web sources.*

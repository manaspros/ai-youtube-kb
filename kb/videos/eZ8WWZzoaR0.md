# Homa: The End of TCP for AI Clusters — John Ousterhout, Stanford

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `eZ8WWZzoaR0` · [watch](https://youtu.be/eZ8WWZzoaR0) · **date:** 2026-09-18 · **length:** 18:48 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** John Ousterhout · **orgs:** Stanford University
- **topics:** infra-cost-scaling, inference-serving · **tags:** tail-latency, incast, tcp, rdma, roce, congestion-control, receiver-driven, homa, srpt, priority-queues, linux-kernel, distributed-inference, kv-cache, network-transport

> Ousterhout argues AI inference and agentic workloads now send many small latency-sensitive messages, which TCP and RDMA handle badly, and presents Homa, a receiver-driven transport with about 13x lower short-message P99 in his benchmark.

## Summary
John Ousterhout (Stanford) argues that AI workloads have shifted from giant throughput-bound transfers, such as training gradients, to many small messages for inference, KV-cache lookups and agentic coordination, where latency matters more. He explains that tail latency, not average latency, stalls GPU barrier synchronization, and that the phases between exchanges are shrinking from seconds toward milliseconds. He blames incast congestion: short messages queue behind long ones at the destination's top-of-rack egress port, and buffer overflow leads to drops and retransmission timeouts. He argues that sender-driven congestion control, including ECN-based schemes, has control lag and oscillates, and that TCP's byte-stream model hides message boundaries and causes head-of-line blocking. He presents Homa, a message-based, receiver-driven transport that uses unscheduled first packets, receiver grants, SRPT ordering and switch priority queues. In his own benchmark across 50 B to 1 MB messages, Homa's short-message P99 is under 100 microseconds versus over 1 ms for TCP, and long messages are also about 2x faster than TCP. Homa exists as a Linux kernel module that is being upstreamed, and the speaker is offering to help others try it.

## Key ideas
- **AI workloads are shifting from large throughput-bound transfers to many small, latency-bound messages.** — Training still moves massive transfers, but inference and agentic workloads send small metadata and coordination messages, such as KV-cache presence checks and barrier syncs, where round-trip time is what matters. ([1:31](https://youtu.be/eZ8WWZzoaR0?t=91))
- **Tail latency, not average latency, is what stalls GPU work.** — In barrier-synchronized compute, one slow exchange holds up every GPU. When compute phases drop to milliseconds, a few milliseconds of sync time wastes a large share of GPU time. ([4:03](https://youtu.be/eZ8WWZzoaR0?t=243))
- **Incast congestion causes the tail latency.** — Several senders hit one destination at once, long messages pile up in the destination's egress queue, and short messages get stuck behind them. Full buffers cause drops, then timeouts and retransmissions make it worse. ([5:26](https://youtu.be/eZ8WWZzoaR0?t=326))
- **Sender-driven congestion control reacts too late to work well.** — Senders learn of congestion from ECN marks or losses that take round trips to arrive. Many senders adjusting at once with one bit of feedback leads to oscillation. He says the problem has been studied for over 20 years without a good fix. ([9:11](https://youtu.be/eZ8WWZzoaR0?t=551))
- **TCP's byte-stream model hides message boundaries.** — Without boundaries the transport cannot prioritize short messages and cannot tell how much data is still coming. Head-of-line blocking follows when a small message sits behind two large ones. ([10:37](https://youtu.be/eZ8WWZzoaR0?t=637))
- **Homa makes the message, not the byte stream, the unit of transport, and it congests from the receiver.** — Requests and responses are independent messages with known lengths, so the receiver knows the remaining size from the first packet. Congestion is controlled at the last downlink, where the receiver has the most information. ([12:03](https://youtu.be/eZ8WWZzoaR0?t=723))
- **Homa uses unscheduled packets, receiver grants, and switch priority queues to implement SRPT.** — The sender transmits the first few packets blindly. The rest go out only when the receiver grants them. The receiver delays grants when many messages are incoming, and it maps message priority onto switch queues so short messages bypass long ones. ([13:20](https://youtu.be/eZ8WWZzoaR0?t=800))
- **The benchmark result is the case for the protocol, and the code is available.** — Homa is a Linux kernel module on GitHub, and he is working to get it upstreamed. He offers to help teams try it. ([12:03](https://youtu.be/eZ8WWZzoaR0?t=723))

## Techniques
- **Message-framed transport (RPC unit)** — Treat each request and response as an independent message with its length carried in the transport header, so the receiver learns the total size from the first packet. *When:* Traffic mixes very small and very large messages and you need to prioritize or predict the remaining bytes.
- **Receiver-driven grant scheduling** — Send only a blind first chunk, then send grant packets that pace the rest. Delay grants when many senders target one receiver, and grant to the shortest remaining message first. *When:* Incast is the bottleneck, such as many nodes sending to one GPU host or one downlink.
- **Unscheduled first-RTT send** — Transmit the first few packets without waiting for permission so a short message finishes in one round trip. *When:* Most messages are short and a handshake round trip would dominate their latency.
- **SRPT via switch priority queues** — Set each packet's switch queue from the sender's remaining message size, so shorter messages use higher-priority egress queues. *When:* Switches expose several egress queues per port, typically eight, and you want short messages to bypass queued long ones.
- **Percentile sweep by message size** — Benchmark round-trip time at P50 and P99 across message sizes from about 50 B to 1 MB, comparing protocols on the same curve. *When:* Evaluating a transport or network change for a mixed-size workload, where averages hide the tail.

## Numbers
- Short-message P99 round-trip time: TCP above 1 ms vs Homa under 100 microseconds, about 13x better (speaker's benchmark). ([15:47](https://youtu.be/eZ8WWZzoaR0?t=947))
- Long-message performance: Homa is almost 2x better than TCP on the longest messages in the same benchmark. ([15:47](https://youtu.be/eZ8WWZzoaR0?t=947))
- Switch egress ports typically have about 8 priority queues that Homa uses for prioritization. ([14:47](https://youtu.be/eZ8WWZzoaR0?t=887))
- Compute phases in agentic workloads are dropping from seconds (for example 5 s with a few ms of exchange) toward the millisecond scale, so sync time becomes a large share of GPU time. ([4:03](https://youtu.be/eZ8WWZzoaR0?t=243))
- Speaker's claim, not shown in the talk: Homa can reduce tail latency by an order of magnitude or more. ([18:10](https://youtu.be/eZ8WWZzoaR0?t=1090))

## Hot takes
- TCP and RDMA are poorly suited to AI clusters that mix small and large messages.
- Congestion control belongs at the receiver, which has better information than senders.
- Tail latency, not average latency, is the metric that limits AI cluster throughput.

## Tools mentioned
Homa (Linux kernel module), TCP, RDMA over Converged Ethernet (RoCE), ECN marking

## Relevance to our work
- **general** (1/3): The tail-latency and barrier-sync argument applies if we ever run multi-node inference or distributed KV-cache lookups. → *Keep the Homa kernel module and talk in mind only if we plan multi-node serving; no action needed now.*

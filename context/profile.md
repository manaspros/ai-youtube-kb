# What we're building (edit me — every Haiku/Sonnet pass reads this)

## AgentOS — "AWS for self-hosted AI agents" (personal/uni project, ~/Codes/AgentOS)
Opt-in infra for ANY agent: point OpenAI base_url at one proxy URL, toggle pillars in a manifest.
- L1 Govrix Scout (Rust proxy :4000): budgets, PII/prompt-injection scan, strategy routing, Merkle audit log.
- L2A MemoryMesh: knowledge buckets, hybrid retrieval (BM25 + pgvector), tiered cross-session memory,
  conflict resolution + provenance, GraphRAG, RAGAS evals.
- L2B InferCraft: vLLM + Ray Serve, pluggable KV-cache strategies (H2O, CPU offload, LMCache),
  speculative decoding (EAGLE-3), quantization (NVFP4), 4-class priority scheduler + preemption on one RTX 5090.
- L2C Crucible: opt-in sandboxed code execution (self-hosted celld, Cloudflare backend), exec-gate guardrails.
- L2D SkillForge: mine agent telemetry → governed, reusable skills (open question: success signal +
  skill-worthiness scoring). EvolveCraft: self-improving agents.
- L3 storage: Postgres/pgvector, TimescaleDB, Redis, Neo4j; roadmap: ClickHouse analytics,
  Parquet + DuckDB archive / per-tenant DuckDB read tier, Redis multi-instance budget counters.
- L4 observability: Prometheus/Grafana, OTel, Locust load tests.
- Next-phase thesis: prove it as a distributed system with benchmarks + correctness checks, not demos.


## ProsHarness (~/Codes/ProsHarness)
- Harness around the Claude Code CLI: checkpoint/resume of long agent runs, plan → critique (Codex) → debate,
  loops/schedules, skill ranking, phone-driven approvals, zero-token credential handling.

## Recurring interests
- Context engineering, Claude Code / coding-agent workflows, subagents & multi-agent orchestration,
  evals for agents, entity resolution / data quality with LLMs, cheap-model (Haiku) pipelines.
- Learning track (Nov 2026+): LLM serving internals (SGLang/vLLM scheduler, KV cache, spec decoding) then Triton
  decode kernels on the RTX 5090. Plan + resource overlap: `context/inference-learning-path.md`.

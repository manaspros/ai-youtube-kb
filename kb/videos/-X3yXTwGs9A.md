# AI Writes Code Faster Than Your Team Can Review It - Andrew Norrish, Sourcegraph

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `-X3yXTwGs9A` · [watch](https://youtu.be/-X3yXTwGs9A) · **date:** 2026-11-02 · **length:** 18:57 · **format:** talk · **quality:** 2/5 · **depth:** practitioner
- **speakers:** Andrew Norrish · **orgs:** Sourcegraph, HackerOne, Anthropic
- **topics:** pr-code-review, enterprise-adoption, observability · **tags:** code-review-bottleneck, incident-response, sre, code-search, agentic-search, monorepo, bulk-remediation, security-triage, rca-agent, vendor-pitch

> Sourcegraph's field director argues AI code outpaces human review, so SRE and platform teams need code-search-driven investigation, monitors and bulk remediation. Mostly a vendor pitch.

## Summary
Andrew Norrish (Director of Field Engineering, Sourcegraph) argues that agentic coding has moved the bottleneck from writing code to reviewing it, with more and larger PRs, lagging trust in AI code, and more incidents traced to unreviewed AI-written changes. He says SRE and platform teams absorb that burden and that AI works best in well-bounded domains such as vulnerability remediation, security scanning and large migrations. He frames Sourcegraph's code graph and search as a context engine for agents and organizes SRE work into investigation, prevention and remediation. He then gives three customer or internal examples: agentic triage of HackerOne reports, an RCA agent that finds the commit behind a production incident, and a read-only code-search agent evaluated over hundreds of historical branches. The statistics are unsourced, and the talk is a vendor pitch with little implementation detail.

## Key ideas
- **Code review, not code writing, is now the bottleneck. PR counts and PR sizes have grown, and developers cannot review AI output as fast as it is produced.** — Speaker's framing of the new constraint. Trust in AI code is low, yet many developers say they do not always verify it. ([3:00](https://youtu.be/-X3yXTwGs9A?t=180))
- **Cross-service incidents traced to unreviewed AI code fall on SRE and platform teams, who often lack the context to fix them. Manual commit scanning cannot keep up with remediation.** — A fix found in one repo may apply to hundreds of others, and disparate teams applying it by hand miss some. The talk says the incident rise is outpacing hiring. ([5:53](https://youtu.be/-X3yXTwGs9A?t=353))
- **AI works best in narrow, well-bounded domains with full context, such as vulnerability remediation, security scanning, large migrations and non-developer prototyping.** — The speaker says broad autonomous code generation is not where AI is winning yet. SRE and platform teams already run semi-autonomous, bounded processes, so they can gain the most. ([10:16](https://youtu.be/-X3yXTwGs9A?t=616))
- **Sourcegraph's SRE workflow has three parts: investigation, prevention and remediation. Each maps to a code-graph or search capability.** — Investigation uses deterministic search across every repo, branch and commit. Prevention uses monitors that alert on risky commits or non-compliant patterns. Remediation uses bulk changes across all repos. ([13:00](https://youtu.be/-X3yXTwGs9A?t=780))
- **Prevention can be done with monitors on commits that flag risky or non-compliant patterns before they reach production.** — The talk describes monitors for risky commits and patterns that may be non-compliant. The speaker presents these as a way to check AI-written code against organizational rules. ([14:03](https://youtu.be/-X3yXTwGs9A?t=843))
- **Security triage at Sourcegraph: HackerOne webhooks call an agentic search that decides whether a report can be ignored, needs a proposed fix, or needs deeper human review.** — Presented as an internal workflow the security team built organically. It targets the growing volume of reports that need real-time judgment. ([15:00](https://youtu.be/-X3yXTwGs9A?t=900))
- **An enterprise RCA agent turns an error-rate spike into a commit. It resolves the deployed tag or branch first, because production is rarely main, then searches git history for the triggering commit and author.** — Afterwards the agent can revert and redeploy, or triage and share its findings with the SRE team. The customer has over 5,000 developers. ([16:25](https://youtu.be/-X3yXTwGs9A?t=985))
- **A customer's internal code-review agent is evaluated against hundreds of historical branches of a large monorepo. Its code-search agent is read-only, deterministic and fast, and the publish step runs only when evals pass.** — Chosen to avoid the non-determinism of other agentic tools. The talk gives no eval metrics. ([17:24](https://youtu.be/-X3yXTwGs9A?t=1044))

## Techniques
- **Deterministic cross-repo code search for incident root cause** — Index the whole org's repos, branches and commits, then run one search query across all of them to locate the code behind an issue. Use this before agentic reasoning to narrow where to look. *When:* Cross-service incidents where the cause spans several repos or the context was never reviewed by a human.
- **Commit-pattern monitors for AI-written code** — Define rules that match risky code patterns or non-compliant constructs and alert when a commit matches them. The talk does not show configuration. *When:* Enforcing org or compliance patterns on high volumes of agent-generated PRs.
- **Bulk remediation across repos** — Once a bad pattern or fix is identified, apply the change across every impacted repo at once, instead of asking each team to apply it. *When:* Vulnerabilities or patterns that recur across many services.
- **Webhook-triggered agentic triage** — Send each incoming security report from a bug-bounty platform (HackerOne) via webhook to an agent with code search. The agent classifies each report as ignore, propose a fix, or escalate to human review. *When:* High-volume security intake that needs fast first-pass judgment.
- **Automated RCA from deploy history** — On an error-rate or downtime alert, (1) identify the branch or tag actually deployed to production, (2) run agentic search over git history to find the triggering commit and author, (3) either revert and redeploy or send a triage report to SREs. Pulls in logs and traces to connect them to source. *When:* Production regressions where the deployed ref differs from main.
- **Eval-gated code-review agent over historical branches** — Build an eval suite from hundreds of historical branches of the codebase, run a read-only code-search agent over them, and only trigger push/publish when the evals pass. The talk does not name the metrics. *When:* Shipping a custom code-review agent for a large monorepo where non-determinism is a risk.

## Numbers
- Industry analyses expect about two-thirds of code to be AI-written by 2027. The speaker gives no source. ([6:52](https://youtu.be/-X3yXTwGs9A?t=412))
- Some organizations estimate about twice as many PRs are merged with agentic coding. PRs are more than twice the size of human-written PRs, so review time roughly doubles. ([7:54](https://youtu.be/-X3yXTwGs9A?t=474))
- Almost every developer says they do not trust all AI-written code, and almost half say they do not always verify it. ([7:54](https://youtu.be/-X3yXTwGs9A?t=474))
- A customer with over 5,000 developers built an RCA agent that runs automatically on downtime or error-rate spikes. ([15:00](https://youtu.be/-X3yXTwGs9A?t=900))
- A customer's code-review agent is evaluated over hundreds of historical branches of a massive monorepo. ([17:24](https://youtu.be/-X3yXTwGs9A?t=1044))

## Hot takes
- Vendor pitch: the talk is a Sourcegraph sales presentation, and the examples are product workflows. Quality is capped at 2 for thin substance.
- The industry statistics (two-thirds of code by 2027, doubled PRs, doubled review time, trust figures, and an Anthropic comprehension claim) are cited without sources, and one slide was skipped during the talk.
- The claim that AI wins in bounded domains and fails at broad autonomous development is a useful framing, but the talk offers no measured evidence for it.
- Strongest content is the three workflow examples (triage, RCA from deployed tag to commit, and eval-gated review over historical branches). The eval metrics and monitor configuration are not shown.

## Tools mentioned
Sourcegraph (code search, code graph, Deep Search, MCP server), HackerOne, git (history search for incident commits)

## Relevance to our work
- **agentos** (1/3): Agent-caused incidents and attribution to commits touch on the audit and governance story (Merkle audit log), but the talk is not about the proxy or memory layers. → *Consider whether the Merkle audit log could record the commit or agent run behind each generated change, so an incident can be traced back to the agent that produced it.*
- **prosharness** (1/3): The eval-gated publish step over historical branches is a pattern for guarding autonomous agent output. ProsHarness already has plan, critique and debate loops. → *Consider gating ProsHarness autonomous commits or pushes on a replay eval over recent historical branches before publish.*

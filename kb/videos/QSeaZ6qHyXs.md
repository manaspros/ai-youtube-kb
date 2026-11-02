# Claude Managed Agents Q&A: Evals, CI/CD and Multi-Tenancy (Part 4 of 4) — Anthropic

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `QSeaZ6qHyXs` · [watch](https://youtu.be/QSeaZ6qHyXs) · **date:** 2026-10-12 · **length:** 18:58 · **format:** other · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Anthropic presenters (unnamed in transcript) · **orgs:** Anthropic
- **topics:** agent-architecture, multi-agent, evals, sandboxing-execution · **tags:** claude-managed-agents, cma, anthropic-cli, yaml-config, ci-cd, eval-sweeps, eval-data-quality, tenant-isolation, workspaces, outcomes-rubric, long-running-sessions, sub-agents, custom-tools, human-in-the-loop, multiplayer-agent, pr-review-agents, self-hosted-sandbox, q-and-a

> Anthropic presenters answer audience questions on Claude Managed Agents: YAML-as-code deployment, eval sweeps, tenant isolation via workspaces, long runs, and sub-agents for custom tools.

## Summary
This is the closing Q&A of a four-part Claude Managed Agents series, with Anthropic presenters answering live audience questions. They describe defining long-lived agent resources as YAML checked into a repo and synced by CI through the Anthropic CLI, Terraform-style. On evals, they run large parallel session sweeps on each new model to strip out harness assumptions, and they stress that eval data quality matters more than the eval tool. For multi-tenancy, the workspace is the access boundary, and true data segregation means one workspace per customer, with a metadata field on sessions for lighter mapping. They explain that sessions can run past six hours with no special setup when an outcome rubric defines the exit criteria, and they describe a coordinator pattern in which a sub-agent handles custom tools so the main agent stays free to accept messages. Several answers are product-specific or sales-leaning, and the sandbox answers point to self-hosted options such as Modal and cookbooks for other providers.

## Key ideas
- **Agent resources can be kept as code** — Long-term agent resources go into YAML in the repo. CI then pushes them to the platform with the CLI on every change, which is Terraform-like. The presenters say they use the same approach internally. ([0:35](https://youtu.be/QSeaZ6qHyXs?t=35))
- **Messages are blocked during a custom tool wait** — While the model waits on a custom tool result, the platform pauses and rejects new user messages with a 400, because the tool result must come next to keep ordering. Messages sent while the model is doing other work are queued. ([1:07](https://youtu.be/QSeaZ6qHyXs?t=67))
- **Eval sweeps run at model-release speed** — The team gets early model access and runs large parallel session sweeps in the cloud, for example 10,000 sessions, to find harness assumptions that can be removed or tuned for each release. The evals cover general tasks, not only coding. ([3:19](https://youtu.be/QSeaZ6qHyXs?t=199))
- **Bad eval data gives misleading 100% scores** — Some early evals were ill-defined and scored 100% without meaning much. The advice is to iterate on the dataset and problem setup first. Mining historical session logs and scoring them is a practical way to build that dataset. ([3:51](https://youtu.be/QSeaZ6qHyXs?t=231))
- **Workspace is the access boundary** — Resources are bound to a workspace, and any API key in that workspace can reach them. There are no fine-grained sharing controls inside a workspace, so teams split access by putting groups in different workspaces under an org. ([5:27](https://youtu.be/QSeaZ6qHyXs?t=327))
- **Tenant isolation needs a workspace per customer** — Separate agents per customer give segregation within one workspace, and a metadata field such as customer ID on the session tracks the mapping. When a customer requires legal-grade separation, the presenters say to use a workspace per customer, or an org per customer for the strongest isolation. ([9:16](https://youtu.be/QSeaZ6qHyXs?t=556))
- **Long runs rely on exit criteria, not special plumbing** — The outcome feature takes an exit criterion or rubric, and the agent keeps iterating until it meets it. Sessions can run past six hours with no special configuration. Status can come from the session events API or from a custom status tool that the agent calls at intervals. ([15:17](https://youtu.be/QSeaZ6qHyXs?t=917))
- **Sub-agent takes the custom tool so the coordinator stays free** — The main coordinator delegates to a sub-agent that defines and handles the custom tool. The main thread stays available for incoming messages while the sub-agent works. The session shows as idle on the main thread even while sub-agents are busy. ([16:56](https://youtu.be/QSeaZ6qHyXs?t=1016))
- **Agents can review PRs and self-QA in a sandbox** — A PR webhook can start many review sessions with sub-agents to look for bugs. Agents can also run the app in a sandbox, check it with a browser, and maybe return a video. The presenters call the volume of agent-written PRs an open problem. ([6:32](https://youtu.be/QSeaZ6qHyXs?t=392))

## Techniques
- **Agent definitions as YAML synced by CI** — Keep each agent (system prompt, model, tools) in YAML under version control. Use the CLI in CI to push changes. For several workspaces, a single definition is synced to every target in one CI run. *When:* When the same agent must exist in several places, or when durable agent config should be reviewed like infrastructure.
- **Parallel eval sweeps on new model releases** — Build data sets for the task. Run many sessions in parallel in the cloud. Score the results, then tune prompts and remove or add harness assumptions. *When:* When a new model arrives and the harness may contain scaffolding that is no longer needed.
- **Historical-session eval dataset** — Export past agent sessions and their outcomes. Score them against the desired result to make a baseline dataset before writing a new eval. *When:* When starting evals for an existing agent and no labeled data exists yet.
- **Workspace-per-customer isolation** — Create one workspace per customer for data segregation. Map customers to agents or sessions with a metadata field such as customer ID. Sync agent definitions across workspaces with CI. *When:* When customers need legal-grade data separation in a multi-tenant product.
- **Rubric-based exit criteria for long runs** — Define an outcome with an explicit rubric. Let the agent loop until it passes, instead of sending it step prompts. Track progress through the events API or a status tool. *When:* For multi-hour tasks that have a clear, checkable end state, such as rebuilding a UI to match a spec.
- **Coordinator with a custom-tool sub-agent** — Create a coordinator agent that delegates to a sub-agent. Define the custom tools on the sub-agent, so the coordinator can keep receiving user messages. *When:* When a human must be able to message the main agent while a tool-using step is still running.
- **Per-thread session mapping for multi-user chat** — Map each chat thread to one session. Inject each user message with the sender's name. Share memory across sessions. Give the agent an explicit post-to-channel tool instead of mirroring its replies. *When:* When building a shared assistant in Slack-style channels with several people talking to one agent.

## Numbers
- Example scale: spin up 10,000 sessions in parallel for an eval sweep (speaker's example of cloud parallelism, not a measured result) ([3:19](https://youtu.be/QSeaZ6qHyXs?t=199))
- Sending a message while a custom tool result is pending returns HTTP 400 ([1:39](https://youtu.be/QSeaZ6qHyXs?t=99))
- Sessions run past six hours with no special configuration when an outcome exit criterion is set ([15:51](https://youtu.be/QSeaZ6qHyXs?t=951))
- Audience member says the presenters deploy every 30 days (question premise, not confirmed by the speaker) ([6:32](https://youtu.be/QSeaZ6qHyXs?t=392))

## Hot takes
- Garbage in, garbage out: an eval that scores 100% can mean nothing, so fix the data and problem setup first.
- The main agent can stay responsive during long tool work only if a sub-agent owns the custom tools.
- Use workspace per customer, not a shared workspace with a metadata tag, when a customer requires real data segregation.

## Tools mentioned
Claude Managed Agents (CMA), Anthropic CLI (transcribed as 'Ancho CLI'), Claude Code, Modal, E2B (transcribed as 'EB2'), Daytona, Slack

## Relevance to our work
- **prosharness** (2/3): ProsHarness does checkpoint/resume of long runs. Rubric-based exit criteria and a status tool or events stream address the same problem of knowing whether a multi-hour run is done and how far it has got. → *Try an outcome-style exit rubric for one long ProsHarness run, and add a status tool that reports checkpoints, to compare with the current resume logic.*
- **agentos** (1/3): AgentOS has a RAGAS eval plan. The talk's advice to build evals from historical sessions and to fix the dataset first fits how AgentOS would bootstrap evals from telemetry. → *Before trusting any AgentOS eval score, build a baseline set from past agent sessions and check that the labels mean what the score claims.*

# We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `LqLoYksJ6do` · [watch](https://youtu.be/LqLoYksJ6do) · **date:** 2026-08-18 · **length:** 21:57 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Moritz Johner · **orgs:** Form3
- **topics:** security-guardrails, sandboxing-execution, software-factory · **tags:** dependency-patching, cve-remediation, blast-radius, prompt-injection, firecracker, microvm, docker-socket, credential-split, deterministic-vs-agentic, egress-policy, agent-retrospective, ci-fix-loop

> Form3's Moritz Johner describes PatchPilot, an agent that patches CVEs across thousands of repos, and why production credentials make a coding agent a supply-chain actor needing deterministic controls, credential splits, and microVM isolation.

## Summary
Moritz Johner from Form3 describes PatchPilot, an internal tool that remediates CVEs across thousands of repositories by combining a deterministic Go orchestrator with agents that do the reasoning. He argues that Dependabot and Renovate only see manifests, so they miss CVEs in base images or Dockerfile downloads and cannot handle coupled upgrades such as a Go runtime bump that forces a linter bump. The core thesis is that once an agent holds production credentials it is a supply-chain actor, so it deserves the same guardrails as an engineer. The design keeps the agent limited to editing files, while the deterministic layer vets, commits, pushes, opens PRs and triggers CI, which limits blast radius if the agent is prompt-injected. He reports that Docker socket access effectively lets an agent escape, so the team moved the agent into a Firecracker microVM with its own kernel and a policed network path. He is candid that prompt injection is unsolved, that sandbox tooling is still immature, and that orchestration on top is still missing.

## Key ideas
- **Dependency bots only see the manifest** — Dependabot and Renovate can only bump versions in manifests. CVEs living in OS packages in base images, or binaries fetched by a Dockerfile URL, are invisible to them. ([1:14](https://youtu.be/LqLoYksJ6do?t=74))
- **Patches are coupled, so you need reasoning, not just bumping** — Bumping the Go runtime may force a linter bump, and the new linter rules can break the codebase. Old tools open a PR and leave the mess behind, so the tool must work out what else has to move to reach green CI. ([1:14](https://youtu.be/LqLoYksJ6do?t=74))
- **A useful agent with production credentials is a supply-chain actor** — The speaker's thesis is that the moment an agent gets production credentials it becomes a supply-chain actor like any engineer, so it should get the same guardrails as engineers. The question is not whether agents are dangerous in general. ([2:43](https://youtu.be/LqLoYksJ6do?t=163))
- **Split deterministic orchestration from agentic reasoning** — A boring Go controller discovers vulnerable images, maps images to repos, clones, vets output, commits, pushes, opens PRs and watches CI. Agents are called only for reasoning, such as remediating a CVE or diagnosing a CI failure. ([3:46](https://youtu.be/LqLoYksJ6do?t=226))
- **Withhold write and CI credentials from the agent** — The agent has no GitHub write access and cannot trigger CI. Those actions sit in the deterministic layer, so a prompt-injected agent has a smaller blast radius. The speaker says that the choice of what is deterministic and what is agentic is the security model. ([11:38](https://youtu.be/LqLoYksJ6do?t=698))
- **Prompt injection cannot be solved, only bounded** — A small patch produced about 70,000 changed lines, which gives a very wide attack surface. The team steers the agent to distrust vendor directories and CI logs, and it runs end-to-end test repos with planted malicious deprecated functions as injection evals. ([13:06](https://youtu.be/LqLoYksJ6do?t=786))
- **A Docker socket inside a sandbox is effectively game over** — Agents want Docker to build and verify images, but a Docker socket lets them spawn privileged containers and read other processes. The team ran this in production, then moved off it. Existing agent sandboxes such as Codex's and Claude Code's are judged insufficient once a Docker socket is present. ([14:37](https://youtu.be/LqLoYksJ6do?t=877))
- **Micro-VM per agent with egress through a policy proxy** — Each agent runs in a Firecracker microVM with its own kernel, so the Docker daemon inside is contained. Networking is cut off except a DNS and TCP forwarder that feeds a proxy applying host, port and CIDR rules. Network policy differs between the deterministic layer and the agent, since Java, Python and Go need different ecosystems. ([15:58](https://youtu.be/LqLoYksJ6do?t=958))

## Techniques
- **Deterministic controller plus scoped agent steps** — Keep discovery, cloning, vetting, committing, pushing, PR creation and CI watching in plain code. Call the agent only for reasoning steps, and give it file edits but no push or CI credentials. *When:* Any autonomous agent that touches production repos or other systems where write actions need to be reliable and auditable.
- **Minimal change-set instruction plus post-agent vetting** — Tell the agent to bump only the versions that fix the finding, with no opportunistic upgrades. After it finishes, a deterministic step checks for empty files and stray compiled binaries before commit. *When:* Automated dependency or remediation work where agents tend to over-change or leave junk artifacts.
- **Bounded CI-fix loop with human escalation** — Open the PR, watch CI, feed the logs and workflow metadata to a fix agent, then repeat. Stop at a maximum retry count and hand the PR to a human. Tell the fix agent not to revert its earlier changes. *When:* Agent-generated PRs where CI failures are common and an endless retry loop would waste budget.
- **End-of-run retrospective aggregated across runs** — At the end of each agent invocation, ask for what went well, what went wrong, what tools were missing and what context would have helped. Aggregate across PRs to separate infrastructure failures from repo-complexity issues, then fix the system prompt or add repo-specific instructions. *When:* Running agents at scale when you need to find recurring failure causes without per-run observability tooling.
- **Planted-injection end-to-end tests as evals** — Build a test repo containing a deprecated function or migration guide that tries to steer the agent into malicious actions, then check that the agent ignores it. *When:* Any agent that reads untrusted repo content, such as vendored code, logs or docs.
- **MicroVM sandbox with a policed egress path** — Run the agent and its Docker daemon inside a Firecracker microVM with its own kernel. Route all traffic through a DNS and TCP forwarder to a proxy that applies host, port and CIDR rules, optionally with a custom CA for TLS inspection. *When:* Agents that must build or run containers, where a shared host kernel or a Docker socket would be unacceptable.

## Numbers
- Thousands of repositories in the patching backlog ([0:08](https://youtu.be/LqLoYksJ6do?t=8))
- A small dependency-bump PR changed about 70,000 lines ([11:38](https://youtu.be/LqLoYksJ6do?t=698))
- The agent system prompt is about 2,000 words ([5:48](https://youtu.be/LqLoYksJ6do?t=348))
- micro sandbox project has existed for about three or four months when the talk was given ([18:20](https://youtu.be/LqLoYksJ6do?t=1100))

## Hot takes
- A coding agent is a supply-chain actor as soon as it has production credentials, so it needs the same guardrails as an engineer.
- Built-in agent sandboxes such as Codex's and Claude Code's are worthless once you give the agent Docker socket access.
- Prompt injection is not solvable, so the only real defence is limiting blast radius.
- The choice of what is deterministic and what is agentic is the security model.

## Tools mentioned
PatchPilot, Dependabot, Renovate, Firecracker, Docker, Kaniko, BuildKit, Landlock, bubblewrap, Go, Slack, GitHub, micro sandbox, Kubernetes agent-sandbox SIG, OpenSandbox

## Relevance to our work
- **agentos** (2/3): Crucible is the opt-in sandboxed code-execution layer, and this talk covers a microVM sandbox with a Docker socket and a policed egress path. → *Compare Crucible's design with a Firecracker microVM plus egress proxy, and check whether its exec path ever exposes a Docker socket or write credentials to the agent.*
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI, so it can apply the credential split and a deterministic commit-and-push step, and the retrospective prompt maps onto its checkpoint and resume design. → *Keep git push, PR and CI-trigger calls in the harness rather than in the Claude Code session, add a pre-commit vet for empty files and binaries, and add an end-of-run retrospective prompt that gets logged.*
- **general** (1/3): The planted-injection end-to-end test is a concrete eval method for any agent that reads untrusted repo content. → *Write one injection test repo with a malicious deprecated function and run it against any agent that edits code before it ships.*

# Your company brain will leak secrets: how we stopped it for big banks — Tanmai Gopal, PromptQL

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `0uC6u0lJJl4` · [watch](https://youtu.be/0uC6u0lJJl4) · **date:** 2026-09-18 · **length:** 26:25 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Tanmay Gopal · **orgs:** PromptQL, Hasura, Anthropic, Instacart, Stitch Fix
- **topics:** memory, governance-compliance, security-guardrails · **tags:** company brain, shared wiki, access control, scopes, credential injection, human-in-the-loop, knowledge management, enterprise security, multiplayer agents, PromptQL

> Tanmay Gopal (PromptQL) on why a shared company brain leaks secrets and how to gate it: one company-wide markdown wiki with per-page scopes, human-approved agent suggestions, and user credentials injected at tool execution.

## Summary
The speaker, PromptQL's CEO, argues that a company brain (shared context plus access rules for coding agents) will leak sensitive data unless access is controlled. He reports that a healthy brain's daily update volume keeps rising, based on about 5,000 wiki pages built over two months. He rejects three designs: GitHub-based shared skills (people will not maintain them), per-team silos, and agent auto-write. His alternative is one linked markdown wiki where each page has read-write scopes and the agent suggests additions that a named human accepts. For tools, he says user credentials should be injected at the HTTP and SQL layers rather than stored in the sandbox, and that the user who adds a tool controls who can use it. He illustrates with an SRE debugging thread where shared knowledge is created but privilege escalation becomes the risk. The talk is a practitioner account from a vendor, so the product pitch is present but the design principles are concrete.

## Key ideas
- **A company brain will leak secrets by default, and this is the main thing holding back deploying shared agents.** — The speaker's example is an intern gaining access to everyone's compensation details. He says this fear is the biggest blocker to rolling out shared agents at scale. ([0:08](https://youtu.be/0uC6u0lJJl4?t=8))
- **A healthy brain's daily update count rises over time instead of falling.** — Over two months, the update volume per day kept creeping up. He reads this as people teaching the system more skills as earlier ones start to work. He admits this is early data. ([4:02](https://youtu.be/0uC6u0lJJl4?t=242))
- **Grow the brain bottom-up. Do not build it top-down.** — Each person owns and writes their own slice. A two-year top-down project will not work for an organization that is decades old. ([10:10](https://youtu.be/0uC6u0lJJl4?t=610))
- **Shared skills in GitHub will not get written, and team-only silo brains do not scale across the company.** — People rarely write skills for colleagues they do not know. A per-team or per-channel memory is locked to one place and cannot be reused elsewhere. ([13:53](https://youtu.be/0uC6u0lJJl4?t=833))
- **The agent should suggest additions and a human should accept them, rather than auto-writing memory.** — Auto-written memory means nobody knows what was added. The middle path is a review box where the user sees the bullet facts, picks the scopes, and clicks Add to Wiki. The user only needs to check that the facts are correct. ([15:17](https://youtu.be/0uC6u0lJJl4?t=917))
- **Two hard rules: one company-wide wiki, and every change is attributed to a named human.** — Entries must never be credited to Claude or to any agent. Attribution to a person is what makes accountability and remediation possible. ([18:11](https://youtu.be/0uC6u0lJJl4?t=1091))
- **Read with the user's own credentials, so the agent sees only what that user can see.** — The agent uses the current user's claims when it reads from the wiki, for every read. This keeps access tied to the human in the conversation. ([19:36](https://youtu.be/0uC6u0lJJl4?t=1176))
- **Multi-person debugging creates the best knowledge, but it also creates privilege escalation.** — In his SRE example, a disagreement about an undocumented technical decision led to a root cause and a documented fix. The same agent in the same thread could also deploy to prod, so the risk is that one agent carries everyone's privileges. ([20:59](https://youtu.be/0uC6u0lJJl4?t=1259))
- **Do not store credentials in the sandbox. Inject the acting user's credentials at the HTTP and SQL layers, and proxy all real-data access.** — The agent then behaves as the human in each interaction. The person who adds a tool controls who can use it. ([23:22](https://youtu.be/0uC6u0lJJl4?t=1402))

## Techniques
- **Single linked markdown wiki with per-page scopes** — Store all shared context as interlinked markdown pages. Give each page read-write scopes and named owners. Keep one company-wide wiki and do not split it into silos. *When:* When many people contribute context that others need to reuse, and access must follow the content.
- **Agent suggests, human accepts** — The agent drafts the fact bullets and the target scopes after a task. A human reviews them in a small box and clicks Add to Wiki. The agent does not write on its own. *When:* When you want shared memory to grow without losing track of who added what or where it came from.
- **Attribute every wiki change to a named human** — Never let an agent be the recorded author. Tie each change to the person who accepted it so that a leak can be traced to someone. *When:* For any shared memory in a regulated or high-trust environment.
- **Per-request user credential injection at the HTTP and SQL layer** — Hold no credentials in the sandbox. Proxy every tool or data call. Attach the acting user's credentials at the HTTP or SQL layer for each call, so the agent acts as that user. *When:* When one shared agent runs tools for several people with different privilege levels, such as a shared Slack agent doing incident work.
- **Proxy and virtualize real-data access** — Route all data and tool access through a layer that the user who registered the tool controls. Use that layer to enforce who may call what. *When:* Whenever an agent touches production or sensitive systems.

## Numbers
- The company brain has about 5,000 interconnected wiki pages, modeled as a wiki. ([2:35](https://youtu.be/0uC6u0lJJl4?t=155))
- PromptQL has partnered with about 15 to 20 organizations over the past year, and is only now opening access more widely. ([1:10](https://youtu.be/0uC6u0lJJl4?t=70))
- Daily wiki update volume has been gently rising over the last two months, which the speaker reads as a sign of a healthy brain. ([5:02](https://youtu.be/0uC6u0lJJl4?t=302))

## Hot takes
- Shared skills in a GitHub repo will not be maintained by busy people, so the approach fails from the start.
- Auto-written agent memory is unsafe in an enterprise, and a human must approve each change.
- Build the company brain bottom-up, one person at a time, since no one can build one top-down for a 100-year-old company.

## Tools mentioned
Claude Code, Slack, GitHub, OpenTelemetry, Opus 4.5, PromptQL, Hasura GraphQL engine

## Relevance to our work
- **agentos** (2/3): The per-scope wiki, human-approved memory writes and per-user credential injection map onto AgentOS MemoryMesh (knowledge buckets, provenance) and the Crucible sandbox. → *Add a suggest-then-accept write path with a required human author field to MemoryMesh's conflict and provenance handling, and check whether credentials can stay out of the sandbox.*
- **general** (2/3): The thesis on scoped, human-attributed shared memory is a general governance pattern for multi-user agents. → *Read the wiki scope model and the credential injection description before designing any shared agent memory.*
- **prosharness** (1/3): ProsHarness runs Claude Code with phone-driven approvals, and the human-accept step is a similar gate. The idea of a shared context store is only loosely relevant. → *Consider a review gate for any memory or skill write that a ProsHarness run proposes, with the human named as author.*

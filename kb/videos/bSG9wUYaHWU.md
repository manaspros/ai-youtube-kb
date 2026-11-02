# Context Is the New Code — Patrick Debois, Tessl

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `bSG9wUYaHWU` · [watch](https://youtu.be/bSG9wUYaHWU) · **date:** 2026-05-18 · **length:** 27:14 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Patrick Debois · **orgs:** Tessl
- **topics:** context-engineering, evals, skills-self-improvement, security-guardrails · **tags:** context development lifecycle, AGENTS.md, CLAUDE.md, skills, skill registry, LLM-as-judge, error budgets, agent logs, AI SBOM, context filter, prompt injection, harness engineering, architect track

> Patrick Debois argues that agent context (instructions, skills, specs) needs its own lifecycle like code: generate, test with evals, distribute as packages, observe logs, then adapt.

## Summary
Debois frames context as the new code and proposes a context development lifecycle, an infinity loop of generate, test, distribute, observe and adapt, borrowed from DevOps. He says skills have replaced large amounts of hand-written helper code, because a plain-language workflow handles cases that would be hard to code. For testing, he suggests layered checks: linters for skill format, LLM judges that can run commands in a sandbox for end-to-end behaviour, and repeated runs with error budgets because results are non-deterministic. For distribution he covers registries, dependency conflicts between context packages, scanning for security, and an AI bill of materials recording how a context was built. For observation he uses agent logs, PR feedback and production traces to find missing context and turn failures into new tests. He also warns that sandboxes do not stop context files from carrying prompt injection, so he proposes a separate filter in front of context loading. The Q&A adds an idea: run the same spec-generation several times and treat agreement across runs as a quality signal. Most of the talk is conceptual, with few measured numbers.

## Key ideas
- **Context is becoming the new code, and code is turning back into context.** — A skill with plain-language steps (detect the package manager, then the ecosystem, then work with the user) solved onboarding problems that would have needed a lot of hand-coded branches. ([1:08](https://youtu.be/bSG9wUYaHWU?t=68))
- **Use a DevOps-style loop for context: generate, test, distribute, observe, adapt.** — He maps the SDLC onto a context development lifecycle, drawn as an infinity loop. Each stage feeds the next, and failures send the context back for regeneration. ([2:31](https://youtu.be/bSG9wUYaHWU?t=151))
- **Test context the way you test code, with several layers.** — Start with a linter that checks skill format (for example, description length). Then use an LLM judge against a rule, such as whether an endpoint has the required prefix. Finally, give the judge tools so it can run the endpoint in a sandbox. The last layer is an end-to-end test. ([6:24](https://youtu.be/bSG9wUYaHWU?t=384))
- **Evals on agents are non-deterministic, so use error budgets rather than single pass or fail runs.** — Run a scenario several times (he uses five as the example) and count the success rate. Give each test set an allowed failure budget. Exact-match testing does not work for context. ([12:46](https://youtu.be/bSG9wUYaHWU?t=766))
- **Distribution brings dependency, registry and security problems.** — Context packages can conflict, much like library dependencies, and some teams pin context to library versions. Scanners check packages for credential leaks and third-party exposure. An AI bill of materials records which model and process built a context. ([16:16](https://youtu.be/bSG9wUYaHWU?t=976))
- **Observation closes the loop: agent logs, PR feedback and production traces become new context and tests.** — Repeated missing-context signals across a team should become shared context. Reviewer comments on agent PRs are feedback on the context that produced them. Production failures can become test cases. ([17:44](https://youtu.be/bSG9wUYaHWU?t=1064))
- **Sandboxes do not protect against malicious context loaded into the agent.** — Agent instruction and skill files load before any sandbox restriction applies. He proposes a separate context filter, similar to a web application firewall, that scans for prompt-injection patterns before loading. ([20:54](https://youtu.be/bSG9wUYaHWU?t=1254))
- **Scale through a library-authoring loop and an organisational loop.** — One loop covers a person writing their own context. A second loop covers a team reusing a library, with feedback from its users. A fix in one team can flow to others, creating a flywheel. ([22:26](https://youtu.be/bSG9wUYaHWU?t=1346))
- **Consistency across parallel runs can be a quality signal for a spec.** — In Q&A he describes running the same rough plan through several parallel runs. If the resulting crisp definitions match, the spec is probably good. If they diverge, the input is too vague. He says he is testing this himself. ([25:11](https://youtu.be/bSG9wUYaHWU?t=1511))

## Techniques
- **Layered context tests (lint, judge, end-to-end)** — Lint skill and context files against their format spec. Use an LLM judge with a rubric for convention rules, such as required URL prefixes. Give the judge a sandboxed tool, such as curl, so it can run the endpoint and check actual behaviour. *When:* When a repo has house rules for agent-written code, or when skills and CLAUDE.md/AGENTS.md change and you need to know the effect.
- **Repeated runs with error budgets** — Run each scenario several times and record the pass rate. Set an allowed failure budget for each test set, with stricter limits for the tests that matter most. *When:* When you evaluate context changes, because single runs of a non-deterministic agent give misleading results.
- **Commit-scoped context A/B scenarios** — For a given commit, run one scenario with and without a specific piece of context, then compare the outcomes to see if the context changed anything. *When:* When you want to tell whether a change to CLAUDE.md or a skill actually helps.
- **Turning feedback into context fixes** — Look at agent logs, PR review comments and production failures. When the same gap shows up repeatedly, write it into shared context and add a test case so it does not recur. *When:* When a team uses shared agent context and wants it to improve from real use.
- **Context filter before loading** — Scan agent instruction and skill files for prompt-injection patterns and suspicious content before the agent loads them. Treat it as a gate that sits outside the sandbox. *When:* When installing third-party skills or context packages, or when context can come from untrusted sources.
- **Packaging context with provenance and scanning** — Publish context as versioned packages with dependency pins to library versions. Scan packages before publishing. Record provenance, including the model and process that built them, in an AI bill of materials. *When:* When context is shared through an internal or public registry.
- **Parallel generation as a spec-quality check** — Give the same rough spec to several parallel runs and compare the crisp definitions they produce. High agreement suggests a good spec. Low agreement means the input needs more detail. *When:* Before handing a plan or spec downstream, such as a planning step that feeds implementation agents.

## Numbers
- Example eval design: run the same test about five times and count how many pass, instead of trusting a single run. The number is an illustrative example, not a measured result. ([12:46](https://youtu.be/bSG9wUYaHWU?t=766))
- Speaker's own estimate: 99.9% of public skills are not up to a quality standard. He says this as hyperbole and gives no measurement. ([14:17](https://youtu.be/bSG9wUYaHWU?t=857))

## Hot takes
- Almost all public skills are low quality, and he expects that to improve slowly.
- Code is turning back into context, so reusable workflow instructions replace much hand-written code.
- LLMs are the engine and context is the fuel. Improving context is the lever a developer actually controls.
- Teams often change two lines of CLAUDE.md and ship them without testing, which he calls YOLO.
- Sandboxing alone does not stop context-borne attacks, because agent instruction and skill files load before the sandbox restrictions apply.

## Tools mentioned
Claude Code, AGENTS.md, CLAUDE.md, SKILL.md, MCP, Tessl, GitHub, GitLab, Slack, Snyk, Gemini, GitHub Copilot

## Relevance to our work
- **agentos** (2/3): The observe loop (agent logs, PR feedback and production failures feeding back into context and tests) addresses the open question of what signal makes a skill worth keeping in SkillForge. → *Log which skills and context files each agent run loaded, and use failed runs as the success signal when scoring skill-worthiness in SkillForge.*
- **prosharness** (2/3): ProsHarness runs a plan step before the Codex critique. The parallel-generation consistency check gives a cheap signal on plan quality before that step. → *Generate the plan several times in parallel and measure how much the plans agree. Send low-agreement plans back for clarification before they reach the critique step.*

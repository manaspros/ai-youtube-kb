# Github's Biggest Release In Years. Stacked PRs.

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `3Z1xcfF2xlY` · [watch](https://youtu.be/3Z1xcfF2xlY) · **date:** 2026-09-02 · **length:** 5:17 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** GitHub, Better Stack
- **topics:** pr-code-review, dev-tools, coding-agents · **tags:** stacked-prs, github, gh-cli, git, pull-requests, code-review, agent-workflows

> Better Stack walks through GitHub's stacked PRs: splitting a large change into a chain of dependent PRs, managing the chain with the gh CLI, and merging the whole stack at once.

## Summary
The video explains stacked PRs as a chain of small, dependent pull requests where the bottom PR targets main and each later PR targets the one below it. The presenter stresses that plain git has no notion of a stack, so the benefit comes from GitHub's own support for stacks in its UI and CLI. A short demo uses the gh CLI to create a three-branch stack (setup database, API, frontend), with several commits per branch, then pushes and opens all three PRs in one command. The stack is then reviewed and merged from the top PR with a "merge stack" action. The presenter also says the same stack can be built by hand by linking PRs base-to-base, and suggests the workflow suits long-running AI agents that can produce a chain of linked PRs. The title ("biggest release in years") is hype; the substance is a practical, short feature walkthrough with no sponsored segment beyond a subscribe call-to-action.

## Key ideas
- **A stack is a chain of dependent PRs: the bottom PR targets the trunk (main) and each subsequent PR targets the one below it.** — Foundational changes such as shared types or DB schemas go in lower PRs; code that depends on them, such as API routes and UI components, goes higher up. Each PR can be reviewed and merged independently. ([0:00](https://youtu.be/3Z1xcfF2xlY?t=0))
- **Plain git has no concept of a stack; the stack only means something inside GitHub.** — Daisy-chaining PRs by hand already works in git. The advantage comes from GitHub recognising the chain as a stack in its UI, list pages, workflows and merge tooling. ([0:58](https://youtu.be/3Z1xcfF2xlY?t=58))
- **The gh CLI builds and submits a whole stack from local branches.** — gh stack init creates the base branch, gh stack add creates each next branch, normal git add and commit work inside each branch, and gh stack submit pushes all branches and opens the PRs together through a small interactive UI for titles and descriptions. ([1:56](https://youtu.be/3Z1xcfF2xlY?t=116))
- **Stacks are merged from the top PR in one action.** — On the top PR, Merge stack merges every PR in the chain into main together, after the stack has been reviewed as a whole. The stack icon and stack references appear across the GitHub UI. ([3:14](https://youtu.be/3Z1xcfF2xlY?t=194))
- **Stacks can be created without the gh CLI by linking PRs manually from main to PR1 to PR2.** — The presenter says GitHub still detects these as a stack, so the CLI is a convenience rather than a requirement. Switching to unrelated branches mid-stack is also fine. ([3:14](https://youtu.be/3Z1xcfF2xlY?t=194))
- **The presenter sees stacks as a fit for AI agents running long loops.** — Agents working for hours could produce a linked chain of PRs rather than one huge PR or many unrelated PRs. This is the presenter's own suggestion and is not tested in the video. ([4:37](https://youtu.be/3Z1xcfF2xlY?t=277))

## Techniques
- **Stacked PR workflow with gh stack** — 1) gh stack init setup-database (base branch, targets main). 2) Make changes, then standard git add and git commit. 3) gh stack add <next-branch> (e.g. api endpoints), change, commit; repeat (multiple commits per branch are fine). 4) gh stack add setup-frontend, change, commit. 5) gh stack submit: the mini CLI UI asks for a title and description per PR (or accept defaults); all branches are pushed and all PRs are created in one command. 6) Review the stack in GitHub and use Merge stack on the top PR. *When:* A large change can be split into layers where lower layers (schema, types, shared code) are needed by higher ones (API, UI), and you want each layer reviewed and merged as a unit.
- **Manual stacking without the CLI** — Open PR1 from branch 1 targeting main, then open PR2 from branch 2 targeting branch 1, and PR3 targeting branch 2. GitHub then shows the chain as a stack (per the presenter). Keep the base-of-each-PR chain intact when rebasing or merging. *When:* You cannot install gh or the stack extension, or you want to keep the workflow fully inside git and the GitHub web UI.
- **Layer the stack by dependency** — Put foundational changes (shared types, database schema or migrations) in the lowest PRs, then the code that uses them (API routes) in the middle, and UI components at the top. Each PR should build on the one below it. *When:* Planning how to split any large feature change into reviewable PRs, human or agent-authored.

## Numbers
- Demo stack has 3 PRs (setup database, API, frontend), each on its own branch, submitted in one gh stack submit command. ([1:56](https://youtu.be/3Z1xcfF2xlY?t=116))
- Multiple commits per branch are shown in the demo (two commits for the API branch). ([1:56](https://youtu.be/3Z1xcfF2xlY?t=116))
- Video runtime is 5:17 and the walkthrough itself covers about 3 minutes. ([0:00](https://youtu.be/3Z1xcfF2xlY?t=0))

## Hot takes
- The title calls this GitHub's 'biggest release in years', which the video does not support; it is a short walkthrough of an existing feature set.
- The presenter says the positive online response is 'overwhelming' without citing evidence.
- The claim that AI agents will benefit from stacked PRs is an untested suggestion, not demonstrated in the video.
- The video is honest that git itself has no stack concept; the value is in GitHub's tooling.

## Tools mentioned
GitHub (stacked pull requests, Merge stack, stack UI), GitHub CLI (gh), with gh stack init / add / submit subcommands, git

## Relevance to our work
- **general** (2/3): Directly applicable to any multi-part code change PR workflow, not tied to our stack. → *Try gh stack on the next large change: install gh, run gh stack init for the first layer, and check how Merge stack behaves for a 3-PR chain.*
- **prosharness** (1/3): ProsHarness runs long Claude Code sessions that could produce dependent changes; the video suggests agents can emit stacked PRs. → *Evaluate whether ProsHarness checkpointed runs could open PRs as a stack via gh stack instead of one large PR.*
- **agentos** (1/3): AgentOS changes often cross layers (storage, proxy, pillars), where lower-layer changes must land first. → *Use the bottom-to-top layering rule for multi-pillar AgentOS changes, starting with storage or schema PRs.*

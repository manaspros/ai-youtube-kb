# Everyone Gets A Software Company — Benjamin Guo, Zo Computer

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Qr15lGAGKpo` · [watch](https://youtu.be/Qr15lGAGKpo) · **date:** 2026-09-18 · **length:** 15:09 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Benjamin Guo · **orgs:** Zo Computer, Anthropic, Venmo, Stripe, Substack
- **topics:** product-ux, agent-architecture, sandboxing-execution · **tags:** personal-cloud, self-hosting, personal-agents, agent-ownership, vendor-lock-in, techno-feudalism, zo-computer, openclaw, hermes, saas-replacement

> Zo Computer co-founder Ben Guo pitches a personal cloud server with built-in AI as a way out of SaaS silos and vendor-owned cloud agents. Mostly a product pitch, with a few ownership arguments worth noting.

## Summary
Ben Guo, co-founder of Zo Computer, argues that most people are locked into fragmented SaaS tools and that the next layer of cloud agents will be owned by vendors rather than users. He defines Zo as a personal cloud: one server where a user keeps files, AI, websites, APIs and automations, reachable from phone or laptop. He shows non-technical users (a private chef, a freediving instructor) replacing SaaS subscriptions with Zo-hosted sites, bookings and notes. He frames company-level cloud agents such as Claude Tag as "intelligence feudalism," where improvements accrue to the model vendor. He ends by proposing a beta platform where individuals or companies publish agents they own, and end-user usage improves them. Most claims are self-reported anecdotes from a product owner, with no benchmarks or independent data.

## Key ideas
- **SaaS lock-in is a structural problem** — The speaker frames users as renters: they pay SaaS vendors, who pay cloud providers, who pay chip makers. Vendors monetise attention and data, so users are fragmented across tools. He calls this techno-feudalism. ([2:54](https://youtu.be/Qr15lGAGKpo?t=174))
- **A personal cloud is one server you own** — Zo is pitched as a personal server with AI built in. The user's files, AI agent, websites, APIs and notes sit in one place, reached from phone, laptop or a local machine, instead of many SaaS silos. ([3:52](https://youtu.be/Qr15lGAGKpo?t=232))
- **Ordinary users should not have to think about deployment** — He compares it to early FTP-to-production web hosting. His argument is that hosting and deployment should be hidden from non-technical people, while developers still get root access and SSH. ([6:17](https://youtu.be/Qr15lGAGKpo?t=377))
- **Whose cloud the agent runs in matters** — He argues company-level cloud agents (he names Claude Tag, Town and Victor) mean that improving the setup mostly improves the vendor. Ownership of intelligence should sit with the company or person. ([12:35](https://youtu.be/Qr15lGAGKpo?t=755))
- **Proposed model: publish agents you own that self-improve from end-user use** — The stated direction is that any individual or company can publish an agent they own, with end users, where usage improves the published agent. Zo has a beta of this publishing platform. No details of how improvement works were given. ([14:01](https://youtu.be/Qr15lGAGKpo?t=841))
- **Bring your own models and subscriptions to a self-hosted box** — Users can bring their own API keys or Codex, Gemini or similar subscriptions. They can host OpenClaw or Hermes on the same server and control it via API or MCP. The speaker presents this as the pitch for developers in the audience. ([9:02](https://youtu.be/Qr15lGAGKpo?t=542))

## Techniques
- **Single personal server as the agent home** — Run the agent, file storage, websites, APIs and scheduled jobs on one always-on Linux VM with root and SSH access. Expose control through an API or MCP server so other devices can drive it. *When:* When you want one place for personal data and agent work, or your own always-on box for a personal agent instead of several SaaS tools.
- **Scheduled agent automations** — Define tasks that run an AI agent on a schedule (e.g. recurring bookkeeping or reminders) inside the same server, with built-in integrations and a large skill library. *When:* For recurring personal or small-business admin where a human would otherwise re-prompt the agent each time.
- **Agent as a gatekeeper for inbound bookings** — Put a self-hosted booking page in front of your calendar, and have the agent review who is requesting time before it is confirmed. He describes his own Calendly replacement this way. *When:* When you get many inbound requests and want to screen them before they reach your calendar.
- **Chat-driven site editing and hosting** — Describe changes to a personal website in chat, and the agent edits and deploys it on the same server, including custom domains and file hosting. *When:* For non-technical users who want a website or small service without a separate deploy pipeline.

## Numbers
- Zo has been out for about a year, per the speaker ([3:52](https://youtu.be/Qr15lGAGKpo?t=232))
- A freediving instructor who was an early user is said to be on track to make $100,000 on Zo (self-reported, unverified) ([6:17](https://youtu.be/Qr15lGAGKpo?t=377))
- Promotional offer of $100 in AI credits for signing up (promo, not a benchmark) ([9:02](https://youtu.be/Qr15lGAGKpo?t=542))

## Hot takes
- Cloud-hosted company agents mean the improvements go to the model vendor, which he calls intelligence feudalism.
- Most people should not think about deployment at all, and hosting should be invisible to them.
- A single personal server can replace many SaaS subscriptions for ordinary people.
- Future agents will mostly run in the cloud, so the real question is whose cloud they run in.

## Tools mentioned
Zo Computer, Claude Code, Codex, Gemini, Claude Tag, OpenClaw, Hermes, Calendly, Squarespace

## Relevance to our work
- **agentos** (1/3): AgentOS is also aimed at self-hosted agent infrastructure, and this talk makes the ownership-of-the-cloud argument for personal agents. Little that directly changes the build. → *Read the Zo beta publishing model for ideas on how an end-user-improves-the-agent loop could be framed in AgentOS. No code change needed yet.*
- **prosharness** (1/3): ProsHarness runs long Claude Code work with checkpoints and loops. The talk's always-on server with scheduled automations is a similar pattern, though it is a product, not a technique. → *Consider whether ProsHarness loops should be able to run on an always-on remote VM with SSH access, as Zo describes. Not urgent.*

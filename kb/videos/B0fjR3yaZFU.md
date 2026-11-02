# How do you diffuse AI into the real world? — Varun Shenoy, Long Lake

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `B0fjR3yaZFU` · [watch](https://youtu.be/B0fjR3yaZFU) · **date:** 2026-09-18 · **length:** 17:46 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Varun Shenoy · **orgs:** Long Lake, General Catalyst, Alpha Wave, American Express Global Business Travel
- **topics:** enterprise-adoption, product-ux, evals, agent-architecture · **tags:** ai-diffusion, autonomy-ladder, copilot-to-coworker, services-businesses, trace-to-eval, implicit-feedback, post-training-on-enterprise-data, continual-learning, co-design, sandboxed-async-agents, jagged-frontier

> Long Lake co-founder on why AI adoption in real services businesses lags: climb an autonomy ladder, turn real work traces into evals, and co-design with users on-site.

## Summary
Varun Shenoy, a co-founder of Long Lake, argues that AI capability is ahead of real-world deployment and that diffusion, like electricity or the Ford factory, takes years of changing equipment, processes and people. Long Lake acquires and runs services businesses (about 35 so far, in HR, property management, architecture) rather than selling software, so it owns the outcomes when the AI fails. He proposes a ladder of agent autonomy from copilot to synchronous agent to asynchronous agent to long-running agent to coworker, and says teams must earn each rung. He contrasts coding, where sandboxed async agents that open PRs are largely solved and engineers already parallelize jobs, with services work, which is serial and lacks that tooling. He describes a flywheel where agent traces (tool calls, failures, human edits) yield ground-truth evals, weekly hill-climbing benchmarks become regression tests, and the same data can be used for post-training on out-of-distribution business tasks. He closes by arguing that continual learning and enablement form one loop, and that adoption requires in-person co-design with the people doing the work. Some of the content is company pitch, but the operating lessons are concrete.

## Key ideas
- **AI diffusion is the bottleneck, not model capability** — He compares AI to electricity and the Ford electrified assembly line: adoption needed new equipment, retraining and process change, which took about a generation. Capability demos do not mean the work has changed. ([1:12](https://youtu.be/B0fjR3yaZFU?t=72))
- **Operate the business instead of selling software into it** — Long Lake buys and runs services firms, so when the AI fails it is their problem, not a vendor's. That ownership is what lets them learn the real work. ([3:18](https://youtu.be/B0fjR3yaZFU?t=198))
- **Earn autonomy one rung at a time** — The ladder runs copilot, synchronous agent (minutes of tool use with a human in the loop), asynchronous agent (background work, external triggers), long-running agent (hours to months), then coworker. Jumping straight to a proactive coworker fails because models are not ready for some tasks and customers need to trust the rungs. ([5:43](https://youtu.be/B0fjR3yaZFU?t=343))
- **Coding solved the async pattern, services has not** — Wrap a coding agent in a sandbox, let it build and test, and return a PR; engineers already run many jobs in parallel. Services work is serial, so the open question is how to fork and parallelize knowledge work, possibly by representing it as code. ([7:09](https://youtu.be/B0fjR3yaZFU?t=429))
- **Real work traces become ground-truth evals** — Tool calls, hiccups and paper cuts are logged. Outcomes like 'was the roof repaired' or 'did the books close' give ground truth. Hill-climbing benchmarks become regression tests each week. ([9:59](https://youtu.be/B0fjR3yaZFU?t=599))
- **Use the human edit as an implicit reward signal** — The diff between what the AI drafted and what the employee finally submitted is rich feedback. Combined with explicit thumbs up or down, it gives evals that score themselves. ([11:59](https://youtu.be/B0fjR3yaZFU?t=719))
- **Real work is hills and ravines, not a clean slope** — Most enterprise tasks fail through many small paper cuts. He argues that the exceptions are the job, and that demos show the easy path. ([13:19](https://youtu.be/B0fjR3yaZFU?t=799))
- **Continual learning and enablement are one loop** — Usage drives data, data drives a better agent, and a better agent drives more usage. Teams usually split these two, but he says they should be owned together. The initial usage problem has to be solved first. ([14:50](https://youtu.be/B0fjR3yaZFU?t=890))
- **Co-design with users in person** — Embed the product inside Excel, ERP, Outlook or CAD where people already work. Run lunch-and-learns, attend customer events and do one-on-one training. He says you cannot co-design with a services business over Zoom or a support ticket. ([16:18](https://youtu.be/B0fjR3yaZFU?t=978))

## Techniques
- **Autonomy ladder rollout** — Stage agent autonomy as copilot, then synchronous, then asynchronous with external triggers, then long-running, then coworker. Advance a rung only when the workflow has earned it with the customer. *When:* Deploying agents into an organization where the work is not yet well understood or trusted.
- **Sandboxed async coding agent with PR output** — Run the same coding agent inside a sandbox where it can build and test, then return the result as a PR. Launch many jobs in parallel and accept that they finish out of order. *When:* Coding tasks where verification is automatic and parallel jobs are cheap to review.
- **Traces to ground-truth evals** — Record every tool call and failure from real work. Define a task-level outcome check (such as the roof repaired or the books closed) as ground truth, then turn the scored cases into a weekly regression suite. *When:* Agent work where a real-world outcome can be verified, and the team needs to measure improvement over time.
- **Diff-based implicit feedback** — Compare the AI's draft output to the version the human actually submitted and treat the difference as a training or eval signal, alongside thumbs up or down. *When:* Human-in-the-loop workflows where the human edits the AI output before it is used.
- **Post-training on enterprise data** — Post-train internal models on the operational data a business produces, so they learn tasks that are absent from public web data. *When:* Owned or deeply embedded business data that frontier models have not seen.
- **Layered customization** — Tailor agents per company, per user and per client, since each uses its own process and standards. *When:* Services work where many clients and staff do the same task in different ways.
- **Co-design embedded in existing tools** — Put the agent inside the software people already use (Excel, ERP, Outlook, CAD) and iterate with them on site, watching how they work. *When:* Enterprise rollouts where adoption is the main obstacle.

## Numbers
- Raised over $3 billion in about two years since founding (investors include Elad Gil, General Catalyst, Alpha Wave) ([2:15](https://youtu.be/B0fjR3yaZFU?t=135))
- Acquired 35 businesses across HR, property management, architecture and other services ([3:18](https://youtu.be/B0fjR3yaZFU?t=198))
- Roughly 40-person team, with more than half in technology ([3:18](https://youtu.be/B0fjR3yaZFU?t=198))
- Announced a $6.3 billion take-private of American Express Global Business Travel ([3:18](https://youtu.be/B0fjR3yaZFU?t=198))
- Synchronous coding agents are typically run for about 1 to 5 minutes of autonomous work ([5:43](https://youtu.be/B0fjR3yaZFU?t=343))
- Engineers commonly launch around 10 parallel jobs and accept out-of-order completion ([7:09](https://youtu.be/B0fjR3yaZFU?t=429))
- Speaker reports about two and a half years of lessons from deploying AI into owned companies ([4:41](https://youtu.be/B0fjR3yaZFU?t=281))

## Hot takes
- AI diffusion may be the single most important problem for the next 20 years.
- Owning the operating business, not selling to it, is the only way to learn what works.
- You have to earn the right to do more: jumping straight to a proactive AI coworker is the wrong start.
- To make AI diffusion work you have to touch some grass; remote co-design does not work for services businesses.
- Representing service knowledge work as code so that coding agents can run it is a promising path (an idea he poses, not a shipped result).

## Tools mentioned
Claude Code, Codex, Claude Cowork, MCP

## Relevance to our work
- **agentos** (2/3): SkillForge's open question is the success signal for mined skills. The talk's diff between AI draft and human-submitted output is a concrete candidate signal, and the traces-to-evals loop is close to MemoryMesh and RAGAS evals. → *Prototype logging the AI draft and final submitted version for each agent task in AgentOS telemetry, then test whether the edit distance works as a success signal for SkillForge skill-worthiness scoring.*
- **prosharness** (1/3): The sync, async, long-running ladder maps onto ProsHarness checkpoint/resume and loop/schedule features. The talk gives a vocabulary for autonomy levels but no concrete mechanism. → *Consider tagging each ProsHarness run with its autonomy rung (sync, async, long-running) so checkpoint and approval policy can differ by rung.*

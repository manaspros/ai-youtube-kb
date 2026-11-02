# This Makes AI Agents WAY More Powerful (just-bash)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `EoyLzyJUcfI` · [watch](https://youtu.be/EoyLzyJUcfI) · **date:** 2026-03-02 · **length:** 6:31 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** ?
- **topics:** sandboxing-execution, token-cost-efficiency, dev-tools · **tags:** just-bash, virtual-filesystem, in-memory-fs, agent-bash-tool, ai-sdk, bash-tool, token-reduction, long-context-alternative, jq, sqlite, curl-whitelist, json-analysis

> Short walkthrough of just-bash, a TypeScript simulated bash with an in-memory virtual filesystem for agents, and how wiring it into an AI SDK chat cut input tokens from 133k to 6k on one JSON query.

## Summary
The presenter introduces just-bash, an npm package that simulates a bash shell in TypeScript over an in-memory virtual filesystem, so agents get shell-like file work without a real shell or containers. He shows that commands are translated into JavaScript functions, that the filesystem is not touched on disk (an optional real filesystem can be attached), and that the command set covers common Unix tools plus jq, Python 3, SQLite and whitelisted curl, along with pipes and redirections. The demo uses a large JSON file: pasting it into the prompt cost about 133,000 input tokens, while exposing the package's bash tool to the AI SDK (with files mounted under /workspace) let the agent run jq, recover from an error with head, and answer with about 6,000 input tokens. A counting question (records between 1000 and 2500 with metadata.active true) is then answered by running a command instead of guessing from context. The video is a single-file, single-model demo with no accuracy measurement, and the "secure sandbox" claim is asserted rather than tested.

## Key ideas
- **Give agents bash-style file and data operations through a TypeScript simulation instead of a real shell, avoiding servers, containers and extra infrastructure.** — just-bash is presented as a simulated bash environment with an in-memory virtual filesystem, meant for agents that need a sandboxed bash. The presenter frames it as a cheap, no-infra alternative to running a real shell. ([0:00](https://youtu.be/EoyLzyJUcfI?t=0))
- **It is a simulation, not a real shell: each command is converted into a JavaScript function and run in-process.** — A file written with echo into greeting.txt exists only in the in-memory filesystem. The result object carries stdout, stderr and an exit code. A real filesystem can optionally be attached. ([0:50](https://youtu.be/EoyLzyJUcfI?t=50))
- **Command coverage is broad: common Unix tools, data tools, network access under a whitelist, and shell features.** — Listed commands include cat, cp, grep, base64, jq, Python 3, SQLite and curl. Curl is restricted by an allowlist. Pipes, redirections and command chaining are supported. ([2:15](https://youtu.be/EoyLzyJUcfI?t=135))
- **Pasting a large file into the prompt is the costly baseline, and it degrades on harder questions.** — With the whole JSON file in the prompt, the demo used about 133,000 tokens. The presenter says it works for simple lookups but is likely to fall apart on analysis over fields or ranges. ([3:19](https://youtu.be/EoyLzyJUcfI?t=199))
- **Mount the data into a virtual workspace and let the agent discover the format with bash.** — Files are passed to the bash tool, placed under a simulated /workspace directory. The agent ran jq, hit an error, ran head to inspect the file, corrected its query, and answered using about 6,000 input tokens. ([4:26](https://youtu.be/EoyLzyJUcfI?t=266))
- **Counting and filtering questions are better answered by running a command than by reasoning over context.** — For records with ID ranges and a boolean metadata field, the agent runs a bash command for an exact count. The presenter argues that the context-only approach would either bloat the prompt or guess. ([5:31](https://youtu.be/EoyLzyJUcfI?t=331))

## Techniques
- **Virtual bash tool for an agent** — Create a simulated bash environment from the just-bash package and call its exec method with a shell command string. Read stdout, stderr and the exit code from the returned object. Use the same environment across calls so files persist within the session. The presenter's shorthand is env.exec. *When:* When an agent needs file or text processing on data but you do not want to provision a shell, container or VM.
- **Mount files into a virtual workspace** — In the chat API endpoint, create the bash tool from the bash-tool package (built on just-bash). Pass the data files in a file map and set the destination to /workspace. Pass the bash tool into the AI SDK stream so the model can call it. *When:* When the input is a large file (JSON records, logs, CSV) that would be wasteful to paste into every prompt.
- **Include the package's agent instructions** — The bash-tool package ships instruction text in node_modules that explains how to use the bash tool. The presenter passes these to the agent as part of its system instructions so it knows the available commands. *When:* When wiring any tool-calling agent to a bash-like tool, so it does not waste turns on guessing the interface.
- **Restrict outbound network with a curl allowlist** — Configure curl with a whitelist of permitted hosts, as the presenter describes. The video does not show the config keys. *When:* When the agent needs HTTP access but the sandbox should not reach arbitrary hosts.

## Numbers
- Full-file JSON pasted into the prompt used about 133,000 tokens and answered a simple record lookup correctly, but is expected to fail on deeper analysis. ([3:19](https://youtu.be/EoyLzyJUcfI?t=199))
- The same lookup via the just-bash bash tool used about 6,000 input tokens, including a failed jq attempt and a head call to inspect the file. The presenter says it took a little longer. ([4:26](https://youtu.be/EoyLzyJUcfI?t=266))
- Total runtime is 6:31. The benchmark is a single JSON file, a single question and a single model, with no accuracy or cost measurement across runs. ([0:00](https://youtu.be/EoyLzyJUcfI?t=0))

## Hot takes
- The title says it makes agents 'WAY more powerful', but the demo only shows token reduction on one lookup and one counting query. It does not test capability breadth.
- The baseline is naive full-file prompting, not RAG or a real sandbox, so the comparison says little about the best alternative.
- Calling it a 'secure sandboxed' environment is asserted, not tested. A simulation that runs in-process is not an OS-level isolation boundary, and the video gives no escape or isolation test.
- Accuracy of the bash-based answer is never measured against ground truth, only shown on the two prompts.

## Tools mentioned
just-bash (TypeScript simulated bash with in-memory virtual filesystem), bash-tool package (AI SDK bash tool built on just-bash), AI SDK, GPT-5.2 (model used for the chat demo, as named by the presenter), jq, Python 3 (inside just-bash), SQLite (inside just-bash), curl (inside just-bash, host whitelist), head

## Relevance to our work
- **agentos** (2/3): Crucible is the opt-in sandboxed code-execution layer, and a cheap in-process bash for read-only data questions could be a lighter first tier. The token reduction also fits the cheap-model and context-cost thesis. → *Prototype a read-only data-query tool in Crucible backed by just-bash, with a file mount from a MemoryMesh bucket. Measure input tokens against a full-context baseline on 20 real queries, and test whether its curl allowlist and filesystem isolation hold against escape attempts before trusting it as a sandbox.*

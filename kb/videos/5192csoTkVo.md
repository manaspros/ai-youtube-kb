# remobi.app: Don't change your terminal workflow for mobile

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `5192csoTkVo` · [watch](https://youtu.be/5192csoTkVo) · **date:** 2026-07-18 · **length:** 9:21 · **format:** demo · **quality:** 2/5 · **depth:** intro
- **speakers:** Connor Adams · **orgs:** ?
- **topics:** coding-agents, dev-tools, product-ux · **tags:** remobi, tmux, phone-access, mobile, progressive-web-app, tailscale, remote-dev, claude-code, lazygit, touch-ui, skills

> Connor Adams demos Remobi, an open-source progressive web app that gives phone access to tmux sessions running Claude Code and other coding agents, reached over a private network such as Tailscale.

## Summary
The speaker, Connor Adams, presents Remobi, an open-source progressive web app for checking and steering coding agents from a phone without changing his terminal workflow. He explains the pull to check on agents while away from the desk, and reviews existing options such as Happy (Claude Code only, with a relay server he does not fully trust), the built-in Claude Code handoff (manual), and generic SSH terminal apps (key setup and touch controls are painful). His own setup is a remote dev machine running tmux with several coding agents in panes, custom key commands, lazygit and a diff-review tool called critique, plus a habit of killing stray processes such as a leftover agent-browser holding a port. Remobi runs on that machine, serves the tmux session to the phone with touch gestures (double-tap to zoom a pane, scroll panes, buttons for things like switching Claude Code into plan mode), and ships an installable skill that sets up tmux and maps key bindings to touch controls. Access is over the internet via Tailscale in his case, with Cloudflare Tunnels or ngrok as alternatives; he is emphatic that exposing it directly to the public internet is a serious security mistake. The talk is a short tool demo and invitation to try it, with no benchmarks or formal evaluation.

## Key ideas
- **Checking coding agents from a phone is a real pull, but existing tools each have gaps.** — Happy works only with Claude Code and relies on a relay server the speaker does not fully trust; the built-in handoff needs a manual step and only covers one tool; generic SSH terminal apps make key setup and touch controls hard. ([0:00](https://youtu.be/5192csoTkVo?t=0))
- **Use tmux as the session host so agents survive and can be reattached from any device.** — The speaker runs several coding agents at once in tmux panes and windows on a remote dev machine, with custom key commands and a status bar. He says he vibe-coded the setup and did not learn tmux by hand. ([2:37](https://youtu.be/5192csoTkVo?t=157))
- **Keep review tools inside the same terminal session.** — After an agent finishes work, he opens lazygit or the critique diff viewer in a tmux window to review changes before committing. He also kills stray processes, such as a background agent-browser holding a dev-server port. ([4:03](https://youtu.be/5192csoTkVo?t=243))
- **A phone client can map touch gestures onto a terminal multiplexer.** — The PWA works on iOS and Android. Double-tap zooms into one pane, panes scroll by touch, and buttons send commands such as Shift+Tab for plan mode or open git and critique. The speaker concedes the UI is minimally functional and not polished. ([5:31](https://youtu.be/5192csoTkVo?t=331))
- **Setup is handled by an installable skill rather than a copied shell script.** — Remobi is installed as an npm package plus a skill. The skill walks the user through installing tmux if needed, or turns an existing tmux config into touch key bindings. The speaker presents this as a safer alternative to pasting random install scripts. ([6:55](https://youtu.be/5192csoTkVo?t=415))
- **Network exposure is the main security decision, and the public internet is off-limits.** — He uses Tailscale, names Cloudflare Tunnels and ngrok as alternatives, and warns that putting the server on the public internet exposes the whole machine. Security is raised as a concern in the Q&A but not analysed in depth. ([8:41](https://youtu.be/5192csoTkVo?t=521))

## Techniques
- **tmux as the agent session host** — Run each long coding-agent session in its own tmux pane or window on a remote machine, with custom key commands for common actions. Sessions keep running when the client disconnects, and any client can reattach. *When:* When you run several coding agents in parallel or want long runs to survive laptop sleep or a device switch.
- **Private-network remote access to a dev box** — Expose the local phone-facing server only over a mesh VPN such as Tailscale, or over a tunnel with access control. Do not publish it on the open internet. *When:* When you need to check or steer agents from a phone away from the desk.
- **Gesture-mapped terminal UI** — A thin PWA reads the tmux session and maps double-tap to pane zoom, touch scrolling, and buttons for keys such as Shift+Tab. Users can add their own buttons from their tmux config. *When:* When you want terminal-level control on a phone without reconfiguring the tools themselves.
- **Diff review in a side window** — Open lazygit or a diff viewer such as critique in a tmux window beside the agent, and review the changes before committing. *When:* Right after an agent finishes a task and before accepting its changes.
- **Skill-driven environment setup** — Ship the setup as an installable agent skill that inspects the existing tmux config and proposes key bindings, rather than asking users to run an unknown shell script. *When:* When a tool needs per-user configuration that you want to make safe and repeatable.

## Numbers
- Demo ran four coding agents in parallel in tmux (the speaker asked whether 16 was realistic and settled on four). ([2:37](https://youtu.be/5192csoTkVo?t=157))
- Talk length is 9:21, and the speaker mentions GitHub stars as the only call to action. No benchmarks, latency figures or adoption numbers are given. ([6:55](https://youtu.be/5192csoTkVo?t=415))

## Hot takes
- If you put it on the public internet you've pwned your own computer.
- Vibe-coding a tmux setup means you don't need to understand tmux yourself.
- Pasting a random install shell script from the internet is what a skill-based setup is meant to avoid.

## Tools mentioned
Remobi, tmux, Tailscale, Cloudflare Tunnels, ngrok, Claude Code, Happy, lazygit, critique, agent-browser, npm, Conductor, Pi

## Relevance to our work
- **prosharness** (1/3): ProsHarness has phone-driven approvals; this talk shows a tmux-over-private-network approach where the speaker distrusts relay servers, which bears on how approvals should reach a phone. → *Compare the Tailscale/tmux access model with ProsHarness's phone approval path and check that approvals do not depend on a third-party relay.*

# Why MCP and ChatGPT Apps Use Double Iframes — Frédéric Barthelet, Alpic

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `c-2eEv2ou7Y` · [watch](https://youtu.be/c-2eEv2ou7Y) · **date:** 2026-06-18 · **length:** 20:11 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Frédéric Barthelet · **orgs:** Alpic, OpenAI, Anthropic
- **topics:** mcp-and-tools, security-guardrails, product-ux · **tags:** MCP apps, iframe, double iframe, CSP, content security policy, sandbox, origin isolation, ChatGPT apps, Apps SDK, SkyBridge, CSP inspector, srcdoc, frame-src

> Frédéric Barthelet (Alpic) explains why ChatGPT and Claude render third-party MCP app UI in nested "double" iframes: CSP and origin isolation rule out simpler options, and the nesting is the workable compromise.

## Summary
The talk explains how MCP apps (the views-based UI extension, first shipped as the OpenAI Apps SDK and later standardized as an MCP extension) render interactive HTML inside ChatGPT and Claude. A view is HTML tied to a tool call, advertised in the tool list, and injected with the tool result. The speaker walks through why the obvious approaches fail: srcdoc iframes inherit the host origin and CSP, so app scripts are blocked; relaxing CSP exposes the host's storage; sandboxing loses origin-bound APIs, and adding allow-same-origin reopens the escape. Serving each app from its own endpoint would require the host to whitelist every app domain in frame-src. The chosen design is a double iframe: a shared loader script is served from a separate domain, with per-app subdomains for origin isolation, and the app's HTML goes in via srcdoc inside it. Apps declare their external domains (connect-src, script/image/frame domains) in MCP metadata so the host can apply a matching CSP. The speaker shows SkyBridge, Alpic's open-source layer on the Apps SDK, and its CSP Inspector, which compares domains a view actually calls against the declared list. He notes that CSP-related rejections in the ChatGPT app store submission process are common.

## Key ideas
- **MCP app UI is rendered as views tied to tool calls** — A view is a small HTML/JS/CSS document. The server advertises it in the tool metadata, and the host renders it in an iframe when that tool is called, injecting the tool result. Views can be cached or fetched on demand. ([2:01](https://youtu.be/c-2eEv2ou7Y?t=121))
- **srcdoc is unsafe because it shares the host origin and CSP** — An srcdoc iframe inherits the parent's origin and CSP, so the host's nonce-based script-src blocks app JS. Relaxing CSP to allow it would let app code read the host's localStorage and cookies, which is unacceptable. ([6:21](https://youtu.be/c-2eEv2ou7Y?t=381))
- **Sandboxing alone does not solve the origin problem** — A sandboxed iframe gets an opaque (null) origin, so localStorage, IndexedDB and cookies stop working. Adding allow-same-origin to restore them brings back the escape path, so the sandbox is back to square one. ([7:42](https://youtu.be/c-2eEv2ou7Y?t=462))
- **Per-app endpoints would require an ever-growing frame-src whitelist** — Serving each app's view from its own domain would force the host to add every app domain to frame-src. The alternative is one controlled proxy domain that hosts the content, which means the host runs infrastructure for untrusted third-party code. ([10:15](https://youtu.be/c-2eEv2ou7Y?t=615))
- **Double iframe: a shared loader on a separate domain** — The host serves the same small loader script from a separate origin. The loader then injects the app HTML via srcdoc inside itself. The nested frame is isolated from the host, and per-app subdomains keep apps from sharing localStorage or cookies with each other. ([11:22](https://youtu.be/c-2eEv2ou7Y?t=682))
- **Apps must declare their external domains in metadata** — Each app lists the domains it connects to, loads scripts or images from, or frames. The host turns these into the CSP for the nested frame. Missing a domain means the app works in dev and breaks in production. ([14:00](https://youtu.be/c-2eEv2ou7Y?t=840))
- **Developer tooling can catch CSP gaps before submission** — ChatGPT's developer mode had removed CSP enforcement, so missing domains only showed up in production. The speaker's SkyBridge CSP Inspector compares domains a view actually calls with the declared list and flags the missing ones, which he says has been a common cause of app store rejections. ([15:18](https://youtu.be/c-2eEv2ou7Y?t=918))

## Techniques
- **Double-iframe isolation for untrusted UI** — Serve a fixed loader script from a separate domain, one subdomain per app for origin separation. The loader writes the untrusted HTML into an inner iframe with srcdoc. The host sets the CSP from the app's declared domains. *When:* Running third-party HTML or JS inside a host app where it must not reach the host's origin, storage or cookies, and the host cannot whitelist every app domain.
- **Declare-then-enforce external domains** — The app lists every external domain it uses (connect, script, image, frame) in MCP metadata. The host derives the nested frame's CSP from that list, so undeclared calls are blocked. *When:* Designing any tool or UI extension that loads remote resources and must pass a host's review or CSP.
- **CSP inspection in dev tools** — Compare the domains in metadata with the domains the view actually requests, and show the diff live as the code changes. *When:* Debugging why a UI works locally but fails in a host's production CSP.

## Hot takes
- Sandboxing an iframe with allow-same-origin reopens the escape path, so the sandbox attribute alone does not protect the host.
- Serving third-party UI from your own domain means you are responsible for code you have not reviewed.
- Running ChatGPT or Claude in developer mode with CSP removed hid missing-domain failures until production.

## Tools mentioned
MCP Apps extension, OpenAI Apps SDK, SkyBridge, HTML iframe (srcdoc, sandbox, allow-same-origin), Content Security Policy (frame-src, script-src, connect-src)

## Relevance to our work
- **general** (1/3): Relevant background for anyone exposing an MCP server with UI views; the double-iframe pattern and CSP domain declaration are useful reference. → *If we ever ship an MCP server with UI, read the MCP Apps extension spec's CSP metadata section before designing the view.*

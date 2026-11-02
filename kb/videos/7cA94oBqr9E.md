# Why CapnWeb is the LAST RPC Library You'll Need

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `7cA94oBqr9E` · [watch](https://youtu.be/7cA94oBqr9E) · **date:** 2025-11-02 · **length:** 4:36 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** Better Stack host (unnamed) · **orgs:** Cloudflare, Better Stack
- **topics:** dev-tools · **tags:** rpc, cap'n web, capnweb, cloudflare, typescript, websockets, http batching, promise pipelining, bun, react, trpc, wrangler

> A 4.5-minute walkthrough of Cap'n Web, Cloudflare's tiny object-capability RPC library, showing HTTP batch and WebSocket bidirectional setups in Bun/React and Node.

## Summary
Better Stack introduces Cap'n Web, a roughly 10 KB RPC library from Cloudflare that runs over HTTP, WebSockets or postMessage, supports request batching, promise pipelining and bidirectional calls. The video converts a simple Bun + React fetch-based app to HTTP batch RPC: a server class extends RpcTarget, is passed to newHttpBatchRpcResponse, and the client creates a stub with newHttpBatchRpcSession and the using keyword. It suggests a React context provider to share one stub across components. For bidirectional calling the speaker found HTTP unworkable and used WebSockets on Node with ws, because Cap'n Web's WebSocket support did not work out of the box on Bun at the time. The host calls the library highly experimental but says he will use it in side projects, and notes Cloudflare uses it for remote bindings in Wrangler. The video gives no benchmarks, so its performance claims are unverified.

## Key ideas
- **Cap'n Web is a tiny RPC library from Cloudflare that works over HTTP, WebSockets or postMessage, and supports batching and bidirectional calls.** — Made by the author of Cap'n Proto. It uses an object-capability model, so objects can only call each other when granted the capability. Roughly 10 KB. ([0:00](https://youtu.be/7cA94oBqr9E?t=0))
- **Promise pipelining removes round trips, and the library uses a fast JSON encoder.** — The speaker claims these give performance benefits over typical request/response RPC, but shows no measurements. ([0:54](https://youtu.be/7cA94oBqr9E?t=54))
- **The server exposes a class that extends RpcTarget, and each method on it becomes callable from the client.** — The API endpoint passes the incoming request and a new instance of the class to newHttpBatchRpcResponse. The client imports newHttpBatchRpcSession and the RpcStub type. ([1:30](https://youtu.be/7cA94oBqr9E?t=90))
- **The client declares a typed interface that extends RpcTarget, mirroring the server method's return type.** — This keeps the client type-safe. The stub is created with a using declaration so it is disposed automatically when it leaves scope. ([2:13](https://youtu.be/7cA94oBqr9E?t=133))
- **A React context provider can hold one stub, and components read it through a useContext-style hook instead of creating a stub each.** — The speaker proposes this as the answer to whether every component needs its own stub. It is a suggested pattern and is not shown in the video. ([2:40](https://youtu.be/7cA94oBqr9E?t=160))
- **Bidirectional calling was hard over HTTP, so the speaker used WebSockets, where each side exposes a class and calls the other.** — Cap'n Web's WebSocket support did not work out of the box on Bun at the time, so he used Node with the ws package. Running the server calls a client function, and running the client calls a server function. ([2:50](https://youtu.be/7cA94oBqr9E?t=170))
- **The speaker says he will use Cap'n Web in his side projects, despite calling it highly experimental.** — Cloudflare already uses it for remote bindings in Wrangler. This is a personal opinion, with no production data. ([3:33](https://youtu.be/7cA94oBqr9E?t=213))

## Techniques
- **HTTP batch RPC server** — Define a class extending RpcTarget with every method you want to expose. In the API route, return newHttpBatchRpcResponse(request, new MyAPI()) instead of the old handler, and remove the old handler. *When:* Replacing a hand-written fetch endpoint with typed, method-style calls between a TypeScript client and server, without writing URLs or parameter parsing.
- **Typed HTTP batch client with disposable stubs** — Import newHttpBatchRpcSession and RpcStub. Declare an interface extending RpcTarget whose method return types match the server. Create the stub with `using stub = ...` so it is disposed at the end of the scope, then call stub.methodName() as if it were local. *When:* Making client calls that are typed end to end and should release connection resources automatically.
- **Shared stub via React context** — Create one stub in a context provider near the app root, expose it with a hook built on useContext, and read it in each component that makes API calls. (Suggested by the speaker, not shown in the video.) *When:* Several React components need the same RPC session, so you avoid creating a new stub per component.
- **Bidirectional RPC over WebSockets** — On both ends, write a class with callable methods (for example hello()) and wrap a WebSocket connection with a session. Create a stub for the remote side on each end, so the server can call client methods and the client can call server methods. The speaker used Node with the ws package, because Bun lacked WebSocket support for Cap'n Web at the time. *When:* The server must call back into the client, for example to push events or request input, and HTTP request/response cannot do that.

## Numbers
- Library size is about 10 KB. ([3:33](https://youtu.be/7cA94oBqr9E?t=213))
- Promise pipelining eliminates multiple round trips, and batching works like GraphQL. Stated qualitatively, with no measured numbers. ([0:00](https://youtu.be/7cA94oBqr9E?t=0))

## Hot takes
- The title says Cap'n Web is 'the LAST RPC library you'll need', but the video is a 4.5-minute hello-world demo with no benchmarks or production evidence.
- The speaker calls it highly experimental and still plans to use it in side projects, citing Cloudflare's use in Wrangler remote bindings as the main reason.
- Cap'n Web's WebSocket support did not work out of the box on Bun when recorded, so Bun users need Node with ws for bidirectional calls.

## Tools mentioned
Cap'n Web (capnweb, Cloudflare), Cap'n Proto, Bun, React, Node.js, ws (WebSocket library for Node), Wrangler, tRPC, oRPC, GraphQL, TypeScript

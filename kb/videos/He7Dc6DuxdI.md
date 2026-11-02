# The BEST Way to Log in Node.js - Winston

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `He7Dc6DuxdI` · [watch](https://youtu.be/He7Dc6DuxdI) · **date:** 2025-11-02 · **length:** 9:41 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed Better Stack presenter · **orgs:** Better Stack
- **topics:** dev-tools, observability · **tags:** nodejs, winston, structured-logging, json-logs, child-logger, request-id, error-stack-traces, exception-handling, better-stack, logtail, log-centralization

> Node.js Winston logging tutorial: JSON logger setup, env-driven levels, default and child metadata, error stacks, exception and rejection files, then shipping logs to Better Stack.

## Summary
A short tutorial from Better Stack on setting up the Winston logging library in Node.js. It walks through createLogger with an info level, JSON formatting and a console transport, then adds metadata two ways: defaultMeta for a service name and child loggers for per-request IDs. It shows that errors passed to the logger log nothing useful by default, and fixes that with an errors format that includes stack traces. It then routes uncaught exceptions and unhandled rejections to their own files. The last ~3.5 minutes are a Better Stack pitch that wires a Logtail transport so logs stream to their hosted service. The technical content is accurate but basic and generic. Most of the value is the metadata and error-handling pattern, not anything specific to agents or LLMs.

## Key ideas
- **Set Winston up explicitly: createLogger with an info level, JSON format and a console transport. The level should come from an environment variable so verbosity changes without code edits.** — Speaker recommends JSON in production; simple and CLI formats are offered as more readable options for local development. JSON is also Winston's default format. ([0:08](https://youtu.be/He7Dc6DuxdI?t=8))
- **Global metadata goes on the logger via defaultMeta, and per-scope metadata goes on a child logger. Per-call metadata gets repetitive.** — Per-call objects work but must be repeated everywhere. A service name set in defaultMeta appears on every line. A child logger created with logger.child({...}) inside a function adds a request ID to every line in that scope. ([2:46](https://youtu.be/He7Dc6DuxdI?t=166))
- **Winston does not log an Error's message or stack by default. An errors format with stack enabled fixes that.** — Logging an Error through logger.error shows only level, service and timestamp. The speaker adds an errors format with stack traces turned on, after which the message and stack appear. ([3:46](https://youtu.be/He7Dc6DuxdI?t=226))
- **Uncaught exceptions and unhandled promise rejections can go to their own transports, so crashes are easy to find in a file.** — Switch the main transport to a file (standard.log). Configure exceptionHandlers and rejectionHandlers as arrays of transports, with exception.log for crashes. Ordinary logs stay in standard.log. ([5:04](https://youtu.be/He7Dc6DuxdI?t=304))
- **Centralizing logs means sending them to one hosted search backend. The speaker uses Better Stack's Logtail transport, with the source token kept in an environment variable on the server only.** — Create a source in the Better Stack dashboard, copy the token, create a Logtail client with it, and add its Winston transport to the array. Call logtail.flush() before exit so batched logs are sent. The Better Stack segment is mostly product pitch. ([6:12](https://youtu.be/He7Dc6DuxdI?t=372))

## Techniques
- **Minimal Winston logger** — Install the winston package with pnpm (or bun). Create the logger with winston.createLogger({ level: 'info' (set from an environment variable), format: winston.format.json(), transports: [new winston.transports.console()] }). Call logger.info('msg') or logger.log('info', 'msg'). Pipe output through jq to read it. *When:* Replacing console.log in any Node service that needs structured, filterable logs.
- **defaultMeta for service-wide fields** — Pass defaultMeta: { service: '<name>' } to createLogger. Every entry then includes the service field without per-call code. *When:* A process or service should tag all of its logs with a fixed identifier.
- **Child logger for request or scope metadata** — Inside a handler, const child = logger.child({ requestId }). Use child.info(...) inside that scope. Metadata from the parent (such as service) is kept. *When:* You need to filter all log lines for one request, job or unit of work.
- **Logging errors with stack traces** — Add winston.format.errors with stack enabled to the format chain (the speaker describes it as an errors format configured to show stacks; the exact literal is not fully shown in the transcript). Then logger.error(err) shows message and stack. *When:* Any time errors are logged. Without this, error objects lose their message and stack.
- **Separate files for crashes and rejections** — Set transports to [new winston.transports.file({ filename: 'standard.log' })]. Set exceptionHandlers and rejectionHandlers to arrays with file transports filename 'exception.log' (and a similar file for rejections). Uncaught exceptions and unhandled promise rejections are then captured without an explicit catch. *When:* You want crash and rejection traces isolated from routine logs, without adding try/catch everywhere.
- **Ship logs to Better Stack via Logtail** — Install the Logtail Node and Winston packages (the transcript names them as the @logtail/node and @logtail/winston packages, inferred from the spoken 'LogTail slash node' and 'slash Winston'). Create the source in Better Stack: Telemetry, Sources, Connect source, JavaScript and Node.js, then copy the source token. Create const logtail = new Logtail(<token from env var>). Add new LogtailTransport(logtail) to the Winston transports. Call await logtail.flush() at app exit. Check Live tail in Better Stack. *When:* Several services or hosts need one searchable place for logs and you are already using Better Stack.

## Numbers
- Video length is 9:41. The Better Stack product segment runs about 6:12 to 9:41, roughly 3.5 minutes, so over a third of the video is vendor promotion. ([6:12](https://youtu.be/He7Dc6DuxdI?t=372))
- The speaker calls Better Stack 'the fastest log search on the planet' and says a free account is enough to start. No benchmark or evidence is given. ([6:12](https://youtu.be/He7Dc6DuxdI?t=372))

## Hot takes
- Keep JSON as the production log format. Local development can use simple or CLI formats.
- Winston drops error messages and stacks by default. Teams should add an errors format before relying on logs for debugging.
- The 'best way to log in Node.js' title is hype. The actual content is a standard Winston intro plus a vendor pitch, with no comparison to pino or other loggers.
- Store the Better Stack source token in an environment variable and keep it on the server only.

## Tools mentioned
Winston (Node.js logging library), Node.js, pnpm, Bun, jq (pretty-printing JSON output in the terminal), Better Stack (hosted log search; Telemetry Sources), Logtail Node client and Winston transport (@logtail/node, @logtail/winston, inferred from spoken names)

## Relevance to our work
- **agentos** (1/3): AgentOS is mostly Rust and Python per the profile, so Winston is not directly usable. The reusable idea is request-scoped child metadata so all log lines for one request can be filtered, which the OTel and observability layer should also carry. → *When wiring the L4 OTel and logging layer, make sure every request span and log line carries a shared request ID, using the same scoped-metadata idea shown here (child logger style).*

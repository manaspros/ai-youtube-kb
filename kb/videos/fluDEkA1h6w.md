# Pino JS - Logging in JavaScript / Node.js applications

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `fluDEkA1h6w` · [watch](https://youtu.be/fluDEkA1h6w) · **date:** 2024-11-02 · **length:** 41:30 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack
- **topics:** observability, dev-tools · **tags:** pino, logging, node.js, structured-logging, json-logs, transports, redaction, pino-pretty, fastify, better-stack, logtail, child-loggers, log-levels

> Better Stack walkthrough of Pino, the fast JSON logger for Node.js: log levels, formatters, child loggers, error logging, worker-thread transports, redaction, Fastify integration, and shipping logs to Better Stack.

## Summary
A hands-on tutorial building up a Node.js logging setup with Pino in a small index.js, then adding Fastify. It covers default JSON output and log levels (including a custom level), piping to pino-pretty for human-readable output, the env-var log level pattern, formatters to change the level label, and child loggers to bind context once. It shows passing Error objects so stack traces are serialized, and uses pino.transport to write to a file, to stdout, and to multiple targets in a worker thread. It finishes with the redact option (mask or remove sensitive paths), Fastify's built-in logger with request.log, and a Better Stack (Logtail) transport with a source token, ending with search examples in the Better Stack UI. The code is simple and reproducible; the last several minutes promote the presenter's own log platform.

## Key ideas
- **Pino emits JSON by default, which is the structured format you need for searching and extraction later.** — Each line has numeric level (info=30, error=50), time, pid, hostname and msg. The speaker calls it a super-fast all-JSON logger with about 12.4k GitHub stars at the time of recording. ([0:00](https://youtu.be/fluDEkA1h6w?t=0))
- **Levels are numeric and ordered (fatal, error, warn, info, debug, trace), so the default threshold filters output.** — Setting the level to warn hides info (30) and keeps warn (40) and above. Custom levels can be added with a numeric value, for example catastrophe at 70, which sits above error. ([6:24](https://youtu.be/fluDEkA1h6w?t=384))
- **Attach per-request or per-user context with a child logger instead of repeating an object on every call.** — logger.child({ username }) returns a logger that stamps that field on every line. Changing the context then only needs editing in one place. ([17:02](https://youtu.be/fluDEkA1h6w?t=1022))
- **Pass the Error object as the first argument to get a serialized error with a stack trace.** — The speaker wraps divide(5, 0) in try/catch, where the function throws on b === 0. Passing the error as the first arg to logger.error(err, msg) puts the full error object, including the stack, in the JSON. ([20:55](https://youtu.be/fluDEkA1h6w?t=1255))
- **Transports run log shipping off the main thread, so file or network I/O does not delay API responses.** — From Pino 7, pino.transport runs the transport in a worker thread. A transport is a module whose default export returns a writable stream. The built-in pino/file target writes to disk, and remote services have npm transports. ([22:19](https://youtu.be/fluDEkA1h6w?t=1339))
- **Multiple destinations use targets in pino.transport, and a formatter that changes the level breaks with multiple transports.** — The speaker sends one pino-pretty target to a file and another to stdout. The docs say the level cannot be customised with multiple transports, so the formatters block has to be removed in that setup. ([27:29](https://youtu.be/fluDEkA1h6w?t=1649))
- **Redact sensitive fields at the logger instead of relying on downstream cleanup.** — The redact option takes a list of paths (email, password, address) that are masked. Switching to an object with remove: true drops those keys entirely. The speaker says to assume logs can be read by anyone, including attackers. ([29:45](https://youtu.be/fluDEkA1h6w?t=1785))
- **Fastify's logger: true uses Pino by default, and request.log gives a per-request logger.** — The same customisation applies inside Fastify handlers. The speaker says Express and NestJS can also be configured to use Pino. ([32:12](https://youtu.be/fluDEkA1h6w?t=1932))
- **A Better Stack source token in a Logtail Pino transport ships the logs to a hosted platform for live tail, search and dashboards.** — The token is pasted into the script for the demo, with a note that it should come from an environment variable in real apps. Search examples use log = error and message contains employee. ([35:55](https://youtu.be/fluDEkA1h6w?t=2155))

## Techniques
- **Minimal Pino setup and pretty output** — npm init -y; npm install pino; npm install pino-pretty (local, not -g). Then const pino = require('pino'); const logger = pino(); logger.info('hello'). Run with: node index.js | npx pino-pretty. *When:* Starting any Node.js service that needs structured logs. Use the pretty output for local development and raw JSON when shipping logs.
- **Log level from environment** — pino({ level: process.env.PINO_LOG_LEVEL || 'info' }). Set the env var before running (PowerShell: $env:PINO_LOG_LEVEL='warn'; Unix: PINO_LOG_LEVEL=warn node index.js, or export it for the session). *When:* Any deployed service, so verbosity can change without a code change (12-factor config).
- **Custom log level** — pino({ customLevels: { catastrophe: 70 } }), then call logger.catastrophe('...'). The speaker calls the option 'custom levels'. *When:* When a severity sits between or above the built-in levels and needs its own method.
- **Uppercase level label via formatter** — pino({ formatters: { level(label) { return { level: label.toUpperCase() }; } } }). The formatter must return a JSON-serialisable object. *When:* When log consumers expect text levels such as ERROR instead of numbers. Not compatible with multiple transports.
- **Child logger for fixed context** — const userLogger = logger.child({ username: 'John Doe' }); then userLogger.info('...') with no extra object argument. In the video the username is hard-coded, but the speaker suggests reading it from request.user in an Express handler. *When:* When the same fields (user, request id, tenant) should appear on every line in a scope.
- **Logging errors with stack traces** — try { const r = divide(5, 0); } catch (err) { logger.error(err, 'An error occurred during the division'); } where divide throws new Error('cannot divide by zero') when b === 0. *When:* Any catch block. Put the error first so Pino serialises it, including the stack.
- **File transport with pino.transport** — const transport = pino.transport({ target: 'pino/file', options: { destination: './logs/output.log', mkdir: true } }); const logger = pino({ level: 'info' }, transport); *When:* When logs should go to disk without blocking the request path. mkdir: true creates the directory.
- **pino-pretty to a file without colour** — Set target: 'pino-pretty' with options: { destination: './logs/output.log', colorize: false }. *When:* Human-readable log files. Keep plain JSON if a log collector will parse them.
- **Multiple log destinations** — pino.transport({ targets: [ { target: 'pino-pretty', options: { destination: './logs/output.log', colorize: false } }, { target: 'pino-pretty', options: { destination: process.stdout.fd } } ] }). Remove any formatters block, because level customisation is not allowed with multiple transports. *When:* Fanning out to a local file and the console at once, or adding a remote shipper as a third target.
- **Redacting sensitive fields** — pino({ redact: ['email', 'password', 'address'] }) masks the values. For removal: pino({ redact: { paths: ['email', 'password', 'address'], remove: true } }). *When:* Any object that holds PII or secrets (employee or user records, tokens). Apply it in the logger config, not in each call site.
- **Fastify with Pino** — const fastify = require('fastify')({ logger: true }); fastify.get('/', (request, reply) => { request.log.info(request, 'request to server'); reply.send({ hello: 'world' }); }); fastify.listen to port 3000 (the video calls fastify.listen with port 3000). *When:* Fastify services. Use request.log so each request's log lines carry request context.
- **Shipping logs to Better Stack** — npm install @logtail/pino. Add a third target: { target: '@logtail/pino', options: { sourceToken: token } }, where token comes from creating a Node.js source in the Better Stack Logs UI. Search there with log = error or message contains employee. *When:* When logs must be centralised and searched or charted. Keep the token in an environment variable, not in source code.

## Numbers
- Pino GitHub repo had about 12,400 stars when recorded. ([0:00](https://youtu.be/fluDEkA1h6w?t=0))
- Default log level values: info=30, error=50. Custom catastrophe level set to 70. ([3:53](https://youtu.be/fluDEkA1h6w?t=233))
- Default level set to warn (40) hides info (30) output. ([9:09](https://youtu.be/fluDEkA1h6w?t=549))
- Transports in worker threads from Pino version 7 onward. ([22:19](https://youtu.be/fluDEkA1h6w?t=1339))
- Fastify GitHub repo had about 29,000 stars. ([32:12](https://youtu.be/fluDEkA1h6w?t=1932))

## Hot takes
- Quality is capped at 3 because the last ~6 minutes (about 35:00 to 41:00) are a product pitch for the presenter's own platform, Better Stack. The first 35 minutes are a generic, accurate Pino walkthrough.
- Redaction should be configured in the logger, not left to downstream tools, and logs should be treated as readable by anyone (stated by the speaker).
- The speaker treats the 12-factor pattern of setting log level by environment variable as the normal way to configure logging.

## Tools mentioned
Pino, pino-pretty, npm, Node.js, npx, VS Code, Fastify, Better Stack Logs, @logtail/pino (Logtail Pino transport), Express (mentioned), NestJS (mentioned), Winston (mentioned), PowerShell, Unix shell

## Relevance to our work
- **agentos** (1/3): AgentOS has an L4 observability layer (Prometheus, Grafana, OTel) and a PII scan in the Govrix proxy. Pino's structured logs and redact paths are a cheap, low-level way to keep PII out of Node-side logs, but the video does not cover tracing or metrics. → *Check whether any Node-side service in AgentOS logs request bodies, headers or user fields. Add Pino redact paths (with remove: true) as a regression test that the fields never appear in output.*

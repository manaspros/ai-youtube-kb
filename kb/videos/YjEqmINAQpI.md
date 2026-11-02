# Winston - Logging in JavaScript & Node.js applications

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `YjEqmINAQpI` · [watch](https://youtu.be/YjEqmINAQpI) · **date:** 2024-11-02 · **length:** 30:28 · **format:** demo · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack
- **topics:** observability, dev-tools · **tags:** winston, nodejs, logging, structured-logging, log-levels, transports, child-logger, defaultMeta, error-stack, profiling, log-centralisation, better-stack

> Tutorial on Winston, the Node.js logging library: levels, transports, JSON and printf formats, child and named loggers, error stacks, startTimer profiling, and shipping logs to Better Stack.

## Summary
The unnamed Better Stack presenter walks through Winston, a Node.js logging library, starting from an empty npm project in VS Code. The video covers log levels (the default level is info, and less severe entries are dropped), transports (console, file, and remote), and per-transport levels. It then shows the JSON and cli formats, a custom printf format that needs the timestamp format, and how to attach key-value metadata with child loggers. Further sections cover error stack traces, named loggers with defaultMeta for separate services, and basic profiling with startTimer and done. The last section adds the community Better Stack (Logtail) transport and demonstrates live tail and a numeric search over an indexed duration key. The content is a clear, practitioner-level how-to. It is a tool walkthrough with light vendor promotion for Better Stack, and the hard-coded token is shown only for the demo.

## Key ideas
- **Each Winston logger can have several transports (console, file, remote service, database), and each transport can have its own level.** — Example: error-only output to a file while info and debug also go to the console. Winston ships with community transports for MongoDB, Syslog, Telegram, MySQL and Better Stack. ([1:19](https://youtu.be/YjEqmINAQpI?t=79))
- **Level filtering happens at the logger and at the transport. Entries less severe than the configured level are discarded.** — The default level is info. Levels run error, warn, info, http, verbose, debug, silly, with lower numbers meaning more severe. ([5:09](https://youtu.be/YjEqmINAQpI?t=309))
- **The default output is JSON. The cli format suits the console, and printf gives a custom string but needs the timestamp format added to combine, or the timestamp prints as undefined.** — Formats are composed with winston.format.combine, using timestamp, printf, prettyPrint and json. ([8:59](https://youtu.be/YjEqmINAQpI?t=539))
- **Key-value context can be attached once with logger.child(...) so every entry from that child carries the fields without passing them to each call.** — The demo uses an HTTP-style request object with method and an authenticated boolean. ([12:55](https://youtu.be/YjEqmINAQpI?t=775))
- **The errors format with stack: true adds stack traces to error entries.** — It is applied inside format.combine on the logger. ([15:25](https://youtu.be/YjEqmINAQpI?t=925))
- **Named loggers created with winston.loggers.add and fetched with winston.loggers.get give each service its own config. defaultMeta tags every entry with a service key.** — The demo has an order logger with a file and console output, and a payment logger that writes JSON only to a file. ([16:43](https://youtu.be/YjEqmINAQpI?t=1003))
- **Profiling uses logger.startTimer(), then profiler.done({message}). The output includes a duration in milliseconds.** — It works with any Winston logger, and the demo measures a simulated request handler. ([22:44](https://youtu.be/YjEqmINAQpI?t=1364))
- **Centralisation uses the Better Stack community transport. The presenter says the token should come from process.env in production, not be hard-coded as in the demo.** — A source is created in the Better Stack UI as a Node.js platform, which gives a source token, and the transport is added alongside the file transport. ([25:14](https://youtu.be/YjEqmINAQpI?t=1514))
- **Once logs are centralised and keys are indexed, numeric comparisons such as duration greater than 500 can find slow requests and feed charts, dashboards and alerts.** — A 975.4 ms request matched the greater-than-500 search, and a threshold of 1000 returned no matches. ([28:54](https://youtu.be/YjEqmINAQpI?t=1734))

## Techniques
- **Basic Winston logger with console and file transports** — npm init -y; npm install winston. Then const winston = require('winston'); const logger = winston.createLogger({ level: 'debug', format: winston.format.json(), transports: [ new winston.transports.Console(), new winston.transports.File({ filename: 'app.log' }) ] }); then logger.info('...') and logger.error('...'). *When:* Starting any Node.js service that needs structured logs in both the terminal and a file.
- **Per-transport level** — Pass level on the transport: new winston.transports.File({ filename: 'app.log', level: 'error' }). The logger's own level still applies first. *When:* Sending only errors to a file, or sending everything to the console.
- **Readable console output and a custom timestamped line** — Use the cli format on the console, or winston.format.combine(winston.format.timestamp(), winston.format.printf(info => `${info.timestamp} ${info.level} ${info.message}`)). Add winston.format.prettyPrint() to the combine call for indented JSON in the terminal. Keep JSON for files and aggregators. *When:* Local development where people read the console, while files stay machine-parseable.
- **Child logger for request-scoped fields** — const child = logger.child({ method: 'GET', isAuthenticated: false }); then call child.info('...') and child.error('...') with no extra object argument. *When:* Many log calls in one request or component share the same context fields.
- **Stack traces for errors** — Add winston.format.errors({ stack: true }) to format.combine, then log the Error object through logger.error. *When:* You want stack traces in error entries, for example on 5xx responses.
- **Named loggers per service** — winston.loggers.add('orderLogger', { level, format, transports: [...], defaultMeta: { service: 'order service' } }). Fetch with const orderLogger = winston.loggers.get('orderLogger'). Use a different file per logger, such as orders.log and payments.log. *When:* Separate service boundaries need different outputs, severity levels or metadata.
- **Timing a block of code** — const profiler = paymentLogger.startTimer(); ...work...; profiler.done({ message: `request ${path} processed` }). The entry gets a duration field in milliseconds. *When:* Adding latency measurements to request handlers without a separate metrics library.
- **Shipping logs to Better Stack with the Winston transport** — Create a source on the Better Stack logs page (platform: JavaScript / Node.js) and copy its source token. Install the packages named in the Better Stack Winston docs (the names are not spoken in the video). Create a Logtail client with the token, then new Logtail transport with that client, and add it to the transports array. Read the token from process.env in production, as the presenter advises. *When:* You need a hosted search, live tail and alerts over structured logs.

## Numbers
- Video length 30:28. Default Winston logger level is info. ([0:00](https://youtu.be/YjEqmINAQpI?t=0))
- Log levels in order of severity: error, warn, info, http, verbose, debug, silly. ([2:35](https://youtu.be/YjEqmINAQpI?t=155))
- Data retention on the free Better Stack plan is three days by default. ([25:14](https://youtu.be/YjEqmINAQpI?t=1514))
- Profiling demo loops 0 to 1 billion, multiplying each value by 2, to simulate latency. ([22:44](https://youtu.be/YjEqmINAQpI?t=1364))
- Profiled request took 975.4 ms. A greater-than-500 search matched it, and a greater-than-1000 search returned nothing. ([28:54](https://youtu.be/YjEqmINAQpI?t=1734))

## Hot takes
- Better Stack promotes its own hosted log service in a tutorial that is framed as generic Winston instruction. The Better Stack transport and source setup are shown as the main next step.
- The presenter warns against hard-coding tokens, but the demo does it anyway, so the warning matters more than the example.
- The video reads as a solid intro to Winston. It does not cover log rotation, performance cost, or sampling, and the presenter says those may come later.

## Tools mentioned
Winston (Node.js logging library, version not stated), Node.js, npm, VS Code, GitHub (Winston readme), Better Stack (log service, with its Winston/Logtail transport), Winston community transports: MongoDB, Syslog, Telegram, MySQL

## Relevance to our work
- **agentos** (1/3): Structured JSON logs with per-request context and duration fields are a useful pattern for the L4 observability stack, but this video is a Node.js-only logging introduction and gives no distributed-systems or benchmark content. → *If any AgentOS service is Node.js, add a child logger with a request id and a startTimer duration to a single handler, then check that the JSON entries can be queried in the existing observability stack.*

# PHP Logging with Monolog

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `GLbeuxNAcn8` · [watch](https://youtu.be/GLbeuxNAcn8) · **date:** 2024-11-02 · **length:** 24:37 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack
- **topics:** observability, dev-tools · **tags:** php, monolog, logging, structured-logging, json-logs, log-handlers, log-formatters, exceptions, composer, better-stack, logtail, laravel, symfony

> Intro tutorial on PHP logging with Monolog (channels, handlers, formatters, exceptions) that ends by shipping logs to Better Stack; useful basics, mostly vendor-tied at the end.

## Summary
A Better Stack tutorial on the Monolog logging package for PHP, run on PHP 8.2 under WSL/Ubuntu with Composer. It walks through creating a named logger (channel) per domain such as "orders", attaching a StreamHandler with a minimum level, and calling level methods with structured context arrays. It then covers formatters, switching from the default line output to JSON and to a custom LineFormatter with its own date and output format, and logging exceptions either by message or by passing the exception object in context. The video closes by creating a Better Stack source, reading its token into a LogtailHandler, and filtering live logs by level and channel. The content is accurate for a beginner but shallow: it spends the last few minutes on a vendor product, and it advises against production use of the rotating file handler.

## Key ideas
- **Monolog is a PHP logging package widely used under frameworks such as Laravel and Symfony; its core concepts are log levels, logger objects (channels), handlers and formatters.** — The video presents Monolog's GitHub page as the reference, noting it has about 20,000 stars and can send logs to files, sockets, inboxes, databases and web services. ([0:00](https://youtu.be/GLbeuxNAcn8?t=0))
- **Create one named logger (channel) per domain or subsystem rather than one global logger.** — Examples given are a channel for database connections, one for routing or caching, and an e-commerce 'orders' channel. Channels can later be filtered on in the log backend. ([4:52](https://youtu.be/GLbeuxNAcn8?t=292))
- **Handlers decide where log entries go, and a logger can have several handlers attached through pushHandler; each handler can have its own minimum level.** — A StreamHandler set to info only processes info and above. The same entries can go to a file and to standard output at the same time. ([6:04](https://youtu.be/GLbeuxNAcn8?t=364))
- **Contextual data is passed as an associative array as the second argument to a level method, and it appears under a context key in the output.** — The speaker logs 'order placed' with an order_id from a unique-id generator. Entries without context show an empty array. ([8:26](https://youtu.be/GLbeuxNAcn8?t=506))
- **Formatters belong to handlers, not to loggers: setFormatter on the handler changes how that destination renders entries.** — Switching the stdout handler to JsonFormatter emits JSON with the context nested under a key. A LineFormatter takes an output format template plus a date format; the template covers datetime, level name, message, context and extra. ([12:27](https://youtu.be/GLbeuxNAcn8?t=747))
- **Log exceptions in two ways: the message only, or the whole exception object in the context array.** — Passing the exception under an 'exception' key in context adds class, location and trace data to the JSON output, which is the more useful one for debugging. ([16:10](https://youtu.be/GLbeuxNAcn8?t=970))
- **Production logs should go to a central service rather than only to files and the terminal, and the service token should come from an environment file, not from source that gets committed.** — The speaker creates a Better Stack source of platform PHP, copies its token, and adds a LogtailHandler. Logtail's PHP client needs the curl extension (php8.2-curl on Ubuntu for PHP 8.2). ([18:38](https://youtu.be/GLbeuxNAcn8?t=1118))
- **The rotating file handler (one file per day) is described as not production-ready; the speaker recommends logrotate on a real system.** — Other handler families listed are email/SendGrid alerts, AMQP, Amazon SQS, and Redis, MongoDB and CouchDB database handlers. ([11:06](https://youtu.be/GLbeuxNAcn8?t=666))

## Techniques
- **Install Monolog with Composer** — Install PHP 8.2 and Composer on Ubuntu/WSL (the install commands are on linked pages and were not read out), then run the composer require command from the Monolog GitHub README. Composer creates composer.json, composer.lock, vendor/ and vendor/autoload.php; commit the lock file so every developer gets the same versions. *When:* Starting any new PHP project that needs structured logging.
- **Bootstrap the autoloader and import aliases** — At the top of the entry file, require_once the vendor/autoload.php file that Composer generated. Add `use` statements for Logger, StreamHandler and the formatter classes so they can be referenced by short names. *When:* Any PHP entry point that uses Composer packages.
- **One logger per channel with a level-filtered file handler** — Create `new Logger('orders')`. Create a StreamHandler with a file path in the current directory (orders.log) and pass the info level as its second argument. Attach it with `$logger->pushHandler($handler)`. Then call `$logger->info('order placed', [...context])` and `$logger->error(...)`. *When:* Separating logs by subsystem (orders, database, routing) and filtering noisy levels per destination.
- **Fan out to multiple destinations** — Create a second StreamHandler that writes to standard output, using the stream syntax shown in the Monolog docs, and push it onto the same logger. Entries then reach both the file and the terminal. Remove the file handler once it is no longer needed. *When:* Development: see logs in the terminal while keeping a file copy.
- **Switch output format with a formatter** — Import JsonFormatter and call `$handler->setFormatter(new JsonFormatter())` on the stdout handler. For a custom single-line format, define a date-format string and an output template with the datetime, level name, message, context and extra placeholders, then pass both to LineFormatter and call setFormatter with it. The LineFormatter import must be added explicitly. *When:* Machine-readable logs (JSON) for a log pipeline, or a fixed human-readable line format.
- **Log exceptions with context** — Wrap the risky code in try/catch. In catch, call `$logger->error($e->getMessage())` for a message-only entry, or `$logger->error('...', ['exception' => $e])` to put the exception object under an exception key, which captures location and trace data in the JSON output. *When:* Input validation or any failure path where you need debuggable error entries.
- **Ship logs to Better Stack (Logtail)** — In Better Stack, open Logs & metrics > Sources, create a source with platform PHP, and copy its source token. Store the token in an environment file (the speaker says not to hard-code it). Install the Better Stack PHP client via the composer require statement from Better Stack's PHP docs; this needs the curl extension (php8.2-curl on Ubuntu). Import the LogtailHandler, instantiate it with the token, and push it onto the logger. Use Live tail and click a level or channel value to filter. *When:* Production centralization, search, dashboards and alerting over logs from several services.

## Numbers
- Monolog GitHub repo has about 20,000 stars (shown on screen as a popularity signal). ([0:00](https://youtu.be/GLbeuxNAcn8?t=0))
- Demo environment is PHP 8.2 on Ubuntu under WSL. ([0:00](https://youtu.be/GLbeuxNAcn8?t=0))
- Default rotating file handler creates one log file per day. ([11:06](https://youtu.be/GLbeuxNAcn8?t=666))
- Demo pin-entry check requires exactly 4 characters. ([16:10](https://youtu.be/GLbeuxNAcn8?t=970))
- Video runtime is 24:37. ([0:00](https://youtu.be/GLbeuxNAcn8?t=0))

## Hot takes
- Intro-level content: nothing about performance, sampling, log volume or cost; it stays on configuration.
- The final ~5 minutes are a demo of the Better Stack product (sources, live tail, filtering) and the video is published on Better Stack's channel, so treat the product-specific parts as vendor content.
- It explicitly advises against the rotating file handler in production and recommends logrotate, which is a useful caveat that beginners often miss.
- Advice to read the Better Stack token from an environment file is correct, but the code samples in the video hard-code it into app.php for the demo.

## Tools mentioned
Monolog (PHP logging package), PHP 8.2, Composer, Ubuntu, Windows Subsystem for Linux (WSL), VS Code, Better Stack Logs (Live tail, sources), Better Stack PHP client (Logtail handler, installed via Composer), php8.2-curl, Laravel, Symfony, Elasticsearch / MongoDB / FluentD formatters (listed, not used), logrotate (recommended for production rotation), SendGrid, AMQP, Amazon SQS, Redis, MongoDB, CouchDB handlers (listed, not used)

## Relevance to our work
- **agentos** (1/3): Per-channel loggers with JSON context and fan-out handlers are a basic pattern for structured logs; AgentOS's L4 observability uses OTel, and this video does not cover tracing. → *Check that gateway and proxy logs use one named channel per pillar (budgets, PII scan, audit) with JSON context keys like request_id, rather than free-text messages.*

# Loguru - Simplified Python Logging with Loguru!

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `gSc1oHcwkE4` · [watch](https://youtu.be/gSc1oHcwkE4) · **date:** 2024-11-02 · **length:** 28:56 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack
- **topics:** dev-tools, observability · **tags:** python, logging, loguru, structured-logging, json-logs, log-rotation, exception-logging, context-binding, better-stack, log-centralization

> Intro tutorial on Loguru, a Python logging library: sinks, format, JSON output, context binding, exception capture, file rotation, and shipping logs to Better Stack.

## Summary
Better Stack walks through Loguru, a third-party Python logging package that the speaker presents as easier than the standard library's logging module. The whole API is driven by one function, logger.add, which registers a sink (stdout, a file path, a function, or a coroutine) along with its format, minimum level, and serialization options. The video covers the seven log levels, colorized and JSON output, custom JSON shaping via logger.patch, per-sink level thresholds, multiple sinks, context via bind and contextualize, exception capture with logger.catch, and file rotation and retention. The final section wires a Better Stack Logtail handler in as another sink and filters live logs by level and by a bound extra field. The Loguru material is practical and reproducible, but the closing segment is a vendor product demo from the channel's own sponsor-adjacent platform, and the popularity claim rests only on a GitHub star count shown on screen. The video is intro-level: it does not discuss performance, thread or process safety, or interop with stdlib logging.

## Key ideas
- **Loguru is presented as the most popular third-party Python logging package and as easier to use than the standard library: import a ready logger object and log immediately.** — The speaker cites 17,400 GitHub stars shown on the repo page as the popularity evidence. The main pitch is less setup than stdlib logging. ([0:00](https://youtu.be/gSc1oHcwkE4?t=0))
- **Loguru has seven levels: trace, debug, info, success, warning, error, critical. Levels let sinks filter by severity.** — Level methods take a message string. The speaker demonstrates logger.info, logger.error and logger.critical. ([3:27](https://youtu.be/gSc1oHcwkE4?t=207))
- **A single entry point, logger.add, configures every output: where logs go, format, minimum level, filters, serialization and file rotation.** — A sink can be sys.stdout, a file path string, a function, a built-in handler, or a coroutine function. ([4:24](https://youtu.be/gSc1oHcwkE4?t=264))
- **Loguru installs a default handler, so a custom handler produces duplicate output until the default is removed with logger.remove().** — The speaker sees each message printed twice after adding a stdout sink, then fixes it by removing the default configuration. ([5:36](https://youtu.be/gSc1oHcwkE4?t=336))
- **serialize=True makes a sink emit JSON, and logger.patch lets you control the JSON shape with a function that writes into the record's extra dict.** — The patch function builds the JSON, stores it at record extra serialized, and the output includes that field. Loguru's own JSON is a default shape. ([8:03](https://youtu.be/gSc1oHcwkE4?t=483))
- **Context fields come in two forms. logger.bind returns a child logger that always carries its fields; logger.contextualize is a context manager that scopes fields to a block.** — The format string must include the extra directive, otherwise bound fields do not appear. Bound and contextualized fields show up under the extra key in JSON output. ([12:03](https://youtu.be/gSc1oHcwkE4?t=723))
- **logger.catch works as a context manager or a decorator and logs the exception with file, line and exception type. Its default level is ERROR, and a level argument can raise it to CRITICAL.** — The speaker shows a missing-file error logged with the line number where it was raised. An exception argument can restrict which exception types are caught. ([16:05](https://youtu.be/gSc1oHcwkE4?t=965))
- **Rotation and retention are file-sink options. Rotation renames the active file with a timestamp and starts a new app.log, and retention deletes rotated files older than a set age.** — The demo uses 5-second rotation and 10-second retention purely to show behavior. Retention accepts a string, an integer or a timedelta. ([20:10](https://youtu.be/gSc1oHcwkE4?t=1210))
- **Better Stack is wired in as one more sink with its own format and level, and its live tail can filter by level or by a bound field such as extra userID.** — The source token is hardcoded in the demo. The speaker warns to move it to an environment file and keep it out of source control. ([25:09](https://youtu.be/gSc1oHcwkE4?t=1509))

## Techniques
- **Minimal Loguru setup** — pip install loguru, then `from loguru import logger`, then call logger.info(...) or logger.error(...) directly. No handler or config is needed for the default output. *When:* Quick scripts or any app where stdlib logging config feels heavy.
- **Replace the default sink with a custom stdout sink** — import sys; logger.add(sys.stdout, format=...) to register a stdout sink with a format string using {time}, {level} and {message}. Then logger.remove() to drop the default handler so each message prints once. *When:* Whenever you want your own terminal format instead of Loguru's default.
- **Colors via format markup** — Wrap text in <green>...</green> to color it. Use <level>...</level> to color by log level, so info appears white and error appears red. Colors only apply to terminal output. *When:* Human-readable local development output.
- **JSON output** — logger.add(sys.stdout, serialize=True) or logger.add('app.log', serialize=True) emits one JSON object per record. *When:* Log shipping and machine-parsed logs.
- **Custom JSON shape with logger.patch** — Define patching(record) that builds the JSON string and sets record['extra']['serialized'] to it. Then use logger = logger.patch(patching) and reference the serialized value in the format string. The exact format directive is not spoken in the transcript, so check the Loguru docs for it. *When:* When log consumers need a specific JSON schema with fixed keys.
- **Per-sink level threshold** — logger.add(sink, level='WARNING') drops messages below WARNING for that sink only. Use exact level names such as WARNING; the speaker's 'warn' raised an error. *When:* Send verbose logs to a file while keeping the terminal quiet, or the reverse.
- **Multiple sinks** — Call logger.add once per destination. Each call takes its own format, level and serialize setting, e.g. a colored stdout sink plus a JSON file sink. *When:* Human-readable console output alongside machine-parsed files.
- **Bound context** — child = logger.bind(user_id=1, ip_address='...'). Log through child. Add {extra} to the format string so the fields appear. *When:* Per-request or per-user fields that should appear on every record from one code path.
- **Scoped context** — with logger.contextualize(user_id=1, ip_address='...'): ... Only records logged inside the block carry the fields. *When:* Temporary context for one block of work, without creating a child logger.
- **Exception capture** — Use `with logger.catch():` around risky code, or decorate a function with `@logger.catch` (or `@logger.catch(level='CRITICAL')`). Pass exception=SomeErrorType to restrict which exceptions are caught; default level is ERROR. *When:* Making unhandled failures in background code or scripts show up in logs with file and line.
- **File rotation and retention** — logger.add('app.log', rotation=<interval>, retention=<age>). The active file stays app.log; rotated files get timestamped names; retention removes rotated files older than the age. The demo used 5 seconds and 10 seconds, which are demo values only. *When:* Long-running services writing to local log files.
- **Better Stack sink** — In Better Stack, go to Logs & Metrics, create a source, choose Python, and copy the source token (default retention shown was 3 days). Install the Better Stack Python driver with the pip command from their guide page. Create the LogTail handler with the token as a keyword argument, then logger.add(handler, format=..., level='DEBUG'). Store the token in an environment file, not in code. *When:* Centralized, searchable logs for a team; filter live tail by level or by extra.userID.

## Numbers
- Loguru has 17,400 GitHub stars, shown on screen as its popularity evidence ([0:00](https://youtu.be/gSc1oHcwkE4?t=0))
- Seven built-in levels: trace, debug, info, success, warning, error, critical ([3:27](https://youtu.be/gSc1oHcwkE4?t=207))
- Demo file rotation every 5 seconds and retention of 10 seconds; demo values only, production should be much longer ([20:10](https://youtu.be/gSc1oHcwkE4?t=1210))
- Better Stack default log retention for a new source is 3 days (adjustable by plan) ([24:09](https://youtu.be/gSc1oHcwkE4?t=1449))

## Hot takes
- The popularity claim rests only on a GitHub star count shown on screen, not on download or usage data.
- The last third is a demo of Better Stack's own platform. The Loguru material stands alone, but the centralization part is a vendor walkthrough.
- The demo hardcodes the Better Stack source token in app.py. The speaker warns against committing it, so treat that as demo-only code.
- Intro-level only: no discussion of performance, multi-process or thread safety, or interop with stdlib logging.

## Tools mentioned
Loguru, Python standard library logging (comparison only), pip, VS Code, Better Stack (Logs & Metrics, Live Tail), Better Stack Python driver with LogTail handler, GitHub (Loguru repo page)

## Relevance to our work
- **agentos** (1/3): AgentOS has many services and a Python-heavy eval and tooling surface; structured JSON logs with bound request fields would help correlate traces, but the Rust proxy and OTel already cover much of this. → *If any AgentOS Python component uses stdlib logging, prototype logger.bind for request-scoped fields and a serialize=True file sink with retention before adding more logging infrastructure.*
- **prosharness** (1/3): ProsHarness wraps long agent runs with checkpoint/resume and multi-step plan and critique loops, where per-run JSON logs and exception capture would help diagnose failed runs. → *Wrap checkpoint/resume and plan-critique steps in logger.catch and write a rotated JSON run log with a bound run_id.*

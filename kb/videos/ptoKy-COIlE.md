# Go Structured Logging with the slog Package (Golang)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `ptoKy-COIlE` · [watch](https://youtu.be/ptoKy-COIlE) · **date:** 2024-11-02 · **length:** 37:23 · **format:** tutorial · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Better Stack, Heroku
- **topics:** observability, dev-tools · **tags:** go, golang, slog, structured-logging, logfmt, json-logging, child-loggers, log-redaction, logvaluer, io-multiwriter

> Better Stack walkthrough of Go's log/slog package (Go 1.21+): levels, text and JSON handlers, attributes, groups, child loggers, file and multi-writer output, and redaction via LogValuer.

## Summary
The video is a hands-on tutorial on structured logging with Go's log/slog package, introduced in Go 1.21. It starts from the classic log package and its limits: no levels, no key-value output, and little configuration. It then shows slog's default logger, text and JSON handlers, the default Info level (overridden with HandlerOptions), and typed or key-value attributes. Groups nest attributes (a nested object in JSON, dot notation in the text handler), and logger.With creates child loggers that carry fixed attributes. The last sections cover writing logs to a file opened with os.OpenFile, fanning out with io.MultiWriter, and redacting sensitive fields by implementing LogValue. The content is generic Go practice with no AI-specific material. Its value to this KB is as a reference for logging hygiene.

## Key ideas
- **log/slog (Go 1.21+) is the built-in structured logger with levels, handlers, attributes, groups and child loggers.** — Structured output can be searched by key, which the classic log package cannot do. The classic package has no levels, no key-value output and little configuration. ([0:00](https://youtu.be/ptoKy-COIlE?t=0))
- **The classic log package has no levels, no structured output and limited configuration.** — Output is a single text string with the flags and message, so key-value lookups are not possible. The speaker's case for moving to slog rests on these limits. ([3:59](https://youtu.be/ptoKy-COIlE?t=239))
- **slog's default level is Info, so Debug lines are dropped unless the handler is configured.** — Setting HandlerOptions{Level: slog.LevelDebug} on the handler enables Debug output. AddSource: true adds a source key that points at the file and line. ([6:20](https://youtu.be/ptoKy-COIlE?t=380))
- **Two built-in handlers: TextHandler writes logfmt-style key=value lines, JSONHandler writes JSON, and both use time, level and msg as default keys.** — The speaker says the text format is commonly called logfmt and was popularized by Heroku. Swapping handlers changes only the output format, not the call sites. ([7:37](https://youtu.be/ptoKy-COIlE?t=457))
- **Attributes can be passed as alternating key/value arguments or as typed slog.Attr values, and an odd argument count produces a bad-key error.** — The speaker calls out the missing-value problem with variadic key/value pairs, which he says has caused debate in the Go community. Typed constructors such as slog.String and slog.Int give stronger typing. ([13:45](https://youtu.be/ptoKy-COIlE?t=825))
- **slog.Group nests related attributes, producing a nested object in JSON and dot-separated keys in the text handler.** — Groups keep request-level and user-level context organised in the output, rather than as flat keys. ([16:18](https://youtu.be/ptoKy-COIlE?t=978))
- **Child loggers via logger.With(...) attach fixed attributes once, so every later call on that logger includes them.** — The speaker recommends this over repeating the same attributes at each call site. Changing the child logger definition updates every use of it. ([20:17](https://youtu.be/ptoKy-COIlE?t=1217))
- **Redact sensitive fields by implementing LogValue() slog.Value on the type, so the logger emits only what that method returns.** — In the demo a User struct with a password field logs only its ID. A fuller version uses slog.StringValue with fmt.Sprintf to build a custom representation. ([30:48](https://youtu.be/ptoKy-COIlE?t=1848))

## Techniques
- **Replace the default logger with a configured one** — logger := slog.New(slog.NewTextHandler(os.Stderr, nil)), then slog.SetDefault(logger). Package-level slog.Info/Error calls then use this handler. Pass &slog.HandlerOptions{Level: slog.LevelDebug} instead of nil to enable Debug, and AddSource: true to add a source key. *When:* Any Go service that needs a single, consistent log format or a non-default minimum level.
- **Switch to JSON for aggregation** — Replace slog.NewTextHandler with slog.NewJSONHandler(w, opts). Keep the call sites unchanged. The speaker's point is that JSON records can then be searched and charted in a platform such as Better Stack. *When:* Logs are shipped to a log platform or parsed by tooling. Text handler is fine for local dev.
- **Typed attributes** — logger.Info("order submitted", slog.String("user", "John Doe"), slog.Int("id", id)). Alternating key/value arguments also work, but a missing value causes a bad-key error. *When:* Prefer typed attributes in code that logs many fields, to avoid argument-pairing mistakes.
- **Group related fields** — g := slog.Group("request", slog.String("method", "GET")), then logger.Info("msg", g). JSON output nests request.method; text output shows request.method. *When:* A set of fields belongs to one entity, such as a user or an HTTP request, and should stay grouped in output.
- **Request-scoped child logger** — requestLogger := logger.With(slog.Group("request", slog.String("method", "GET")), "content-type", "application/json"). Then call requestLogger.Info(...) and requestLogger.Error(...) in the handler. The speaker notes both groups and plain key/value pairs work with With. *When:* Fields such as request ID or content type must appear on every line emitted while handling one request, without repeating them at each call.
- **Log to a file and to stderr** — Read the path from the environment (export LOG_FILE=app.log on Unix; the speaker used PowerShell syntax on Windows). Open it with f, err := os.OpenFile(os.Getenv("LOG_FILE"), os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0666), panic on error, and defer f.Close(). Then w := io.MultiWriter(os.Stderr, f) and pass w to the handler. *When:* Keep a persistent local log while still showing output on the terminal during development.
- **Redact fields with LogValuer** — Define func (u *User) LogValue() slog.Value { return slog.IntValue(u.ID) } to log only the ID. For a custom format, return slog.StringValue(fmt.Sprintf("user ID %d for user %s", u.ID, u.Username)). The Password field is never emitted. *When:* A struct with secrets or PII is passed to a log call, and the log must show only a safe projection of it.

## Numbers
- slog was introduced in Go 1.21. ([0:00](https://youtu.be/ptoKy-COIlE?t=0))
- Default slog level is Info; Debug messages are hidden unless HandlerOptions sets LevelDebug. ([6:20](https://youtu.be/ptoKy-COIlE?t=380))
- Log file is opened with flags O_CREATE|O_WRONLY|O_APPEND and permissions 0666. ([26:59](https://youtu.be/ptoKy-COIlE?t=1619))
- Demo IDs come from rand.Intn(50), so they range 0 to 49. ([13:45](https://youtu.be/ptoKy-COIlE?t=825))

## Hot takes
- The speaker says the required even key/value pairing in slog has caused debate in the Go community, and prefers typed slog attributes for stronger typing.
- Quality is capped at a solid tutorial. It is clear and correct for basic usage but has no benchmarks, no context.Context integration (only mentioned as a next step), and no discussion of performance or allocation cost.
- The text handler's key=value format is attributed to Heroku popularization (speaker's claim, unverified in the video).

## Tools mentioned
Go 1.21 (speaker's version shown as 1.21.0.4 in the captions), log/slog (NewTextHandler, NewJSONHandler, HandlerOptions, Group, With, SetDefault, LogValuer), log (standard library: New, SetOutput, Default, Lshortfile, LDate flags), io.MultiWriter, os.OpenFile, os.Getenv, math/rand (Intn), VS Code, Better Stack (log platform)

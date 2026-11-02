# Go's Built-in Package for Better Logging (using slog)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `_mqB7LLgwgs` · [watch](https://youtu.be/_mqB7LLgwgs) · **date:** 2025-11-02 · **length:** 8:51 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack
- **topics:** dev-tools, observability · **tags:** go, slog, structured-logging, json-logging, log-levels, child-logger, logging

> A short Go tutorial on the standard-library log/slog package: JSON output, levels, typed attributes, groups, child loggers, and swappable handlers.

## Summary
The video walks through Go's log/slog package, available since Go 1.21 with nothing to install, as a way to replace plain text logs with structured JSON. The presenter builds a JSON handler on stdout, sets it as the default logger so existing log calls also emit JSON, and shows that the default level is Info until handler options raise it to Debug. He then covers loosely typed key/value pairs, the typed helpers (String, Int) and the stricter LogAttrs call, followed by slog.Group for nested objects. The last part covers child loggers created with With for attributes shared across messages, WithGroup for nesting everything under one key, and the idea that slog's frontend API stays fixed while the handler backend can be swapped. It is a beginner-level tour with no benchmarks or production war stories, and the opening claim about cutting debug time is not backed by anything shown.

## Key ideas
- **slog ships in the Go standard library from Go 1.21, so there is nothing to install; slog.Info(msg) is the basic call.** — The first value is always the message; the rest are attributes. The presenter notes the output is not much different from log until a JSON handler is attached. ([0:00](https://youtu.be/_mqB7LLgwgs?t=0))
- **A JSON handler on os.Stdout plus slog.SetDefault gives consistent JSON output, and the old log package output is routed through it too, which makes migration easy.** — Setup is logger := slog.New(slog.NewJSONHandler(os.Stdout, nil)) followed by slog.SetDefault(logger). Output keys are time, level and msg. ([0:00](https://youtu.be/_mqB7LLgwgs?t=0))
- **The default level is Info, so Debug messages are silently dropped until the handler options set a lower level.** — The fix shown is passing handler options with Level set to Debug in place of nil when creating the JSON handler. ([1:19](https://youtu.be/_mqB7LLgwgs?t=79))
- **Loosely typed key/value pairs are easy to get wrong; a mismatched count shows up as a bad-key entry, and go vet flags it.** — The speaker shows a key with no value producing a BADKEY-style entry in the output and an error from go vet in the IDE. ([2:41](https://youtu.be/_mqB7LLgwgs?t=161))
- **Typed helpers such as String and Int catch type mistakes at compile time, and the strict LogAttrs call allows only typed attributes.** — Passing an integer to slog.String is a compile error. LogAttrs takes a context, a level, a message and typed attributes, so loose pairs are not accepted. ([3:58](https://youtu.be/_mqB7LLgwgs?t=238))
- **slog.Group nests related attributes under one key, producing a nested JSON object.** — The example groups a request key with a method attribute inside it. ([5:10](https://youtu.be/_mqB7LLgwgs?t=310))
- **A child logger created with With attaches shared attributes to every message it logs, which avoids repeating them in each call.** — The speaker moves a method attribute into the With call on a child logger and shows it appearing on both info and second messages. ([6:33](https://youtu.be/_mqB7LLgwgs?t=393))
- **WithGroup puts all later attributes under one named object while keeping time, level and msg at the top level.** — The speaker calls logger.WithGroup("info") and shows custom attributes nested under an info object. ([6:33](https://youtu.be/_mqB7LLgwgs?t=393))
- **slog separates a fixed logging front end from a replaceable handler backend, so switching libraries like zap or zerolog should only mean changing the handler.** — This is presented as one of slog's main design goals, which keeps the logging API consistent across dependencies that use different backends. ([7:55](https://youtu.be/_mqB7LLgwgs?t=475))

## Techniques
- **JSON logger as the process default** — logger := slog.New(slog.NewJSONHandler(os.Stdout, nil)); slog.SetDefault(logger). Existing slog.Info calls and legacy log calls then emit JSON. Remove the old log setup once migrated. *When:* Starting a Go service or migrating from the log package to structured logs with minimal call-site changes.
- **Set the minimum level through handler options** — Pass &slog.HandlerOptions{Level: slog.LevelDebug} as the second argument to slog.NewJSONHandler in place of nil. The video says slog.HandlerOptions with slog.Level debug; the default without this is Info. *When:* Debug messages are being dropped, or you need different verbosity per environment.
- **Typed attributes with helpers** — logger.Info("msg", slog.String("key1", "value1"), slog.Int("count", 2)). The video calls the helper slog.integer and slog.int in places; the Go standard library name is slog.Int. Loose pairs still compile but can go wrong at runtime. *When:* Any structured log call where field types should be enforced, such as IDs, durations and counts.
- **Strict logging with LogAttrs** — slog.LogAttrs(context.Background(), slog.LevelInfo, "msg", slog.String("key", "value")). The video calls this slog.logAttributes. Only typed attributes are accepted. *When:* You want the compiler to reject untyped attributes at every log call.
- **Nested objects with Group** — slog.Info("msg", slog.Group("request", slog.String("method", "GET"))) produces a request object containing method. *When:* Grouping related fields, such as HTTP request details, into one JSON object.
- **Child logger for shared fields** — child := logger.With(slog.String("method", "GET")); then child.Info(...) or child.LogAttrs(...). Every message from child includes method. *When:* A function or request handler where the same fields (request ID, method, tenant) should appear on every log line.
- **Group the custom fields under one key** — logger.WithGroup("info").Info("msg", slog.String("k", "v")). Defaults stay at top level; custom fields land under info. *When:* You want a fixed top-level schema for observability tools while keeping per-event fields in one object.
- **Keep call sites on slog and choose the backend in one place** — Write all logging against the slog front end and set the backend only where the handler is constructed. The video says switching from one third-party backend such as zap to zerolog should need only the handler change, though it does not show this. *When:* Dependencies or libraries in one codebase use different logging backends and you want a single API.

## Numbers
- slog was added to Go in version 1.21 and needs no install. ([0:00](https://youtu.be/_mqB7LLgwgs?t=0))
- Default slog level is Info; Debug messages are suppressed until handler options set Level to Debug. ([1:19](https://youtu.be/_mqB7LLgwgs?t=79))
- The presenter says slog can cut debug time 'from five hours to five minutes', a claim with no supporting data in the video. ([0:00](https://youtu.be/_mqB7LLgwgs?t=0))

## Hot takes
- The opening claim that slog takes debug time from five hours to five minutes is hype with no evidence shown.
- Calling slog a unified front end where handlers swap freely is presented as a major benefit, but the video demonstrates only the JSON handler and does not show swapping to zap or zerolog.
- The video frames slog's default-logger behavior as an easy migration path, which is useful, but it does not mention any caveats about legacy log flags or output formatting.

## Tools mentioned
Go (log/slog standard library, Go 1.21+), log (standard library, migrated to slog output via SetDefault), go vet, zap (Uber logging library, mentioned as a possible handler backend), zerolog (mentioned as a possible handler backend), IDE (unnamed, showing vet errors)

## Relevance to our work
- **agentos** (1/3): AgentOS is mainly a Rust proxy plus Python-style agent infra, so Go logging is only indirectly relevant. The L4 stack (Prometheus, OTel) is where structured logs would be consumed. → *If any Go helper or sidecar is added to AgentOS, use slog's JSON handler with a child logger carrying request IDs so logs can be parsed by the L4 observability stack.*
- **general** (1/3): Go logging basics are a small, cheap improvement across any Go code the user writes, and the talk covers the standard-library defaults. → *For any new Go service, start from slog.NewJSONHandler with SetDefault and use With for per-request fields instead of adding a third-party logger.*

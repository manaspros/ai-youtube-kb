# JSON logs in Python apps - with FastAPI & python-json-logger!

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `aJCK0LWz8kg` · [watch](https://youtu.be/aJCK0LWz8kg) · **date:** 2024-11-02 · **length:** 20:59 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack
- **topics:** observability, dev-tools · **tags:** python, logging, structured-logs, json-logs, fastapi, uvicorn, python-json-logger, better-stack, logtail, log-shipping, live-tail

> Tutorial on turning Python standard-library logs into JSON with python-json-logger in a FastAPI app, passing per-request fields via extra=, and shipping the logs to Better Stack with a Logtail handler.

## Summary
The video builds a small FastAPI app with two endpoints (list bands, get band by ID) and walks through making its Python logs structured. It starts from the default plain-text logging setup (a file handler and a Formatter with a format string), then adds custom fields (client IP, HTTP method, status code) by passing a dict through the logger's extra= argument. The key gotcha shown is that those extra keys are silently absent from the output until the formatter references them. Swapping the formatter for the JSON formatter from python-json-logger turns each record into JSON, and the extra keys then appear as top-level fields, and this works the same with a stream handler as with a file handler. The final section adds a Better Stack Logtail handler so the same records are shipped to a cloud log platform, where the extra keys become searchable fields and Live Tail can filter on values such as status code = 404. The content is a basic, reproducible tutorial for logging in Python, and the second half is tied to Better Stack's product.

## Key ideas
- **Default Python logs are plain text, which is hard to query and group by field.** — The speaker's motivation: plain-text lines need parsing before you can analyse them, while JSON gives you keys and values you can search centrally. ([0:00](https://youtu.be/aJCK0LWz8kg?t=0))
- **Custom log fields are passed with extra= and are dropped unless the formatter references them.** — After adding a dict of request data as extra=, the log line is unchanged. The fields only appear once they are named in the format string, which the speaker demonstrates with IP address, method and status code. ([7:17](https://youtu.be/aJCK0LWz8kg?t=437))
- **Swapping the formatter for the JSON formatter makes the whole record JSON, and extra keys become top-level fields.** — Only the formatter line changes (logging.Formatter becomes the JSON formatter from python-json-logger). The timestamp, level, message and extra keys all come out as JSON keys with no format string to maintain. ([9:27](https://youtu.be/aJCK0LWz8kg?t=567))
- **The JSON formatter is handler-agnostic.** — It works the same with a FileHandler (app.log) and a StreamHandler (stdout). The speaker switches handlers to show the JSON lines on stdout in the uvicorn terminal. ([10:30](https://youtu.be/aJCK0LWz8kg?t=630))
- **Logs can be shipped directly from the app with a Logtail handler, and extra keys are parsed into searchable fields automatically.** — The speaker creates a Better Stack Python source, takes its token, and adds a LogtailHandler to the same logger as the file and stream handlers. He says the platform picks the extra dict keys out automatically, and he prefers this to routing through Vector or Fluentd for this demo. ([11:43](https://youtu.be/aJCK0LWz8kg?t=703))
- **Keep the source token out of code.** — The speaker hard-codes the token for the demo but says a real application should read it from an environment file or a secret manager. ([13:09](https://youtu.be/aJCK0LWz8kg?t=789))
- **Status codes logged as extra fields let you filter request outcomes on the platform.** — For a lookup-by-ID endpoint, the speaker logs a 404 when no band matches and a 200 when one does, then filters Live Tail on status code = 404 and on not-equal-200. He says dashboards and alerts can be built on the same fields. ([18:44](https://youtu.be/aJCK0LWz8kg?t=1124))

## Techniques
- **Install python-json-logger and swap the formatter** — pip install python-json-logger in the venv (the command comes from the project's GitHub README). Import the JSON formatter object from the package's json logger module, which the captions garble, so check the README for the exact import path. In the logger setup, call handler.setFormatter(JsonFormatter()) in place of logging.Formatter(...). Nothing else in the setup changes. *When:* When a standard-library logging setup emits text lines and you want structured output without rewriting call sites.
- **Add per-request fields with extra= and let the formatter see them** — Build a dict such as data = {ip, method, status_code} and call logger.info('message', extra=data) (the speaker says the dict is passed through the extra keyword argument; the keys become attributes on the log record). The same keys must be referenced by the formatter: in the plain-text version, add %(key)s directives after the message; with the JSON formatter, they appear automatically. *When:* When log lines need request-scoped context (IP, method, status, IDs) that should be queryable later, not just embedded in the message string.
- **Logtail / Better Stack handler alongside local handlers** — In Better Stack, create a source with the Python platform and copy its source token. Install the Logtail Python package (the 'Logtail Python' pip install from the Better Stack docs), import LogtailHandler, instantiate it with the source token, and call logger.addHandler(...) next to the FileHandler and StreamHandler. Read the token from an env var or secret store, not from source code. *When:* When logs should be centralised and searchable on a hosted platform straight from the app, without a log shipper such as Vector or Fluentd in between.
- **Log outcome and return 404 from a lookup endpoint** — Search the list with next((b for b in bands if b['id'] == band_id), None). If the result is None, call logger.info('No band found with the given id', extra={status_code: 404, ...}) and raise HTTPException(status_code=404, detail='No band found'). Otherwise log with status_code 200 and return the band. The variable names in the speaker's code are band and band_id. *When:* When you want each endpoint's status to be a logged, filterable field rather than something you only see in the HTTP response.
- **Filter structured logs by field in Live Tail** — In the source's Live Tail, enter a search such as status code = 404, or status code != 200, and expand an entry to see the parsed extra fields. The speaker says dashboards and alerts can be built from the same fields. *When:* When you need to pull out a class of requests (errors, a status code range) from a live log stream without writing a parser.

## Numbers
- python-json-logger had about 1,600 GitHub stars when the video was made. ([0:00](https://youtu.be/aJCK0LWz8kg?t=0))
- The demo's hard-coded dataset has four bands, each with an id, name and genre. ([1:28](https://youtu.be/aJCK0LWz8kg?t=88))
- The demo uses Python 3.11 and a venv; the speaker says the concepts should work on other versions. ([2:40](https://youtu.be/aJCK0LWz8kg?t=160))
- Video length is 20:59. ([0:00](https://youtu.be/aJCK0LWz8kg?t=0))

## Hot takes
- The JSON formatting part is vendor-neutral, but the second half is a product walkthrough for Better Stack, and the shipping section is presented as the payoff. No sponsorship is labelled.
- The tutorial stops at the basics. It does not cover exception and traceback formatting, request or correlation IDs, or log volume and cost, which matter once this runs in production.
- The demo hard-codes the Better Stack source token in code. The speaker warns against this in one sentence but does not show the env-var or secret-store alternative.

## Tools mentioned
Python logging module, python-json-logger, FastAPI, Uvicorn, Better Stack (Logtail), Logtail Python handler, VS Code, venv, pip, Vector (mentioned as an alternative), Fluentd (mentioned as an alternative)

## Relevance to our work
- **agentos** (1/3): AgentOS has L4 observability planned around Prometheus, Grafana and OTel. This is a basic structured-logging pattern for the Python side of the stack, not a tracing or metrics approach. → *Where Python services log per-request decisions (budget checks, PII scan result, routing choice), pass them as extra= fields and confirm each key is referenced by the JSON formatter, since missing keys are silently dropped.*

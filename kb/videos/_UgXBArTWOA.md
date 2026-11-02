# Python QueueHandler & QueueListener - Offload Log Processing to Separate Thread | FastAPI demo

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `_UgXBArTWOA` · [watch](https://youtu.be/_UgXBArTWOA) · **date:** 2024-11-02 · **length:** 21:51 · **format:** tutorial · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Better Stack
- **topics:** observability, dev-tools · **tags:** python, logging, QueueHandler, QueueListener, SMTPHandler, threading, FastAPI, lifespan, uvicorn, async-logging

> Walkthrough: Python QueueHandler and QueueListener move slow log sinks like SMTP email onto a background thread, shown in FastAPI. Gotcha: stop the listener on shutdown or queued records are dropped.

## Summary
Better Stack shows how Python's logging.handlers QueueHandler and QueueListener keep slow log sinks off the request path. The motivating case is emailing admins on a critical error, which blocks the response for about two seconds. The speaker first wires a logger at CRITICAL level to an SMTPHandler, measures the blocking cost, then swaps it for a QueueHandler whose queue is drained by a QueueListener thread. The FastAPI section moves logger setup into logger.py, starts the listener at app startup and stops it in a lifespan context manager so queued records are not lost on shutdown. The demo is deliberately small (one handler, one endpoint, a free test SMTP host) and measures only single-request durations, not throughput or failure handling.

## Key ideas
- **Slow log handlers (email, network log shipping) block the thread that logs. Offloading them to a separate thread keeps web response times independent of that latency.** — Motivating example is emailing admins on a critical error from a Django or FastAPI service; the speaker says this is the case where the response would otherwise be delayed. ([0:00](https://youtu.be/_UgXBArTWOA?t=0))
- **Restrict the email handler by log level. Attaching it to a logger at CRITICAL level means only critical events generate mail, not every log line.** — The speaker explicitly warns that emailing every log entry would flood administrators; the level filter is the control. ([1:19](https://youtu.be/_UgXBArTWOA?t=79))
- **Measured cost of a direct SMTP handler: about 1.9 s for a trivial script and about 2.27 s for an endpoint response, all spent in the logger.critical call.** — Latency comes from the network round trip to the SMTP host, so it scales with the sink, not the log message. ([7:24](https://youtu.be/_UgXBArTWOA?t=444))
- **QueueHandler on the logger only enqueues records; QueueListener runs the real handlers on its own thread. The logging call returns almost immediately.** — After the change the script's duration prints as zero seconds, versus 1.9 s before. ([8:31](https://youtu.be/_UgXBArTWOA?t=511))
- **The listener must be stopped before the process exits, or records still on the queue are never processed.** — The speaker quotes the docs' point that leftover records will not be processed, so listener.stop() belongs in shutdown code. ([17:57](https://youtu.be/_UgXBArTWOA?t=1077))
- **In FastAPI, tie listener start and stop to the app lifecycle with a lifespan async context manager instead of relying on module import.** — Start happens before the app is built; code after yield (listener.stop()) runs when uvicorn shuts down; the function is passed as FastAPI(lifespan=...). ([16:41](https://youtu.be/_UgXBArTWOA?t=1001))
- **Split logging setup into its own module (logger.py) that defines the queue, the QueueHandler, and the listener; the app module imports the logger and only calls logger.critical in endpoints.** — The endpoint response duration fell from about 2.27 s to effectively zero after the change, verified in the browser with uvicorn --reload on localhost:8000. ([9:33](https://youtu.be/_UgXBArTWOA?t=573))
- **Verify asynchronous delivery by changing the recipient address to a new one and checking the test inbox after the request returns.** — The email arrives after the response, which is the observable proof that the work moved to the listener thread. ([20:06](https://youtu.be/_UgXBArTWOA?t=1206))

## Techniques
- **Level-gated SMTP alerting** — logger = logging.getLogger(__name__); logger.setLevel(logging.CRITICAL); create a Formatter with time, level and message; smtp = SMTPHandler with the SMTP host, from address, to address (a string or a list of admins), subject 'critical error in the application', secure=None (no TLS for the test host); smtp.setFormatter(formatter); logger.addHandler(smtp). *When:* Alerting humans on rare, unrecoverable failures. Never attach an email handler at INFO or DEBUG level.
- **QueueHandler + QueueListener offload** — log_queue = queue.Queue(); queue_handler = QueueHandler(log_queue); logger.addHandler(queue_handler) (remove the direct SMTP addHandler); listener = QueueListener(log_queue, smtp_handler); listener.start(); ... listener.stop() before exit. Logging calls now only enqueue. *When:* Any handler that does network I/O (email, remote log shipping, webhooks) that runs on a request path where response latency matters.
- **Lifespan-managed listener for FastAPI** — Create the listener in the logger module and call listener.start() before building the app. Define @asynccontextmanager async def lifespan(app): yield, with listener.stop() after the yield. Build the app with app = FastAPI(lifespan=lifespan). Import the logger and listener from logger.py in main.py and call logger.critical from endpoints. Run with: uvicorn main:app --reload (localhost:8000). *When:* ASGI web services where a server restart must not silently drop queued log records.
- **Module split for logging config** — Move all logger, handler, queue and listener setup into logger.py; keep endpoints in main.py and import the configured logger. Remove the per-file logger creation from application code. *When:* Apps with more than one module logging, so configuration lives in one place.
- **Quick before/after latency check** — Record start = time.time() at the top of the endpoint and return {'duration': time.time() - start} after the logger.critical call. Swap the handler, reload, and compare the returned durations. *When:* Verifying that a logging change removed blocking latency, without a profiler.

## Numbers
- Trivial script with a direct SMTP handler on one critical log call took about 1.9 s; the speaker puts the email send latency at nearly two seconds. ([6:05](https://youtu.be/_UgXBArTWOA?t=365))
- Email send latency with direct SMTP handler described as 'nearly two seconds'. ([7:24](https://youtu.be/_UgXBArTWOA?t=444))
- FastAPI endpoint response with direct SMTP handler took 2.27 s. ([15:29](https://youtu.be/_UgXBArTWOA?t=929))
- Script duration after switching to QueueHandler/QueueListener printed as zero seconds. ([12:08](https://youtu.be/_UgXBArTWOA?t=728))
- FastAPI endpoint duration after the queue change: zero, with 'minuscule' latency; the email for the new address arrived after the response. ([18:53](https://youtu.be/_UgXBArTWOA?t=1133))

## Hot takes
- The speedup is shown only for one trivial endpoint with a single handler against a free remote test SMTP host; there is no throughput, load, or failure-case measurement.
- The demo logs at critical and returns normally, while the speaker himself notes critical usually means the app cannot proceed and should exit. The demo does not follow that advice.
- Not covered: what happens when a handler on the listener thread raises, queue size limits or backpressure, and whether multiple listeners or processes are needed. Treat those as open questions.

## Tools mentioned
Python logging (logging.handlers: SMTPHandler, QueueHandler, QueueListener), Python queue module, contextlib asynccontextmanager (called 'context lib' in transcript), FastAPI (lifespan parameter), uvicorn (main:app, --reload), time module, VS Code, a free SMTP test service (unnamed in transcript)

## Relevance to our work
- **agentos** (1/3): L4 observability and gateway logging: any network-bound log or alert sink on the proxy request path would block responses; the queue pattern addresses that, but this video only covers stdlib logging in a single FastAPI app. → *When adding alerting or remote log sinks to the Govrix proxy or any FastAPI service, route them through QueueHandler + QueueListener and call listener.stop() in the app's lifespan shutdown.*

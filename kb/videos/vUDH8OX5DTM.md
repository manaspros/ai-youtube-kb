# Fastify Application Development | Logging with Pino.js

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `vUDH8OX5DTM` · [watch](https://youtu.be/vUDH8OX5DTM) · **date:** 2024-11-02 · **length:** 20:45 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, Fastify
- **topics:** observability, dev-tools · **tags:** fastify, pino, logging, structured-logs, better-stack, logtail, nodejs, npm, nodemon, esm, plugins, log-transports

> Beginner tutorial on building a small Fastify API in Node.js, configuring its built-in Pino logger, and shipping the logs to Better Stack through a Pino transport.

## Summary
The video builds a four-route-or-so Fastify API serving synthetic band data, starting from npm init, a dev script with nodemon, and "type": "module" for ESM imports. It shows that Fastify ships with Pino logging, enabled by passing logger: true, and how to move routes into a registered plugin. Inside a handler, the reply object exposes the Pino logger, which the speaker uses to log an error before returning a 404 for a missing ID. The logger is then configured with a level and a file destination, and finally pointed at Better Stack via the @logtail/pino transport. The last section shows fanning logs out to multiple targets (Better Stack plus stdout via pino/file) and filtering hosted logs by response status code. Substance is basic and the walkthrough is tied to one vendor's platform.

## Key ideas
- **Fastify ships with Pino logging built in; passing logger: true when constructing the app gives JSON logs with no extra packages.** — The default logger is Pino, and the speaker notes the output is JSON with level and timestamp fields. Output starts as soon as the server runs. ([0:00](https://youtu.be/vUDH8OX5DTM?t=0))
- **Node needs "type": "module" in package.json before import statements work in server.js.** — Without it, Node errors on the import statement. The default is CommonJS with require. This setting is an easy first-run failure to hit. ([3:56](https://youtu.be/vUDH8OX5DTM?t=236))
- **Routes can be moved into a Fastify plugin: an exported async function taking the instance and options, registered with fastify.register.** — The speaker moves the bands route into routes.js and registers it from server.js. The behavior is unchanged afterward, which makes it a basic route-organization pattern. ([6:37](https://youtu.be/vUDH8OX5DTM?t=397))
- **Handlers can log through reply.log, which exposes the Pino logger from the reply object.** — The speaker calls reply.log.error when an ID is not found, then returns reply.status(404).send with a message. The error line is what later reaches the hosted log platform. ([9:30](https://youtu.be/vUDH8OX5DTM?t=570))
- **Logger behavior is set by passing an options object instead of true: level filters output below the threshold, and a file key redirects output to a file.** — Setting the level to warn hides info-level (30) lines. The speaker sets file to server.log, and JSON output moves from the console to that file. The speaker shows this config as working in the demo. ([12:04](https://youtu.be/vUDH8OX5DTM?t=724))
- **Logs go to Better Stack by adding the Logtail Pino transport to the logger config with a sourceToken option.** — The speaker creates a Node.js source in Better Stack, copies its token, installs the transport package, and sets the logger transport target. Error-level logs from 404 handlers then appear in live tail. ([15:56](https://youtu.be/vUDH8OX5DTM?t=956))
- **The speaker hardcodes the source token in server.js and then warns that tokens should live in an environment file, not in source control.** — The warning is given in passing during the source-creation step, before the hardcoded config. Treat the demo code as illustrative only. ([14:41](https://youtu.be/vUDH8OX5DTM?t=881))
- **A transport config can take a targets array to send one Pino stream to several destinations, such as Better Stack plus stdout via pino/file.** — Each array entry is a target object with its own options. pino/file defaults to standard output. The speaker shows logs still reaching both the terminal and the hosted live tail. ([18:37](https://youtu.be/vUDH8OX5DTM?t=1117))
- **Once logs are central, you can filter on structured fields such as response status code to find all 404 requests.** — The speaker searches the status code property on the response object in Better Stack. The point is that structured fields make cross-request questions cheap to answer, compared with grepping files on several servers. ([17:18](https://youtu.be/vUDH8OX5DTM?t=1038))

## Techniques
- **Fastify app bootstrap with ESM and nodemon** — npm init -y; npm install fastify; add "type": "module" to package.json; npm install nodemon; add scripts.dev = "nodemon server.js"; run npm run dev. Nodemon restarts the server when files change. *When:* Starting any small Node API where you want ES module imports and a save-to-restart loop.
- **Enable Pino logging in Fastify by config object** — const fastify = Fastify({ logger: true }) for defaults. For control, pass an object, e.g. { logger: { level: 'info' } }. Levels follow Pino naming (debug, info, warn, error). Setting a file key sends output to that file in the demo. *When:* Any Fastify service that needs structured JSON logs without adding a logging library.
- **Log from inside a route with reply.log** — Inside the handler: if a lookup finds nothing, call reply.log.error(`no band with id ${id}`), then return reply.status(404).send({ message: ... }). Otherwise send the record with reply.send(band). *When:* Logging domain-level events (not found, bad input) alongside the response, so the log line and the status code come from one request.
- **Route extraction into a plugin** — In routes.js: export default async function routes(fastify, options) { fastify.get('/bands', ...); fastify.get('/bands/:id', async (request, reply) => { const id = request.params.id; ... }) }. In server.js: fastify.register(routes). *When:* Splitting a growing Fastify app into modules, one plugin per resource.
- **Ship Fastify logs to Better Stack via the Logtail Pino transport** — npm install @logtail/pino. Create a Node.js source in Better Stack and copy its source token. Set the logger config to { transport: { target: '@logtail/pino', options: { sourceToken: '<token>' } } }. Load the token from an env file or secret store in real use. Restart and watch Live tail. *When:* You want one hosted place to search logs from several services, and a Pino transport fits the stack.
- **Fan out logs to multiple transports** — Replace the single transport with transport: { targets: [ { target: '@logtail/pino', options: { sourceToken: '<token>' } }, { target: 'pino/file' } ] }. pino/file with no destination writes to stdout. *When:* You need the hosted log platform and local terminal output from the same logger, without changing call sites.
- **Search hosted logs by a structured field** — In Better Stack Live tail, search for the response object's status code property, e.g. 404, to list matching requests with their level, message and host fields. *When:* Finding error patterns (such as a page or route that keeps returning 404) across request logs.

## Numbers
- Pino info-level lines have numeric level 30 and error-level lines have level 50 in the JSON output. ([12:04](https://youtu.be/vUDH8OX5DTM?t=724))
- Filtering hosted logs by the response status property 404 returns every completed request with that status (demo result, no volume figures given). ([17:18](https://youtu.be/vUDH8OX5DTM?t=1038))

## Hot takes
- The whole walkthrough is built around one vendor's platform (Better Stack, which runs the channel), and the transport choice is that vendor's package. Pino transports are pluggable, so other destinations would need a different target. No alternatives are compared.
- The demo hardcodes the source token in server.js right after saying tokens must not be committed. Read it as a demo shortcut, not a pattern to copy.
- Beginner-level content: no discussion of production concerns such as log volume, cost, sampling, redaction of PII, or async transport failure behavior.

## Tools mentioned
Fastify, Node.js, npm, Pino (Fastify's default logger), @logtail/pino (Better Stack Logtail Pino transport), nodemon, Better Stack (log platform, Live tail and search), VS Code

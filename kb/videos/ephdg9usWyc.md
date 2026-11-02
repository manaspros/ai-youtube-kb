# fluentd Data Collector | Collecting, Transforming and Routing Log Events

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `ephdg9usWyc` · [watch](https://youtu.be/ephdg9usWyc) · **date:** 2024-11-02 · **length:** 24:34 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, Fluentd project, Calyptia, Apache Software Foundation, Canonical (Ubuntu)
- **topics:** dev-tools, observability · **tags:** fluentd, log-shipping, log-redaction, apache, better-stack, logtail, log-parsing, linux

> Hands-on Fluentd tutorial: tail an Apache access log, parse it to JSON, strip a field, and ship it to Better Stack. Solid practical config walkthrough with a vendor-flavored destination.

## Summary
The video walks through installing Fluent Package (the stable Fluentd distribution) on Ubuntu 22.04 and verifying it, then explains Fluentd's pipeline model: sources collect events, filters transform them, and match blocks route them to destinations. It builds a working config that tails the Apache access log, uses a built-in apache2 parser to turn plain text into JSON, and first prints to stdout using a dry-run check before switching the output to Better Stack via the LogTail plugin. It then adds a record_transformer filter that removes the host field, and shows field-based searches (for example, status code 404 or not 200) in the Better Stack live tail. The talk is a vendor-flavored but reproducible tutorial; it covers the core config model and a practical redaction example, and it skips error handling, multi-host deployment, and performance.

## Key ideas
- **Fluentd is a log shipper modeled as a pipeline: collect from many sources, normalize into a standard event format, filter or enrich, then forward to one or more destinations.** — The speaker frames Fluentd as a unified logging layer. Sources can be Apache logs, app logs, syslog, auth logs, or database messages. Destinations named include MongoDB, MySQL, S3 and Better Stack. ([0:00](https://youtu.be/ephdg9usWyc?t=0))
- **The config file is organized into source, filter and match blocks, and tags are what connect them.** — Source blocks read data and attach a tag. Filter blocks transform events by tag. Match blocks send events to destinations, and the match pattern is a regex-style match against the tag. ([5:27](https://youtu.be/ephdg9usWyc?t=327))
- **The tail input needs a pos_file so Fluentd remembers its read offset across restarts.** — The pos_file gives Fluentd a small amount of state so it does not re-send data it already read. The speaker says the docs call this highly recommended. The example stores it under a td-agent directory in /var/log. ([9:15](https://youtu.be/ephdg9usWyc?t=555))
- **A parse block turns unstructured text into structured JSON, which is what makes later field search and filtering possible.** — Fluentd ships built-in parsers for apache2, apache error, nginx, syslog, csv, json, and a regex parser for custom formats. Once the Apache access log is parsed, each request becomes keys and values such as status code, user agent, method and path. ([10:40](https://youtu.be/ephdg9usWyc?t=640))
- **Validate config with a dry run before starting, and stop the systemd daemon first when running Fluentd by hand.** — The dry-run flag checks the config without moving any logs. The speaker stops the installed systemd unit so the manually started process is the only one tailing the file. ([13:23](https://youtu.be/ephdg9usWyc?t=803))
- **Switching destinations means installing a plugin and dropping in a per-source token, and the rest of the pipeline stays the same.** — The LogTail plugin is installed with the fluent gem command using sudo. The match block changes its type to the LogTail output and adds the source token copied from the Better Stack source's configure page. Sources and filters are unchanged. ([15:53](https://youtu.be/ephdg9usWyc?t=953))
- **Redaction is done in-pipeline with a record_transformer filter that removes keys before forwarding.** — The speaker removes the host key from the parsed records. Other fields such as agent and status code are kept. The filter sits between the source and the match block and is matched by tag. The transcript notes that the same approach can mask email or IP addresses. ([20:04](https://youtu.be/ephdg9usWyc?t=1204))

## Techniques
- **Install Fluent Package on Ubuntu and verify** — Use the Fluent Package curl installer from the Fluentd docs for your Ubuntu release. The speaker uses Ubuntu jammy (22.04 LTS) and notes a focal (20.04) link as an alternative. Verify with `fluentd --version`, which reports Fluent Package 5.0.2 in the video. Fluent Package is recommended over Calyptia's Fluentd distribution for stability because the core is a Ruby daemon with C-accelerated parts. *When:* Setting up a log shipper on a Linux host and wanting the stable distribution.
- **Minimal tail source with pos_file and tag** — Config snippet in /etc/fluent/fluentd.conf (the speaker empties the default file first with truncate, then edits it with nano):
<source>
  @type tail
  path /var/log/apache2/access.log
  pos_file /var/log/td-agent/access.log.pos
  tag betterstack.apache.access
  <parse>
    @type apache2
  </parse>
</source>
Note: the speaker says 'type' on screen; Fluentd's syntax is @type. The Apache directory is spoken as 'Apache 2'; the path shown is the standard Ubuntu location. Confirm both on your system. *When:* Tailing a growing file (access logs, app logs) and converting it to structured records.
- **Stdout-first validation before wiring a remote destination** — Add a match block for the tag with `@type stdout`, run `fluentd --dry-run` to validate, then run fluentd and refresh the page or generate requests. Confirm parsed JSON appears in the terminal before changing the output. *When:* Checking a new parser or source without risking a bad remote destination.
- **Remote destination with LogTail plugin** — Install the LogTail plugin with the fluent gem command as root (the speaker used sudo). Create the source in the Better Stack Logs & Metrics UI, copy its token from the Configure section, then replace the stdout match block with:
<match betterstack.**>
  @type logtail
  <token parameter from the source>
</match>
The token parameter name is shown on screen but not spoken; check the plugin docs. Dry-run, restart Fluentd, and confirm events appear in live tail. *When:* Sending parsed logs to a hosted log platform.
- **Redact fields with record_transformer** — Add a filter block between source and match, matched by the same tag:
<filter betterstack.**>
  @type record_transformer
  remove_keys host
</filter>
Run the dry-run check, restart, and confirm the field is missing from new records. The speaker says the same approach works for other sensitive fields, such as email or IP addresses. *When:* Removing PII or internal host details before logs leave the machine.
- **Field search on structured logs** — In the destination UI, click a field such as code (HTTP status) in the search bar and filter on values, for example equals 404 or not equal to 200. The speaker says searches on parsed fields are what make centralized logs useful. *When:* Triage on structured HTTP access logs after parsing.
- **Operate by tag, not by file** — Give each source its own tag and route with match or filter patterns. Add more sources (syslog, nginx, app logs, Docker) to the same config and send them to the same or different destinations. *When:* Running several log sources through one shipper.

## Numbers
- Fluent Package version 5.0.2 reported by `fluentd --version` after install ([2:05](https://youtu.be/ephdg9usWyc?t=125))
- Target OS is Ubuntu 22 jammy, described as the LTS at the time of recording; Ubuntu focal (20) also supported by the installer ([2:05](https://youtu.be/ephdg9usWyc?t=125))
- Default fluentd.conf is truncated to 0 bytes before writing the new config ([7:55](https://youtu.be/ephdg9usWyc?t=475))
- No benchmarks, throughput, or cost figures are given ([0:00](https://youtu.be/ephdg9usWyc?t=0))

## Hot takes
- Vendor-flavored tutorial: the only destination demonstrated is Better Stack, and the Better Stack UI is used for the search and live-tail payoff. The Fluentd parts are reusable, but the destination steps are product-specific.
- Recommends Fluent Package over the core Ruby daemon for stability, citing installation difficulty for some users with Ruby daemons.
- Teaches a practical redaction pattern (record_transformer remove_keys) in the same pipeline, rather than in the app or at the destination.
- Several details are spoken without the exact syntax on screen (the directive is spoken as 'type' but Fluentd uses @type; the LogTail parameter name and gem name are not spoken). Check the docs before copying snippets.
- Does not cover failure modes such as buffering, retries, backpressure, or multi-host setups.

## Tools mentioned
Fluentd, Fluent Package 5.0.2, Calyptia Fluentd, td-agent (named as the pos_file directory), Better Stack Logs, LogTail (Fluentd output plugin for Better Stack), Apache HTTP Server (apache2 parser), Ubuntu 22.04 LTS (jammy), systemctl, truncate, nano, fluent-gem, Vector (referenced as a comparison video, not demonstrated), MongoDB, MySQL, Amazon S3 (mentioned as possible destinations)

## Relevance to our work
- **agentos** (1/3): The tail + pos_file + tag routing model is a small, reusable pattern for shipping logs from the L1 proxy and other services. The profile's L4 observability plan is Prometheus/OTel, so this is an alternative, not a core change. → *When you wire log shipping for the Govrix proxy or other AgentOS services, check the pos_file checkpoint and tag-routing pattern against the OTel collector before choosing a log shipper.*

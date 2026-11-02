# How To Start Logging With MySQL

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `4nrbbGiG0x4` · [watch](https://youtu.be/4nrbbGiG0x4) · **date:** 2024-11-02 · **length:** 18:27 · **format:** tutorial · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Better Stack
- **topics:** observability, dev-tools · **tags:** mysql, logging, slow-query-log, general-log, binary-log, error-log, log-centralization, alerting, vector, better-stack, mysqldumpslow, ubuntu

> Walkthrough of MySQL's four log types (error, general, slow query, binary) on Ubuntu, then shipping them and server metrics to Better Stack with a slow-query anomaly alert.

## Summary
The presenter explains the four MySQL log types and where each lives on a Linux server: the error log (startup, shutdown and runtime diagnostics), the general query log (connects, disconnects and every query, off by default), the slow query log (queries over a configurable time), and the binary log (data-changing events used for replication and restore). Each is enabled or tuned either at runtime with SET GLOBAL or persistently in my.cnf under [mysqld], followed by a service restart. The slow log is verified with SLEEP(1) versus SLEEP(3) against a 2-second threshold, and mysqldumpslow is used to summarize it. The second half sets up Better Stack: a MySQL log source, a read-only metrics user, the Better Stack MySQL exporter, and Vector to forward logs. It then shows Live Tail, a MySQL dashboard template, and an automatic anomaly alert on slow queries per second. The content is generic MySQL operations with a vendor product walkthrough for the centralization half; nothing is AI-specific.

## Key ideas
- **The error log is the first place to look when MySQL won't start or is misbehaving, but it always contains startup and shutdown messages, so entries alone do not indicate a fault.** — Default path on Ubuntu is /var/log/mysql/error.log. Each line carries timestamp, thread id, label, error code, subsystem and message. The verbosity is set with log_error_verbosity: 1 logs errors only, 2 (default) errors and warnings, 3 adds informational messages. The presenter recommends keeping the default. ([0:52](https://youtu.be/4nrbbGiG0x4?t=52))
- **The general query log records every connect, disconnect and received SQL statement, which makes it the best tool for seeing exactly what a client sent. It is off by default.** — It is a debugging log rather than a performance log. The speaker notes it does not map one-to-one to commands the user typed: session init statements and server-restart commands also appear. ([2:14](https://youtu.be/4nrbbGiG0x4?t=134))
- **The slow query log captures only queries that exceed a configurable threshold, which makes it the practical way to find queries worth optimizing.** — Threshold is long_query_time in seconds (demo uses 2; the speaker suggests raising it if normal queries already take around 2 seconds). Log rows show query time, rows sent and rows examined. ([8:23](https://youtu.be/4nrbbGiG0x4?t=503))
- **The binary log stores data-modifying events (for example CREATE, DELETE even with no matched rows) and not reads; it serves replication and point-in-time recovery, and it is not meant to be read by hand.** — Use SHOW BINARY LOGS and SHOW VARIABLES LIKE 'log_bin' to list files and locate them. Files are in /var/lib/mysql, with an index file. ([10:51](https://youtu.be/4nrbbGiG0x4?t=651))
- **Local log files are hard to monitor at scale, so the presenter ships them to a hosted log service and gets metrics from the same server.** — Setup uses a Better Stack source with its token, a dedicated read-only metrics user instead of root, the Better Stack MySQL exporter script, and a Vector install script that wires up the logs. Live Tail then shows entries as they arrive. ([13:11](https://youtu.be/4nrbbGiG0x4?t=791))
- **A built-in MySQL dashboard template with anomaly-based alerting on slow queries per second catches regressions without hand-written thresholds.** — The alert compares the current rate against a moving average and can notify by email, SMS or Slack. The presenter says percentage-change and fixed-threshold rules are also available. ([16:53](https://youtu.be/4nrbbGiG0x4?t=1013))

## Techniques
- **Enable general log at runtime** — Run `SHOW VARIABLES LIKE 'general%';`, then `SET GLOBAL general_log = 'ON';` and `SET GLOBAL general_log_file = '/var/log/mysql/general.log';`. The file must be writable by the mysql user. *When:* Temporary debugging of what a client actually sent, without a restart.
- **Enable logs persistently in my.cnf** — Edit /etc/mysql/my.cnf (sudo nano). Under [mysqld] add: general_log = 1, general_log_file = /var/log/mysql/general.log, slow_query_log = 1, slow_query_log_file = /var/log/mysql/slow.log, long_query_time = 2. Then `sudo systemctl restart mysql.service`. *When:* Logs that must survive restarts; the config-file method is the one the presenter prefers for clarity.
- **Slow query log threshold check** — Run `SELECT SLEEP(1);` (not logged) and `SELECT SLEEP(3);` (logged at long_query_time = 2). Then inspect the file with `sudo mysqldumpslow /var/log/mysql/slow.log`. *When:* Confirming the threshold works and summarizing slow queries in readable form.
- **Locate binary logs** — Inside the mysql client: `SHOW BINARY LOGS;` and `SHOW VARIABLES LIKE 'log_bin';` (the log_bin_index and base name show the path, /var/lib/mysql). Do not parse them by hand. *When:* Before recovery or replica setup, to know which files to keep.
- **Ship MySQL logs and metrics to Better Stack** — In Better Stack, go to Logs > Sources > Connect source, choose platform MySQL, and copy the source token. Follow the docs' logs-and-metrics option: create a dedicated monitoring user (named BetterStackMetrics in the video) with a password of your own, run the provided exporter install script, then run the Vector install command with the token substituted (chosen OS: Ubuntu). Verify in Live Tail. *When:* Central log search and dashboards without SSH-ing into each server.
- **Dashboard template plus anomaly alert** — In Better Stack: Dashboards > Create dashboard > search the MySQL template > Add. The template comes with an automatic alert on slow queries per second. Adjust the rule to a percentage change or a fixed threshold, and route it to email, SMS or Slack. *When:* Detecting a sudden rise in slow queries without writing your own detector.

## Numbers
- log_error_verbosity default is 2 (errors and warnings); 1 = errors only, 3 = adds informational messages. ([2:14](https://youtu.be/4nrbbGiG0x4?t=134))
- Demo slow-query threshold: long_query_time = 2 seconds; SLEEP(1) is not logged, SLEEP(3) is. The speaker suggests a higher threshold, around 4, if normal queries already take about 2 seconds. ([8:23](https://youtu.be/4nrbbGiG0x4?t=503))
- Demo buffer pool size is 128 MB, and the server had been up for 49 seconds at the time of the dashboard screenshot. ([16:53](https://youtu.be/4nrbbGiG0x4?t=1013))
- Better Stack's free tier is mentioned as the starting point (no pricing given). ([13:11](https://youtu.be/4nrbbGiG0x4?t=791))

## Hot takes
- Quality capped at 3, not 4: the centralization half is a walkthrough of one vendor's product, with a free-account pitch, but the local-log half is accurate, practical and reproducible.
- Not AI-related; relevant to our observability layer, not to agent-specific design.
- The general query log is presented as a debugging tool and the speaker does not discuss its overhead or retention, which matters on busy production servers.
- Anomaly-based alerting on slow queries per second is presented as an automatic default, with no discussion of false positives or tuning.

## Tools mentioned
MySQL server (version not stated), mysql command-line client, Ubuntu, systemctl, less / cat / nano, mysqldumpslow, Better Stack (logs, Live Tail, dashboards, alerts), Vector, Better Stack MySQL exporter

## Relevance to our work
- **agentos** (1/3): L4 observability and L3 storage: the slow-query threshold plus anomaly alert pattern applies to Postgres or ClickHouse latency monitoring, though the video covers MySQL only. → *When wiring slow-query monitoring for the Postgres/pgvector or ClickHouse tiers, copy the pattern: a threshold log (long_query_time-style), a summary tool, and an anomaly alert on slow-query rate, then check it with a deliberately slow query.*

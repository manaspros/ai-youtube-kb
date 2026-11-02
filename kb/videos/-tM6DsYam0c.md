# Logrotate - Log Management on Linux Servers

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `-tM6DsYam0c` · [watch](https://youtu.be/-tM6DsYam0c) · **date:** 2024-11-02 · **length:** 27:16 · **format:** tutorial · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Better Stack
- **topics:** dev-tools, observability · **tags:** logrotate, linux, log-management, cron, copytruncate, compression, apache, heartbeat-monitoring, sysadmin, ubuntu

> Practical walkthrough of logrotate on Ubuntu: per-service configs, create vs copytruncate, compression, scheduling via cron, and a heartbeat curl in postrotate to alert when rotation stops.

## Summary
The presenter explains logrotate as the standard Linux tool for rotating, compressing and deleting growing log files, and notes it is preinstalled and usually runs as a daily cron job. He walks through the global /etc/logrotate.conf (weekly default, keep four rotations, include /etc/logrotate.d) and then a per-service Apache 2 block with daily rotation, rotate 14, compression, delaycompress, notifempty and pre/post-rotate hooks. He contrasts the default create strategy (rename, then start a new empty file) with copytruncate (copy, then truncate the original), and says copytruncate can lose a brief window of log lines. A live demo shows forced rotations with logrotate --force against the Apache config, including the delaycompress effect and rotation count pruning. The video then shows how to move the logrotate script from cron.daily to cron.hourly, and how to add a curl to a heartbeat URL in postrotate so a monitoring service alerts if rotation stops. The content is basic-to-intermediate sysadmin material aimed at Debian and Ubuntu, with the final section tied to Better Stack's own heartbeat product.

## Key ideas
- **Logrotate is preinstalled on Ubuntu and most mainstream distros and is the standard way to stop log files from filling disks.** — It rotates on a schedule or when a file exceeds a size, compresses old logs, deletes old backups, and can optionally mail logs. It normally runs as a daily cron job. ([0:00](https://youtu.be/-tM6DsYam0c?t=0))
- **Global defaults live in /etc/logrotate.conf, and per-service rules live in /etc/logrotate.d/.** — The global file sets defaults (weekly schedule, rotate 4, create, root user and admin group) and includes /etc/logrotate.d. Each service gets its own file, such as apache2 or rsyslog, so each can have its own retention. ([4:29](https://youtu.be/-tM6DsYam0c?t=269))
- **Each config block targets a log path glob and can apply to several paths at once.** — The Apache example uses /var/log/apache2/*.log. The rsyslog example applies one block to multiple paths such as /var/log/messages and /var/log/debug. ([7:09](https://youtu.be/-tM6DsYam0c?t=429))
- **Create and copytruncate are the two rotation strategies, and the choice is about whether the app can reopen its log file.** — Create renames the live file and makes a new empty one, which is the default. Copytruncate copies the file and then empties the original so the app can keep writing to the same handle. The speaker warns that copytruncate may drop a brief window of log lines and says this is usually acceptable for apps that don't need continuous analysis. ([11:15](https://youtu.be/-tM6DsYam0c?t=675))
- **delaycompress keeps the most recent rotated file uncompressed and compresses older ones.** — The first rotation is left as plain text so the newest backup is quick to read. In the demo, the older file went from 1802 bytes to 291 bytes after gzip. ([18:42](https://youtu.be/-tM6DsYam0c?t=1122))
- **The rotate count sets retention, and the oldest backup is deleted once the limit is exceeded.** — With rotate 2 and daily runs, the oldest file is removed on each new rotation and the newest files shift up. The demo uses rotate 2 for a two-day window instead of the configured 14. ([20:05](https://youtu.be/-tM6DsYam0c?t=1205))
- **Cron frequency is changed by moving the logrotate script into a different cron.* directory.** — The default script sits in cron.daily. Moving it to cron.hourly makes it run every hour, which matters if the config uses hourly-level rotation. ([21:28](https://youtu.be/-tM6DsYam0c?t=1288))
- **A postrotate curl to a heartbeat URL turns silent failure of rotation into an alert.** — The speaker adds a plain curl GET to the Better Stack heartbeat URL after the existing if block in postrotate. The heartbeat is expected hourly with a 5-second grace period, and escalation can use phone, SMS, email or push. ([24:10](https://youtu.be/-tM6DsYam0c?t=1450))

## Techniques
- **Check the installed logrotate version and defaults** — Run `logrotate --version` (3.19 in the demo). Then read /etc/logrotate.conf to see the global schedule (weekly), `rotate 4`, the `create` default, the commented-out `dateext` and `compress` options, and the `include /etc/logrotate.d` line. *When:* On a new server, before adding service-specific rules, to confirm the defaults that apply to every log without its own block.
- **Per-service rotation block in /etc/logrotate.d/** — Create one file per service with a block that starts with the log path glob, then `{`. Inside, set `daily`, `missingok`, `rotate 14`, `compress`, `delaycompress`, `notifempty`, optional owner and permission options, and `prerotate` / `postrotate` hooks ending in `endscript`. The demo's Apache file is /etc/logrotate.d/apache2 targeting /var/log/apache2/*.log. *When:* When a service writes to a predictable directory and needs its own retention, compression or hooks. Logs are kept per service so retention can differ.
- **Choose the rotation strategy per app** — Keep the default `create` for apps that reopen their log file or reload on signal. For apps that keep the file open and cannot reopen it, add the `copytruncate` directive, which copies the file and then truncates the original in place. *When:* Use copytruncate when you cannot signal or restart the app. Accept the possibility of a small gap in log lines during the copy.
- **Force a rotation to test a config** — Run `sudo logrotate --force` pointed at a single config file, e.g. `/etc/logrotate.d/apache2`. Then `ls` the log directory to confirm the live file is now zero bytes and a .1 file exists. Run it again to see compression and rotation-count pruning. *When:* After editing a rotation config, or to check retention and compression without waiting for the cron schedule.
- **Run logrotate hourly instead of daily** — Move the logrotate script from cron.daily to cron.hourly, e.g. `sudo mv /etc/cron.daily/logrotate /etc/cron.hourly/`. Verify with `ls` in the target directory. *When:* When the rotation policy needs an hourly cadence, such as high-volume logs, and the per-service config is written to match.
- **Heartbeat alert on successful rotation** — In the service's postrotate block, after the existing commands, add a `curl` GET to the monitoring service's heartbeat URL. Set the heartbeat's expected interval to match the cron cadence (hourly in the demo) and a small grace period (5 seconds in the demo). Route escalation to on-call channels. *When:* When missed rotations would go unnoticed, for example if the disk fills and rotation silently stops.

## Numbers
- logrotate version 3.19 on the demo Ubuntu machine ([3:26](https://youtu.be/-tM6DsYam0c?t=206))
- Global default is a weekly schedule with rotate 4, so four weeks of backlogs are kept ([4:29](https://youtu.be/-tM6DsYam0c?t=269))
- Apache demo config is daily with rotate 14, a 14-day retention window ([7:09](https://youtu.be/-tM6DsYam0c?t=429))
- Demo lowers retention to rotate 2 for a two-day window ([16:12](https://youtu.be/-tM6DsYam0c?t=972))
- Gzip shrank a rotated access.log from 1802 bytes to 291 bytes, about 84% smaller (computed from the two numbers) ([18:42](https://youtu.be/-tM6DsYam0c?t=1122))
- Heartbeat expected hourly with a 5-second grace period ([24:10](https://youtu.be/-tM6DsYam0c?t=1450))

## Hot takes
- copytruncate can silently drop log lines written between the copy and the truncate, which the speaker accepts for apps without continuous log analysis.
- The final section is a Better Stack product demo (heartbeats), so it is a light vendor tie-in. The postrotate curl pattern itself is not specific to that vendor, but the video only shows Better Stack.
- Config paths and cron directories are Debian and Ubuntu specific (/var/log/apache2, /etc/cron.hourly). The speaker says so only implicitly, so a RHEL-family server will differ.

## Tools mentioned
logrotate 3.19, cron (cron.daily, cron.hourly), Apache 2 (apache2), rsyslog, UFW, gzip / gunzip, mail, nano, tmux, curl, Better Stack Heartbeats, Ubuntu

## Relevance to our work
- **agentos** (1/3): AgentOS's self-hosted services (vLLM, Ray Serve, Postgres, Redis, the Rust proxy) will write logs that grow on one RTX 5090 box. Logrotate with per-service copytruncate or create rules is the basic hygiene that keeps those files from filling the disk. → *Audit the log directories of the AgentOS self-hosted services and add /etc/logrotate.d entries per service, using copytruncate for any process that cannot reopen its log file.*
- **prosharness** (1/3): ProsHarness runs loops and schedules around the Claude Code CLI. A scheduled run that stops silently is a real failure mode, and a dead-man heartbeat is a cheap way to detect it. → *Give each ProsHarness scheduled loop a heartbeat URL that is pinged on success, with an alert when the expected interval passes without a ping.*

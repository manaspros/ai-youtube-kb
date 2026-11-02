# Setup Centralized Logging with Rsyslog

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `JocDslKu3j4` · [watch](https://youtu.be/JocDslKu3j4) · **date:** 2025-11-02 · **length:** 6:12 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack
- **topics:** dev-tools, observability · **tags:** rsyslog, syslog, centralized-logging, log-forwarding, linux, ubuntu, tcp, ufw

> Six-minute Better Stack tutorial on centralizing Linux logs with rsyslog: enable TCP reception on a collector, forward from clients over TCP 514, and verify with logger.

## Summary
The video walks through sending logs from several Linux servers to one central server using rsyslog, which the presenter says is usually preinstalled on distros (he uses Ubuntu). On the central server, he checks the install and service status, notes the server's IP, enables the TCP syslog input module in /etc/rsyslog.conf (default port 514), and adds template lines so incoming logs are stored per sending host and per program. He opens TCP 514 in ufw, restarts rsyslog, and confirms the listener with ss. On each client, one forwarding rule in /etc/rsyslog.d/50-default.conf sends all facilities and priorities to the central host over TCP, followed by a service restart. He verifies by writing a test message with logger, finding a per-client directory under /var/log on the central server, and tailing the forwarded user log. The video does not discuss encryption, retention, or scale. It ends with a plug for Better Stack's observability product.

## Key ideas
- **Centralized logging needs one collector (central) server and one or more client servers that send logs to it.** — rsyslog is typically preinstalled on most Linux distributions, so the setup needs no new packages in the presenter's Ubuntu example. ([0:00](https://youtu.be/JocDslKu3j4?t=0))
- **The collector must be told to accept logs over TCP, and to store them in a per-host, per-program directory layout.** — In /etc/rsyslog.conf the TCP reception input is uncommented under the UDP section, default port 514 kept. Template lines at the top of the file create a directory per sending hostname and per program, apply the template to all incoming logs, and stop further processing so logs are not duplicated. ([1:23](https://youtu.be/JocDslKu3j4?t=83))
- **Clients forward everything with a single rule rather than per-file configuration.** — On each client, a line in /etc/rsyslog.d/50-default.conf sends all logs (asterisk dot asterisk) to the central server's address on port 514, using the double-@ form for TCP. Only that host and port need to change. ([4:06](https://youtu.be/JocDslKu3j4?t=246))
- **Verification is a loggers test message followed by a check on the collector side.** — Run logger with a test string on the client, confirm it appears in the client's local syslog, then check that the central server created a directory named after the client and holds log files such as the user log. ([4:06](https://youtu.be/JocDslKu3j4?t=246))
- **A second test message confirms forwarding is continuous, not a one-off.** — After the first forwarded message appears in the collector's per-client user log, the presenter sends another and sees it arrive. ([5:30](https://youtu.be/JocDslKu3j4?t=330))

## Techniques
- **Enable TCP syslog reception on the collector** — On the central server: run rsyslogd -v to confirm the install, systemctl status rsyslog to confirm it is running, hostname -i to note the IP. Edit /etc/rsyslog.conf (sudo nano). Uncomment the TCP reception module and input under the 'provides TCP syslog reception' section (below the UDP section), keeping port 514. Add the template lines at the top of the file so logs land in a per-host, per-program path; the transcript describes them but does not read out their exact text. Open the firewall with sudo ufw allow 514/tcp. Restart with sudo systemctl restart rsyslog.service. Verify with sudo ss -tulnp | grep rsyslog, which should show a TCP listener on 514. *When:* Setting up a single log collector for several Linux hosts on a private network where plain TCP is acceptable.
- **Forward all logs from a client with one rule** — On each client: run rsyslogd -v to confirm the install. Edit /etc/rsyslog.d/50-default.conf (sudo nano) and add, below the comments, the line '*.* @@<central-server-address>:514' (the video uses central-server.lan as the name; an IP also works). Save, then sudo systemctl restart rsyslog.service. *When:* Quickly adding another host to an existing central collector, where you want every facility and priority forwarded.
- **Verify forwarding end to end** — On the client run logger "hi from client", then sudo tail /var/log/syslog to confirm the message is local. On the central server run ls /var/log to find a directory named after the client, ls it to see per-program logs (user, kernel, and others), then sudo tail /var/log/<client-hostname>/<user>.log to see the forwarded line. Repeat logger and tail again to confirm ongoing forwarding. *When:* Confirming a new forwarding setup works before depending on it.

## Numbers
- Video length is 6:12; the presenter frames setup as under six and a half minutes. ([0:00](https://youtu.be/JocDslKu3j4?t=0))
- Setup uses 2 servers in the demo (1 central collector, 1 client), with port 514 over TCP. ([0:00](https://youtu.be/JocDslKu3j4?t=0))
- Collector stores each client's logs under /var/log/<client hostname>/ with one file per program (for example user, kernel). ([4:06](https://youtu.be/JocDslKu3j4?t=246))

## Hot takes
- The promised 'under six and a half minutes' setup covers only a two-server demo on a private LAN; no TLS, authentication, retention, or scale is discussed.
- The closing segment is a plug for Better Stack's own observability product, not a sponsored segment.

## Tools mentioned
rsyslog, syslog, systemctl, ufw, nano, logger, ss, hostname, Ubuntu, Better Stack

## Relevance to our work
- **agentos** (1/3): AgentOS L4 observability and L3 storage are Prometheus/OTel-based; plain rsyslog collection is a basic host-level log layer that barely touches that stack. → *If agent-gateway host logs are still scattered, consider a central syslog collector as a cheap fallback before the OTel pipeline exists; otherwise skip.*

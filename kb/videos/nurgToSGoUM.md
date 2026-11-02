# Python Job Scheduling - with the Schedule package

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `nurgToSGoUM` · [watch](https://youtu.be/nurgToSGoUM) · **date:** 2024-11-02 · **length:** 27:32 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack
- **topics:** dev-tools, observability · **tags:** python, schedule, job-scheduling, cron, heartbeat, dead-mans-switch, monitoring, web-scraping, beautifulsoup, requests, better-stack, celery-beat, serverless

> Tutorial on running periodic Python jobs with the schedule package, scraping Hacker News, and alerting on missed runs with a Better Stack heartbeat.

## Summary
The video builds a small Python script that scrapes the top Hacker News front-page articles with requests and BeautifulSoup, sorts them by points, and returns the top N. It then runs that function periodically using the schedule package, first with every(N).seconds/minutes and a daily at("11:49") job, then with the @repeat decorator, and finally passes arguments such as n=1 into scheduled jobs. The speaker stresses that schedule is a simple library with no process manager, so the script needs its own while loop calling run_pending(), and that the package is not meant for persistence, exact timing, concurrency or localization. The second half adds monitoring: a Better Stack heartbeat with an expected interval and a grace period (20% extra recommended), pinged with a GET request at the end of each job, with an incident and email raised when pings stop. The video closes with alternatives (OS cron, Celery Beat, serverless functions) and notes that heartbeat monitoring works with all of them. It is a beginner-level tutorial, and most of the monitoring segment promotes Better Stack's own product.

## Key ideas
- **schedule is a scheduler library, not a process manager** — Jobs are declared with every(N).unit.do(fn) or every().day.at("HH:MM").do(fn), but nothing runs them until the script has a loop (while True with schedule.run_pending() and time.sleep(1)) that keeps it alive. ([1:09](https://youtu.be/nurgToSGoUM?t=69))
- **Scraped values are strings and need cleaning before sorting** — The score span reads like '13 points'. The speaker splits on whitespace, takes the first token, and converts it with int() before sorting with sorted(key=..., reverse=True) and slicing the top N. ([9:59](https://youtu.be/nurgToSGoUM?t=599))
- **Pairing scraped lists with zip and building dicts** — Anchor tags (title text, href) and score spans come from two CSS selects over the same page and are combined with zip into one dict per article, which is then sorted. ([8:58](https://youtu.be/nurgToSGoUM?t=538))
- **Decorator form keeps the schedule next to the job** — Using @repeat(every(5).seconds) above the function replaces the separate schedule.every(...).do(...) call. Job arguments are passed as extra decorator keyword arguments (n=1), or as keyword arguments to .do(). ([18:33](https://youtu.be/nurgToSGoUM?t=1113))
- **Know the limits of schedule before relying on it** — The docs describe it as a solution for simple problems. The speaker lists job persistence, exact timing, concurrent execution and localization as reasons to move to a more robust tool. ([17:26](https://youtu.be/nurgToSGoUM?t=1046))
- **Silent failure is why scheduled jobs need monitoring** — A periodic job can stop without any visible error. The speaker argues that you need a way to notice a missed run, not just a way to run the job. ([21:35](https://youtu.be/nurgToSGoUM?t=1295))
- **Dead-man's-switch heartbeat: ping at the end of the job** — Create a heartbeat in Better Stack with an expected interval (about 30 seconds in the demo) and a grace period (20% over expected duration recommended), then request the URL at the end of the job. When pings stop, an incident is raised, and the speaker shows an email alert after stopping the script. ([23:36](https://youtu.be/nurgToSGoUM?t=1416))
- **Alternatives for other environments** — OS cron suits backups and scripts, Celery Beat suits Django apps, and serverless platforms (AWS Lambda, Azure Functions) handle infrastructure. The speaker says heartbeat monitoring works with all of these. ([27:11](https://youtu.be/nurgToSGoUM?t=1631))

## Techniques
- **Declarative recurring jobs with schedule** — pip install schedule. Declare jobs with schedule.every(5).seconds.do(fn), schedule.every(10).minutes.do(fn), or schedule.every().day.at("11:49").do(fn). Run them with: while True: schedule.run_pending(); time.sleep(1). The speaker mentions a timezone argument to at() exists but does not show it. *When:* Single-process scripts with a few simple recurring tasks (scrapes, backups, digests) where a full scheduler or cron is more than needed.
- **Decorator-based job registration** — from schedule import repeat, every. Put @repeat(every(5).seconds) above the job function. For arguments, add them to the decorator: @repeat(every(1).day, n=1) on def get_top_n(n). The loop still calls schedule.run_pending(). *When:* When the schedule belongs with the job definition and you want to avoid a separate block of .every().do() calls.
- **HTML scrape to dict list with BeautifulSoup** — resp = requests.get(url); soup = BeautifulSoup(resp.content, "html.parser"). Use soup.select(css) with class selectors to get the title spans and their child anchors (anchor.text, anchor["href"]) and the score spans (span.text). Zip the two lists and build a dict per row with name, url and score (int of the first token). Sort with sorted(rows, key=lambda x: x["score"], reverse=True)[:n]. *When:* Periodic scraping of a listing page where each item has a title, link and numeric field to rank by. The speaker uses Hacker News as the example.
- **Heartbeat ping at the end of each scheduled job** — In Better Stack, open Heartbeats, click Create heartbeat, and set the expected period (the demo uses about 30 seconds) and a grace period (BetterStack recommends about 20% over expected duration). Copy the URL. At the end of the job, before returning, call requests.get(heartbeat_url). Set up on-call escalation for call, SMS, email or push alerts when pings stop. *When:* Any scheduled job, cron entry or serverless function where a silent failure or a missed run matters. The pattern is platform-neutral: any URL that accepts a GET or HEAD request can serve as the dead-man's switch.
- **Choose the scheduler by requirement** — Simple periodic script: schedule. Recurring database backup or script on a server: OS cron. Django app: Celery with Celery Beat. Managed infrastructure: AWS Lambda or Azure Functions on a timer trigger. The speaker says you can attach heartbeat monitoring to any of them. *When:* When deciding how to run a periodic job, especially once you need persistence, exact timing, concurrency or localization.

## Numbers
- Video length is 27:32; the scheduling portion is about 0:00 to 21:00 and monitoring follows. ([0:00](https://youtu.be/nurgToSGoUM?t=0))
- Example score parsed from the page is '13 points' before conversion to int 13. ([9:59](https://youtu.be/nurgToSGoUM?t=599))
- Sorted sample shows top article at 380 points and the fifth at 235 points. ([11:02](https://youtu.be/nurgToSGoUM?t=662))
- Demo interval for every(5).seconds is 5 seconds, with a loop sleep of 1 second. ([14:03](https://youtu.be/nurgToSGoUM?t=843))
- Daily at() demo used 11:49, which was about one minute after the recording time. ([16:07](https://youtu.be/nurgToSGoUM?t=967))
- BetterStack recommends a grace period about 20% over expected duration. ([22:26](https://youtu.be/nurgToSGoUM?t=1346))
- Heartbeat demo expects a ping roughly every 30 seconds; the dashboard waited 1 min 27 s before the first ping. ([23:36](https://youtu.be/nurgToSGoUM?t=1416))
- After the script was stopped, the last heartbeat was 45 seconds old, and the job went down with an incident and email alert. ([24:43](https://youtu.be/nurgToSGoUM?t=1483))

## Hot takes
- The monitoring segment is product promotion for Better Stack (the channel's own platform). The heartbeat pattern is generic, but the walkthrough shows only that vendor's UI.
- The video names concurrent execution as a limitation of schedule but does not show what happens when a job runs longer than its interval or when run_pending blocks. Overlapping runs go unaddressed.
- Scheduling is demonstrated with wall-clock times in one timezone, and the timezone argument is mentioned but not shown.
- Quality is capped at 3 because it is a beginner walkthrough with no sponsor segment and no production-grade discussion of failure handling.

## Tools mentioned
schedule (Python package), requests, BeautifulSoup 4 (bs4) with html.parser, pprint, Better Stack (Heartbeats, incidents, on-call escalation), VS Code, Hacker News (scraped source), Unix cron, Celery, Celery Beat, Django, AWS Lambda, Azure Functions

## Relevance to our work
- **prosharness** (1/3): ProsHarness runs loops and schedules. The video's list of what schedule lacks (persistence, exact timing, concurrency control, localization) is a useful checklist for a checkpointed scheduler. → *Check whether ProsHarness loops overlap or resume after a crash. If they do not, add a heartbeat ping at the end of each loop iteration so a stalled loop triggers an alert.*
- **agentos** (1/3): Roadmap items such as the Parquet/DuckDB archive and budget counter sync are periodic jobs. The video covers the dead-man's-switch pattern for them, which is simple but is not an AgentOS-specific technique. → *Add a missed-run alert (heartbeat pattern) to the planned Parquet/DuckDB archive job before it runs in production.*

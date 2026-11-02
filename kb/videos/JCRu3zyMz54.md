# Django 6.0 Just Changed Everything

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `JCRu3zyMz54` · [watch](https://youtu.be/JCRu3zyMz54) · **date:** 2026-01-02 · **length:** 7:02 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Django, Better Stack
- **topics:** dev-tools · **tags:** django, django-tasks, background-jobs, task-queue, celery, python, redis, rq

> Django 6.0 adds a built-in tasks API for background jobs: you define and enqueue tasks, but there is no worker, retry system or scheduler. It suits simple offload work, not a Celery replacement.

## Summary
The video walks through Django 6.0's new django.tasks module, which gives Django a standard way to declare and enqueue background work such as emails, uploads and API calls. The design (Django Tasks, an accepted enhancement proposal by core contributor Jake Howard) is deliberately minimal: Django defines the decorator, the enqueue API and the result abstraction, while backends or third-party packages handle storage and execution. The speaker demonstrates a @task decorator with priority, queue name and takes_context, enqueueing after a transaction commits, and a status endpoint built on a Django 5 backport. The comparison to Celery is that Django Tasks is lighter and Django-native, but Celery still wins for distributed scale and built-in retries. The speaker lists the gaps: no built-in worker, no retries, schedules or chains, and JSON-serializable arguments only. Community Redis and RQ adapters are filling those gaps, and a Celery bridge is only under discussion.

## Key ideas
- **Django 6.0 ships a built-in tasks module for background work, from the Django Tasks enhancement proposal.** — Django defines how tasks are declared and enqueued, and backends own storage and execution. The initial version is small on purpose and ships no production worker. ([0:00](https://youtu.be/JCRu3zyMz54?t=0))
- **Django Tasks is an entry ramp for simple offload, not a Celery killer.** — The speaker's estimate is that it covers about 80% of simple offload cases (emails, uploads, API hits). Heavy distributed workflows still need Celery, Huey, RQ or similar. ([1:05](https://youtu.be/JCRu3zyMz54?t=65))
- **The API surface is a @task decorator, enqueue(), and a result object that can be reloaded later.** — The decorator takes priority and queue_name. takes_context=True injects a task context with attempt count and result ID. get_result reloads status, errors and return value. The built-in immediate and dummy backends do not provide real background execution. ([2:03](https://youtu.be/JCRu3zyMz54?t=123))
- **Enqueue inside a transaction, but only after the commit.** — The speaker saves an order inside transaction.atomic so the write is all-or-nothing, then enqueues the notification from an on_commit hook. The worker therefore only runs once the data is durable. ([3:23](https://youtu.be/JCRu3zyMz54?t=203))
- **Trade-off against Celery: Django-native and light versus distributed scale and built-in retries.** — Django Tasks keeps dependencies minimal and feels native to Django. Celery offers distributed scale and retries, but with steeper configuration and overhead. ([4:26](https://youtu.be/JCRu3zyMz54?t=266))
- **Django Tasks does not include a worker, retries, schedules or chains.** — You need a separate worker process, and those features come from the backend or third-party tooling. Task arguments must be JSON-friendly. Community Redis adapters are already filling the gaps. ([5:32](https://youtu.be/JCRu3zyMz54?t=332))
- **Django 5 users can try the API through a backport, then migrate.** — The backport lets a Django 5 project adopt the tasks API now, so the code can move to Django 6 without rewriting. ([6:38](https://youtu.be/JCRu3zyMz54?t=398))

## Techniques
- **Declare tasks with the task decorator and context injection** — Decorate the function with @task(priority=..., queue_name=...). Set takes_context=True to receive a task context as the first argument, which exposes attempt count and the task result ID. Higher priority numbers mean higher priority, as interpreted by the backend. *When:* Offloading work such as sending a notification, processing an upload or calling an external API, when retries are handled by you or the backend.
- **Enqueue after the DB commit** — Wrap the write in transaction.atomic so it commits or rolls back as one unit. Enqueue the task from an on_commit hook, not inline, so the worker never sees rows that are not yet committed. The exact call form is not shown in the captions. *When:* Any task that reads data written during the request, such as an order confirmation email.
- **Status endpoint over stored result IDs** — Pass the returned result ID to the client. Expose a GET view at a tasks/<id>/status URL that reloads the result with get_result and returns finished state, return value and attempt count. The speaker runs this on Django 5 with the backport. *When:* The client needs to poll for the outcome of async work.
- **Keep task arguments JSON-serializable** — Pass IDs and primitive values, not model instances or other objects that do not survive serialization. *When:* Designing the arguments for any task that will go through a real backend or queue.
- **Adopt on Django 5 via the backport, then migrate** — Install the Django Tasks backport on Django 5 and use the same decorator and enqueue API, so the code moves to Django 6 with minimal change. *When:* Trialing the API before upgrading to Django 6.

## Numbers
- Django 6.0 tasks went through alpha in September 2025, beta in October and RC1 in November before the December 2025 release. ([0:00](https://youtu.be/JCRu3zyMz54?t=0))
- The speaker's estimate is that Django Tasks covers about 80% of apps and simple offload use cases, based on early write-ups and discussions, not measured data. ([1:05](https://youtu.be/JCRu3zyMz54?t=65))
- The speaker gives no benchmarks, latency or cost figures. ([4:26](https://youtu.be/JCRu3zyMz54?t=266))

## Hot takes
- The Django 6 hype is qualified: the speaker calls it an entry ramp, not a Celery killer, and says it is minimal by design.
- The 80% figure is attributed to early write-ups and is unverified.
- The title's 'Changed Everything' is stronger than the content, which is a measured feature overview with caveats.
- The captions say the immediate and dummy backends 'never actually execute'. This is ambiguous for the immediate backend and should be checked in the Django docs.
- A Celery bridge for the Django tasks interface is only under discussion and not on the roadmap.

## Tools mentioned
Django 6.0, Django Tasks (django.tasks module), Django Tasks backport for Django 5, Celery, Huey, RQ, Redis (community adapters), Django tasks worker (separate process, referenced generically)

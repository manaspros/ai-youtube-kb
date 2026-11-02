# SQL Used to Be Mandatory… But Not Anymore (Here’s the Shift)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `nTRzoISgDpo` · [watch](https://youtu.be/nTRzoISgDpo) · **date:** 2025-12-02 · **length:** 5:05 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, FastAPI
- **topics:** dev-tools, data-engineering · **tags:** sqlmodel, sqlalchemy, pydantic, fastapi, orm, python, sql, database

> Beginner tutorial arguing Python developers can skip raw SQL by using SQLModel, an ORM that combines SQLAlchemy and Pydantic, while still learning SQL basics.

## Summary
Better Stack's 5-minute intro argues that Python developers, especially beginners, do not need to write raw SQL to build real apps. It presents SQLModel, a library that merges SQLAlchemy's ORM with Pydantic validation, and says it is built by the FastAPI author. The speaker walks through the raw-SQL pattern (connection, cursor, long query string) and contrasts it with defining a table as a Python class, creating an engine, inserting objects with add and commit, and fetching rows with a select statement. He claims one model can double as a FastAPI endpoint schema, handling validation, type conversion, relationships and serialization. The video ends by saying SQL is optional for ORM work but still worth learning for debugging and tuning. No benchmarks or code details beyond the high-level flow are shown in the transcript, so the notes give no reproducible commands.

## Key ideas
- **Python developers do not need raw SQL to build real apps.** — The speaker frames raw SQL as repetitive and error-prone (string concatenation, typos, messy joins) and argues ORMs let you query the database from Python. ([0:00](https://youtu.be/nTRzoISgDpo?t=0))
- **SQLModel merges SQLAlchemy's ORM with Pydantic.** — One class serves as the table definition and the validation schema; the speaker says it is built by the FastAPI author and is built on top of SQLAlchemy, so full SQLAlchemy control remains available. ([1:14](https://youtu.be/nTRzoISgDpo?t=74))
- **Tables defined as classes replace hand-written SQL for CRUD.** — Insert is create an object, add it to the session and commit. Fetch is a select on the model class. The speaker says the same flow is far less boilerplate than the cursor-based raw SQL version shown first. ([2:31](https://youtu.be/nTRzoISgDpo?t=151))
- **One model can double as the FastAPI endpoint schema.** — Because the model is also a Pydantic model, it handles data validation, type conversion, relationships and serialization for API endpoints, per the speaker. ([1:14](https://youtu.be/nTRzoISgDpo?t=74))
- **SQL knowledge is still worth having even with an ORM.** — The speaker says you can build full apps without writing SQL, but debugging and performance tuning still benefit from knowing how SQL works, so learning the basics is recommended. ([3:45](https://youtu.be/nTRzoISgDpo?t=225))

## Techniques
- **Model-as-table with SQLModel** — Define a class that is both the database table and the Pydantic schema, then create an engine and create the tables from the model. The transcript does not show exact code, flags or names beyond this flow. *When:* Small-to-medium Python services, especially FastAPI backends, where you want one type-safe model for storage, validation and API responses.
- **Object-based insert and fetch instead of raw SQL** — Insert by instantiating the model with keyword arguments, adding it to a session and committing. Fetch by selecting from the model class with a where condition. Exact session and statement syntax is not shown in the transcript. *When:* Routine CRUD in Python where string-built SQL is error-prone and hard to review.
- **Drop to raw SQL when needed** — Because SQLModel sits on SQLAlchemy, the speaker says full control remains available, so fall back to lower-level SQL for tuning or unusual queries. *When:* Queries that the ORM generates poorly, or when debugging performance.

## Numbers
- Example User model has four properties (fields). ([1:14](https://youtu.be/nTRzoISgDpo?t=74))
- Video runtime is 5:05; no performance benchmarks, latencies or adoption figures are given. ([0:00](https://youtu.be/nTRzoISgDpo?t=0))

## Hot takes
- The speaker says SQL is optional for building apps but still valuable for debugging and tuning.
- Claims that ORMs remove 'fighting the database' and that SQLModel offers 'the best of both worlds' are asserted without evidence, examples or trade-offs (no discussion of N+1 queries, performance costs or migrations).

## Tools mentioned
SQLModel, SQLAlchemy, Pydantic, FastAPI

## Relevance to our work
- **agentos** (1/3): AgentOS runs Postgres/pgvector and Python services; a typed model layer could help the control-plane tables, but this is a generic intro with no performance or correctness content. → *If a Python control-plane service needs a typed DB layer for budget or registry tables, compare SQLModel against raw SQL on one table before adopting it.*
- **general** (1/3): Useful only as a beginner reference for the ORM-versus-raw-SQL trade-off.

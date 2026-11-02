# Run S3 on Your Laptop? This Changes Everything (MinIO)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `GHeLgENOBb4` · [watch](https://youtu.be/GHeLgENOBb4) · **date:** 2026-05-02 · **length:** 5:30 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed Better Stack presenter · **orgs:** Better Stack, MinIO, Amazon Web Services
- **topics:** dev-tools, infra-cost-scaling · **tags:** object-storage, s3-compatible, minio, local-dev, docker, boto3, cloud-cost, egress-fees, license

> Short intro to running MinIO, an S3-compatible object store, on a laptop for local dev and prototypes, with the caveats that the repo is archived and the project is moving to a paid AI Store.

## Summary
The presenter argues that S3 bills and data egress push teams toward running an S3-compatible object store locally. He runs MinIO in one Docker container on an M4 Pro Mac, creates a bucket with the MinIO client (mc), uploads an image, a text file and a JSON file, and shows that an existing boto3 Python script works against it. He presents MinIO as an S3 API server that runs anywhere (Docker, Kubernetes, bare metal, edge, laptop) and suggests a tiered pattern of MinIO locally, MinIO or S3 in staging, and cloud in production. He flags that the open-source repo is archived and in maintenance mode, that the vendor has shifted to a MinIO AI Store with a free single-node tier and paid cluster/HA tiers, and that for production clusters he would look at AI Store, Ceph or Garage. The video is short (5:30) and mostly an overview; it gives no benchmarks and does not show the endpoint configuration that would point boto3 at localhost.

## Key ideas
- **Motivation: cloud S3 costs (predictable bills, egress fees, latency from data far from compute) and AI/RAG workloads that want fast local storage.** — The presenter frames a local S3-compatible store as a way to avoid cloud bills for development and data-heavy apps. He says the setup suits local dev, prototypes, RAG pipelines, media and backups. ([0:00](https://youtu.be/GHeLgENOBb4?t=0))
- **MinIO is an object storage server that speaks the Amazon S3 API, so existing SDKs and mental models carry over.** — He describes it as a single binary or Docker image with strong S3 compatibility that can run on Docker, Kubernetes, bare metal, edge or a laptop. He calls it good for development and testing, not production. ([2:12](https://youtu.be/GHeLgENOBb4?t=132))
- **The repo is archived and in maintenance mode; the project has shifted to MinIO AI Store.** — He says the GitHub repo is archived and the focus has moved to the AI Store product (the MinIO name remains). He still considers it usable for a good while, but it is a risk for long-term dependence. ([1:01](https://youtu.be/GHeLgENOBb4?t=61))
- **Demo: an existing boto3 script runs unchanged against the local store, and the browser UI previews uploaded objects.** — He uploads an image, a text file and a JSON file with the mc client, lists them as a clean bucket structure, and runs a Python boto3 script. He says no code changes were needed. The browser UI on localhost lets him browse folders and preview the image. ([2:12](https://youtu.be/GHeLgENOBb4?t=132))
- **Suggested tiering: local MinIO for development, MinIO or S3 for staging, cloud for production, all behind the same S3 API.** — The argument is that matching the S3 model locally means the app code does not change between environments. He says local setups are for building and debugging data-heavy apps before touching production. ([3:31](https://youtu.be/GHeLgENOBb4?t=211))
- **Licensing and tiers: the open-source server is AGPLv3; the AI Store has a free single-node tier and paid cluster/HA tiers.** — He says the open-source MinIO is free under AGPL v3 and works for demos, local dev and prototypes. Clustering and high availability are paid features of the AI Store. ([3:31](https://youtu.be/GHeLgENOBb4?t=211))
- **For production clusters, consider AI Store, Ceph or Garage rather than the open-source local build.** — He compares AWS S3 (managed but costly and lock-in), Ceph (scalable but more moving parts) and MinIO, and concludes the open-source build is for learning, small projects and experiments, not fully managed or HA infra. ([4:46](https://youtu.be/GHeLgENOBb4?t=286))

## Techniques
- **Run a local S3-compatible store in Docker** — Run MinIO as one Docker container on the laptop (the presenter used an M4 Pro Mac). The exact docker run command and flags are not shown in the video. Point app code at the local endpoint instead of AWS. *When:* Local development, prototypes and debugging data-heavy apps where you want S3 semantics without a cloud account or egress costs.
- **Register the local server with the MinIO client (mc) as an alias** — Run `mc alias set local <host>` with the server address and the login credentials from the MinIO docs (the presenter used the default credentials 'for now'). Then use the `local/` alias for bucket and object commands. The video shows the alias command, then bucket creation and uploads, but the exact subcommands and bucket name spelling are not fully legible in the transcript. *When:* Scripting bucket setup for local dev, or checking uploaded objects from the terminal.
- **Keep the S3 SDK code and only change the endpoint** — Use the existing boto3 (or other S3 SDK) code. The presenter says the same script runs against local MinIO with no changes. The transcript does not show how the endpoint is set, so verify it (typically an endpoint URL setting in the client) before relying on it. *When:* Moving an S3-using app to a local or staging object store without rewriting storage code.
- **Tiered environments behind one S3 API** — Local MinIO for development, MinIO or S3 for staging, cloud S3 for production. Keep the same bucket and object model in each tier so application code does not branch. *When:* Teams that want to cut dev and test storage costs while keeping environment parity with production.
- **Browse and preview objects in the MinIO web console** — Open the local MinIO web UI on localhost, expand bucket folders and click an object to preview it (the presenter previewed an image). *When:* Quickly checking what a pipeline or app wrote to a bucket during development.

## Numbers
- Demo hardware: MinIO running in a single Docker container on an M4 Pro Mac, with a 5:30 video length. ([0:00](https://youtu.be/GHeLgENOBb4?t=0))
- Open-source MinIO is licensed under AGPL v3. ([3:31](https://youtu.be/GHeLgENOBb4?t=211))
- No benchmarks, latency or cost figures are given; cost and performance claims are qualitative. ([3:31](https://youtu.be/GHeLgENOBb4?t=211))

## Hot takes
- Object storage for dev and test is a good use of a local S3-compatible store, but the presenter says it is not for production.
- The project is archived and in maintenance mode; treating it as a long-term dependency is risky, and the presenter himself says it can only be used 'for a good while'.
- Cost savings are asserted (egress fees, cloud bills) without any measured numbers.
- The 'no code changes' claim is shown with a boto3 script but the endpoint configuration is not shown on screen.

## Tools mentioned
MinIO, MinIO AI Store, mc (MinIO client), Docker, boto3, Python, Kubernetes, Ceph, Garage, AWS S3

## Relevance to our work
- **agentos** (1/3): AgentOS roadmap has Parquet + DuckDB archive tiers and RAG/knowledge-bucket storage. A local S3-compatible store could serve as a dev-time stand-in, but the video is a short overview and the project is archived. → *Before adopting MinIO for dev-time archive or RAG artifacts, check its archived/maintenance status and AGPL terms, and compare it with Garage or Ceph; the video itself says it is not for production.*

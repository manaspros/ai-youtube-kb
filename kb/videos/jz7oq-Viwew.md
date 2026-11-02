# Run AWS Locally with Docker (LocalStack)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `jz7oq-Viwew` · [watch](https://youtu.be/jz7oq-Viwew) · **date:** 2026-01-02 · **length:** 4:13 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** Better Stack presenter (not named in transcript) · **orgs:** LocalStack, AWS, Better Stack
- **topics:** testing-verification, dev-tools, sandboxing-execution · **tags:** localstack, aws, docker, local-emulation, ci, terraform, aws-cdk, serverless, lambda, s3, dynamodb, sqs, api-gateway, homebrew

> Short intro to LocalStack, a Docker-based AWS emulator. The main takeaway is to use it for the inner dev loop and CI, and still verify critical paths on real AWS.

## Summary
The presenter introduces LocalStack as a cloud emulator that runs AWS services such as S3, Lambda, DynamoDB, SQS and API Gateway inside a single Docker container on the laptop. The pitch is faster feedback, no cloud bill for experiments, and working without an AWS account or internet connection. On a Mac, LocalStack is installed with Homebrew and started with one command, after which the normal AWS CLI and SDKs can target the local endpoint. The demo deploys a static site and Lambda packages from a sample repo to the local emulator and uploads a file to confirm it works. The presenter then says LocalStack fits Terraform, AWS CDK and Serverless Framework workflows through a small endpoint override, and that the same start-test-stop pattern works in CI. The video is light on commands and config, and it closes with the caveat that LocalStack is not a perfect clone, so critical paths should be tested on real AWS.

## Key ideas
- **LocalStack runs AWS services (S3, Lambda, DynamoDB, SQS, API Gateway) locally in one Docker container, and the SDKs, CLI and IaC tools stay the same.** — The only change is the endpoint. The speaker stresses it is emulation, not a mock or fake config, and that no AWS account or internet connection is needed. ([0:00](https://youtu.be/jz7oq-Viwew?t=0))
- **The pitch is the developer loop: real AWS feedback is slow, CI is slow, shared environments are risky to experiment in, and every experiment costs money.** — LocalStack is framed as a place to break things without fear. It is positioned as a development and test environment, not a replacement for AWS. ([0:00](https://youtu.be/jz7oq-Viwew?t=0))
- **Setup is one install and one start command on macOS.** — Install via Homebrew, then run the LocalStack start command, which launches a Docker container that exposes an AWS-compatible endpoint on the laptop. ([1:17](https://youtu.be/jz7oq-Viwew?t=77))
- **The demo deploys real artifacts to the emulator: Lambda packages built locally, an S3 bucket, and a static site whose URLs are opened in a browser.** — The sample app is a Git repo taken from the LocalStack docs. The presenter uploads a file to confirm the app works. All steps run locally with no cloud resources. ([1:17](https://youtu.be/jz7oq-Viwew?t=77))
- **LocalStack is meant to plug into IaC and CI workflows: point Terraform, CDK or Serverless at it with an endpoint override, run tests, then tear everything down in seconds.** — The speaker says service logs, local debugging and integrations such as Testcontainers also work. He presents this as the same approach in CI, where Docker starts LocalStack, tests run, and it shuts down. ([2:35](https://youtu.be/jz7oq-Viwew?t=155))
- **Emulation is not identical to AWS. Some services behave differently, some edge cases differ, and not every service is fully supported.** — The advice is to test critical paths against real AWS. LocalStack is the inner dev loop, CI test environment and sandbox, but not production. ([3:34](https://youtu.be/jz7oq-Viwew?t=214))

## Techniques
- **Point AWS SDK, CLI and IaC at a local emulator** — Run LocalStack in Docker and override the service endpoint in the AWS CLI, SDK or IaC tool to the local endpoint instead of real AWS. The video shows the idea but not the exact endpoint flag or config keys; the speaker says it is usually a small config change. *When:* Local development of AWS-backed services where you want fast iteration without cloud cost or shared-environment risk.
- **Ephemeral LocalStack in CI** — In CI, start LocalStack in Docker, run the test suite against the local endpoint, then shut the container down. The speaker names Testcontainers as one integration option. *When:* Integration tests for code that depends on S3, Lambda, SQS, DynamoDB or API Gateway, where a clean, disposable environment per run is useful.
- **Split test tiers: emulator for the inner loop, real AWS for critical paths** — Run most tests against LocalStack for speed and cost, and reserve a smaller set of checks for real AWS to catch behavioral differences in the emulator. *When:* Any AWS-dependent system where emulator fidelity gaps could hide production bugs.

## Numbers
- LocalStack launches with a single start command after a one-line brew install on macOS. ([1:17](https://youtu.be/jz7oq-Viwew?t=77))
- Environments can be torn down in seconds, per the speaker. No benchmark or measured figure is given. ([2:35](https://youtu.be/jz7oq-Viwew?t=155))
- No cost, latency or adoption numbers are given. The only cost argument is qualitative: experiments on real AWS cost money. ([0:00](https://youtu.be/jz7oq-Viwew?t=0))

## Hot takes
- The core advice, that LocalStack is not a perfect clone and critical paths need real AWS testing, is the most useful and most accurate claim in the video.
- The video is thin for a tutorial. It shows no commands beyond the install and start steps, no config file, and no endpoint settings, and it skips the demo's deploy commands.
- The 'AWS without the anxiety' framing is promotional. Quality is capped at 2 because the substance is a short overview with no reproducible steps. The video is not sponsored in the transcript.

## Tools mentioned
LocalStack, Docker, AWS CLI, AWS SDKs, Terraform, AWS CDK, Serverless Framework, Testcontainers, Homebrew (brew), AWS Lambda, Amazon S3, Amazon DynamoDB, Amazon SQS, Amazon API Gateway

## Relevance to our work
- **agentos** (1/3): AgentOS is self-hosted and runs on its own stack, so AWS emulation is at most a test convenience for any AWS-facing pieces, such as storage or queues. It does not change the architecture. → *If any AgentOS component is written against S3, SQS or Lambda, evaluate LocalStack for local and CI tests of those paths. Keep a real-AWS check for anything whose behavior matters.*

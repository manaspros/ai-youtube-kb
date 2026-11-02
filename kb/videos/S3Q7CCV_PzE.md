# Before You Pay for Manus AI, See What This Free Tool Can Do

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `S3Q7CCV_PzE` · [watch](https://youtu.be/S3Q7CCV_PzE) · **date:** 2025-11-02 · **length:** 10:23 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Manus, OpenAI, DeepSeek, Hugging Face, Together AI, Google
- **topics:** local-ai, multi-agent, agent-architecture · **tags:** agentic-seek, manus, open-source-agent, local-llm, api-mode, docker, config-ini, headless-browser, gpu-requirements, install-walkthrough

> Walkthrough of installing and running Agentic Seek, an open-source Manus-style multi-agent tool that runs locally or through a cloud API, with the speaker's hardware and cost caveats.

## Summary
The host argues that Manus AI's credit pricing adds up quickly and presents Agentic Seek, an open-source agent with a planner that splits a request across specialized agents, as a free alternative. He shows the project's own demo (ranking candidate CVs against a project's skill needs) and two of his own runs: a movie-list search that took about 4 minutes with 3 sources and about 8 minutes with 10. The core of the video is a setup tutorial: clone the repo, create a Python environment, run the OS install script, set config.ini to API mode with a provider and model, add the API key to the env file, start Docker and the service script, then run the backend with python3.10 and open localhost:3000. He says local use needs a 32B-class model (an RTX 4090 for that) and that smaller 14B models perform poorly, so most viewers would need an API key. He found GPT-4o clearly better than GPT-4o mini, and Claude was not supported at the time. The evidence is two anecdotal runs and no quality comparison with Manus.

## Key ideas
- **Motivation: Manus AI's credit pricing gets expensive fast. The $19/month basic plan gives 1,900 monthly credits plus 300 refresh credits per day, and a simple chart can cost up to 200 credits while a web app costs 900.** — Pricing figures are the speaker's reading of Manus's plan, not verified here. The pitch is that a local, open-source agent avoids this metering. ([0:00](https://youtu.be/S3Q7CCV_PzE?t=0))
- **Agentic Seek is presented as an open-source Manus-like agent with browser and local file access. It can run fully local or through a hosted API key, and the speaker frames it as having no subscription or credit limits.** — 'Free' only holds for the local path. The API path still bills per model call, and the speaker says he used API credits himself. ([1:24](https://youtu.be/S3Q7CCV_PzE?t=84))
- **The project's demo shows a planner agent that delegates work to specialized agents. It reads the GitHub README to learn the project's required skills, unzips a candidate archive, reads each CV, and ranks the candidates by fit. The planner also fetched a comparison page against Manus, which the speaker could not explain.** — This is the vendor-provided demo. The speaker does not evaluate whether the rankings are correct. ([1:24](https://youtu.be/S3Q7CCV_PzE?t=84))
- **Anecdotal runtime data: a movie-list task (search popular 2024 sci-fi, pick three, save to a text file) took about 4 minutes with 3 sources and about 8 minutes with 10 sources. The output was saved to movies.txt in the agent folder.** — Two single runs on one machine. No accuracy check on the picks. ([3:27](https://youtu.be/S3Q7CCV_PzE?t=207))
- **Local models have a steep hardware bar. The speaker says a 32B-class model is needed for good results and that 14B models from Ollama, DeepSeek or Qwen will not perform well.** — Based on his testing, not a benchmark. He also says the 32B setup needs an RTX 4090, and 14B needs at least an RTX 3060. ([5:50](https://youtu.be/S3Q7CCV_PzE?t=350))
- **API mode is the fallback. Supported providers are OpenAI, DeepSeek, Hugging Face, Together AI and Google. Claude was not supported when he recorded. In his test, GPT-4o clearly beat GPT-4o mini.** — The GPT-4o vs mini judgment is subjective and based on a few tasks. He notes that stronger models would likely do better still. ([7:05](https://youtu.be/S3Q7CCV_PzE?t=425))
- **Operational gotchas: Docker must be running before the services start, because the stack is containerized and pulls its own images. The backend and frontend run in separate terminals, and the backend must be started with python3.10 explicitly, since plain python or python3 fails for him.** — The frontend is served at localhost:3000. ([8:03](https://youtu.be/S3Q7CCV_PzE?t=483))

## Techniques
- **Install from the README** — Clone the repo and rename the example env file to the real env file. Create a Python virtual environment inside the repo folder. Run the install script for your OS (he uses the macOS one). If the script asks for Python 3.10, install that exact version first. The exact commands are on the project's GitHub README, which the video does not show in full. *When:* First-time setup on macOS, Linux or Windows.
- **Switch config.ini from local to API mode** — In config.ini, set the 'is local' flag to false (the default is true). Set the provider name to one of the supported providers. Set the provider model (he uses GPT-4o rather than GPT-4o mini). Put the matching API key into the env file. The key spellings are spoken, not shown on screen, so check the README for the exact names. *When:* No 32B-class local GPU, so you want to run the agent through a hosted model.
- **Headless browser and voice options** — Leave the headless-browser option set to true so the agent browses in the background. Set the speak and listen options to true to enable spoken replies and voice input. *When:* Running long browser tasks unattended, or wanting a voice interface.
- **Start order** — 1) Start Docker. 2) In a fresh activated venv, run the service-start command from the README (the macOS command also works on Linux). 3) In a second terminal, run 'python3.10 api.py' to start the backend. 4) Open localhost:3000 for the frontend. *When:* Each session, after setup is complete.
- **Planner plus specialized agents** — The planner breaks the user request into subtasks and routes them to agents for browsing, file reading and writing. Each run can take several minutes because the agent browses many sources in sequence. *When:* Multi-step tasks that combine web search, file I/O and synthesis, where a single prompt should produce a saved output file.

## Numbers
- Manus basic plan is $19/month with 1,900 monthly credits and 300 refresh credits per day ([0:00](https://youtu.be/S3Q7CCV_PzE?t=0))
- A simple chart can cost up to 200 Manus credits, and a web app 900 credits ([0:00](https://youtu.be/S3Q7CCV_PzE?t=0))
- Movie-list task with 3 sources took about 4 minutes; with 10 sources about 8 minutes (one run each, author's machine) ([3:27](https://youtu.be/S3Q7CCV_PzE?t=207))
- Good local performance needs at least a 32B model (speaker's claim); 14B models are not good enough ([5:50](https://youtu.be/S3Q7CCV_PzE?t=350))
- 32B local model requires an RTX 4090; 14B needs at least an RTX 3060 (speaker's claim) ([7:05](https://youtu.be/S3Q7CCV_PzE?t=425))

## Hot takes
- 'Free' is conditional. The local path needs a 32B-class model and roughly RTX 4090-class hardware by the speaker's account. Everyone else pays per token through an API, and the 'no credit limits' framing applies only to the local app.
- The 'completely local, fully private' claim does not hold in API mode, where prompts go to the chosen provider. The video does not say this.
- The evidence is two single timed runs and an anecdotal GPT-4o vs GPT-4o mini comparison. No quality comparison with Manus is shown.
- The title is a comparison hook, but the substance is an install walkthrough plus a vendor demo. The video does not show whether the output quality matches Manus.
- The speaker says Claude is not supported yet. Not sponsored; the only pitch is a channel membership plea.

## Tools mentioned
Agentic Seek (version not stated), Manus AI, Docker, Python 3.10, Ollama, Qwen, DeepSeek, GPT-4o, GPT-4o mini, Cursor (editor used for config)

## Relevance to our work
- **agentos** (1/3): Agentic Seek is a single-user local agent, not infrastructure. It only touches AgentOS through the local-model hardware bar, which is useful context for the InferCraft and single-RTX-5090 work. → *Skip as a dependency. If we want a local-only agent demo, note the speaker's claim that a 32B-class local model is the minimum for usable output, and benchmark that claim on our own hardware.*
- **prosharness** (1/3): The planner-to-specialized-agents flow is a loose parallel to ProsHarness's plan, critique and debate loop, but the video gives no detail on how the planner decides or verifies its work. → *Compare Agentic Seek's planner breakdown (subtask routing across browser and file agents) with ProsHarness's plan step to see whether any checkpoint or verification stage is worth borrowing. Read the project's README first, not this video.*

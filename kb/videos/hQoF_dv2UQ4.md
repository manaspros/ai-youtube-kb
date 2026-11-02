# Qwen 3.5 Small Models Are INCREDIBLE! (Testing 0.8B & 2B On Edge Devices)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `hQoF_dv2UQ4` · [watch](https://youtu.be/hQoF_dv2UQ4) · **date:** 2026-04-02 · **length:** 13:07 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Andres (Better Stack host) · **orgs:** Better Stack, Alibaba, Apple, LM Studio, Cline, IBM
- **topics:** local-ai, models-research, coding-agents · **tags:** qwen-3.5, small-models, edge-ai, offline, lm-studio, cline, mlx, ios, multimodal, ocr, hallucination, repetition-loops, gguf

> Hands-on offline tests of Qwen 3.5 0.8B and 2B on a laptop and iPhone: fast and surprisingly multimodal, but repetition loops and hallucinations rule out serious coding.

## Summary
Better Stack's host tests Alibaba's Qwen 3.5 small multimodal models (0.8B and 2B) fully offline, pitching them as high "intelligence density." He cites MMLU, OCRBench and 262k-context figures without verifying them in the video. On a laptop he runs both through LM Studio's local server with the Cline VS Code extension to build a cafe website: the 0.8B output is bland and hard-codes broken image URLs, while the 2B plans first and gives a cleaner design but repeatedly gets stuck in output loops. On an iPhone 14 Pro he runs both in a native Swift app built on MLX Swift, in airplane mode, with fast streamed replies. Quick vision and reasoning probes give mixed results: both pass a car-wash reasoning trick, both misidentify a dog breed, and only the 2B correctly identifies Latvian text. He concludes these are the strongest tiny models he has used but not fit for serious coding, and closes with an unconfirmed report of major departures on the Qwen team.

## Key ideas
- **Qwen 3.5 small series (0.8B and 2B) are natively multimodal and pitched to run offline on old laptops and phones** — Speaker frames the release as Alibaba's native multimodal small models, and contrasts them with IBM Granite 4.0 nano (about 300M parameters), which he covered earlier. ([0:00](https://youtu.be/hQoF_dv2UQ4?t=0))
- **The speaker's thesis is 'intelligence density': small models now combine text, vision and coding in one architecture** — He argues the old rule that seeing, reasoning and coding required a huge model no longer holds, and says the models keep vision and coding capability in a unified design. ([1:18](https://youtu.be/hQoF_dv2UQ4?t=78))
- **Reported benchmarks put the 2B model well above the 0.8B on general knowledge and OCR** — He quotes MMLU of 66.5 for the 2B and 42.3 for the 0.8B, and compares the 0.8B to Llama 2 7B (45.3). He also cites OCRBench scores of 85.4 and 79.1. Both models advertise a 262k context window. He presents these figures without checking them. ([2:29](https://youtu.be/hQoF_dv2UQ4?t=149))
- **Offline coding in LM Studio plus Cline: the 0.8B model finishes fast but produces a weak result** — It built a bland cafe site in about a minute, hard-coded Unsplash image URLs (most broken), and could not reliably fix them on retry. He concludes it is capable of coding and tool calling, but too small for real use. ([3:36](https://youtu.be/hQoF_dv2UQ4?t=216))
- **The 2B model plans before coding and gets a better design, but loops repeatedly** — It took about three minutes, produced a cleaner brown theme with a cart sidebar (missing an add-to-cart button), and then fell into an infinite loop during fixes. He is unsure whether the model, the LM Studio server or Cline is at fault. ([5:54](https://youtu.be/hQoF_dv2UQ4?t=354))
- **On an iPhone 14 Pro, a native MLX Swift app runs the models offline with fast streaming** — MLX uses the Metal GPU on Apple Silicon unified memory. The app downloads the 0.8B model on first launch. In airplane mode, replies stream quickly. ([6:50](https://youtu.be/hQoF_dv2UQ4?t=410))
- **Small-model vision and reasoning are inconsistent, and confident hallucinations appear** — The 0.8B called itself Alex, passed the car-wash test, called a banana a 'dog banana', and claimed Latvian text was Slovenian. The 2B passed the car-wash test, read the banana as ripe, misnamed a dog breed (Pomeranian), and correctly identified Latvian. ([7:55](https://youtu.be/hQoF_dv2UQ4?t=475))
- **Verdict: strongest tiny models he has used, but not for serious coding; Qwen team departures reported** — He calls these the most powerful tiny models he has used despite inconsistencies. He reports, without confirmation, that Alibaba is restructuring the Qwen team and that leaders and engineers have left, so this may be the last major release from the team for a while. ([11:31](https://youtu.be/hQoF_dv2UQ4?t=691))

## Techniques
- **Local OpenAI-style server in LM Studio, wired into Cline** — In LM Studio's Models tab, download the GGUF builds of Qwen 3.5 0.8B and 2B. Raise the context length substantially for coding work, then start the local server. In Cline's API configuration, choose the custom LM Studio server URL and select the model. Turn off Wi-Fi to confirm the setup works offline. No config keys or flags are shown in the video. *When:* Offline or privacy-constrained coding experiments with small local models on a laptop.
- **Constrain the stack so offline output has no external dependencies** — Name the exact stack in the prompt, for example plain HTML, CSS and JavaScript with no external libraries. Leaving the framework open made the model pick React, which fails without network access. *When:* Any local-model code generation run without internet access, where package installs or CDN assets will not load.
- **On-device iPhone inference with MLX Swift** — Build a native iOS app in Swift on the MLX Swift framework, which runs models on Apple Silicon unified memory through the Metal GPU. The app downloads the 0.8B model on first open. Enable airplane mode, then prompt. The speaker says the repo is linked in the video description, which the transcript does not include. *When:* Offline or on-device features on Apple hardware where data should not leave the phone.
- **Five-prompt probe battery for tiny multimodal models** — Run the same prompts on each model: a greeting (to check identity), the car-wash reasoning trick question, a photo of a banana (identify it and judge ripeness), a dog photo (breed), and a photo of printed text (identify the language). Judge the answers by hand. *When:* A quick sanity check before deeper evals. This is anecdotal, single-run testing, not a benchmark.

## Numbers
- Qwen 3.5 2B scores 66.5 on MMLU; 0.8B scores 42.3 (as reported in the video) ([1:18](https://youtu.be/hQoF_dv2UQ4?t=78))
- Llama 2 7B (2023) scored 45.3 on MMLU, cited as a comparison point ([1:18](https://youtu.be/hQoF_dv2UQ4?t=78))
- OCRBench: 2B scores 85.4, 0.8B scores 79.1 ([2:29](https://youtu.be/hQoF_dv2UQ4?t=149))
- Both models advertise a 262k-token context window ([2:29](https://youtu.be/hQoF_dv2UQ4?t=149))
- 0.8B cafe-website build took roughly 1 minute offline ([3:36](https://youtu.be/hQoF_dv2UQ4?t=216))
- 2B cafe-website build took roughly 3 minutes offline (with looping on fixes) ([5:54](https://youtu.be/hQoF_dv2UQ4?t=354))
- IBM Granite 4.0 nano is about 300M parameters (comparison point) ([0:00](https://youtu.be/hQoF_dv2UQ4?t=0))

## Hot takes
- The 0.8B model is not viable for real coding; the 2B's repetition loops also make offline coding unreliable in this LM Studio plus Cline setup.
- Despite inconsistent answers, these are the most powerful tiny models the host has used, and running a native multimodal LLM offline on an iPhone 14 Pro is impressive.
- Tiny models hallucinate confidently: the 0.8B misidentified Latvian as Slovenian and invented a translation.
- Caveat: the tests are single-run and anecdotal. The host himself suspects the loops are a LM Studio or Cline configuration issue rather than the model.
- The benchmark numbers are quoted from the release, not verified in the video. The Qwen team departure report is unconfirmed, and the speaker says so only by calling it reported.

## Tools mentioned
Qwen 3.5 (0.8B and 2B, GGUF builds), LM Studio, Cline (VS Code extension; transcribed as 'Klein' and 'Climb'), MLX / MLX Swift, Swift / Xcode-style iOS app, Metal GPU, IBM Granite 4.0 nano (mentioned), Llama 2 7B (mentioned as a comparison point), Unsplash (image URLs the model hard-coded), OCRBench (benchmark named), MMLU (benchmark named)

## Relevance to our work
- **agentos** (1/3): A sub-3B multimodal model that runs offline on a laptop or phone could serve as a low-cost local tier. The video gives no serving benchmarks, and the repetition loops would matter for agent turns. → *Add Qwen3.5-2B as a small-tier baseline in the InferCraft model matrix, and check for repetition loops under the server's sampling settings before using it for agent turns.*

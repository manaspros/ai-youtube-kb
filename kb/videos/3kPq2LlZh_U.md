# AI vs GeoGuessr Pro

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `3kPq2LlZh_U` · [watch](https://youtu.be/3kPq2LlZh_U) · **date:** 2025-11-02 · **length:** 6:00 · **format:** demo · **quality:** 2/5 · **depth:** intro
- **speakers:** ZigZag (GeoGuessr World Cup player, human challenger) · **orgs:** OpenAI, Better Stack, GeoGuessr, Google
- **topics:** models-research, voice-multimodal · **tags:** o3, chatgpt, geoguessr, vision, image-geolocation, reasoning-models, benchmark-demo, street-view

> Better Stack pits OpenAI's o3 (screenshot only, no web search) against GeoGuessr pro ZigZag over five rounds; o3 wins 22,197 to 21,379 on the video's totals.

## Summary
The video sets OpenAI's o3 model against ZigZag, a GeoGuessr World Cup player, in a five-round location-guessing game with no panning, zooming or moving. o3 gets a screenshot plus a prompt that says to play GeoGuessr and not to use the web, including to look up text visible in the image. ZigZag's reasoning is taken from his second channel. The presenter reads o3's reasoning trace, which shows it cropping and re-examining parts of the image several times before guessing. o3 leads on rounds 1, 2 and 4 and loses rounds 3 and 5 narrowly, so the total is a close win for the model. Per-round o3 scores in the transcript add up to 22,126, not the 22,197 the presenter states, which suggests a transcription or on-screen number error. The presenter treats the result as a dystopian milestone, but the evidence is one run over five locations, and the entertainment framing and the unverified Street View speculation make it weak support for any engineering conclusion.

## Key ideas
- **Setup: the test gives o3 only a screenshot and a prompt to play GeoGuessr. The prompt forbids web search, including for text in the image, so the model must work from visual cues alone, the same constraint a human player has.** — Both players get no panning, moving or zooming. The presenter's stated reason for banning web search is that a readable restaurant name or domain could give away the location. ([0:00](https://youtu.be/3kPq2LlZh_U?t=0))
- **Round 1 (Australia): o3 wins 4,889 to 4,713. ZigZag reads double white lines, black-and-yellow chevrons and red guardrail reflectors. o3 cites vegetation, road markings, chevrons and overall landscape, and takes 1:38.** — The presenter says o3 uses internal tools to crop the image and re-examine parts of it several times before committing to a pin. ([1:06](https://youtu.be/3kPq2LlZh_U?t=66))
- **Round 2 (southeast Oklahoma): o3 wins 4,319 to 3,718. ZigZag uses the trees, double yellow lines and the spacing between them. o3 cites the double solid yellow line, the missing paved shoulder typical of minor US highways, a pine and broadleaf mix, and a barbed-wire fence on private cattle land.** — o3 took 3:44 for this round. ([2:20](https://youtu.be/3kPq2LlZh_U?t=140))
- **Round 3 (Colombia): ZigZag wins 3,624 to 3,523, the first round the human wins. The sign text and the yellow rear plate are the key cues. o3 takes 6:57, cites right-hand traffic, concrete roads, a power pole design and a pig-rearing reference, and reads the text on a sign.** — The presenter calls the black cross on the back of a road sign a piece of GeoGuessr knowledge that players remember. ([3:28](https://youtu.be/3kPq2LlZh_U?t=208))
- **Round 4 (northern Norway): o3 wins 4,608 to 4,533. ZigZag reads the long dashed road markings as Norway. o3 takes 8:10 and uses midnight-sun glare plus the compass direction of the sun.** — This is the longest o3 response time in the video. ([3:28](https://youtu.be/3kPq2LlZh_U?t=208))
- **Round 5 (Tunisia): ZigZag wins 4,791 to 4,787, so o3 loses the final round by four points. The antenna on the Street View car and a telecom mast point to Tunisia. o3 is fast here, at 0:44.** — o3 cites right-hand traffic, white dashed centre lines and the mast. The presenter credits the human's knowledge of the Street View car as the best GeoGuessr meta in the video. ([4:43](https://youtu.be/3kPq2LlZh_U?t=283))
- **Final totals as stated: o3 22,197, ZigZag 21,379. The presenter concludes that a skill that once belonged to a few experts is now available to anyone with a chat window, and speculates that o3 may have Street View training data.** — The speculation about Street View training data is unverified, and the presenter says Google would likely lock such data down for its Gemini models. ([4:43](https://youtu.be/3kPq2LlZh_U?t=283))

## Techniques
- **Blind visual-geolocation eval with a human expert as baseline** — Show a vision model a single image with a task prompt. Forbid web search and text-based lookup, and keep the image fixed. Score the guess against the ground truth and compare it with an expert's reasoning, as the video does by comparing against ZigZag's stated clues. Score per round, then total. *When:* A quick, informal check of whether a multimodal model reasons from visual cues rather than memorised facts. Use it when you want a human-readable comparison, not a rigorous benchmark, because a five-location sample is too small to draw conclusions.
- **Reading the reasoning trace for the cues a model used** — Inspect the model's visible reasoning and check each cited cue (road markings, plate colours, vegetation, signage text) against the image, instead of trusting the final answer. The presenter does this to see that o3 cites specific visual evidence and repeatedly crops and re-inspects image regions. *When:* When assessing vision reasoning quality, or when deciding whether a multimodal agent's conclusions are grounded in what it saw.

## Numbers
- Round scores (o3 vs ZigZag): R1 4,889 vs 4,713; R2 4,319 vs 3,718; R3 3,523 vs 3,624; R4 4,608 vs 4,533; R5 4,787 vs 4,791. ([1:06-4:43](https://youtu.be/3kPq2LlZh_U?t=0))
- Stated totals: o3 22,197 vs ZigZag 21,379. The o3 per-round scores sum to 22,126, which is 71 points less than the stated total. The ZigZag scores sum to 21,379, which matches. ([4:43](https://youtu.be/3kPq2LlZh_U?t=283))
- o3 response times per round: R1 1:38, R2 3:44, R3 6:57, R4 8:10, R5 0:44. ([1:06-4:43](https://youtu.be/3kPq2LlZh_U?t=0))
- Sample size: one run, five locations, one human challenger. ([0:00](https://youtu.be/3kPq2LlZh_U?t=0))

## Hot takes
- The result is one run over five locations against one player, so it says little about general vision reliability. The presenter's 'it's over for humans' framing goes beyond what the test shows.
- The o3 total in the video does not match its per-round scores (22,126 from the rounds vs 22,197 stated). Treat the headline number as unverified.
- The presenter's claims that o3 may have Street View training data and that a Google lockdown is likely are speculation with no evidence in the video.
- The tool-based cropping behaviour is taken from the visible reasoning shown in the ChatGPT interface, not from any documented API behaviour.
- Quality is capped low because the video is entertainment with thin technical substance, and the scoring rules allow no more than 2 for that kind of content.

## Tools mentioned
ChatGPT, OpenAI o3, GeoGuessr, Google Street View

## Relevance to our work
- **general** (1/3): The blind test against a human expert, with the reasoning trace compared to the expert's stated cues, is a cheap eval format that could be adapted for judging multimodal outputs. → *Low priority: note the blind expert-vs-model comparison with trace review as an informal eval idea; no change is needed to any project.*

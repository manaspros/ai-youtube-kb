# The Prompt Is Still a Punch Card - Ted Johnson, JoinIn AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `hVJOnuhFmTA` · [watch](https://youtu.be/hVJOnuhFmTA) · **date:** 2026-07-18 · **length:** 20:13 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Ted Johnson · **orgs:** JoinIn AI, NVIDIA, OpenAI, MIT
- **topics:** voice-multimodal, product-ux, context-engineering · **tags:** prompt-as-punch-card, turn-taking, speech-to-speech, backchannel, addressee-detection, group-conversation-agent, floor-control, interface-design, batch-vs-interactive, approval-workflow

> Ted Johnson (JoinIn AI) argues that prompting is a batch-style punch-card protocol that leaves users doing the work, and that AI interfaces should become turn-taking, conversation-like, and aware of who is being addressed.

## Summary
Ted Johnson, co-founder of JoinIn AI, frames the chat prompt box as a punch-card protocol: you assemble a full request, submit it, wait, then read and repair the output. He uses three concepts: the channel (the physical medium, which has barely changed), expression (how much meaning the channel can carry, which LLMs have greatly widened), and the protocol (the rules of the exchange, which he says has not advanced). He argues that faster batch, voice input, and added follow-up features are still batch, and that users blame themselves for a mismatch that is really in the interface. He shows a voice-mode failure where the model answered a sentence not addressed to it, and a research demo (NVIDIA Personaplex, not JoinIn's) that yields and resumes when interrupted. He then demos JoinIn's group-meeting assistant, which labels statements (question, proposal, answer), speaks only when no one holds the floor, and changes an expense-approval threshold from $5,000 to $10,000 by voice. He closes with a design question: what burden are we still putting on humans only because machines used to be too limited to carry it. Most of the talk is framing, and the product demo is a showcase with no benchmarks.

## Key ideas
- **Prompting is a batch protocol, not a new skill** — The user packages a whole request, submits it, waits, then repairs the output. Speaker says prompt tips (step by step, personas, markdown) are rules for packaging batch and that the protocol is what has not advanced. ([7:16](https://youtu.be/hVJOnuhFmTA?t=436))
- **Channel, expression, protocol as three separate axes** — The channel (keyboard, mic, screen) carries bandwidth. Expression is how much meaning gets through, which LLMs have widened a lot. The protocol (turn rules, shape of exchange) has lagged behind. ([1:31](https://youtu.be/hVJOnuhFmTA?t=91))
- **Expression grew, but the channel stayed a box** — Shell, languages, and natural language each widened what a user can say. Natural language opened the menu, yet the user still types into a box and presses submit. ([4:21](https://youtu.be/hVJOnuhFmTA?t=261))
- **Model capability rises while interface effort stays with the human** — The human still chooses context, timing, what to ask, and how to repair output. Speaker argues people blame themselves for failures that come from the interface, not from their own use. ([9:39](https://youtu.be/hVJOnuhFmTA?t=579))
- **Single-slot turn protocol cannot tell who is being addressed** — A voice-mode demo answered a sentence the co-founder said to a colleague, because the model only has one slot: your message, then its reply. Speaker says models need to know whether speech was meant for them. ([10:58](https://youtu.be/hVJOnuhFmTA?t=658))
- **Real turn-taking needs yield, resume, and back-channels** — A research speech model (NVIDIA Personaplex) stopped when interrupted and picked the thread back up. Speaker treats back-channel sounds as a basic part of listening, while noting they do not show the model knows who is in the room. ([12:23](https://youtu.be/hVJOnuhFmTA?t=743))
- **Group assistant labels statements and only speaks when the floor is free** — JoinIn's demo classifies each participant statement (question, proposal, answer), acts on goals it creates, and takes a turn only when nobody else is speaking. It then records a decision and changes a threshold on request. ([13:48](https://youtu.be/hVJOnuhFmTA?t=828))

## Techniques
- **Classify each utterance, then act only at a floor-free moment** — Label every participant statement by speech act (question, proposal, answer), keep goals derived from those labels, and speak only when no one else holds the floor. Speaker says the system also tracks who a reference points to when there is no direct address. *When:* Multi-party meetings or shared channels where an assistant should join without being addressed every time.
- **Full-duplex turn-taking with yield and resume** — Model listens while speaking, yields when interrupted, and resumes the earlier thread instead of restarting the answer. Back-channel sounds (mm-hmm, right) show listening. *When:* Voice agents where a user may interrupt or talk while the model is speaking.
- **Ask what burden the human still carries** — Audit each step where the user encodes intent, times input, picks the channel, or repairs output. Remove those steps by letting the AI ask follow-ups, clarify mid-thought, or choose the channel. *When:* Designing an AI product flow, to decide where the interface should take over from the user.
- **Voice-driven record edits in a meeting** — Speaker shows a spoken edit (threshold changed from $5,000 to $10,000) that updates a stored requirement, after the assistant asks for confirmation. *When:* Capturing decisions and requirement changes during live meetings.

## Numbers
- Keyboard layout patent drawing dates to about 1860 (speaker's note on the QWERTY-era layout) ([1:31](https://youtu.be/hVJOnuhFmTA?t=91))
- Channels for computers have stayed much the same for about 15 years, and some ~180 years in the sense of keyboard lineage ([5:49](https://youtu.be/hVJOnuhFmTA?t=349))
- Speaker says humans adapted to machines for 75 years (syntax, forms, timing, batch) ([17:24](https://youtu.be/hVJOnuhFmTA?t=1044))
- OpenAI released GPT Realtime 2 in late May, with back-channel behavior in voice mode ([10:58](https://youtu.be/hVJOnuhFmTA?t=658))
- Meeting demo: expense approvals under a threshold need one tap; over the threshold a second approver is routed in; changed to $10,000 by voice (transcript states $5,000 and an unclear 'under 5' figure) ([14:50](https://youtu.be/hVJOnuhFmTA?t=890))
- Speaker says the wait for interactive AI shrank from overnight batch to seconds or minutes, but the protocol stayed batch ([7:16](https://youtu.be/hVJOnuhFmTA?t=436))

## Hot takes
- The prompt is still a punch card. Faster batch is still batch, and the protocol is the part that has not advanced.
- Users are not bad at AI. The mismatch is the interface, not the person.
- Prompt engineering is a set of rules for packaging batch, and it feels like mastery but is the same skill a punch-card operator had.
- AI is increasingly an interface technology, not just an intelligence technology.

## Tools mentioned
NVIDIA Personaplex, OpenAI GPT Realtime 2

## Relevance to our work
- **prosharness** (1/3): Phone-driven approvals is a ProsHarness feature; the talk's demo routes approvals above a threshold to a second approver. → *Consider threshold-based second-approver routing for ProsHarness approvals; no work needed beyond noting the pattern.*
- **general** (1/3): Speaker argues prompts are packaged batch and that the human should not carry context and timing burden. Relevant to the context-engineering interest, though no concrete method is given. → *Use the 'what burden is still on the human' question as a review checklist when designing agent prompts and handoffs.*

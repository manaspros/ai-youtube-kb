# Google Just Made A HISTORICAL Quantum Breakthrough!

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `HQEZLSEzxOA` · [watch](https://youtu.be/HQEZLSEzxOA) · **date:** 2025-11-02 · **length:** 8:32 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** Andres · **orgs:** Google, Better Stack
- **topics:** models-research · **tags:** quantum computing, Google Willow, Quantum Echoes, OTOC, verifiable quantum advantage, error correction, hybrid computing

> Explainer on Google's Quantum Echoes run on the 105-qubit Willow chip, presented as the first verifiable quantum advantage, with background on qubits, OTOCs and why the result can be checked.

## Summary
Better Stack presents Google's Quantum Echoes experiment on its 105-qubit Willow chip as a verifiable quantum advantage, contrasting it with the 2019 Sycamore supremacy claim that critics said could not be independently checked. The explainer covers superposition, entanglement and decoherence, then describes the protocol: run a circuit forward, perturb one qubit, run it backward, and measure how far the echo deviates, which gives an out-of-time-order correlator (OTOC). The speaker says Willow finished the task about 1300 times faster than the best classical simulation. Verification works by running the same circuit on smaller qubit counts where a classical supercomputer can match the quantum result, then scaling up to 105 qubits where classical simulation is no longer feasible. The video closes with speculation about future developer SDKs that offload calls to quantum processors, and Google's roadmap milestone of a long-lived error-corrected logical qubit. The content is general background with few hard details, and the title and framing are stronger than the substance.

## Key ideas
- **Quantum Echoes on Willow is pitched as the first verifiable quantum advantage; the 2019 Sycamore claim was criticized because its output could not be checked independently.** — The speaker's main framing: the new result matters because its output can be validated, a requirement for the word 'verifiable'. ([0:00](https://youtu.be/HQEZLSEzxOA?t=0))
- **The protocol runs a circuit forward, perturbs one qubit, then runs it backward; the echo's deviation from the original state measures how quantum information spreads and scrambles.** — Described as measuring an out-of-time-order correlator (OTOC). Analogy used: a pebble dropped in a still pond, then time run backward to see whether the ripples cancel. ([3:02](https://youtu.be/HQEZLSEzxOA?t=182))
- **The experiment is hard because every gate must be very precise; small noise makes the echo collapse into randomness.** — The speaker credits better calibration, timing control and gate fidelity on Willow for making the echo survive. Qubits also need near-absolute-zero operation. ([3:57](https://youtu.be/HQEZLSEzxOA?t=237))
- **The speaker says Willow finished the task about 1300 times faster than the best classical simulation.** — Single headline speedup figure in the video; no methodology or classical baseline details are given. ([3:57](https://youtu.be/HQEZLSEzxOA?t=237))
- **Verification scales up from small circuits: quantum and classical runs are compared where classical simulation still works, then the same method is run at 105 qubits.** — Results matched at small sizes, which the speaker treats as validation of the method before it is applied where classical machines cannot follow. ([5:09](https://youtu.be/HQEZLSEzxOA?t=309))
- **Quantum Echoes is described as a mathematical procedure rather than a proprietary chip operation, so it could in principle run on other hardware with similar gate operations.** — Speaker's claim with the qualifier 'in principle'; no cross-hardware experiment is shown. ([5:09](https://youtu.be/HQEZLSEzxOA?t=309))
- **The speaker expects quantum to follow the GPU path: specialist use first, then SDKs where developers call quantum routines from Python.** — Speculative: compiler optimization, ML and molecular or materials simulation are named as possible targets. Google's next milestone is a long-lived logical qubit with full error correction. ([6:17](https://youtu.be/HQEZLSEzxOA?t=377))

## Techniques
- **Echo-based (OTOC) probe of a quantum system** — Apply a sequence of gates forward, perturb a single qubit mid-circuit, apply the inverse sequence, then measure how far the final state deviates from the original. The deviation shows how information spread and scrambled. *When:* Studying how quantum information propagates in a device; useful as a sensitive probe of gate fidelity and noise.
- **Scale-up verification against classical simulation** — Run the same circuit on the quantum device and on a classical supercomputer at a size where classical simulation is still feasible. Confirm the outputs match, then run the quantum device at a size classical methods cannot reach. *When:* Any quantum or hard-to-simulate result that must be trusted beyond the classical-simulation limit. Generalizes to any claim where the output can be validated only at small scale.

## Numbers
- Willow has 105 qubits; the verified circuit is the full 105-qubit size. ([0:46](https://youtu.be/HQEZLSEzxOA?t=46))
- Willow ran the task about 1300 times faster than the world's best classical simulation (speaker's figure, no baseline details). ([3:57](https://youtu.be/HQEZLSEzxOA?t=237))
- Willow operates near absolute zero, which the speaker describes as colder than outer space. ([1:49](https://youtu.be/HQEZLSEzxOA?t=109))
- Google's 2019 Sycamore supremacy claim is the earlier reference point. ([0:00](https://youtu.be/HQEZLSEzxOA?t=0))

## Hot takes
- The 'HISTORICAL' title and 'verifiable quantum advantage has finally been achieved' overstate what the video itself shows; no primary paper or data is cited.
- Much of the runtime is generic qubit background. The protocol explanation is short, and the speedup figure comes without a stated classical baseline.
- The SDK and Python-offload future is speculation presented as the likely path, not a finding from the experiment.
- Auto-caption renders the perturbation step oddly ('flipped or... protruded'); the intended word is most likely 'perturbed'.

## Tools mentioned
Google Willow (105-qubit quantum chip), Google Sycamore (2019 quantum chip), Quantum Echoes (algorithm)

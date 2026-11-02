# The Internet Is Torturing a Fruit Fly... (opensource brain)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `KOwsVDogscY` · [watch](https://youtu.be/KOwsVDogscY) · **date:** 2026-10-02 · **length:** 6:26 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed Better Stack host · **orgs:** Google, Janelia Research Campus, Better Stack
- **topics:** models-research · **tags:** connectome, fruit-fly, electron-microscopy, flood-filling-network, neuroscience, open-data, viral-demos, learned-readout

> Better Stack on Google and Janelia's open-sourced male fruit fly connectome (MaleCNS v1): how it was mapped, and why viral "fly plays games" demos are trained readouts, not simulated brains.

## Summary
The host covers Google and Janelia Research Campus releasing the wiring diagram of a male fruit fly's brain and nerve cord, MaleCNS Version 1, as open data. It opens with viral demos of the connectome driving a fly in Minecraft, Beat Saber, Doom, a Bitcoin trade and a social network, and says most of them carry heavy caveats. The dataset comes from slicing one fly into about 134,000 sections of roughly 8 nm, imaging them with an electron microscope, and tracing neurons with a flood-filling network; the result has about 166,000 cell bodies and about 125 million synapses. The host then builds a toy version himself: 80 real cells, eyes pointed at a subscribe button, and a reward signal for cursor position, trained for about 200,000 attempts. He stresses that the map shows wiring but not connection strength or what the cells do, so he set every weight equal and used a small learned readout with 163 parameters to choose moves. He cites one validation, where switching off a neuron type reproduced a 2015 real-fly courtship result, and notes that a female connectome now exists too, with about 5% of the central brain sex-specific. Zebrafish and mouse are next; the human brain is out of reach.

## Key ideas
- **The viral fly demos are not a sentient brain running a game. A person decides what the inputs mean, someone guesses how the cells behave, and a trained network on top does the playing.** — The host says the demos all share this structure and that the 'sentient fly' framing is a joke. He treats the connectome as the wiring, not the behavior. ([4:43](https://youtu.be/KOwsVDogscY?t=283))
- **The dataset is MaleCNS v1: a wiring map, not a simulation.** — It holds about 166,000 cell bodies and about 125 million synaptic connections across the optic lobes, central brain and descending neurons. It tells you which neuron connects to which and how many synapses sit between them, but not connection strength or what happens when a signal travels. ([2:11](https://youtu.be/KOwsVDogscY?t=131))
- **The map was made by serial-section electron microscopy plus automated tracing.** — One fly was sliced into about 134,000 sections of roughly 8 nm each and imaged with an electron microscope. A flood-filling network starts from one pixel and grows through every section to collect all pixels belonging to the same neuron. ([2:11](https://youtu.be/KOwsVDogscY?t=131))
- **The escape circuit shows how dense the wiring is around a single neuron.** — The giant fiber, which drives the escape jump, receives nearly 25,000 synapses from over 3,000 other cells. The looming detectors, which fire on fast-approaching objects, have about 6,500 synapses between them. ([3:33](https://youtu.be/KOwsVDogscY?t=213))
- **The host's own toy experiment: 80 real cells, eyes on a subscribe button, a reward signal, and a random-search readout.** — Screen position goes into the input cells, all synaptic weights are set equal, and a 163-parameter translator chooses left, right or click. Random settings are tried and the best are kept, for about 200,000 attempts, until the success rate reached 100%. ([2:11](https://youtu.be/KOwsVDogscY?t=131))
- **The most credible claim is a lesion check against published biology.** — Switching off one neuron type in the model changed the courtship neurons the same way a 2015 real-fly experiment did. The host argues this is why the data is worth having, unlike the entertainment demos. ([4:43](https://youtu.be/KOwsVDogscY?t=283))
- **Two complete connectomes now exist, one male and one female.** — About 5% of the central brain is sex-specific, and that is where courtship and aggression circuits sit. Comparing them shows the wiring differences, and the similar parts show how much wiring varies between individuals of one species. ([4:43](https://youtu.be/KOwsVDogscY?t=283))
- **Next steps are zebrafish, then mouse. The human brain, at 86 billion neurons, is still out of reach.** — Janelia and Google are reportedly working on a zebrafish brain and then a mouse brain. The host says the human brain is not yet feasible. ([5:50](https://youtu.be/KOwsVDogscY?t=350))

## Techniques
- **Seeded flood-fill segmentation for neuron reconstruction** — Start at one voxel of a labeled neuron in a serial EM volume and grow outward through the 3D volume, collecting every voxel that belongs to the same neuron across all sections. The video names the flood-filling network (FFN) as the method used. *When:* Reconstructing individual cells from dense 3D imaging (EM or similar) where manual tracing does not scale.
- **Structure-only network with a learned readout** — Map observations onto input neurons, route them through a fixed wiring graph with uniform weights, then train a small readout (here 163 parameters) that maps the output units to actions. Train by random search: try random settings, keep the best, and repeat for about 200,000 trials, using a reward tied to a measurable target. *When:* Demonstrating or testing what a wiring diagram can do when its parameters are unknown. It also shows why a trained readout, not the graph, may be doing the work in a demo.
- **Lesion test of a circuit model against published experiments** — Switch off one cell type in the model, record the change in another population's activity, and compare it with a published real-animal experiment. The host cites a 2015 courtship experiment as the reference. *When:* Validating a biologically derived model before trusting its predictions. The same idea applies to ablation checks on any learned system.
- **Using the public connectome data** — The video names three access points: NeuroGlancer, a web viewer for the image volumes; neuPrint, a query interface with Python and R packages for the connectivity tables; and downloadable raw image volumes and connectivity tables. *When:* Querying synapse counts between neuron types or pulling connectivity tables for analysis or modeling.

## Numbers
- Over 166,000 cell bodies in MaleCNS v1 ([2:11](https://youtu.be/KOwsVDogscY?t=131))
- About 125 million synaptic connections in the connectome; the table has about 125 million rows ([2:11](https://youtu.be/KOwsVDogscY?t=131))
- About 134,000 serial sections, each about 8 nm thick, imaged with an electron microscope ([2:11](https://youtu.be/KOwsVDogscY?t=131))
- A single synapse is visible at roughly 100x zoom ([2:11](https://youtu.be/KOwsVDogscY?t=131))
- The giant fiber has nearly 25,000 synapses from over 3,000 other cells ([3:33](https://youtu.be/KOwsVDogscY?t=213))
- The looming detectors have nearly 6,500 synapses between them ([3:33](https://youtu.be/KOwsVDogscY?t=213))
- The host's toy circuit uses 80 real cells, a 163-parameter readout, and about 200,000 training attempts to reach 100% subscribe success ([2:11](https://youtu.be/KOwsVDogscY?t=131))
- The Doom demo had over 8,000 attempts and had not beaten the game at the time of recording ([0:56](https://youtu.be/KOwsVDogscY?t=56))
- A fly trading Bitcoin with $100 reportedly beat many day traders (demo claim, unverified) ([0:56](https://youtu.be/KOwsVDogscY?t=56))
- About 5% of the central brain is sex-specific (courtship and aggression circuits) ([4:43](https://youtu.be/KOwsVDogscY?t=283))
- The human brain has about 86 billion neurons and is still out of reach ([5:50](https://youtu.be/KOwsVDogscY?t=350))

## Hot takes
- The viral 'fly plays Minecraft/Doom/Bitcoin' demos mostly test a trained readout on top of an unweighted wiring graph, not the connectome itself. The host says so himself.
- The title, 'The Internet Is Torturing a Fruit Fly', is clickbait relative to the content, which is a mostly accurate explainer of a neuroscience dataset with little AI engineering substance.
- The lesion-versus-2015-experiment check is the strongest evidence in the video, but the host gives no numbers for it.
- The 'Fly Slop' framing is a joke, and the host doubts the demos are close to a real achievement. It is a sober take on hype, not a claim about the science.

## Tools mentioned
MaleCNS Version 1 (connectome dataset), NeuroGlancer (web viewer), neuPrint (query interface, Python and R packages), Flood-filling network (FFN) for neuron segmentation, Electron microscopy (serial-section imaging), Minecraft (demo environment), Beat Saber (demo environment), Doom (demo environment)

## Relevance to our work
- **general** (1/3): The video's main lesson for AI engineering is that a demo of a learned system can be carried by its trained readout, not the structure it claims to show. That matters for evaluating agent demos. → *When reviewing an agent demo, run an ablation that removes the claimed structure (or randomizes it) and check whether the result still holds.*

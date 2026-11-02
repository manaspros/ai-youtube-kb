# How Transformers Finally Ate Vision – Isaac Robinson, Roboflow

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `VhfAVA3BG2I` · [watch](https://youtu.be/VhfAVA3BG2I) · **date:** 2026-05-18 · **length:** 17:05 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Isaac Robinson · **orgs:** Roboflow
- **topics:** models-research, training-finetuning-rl, inference-serving · **tags:** vision-transformer, masked-autoencoder, pretraining, inductive-bias, flash-attention, SAM3, neural-architecture-search, edge-deployment, linear-probe, RF100-VL, Hiera, ConvNeXt, Swin, DINOv3

> Isaac Robinson (Roboflow) traces how plain ViTs beat CNN and hybrid backbones, crediting massive ViT-specific pretraining, borrowed LLM speedups, and NAS over one foundation model for deployable vision.

## Summary
Robinson argues that transformers beat convolutional vision backbones not because of their architecture but because of large ViT-specific pretraining (especially masked autoencoding), plus speedups borrowed from LLM infrastructure such as FlashAttention. He walks through the lineage: ViT, then Swin (windowed attention), ConvNeXt (a convnet borrowing transformer structure), and Hiera (a stripped-down biased transformer), which each lose to the plain ViT once pretraining and attention kernels are considered. He shows that self-supervised ViT features (DINOv2/v3) reach near-supervised quality with only a linear probe. The SAM family follows the same pattern, but the resulting models are large and slow for deployment, with SAM3 at 800M parameters and about 300 ms on a T4. Roboflow's response is RF100-VL, a transfer benchmark, and a neural architecture search that derives a family of deployable detectors and segmenters from one pretrained foundation backbone, reporting roughly 40x speedup at equal accuracy versus fine-tuning SAM3. The talk ends with a three-part recipe: ViT pretraining, LLM-derived speedups, and pretraining-compatible NAS. The speaker is candid that the field's answer is "the simple thing that scales," and that video equivalents like V-JEPA have not yet shown clear downstream gains.

## Key ideas
- **Transformers won vision by scale, not architecture** — The speaker's thesis: plain ViTs beat biased CNN and hybrid designs because of massive ViT-specific pretraining, plus speedups borrowed from LLM work. Inductive bias is learned from data instead of built into the architecture. ([0:00](https://youtu.be/VhfAVA3BG2I?t=0))
- **A plain ViT beats a CNN despite having no inductive bias** — CNNs have locality and translation equivariance built in. ViT has none and costs roughly n^4 in resolution, yet it wins on accuracy. The speaker attributes this to pretraining, not to the design. ([2:43](https://youtu.be/VhfAVA3BG2I?t=163))
- **Masked pretraining learns back the inductive biases** — MAE drops most image patches and asks the model to reconstruct them. At scale the model recovers locality-like structure on its own. The catch is that MAE is hard to apply to convnets, so this is a ViT-specific advantage. ([6:47](https://youtu.be/VhfAVA3BG2I?t=407))
- **Biased variants lose their speed edge once attention kernels are used everywhere** — Hiera reported a speedup over ViT without FlashAttention. When FlashAttention is added to the baseline, the speedup largely disappears, so the ViT stays competitive. ([8:52](https://youtu.be/VhfAVA3BG2I?t=532))
- **Foundation models lack deployment flexibility** — SAM3 is about 800M parameters and runs about 300 ms on a T4. One fixed large backbone cannot serve edge hardware, so vision needs a way to derive smaller models from the foundation model. ([11:28](https://youtu.be/VhfAVA3BG2I?t=688))
- **NAS over a pretrained backbone gives a model family** — Roboflow adds flexible knobs that are drop-in compatible with existing foundation-model infrastructure. Mixing them for a target dataset and hardware yields a family of real-time models. The speaker says these beat the prior best real-time convolutional instance-segmentation models. ([13:59](https://youtu.be/VhfAVA3BG2I?t=839))
- **Summary recipe: ViT pretraining, LLM speedups, pretraining-compatible NAS** — The three ingredients together explain the outcome. The speaker says video JEPA-style models have not yet shown clear downstream transfer gains in video. ([15:02](https://youtu.be/VhfAVA3BG2I?t=902))

## Techniques
- **Benchmark attention variants against a FlashAttention baseline** — When claiming a speedup for a new attention or backbone design, rerun the baseline with the same fused attention kernels. Otherwise the gain may disappear. *When:* Any architecture or inference-optimization comparison against a standard transformer.
- **Masked-patch pretraining to instill inductive bias** — Drop most image patches and train the model to reconstruct them from context. Let the pretraining, not the architecture, supply locality and similar structure. *When:* You want a generic backbone that transfers well without hand-designed biases, and you can run large-scale pretraining.
- **Linear-probe check for frozen features** — Freeze the backbone, train only a linear layer on downstream labels, and compare against fully supervised results. This measures feature quality without tuning the backbone. *When:* Judging whether a self-supervised or foundation backbone is good enough to reuse.
- **NAS over a pretrained foundation model** — Expose a few architectural knobs that stay compatible with the foundation model's weights and infrastructure. Search across them for the target dataset and hardware to get a family of models from one pretrained backbone. *When:* A single large foundation model is too slow or too big for the deployment hardware.
- **Transfer benchmark for foundation models** — Measure how well a foundation model transfers to varied downstream detection tasks, using a dataset such as RF100-VL, rather than relying on a single benchmark. *When:* Comparing candidate vision backbones for real downstream use.

## Numbers
- SAM3 has about 800M parameters and takes about 300 ms per run on a T4 GPU ([11:28](https://youtu.be/VhfAVA3BG2I?t=688))
- About 40x speedup at equal accuracy versus fine-tuning SAM3 on RF100-VL object detection ([12:27](https://youtu.be/VhfAVA3BG2I?t=747))
- About 15x speedup still gives a meaningful accuracy improvement ([12:27](https://youtu.be/VhfAVA3BG2I?t=747))
- ViT compute scales as n^4 with image side length n, versus n^2 for convolution ([2:43](https://youtu.be/VhfAVA3BG2I?t=163))
- Original ViT used 16x16 patches; ConvNeXt-style variant used 4x4 patches ([5:15](https://youtu.be/VhfAVA3BG2I?t=315))
- Linear probe on frozen DINOv3 features gets close to the best fully supervised results ([8:52](https://youtu.be/VhfAVA3BG2I?t=532))

## Hot takes
- Transformers won vision because of pretraining and LLM infrastructure, not architecture.
- Pretraining learns back the inductive biases that architectures hard-code.
- Hiera's reported speedup disappears once FlashAttention is used in the baseline.
- SAM3 is too large for most real deployments, so the one-size-fits-all foundation model is a problem.
- The field keeps returning to the simple scalable thing, the plain ViT.

## Tools mentioned
SAM, SAM2, SAM3, MobileSAM, TinyViT, Hiera, ConvNeXt, Swin Transformer, ViT, MAE, DINOv2, DINOv3, FlashAttention, V-JEPA, RF100-VL, RF-DETR (transcribed as 'RF Detter')

## Relevance to our work
- **agentos** (1/3): InferCraft is about serving and attention-kernel choices. The talk's main benchmarking lesson applies there, though its subject is vision backbones. → *When benchmarking any new attention or KV-cache strategy in InferCraft, include a baseline that uses the same fused attention kernels, so the speedup is not an artifact of a slow baseline.*
- **general** (1/3): Speedup claims are easy to inflate. The talk shows that a baseline without standard kernels can exaggerate a gain, which applies to any efficiency comparison. → *For any efficiency claim in our notes or benchmarks, rerun the baseline with the same optimized kernels before reporting the gain.*

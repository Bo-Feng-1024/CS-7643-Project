# Efficient LLM Supervised Fine-Tuning: long dialogue conversations

objectives: 

>  Our project aims to explore alternatives to in-context learning, focusing on efficient supervised fine-tuning techniques.

evaluation benchmark: 

- paper: [Few-shot Fine-tuning vs. In-context Learning: A Fair Comparison and Evaluation](https://github.com/uds-lsv/llmft)

- repo: https://github.com/uds-lsv/llmft
- fine-tuning task: natural language inference (NLI) classification

GPU resource: 

- [PACE-ICE GPU Resources](https://edstem.org/us/courses/60909/discussion/5405752) 

- experience from ppl who use: https://edstem.org/us/courses/60909/discussion/5697429

model selection: 

- baselines: available from opt-125m, opt-350m, opt-1.3b, opt-2.7b, opt-6.7b, opt-13b, opt-30b models.

  - model link 
    - collection: https://huggingface.co/collections/facebook/opt-66ed00e15599f02966818844
    - e.g. (opt-125m): https://huggingface.co/facebook/opt-125m

  - dataset: https://github.com/uds-lsv/llmft

fine tuning methods: 

- baseline methods:
  - Vanilla Fine-Tuning
  - Pattern-based fine-tuning
  - Both combined with BitFIt or LORA
    - LORA:
      - paper:  https://arxiv.org/pdf/2106.09685
      - concept tutorial: https://huggingface.co/docs/peft/main/en/conceptual_guides/lora
      - code tutorial: https://huggingface.co/docs/transformers/v4.46.3/en/peft#transformers.integrations.PeftAdapterMixin
    - BitFit: 
      - paper: https://arxiv.org/pdf/2106.10199
  - llmft repo includes both baseline and combined LORA and BitFit methods. 

- context distillation: 
  - paper: https://arxiv.org/pdf/2112.00861
  - sample repo (not official): https://github.com/DaertML/context_distillation
- Others:
  - 

Evaluation:

> Compare in-domain accuracy and out-of-domain accuracy as shown in the papers. Approaches should also be compared in terms of system resource requirements such as execution time and memory capacity.

# Efficient LLM Supervised Fine-Tuning: Long Dialogue Conversations

## Objectives  

Our project explores alternatives to in-context learning (ICL) by focusing on efficient supervised fine-tuning techniques, such as the **context distillation method**, for the **natural language inference (NLI)** classification task. We aim to compare these techniques with the ICL approach.  

---

Previous work has evaluated various fine-tuning methods (e.g., Vanilla FT, PBFT, LoRA, Context Distillation) but primarily on **CoLA** and **MNLI** datasets.  

- Reference Paper:  
  [Comparative Analysis of Different Efficient Fine-Tuning Methods of Large Language Models (LLMs) in Low-Resource Settings](https://arxiv.org/pdf/2405.13181v1)  

- Related Repository:  
  [iamvarada/llm_finetuning](https://github.com/iamvarada/llm_finetuning)  

---

## Evaluation Benchmark  

- Reference Paper:  
  [Few-shot Fine-tuning vs. In-context Learning: A Fair Comparison and Evaluation](https://github.com/uds-lsv/llmft)  

- Repository:  
  [uds-lsv/llmft](https://github.com/uds-lsv/llmft)  

- **Fine-tuning Task**:  
  Natural Language Inference (NLI) Classification  

---

## GPU Resources  

- [PACE-ICE GPU Resources](https://edstem.org/us/courses/60909/discussion/5405752)  
- Feedback from other users: [Discussion Link](https://edstem.org/us/courses/60909/discussion/5697429)  

---

## Model Selection  

- **Baselines**:  
  Available models include **OPT-125M**, **OPT-350M**, **OPT-1.3B**, **OPT-2.7B**, **OPT-6.7B**, **OPT-13B**, and **OPT-30B**.  

  - Model Collection: [HuggingFace Facebook/OPT Collection](https://huggingface.co/collections/facebook/opt-66ed00e15599f02966818844)  
  - Example Model (OPT-125M): [HuggingFace OPT-125M](https://huggingface.co/facebook/opt-125m)  

---

## Dataset  

- Repository: [uds-lsv/llmft](https://github.com/uds-lsv/llmft)  

---

## Fine-Tuning Methods  

### Baseline Methods  

1. **Vanilla Fine-Tuning**  
2. **Pattern-based Fine-Tuning (PBFT)**  
3. **BitFit and LoRA (Combined with Vanilla FT and PBFT)**  
   - **LoRA**:  
     - Paper: [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/pdf/2106.09685)  
     - [Concept Tutorial](https://huggingface.co/docs/peft/main/en/conceptual_guides/lora)  
     - [Code Tutorial](https://huggingface.co/docs/transformers/v4.46.3/en/peft#transformers.integrations.PeftAdapterMixin)  
   - **BitFit**:  
     - Paper: [BitFit: Parameter-efficient Fine-tuning](https://arxiv.org/pdf/2106.10199)  
4. **Combined Baselines**: Available in the [uds-lsv/llmft repository](https://github.com/uds-lsv/llmft).  

### Context Distillation  

- Paper: [Context Distillation](https://arxiv.org/pdf/2112.00861)  
- Sample Repository (Unofficial): [DaertML/context_distillation](https://github.com/DaertML/context_distillation)  

### Additional Methods  

- To Be Determined (TBD)  

---

## Evaluation Criteria  

1. **Accuracy**:  
   Compare **in-domain** and **out-of-domain** accuracy as outlined in the reference papers.  

2. **Resource Requirements**:  
   Evaluate execution time and memory consumption for each approach.  

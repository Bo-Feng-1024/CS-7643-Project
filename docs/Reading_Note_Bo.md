# Reading Note: 

by Bo Feng

---

## **Paper Summary: Comparative Analysis of Different Efficient Fine-Tuning Methods of Large Language Models (LLMs) in Low-Resource Settings**

### **Title**

Comparative Analysis of Different Efficient Fine Tuning Methods of Large Language Models (LLMs) in Low-Resource Setting

### **Authors**

Krishna Prasad Varadarajan Srinivasan, Prasanth Gumpena, Madhusudhana Yattapu, Vishal H. Brahmbhatt

------

### **Abstract Overview**

This paper investigates the efficacy of various fine-tuning techniques for large language models (LLMs) in low-resource settings. Building on prior work highlighting the generalization properties of full-model fine-tuning methods like Vanilla Fine Tuning (FT) and Pattern-Based Fine Tuning (PBFT) as well as In-Context Learning (ICL), the study aims to expand understanding through a comparative analysis. Key findings include:

- Context distillation outperforms traditional fine-tuning methods in certain setups.
- Adaptive fine-tuning and Low-Rank Adaptation (LoRA) exhibit comparable performance but are resource-efficient alternatives.
- The choice of a fine-tuning method should align with task adaptability and available computational resources.

------

### **Key Contributions**

The study performs a comprehensive evaluation of LLM fine-tuning strategies using two datasets: COLA and MNLI. The methods analyzed include:

1. **Vanilla Fine Tuning (FT)**
2. **Pattern-Based Fine Tuning (PBFT)**
3. **Low-Rank Adaptation (LoRA)**
4. **Context Distillation (with and without few-shot learning)**

------

### **Datasets**

1. **MNLI**: Multi-Genre Natural Language Inference dataset containing sentence pairs annotated for entailment relations. Training utilized 261,802 examples via GLUE, with the HANS dataset serving as out-of-domain data.
2. **COLA**: Corpus of Linguistic Acceptability designed to test grammatical nuances. The dataset includes binary labels for grammatical acceptability.

------

### **Fine-Tuning Techniques**

1. **Vanilla Fine Tuning (FT)**
   - Standard model fine-tuning without prompts.
   - Applied to OPT 125M and OPT 350M models.
2. **Pattern-Based Fine Tuning (PBFT)**
   - Incorporates task-specific prompts and patterns for improved guidance during training.
3. **Adaptive Fine Tuning**
   - Employs freezing layers and dynamic learning rates to selectively train the model.
4. **Low-Rank Adaptation (LoRA)**
   - Reduces model parameterization by decomposing weight matrices into smaller, low-rank matrices.
5. **Context Distillation**
   - Combines distillation and classification loss for fine-tuning. The process is computationally efficient and performs well with in-domain data.

------

### **Experiment Results**

#### **Vanilla Fine Tuning**

- Increasing sample size improves in-domain accuracy for smaller models like OPT 125M but has diminishing returns for larger models (OPT 350M).
- Out-of-domain accuracy remains relatively stagnant across sample sizes.

#### **Pattern-Based Fine Tuning (PBFT)**

- Larger few-shot sizes yield better performance.
- OPT 350M model achieves slight out-of-domain accuracy gains at larger sample sizes.
- Improved prompts could enhance performance but were not explored further in this study.

#### **Adaptive Fine Tuning**

- Performance improves as sample size increases but remains lower than full-model fine-tuning due to selective training of the last layers.

#### **Low-Rank Adaptation (LoRA)**

- Shows a positive trend with increasing training data but plateaus or decreases at larger few-shot sizes.
- Performance is limited when applied to sequence classification tasks on OPT models.

#### **Context Distillation**

- Outperforms traditional fine-tuning in in-domain accuracy.
- Few-shot distillation enhances resource efficiency, achieving comparable results in much less time (5 minutes vs. 1 hour 51 minutes for traditional methods).
- Out-of-domain performance varies and is generally less consistent.

------

### **Challenges and Insights**

1. **Training Instability**: Model performance across methods can be unstable. Larger models (OPT 350M) may struggle with generalization.
2. **Prompt Engineering**: Effective prompts significantly impact PBFT performance but were outside the study’s scope.
3. **Trade-Offs**: The choice of fine-tuning method depends on memory, computational constraints, and specific task requirements.

------

### **Conclusions**

1. **Context Distillation** is a promising alternative to full-model fine-tuning for achieving competitive in-domain accuracy with fewer computational resources.
2. **LoRA and Adaptive Fine Tuning** offer efficient solutions for limited-resource environments but require further refinement to match full-model performance.
3. Fine-tuning strategies should balance computational efficiency and task-specific performance goals.

# Experiment: Compare Performance Between Smaller and Larger LLM

## In-Context Learning

- what is in-context learning: According to Mosbach et al. (2023), In-context learning (ICL) is a task adaptation strategy. Unlike other methods, ICL does not update the weights of the pretrained model. Instead, it adapts a model to a task by conditioning it on a sequence of demonstrations. A demonstration is simply an input x accompanied by its ground-truth label y, both of which are converted to a specific format using a pattern and a verbalizer.  
- experiment setting: 
  - This experiment evaluates the in-context learning capabilities of the OPT-125M language model on natural language inference tasks using different numbers of demonstration examples (shots). The evaluation focuses on both in-domain (RTE) and out-of-domain (HANS) performance. 
  - Model and Tasks
    - Model: Facebook's OPT-125M
    - In-domain task: RTE (Recognizing Textual Entailment)
    - Out-of-domain task: HANS (Heuristic Analysis for NLI Systems)
    - Shot variations: 2, 32, and 128 examples
  - Prompt Design: The experiment uses a consistent GPT-3 pattern prompt template. 
  - Implementation Details
    - Balanced sampling ensures equal representation of each label class
    - Demonstrations are shuffled for better robustness
    - Binary classification task: Yes (entailment) or No (contradiction)
    - Maximum sequence length: 1024 tokens
    - Seeds are fixed for reproducibility (42)
- experiment result:
  - The results show exact consistency across all shot counts: RTE accuracy: 47.29% for 2, 32, and 128 shots; HANS accuracy: 50.00% for 2, 32, and 128 shots; 
  - problem diagnosis: 
    - Context Processing
      - The identical scores across different shot counts suggest the model isn't effectively utilizing the demonstration examples 
      - The context might be getting truncated for larger shot counts (128 shots). 
    - Model Size
      - OPT-125M is a relatively small language model (125M parameters), which might not have sufficient capacity to benefit from increasing the number of demonstrations. 
      - The consistent accuracy of around 47.3% for RTE and 50% for HANS suggests the model might be defaulting to random guessing.

## Context Distillation

- what is context distillation: according to Askell et al. (2021), context distillation as a method finetunes a model to mimic the behavior of a prompted model without the need for the prompt at inference time. This addresses the issues of limited context window size and computational inefficiency associated with prompting. 
  - how context distillation works: 
    - **Training data generation:** A large language model is first prompted with the desired context, such as the helpful, honest, and harmless (HHH) prompt, and used to generate text samples. The model's top predicted probabilities for each token are stored, along with their corresponding token indices. This data represents the desired behavior encoded by the prompt.
    - **Finetuning with KL divergence loss:** A separate language model is then finetuned using the generated data. The training objective is to minimize the KL divergence between the probability distribution of the prompted model and the finetuned model's predictions. This encourages the finetuned model to learn the same behavioral patterns as the prompted model.
    - **Eliminating the need for the prompt at inference:** The resulting finetuned model, having internalized the prompt's context, can then generate responses that align with the desired behavior without requiring the prompt at inference time.
    - **Benefits of context distillation:**
      - **Efficiency:** It avoids the computational overhead and context window limitations associated with prompting at inference time.
      - **Similar performance to prompting:** The sources report that context distillation achieves similar performance to prompting on various alignment evaluations, including the HHH evaluations and toxicity reduction.
- experiment setting: 
  -  This experiment investigates context distillation using the OPT-125M model for natural language inference tasks, specifically focusing on the RTE (Recognizing Textual Entailment) dataset and evaluating generalization on the HANS dataset.
  - **Model Architecture**
    - Teacher and Student Models: OPT-6.7B with 2 output labels
    - Models configured with dropout probabilities of 0.1 for both hidden layers and attention
    - Half-precision (FP16) training implemented for memory efficiency
    - Gradient checkpointing enabled to manage memory usage
  - **Training Setup**
    - Dataset sizes: 2, 32, and 128 examples per class
    - 10 runs per dataset size for statistical reliability
    - Training conducted for 40 epochs
    - Batch size of 8 with gradient accumulation steps of 4
    - Learning rate: 1e-5 with warmup over 10% of total steps
  - **Loss Function**: equally weighted average on distillation loss and classification loss, where distillation_loss uses KL divergence between teacher and student outputs, and classification_loss uses standard cross-entropy. 
  - **Optimization**
    - AdamW optimizer with weight decay set to 0
    - FP16 training enabled
    - Gradient accumulation implemented for effective batch size of 32
    - Device mapping automatically handled for optimal resource utilization
- experiment result: 
  - 

# Meeting Notes - 12/04

### Topics Discussed

#### 1. Experiments

- **Datasets**: RTE, HANS
- **Models**: 125M, 6.7B
- Fine-tuning Methods:
  - Vanilla fine-tuning (FT)
  - Context distillation
  - LoRA (PEFT)
- **Prompt Design**: Few-shot learning (time permitting)
- **Additional Task**: Add code to measure and log runtime for each experiment as part of performance matrix 

#### 2. Task Assignments

- **Bo**:

  - Fix the preprocessing bug in the RTE dataset prompting code and upload the corrected version.

    - Updated functions:

      ```python
      def manipulate_inputs_rte(batch):
          encoding = tokenizer(
              [f'Given the statement "{sentence1}", does it necessarily follow that "{sentence2}" is true?'
               for sentence1, sentence2 in zip(batch["sentence1"], batch["sentence2"])],
              truncation=True,
              padding="max_length",
              max_length=128,
              return_tensors='pt'
          )
          batch["input_ids"] = encoding["input_ids"].squeeze()
          batch["attention_mask"] = encoding["attention_mask"].squeeze()
          return batch
      
      # Prepare the inputs with the fixed context for HANS
      def manipulate_inputs_hans(batch):
          fixed_context = "Given the premise, does the hypothesis hold true? "
          encoding = tokenizer(
              [f'{fixed_context} Premise: {premise} Hypothesis: {hypothesis}'
               for premise, hypothesis in zip(batch["premise"], batch["hypothesis"])],
              truncation=True,
              padding="max_length",
              max_length=128,
              return_tensors='pt'
          )
          batch["input_ids"] = encoding["input_ids"].squeeze()
          batch["attention_mask"] = encoding["attention_mask"].squeeze()
          return batch
      ```

  - Continue work on **context distillation**.

- **Yue**: Focus on **LoRA implementation**.

- **Qi**: Work on **vanilla fine-tuning (FT)**.

- **Jialin**: Task to be decided (TBD).

------

### Follow-up

- Next Meeting: Tentatively Friday or Saturday. Confirm the timing via WeChat with Jialin.

------

### References

**RTE Dataset**:

- Paper: https://arxiv.org/pdf/2305.14877
- HuggingFace: https://huggingface.co/datasets/gimmaru/glue-rte
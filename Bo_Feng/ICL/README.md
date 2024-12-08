**Repository and Code**

- Repository: https://github.com/uds-lsv/llmft/tree/main
- Main Python Script: [`eval.py`](https://github.com/uds-lsv/llmft/blob/main/eval.py)

**Global Parameter Settings**
 The `eval.py` script uses a set of global parameters configured through command-line arguments.

**Running the In-Context Learning Experiment**

1. Run the shell script `experiments/in_context/opt.sh`.
2. This script calls `scripts/in_context/mnli/run_minimal.sh`.
3. That shell script then runs `eval.py` with specified parameters.

------

**Code Flow and Key Steps**

1. **Setup and Configuration**

   ```python
   parser = HfArgumentParser((ModelArguments, DataTrainingArguments, TrainingArguments, InContextLearningArguments))
   ```

   - The code begins by parsing model arguments, data arguments, training arguments, and in-context learning arguments.
   - It sets up logging and seeds for reproducibility.

2. **Data Loading and Processing**

   ```python
   if data_args.task_name in ["rte", "mnli", "mnli-original", "qqp", "cola"]:
       raw_datasets, label_list, num_labels, is_regression = load_glue_datasets(data_args, model_args)
   ```

   - It loads the specified dataset (for example, MNLI).
   - It can also load additional evaluation datasets, such as HANS.

3. **Creating the In-Context Learning Prompt**

   ```python
   context, contex_indices = create_few_shot_context(
       data_args.task_name, 
       raw_datasets["train"], 
       in_context_args.num_shots,
       pattern=in_context_args.pattern,
       label_to_tokens=id_to_target_token,
       separate_shots_by=in_context_args.separate_shots_by, 
       description=in_context_args.task_description,
       target_prefix=in_context_args.target_prefix,
       balanced=in_context_args.balanced, 
       shuffle=in_context_args.shuffle,
       seed=training_args.data_seed
   )
   ```

   - This step generates a few-shot context using training examples.
   - It uses parameters like the number of examples (shots), format patterns, and optional shuffling for balanced sampling.

4. **Preprocessing Examples**

   ```python
   def preprocess_function(examples):
       if context != "":
           pattern = f"{context}{in_context_args.pattern}"
       else:
           pattern = in_context_args.pattern
       
       pattern_examples = [
           pattern.format(
               text1=examples[sentence1_key][idx],
               text2=examples[sentence2_key][idx] if sentence2_key is not None else None
           )
           for idx in range(len(examples[sentence1_key]))
       ]
   ```

   - Each example is formatted using the chosen pattern and the created context.
   - Labels are mapped to target tokens.
   - After formatting, the examples are tokenized.

5. **Evaluation**

   ```python
   trainer = FtTrainer(
       model=model,
       args=training_args,
       train_dataset=None,
       eval_dataset=None,
       compute_metrics=compute_metrics,
       tokenizer=tokenizer,
       data_collator=data_collator,
       data_args=data_args,
       eval_only=True
   )
   ```

   - Uses a custom `FtTrainer` for evaluation.
   - Computes metrics such as accuracy.
   - Can handle both in-domain and out-of-domain datasets.

6. **Example Input Formats for MNLI**
    Possible input patterns include:

   ```
   # GPT-3 style:
   "{text1} question: {text2} Yes or No?"
   
   # Minimal style:
   "{text1} {text2} ?"
   
   # Eval-harness style:
   "{text1} \nQuestion: {text2} True or False?"
   ```

   These patterns guide how text is presented to the model for in-context learning.

7. **Results Collection**

   ```python
   all_results = _add_args_to_results(in_context_args, all_results)
   all_results["indices"] = contex_indices
   all_results["context"] = context
   all_results["data_seed"] = training_args.data_seed
   ```

   - Finally, the script aggregates all results.
   - It includes metadata such as the chosen context, data seed, and argument settings.

------

**Source**: https://github.com/uds-lsv/llmft/tree/main
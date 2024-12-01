# How to Fix Code to Adapt for Using Weights & Biases (wandb)

by Bo Feng

e.g. code: `Bo_Feng/notebooks/vanilla_cola_baseline.ipynb`

1. First, add the wandb initialization code inside your training loop, just before creating the TrainingArguments:

   ```python
   for n in few_shot_sample_size:
       for run_idx in range(num_runs):
           # re-initialize model
           model = AutoModelForSequenceClassification.from_pretrained("facebook/opt-125m", config=config)
           optimizer = AdamW(model.parameters(), lr=learning_rate)
   
           # Initialize wandb for this run
           wandb.init(
               project="bo_cola-fewshot",
               name=f"bo_cola_fewshot_n{n}_run{run_idx}",
               config={
                   "learning_rate": learning_rate,
                   "epochs": num_epochs,
                   "batch_size": batch_size,
                   "model": "facebook/opt-125m",
                   "few_shot_size": n
               },
               reinit=True  # Allow multiple runs in the same script
           )
   
           # Rest of your training code...
           
           # Make sure to close the wandb run at the end of each iteration
           wandb.finish()
   ```

2. Modify your TrainingArguments to explicitly use wandb:

   ```python
   training_args = TrainingArguments(
       output_dir="./results",
       run_name=f"bo_cola_fewshot_n{n}_run{run_idx}",
       overwrite_output_dir=True,
       num_train_epochs=num_epochs,
       per_device_train_batch_size=batch_size,
       learning_rate=learning_rate,
       weight_decay=weight_decay,
       save_steps=10_000,
       save_total_limit=2,
       warmup_steps=int(warmup_ratio * total_steps),
       report_to=["wandb"],  # Explicitly enable wandb reporting
       logging_strategy="steps",
       logging_steps=10  # Log every 10 steps
   )
   ```

3. Before running your script, you need to login to wandb:

   ```python
   # Add this at the beginning of your script
   import wandb
   wandb.login()  # This will prompt for your API key if not already logged in
   ```

When you run this code, Weights & Biases will automatically:

- Create a new project called "bo-cola-fewshot" if it doesn't exist
- Track separate runs for each combination of `n` and `run_idx`
- Log training metrics like loss and accuracy
- Record your hyperparameters
- Create visualizations of your training progress

You can then view all your experiments in the W&B dashboard by:

1. Going to wandb.ai
2. Selecting your project "bo-cola-fewshot"
3. Viewing individual runs or comparing multiple runs
4. Analyzing training metrics, system metrics, and hyperparameters
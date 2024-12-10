**Repository and Code**

- Repository: https://github.com/uds-lsv/llmft/tree/main
- Main Python Script: [`eval.py`](https://github.com/uds-lsv/llmft/blob/main/eval.py)

## Repo Description

This repository is focused on fine-tuning Large Language Models (LLMs) and contains several key components:

1. Purpose:

- The repository provides tools and scripts for fine-tuning large language models
- It supports various NLP (Natural Language Processing) tasks
- Includes optimization capabilities through DeepSpeed integration

1. Main Components:

- Model wrappers: Interfaces for working with different language models
- Training scripts: Code for training and fine-tuning models
- Configuration files: Settings for optimization and training parameters
- Dataset utilities: Tools for managing and processing training data

1. Key Features:

- DeepSpeed integration for improved performance and distributed training
- Support for multiple NLP tasks
- Flexible configuration options
- Evaluation capabilities

1. Structure:

- Training scripts for model fine-tuning
- Evaluation scripts for assessing model performance
- Configuration files for DeepSpeed and other settings
- Utility functions for data handling and processing

This repository serves as a toolkit for researchers and developers who want to fine-tune large language models for specific tasks or domains, with a focus on efficiency and performance through DeepSpeed optimization.

## In-Context Learning Experiment

Based on the repository content, here's how this repo simulates in-context learning experiments:

1. Model Support:

- Supports multiple large language models including:
  - OPT models (125M to 30B parameters)
  - Pythia models (410M to 12B parameters)

1. Experiment Scripts Structure: The main experiment scripts are located in `/experiments/in_context/`:

a) Model-specific orchestration scripts:

- `opt.sh`: Orchestrates experiments for OPT models
- `pythia.sh`: Orchestrates experiments for Pythia models

b) Task-specific evaluation scripts in `/scripts/in_context/`:

- `mnli/run_minimal.sh`: Minimal format evaluation
- `mnli/run_gpt3.sh`: GPT-3 style evaluation
- `mnli/run_eval_harness.sh`: Evaluation harness format

1. Evaluation Patterns: Supports different input formatting patterns:

- Minimal format: Simple pattern with basic prompting
- GPT-3 format: Following GPT-3 style prompting
- Eval-harness format: Structured evaluation format

1. Key Components of Experiments:

- Uses DeepSpeed for distributed training/evaluation
- Supports different batch sizes (2, 16, 32)
- Multiple evaluation runs with different data seeds (0-9) for robustness
- Configurable parameters:
  - Number of shots
  - Maximum sequence length
  - Model configurations
  - Input/output patterns
  - Evaluation tasks

1. Example Execution Flow:

   ```bash
   # For each batch size:
   bash run_minimal.sh mnli <batch_size> <model_name> 1 60000
   bash run_gpt3.sh mnli <batch_size> <model_name> 1 60000  
   bash run_eval_harness.sh mnli <batch_size> <model_name> 1 60000
   ```

2. Evaluation Features:

   - Balanced evaluation

   - Data shuffling

   - FP16 precision support

   - Configurable random seeds

   - Multiple evaluation metrics

   - Support for out-of-domain evaluation

This setup allows for systematic experimentation with in-context learning across different models, formats, and evaluation settings while ensuring reproducibility and robustness through multiple runs with different seeds.
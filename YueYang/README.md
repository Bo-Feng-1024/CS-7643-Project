# Context distillation using Cola
Use CPU, optimizer = AdamW(student_model.parameters(), **lr=5e-5**) instead of 1e-5,downloaded the Hans dataset, and pre-process the dataset.
Runnig time 91m for 3 epoches

## For Cola:
in_domain_accuracy	out_of_domain_accuracy
0.7430	0.5108
0.6807	0.5261
**0.7440	0.5178**

## For Cola: 1e-5
in_domain_accuracy	out_of_domain_accuracy
Epoch 1: In-Domain Accuracy = 0.7709, Out-of-Domain Accuracy = 0.5003

Context distillation using **Mnli,** results from the file
in_domain_accuracy	out_of_domain_accuracy
0.6313508667065150	0.5003666666666670
0.6676628810520020	0.5249666666666670
**0.7208607292289300	0.49746666666666700**


# PEFT+LoRa RTE:
- Looping through 5 config, with r = 1,2,4,8,64. 
- Parameters:
    few_shot_sample_size = [2, 32, 128]  
    num_epochs = 40
    batch_size = 32
    learning_rate = 1e-5
    weight_decay = 0.0
    warmup_ratio = 0.1
    num_runs = 10
  
- **Time: 7.5h,** n = 2, r = 1,2,4,8.
- Consider use a **single r (4**) for lora config, or reduce number of iteration.

**- lora_configs = [lora_config_r1, lora_config_r2, lora_config_r4, lora_config_r8, lora_config_r64]**
| **LoRA Rank (`r`)** | **In-Domain Accuracy (RTE)** | **Out-of-Domain Accuracy (HANS)** |
|----------------------|-----------------------------|------------------------------------|
| 1                    | 0.5451                     | 0.5182                            |
| 2                    | 0.5487                     | 0.5184                            |
| 4                    | 0.5487                     | 0.5189                            |
| 8                    | 0.5415                     | 0.5197                            |

## Observation:
1. **In-Domain Accuracy (RTE)**:
   - The highest accuracy (**0.5487**) is achieved with `r=2` and `r=4`.
   - Higher rank (`r=8`) slightly decreases in-domain accuracy, possibly due to overfitting with the small dataset size.

2. **Out-of-Domain Accuracy (HANS)**:
   - The highest accuracy (**0.5197**) is achieved with `r=8`.
   - Accuracy improves slightly as the rank increases, showing better generalization for higher ranks.

## Results by LoRA Rank and Iteration
- Does not change much after 1 iter, consider to reduce it to **3.**

| **Rank (`r`)** | **Iteration** | **In-Domain Accuracy (RTE)** | **Out-of-Domain Accuracy (HANS)** |
|----------------|---------------|------------------------------|------------------------------------|
| 1              | 1             | 0.5812                      | 0.5008                            |
|                | 2             | 0.5451                      | 0.5182                            |
|                | 3             | 0.5451                      | 0.5182                            |
|                | 4             | 0.5451                      | 0.5182                            |
|                | 5             | 0.5451                      | 0.5182                            |
|                | 6             | 0.5451                      | 0.5182                            |
|                | 7             | 0.5451                      | 0.5182                            |
|                | 8             | 0.5451                      | 0.5182                            |
|                | 9             | 0.5451                      | 0.5182                            |
|                | 10            | 0.5451                      | 0.5182                            |
| 2              | 1             | 0.5487                      | 0.5184                            |
|                | 2             | 0.5487                      | 0.5184                            |
|                | 3             | 0.5487                      | 0.5184                            |
|                | 4             | 0.5487                      | 0.5184                            |
|                | 5             | 0.5487                      | 0.5184                            |
|                | 6             | 0.5487                      | 0.5184                            |
|                | 7             | 0.5487                      | 0.5184                            |
|                | 8             | 0.5487                      | 0.5184                            |
|                | 9             | 0.5487                      | 0.5184                            |
|                | 10            | 0.5487                      | 0.5184                            |
| 4              | 1             | 0.5487                      | 0.5189                            |
|                | 2             | 0.5487                      | 0.5189                            |
|                | 3             | 0.5487                      | 0.5189                            |
|                | 4             | 0.5487                      | 0.5189                            |
|                | 5             | 0.5487                      | 0.5189                            |
|                | 6             | 0.5487                      | 0.5189                            |
|                | 7             | 0.5487                      | 0.5189                            |
|                | 8             | 0.5487                      | 0.5189                            |
|                | 9             | 0.5487                      | 0.5189                            |
|                | 10            | 0.5487                      | 0.5189                            |
| 8              | 1             | 0.5415                      | 0.5197                            |
|                | 2             | 0.5415                      | 0.5197                            |
|                | 3             | 0.5415                      | 0.5197                            |
|                | 4             | 0.5415                      | 0.5197                            |
|                | 5             | 0.5415                      | 0.5197                            |
|                | 6             | 0.5415                      | 0.5197                            |
|                | 7             | 0.5415                      | 0.5197                            |
|                | 8             | 0.5415                      | 0.5197                            |
|                | 9             | 0.5415                      | 0.5197                            |
|                | 10            | 0.5415                      | 0.5197                            |

# Shorter Version Results
- config: r = 4. 
- Parameters:
    few_shot_sample_size = [2, 32, 128]  
    num_epochs = 40
    batch_size = 32
    learning_rate = 1e-5
    weight_decay = 0.0
    warmup_ratio = 0.1
    num_runs = 3
## **Accuracy Across Different `n` and `Rank` Values**

| **n** | **Rank (`r`)** | **Run** | **In-Domain Accuracy (RTE)** | **Out-of-Domain Accuracy (HANS)** |
|-------|----------------|---------|------------------------------|------------------------------------|
| 2     | 4              | 0       | 0.5740                       | 0.5011                            |
| 2     | 4              | 1       | 0.5560                       | 0.5194                            |
| 2     | 4              | 2       | 0.5560                       | 0.5194                            |
| 32    | 4              | 0       | 0.5451                       | 0.5193                            |
| 32    | 4              | 1       | 0.5451                       | 0.5193                            |
| 32    | 4              | 2       | 0.5451                       | 0.5193                            |
| 128   | 4              | 0       | 0.5560                       | 0.5195                            |
| 128   | 4              | 1       | 0.5560                       | 0.5195                            |
| 128   | 4              | 2       | 0.5560                       | 0.5195                            |

- Time used: 14545.49 seconds ( 4 hrs, 2 min, and 25 sec).

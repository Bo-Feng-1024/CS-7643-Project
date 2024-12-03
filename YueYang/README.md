Context distillation using Cola
Use CPU, optimizer = AdamW(student_model.parameters(), **lr=5e-5**) instead of 1e-5,downloaded the Hans dataset, and pre-process the dataset.
Runnig time 91m for 3 epoches

**For Cola:**
in_domain_accuracy	out_of_domain_accuracy
0.7430	0.5108
0.6807	0.5261
**0.7440	0.5178**

**For Cola:** 1e-5
in_domain_accuracy	out_of_domain_accuracy
Epoch 1: In-Domain Accuracy = 0.7709, Out-of-Domain Accuracy = 0.5003

Context distillation using **Mnli,** results from the file
in_domain_accuracy	out_of_domain_accuracy
0.6313508667065150	0.5003666666666670
0.6676628810520020	0.5249666666666670
**0.7208607292289300	0.49746666666666700**

---
source_path: leveraging_machine_learning_for_employee_resignation_prediction_in_hr_analytics.md
pages: n/a-n/a
chunk_id: 84861ab0f6e9c39bdaf5d3d180f27b18d3201112
title: leveraging_machine_learning_for_employee_resignation_prediction_in_hr_analytics
---
# Where h(L)

is the (cid:2647)nal feature representation of node i a(cid:2383)er L i layers, wout is the bias term. (cid:2399)e output ˆ𝑦i represents the predicted probability of a(cid:2386)rition for employee i.

is the output weight vector, and bout

3.3 Loss Function Binary cross-entropy loss, widely utilized in binary classi(cid:2647)cation problems, is our method of model training. For one forecast, the loss is expressed as:

L (yi, ˆ𝑦i) = −yilog (ˆ𝑦i) − (1 − yi) log (1 − ˆ𝑦i)

Where ˆ𝑦i is the expected a(cid:2386)rition probability for node i and yi is the actual label for node ii (either 0 or 1). (cid:2399)e binary cross-entropy loss across all of the nodes determines the loss for the whole dataset:

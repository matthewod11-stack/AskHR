# L (yi, ˆ𝑦i)

Where N is the number of nodes (employees) in the graph. We minimize the overall loss by optimizing the model with the Adam optimizer. Learning the a(cid:2386)ention coe(cid:2649)cients 𝛼ij, weight matrices W, and output layer weights wout during training.

4 Experiment Results and Analysis 4.1 Experimental Setup Along with the target variable indicating whether the employee le(cid:2383) thecompany (a(cid:2386)rition= 1)or stayed (a(cid:2386)rition= 0), weused the IBM Employee A(cid:2386)raction Dataset (or another pertinent dataset) for the experiments including age, job satisfaction, salary, and years at the company. (cid:2399)ere is a training set (80%) and a test set (20%) out of the dataset. We included demographic data (e.g., age, marital status), job-related variables (e.g., job satisfaction, salary), and tenure (e.g., years at the company) in a subset of features typically linked with employee a(cid:2386)rition. We assessed the models using the following benchmarks:

Accuracy: (cid:2399)e proportion of accurately anticipated labels. F1-Score: Precision and recall’s harmonic mean. We evaluated the GAT model against the following baseline
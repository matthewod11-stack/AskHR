# conventional se(cid:2386)ings.

4.2 Results and Analysis Table 1 shows the experiment (cid:2647)ndings, which on the test set com- pare the GAT model performance with that of the baseline models. Across both accuracy and F1-score, the GAT model beats logistic regression and decision trees as Table 1 shows. Higher than the accuracy of 84% for logistic regression and 86% for decision trees, the GAT model had an accuracy of 91%. Moreover, the GAT model displayed a greater F1-score, meaning improved general accuracy in employee a(cid:2386)rition prediction. (cid:2399)e GAT model’s great accuracy can be ascribed to its capacity to use the a(cid:2386)ention mechanism to capture intricate relationships between employees. Using the graph structure, the model e(cid:2649)ciently aggregates information from an employee’s neighbors (i.e., employees with similar characteris- tics), which conventional models such as logistic regression and decision trees cannot accomplish. Higher for the GAT model as well as for the F1-score, which strikes a mix between accuracy and recall, the model is successful in keeping a balance between spo(cid:2386)ing a(cid:2386)rition cases and reducing false positives.

We presented employee features in a circular arrangement with lines linking strongly connected features in order to be(cid:2386)er grasp their relationships. As Figure 1 illustrates, the strength of these connections is re(cid:2648)ected in the line intensity. Strong links between elements like JobSatisfaction and Performance Rating are high- lighted in the plot, which would suggest that workers who are more job satis(cid:2647)ed usually have superior performance. (cid:2399)ese real- izations can direct HR choices on employee satisfaction policies and retention methods.

4.3 Ablation Study We performed an ablation study, testing the following variants, in order to assess the e(cid:2646)ect of the graph structure and a(cid:2386)ention mechanism even more:

GAT without a(cid:2386)ention: (cid:2399)is variant eliminates the a(cid:2386)ention component so enabling the model to evenly aggregate features over all neighbors.

GAT with random graph: In this variant, we randomly permuted the graph structure to break the relationships between employees.

(cid:2399)e results of the ablation study are presented in Table 2 (cid:2399)e performance of the model is shown to be much in(cid:2648)uenced by the a(cid:2386)ention mechanism as well as the graph topology. (cid:2399)e GAT model without a(cid:2386)ention shows quite poor performance, which emphasizes the need of a(cid:2386)ention for learning the value of various

345
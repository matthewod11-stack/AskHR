---
source_path: from_big_data_to_deep_data_to_support_people_analytics_for_employee_attrition_pr.md
pages: n/a-n/a
chunk_id: 9f218ad171b2e3d7ba8d0d58a33abb75d3583816
title: from_big_data_to_deep_data_to_support_people_analytics_for_employee_attrition_pr
---
## FIGURE 2. Combination matrix of SelectKBest and RFE results.

helpful to mention here that we used GridSearch technique to identify the value of k. In fact, we used cross-validation to divide data into three sets (10% for the validation set which is used by GridSearch to ﬁnd the best hyperparameter k, 70% for the training data and 20% for the test set). The best k recommended by GridSearch here is 8 features for both IBM and Kaggle HR analytics datasets. After applying SelectKBest method to the collected data, the 5 algorithms select the 8 same features which are: Age, Grade, Tenure, Job performance, Job satisfaction, Rewards, Environment satisfaction and Job involvement.

jointly beneﬁt from two popular feature selection methods namely, Recursive Feature Elimination (a wrapper method) and SelectKBest (a ﬁlter method).

Recursive Feature Elimination (RFE) is a feature selec- tion method that ﬁts a model using an external estimator that assigns weights to the features (e.g., the coefﬁcients of a linear model) removes the weakest feature(s). Features are ranked by the model’s coefﬁcients or features importance attributes and by recursively eliminating a small number of featuresperloopRFEattemptstoeliminatedependenciesand collinearity that may exist in the model. When a predictive model or algorithm assigns the value False to an attribute meaning that the attribute has to be eliminated from the data columns and when the model assigns the value True to an attribute, which should be retained. In this step, we used 5 famous and accurate classiﬁers (XGB, RF, DT, LR and SVM). As employee attrition prediction is considered here as a classiﬁcation problem, these classiﬁers have been chosen because they are the best representatives of the different clas- siﬁcation approaches and at the same time they often be have well when dealing with statistical data [27]. Table 3 shows the results of RFE method applied by the 5 classiﬁers or pre- dictive models. Then, from these results, a majority vote was made to select candidate features of the RFE algorithm, so the selected ones to be eliminated by RFE (that have False values more than True values) are: Gender, Age, Grade, Education, Tenure, Promotability, Relationship satisfaction, and Work/life balance.

Fig. 2 presents a combination matrix of the results of the two feature selection techniques. Then, we propose to retain features that are selected by SelectKBest even though they are eliminated by RFE. Additionally, features that are not selected by SelectKBest and not eliminated by RFE are equally retained. Finally, features that are not selected by SelectKBest and eliminated by RFE are then removed. So, we ended up eliminating the following attributes: Gender, Education, Promotability, Relationship satisfaction and Work/life balance.

In conclusion, according to the combination of the two feature selection techniques (RFE and SelectKBest) and the collected data, the 11 main attritionary features necessary for the employee attrition prediction are: Age, Marital status, Tenure,Grade,Rewards,Jobinvolvement,Training,Business Travel, Job satisfaction, Job performance, and Environment satisfaction.

IV. THE PROPOSED ATTRITION PREDICTION APPROACH The second part of the study deals with proposing a solution for employee attrition prediction. To do so, we will start this section by an overview of the related works with regards to attrition prediction solutions based on predictive models. Then, we will focus on our proposed predictive approach and its steps details.

SelectKBest is a feature selection algorithm that scores the features of a dataset using a score function and then removes all but the k-highest scored features. It then simply retains the ﬁrst k features of training set with the highest scores. It is

With the help of our previous research studies and col- lected data from the employees’ survey, we found the main impactful features on employee attrition which will help us effectivelypredictingthisattrition.Thecollectedandselected data will be considered as an input to our predictive approach that is based on three steps. Fig. 3 presents the architecture of

VOLUME 9, 2021

60451

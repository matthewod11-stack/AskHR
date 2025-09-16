---
source_path: from_big_data_to_deep_data_to_support_people_analytics_for_employee_attrition_pr.md
pages: n/a-n/a
chunk_id: c1499dc664ee3b9a7a3b3b6a117b3078f29a8c8e
title: from_big_data_to_deep_data_to_support_people_analytics_for_employee_attrition_pr
---
# N. B. Yahia et al.: From Big Data to Deep Data to Support People Analytics for Employee Attrition Prediction

- 3) ENSEMBLE LEARNING BASED PREDICTIVE MODELS The main goal of ensemble learning (EL) is to combine sev- eral models in order to ﬁnd a better solution that gives better results [34]. So, EL is used here to combine the classiﬁers and their predictions in order to improve robustness over a single classiﬁer. In this study, we will test three ensemble learning models:

- 1. Random Forest is a popular tree-based ensemble learn- ing technique and a bagging algorithm where successive trees are constructed using a different bootstrap sample of the dataset. By the end, a simple majority vote is taken for pre- diction. Random forests are different from standard trees as each node is split using the best among a subset of predictors randomly chosen at that node which makes it robust against over-ﬁtting [35].

somewhere else. In fact, organizations retention policies and all other internal policies governance play a signiﬁcant role in improving workplace productivity, engaging employees emotionally and, hence controlling attrition. How to retain productive employees and their valued skills is one of the biggest problem that plague organizations, so we aim in this study not only to help HR managers in early detection of employee intention to leave but also to enable them to be aware of the facts leading to employees’ attrition, thus they can take few measures and effective management strategies to retain their employees. Indeed, it is equally very important for HR managers to not only have an accurate, but also an interpretable and an explicative predictive model that indicate which features triggering employee attrition and what makes an employee quit.

- 2. XGBoost is a gradient boosted tree algorithm that involves ﬁtting a set of weak learners and in which ﬁnal prediction is produced by the combination of predictions from all of them through a weighted majority vote (or sum). This boosting algorithm is based on the use of a regularized- model formalization to control over-ﬁtting, which makes it highly robust and gives it better performance [36].

- 3. Voting Classiﬁer is an ensemble learning model that trains on an ensemble of classiﬁers and then predicts the output class basing on a majority vote according to two different strategies. The ﬁrst one is the Hard Voting where the predicted output class is the class which had the highest probability of being predicted by each of the classiﬁers. The second one is the Soft Voting where the output class is the prediction based on the average of probability given to that class. In our case, we use a Voting classiﬁer that combines our chosen ML models and that is based on the majority vote strategy (Hard vote) to predict the output class. Such a classiﬁer can be useful for a set of equally well performing model in order to balance out their individual weaknesses.

- 4. Stacked ANN-based model where outputs of the three chosen deep learners (DNN, LSTM and CNN) are collected to create a new dataset encompassing also for each row the real expected value that will be used to train a new DNN learning model, called meta-learner. It is helpful to recall here that we used GridSeach for 10% of dataset as validation set to identify the best hyperparame- ters for each model (such as decision criterion and max-depth forDT,thehiddenlayersnumberandunitsorneuronsnumber in each layer for DNN, LSTM and CNN).

C. INTERPRETATION OF THE EMPLOYEE ATTRITION PHENOMENON Employee retention refers to organizations’ practices and policies that are used to prevent valuable and skilled employ- ees from leaving their jobs [37].

Thus, in this step of our approach, we will show how we can use our proposed models for attrition interpretation as well as attrition prediction using features importance. It is a statistical method that allows us to evaluate and quantify the participation of each feature in the prediction of the classiﬁ- cation task. So, we will use it here to identify attritionary fea- tures and to understand these features’ inﬂuence on employee attrition. Generally, features importance provides a score for each attribute that indicates either how much an attribute contributes to the improvement of the performance, or how much does the model depends on each of its features in the prediction.

So, our aim here is to search for real reasons behind the phenomenon of attrition, so interpretation has to focus only on attritional employees and those who have intention to leave, i.e. only taking into account samples where the value of Attrition = 1 (and we ignore samples where the value of Attrition = 0). Then, we consider ‘‘Job satisfac- tion’’ feature as our new target because employee job sat- isfaction is a key ingredient of employee retention. In fact, evidence suggests that employee attrition is triggered by job dissatisfaction and many researchers have shown that the employee satisfaction with job is signiﬁcantly correlated to the intention to leave [38]. We then proceed to the following steps:

- 1. Remove rows that present employees who did not leave their jobs or don’t have intention to leave (with Attrition = 0).

- 2. Delete the ‘‘Attrition’’ column and consider ‘‘Job satis- faction’’ as the new target.

- 3. Convert values of job satisfaction column 1, 2 and 3, 4 into respectively 0 and 1 as satisﬁed and not satisﬁed. 4. Apply features importance using the Random Forest (RF) classiﬁer to identify the most impactful features on employee job satisfaction (we choose RF because it is the most performing predictor whereas ensemble method cannot be used here as its inputs are classiﬁers and not data).

Thus, retention is totally opposite of attrition, it means the ability of organizations to keep their employees, in par- ticular, productive ones, and stop them from going to work

Results of applying features importance on our RF classiﬁer are depicted in Fig. 4.

VOLUME 9, 2021

60453

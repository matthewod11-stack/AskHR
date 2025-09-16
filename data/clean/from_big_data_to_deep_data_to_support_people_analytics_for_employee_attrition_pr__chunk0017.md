---
source_path: from_big_data_to_deep_data_to_support_people_analytics_for_employee_attrition_pr.md
pages: n/a-n/a
chunk_id: 14911a137576520e561795dc96f81704fdaaa743
title: from_big_data_to_deep_data_to_support_people_analytics_for_employee_attrition_pr
---
## FIGURE 4. Features importance of the random forest model.

V. EXPERIMENTATION RESULTS After conducting an exploratory and deep data analysis and then identifying all models settings (parameters and hyper-parameters), we are now ready to proceed onto build- ing our models and to assess their performance. Indeed, we will present in this section the experimental results of machine, ensemble and deep learning predictive models. To best assess the performance of these prediction models in a variety of scenarios, the large-sized Kaggle HR simu- lated dataset (15000 samples), the medium-sized IBM HR simulateddataset(1470samples)andoursmall-sizedHRreal dataset (450 samples) are used. Finally, the salient contribu- tion of these models will be presented towards the end of this experimentation to enable the HR manager not only to predict attrition but also to understand why and so to identify keys to retention. Evaluation criteria for these models and the comparison of their results are explained in following sections.

TABLE 5. Performance evaluation of models using our real dataset.

A. RESULTS OF PREDICTIVE MODELS FOR TWO SIMULATED HR DATASETS In this section, the two simulated human resources datasets are used to assess the performance of our predictive models. Theﬁrstoneisthelargesized-datasetsuppliedbyKagglethat contains 15000 samples where its target variable is ’’left’’ and its 9 features are satisfaction level; last evaluation; number project; average monthly hours; time spend company; Work accident; promotion last 5 years; sales and Salary. The second simulated human resources analytics dataset is a medium sized-dataset provided by IBM and it contains 1470 samples with34 features andits targetvariableisattritionthatisrepre- sented as ’’No’’ (employee did not left) or ’’Yes’’ (employee left). In this second simulated dataset, we ﬁnd our 11 selected features as part of its 34 features, so we will check the performance of our predictors using the entire dataset of IBM with its 34 features. Then, we will assess their performance using the same dataset but we will keep only the 11 selected features of our employee attrition model (Marital status, Age, Tenure,Grade,Rewards,Jobinvolvement,Training,Business Travel, Job satisfaction, Job performance, and Environment satisfaction). Table 4 shows the results in terms of accuracy (that is deﬁned as the percentage of the correctly classiﬁed data by the model and it represents the ratio of the predictions

total number that is correct) and F1-score using the two simulated datasets.

B. RESULTS OF PREDICTIVE MODELS FOR OUR REAL DATASET In this section, we compare our classiﬁcation predictors for understanding which predictor is more beneﬁting to classify churners and non-churners using our real dataset. Models accuracies are measured before and after feature selection algorithms which means that for the ﬁrst time we use the entire real dataset with its 16 features. Next, models are eval- uated using only the 11 features selected after applying the featureselection process by combining RFE and SelectKbest. Results are shown in Table 5.

VI. FINDINGS AND DISCUSSION In this section, we aim to discuss our experiment results and to put the light on the novelties of this research.

Firstly,regardingthequantitativeassessmentofourpredic- tors’performance,resultsdepictedinTables4and5showthat the ensemble learning model Voting Classiﬁer VC performs better than the other models for the simulated as well as

60454

VOLUME 9, 2021

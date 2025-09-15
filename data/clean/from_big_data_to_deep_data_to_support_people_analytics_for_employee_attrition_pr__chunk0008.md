# N. B. Yahia et al.: From Big Data to Deep Data to Support People Analytics for Employee Attrition Prediction

recommendations to ﬁght this possible attrition and to take necessary HR management policies.

TABLE 1. Recent related works.

The outline of this paper is as follows: In the second section, we will present an overview of related works. The research methodology conducted in this research to collect data for our study and to design our ﬁnal employee attri- tion model will be presented in the third section. In the ford section, we will present our approach and the various intelligent and predictive models proposed in order to predict employee attrition as soon as possible. The ﬁfth section will show the experimental results as well as the ﬁndings of this research i.e. interpretation of the results to understand what makes an employee quit. Finally, we conclude and present an outlook on future works.

II. RELATED WORKS Literature reports several employee attrition and voluntary turnover predictive models. In this study, we particularly consider recent works that are based on machine and deep learning models applied to the simulated HR datasets of IBM and Kaggle e.g. [14]– [25] and [26]. This choice is motivated by the existence of experiments results of predictive models’ accuracyfortheseopendatasetssowecancomparethemwith our proposed models.

the features. 2) They generally focus only on the employee attrition prediction however for a HR manager it is important tonotonlypredictassoonaspossibleanemployee’sintention to leave but also to interpret and explain why the employee has this intention to leave.

IBM HR simulated dataset is a medium sized-dataset provided by IBM and it contains 1470 samples with 34 input features (Age, Business Travel, Daily Rate, Department, Distance From Home, Education, Education Field, Employee Count, Employee Number, Environment Satisfaction, Gender, Hourly Rate, Job Involvement, Job Level, Job Role, Job Satisfaction, Marital Status, Monthly Income, Monthly Rate, Num Companies Worked, Over18, Over Time, Percent Salary Hike, Performance Rating, Rela- tionship Satisfaction, Standard Hours, Stock Option Level, Total Working Years, Training Times Last Year, Work Life Balance, Years At Company, Years In Current Role, Years Since Last Promotion, Years With Current Manager) and its target variable is attrition that is represented as ’’No’’ (employee did not left) or ’’Yes’’ (employee left).

Kaggle HR dataset is a large sized-dataset supplied by Kaggle that contains 15000 samples where its target variable is ’’left’’ and its 9 features are satisfaction level; last eval- uation; number project; average monthly hours; time spend company; Work accident; promotion last 5 years; sales and Salary.

In Table 1 authors present an overview of recent solutions to predict employee turnover. For each solution, used datasets and proposed models are presented such as Support vector Machine (SVM), Decision Tree (DT), Logistic Regression (LR), Random Forest (RF), XGBoost (XGB) and K Nearest Neighbors (KNN).

III. A MIXED METHOD FOR EMPLOYEE ATTRITION MODELING As employee attrition or voluntary turnover is a non- avoidable phenomenon, modelling it is a key issue for the process of attrition prediction. In addition, as we aim to adopt a deep data-driven approach, a research methodology that allows us to match theoretical models and experiments must be adopted. That’s why we propose to conduct a mixed research method based on the combination of an exploratory research and a quantitative method where the aim is to under- stand and explain employee attrition phenomena. These two combined methods are used sequentially (e.g., ﬁndings from one method inform the other). Thus, such a combined method can leverage the strengths and weaknesses of exploratory and quantitative methods and offer greater insights on a phenomenon that each of these methods individually cannot offer.

In fact, in order to gain a deeper understanding of the phenomenon of high attrition and identifying the factors behind it, an exploratory study based on reviewing avail- able literature is ﬁrstly established in detail using studies, papers and open datasets provided by HR experts and researchers. Secondly, these collected features are compared with causal factors for attrition identiﬁed through a question- naire and feature selection techniques (a quantitative research method).

While these solutions proposed accurate predictive models to predict employee attrition, they suffer from two major crit- ics: 1) there are no deep studies of employee features selected and used to predict the attrition that justiﬁes the choice of

The architecture of the conducted research methodology in this study is depicted in Fig. 1. We will explain in the following sections the different steps of the proposed mixed method.

VOLUME 9, 2021

60449
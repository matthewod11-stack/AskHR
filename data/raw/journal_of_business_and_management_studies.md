Journal of Business and Management Studies ISSN: 2709-0876 DOI: 10.32996/jbms Journal Homepage: www.al-kindipublisher.com/index.php/jbms

# JBMS

## AL-KINDI CENTER FOR RESEARCH AND DEVELOPMENT

# | RESEARCH ARTICLE

Employee Attrition Prediction in the USA: A Machine Learning Approach for HR Analytics and Talent Retention Strategies

Md Sumon Gazi1 Islam6 16MBA Business Analytics, Gannon University, USA 2Department of Management Science and Quantitative Methods, Gannon University, USA 3Master of Arts in Physics, Western Michigan University, USA 4PhD Student in Information Technology, University of the Cumberlands, KY, USA 5Masters of Science in Management, ST. Francis College Corresponding Author: Md Sumon Gazi, E-mail: sumonmkt87@gmail.com

# Md Nasiruddin2, Shuvo Dutta3, Rajesh Sikder4, Chowdhury Badrul Huda5 and Md Zahidul

✉

| ABSTRACT In the dynamic business domain in the USA, human capital is one of the most instrumental assets for companies. Maintaining high performance and reducing employee attrition has become an utmost priority in the USA since the costs related to employee attrition can be significant. The chief objective of this study was to explore the application of machine learning in terms of forecasting employee attrition and its ramifications for HR analytics and talent retention strategies. In this study, the investigator used Jupyter Notebook, an interactive platform for Python users, to design machine learning algorithms. The dataset utilized in this research was attained from the IBM Human Resource workforce attrition survey dataset. In the current research, the investigator proposed an array of machine learning models, most notably, Decision Tree, Ada-boost classifier, Random Forest, and gradient-boosted classifier. By referring to the model’s performance evaluation, it was apparent that the Random Forest algorithm had the highest accuracy, followed by Gradient Boosting and Decision Tree respectively. AdaBoost had the lowest accuracy. Concerning precision, the Random Forest algorithm again had the highest precision followed by Gradient Boosting and AdaBoost accordingly. By implementing the proposed models’ organizations in the USA can identify high-performing employees at risk of quitting, and subsequently take proactive steps to retain them, saving significant organizational resources. Ultimately, the proposed machine learning techniques can assist the government in maintaining high-performing employees, reducing the impact of labor shortages, and maintaining business continuity.

# | KEYWORDS

# Employee Attrition; Talent Retention Python; Random Forest; Gradient Boosting; Ada-boost; Decision Tree

# | ARTICLE INFORMATION

ACCEPTED: 01 May 2024 PUBLISHED: 18 May 2024 DOI: 10.32996/jbms.2024.6.3.6

- 1. Introduction In the recent past, employee attrition or turnover rate has become a substantial concern for companies in the USA, because it results in loss of productivity, human capital, increased organizational costs, and the demand for talent acquisition. Employee attrition refers to the involuntary or voluntary departure of personnel from a company. Global surveys by the World Bank demonstrate that 15-25% of staff voluntarily quit their jobs annually (Naik, 2023). Therefore, retaining top performers is paramount for organizational success. In that respect, companies require strategies and tools to strategically pinpoint at-risk employees and resolve their needs respectively. With the large volume of employee data now available on the company database, machine learning can be utilized to build predictive models for employee attrition (Musanga, 2023). This study aims to delve into the Copyright: © 2024 the Author(s). This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC-BY) 4.0 license (https://creativecommons.org/licenses/by/4.0/). Published by Al-Kindi Centre for Research and Development, London, United Kingdom.

Page | 47

# Employee Attrition Prediction in the USA: A Machine Learning Approach for HR Analytics and Talent Retention Strategies

application of machine learning in terms of forecasting employee attrition and its ramifications for HR analytics and talent retention strategies.

Marvin and Jackson (2021), contend that in the versatile business spectrum in the USA, human capital is one of the most instrumental assets for companies. Retaining top performing and diminishing employee attrition has become an utmost priority in the USA since the costs related to employee attrition can be significant. These organizational costs comprise the disruptions in productivity, loss of institutional knowledge, and the high cost involved in training and recruiting new employees. As such, efficient talent retention tactics are instrumental for retaining a skilled and productive workforce, affirming business continuity, and promoting a competitive advantage.

IJRASET (2021), indicates that conventional methods for employee turnover rates frequently depend on reactive tools, such as the employee departure survey questionnaire, which gives Human Resource managers valuable information after the staff has already decided to quit their employment. Nevertheless, by deploying advanced machine learning and data analytics methods, organizations can take a comprehensive method to detect and reduce the risk of employee attrition. Machine learning, a sub- category of artificial intelligence, allows the crating of predictive models that can evaluate large volumes of datasets and expose relationships and patterns that may not be instantly visible. By deploying machine learning models to historical employee data, companies can build algorithms capable of forecasting the probability of employee churning grounded on various factors, such as career development opportunities, compensation, job satisfaction, and work-life balance.

1.1 Problem Statement In retrospect, employee attrition presents a myriad of challenges for companies across industries in the USA, particularly, high attrition rates result in the loss of valuable talent, and human capital, disrupt team dynamics, as well as increase recruitment and training costs. The departure of well-trained and high-performing employees from an organization frequently results in a major organizational loss. In that light, this research paper aims to explore the root causes that lead to employee attrition, such as salary changes, promotional opportunities, the nature of the work environment, business travel opportunities, the nature of relations between superiors and subordinates, recognition and appreciation, and the time gap since the last promotion. Machine learning techniques will be the basis on which organizations in the USA can predict employee attrition. Such predictions can be made for the retention of valuable employees through various AI and machine learning methodologies.

- 2. Related Works A myriad of groundbreaking studies have been conducted to explore the efficacy of machine learning algorithms in predicting employee attrition. For instance, Qutub et al. (202), investigated employee attrition by applying distinct machine learning techniques, most notably, Logistic Regression (LR), K-Nearest Neighbors (KNN), Naive Bayes (NB), Support Vector Machines (SVM), Decision Trees (DT), and random forests (RF). The investigators performed two different experiments – one integrating feature selection and the other without. As a result, across both experimental instances, the support vector machine (SVM) algorithm proved to be the most effective and accurate technique for predicting employee attrition. By contrast, Sani (2023), in his in-depth study, discovered they found out that Naive Bayes had a relatively higher recall rate of 0.541. Nonetheless, they also discovered that deploying Naive Bayes on real-world turnover data presents challenges because of the assumption of predictor autonomy, which may not hold. This, combined with its lesser performance, results in relatively lower accurate predictions of employee attrition. In their study, they also established that the Decision tree algorithm performed second best, with logistic regression following closely in performance.

Raza et al. (2022), in their experimentation, ascertained that the XG-Boost (XGB) model outshined Logistic Regression, Random Forest, and Naive Bayes in terms of accuracy. They also outlined that XGB's innate regularization assists in terms of overcoming overfitting issues. The researchers equally pinpointed that the data used forecasting employee churning contains noise, and XGB can efficiently handle this noise, preventing it from being misinterpreted as relevant data.

Ajit (2022), designed an algorithm deploying a gradient-boosting classifier. After evaluating the algorithm's performance through precision, recall, and accuracy measurements, the gradient boosting tree model showcased superior outcomes compared to other techniques, attaining an accuracy of 97%. The experiment findings indicated that workers who are dissatisfied are more likely to quit and leave the company, while those with longer tenure and higher work involvement were less likely to resign.

IJRASET (2021), in their research, evaluated the efficiency of machine learning models in forecasting employee attrition. The goal of the investigators was to compare and contrast the accuracy of employee attrition forecasting attained via distinct machine learning algorithms, including Naive Bayes, Support Vector Machines, and Decision Trees. The result suggested that Random Forest displayed a relatively solid forecasting capability. The assessment indicated that employing more complicated machine learning Page | 48

# JBMS 6(3): 47-59

methods and validating feature importance through multi-criteria models could have potentially led to even higher levels of accuracy.

- 3. Methodology In this research paper, the investigator uses Jupyter Notebook, an interactive platform for Python users, to design machine learning algorithms. According to Hasan et al (2024), Python is an open-source program prevalently utilized for data science and machine learning tasks. Besides, R programming was also used, which is also an open-source language for developing machine learning algorithms. R-programming affords various graphical and statistical approaches for evaluating data and crafting predictive analytics resolutions. Both Python and R-system were considered appropriate programming languages for the objective of this study, as they provide robust libraries and functionality for employing machine learning techniques and constructing predictive models from data. 3.1 Dataset The dataset utilized in this research was attained from the IBM Human Resource workforce attrition survey dataset. Initially, the dataset comprised 35 features or variables. Nevertheless, 14 of these attributes were pinpointed as redundant and eliminated via data cleaning. This culminated in a final dataset with 21 attributes. Table 1 highlights and portrays these 21 attributes, entailing their distinguished data types as either numeric or non-numeric categorical variables (Pro-AI-Rokibul, 2024). Ultimately, these attributes capture distinct components of employees' job satisfaction, demographic characteristics, and work environment, to assist in evaluating and predicting the likelihood of attrition.

3.2 Pre-Processing Pre-processing entailed data reduction and cleaning was performed, comprising tasks such as the transformation of feature type from numerical to nominal. Based on the pre-processing, four (4) features were pinpointed and subsequently eliminated, resulting in a remaining set of 21 attributes (Pro-AI-Rokibul, 2024). After the production of the interquartile filter, outliers were detected and eliminated in the dataset.

S/No 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 17 18 19 20 21

Attribute Age bracket Daily Rate Department Business Travel Education Gender Distance from home Job involvement Hourly Rate Job Satisfaction Job level Job role Monthly rate Monthly income Number of organizations worked Performance rating Total Working Years Years at the Organization Years at the Present Role Work-Life Balance

Data Type Numeric type Numeric Categorical Categorical Categorical Categorical Numeric Categorical Numeric Categorical Categorical Categorical Numeric Numeric Numeric Categorical Numeric Numeric Numeric Categorical

3.3 Feature Engineering Selection Feature selection in this research entailed the careful selection of relevant features while discarding redundant and irrelevant information from the dataset. The objective was to diminish the dimensionality of the dataset, therefore enhancing accuracy, combating overfitting, minimizing training time, and pinpointing the most subjective and predictive domains for the evaluation (Pro-AI-Rokibul, 2024). Several feature selection techniques, such as Symmetrical Uncertainty Attributes, Gain Ratio Attributes, and Correlation Attributes, were adopted to choose the top twenty-one features out of the total of 30 features.

Page | 49

# Employee Attrition Prediction in the USA: A Machine Learning Approach for HR Analytics and Talent Retention Strategies

- 4. Proposed Models and Metrics In the current research, the investigator proposed an array of machine learning models, most notably, a Decision Tree, Ada-boost classifier, Random Forest, and Gradient Boosted Classifier. The assessment and evaluation were performed using Jupyter Notebook, an engaging algorithm development forum for Python, an open-source programming language predominantly adopted in machine learning algorithm development (Hasan et al. 2024). Besides, R-programming was also utilized in building the models.

# 4.1 Random Forest

Random Forest is a form of ensemble classifier that incorporates multiple algorithms to categorize items by making a collective decision. For example, it can consolidate algorithms such as Decision Tree, Support Vector Machines (SVM), and Naive Bayes. After consolidating these systems, it makes the final votes from each of the algorithms to develop the model’s classification. In the Random Forest classifier, a category of decision trees is initially established utilizing a sub-category of the training data (Hasan et al. 2024). Afterward, the votes from the different trees are combined to make the ultimate result of the algorithm’s class. The performance of the Random forest is demonstrated in Figure 1 below, portraying the evaluation of its effectiveness.

# 4.2 Gradient Boosting

Gradient boosting is a dynamic algorithm employed for both classification and regression tasks, facilitating the development of prediction algorithms. What distinguishes Gradient Boosting from the rest is its scalability and remarkable speed during deployment. In the setting of classification, gradient boosting functions sequentially, with every novel predictor learning from the errors made by preceding predictors. This repeated learning process enables swift classification and faster production of outcomes because of the algorithm’s capability to learn from previous mistakes (Jain & Nayyar, 2018). The performance measure of the Gradient Boosting classifier is demonstrated in Figure 3 below, illustrating the evaluation of its effectiveness.

Page | 50

# JBMS 6(3): 47-59

# 4.3 Ada-Boost Algorithm

Hasan et al. (2024), indicate that the AdaBoost algorithm is a classifier that integrates weak classifier models to establish a solid classifier. Independently, a single model may result in poor classification performance. Nevertheless, by incorporating multiple classifiers and cautiously choosing the training set at every experiment, along with strategically designating weights during the last voting process, it becomes possible to attain a high-level accuracy score for the final classifier. This classifier employs the collaborative strength of multiple classifiers to elevate the effectiveness and accuracy of the classification process.

# 4.4 Decision Tree Algorithm

Decision Trees are prominent classifier models due to their simplicity in implementation and interpretation. The model develops a tree architecture from the training dataset, where every leaf node stands for a feature, and the branches represent the respective feature values (Hasan et al. 2024). This hierarchical portrayal enables straightforward visualization and representation of the decision-making process within the algorithm.

4.5 Importing Libraries Initially, the analyst loaded the Human Resource Employee Attrition dataset into Jupyter Notebook which is an IDE of Python on which the analyst performed all the analysis, the figure below displays the loading of the dataset and dataset attributes.

Page | 51

# Employee Attrition Prediction in the USA: A Machine Learning Approach for HR Analytics and Talent Retention Strategies

# Output:

After the dataset was loaded, the researcher progressed with data preprocessing steps, which entailed eliminating records that comprised null values and converting the data to satisfy the protocol of the model being developed.

Page | 52

# JBMS 6(3): 47-59

After the preprocessing steps, the investigator explored the dataset, particularly exploring the correlations between different variables.

To ascertain the age distribution in the dataset, the analyst applied a code snippet to generate a suitable histogram respectively, the results can be showcased as follows:

# Outcomes:

Page | 53

# Employee Attrition Prediction in the USA: A Machine Learning Approach for HR Analytics and Talent Retention Strategies

To determine the correlation between job role and monthly income, an ideal code snippet was imposed to generate a scatter plot as showcased below:

# Output:

To establish the correlation between distance from home and the years at the organization, the analyst equally employed a suitable code snippet to generate an appropriate scatter plot which can be exhibited below:

# Output:

Page | 54

# JBMS 6(3): 47-59

To substantiate the association between monthly income by attrition and department, the following code snippet was applied to generate the appropriate scatter plot:

# Output:

Page | 55

# Employee Attrition Prediction in the USA: A Machine Learning Approach for HR Analytics and Talent Retention Strategies

To ascertain the connection between education level and job satisfaction, the following code snippet was imposed:

# Output:

Page | 56

# JBMS 6(3): 47-59

- 5. Models Performance Evaluation Confusion matrix was applied to assess the performance of the models in terms of accuracy, precision, and recall.

# Actual Class

# Class=No Class=Yes

## Predicted Class Class=No False Positive True Positive

# Class=Yes True Negative False Negative

# 5.1 Algorithm Performance Evaluation

## Models Random forest Decision Tree Gradient Boosting AdaBoost

Precision 83.33% 52.38% 62.96% 56.52%

Accuracy 86.05% 83.67% 85.71% 84.35%

F1 Score 32.78% 31.42% 44.73% 36.11%

Recall 20.40% 22.44% 34.69% 26.53%

By referring to the table above, it was evident that the Random Forest algorithm had the highest accuracy (86.05%), followed by Gradient Boosting (85.71%) and Decision Tree (83.67%) respectively. AdaBoost has the lowest accuracy (84.35%). Concerning precision, the Random Forest algorithm again had the highest precision (83.33%), followed by Gradient Boosting (62.96%) and AdaBoost (56.52%) accordingly. The Decision Tree algorithm had a relatively lower precision (52.38%).

5.2 Business Impact 5.2.1 Benefits of Implementing the Models on the Organizations in the USA Diminishing turnover costs: By deploying the proposed models’ organizations in the USA can identify high-performing employees at risk of quitting, and subsequently take proactive steps to retain them, saving significant organizational resources.

Enhanced Talent Management: Implementing the proposed models can assist businesses in the USA understand the root causes of employee attrition. Organizations can target retention efforts toward specific areas by evaluating aspects such as compensation, workload, and performance rating data, creating a more engaging work environment.

Page | 57

# Employee Attrition Prediction in the USA: A Machine Learning Approach for HR Analytics and Talent Retention Strategies

Improved Employer Brand: The recommended models can assist organizations in proactively resolving workers' issues and promoting a positive work atmosphere. As a result, the organization can enhance its employer brand. Consequently, this attracts top talent and minimizes the need for expensive and time-consuming recruitment efforts.

5.2.2 Benefits to the USA Economy Combating Labor Shortages: The US economy is presently confronting a tight labor market. As a result, Machine learning can assist the government in maintaining high-performing employees, reducing the impact of labor shortages, and maintaining business continuity.

Elevated productivity: The proposed can automate repetitive tasks across different sectors, liberating human workers to concentrate on higher-value activities. As a result, this leads to improved efficiency and overall productivity in the American economy.

Competitive Advantage: By employing the proposed models, consequently the government can affirm a significant competitive advantage, by retaining valuable and high-performing employees. As a result, this can lead to increased exports and a better overall position for the US economy in the global market.

Enhanced public service: The recommended algorithms can be employed to optimize government operations, predict attrition patterns and customize social services. This can result in a more equitable allocation of resources and better outcomes for US citizens.

5.3 How to Implement the Model Step 1: Define Business Problem and Data Needs-Business in the USA should first consider the specific business challenges confronting their respective organization and determine the data required to solve those challenges.

Step 2: Select the Right Model- The random Forest algorithm might be suitable for general classification with low error margins, while the Gradient Boosting algorithm could be appropriate for detecting positive case identification.

Step 3: Data Pre-processing and Preparation- Subsequently, the business analyst should resolve the outliers, inconsistencies, and missing values. Besides, the analyst should standardize data formats for algorithm compatibility.

Step 4: Model Training & Evaluation-Afterwards the business analyst should split the data into training, validation, and testing. As a result, the analyst should utilize the testing data to evaluate metrics such as precision, accuracy, and recall.

Step 5: Model Implementation and Monitoring: The business should track the metrics constantly and update the model with new data to avoid degradation.

- 6. Conclusion The focal aim of this research paper was to delve into the application of machine learning in terms of forecasting employee attrition and its ramifications for HR analytics and talent retention strategies. In this study, the investigator used Jupyter Notebook, an interactive platform for Python users, to design machine learning algorithms. The dataset utilized in this research was attained from the IBM Human Resource workforce attrition survey dataset. In the current research, the investigator proposed an array of machine learning models, most notably, a Decision Tree, Ada-boost classifier, Random Forest, and Gradient Boosted Classifier. By referring to the performance evaluation, it was evident that the Random Forest algorithm had the highest accuracy, followed by Gradient Boosting and Decision Tree respectively. AdaBoost had the lowest accuracy. Concerning precision, the Random Forest algorithm again had the highest precision followed by Gradient Boosting and AdaBoost accordingly. By implementing the proposed models’ organizations in the USA can identify high-performing employees at risk of quitting, and subsequently take proactive steps to retain them, saving significant organizational resources. Ultimately, the proposed machine learning techniques can assist the government in maintaining high-performing employees, reducing the impact of labor shortages, and maintaining business continuity.

Funding: This research received no external funding. Conflicts of Interest: The authors declare no conflict of interest. Publisher’s Note: All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers.

Page | 58

# JBMS 6(3): 47-59

References [1] Ajit, P. (2019). Prediction of employee turnover in organizations using machine learning algorithms. algorithms, 4(5), C5. [2] Ahmad, M., Ali, M. A., Hasan, M. R., Mobo, F. D., & Rai, S. I. (2024). Geospatial Machine Learning and the Power of Python Programming: Libraries, Tools, Applications, and Plugins. In Ethics, Machine Learning, and Python in Geospatial Analysis (pp. 223-253). IGI Global.

[3] Gurung, N., Gazi, M. S., & Islam, M. Z. (2024). Strategic Employee Performance Analysis in the USA: Deploying Machine Learning Algorithms

[4]

[5]

Intelligently. Journal of Business and Management Studies, 6(3), 01-14. IJRASET (2021). Prediction of employee attrition using machine learning approach. www.academia.edu. https://www.academia.edu/52266979/Prediction_of_Employee_Attrition_Using_Machine_Learning_Approach?sm=b Jain, R., & Nayyar, A. (2018, November). Predicting employee attrition using the xgboost machine learning approach. In 2018 international conference on system modeling & advancement in research, trends (smart) (pp. 113-120). IEEE.

[6] Marvin, G., & Jackson, M. (2021). A machine learning approach for employee retention prediction. Mak.

# https://www.academia.edu/56415761/A_Machine_Learning_Approach_for_Employee_Retention_Prediction?sm=b

[7] Musanga, V. (2023). A supervised machine learning model to optimize human resources analytics for employee churn prediction.

# www.academia.edu. https://www.academia.edu/99465169/A_Supervised_Machine_Learning_Model_to_Optimize_Human_Resources_Analytics_for_Employee_Chu rn_Prediction?sm=b

[8] Naik, P. (2023). Machine Learning approach for employee attrition analysis. www.academia.edu.

# https://www.academia.edu/75198011/Machine_Learning_Approach_for_Employee_Attrition_Analysis?sm=b

# [9] Pro-AI-Rokibul. (2024). Employee-Attrition-Prediction/Model/main.ipynb at main · proAIrokibul/Employee-Attrition-Prediction. GitHub.

# https://github.com/proAIrokibul/Employee-Attrition-Prediction/blob/main/Model/main.ipynb

[10] Qutub, A., Al-Mehmadi, A., Al-Hssan, M., Aljohani, R., & Alghamdi, H. S. (2021). Prediction of employee attrition using machine learning and

## ensemble methods. Int. J. Mach. Learn. Comput, 11(2), 110-114.

[11] Raza, A., Munir, K., Almutairi, M., Younas, F., & Fareed, M. M. S. (2022). Predicting employee attrition using machine learning

## approaches. Applied Sciences, 12(13), 6424.

[12] Sani, N. S. (2023). Machine learning for predicting employee attrition. www.academia.edu.

# https://www.academia.edu/98899513/Machine_Learning_for_Predicting_Employee_Attrition?sm=b

[13] Zhao, Y., Hryniewicki, M. K., Cheng, F., Fu, B., & Zhu, X. (2019). Employee turnover prediction with machine learning: A reliable approach.

In Intelligent Systems and Applications: Proceedings of the 2018 Intelligent Systems Conference (IntelliSys) Volume 2 (737-758). Springer International Publishing.

Page | 59
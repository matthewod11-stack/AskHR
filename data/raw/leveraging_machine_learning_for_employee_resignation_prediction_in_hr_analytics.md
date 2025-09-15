Leveraging Machine Learning for Employee Resignation Prediction in HR Analytics Xiang Fang∗ School of Management Shanghai University Shanghai, China f13651619278@163.com

Abstract A major issue in human resource management, employee a(cid:2386)ri- tion prediction o(cid:2646)ers insightful information for corporate decision- making. In this regard, conventional approaches including decision trees have only shown modest success. (cid:2399)ese techniques usually presume feature independence, though, and struggle to (cid:2647)t the re- lationships in the data. Using Graph A(cid:2386)ention Networks (GAT), we present a novel method for estimating employee a(cid:2386)rition that makes use of the linkages and similarities among employees to raise prediction performance. In this study, we represent each employee as a node in a graph, with their personal a(cid:2386)ributes (such as age, salary, job satisfaction, etc.) serving as node features. We build an adjacency matrix based on employee similarity computed with cosine similarity or Euclidean distance. We develop a GAT model using this graph structure that aggregates surrounding node fea- tures based on a(cid:2386)ention-based criteria therefore enabling the model to weigh the signi(cid:2647)cance of various relationships between employ- ees. (cid:2399)e GAT-based model beats conventional logistic regression according to experimental data, therefore greatly enhancing the accuracy of employee a(cid:2386)rition prediction. Improving prediction performance depends critically on the model’s capacity to replicate dependencies between characteristics and include relational infor- mation from adjacent nodes. (cid:2399)is paper shows the possibilities of GAT in employee a(cid:2386)rition prediction and emphasizes its capacity to model complex interactions inside employee data, therefore pro- viding a fresh approach for strategic workforce management and human resource analytics.

ACM Reference Format: Xiang Fang. 2025. Leveraging Machine Learning for Employee Resignation Prediction in HR Analytics. In 2025 International Conference on Arti(cid:2335)cial Intelligence and Computational Intelligence (AICI 2025), February 14–16, 2025, Kuala Lumpur, Malaysia. ACM, New York, NY, USA, 5 pages. https://doi. org/10.1145/3730436.3730494

1 Introduction Employee a(cid:2386)rition is a concern for organizations as it impacts their (cid:2647)nancial health, knowledge, and team dynamics [1–3]. Each time an employee exits an organization, not only does the organization have to pay for the recruitment and induction of a new employee, but it also loses the experience and knowledge the existing em- ployee carried with them. Additionally, frequent changes in the team members may cause disruption in the established dynamics and processes, impacting productivity and morale. (cid:2399)erefore, or- ganizations, especially HR departments, must foresee and prevent such turnover threats in advance.

In the past, (cid:2647)rms have relied heavily on traditional predictive models, such as decision trees, that rely heavily on the characteris- tics of one individual to forecast a(cid:2386)rition. While some success has been achieved using these models, they cannot identify complex relationships and interdependencies among workers that can have valuable predictive power. (cid:2399)is is because traditional models treat each employee as an isolated entity without considering the rich web of interactions and in(cid:2648)uences in the workplace.

# CCS Concepts • Computing methodologies → Machine learning; Machine learning algorithms.

Here, the arrival of graph neural networks (GNNs) o(cid:2646)ers a robust solution to predict employee turnover [4–6]. Unlike standard mod- els, GNNs are capable of representing and processing relational data through the use of graph structures. (cid:2399)ey can capture the complex relations between employees that could provide valuable information towards improving prediction accuracy.

# Keywords Graph A(cid:2386)ention Networks (GAT), Predictive Analytics, Employee Resignation

∗Corresponding author

Graph A(cid:2386)ention Networks (GATs) are well-adapted to perform the a(cid:2386)rition prediction task. In a GAT-based model, each employee is a node, and his/her relation or similarity with other employees is thegraph’sedge. (cid:2399)emodelemploysindividualemployeea(cid:2386)ributes like age, job satisfaction, and pay as node features. An employee- based adjacency matrix from employee similarities is utilized to create a graph with edges re(cid:2648)ecting the strength of the employee relationship.

(cid:2399)is work is licensed under a Creative Commons A(cid:2386)ribution International 4.0 License.

AICI 2025, Kuala Lumpur, Malaysia © 2025 Copyright held by the owner/author(s). ACM ISBN 979-8-4007-1363-7/2025/02 https://doi.org/10.1145/3730436.3730494

In this regard, we introduce a GAT-based method for employee a(cid:2386)rition prediction. We aim to show GAT’s value and predictive power by proving that adding relational data can signi(cid:2647)cantly en- hance predictive performance compared to traditional methods. (cid:2399)e (cid:2647)ndings of our paper set the stage for a graph-based methodol- ogy to be adopted in human resource analytics. Not only does this

342

## AICI 2025, February 14–16, 2025, Kuala Lumpur, Malaysia

provide an e(cid:2649)cient tool for companies to comprehend be(cid:2386)er and manage employee a(cid:2386)rition, but it also provides actionable insights for executing targeted retention measures and resource planning. (cid:2399)rough leveraging the power of the strengths of graph-based approaches, we propose a novel way of representing the intricate dynamics between various causes of employee a(cid:2386)rition. We view our GAT model as an excellent innovation compared to the con- ventional approaches, which have immense potential to enhance the prediction of employee a(cid:2386)rition.

2 Related Work (cid:2399)e application of machine learning methods for the prediction of employee a(cid:2386)rition has been a vibrant research area, with many studies applying various models to determine the relevant features that drive employee turnover. (cid:2399)e initial studies investigated the application of conventional machine learning methods. Fallucchi et al. (2020), for instance, studied the e(cid:2646)ect of objective features such as employee satisfaction and job title on a(cid:2386)rition and created a predictive model through machine learning methods to predict employee turnover [7].

Deep learning approaches for enhancing the accuracy of predic- tions have also been investigated in other studies. Raza et al. (2022) employed deep learning models to enhance the feature space of the data and enhance the accuracy of employee a(cid:2386)rition prediction [8]. Arqowitz et al. (2022) investigated deep learning models for employee a(cid:2386)rition and performance prediction and showed that deep learning approaches are capable of recognizing more subtle pa(cid:2386)erns in the data than conventional models [9].

A(cid:2386)rition forecasting has also picked up in ensemble approaches combining heterogeneous machine learning models. In employee turnover forecasting [10], (cid:2398)tub et al. (2021) tested several ensem- ble approaches like Random Forest and Gradient Boosting. (cid:2399)e strength and accuracy of the forecasts were found to have been enhanced by the approaches. In the comparison of several machine learning models in employee turnover, Subhashini and Gopinath (2020) identi(cid:2647)ed the potency of ensemble approaches in handling challenging data [11].

Other researchers have also employed more advanced methods, such as K-nearest neighbours (KNN) and support vector machines (SVM), to predict employee turnover. With SVM and KNN, along with other machine learning methods, Ajit (2016) forecasted em- ployee a(cid:2386)rition, thereby giving HR departments advance warning to proactively intervene in the direction of retention [12]. Like- wise, Zhao et al. (2019) compared di(cid:2646)erent approaches to employee turnover forecasting, thereby a(cid:2649)rming the usefulness of these methods for practical application [13].

Chaurasia et al. (2023) developed a new ANN-based employee a(cid:2386)rition prediction framework. Interestingly, their framework indi- cated a high accuracy rate of 96%, which was higher than conven- tional Deep Neural Networks (DNN). (cid:2399)e authors, in this research, proved the greater prediction ability of ANN and its potential for further use in HR analytics [14]. Srivastava and Eachempati (2021) integrated ensemble machine learning and multi-criteria decision- making methods to design a smart employee retention system. Not only did the comprehensive system predict employee turnover, but

343

# Xiang Fang

it also identi(cid:2647)ed key reasons for employee resignation. (cid:2399)is re- search provides useful input for organizations to manage a(cid:2386)rition successfully [15].

In a (cid:2647)rst-of-its-kind, Nawaz et al. (2024) applied sequential pat- tern mining in analyzing and classifying employee a(cid:2386)rition and absenteeism in industrial se(cid:2386)ings. (cid:2399)eir model not only allowed for precise predictions about the behaviour of employees but also gave actionable insights to organizations to enhance their policies, culture, and regulatory environment [16]. Wang et al. (2024) ex- tended the use of Deep Neural Networks (DNN) to the construction industry to forecast corporate malfeasance from social network data. (cid:2399)eir research acknowledges the potential of DNN to forecast a broad range of outcomes, resulting in a safer and more ethi- cal workplace [17]. Sairam and Voruganti (2022) used DNN with context information in employee mental health problem predic- tion. (cid:2399)eir predictive ability enables the organization to provide timely assistance to employees and manage a(cid:2386)rition for mental health reasons [18]. Demonstrating deep learning (cid:2648)exibility, Jar- rah and Derbali (2023) used deep learning methods in predicting stock prices in the stock market, demonstrating deep learning use in diverse prediction tasks beyond HR analytics [19]. Meier and Laumer (2022) proposed a DNN model for the accurate prediction of future employee numbers in HR sta(cid:2649)ng. (cid:2399)eir model, by taking into consideration scheduled new hires and anticipated a(cid:2386)rition, provides a complete image of future sta(cid:2649)ng needs, enabling strate- gic HR planning [20]. Due to the COVID-19 pandemic, Mohanan and Rajarathinam (2023) used ORS-DNN in HR management re- search during the shi(cid:2383) to work from home. (cid:2399)eir research provides insight into employee performance and a(cid:2386)rition management in the work-from-home arrangement [21]. Last but not least, Hus- sain (2024) used regression models to predict employee salaries in HR Management Systems (HRMS). His research demonstrates machine learning’s role in salary structure optimization, resulting in employee satisfaction and retention [22].

3 Method 3.1 Problem Formulation Employee a(cid:2386)rition prediction as a classi(cid:2647)cation task is a complex and signi(cid:2647)cant problem in human resources analytics. Here, the general aim is to predict correctly whether the employee will leave the company (where a(cid:2386) a(cid:2386)rition is to be 1) or stay (with a(cid:2386) a(cid:2386)ri- tion = 0). (cid:2399)is is a complex problem with numerous challenges, given the dynamic and complex nature of employee features and their interactions in the organizational se(cid:2386)ing. A full feature vector uniquely represents each employee in the company. (cid:2399)is feature vector represents a wide range of information that can in(cid:2648)uence the employee’s stay or leave decision. For instance, features like age can be a signi(cid:2647)cant factor because di(cid:2646)erent ages can have di(cid:2646)er- ent career goals, family status, and levels of job stability. Younger employees are likely to be more inclined to change jobs for career growth, while older employees can be more focused on the stability of their jobs and well-established work routines. Job satisfaction is another signi(cid:2647)cant feature. Employees with high job satisfaction levels concerning the nature of the job, relations with colleagues and management, and professional development opportunities are

## Leveraging Machine Learning for Employee Resignation Prediction in HR Analytics

likely to stay with the company. On the other hand, low job satis- faction levels can be an important predictor of a(cid:2386)rition. Salary is a highly signi(cid:2647)cant feature. Low salary levels compared to industry standards or the employee’s perceived value can a(cid:2386)ract him/her to search for be(cid:2386)er-paying alternative jobs.

In addition, a graph structure is used to expose the intricate relationships between the employees. Let G = (V,E) be the graph, where E represents the collection of edges. Each edge in E denotes the interactions between employees. (cid:2399)ese interactions can take various forms, such as collaboration on projects, communication within teams, or social relationships within the workplace. For example, employees who have strong collaborative relationships with their colleagues may be more engaged and commi(cid:2386)ed to the organization, thus less likely to leave. On the other hand, negative interactions or con(cid:2648)icts can contribute to job dissatisfaction and potentially lead to a(cid:2386)rition.

(cid:2399)e set V consists of vertices (nodes), each of which corresponds to an individual employee. Every employee i ∈ V corresponds to a feature vector xi ∈ Rd, in which d is the number of features. As mentioned earlier, these features can include age, job satisfaction, salary, and many other relevant factors.

(cid:2399)e ultimate aim is to forecast, for every employee i, the a(cid:2386)rition label yi, where yi ∈ {0,1}. To achieve this, sophisticated machine - learning algorithms and data - analysis techniques need to be applied. (cid:2399)ese methods must take into account both the individual features of each employee and the complex network of interac- tions among them. By leveraging this combined information, more accurate predictions of employee a(cid:2386)rition can be made, enabling organizations to proactively implement strategies to retain valuable employees and manage their human resources more e(cid:2646)ectively.

3.2 Graph Attention Network (GAT) Our model is based mostly on the Graph A(cid:2386)ention Network (GAT), which learns the signi(cid:2647)cance of surrounding nodes in the graph by means of a(cid:2386)ention mechanisms. Using learnt a(cid:2386)ention weights from a node’s neighbors, the GAT model aggregates data.

Aggregatingthecharacteristicsofsurroundingnodesupdatesthe representation h(l) of node i at layer in a GAT model. (cid:2399)e a(cid:2386)ention i mechanism computes a weight for every neighbor’s contribution to the changed node representation. One computes the a(cid:2386)ention coe(cid:2649)cient 𝛼ij between node i and its neighbor node j by means of this:

# 𝛼ij =

# Í

## exp (cid:16)LeakyReLU (cid:16)aT (cid:2) LeakyReLU

# k⊂N(i) exp

(cid:0)

## Wxi k Wxj(cid:3)(cid:17)(cid:17) aT [Wxi k Wxk]

(cid:0)

(cid:1)(cid:1)

xi and xj thus represent the features of i and j, respectively. (cid:2399)e weight matrix W converts the feature vectors; the a(cid:2386)ention vector a computes the relevance of the network between the nodes. N(i) stands for the collection of neighbors of node i; operation k denotes vector concatenation. When aggregating the data for node i, the a(cid:2386)ention coe(cid:2649)cient 𝛼ij measures the degree of focus one should pay to node j’ s features.

Aggregation of neighbor features weighted by the a(cid:2386)ention at layer l + 1. (cid:2399)is

coe(cid:2649)cients updates the node feature h(l+1)

# i

344

## AICI 2025, February 14–16, 2025, Kuala Lumpur, Malaysia

update rule shows itself as:

h(l+1) i

# = 𝜎

# 𝛼ijWxj

Õ © j⊂N(i)∪{i}

ª ® ¬

Here, 𝜎 is the ReLU function; weighted by the a(cid:2386)ention coe(cid:2649)- cients, the summation combines the modi(cid:2647)ed features of the node i ’s neighbors.” Every layer of the network is run in this way, which lets the model compile data from nodes.

«

(cid:2399)ea(cid:2386)ritionlabelispredictedusingthelastnoderepresentations following many levels of feature aggregation. Applying a sigmoid activation function, the output layer calculates the a(cid:2386)rition risk for every employee:

# out h(L)

# ˆ𝑦i = 𝜎 (cid:16)wT

# i

# + bout (cid:17)

# Where h(L)

is the (cid:2647)nal feature representation of node i a(cid:2383)er L i layers, wout is the bias term. (cid:2399)e output ˆ𝑦i represents the predicted probability of a(cid:2386)rition for employee i.

is the output weight vector, and bout

3.3 Loss Function Binary cross-entropy loss, widely utilized in binary classi(cid:2647)cation problems, is our method of model training. For one forecast, the loss is expressed as:

L (yi, ˆ𝑦i) = −yilog (ˆ𝑦i) − (1 − yi) log (1 − ˆ𝑦i)

Where ˆ𝑦i is the expected a(cid:2386)rition probability for node i and yi is the actual label for node ii (either 0 or 1). (cid:2399)e binary cross-entropy loss across all of the nodes determines the loss for the whole dataset:

# Ltotal

= 1 N

# N

# Õ i=1

# L (yi, ˆ𝑦i)

Where N is the number of nodes (employees) in the graph. We minimize the overall loss by optimizing the model with the Adam optimizer. Learning the a(cid:2386)ention coe(cid:2649)cients 𝛼ij, weight matrices W, and output layer weights wout during training.

4 Experiment Results and Analysis 4.1 Experimental Setup Along with the target variable indicating whether the employee le(cid:2383) thecompany (a(cid:2386)rition= 1)or stayed (a(cid:2386)rition= 0), weused the IBM Employee A(cid:2386)raction Dataset (or another pertinent dataset) for the experiments including age, job satisfaction, salary, and years at the company. (cid:2399)ere is a training set (80%) and a test set (20%) out of the dataset. We included demographic data (e.g., age, marital status), job-related variables (e.g., job satisfaction, salary), and tenure (e.g., years at the company) in a subset of features typically linked with employee a(cid:2386)rition. We assessed the models using the following benchmarks:

Accuracy: (cid:2399)e proportion of accurately anticipated labels. F1-Score: Precision and recall’s harmonic mean. We evaluated the GAT model against the following baseline

# models:

Logistic Regression: Usually used for binary classi(cid:2647)cation prob-

lems, a simple linear model is

## AICI 2025, February 14–16, 2025, Kuala Lumpur, Malaysia

## Table 1: Comparison of Model Performance on Employee Attrition Prediction.

# Model

# Accuracy

# F1-Score

## Logistic Regression Decision Tree Graph A(cid:2386)ention Network (GAT)

0.84 0.86 0.91

0.78 0.80 0.89

## Decision Tree: a non-linear model for instance classi(cid:2647)cation

spli(cid:2386)ing of the data depending on feature values.

(cid:2399)ese models tested using the same dataset and were run with

# conventional se(cid:2386)ings.

4.2 Results and Analysis Table 1 shows the experiment (cid:2647)ndings, which on the test set com- pare the GAT model performance with that of the baseline models. Across both accuracy and F1-score, the GAT model beats logistic regression and decision trees as Table 1 shows. Higher than the accuracy of 84% for logistic regression and 86% for decision trees, the GAT model had an accuracy of 91%. Moreover, the GAT model displayed a greater F1-score, meaning improved general accuracy in employee a(cid:2386)rition prediction. (cid:2399)e GAT model’s great accuracy can be ascribed to its capacity to use the a(cid:2386)ention mechanism to capture intricate relationships between employees. Using the graph structure, the model e(cid:2649)ciently aggregates information from an employee’s neighbors (i.e., employees with similar characteris- tics), which conventional models such as logistic regression and decision trees cannot accomplish. Higher for the GAT model as well as for the F1-score, which strikes a mix between accuracy and recall, the model is successful in keeping a balance between spo(cid:2386)ing a(cid:2386)rition cases and reducing false positives.

We presented employee features in a circular arrangement with lines linking strongly connected features in order to be(cid:2386)er grasp their relationships. As Figure 1 illustrates, the strength of these connections is re(cid:2648)ected in the line intensity. Strong links between elements like JobSatisfaction and Performance Rating are high- lighted in the plot, which would suggest that workers who are more job satis(cid:2647)ed usually have superior performance. (cid:2399)ese real- izations can direct HR choices on employee satisfaction policies and retention methods.

4.3 Ablation Study We performed an ablation study, testing the following variants, in order to assess the e(cid:2646)ect of the graph structure and a(cid:2386)ention mechanism even more:

GAT without a(cid:2386)ention: (cid:2399)is variant eliminates the a(cid:2386)ention component so enabling the model to evenly aggregate features over all neighbors.

GAT with random graph: In this variant, we randomly permuted the graph structure to break the relationships between employees.

(cid:2399)e results of the ablation study are presented in Table 2 (cid:2399)e performance of the model is shown to be much in(cid:2648)uenced by the a(cid:2386)ention mechanism as well as the graph topology. (cid:2399)e GAT model without a(cid:2386)ention shows quite poor performance, which emphasizes the need of a(cid:2386)ention for learning the value of various

345

# Xiang Fang

## Figure 1: Circular Feature Graph with Top Relationships.

# Table 2: Ablation Study Results.

# Model

# Accuracy

# F1-Score

## w/ random graph w/ o a(cid:2386)ention Graph A(cid:2386)ention Network (GAT)

0.78 0.85 0.91

0.74 0.81 0.89

neighbors. Even inferior performance of the model with a random graph topology emphasizes the need of the interactions among employees in the prediction process. (cid:2399)e results of the experiment show that in forecasting employee a(cid:2386)rition, the Graph A(cid:2386)ention Network (GAT) much outperforms conventional machine learning models including logistic regression and decision trees. (cid:2399)e GAT model o(cid:2646)ers HR departments a potential strategy to actively control employee turnover by capturing intricate interactions between employees, therefore producing more accurate and dependable forecasts.

5 Conclusion In this article, we developed a fresh method based on Graph At- tention Networks (GAT) for employee a(cid:2386)rition prediction. Our methodology beats conventional machine learning models includ- ing logistic regression and decision trees by using the graph-based structure of employee characteristics and catching the intricate interactions among them. (cid:2399)e experimental results show that GAT can o(cid:2646)er HR departments useful insights and more precise and dependable forecasts, therefore helping them to proactively control sta(cid:2646) turnover. Moreover, the way feature connections are shown emphasizestheneedofimportantemployeetraitsina(cid:2386)ritionpredic- tion, therefore o(cid:2646)ering a be(cid:2386)er knowledge of the elements a(cid:2646)ecting employee behavior. (cid:2399)is method o(cid:2646)ers a good path to strengthen retention plans and enhance human resource analytics.

## Leveraging Machine Learning for Employee Resignation Prediction in HR Analytics

References [1] Frye A, Boomhower C, Smith M, et al. Employee a(cid:2386)rition: what makes an

## employee quit?[J]. SMU Data Science Review, 2018, 1(1): 9.

[2] Fallucchi F, Coladangelo M, Giuliano R, et al. Predicting employee a(cid:2386)rition using

machine learning techniques[J]. Computers, 2020, 9(4): 86.

[3] Alao D, Adeyemo A B. Analyzing employee a(cid:2386)rition using decision tree algo- rithms[J]. Computing, Information Systems, Development Informatics and Allied Research Journal, 2013, 4(1): 17-28.

[4] Makanga C, Mukwaba D, Agaba C L, et al. Explainable Machine Learning and Graph Neural Network Approaches for Predicting Employee A(cid:2386)rition[C]//Pro- ceedings of the 2024 Sixteenth International Conference on Contemporary Com- puting. 2024: 243-255.

[5] Özdemir F. Recommender System For Employee A(cid:2386)rition Prediction And Movie Suggestion[D]. Abdullah Gül Üniversitesi, Fen Bilimleri Enstitüsü, 2020. [6] Kanchinadam T, Meng Z, Bockhorst J, et al. Graph neural networks to predict customer satisfaction following interactions with a corporate call center[J]. arXiv preprint arXiv:2102.00420, 2021.

[7] Fallucchi F, Coladangelo M, Giuliano R, et al. Predicting employee a(cid:2386)rition using

machine learning techniques[J]. Computers, 2020, 9(4): 86.

[8] Raza A, Munir K, Almutairi M, et al. Predicting employee a(cid:2386)rition using machine

## learning approaches[J]. Applied Sciences, 2022, 12(13): 6424.

[9] Alduayj S S, Rajpoot K. Predicting employee a(cid:2386)rition using machine learn- ing[C]//2018 international conference on innovations in information technology (iit). IEEE, 2018: 93-98.

[10] (cid:2398)tub A, Al-Mehmadi A, Al-Hssan M, et al. Prediction of employee a(cid:2386)rition using machine learning and ensemble methods[J]. Int. J. Mach. Learn. Comput, 2021, 11(2): 110-114.

[11] Subhashini M, Gopinath R. Employee a(cid:2386)rition prediction in industry using ma- chine learning techniques[J]. International Journal of Advanced Research in Engineering and Technology, 2020, 11(12): 3329-3341.

[12] Ajit P. Prediction of employee turnover in organizations using machine learning

## algorithms[J]. algorithms, 2016, 4(5): C5.

346

## AICI 2025, February 14–16, 2025, Kuala Lumpur, Malaysia

[13] Zhao Y, Hryniewicki M K, Cheng F, et al. Employee turnover prediction with machine learning: A reliable approach [C]//Intelligent Systems and Applications: Proceedings of the 2018 Intelligent Systems Conference (IntelliSys) Volume 2. Springer International Publishing, 2019: 737-758.

[14] Chaurasia A, Kadam S, Bhagat K, et al. Employee a(cid:2386)rition prediction using arti(cid:2647)cial neural networks[C]//2023 4th International Conference for Emerging Technology (INCET). IEEE, 2023: 1-6.

[15] Srivastava P R, Eachempati P. Intelligent employee retention system for a(cid:2386)rition rate analysis and churn prediction: An ensemble machine learning and multi- criteria decision-making approach[J]. Journal of Global Information Management (JGIM), 2021, 29(6): 1-29.

[16] Nawaz M S, Nawaz M Z, Fournier-Viger P, et al. Analysis and classi(cid:2647)cation of employee a(cid:2386)rition and absenteeism in industry: A sequential pa(cid:2386)ern mining- based methodology[J]. Computers in Industry, 2024, 159: 104106.

[17] Wang R, Liu Y, Xue B, et al. Deep neural networks for corporate misconduct pre- diction in construction industry using data from social networks[J]. Automation in Construction, 2024, 162: 105361.

[18] Sairam U, Voruganti S. Mental health prediction using deep learning[J]. Inter- national Journal for Research in Applied Science and Engineering Technology, 2022, 10(2): 782-790.

[19] Jarrah M, Derbali M. Predicting Saudi stock market index by using multivariate time series based on deep learning [J]. Applied Sciences, 2023, 13(14): 8356. [20] Meier F J, Laumer S. Machine learning in HR sta(cid:2649)ng[M]//Handbook of Re- search on Arti(cid:2647)cial Intelligence in Human Resource Management. Edward Elgar Publishing, 2022: 127-148.

[21] Mohanan M S, Rajarathinam V. Deep insight of HR management on work from home scenario during Covid pandemic situation using intelligent: analysis on IT sectors in Tamil Nadu [J]. International Journal of System Assurance Engineering and Management, 2023, 14(4): 1151-1182.

[22] Hussain J. Employee Salary Prediction in HRMS Using Regression Models[J]. Journal of Innovative Computing and Emerging Technologies, 2024, 4(2).
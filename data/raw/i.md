(cid:32)

(cid:32)

(cid:32)

(cid:32)

(cid:80)(cid:114)(cid:101)(cid:100)(cid:105)(cid:99)(cid:116)(cid:105)(cid:118)(cid:101)(cid:32)(cid:80)(cid:101)(cid:111)(cid:112)(cid:108)(cid:101)(cid:32)(cid:97)(cid:110)(cid:97)(cid:108)(cid:121)(cid:116)(cid:105)(cid:99)(cid:115)(cid:32)(cid:97)(cid:110)(cid:100)(cid:32)(cid:105)(cid:116)(cid:115)(cid:32)(cid:97)(cid:112)(cid:112)(cid:108)(cid:105)(cid:99)(cid:97)(cid:116)(cid:105)(cid:111)(cid:110)(cid:32)(cid:105)(cid:110)(cid:32) (cid:101)(cid:109)(cid:112)(cid:108)(cid:111)(cid:121)(cid:101)(cid:101)(cid:32)(cid:97)(cid:116)(cid:116)(cid:114)(cid:105)(cid:116)(cid:105)(cid:111)(cid:110)(cid:32)(cid:112)(cid:114)(cid:101)(cid:100)(cid:105)(cid:99)(cid:116)(cid:105)(cid:111)(cid:110)(cid:32)

Master’s thesis in Information Systems Supervisor: Professor Jozsef Mezei Faculty of Social Sciences, Business and Economics, and Law Åbo Akademi University Turku 2024

i

ÅBO AKADEMI UNIVERSITY – Faculty of Social Sciences, Business and Economics and Law

Abstract for master’s thesis Subject: Governance of Digitalization Writer: Mai Ho-Peltonen Title: Predictive People Analtyics and its application in employee attrition prediction Supervisor : Prof. Jozsef Mezei Abstract:

Human Resources (HR) has demonstrated its status as a dynamic business function

undergoing continual evolution. While traditional responsibilities such as workforce

management and talent acquisition remain pivotal, HR also faces the imperative to advance

its digital capabilities, where it lags behind other business functions. Empirical research

underscores the potential of People Analytics (PA) to substantially reduce HR and overall

business costs. However, despite its promise, People Analytics remains underutilized and

underdeveloped relative to its potential impact. Notably, Predictive Analytics emerges at the

forefront of PA, holding promise for delivering significant business value through informed

## decision-making and strategic planning across diverse organizational contexts.

# Through a comprehensive literature review of academic books and journals, empirical

research, and industry reports, the essential skills, resources, and technologies required for

effective People Analytics implementation are identified. Additionally, the thesis explores

the application of predictive analytics in employee retention using a HR dataset. The analysis

employed a comparative approach, assessing the effectiveness of various analytical methods:

Logistics Regression, Regression Tree and Random Forest. Notably, Random Forest

emerged as the most effective method for handling the complexity associated with multiple

predictive variables. Ethical aspects and challenges associated with predictive PA are also

discussed in this thesis at the same time with recommendations for future study endeavor.

Keywords: People Analytics, Predictive People Analytics, Human Resource Analytics,

## People Analytics Technology, Employee Retention, Attrition prediction.

Date: 09.04.2024

# Number of Pages: 94

ii

(cid:32)

# Table of Contents

(cid:67)(cid:104)(cid:97)(cid:112)(cid:116)(cid:101)(cid:114)(cid:32)(cid:49)(cid:58)(cid:32)(cid:73)(cid:110)(cid:116)(cid:114)(cid:111)(cid:100)(cid:117)(cid:99)(cid:116)(cid:105)(cid:111)(cid:110)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:32)(cid:49)

(cid:49)(cid:46)(cid:49)(cid:32)(cid:82)(cid:101)(cid:115)(cid:101)(cid:97)(cid:114)(cid:99)(cid:104)(cid:32)(cid:66)(cid:97)(cid:99)(cid:107)(cid:103)(cid:114)(cid:111)(cid:117)(cid:110)(cid:100)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:32)(cid:49) (cid:32) (cid:49)(cid:46)(cid:50)(cid:32)(cid:83)(cid:99)(cid:111)(cid:112)(cid:101)(cid:32)(cid:111)(cid:102)(cid:32)(cid:116)(cid:104)(cid:101)(cid:32)(cid:115)(cid:116)(cid:117)(cid:100)(cid:121)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:32)(cid:50) (cid:32) (cid:49)(cid:46)(cid:51)(cid:32)(cid:82)(cid:101)(cid:115)(cid:101)(cid:97)(cid:114)(cid:99)(cid:104)(cid:32)(cid:113)(cid:117)(cid:101)(cid:115)(cid:116)(cid:105)(cid:111)(cid:110)(cid:115)(cid:58)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:32)(cid:50) (cid:32) (cid:49)(cid:46)(cid:52)(cid:32)(cid:77)(cid:111)(cid:116)(cid:105)(cid:118)(cid:97)(cid:116)(cid:105)(cid:111)(cid:110)(cid:32)(cid:111)(cid:102)(cid:32)(cid:116)(cid:104)(cid:101)(cid:32)(cid:115)(cid:116)(cid:117)(cid:100)(cid:121)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:32)(cid:50) (cid:32) (cid:49)(cid:46)(cid:53)(cid:32)(cid:83)(cid:116)(cid:114)(cid:117)(cid:99)(cid:116)(cid:117)(cid:114)(cid:101)(cid:32)(cid:111)(cid:102)(cid:32)(cid:116)(cid:104)(cid:101)(cid:32)(cid:115)(cid:116)(cid:117)(cid:100)(cid:121)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:32)(cid:51) (cid:32) (cid:67)(cid:104)(cid:97)(cid:112)(cid:116)(cid:101)(cid:114)(cid:32)(cid:50)(cid:58)(cid:32)(cid:76)(cid:105)(cid:116)(cid:101)(cid:114)(cid:97)(cid:116)(cid:117)(cid:114)(cid:101)(cid:32)(cid:82)(cid:101)(cid:118)(cid:105)(cid:101)(cid:119)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:32)(cid:52) (cid:32) (cid:50)(cid:46)(cid:49)(cid:32)(cid:76)(cid:105)(cid:116)(cid:101)(cid:114)(cid:97)(cid:116)(cid:117)(cid:114)(cid:101)(cid:32)(cid:83)(cid:101)(cid:108)(cid:101)(cid:99)(cid:116)(cid:105)(cid:111)(cid:110)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:32)(cid:52) (cid:32) (cid:50)(cid:46)(cid:50)(cid:32)(cid:68)(cid:97)(cid:116)(cid:97)(cid:32)(cid:65)(cid:110)(cid:97)(cid:108)(cid:121)(cid:116)(cid:105)(cid:99)(cid:115)(cid:32)(cid:97)(cid:110)(cid:100)(cid:32)(cid:66)(cid:117)(cid:115)(cid:105)(cid:110)(cid:101)(cid:115)(cid:115)(cid:32)(cid:86)(cid:97)(cid:108)(cid:117)(cid:101)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:32)(cid:53) (cid:32)

(cid:50)(cid:46)(cid:50)(cid:46)(cid:49)(cid:32)(cid:65)(cid:110)(cid:97)(cid:108)(cid:121)(cid:116)(cid:105)(cid:99)(cid:115)(cid:32)(cid:116)(cid:111)(cid:32)(cid:66)(cid:117)(cid:115)(cid:105)(cid:110)(cid:101)(cid:115)(cid:115)(cid:32)(cid:107)(cid:110)(cid:111)(cid:119)(cid:108)(cid:101)(cid:100)(cid:103)(cid:101) (cid:50)(cid:46)(cid:50)(cid:46)(cid:50)(cid:32)(cid:72)(cid:111)(cid:119)(cid:32)(cid:116)(cid:111)(cid:32)(cid:101)(cid:120)(cid:116)(cid:114)(cid:97)(cid:99)(cid:116)(cid:32)(cid:118)(cid:97)(cid:108)(cid:117)(cid:101)(cid:32)(cid:111)(cid:117)(cid:116)(cid:32)(cid:111)(cid:102)(cid:32)(cid:100)(cid:97)(cid:116)(cid:97) (cid:50)(cid:46)(cid:50)(cid:46)(cid:51)(cid:32)(cid:68)(cid:97)(cid:116)(cid:97)(cid:32)(cid:116)(cid:121)(cid:112)(cid:101)(cid:32)(cid:97)(cid:110)(cid:100)(cid:32)(cid:100)(cid:97)(cid:116)(cid:97)(cid:32)(cid:115)(cid:111)(cid:117)(cid:114)(cid:99)(cid:101) (cid:50)(cid:46)(cid:50)(cid:46)(cid:52)(cid:32)(cid:83)(cid:99)(cid:111)(cid:112)(cid:101)(cid:32)(cid:111)(cid:102)(cid:32)(cid:68)(cid:97)(cid:116)(cid:97)(cid:32)(cid:65)(cid:110)(cid:97)(cid:108)(cid:121)(cid:116)(cid:105)(cid:99)(cid:115) (cid:50)(cid:46)(cid:50)(cid:46)(cid:53)(cid:32)(cid:70)(cid:114)(cid:97)(cid:109)(cid:101)(cid:119)(cid:111)(cid:114)(cid:107)(cid:32)(cid:116)(cid:111)(cid:32)(cid:103)(cid:101)(cid:116)(cid:32)(cid:107)(cid:110)(cid:111)(cid:119)(cid:108)(cid:101)(cid:100)(cid:103)(cid:101)(cid:32)(cid:102)(cid:114)(cid:111)(cid:109)(cid:32)(cid:68)(cid:97)(cid:116)(cid:97)(cid:32)(cid:65)(cid:110)(cid:97)(cid:108)(cid:121)(cid:115)(cid:105)(cid:115)

(cid:32) (cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:32)(cid:53)(cid:32) (cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:32)(cid:54)(cid:32) (cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:32)(cid:57)(cid:32) (cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:49)(cid:48)(cid:32) (cid:50)(cid:46)(cid:51)(cid:32)(cid:32)(cid:80)(cid:101)(cid:111)(cid:112)(cid:108)(cid:101)(cid:32)(cid:65)(cid:110)(cid:97)(cid:108)(cid:121)(cid:116)(cid:105)(cid:99)(cid:115)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:49)(cid:54) (cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:49)(cid:52)(cid:32)

(cid:50)(cid:46)(cid:51)(cid:46)(cid:49)(cid:32)(cid:68)(cid:101)(cid:102)(cid:105)(cid:110)(cid:105)(cid:116)(cid:105)(cid:111)(cid:110)(cid:32)(cid:111)(cid:102)(cid:32)(cid:80)(cid:101)(cid:111)(cid:112)(cid:108)(cid:101)(cid:32)(cid:65)(cid:110)(cid:97)(cid:108)(cid:121)(cid:116)(cid:105)(cid:99)(cid:115) (cid:50)(cid:46)(cid:51)(cid:46)(cid:50)(cid:32)(cid:72)(cid:105)(cid:115)(cid:116)(cid:111)(cid:114)(cid:121)(cid:32)(cid:111)(cid:102)(cid:32)(cid:80)(cid:101)(cid:111)(cid:112)(cid:108)(cid:101)(cid:32)(cid:65)(cid:110)(cid:97)(cid:108)(cid:121)(cid:116)(cid:105)(cid:99)(cid:115) (cid:50)(cid:46)(cid:51)(cid:46)(cid:51)(cid:32)(cid:70)(cid:105)(cid:118)(cid:101)(cid:32)(cid:83)(cid:116)(cid:97)(cid:103)(cid:101)(cid:115)(cid:32)(cid:111)(cid:102)(cid:32)(cid:80)(cid:101)(cid:111)(cid:112)(cid:108)(cid:101)(cid:32)(cid:65)(cid:110)(cid:97)(cid:108)(cid:121)(cid:116)(cid:105)(cid:99)(cid:115)(cid:32)(cid:68)(cid:101)(cid:118)(cid:101)(cid:108)(cid:111)(cid:112)(cid:109)(cid:101)(cid:110)(cid:116) (cid:50)(cid:46)(cid:51)(cid:46)(cid:52)(cid:32)(cid:84)(cid:104)(cid:101)(cid:32)(cid:97)(cid:100)(cid:111)(cid:112)(cid:116)(cid:105)(cid:111)(cid:110)(cid:32)(cid:109)(cid:111)(cid:100)(cid:101)(cid:108)(cid:32)(cid:111)(cid:102)(cid:32)(cid:80)(cid:101)(cid:111)(cid:112)(cid:108)(cid:101)(cid:32)(cid:65)(cid:110)(cid:97)(cid:108)(cid:121)(cid:116)(cid:105)(cid:99)(cid:115) (cid:50)(cid:46)(cid:51)(cid:46)(cid:53)(cid:32)(cid:65)(cid:100)(cid:111)(cid:112)(cid:116)(cid:105)(cid:111)(cid:110)(cid:32)(cid:70)(cid:114)(cid:97)(cid:109)(cid:101)(cid:119)(cid:111)(cid:114)(cid:107)(cid:32)(cid:111)(cid:102)(cid:32)(cid:80)(cid:65) (cid:50)(cid:46)(cid:51)(cid:46)(cid:53)(cid:32)(cid:84)(cid:104)(cid:101)(cid:32)(cid:118)(cid:97)(cid:108)(cid:117)(cid:101)(cid:32)(cid:111)(cid:102)(cid:32)(cid:68)(cid:97)(cid:116)(cid:97)(cid:32)(cid:65)(cid:110)(cid:97)(cid:108)(cid:121)(cid:116)(cid:105)(cid:99)(cid:115)

(cid:32) (cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:49)(cid:54)(cid:32) (cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:49)(cid:56)(cid:32) (cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:49)(cid:57)(cid:32) (cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:50)(cid:50)(cid:32) (cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:50)(cid:52)(cid:32) (cid:50)(cid:46)(cid:52)(cid:32)(cid:83)(cid:107)(cid:105)(cid:108)(cid:108)(cid:32)(cid:115)(cid:101)(cid:116)(cid:115)(cid:32)(cid:111)(cid:102)(cid:32)(cid:72)(cid:82)(cid:32)(cid:115)(cid:112)(cid:101)(cid:99)(cid:105)(cid:97)(cid:108)(cid:105)(cid:115)(cid:116)(cid:32)(cid:105)(cid:110)(cid:32)(cid:111)(cid:114)(cid:100)(cid:101)(cid:114)(cid:32)(cid:116)(cid:111)(cid:32)(cid:112)(cid:101)(cid:114)(cid:102)(cid:111)(cid:114)(cid:109)(cid:32)(cid:80)(cid:65)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:51)(cid:48) (cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:50)(cid:55)(cid:32) (cid:50)(cid:46)(cid:53)(cid:32)(cid:65)(cid:110)(cid:97)(cid:108)(cid:121)(cid:116)(cid:105)(cid:99)(cid:115)(cid:32)(cid:115)(cid:107)(cid:105)(cid:108)(cid:108)(cid:115)(cid:32)(cid:111)(cid:102)(cid:32)(cid:72)(cid:82)(cid:32)(cid:68)(cid:101)(cid:112)(cid:97)(cid:114)(cid:116)(cid:109)(cid:101)(cid:110)(cid:116)(cid:32)(cid:105)(cid:110)(cid:32)(cid:99)(cid:117)(cid:114)(cid:114)(cid:101)(cid:110)(cid:116)(cid:32)(cid:108)(cid:97)(cid:110)(cid:100)(cid:115)(cid:99)(cid:97)(cid:112)(cid:101)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:51)(cid:49) (cid:32) (cid:50)(cid:46)(cid:54)(cid:32)(cid:66)(cid:117)(cid:115)(cid:105)(cid:110)(cid:101)(cid:115)(cid:115)(cid:32)(cid:65)(cid:110)(cid:97)(cid:108)(cid:121)(cid:116)(cid:105)(cid:99)(cid:115)(cid:32)(cid:116)(cid:111)(cid:32)(cid:80)(cid:101)(cid:111)(cid:112)(cid:108)(cid:101)(cid:32)(cid:65)(cid:110)(cid:97)(cid:108)(cid:121)(cid:116)(cid:105)(cid:99)(cid:115)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:51)(cid:51) (cid:32) (cid:50)(cid:46)(cid:55)(cid:32)(cid:80)(cid:101)(cid:111)(cid:112)(cid:108)(cid:101)(cid:32)(cid:65)(cid:110)(cid:97)(cid:108)(cid:121)(cid:116)(cid:105)(cid:99)(cid:115)(cid:32)(cid:77)(cid:97)(cid:116)(cid:117)(cid:114)(cid:105)(cid:116)(cid:121)(cid:32)(cid:109)(cid:111)(cid:100)(cid:101)(cid:108)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:51)(cid:52) (cid:32) (cid:50)(cid:46)(cid:56)(cid:32)(cid:80)(cid:114)(cid:101)(cid:100)(cid:105)(cid:99)(cid:116)(cid:105)(cid:118)(cid:101)(cid:32)(cid:97)(cid:110)(cid:97)(cid:108)(cid:121)(cid:115)(cid:105)(cid:115)(cid:32)(cid:102)(cid:111)(cid:114)(cid:32)(cid:111)(cid:114)(cid:103)(cid:97)(cid:110)(cid:105)(cid:122)(cid:97)(cid:116)(cid:105)(cid:111)(cid:110)(cid:32)(cid:112)(cid:101)(cid:114)(cid:102)(cid:111)(cid:114)(cid:109)(cid:97)(cid:110)(cid:99)(cid:101)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:51)(cid:54) (cid:32) (cid:50)(cid:46)(cid:57)(cid:32)(cid:87)(cid:104)(cid:97)(cid:116)(cid:32)(cid:100)(cid:97)(cid:116)(cid:97)(cid:32)(cid:104)(cid:97)(cid:118)(cid:101)(cid:32)(cid:98)(cid:101)(cid:101)(cid:110)(cid:32)(cid:117)(cid:115)(cid:101)(cid:100)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:51)(cid:54) (cid:32) (cid:50)(cid:46)(cid:49)(cid:48)(cid:32)(cid:68)(cid:97)(cid:116)(cid:97)(cid:32)(cid:65)(cid:99)(cid:113)(cid:117)(cid:105)(cid:115)(cid:105)(cid:116)(cid:105)(cid:111)(cid:110)(cid:32)(cid:97)(cid:110)(cid:100)(cid:32)(cid:72)(cid:82)(cid:32)(cid:73)(cid:84)(cid:32)(cid:73)(cid:110)(cid:102)(cid:114)(cid:97)(cid:115)(cid:116)(cid:114)(cid:117)(cid:99)(cid:116)(cid:117)(cid:114)(cid:101)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:51)(cid:57) (cid:32)

(cid:50)(cid:46)(cid:49)(cid:48)(cid:46)(cid:49)(cid:32)(cid:67)(cid:117)(cid:114)(cid:114)(cid:101)(cid:110)(cid:116)(cid:32)(cid:83)(cid:116)(cid:97)(cid:116)(cid:101) (cid:50)(cid:46)(cid:49)(cid:48)(cid:46)(cid:50)(cid:32)(cid:73)(cid:110)(cid:102)(cid:114)(cid:97)(cid:115)(cid:116)(cid:114)(cid:117)(cid:99)(cid:116)(cid:117)(cid:114)(cid:101)(cid:32)(cid:97)(cid:115)(cid:32)(cid:101)(cid:110)(cid:97)(cid:98)(cid:108)(cid:101)(cid:114)

(cid:32) (cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:51)(cid:57)(cid:32) (cid:50)(cid:46)(cid:49)(cid:49)(cid:32)(cid:80)(cid:101)(cid:111)(cid:112)(cid:108)(cid:101)(cid:32)(cid:97)(cid:110)(cid:97)(cid:108)(cid:121)(cid:116)(cid:105)(cid:99)(cid:115)(cid:32)(cid:83)(cid:99)(cid:111)(cid:112)(cid:101)(cid:32)(cid:111)(cid:102)(cid:32)(cid:97)(cid:110)(cid:97)(cid:108)(cid:121)(cid:115)(cid:105)(cid:115)(cid:58)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:52)(cid:51) (cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:52)(cid:48)(cid:32) (cid:50)(cid:46)(cid:49)(cid:50)(cid:32)(cid:80)(cid:101)(cid:111)(cid:112)(cid:108)(cid:101)(cid:32)(cid:65)(cid:110)(cid:97)(cid:108)(cid:121)(cid:116)(cid:105)(cid:99)(cid:115)(cid:32)(cid:102)(cid:114)(cid:97)(cid:109)(cid:101)(cid:119)(cid:111)(cid:114)(cid:107)(cid:58)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:52)(cid:52) (cid:32) (cid:50)(cid:46)(cid:49)(cid:51)(cid:32)(cid:80)(cid:114)(cid:101)(cid:100)(cid:105)(cid:99)(cid:116)(cid:105)(cid:118)(cid:101)(cid:32)(cid:97)(cid:110)(cid:97)(cid:108)(cid:121)(cid:116)(cid:105)(cid:99)(cid:115)(cid:32)(cid:119)(cid:105)(cid:116)(cid:104)(cid:32)(cid:80)(cid:121)(cid:116)(cid:104)(cid:111)(cid:110)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:53)(cid:51) (cid:32)

iii

(cid:32)

(cid:67)(cid:104)(cid:97)(cid:112)(cid:116)(cid:101)(cid:114)(cid:32)(cid:51)(cid:58)(cid:32)(cid:80)(cid:114)(cid:101)(cid:100)(cid:105)(cid:99)(cid:116)(cid:105)(cid:118)(cid:101)(cid:32)(cid:65)(cid:110)(cid:97)(cid:108)(cid:121)(cid:115)(cid:105)(cid:115)(cid:32)(cid:102)(cid:111)(cid:114)(cid:32)(cid:69)(cid:109)(cid:112)(cid:108)(cid:111)(cid:121)(cid:101)(cid:101)(cid:32)(cid:65)(cid:116)(cid:116)(cid:114)(cid:105)(cid:116)(cid:105)(cid:111)(cid:110)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:32)(cid:53)(cid:52)

(cid:51)(cid:46)(cid:49)(cid:32)(cid:68)(cid:97)(cid:116)(cid:97)(cid:115)(cid:101)(cid:116)(cid:32)(cid:101)(cid:120)(cid:112)(cid:108)(cid:111)(cid:114)(cid:97)(cid:116)(cid:105)(cid:111)(cid:110)(cid:32)(cid:97)(cid:110)(cid:100)(cid:32)(cid:99)(cid:108)(cid:101)(cid:97)(cid:110)(cid:105)(cid:110)(cid:103)(cid:32)(cid:117)(cid:115)(cid:105)(cid:110)(cid:103)(cid:32)(cid:80)(cid:121)(cid:116)(cid:104)(cid:111)(cid:110)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:53)(cid:52) (cid:32) (cid:51)(cid:46)(cid:50)(cid:32)(cid:76)(cid:111)(cid:103)(cid:105)(cid:115)(cid:116)(cid:105)(cid:99)(cid:32)(cid:114)(cid:101)(cid:103)(cid:114)(cid:101)(cid:115)(cid:115)(cid:105)(cid:111)(cid:110)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:54)(cid:51) (cid:32) (cid:51)(cid:46)(cid:51)(cid:32)(cid:80)(cid:114)(cid:101)(cid:100)(cid:105)(cid:99)(cid:116)(cid:105)(cid:118)(cid:101)(cid:32)(cid:65)(cid:110)(cid:97)(cid:108)(cid:121)(cid:115)(cid:105)(cid:115)(cid:32)(cid:119)(cid:105)(cid:116)(cid:104)(cid:32)(cid:76)(cid:111)(cid:103)(cid:105)(cid:115)(cid:116)(cid:105)(cid:99)(cid:32)(cid:82)(cid:101)(cid:103)(cid:114)(cid:101)(cid:115)(cid:115)(cid:105)(cid:111)(cid:110)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:54)(cid:51) (cid:32) (cid:51)(cid:46)(cid:52)(cid:32)(cid:84)(cid:114)(cid:101)(cid:101)(cid:32)(cid:97)(cid:110)(cid:100)(cid:32)(cid:82)(cid:97)(cid:110)(cid:100)(cid:111)(cid:109)(cid:32)(cid:70)(cid:111)(cid:114)(cid:101)(cid:115)(cid:116)(cid:32)(cid:119)(cid:105)(cid:116)(cid:104)(cid:32)(cid:80)(cid:121)(cid:116)(cid:104)(cid:111)(cid:110)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:54)(cid:54) (cid:32) (cid:51)(cid:46)(cid:53)(cid:32)(cid:73)(cid:109)(cid:112)(cid:108)(cid:101)(cid:109)(cid:101)(cid:110)(cid:116)(cid:105)(cid:110)(cid:103)(cid:32)(cid:84)(cid:114)(cid:101)(cid:101)(cid:32)(cid:82)(cid:101)(cid:103)(cid:114)(cid:101)(cid:115)(cid:115)(cid:105)(cid:111)(cid:110)(cid:32)(cid:97)(cid:110)(cid:100)(cid:32)(cid:82)(cid:97)(cid:110)(cid:100)(cid:111)(cid:109)(cid:32)(cid:70)(cid:111)(cid:114)(cid:101)(cid:115)(cid:116)(cid:32)(cid:32)(cid:119)(cid:105)(cid:116)(cid:104)(cid:32)(cid:80)(cid:121)(cid:116)(cid:104)(cid:111)(cid:110)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:54)(cid:56) (cid:32) (cid:51)(cid:46)(cid:54)(cid:32)(cid:67)(cid:111)(cid:110)(cid:99)(cid:108)(cid:117)(cid:115)(cid:105)(cid:111)(cid:110)(cid:32)(cid:102)(cid:114)(cid:111)(cid:109)(cid:32)(cid:97)(cid:110)(cid:97)(cid:108)(cid:121)(cid:115)(cid:105)(cid:115)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:55)(cid:54) (cid:32) (cid:67)(cid:104)(cid:97)(cid:112)(cid:116)(cid:101)(cid:114)(cid:32)(cid:52)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:32)(cid:55)(cid:55) (cid:32) (cid:52)(cid:46)(cid:49)(cid:32)(cid:69)(cid:116)(cid:104)(cid:105)(cid:99)(cid:115)(cid:32)(cid:97)(cid:110)(cid:100)(cid:32)(cid:79)(cid:116)(cid:104)(cid:101)(cid:114)(cid:32)(cid:67)(cid:111)(cid:110)(cid:115)(cid:105)(cid:100)(cid:101)(cid:114)(cid:97)(cid:116)(cid:105)(cid:111)(cid:110)(cid:115)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:55)(cid:55) (cid:32) (cid:52)(cid:46)(cid:50)(cid:32)(cid:80)(cid:114)(cid:101)(cid:100)(cid:105)(cid:99)(cid:116)(cid:105)(cid:118)(cid:101)(cid:32)(cid:97)(cid:110)(cid:97)(cid:108)(cid:121)(cid:116)(cid:105)(cid:99)(cid:115)(cid:32)(cid:99)(cid:114)(cid:105)(cid:116)(cid:105)(cid:99)(cid:105)(cid:115)(cid:109)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:55)(cid:56) (cid:32) (cid:52)(cid:46)(cid:51)(cid:32)(cid:79)(cid:116)(cid:104)(cid:101)(cid:114)(cid:32)(cid:115)(cid:117)(cid:103)(cid:103)(cid:101)(cid:115)(cid:116)(cid:105)(cid:111)(cid:110)(cid:115)(cid:32)(cid:116)(cid:111)(cid:32)(cid:117)(cid:116)(cid:105)(cid:108)(cid:105)(cid:122)(cid:101)(cid:32)(cid:80)(cid:101)(cid:111)(cid:112)(cid:108)(cid:101)(cid:32)(cid:65)(cid:110)(cid:97)(cid:108)(cid:121)(cid:116)(cid:105)(cid:99)(cid:115)(cid:32)(cid:111)(cid:114)(cid:32)(cid:80)(cid:114)(cid:101)(cid:100)(cid:105)(cid:99)(cid:116)(cid:105)(cid:118)(cid:101)(cid:32)(cid:65)(cid:110)(cid:97)(cid:108)(cid:121)(cid:116)(cid:105)(cid:99)(cid:115)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:55)(cid:57) (cid:32) (cid:52)(cid:46)(cid:52)(cid:32)(cid:69)(cid:108)(cid:101)(cid:109)(cid:101)(cid:110)(cid:116)(cid:115)(cid:32)(cid:116)(cid:111)(cid:32)(cid:69)(cid:118)(cid:111)(cid:108)(cid:117)(cid:116)(cid:105)(cid:111)(cid:110)(cid:32)(cid:111)(cid:102)(cid:32)(cid:80)(cid:101)(cid:111)(cid:112)(cid:108)(cid:101)(cid:32)(cid:65)(cid:110)(cid:97)(cid:108)(cid:121)(cid:116)(cid:105)(cid:99)(cid:115)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:56)(cid:48) (cid:32) (cid:67)(cid:104)(cid:97)(cid:112)(cid:116)(cid:101)(cid:114)(cid:32)(cid:53)(cid:58)(cid:32)(cid:68)(cid:105)(cid:115)(cid:99)(cid:117)(cid:115)(cid:115)(cid:105)(cid:111)(cid:110)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:32)(cid:56)(cid:50) (cid:32)

(cid:65)(cid:112)(cid:112)(cid:101)(cid:110)(cid:100)(cid:105)(cid:120)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:32)(cid:56)(cid:53) (cid:32)

(cid:82)(cid:101)(cid:102)(cid:101)(cid:114)(cid:101)(cid:110)(cid:99)(cid:101)(cid:32)(cid:108)(cid:105)(cid:115)(cid:116)(cid:58)(cid:32)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:46)(cid:32)(cid:56)(cid:55) (cid:32)

iv

(cid:32)

# List of Figures

Figure 1: Analytics Process ....................................................................................................... 7 Figure 2: Cost of Storage and data availability ......................................................................... 8 (cid:32) Figure 3: Datatype ................................................................................................................... 10 (cid:32) Figure 4: Big Data Processes .................................................................................................. 11 (cid:32) Figure 5: Data Analysis Levels ................................................................................................ 11 (cid:32) Figure 6: Descriptive Analytics Model ..................................................................................... 12 (cid:32) Figure 7: Predictive Analytics Model ....................................................................................... 13 (cid:32) Figure 8: Prescriptive Analytics Model .................................................................................... 14 (cid:32) Figure 9: Process View of Data Analytics ............................................................................... 15 (cid:32) Figure 10: Five Ages of People Analytics .............................................................................. 20 (cid:32) Figure 11: Nine Dimensions for Excellence in People Analytics Models .............................. 22 (cid:32) Figure 12: IMPACT model ....................................................................................................... 26 (cid:32) Figure 13: Analytics Achievement ........................................................................................... 29 (cid:32) Figure 14:Six elements of an excellent People Analytics Expert ............................................ 31 (cid:32) Figure 15: People Data Analyst skills ..................................................................................... 33 (cid:32) Figure 16: People Analytics Maturity Model ............................................................................ 35 (cid:32) Figure 17: From Business Question to People Analytics ........................................................ 37 (cid:32) Figure 18: Waves of People Analytics Technology ................................................................. 41 (cid:32) Figure 19: People Analytics Continuum .................................................................................. 43 (cid:32) Figure 20: Job seeker’s journey .............................................................................................. 47 (cid:32) (cid:32)

# List of Table

Table 1: Authors and People Analytics ................................................................................... 52

# List of Abbreviation

# PA

# People Analytics

# HR

# Human Resource

# HRA

# Human Resource Analytics

v

# Chapter 1: Introduction

# 1.1 Research Background

Human resources are undoubtedly a critical resource for various organizations. Although the

HR function has been considered a cost center and a business supporting center, research has

proven that the HR function is an evolving business function and has become an essential

business strategy driver. Managing the workforce and reaching out to the labor pool is a

significant part of the operation. Still, HR needs to catch up in digitization compared to other

business functions (Isson et al.,p.6, page 29). PA is still in its early stage; a mere 16% of

organizations have conducted advanced PA based on the Sierra-Cedar survey in 2018,

conducted by 1636 organizations in over 70 countries. Digitalization has impacted the

workplace in different ways (Cijan et al., 2019). The process has brought with it novel

professions and novel tasks, as simple operation repetitive tasks, and machines and different

equipment now perform other labor-intensive jobs while needs for new competencies and skills

arise. New working conditions have been introduced: in addition to full-time, on-site

employee: hybrid, remote work or freelancing. The process has changed how disputes between

organizations and their employees are settled. Understanding the workforce motivation,

technological skills, concerns, and value at work is vital.

Regarding the US and Western labor market, McKinsey (2021) also raised an alert about a

<Great Attrition= when labor shortages happen in various industries. Technology has increased

job satisfaction but also offers flexibility regarding career changes and job searches (Cijan et

al., 2019). The competition in talent recruiting has also become fierce because of globalization,

which provides opportunities and challenges while inducing highly skilled workers’s mobility.

People tend to be loyal to their profession, but their engagement in their workplaces has

decreased over time; in other words, we have witnessed a continuous decrease in highly skilled

## workers’ average working time at one corporation.

Pease et al. (2014, page 2) postulate the difference in beliefs and life experiences between

generations currently in the workforce. Isson (2016) suggests that the new generations enter

the job market and bring different employer-employee dynamics, which should be understood.

McKinsey's Global Growth Model study suggests that in 2015, the US Deloitte consulting

ranked the cost for HR recruitment, retention, and relocation at 400 billion dollars. Expensive

1

as it was, employees, in general, report being underused at work. A survey by the talent

mobility firm Lee Hecht Harrison reveals that 86% of workers say they often (62%) or

sometimes (24%) feel underutilized in their jobs.

The workforce, which considered to be the most valuable asset of many businesses, needs to

be understood the same way companies understand their customers. Technology development

has allowed corporations to retain and utilize their relevant data for analysis. The PA is believed

to provide the HR department with tools to generate knowledge for decision-making.

# 1.2 Scope of the study

This research's notable limitation is its reliance on secondary data sources. The dataset

employed for the purpose of data analysis is sourced from publicly available repositories.

# 1.3 Research questions:

- 1. What techniques of PA and predictive analytics are being used? What are the essential

skills and resources required to utilize and analyze data?

- 2. What specific data points are typically collected for People Analytics and predictive

# analysis?

- 3. How is the collected data processed and prepared for attrition prediction modeling?

Predictive modeling for attrition rate with three methods Logistic Regression,

Classification Tree, and Random Forest, using a public dataset.

# 1.4 Motivation of the study

First to contribute to the process of facilitating the integration of data analytics within the realm

of Human Resources (HR) in the contemporary era of digitalization. By embracing data

analytics, HR functions can effectively align themselves with the ongoing advancements,

which can be observed across various other business sectors. This strategic alignment is crucial

2

to ensure that HR remains synchronized with the rapid evolution of modern business practices.

Leveraging data analytics enables HR to extract actionable insights from the available

information, thereby fostering informed decision-making and precision in workforce

management. Embracing this transformative approach empowers HR to keep pace with other

functional domains and proactively contribute to the organization's overarching objectives,

ultimately bolstering operational efficiency and strategic efficacy.

Secondly, To examine the strategic utilization of predictive analytics within the Human

Resources (HR) domain and to ascertain the business value inherent in its application. The

investigation seeks to delve into the methodologies and practices through which predictive

analytics can be harnessed effectively within HR processes. By delving into this realm, the

thesis intends to unravel the tangible benefits and potential gains that organizations attain by

embracing predictive analytics in their HR operations.

Thirdly, this study aims to make a meaningful contribution to the existing body of literature

# surrounding People Analytics.

# 1.5 Structure of the study

# Chapter 1: Introduction

This chapter will present a comprehensive overview of the thesis framework, encompassing its

intention, arrangement, and contextual backdrop. Furthermore, the chapter will describe the

## fundamental objectives and goals of the research.

# Chapter 2: Literature review

# Data Analytics

This literature review section encompasses academic discussions regarding data analytics and

Big Data analytics, exploring their respective frameworks for extracting information to enrich

business knowledge and strengthen business strategy. The review covers topics such as data

types and sources, the diverse scopes of data analytics, and their influence on business

performance. Additionally, it investigates the value derived from data analytics in terms of its

## impact on both business and financial outcomes.

3

# People Analytics

It explores the practical implementation of People Analytics (PA) across a spectrum of

scenarios and delves into the various data sources involved. Furthermore, the chapter reviews

the essential infrastructure and technology needed to ensure the success of People Analytics

initiatives. In addition, it offers a closer look at the skill sets required for HR analysts,

identifying and defining existing gaps in proficiency and highlighting the value predictive PA

# brings to business.

# Chapter 3: Regression in People Analytics, an application of Regression, Classification Tree

and Random Forest in Attrition prediction. More specifically, this chapter discusses the

utilization of these three techniques in People Analytics as a strategic approach, particularly in

the context of attrition prediction. This analysis involves applying regression analysis to

forecast and understand the factors influencing employee attrition within an organization.

Chapter 4: is a discussion of the ethical dimensions and various arguments surrounding People

# Analytics (PA) topics.

Additionally, this section introduces alternative suggestions for enhancing the effectiveness

## and quality of People Analytics practices.

## Chapter 5: a discussion of the whole thesis.

# Chapter 2: Literature Review

# 2.1 Literature Selection

A comprehensive search strategy was devised to identify scholarly works related to the research

topic. Databases of reputable academic repositories of Åbo Akademi and Google Scholar were

meticulously queried, encompassing a diverse range of disciplines and fields relevant to the

subject. Specific keywords and criteria delimited the search to ensure relevance and coherence.

Moreover, a manual screening process was conducted to refine the inclusion of studies aligning

with the research objectives further. The final collection of literature is characterized by its

4

significance in contributing to the research endeavor's conceptual framework and theoretical

# underpinning.

The literature was selected from academic research articles, books, university blogs, and other

# official HR association reports.

# The literature retrieval process:

The process of literature retrieval involved utilizing the following keywords for searching book

# titles: "Human resource analytics," "People Analytics," and "Workforce Analytics" on

abo.finna.fi in the English language across all fields. The initial search yielded 32 books. The

literature list was subsequently refined through careful screening, narrowing it down to a final

# selection of 11 relevant books.

The literature list also consists of materials recommended by the Supervisor and backward-

chaining citations from the academic books.

# 2.2 Data Analytics and Business Value

The comprehensive literature review delves into prior studies concerning the subjects of Data

and Big Data analytics. It presents an extensive overview of literature pertaining to Human

Resource Analytics or People Analytics (PA) encompassing skill sets and competencies.

The review also introduces insights into the realm of PA within the business context.

Furthermore, it explains the domain of knowledge discovery facilitated through adept data

analysis techniques. By examining these areas, the literature review offers a comprehensive

# understanding of the interplay between data, analytics, human resources, and business.

The literature review was conducted using Åbo Akademi library system alma.abo.fi and

# Google Scholar

# 2.2.1 Analytics to Business knowledge

The analysis of the primary research studies revealed that the adoption of Big Data Analytics

(BDA) provides firms with knowledge regarding different factors, such as innovation,

information, agility market knowledge, technology knowledge, human resource knowledge,

and business knowledge (Hinawi, 2023). Data analysis or BDA facilitates companies in

5

enhancing their financial or non-financial performance with competitive advantage (van de

Wetering et al., 2019; Wamba et al., 2017). This improvement is realized at its most when

managers pay attention to data infrastructure capability, as well as planning, investment,

coordination, and control. The factors of advanced BDA tools and employees with strong

analytical skills are also crucial to improving companies' performance using BDA (Wamba et

al., 2017). When companies make adequate investments in BDA solutions, it can result in

increased customer satisfaction and better overall market performance, consequently

contributing to the enhancement of the company's financial performance.

Research suggests that companies that effectively utilize BDA resources tend to perform better,

primarily when operating in expanding markets.

## According to Asadi Someh & Shanks (2015), Big Data Analytics (BDA) significantly

improves the overall performance of companies, particularly in markets experiencing

growth. Wamba et al. (2017) investigated the relationship between BDA resources and

company performance. They found evidence that BDA is positively correlated with companies’

performance and this is especially true in markets that are currently expanding.

In the realm of big data, possessing a robust BDA empowers companies to uncover valuable

patterns, trends, and knowledge that can inform strategic decisions and innovative initiatives.

Wamba et al. (2017) suggest that by cultivating and harnessing BDA, companies can gain a

competitive edge that will last over time. This stems from the capacity to make well-informed,

data-driven decisions, swiftly adapt to changing market conditions, and proactively address

emerging challenges. The ability to leverage big data analytics effectively enables companies

to optimize their operations, enhance customer experiences, identify new market opportunities,

and craft targeted marketing strategies.

2.2.2 How to extract value out of data

6

# Figure 1: Analytics Process

# (Ruohonen,S.( 2015( Combine from Modified from Fitz-enz and Mattox (2014)and Gartner

(2013)

Data analytics : A definition of data analytics and different levels of data analytics.

Data is defined by the Oxford Dictionary as1. facts or information, especially when examined

and used to discover things or make decisions. 2. information that is stored by a computer. Data

is the collection of factual information existing in all many different types and formats, for

## example, text, number or even image or sound.

Meanwhile, the amount of data retained is continuously growing due to the advancement of

technology. In 2011, IBM estimated that 90% of the world's data was created in several

previous years, while the UN stated that the amount of data in 2011 alone was more significant

than that of the whole history of humanity. As data storage becomes more affordable, data

# becomes cheaper and ubiquitous.

With this tremendous amount of facts available, it is necessary to change it to information with

context and knowledge that businesses can consume to create value. Therefore, a need for data

# analysis.

7

## Figure 2: Cost of Storage and data availability

# (Source: James Evan (2017))

According to Evans (2017), data analysis employs statistical tools, other mathematical

methods, and information technology to draw insight from data. Evans also defines data

analysis for business as <a process of transforming data into actions through analysis and

# insights in the context of organizational decision-making and problem-solving.= Fit-enz and

Matox (2014) describe analytics as a <merging of art and science= when combining the

statistical method, logical sense of the data, and mental framework of the context to understand

the status and get actionable recommendations and some predictions of the future.

Analytics is also described as a process based in factual information to yield insights and

# potential implications for future actions within an organizational context. This process

encompasses various practices, ranging from basic monitoring of facts and indicators to the

utilization of advanced analytical methods. What ties these various practices together is their

shared reliance on factual data and a "rational" foundation.

Data analytics (DA) and its mining technique are methods to identify and discover new

knowledge (Frawley, PiatetskyShapiro, and Matheus,1991). Davenport and Harris writes: <the

extensive use of data, statistical and quantitative analysis, explanatory and predictive models,

and fact-based management to drive decisions and actions=. Stubbs (2011) defines DA as <a

process that involves the use of statistical techniques (measures of central tendency, graphs and

so on), information system software (data mining, sorting routines) and operations research

methodologies (linear programming) to explore, visualize, discover and communicate patterns

8

or trends in data=. Data analysis is a process of extracting knowledge, and insights ( Gandomi

&Haide, 2014)

# 2.2.3 Data type and data source

Data is classified as structured, semistructured and unstructured. (Bay University, 2020)

Structured data: arranged in a table and has a tabular schema with distinct rows and columns

to denote instances and features, making it easier to process and analyze.. Structured data is

valuable to business, and it’s quite easy to gather structured data from different sources.

Traditionally, business data is in structured format however, with the growing demand for

knowledge extraction, the need to analyze unstructured data of business was raised.

Unstructured data, on the other hand, <has no predefined conceptual definition= which makes

it not easy to analyze. Unstructured data grows enormously in amount and makes a significant

part of big data. Data from sources like social media is unstructured, and other typical

unstructured data businesses usually deal with are emails, meeting minutes, call records, or in

People analytics, unstructured data are job seeker’s curriculum vitae and cover letters..

Semi-structured data is a hybrid of the above two groups.

Soraya (2018, page 5,6,7) suggests classifying data type into four categories: Database, Raw

# data, Text and Internet of Things.

Database, where various types of structured data can be found. Data from organizations that

are nicely placed on spreadsheets such as M.S. Excel, accounting systems, banking transaction

recording systems, etc.

Raw data, which is complex, unclean, and needs preprocessing before it can be used for

analyzing

Text: By this, the book’s author refers to all natural language text from books, articles

Images, audio, and video: this type of unstructured data which are becoming more ubiquitous

# recently.

Internet of Things (IoT): The amount of data by IoT went up by tenfold within seven years,

from 2013 to 2020.

9

# Figure 3: Datatype

## (Source: Soraya Sedkaoui, Data, and Big Data Analytics, 2018)

# 2.2.4 Scope of Data Analytics

Gandomi and Haider (2014) explain the data analytics processes with citation from the work

of Labrinidis & Jagadish, 2012, whose work divides the analysis process into five phases. The

first three phases are under the Data Management stage.

In the Acquisition phase, data is collected from different sources such as online databases,

social media platforms, or public records, and recorded to the database system. Data is rarely

collected, being clean and ready for analysis but always comes in messy, duplicated,

inconsistent, and incomplete format. In the next step, data needs to be cleaned, filtered, and

transformed into a format ready for analysis. The next stage may involve tasks such as data

## cleansing, data normalization, data integration, and data sampling.

The Analytics phase is called by Gandomi and Haider (2015) as <insight extraction= phase,

which utilizes many tools and techniques (Caughlin, 2022) :

- Mathematics, which includes arithmetic, geometry, and calculus

- Statistics, which includes descriptive statistics, inferal statistics, parametric statistics

# and nonparametric statistics

- Machine learning which has two main sub-categories: supervised machine learning and

# unsupervised machine learning

- Computational modeling and simulations

10

- Text analyses and qualitative analyses

# Figure 4: Big Data Processes

# (Source: Gandomi& Haider, 2015)

Traditionally there are three levels of big data analysis for business insights in practices:

descriptive analytics, predictive analytics and prescriptive analytics. At different levels,

analytics unlock different values from data on hand and leverage them for different purposes.

## Figure 5: Data Analysis Levels (Source: Fitz-Enz, 2012)

11

# Descriptive analysis:

This is the ground level of data analysis, where the facts are presented in the form of a chart

in different forms: line chart, bar chart, pie chart, histogram… and other statistical metrics for

example mean, mode, median, standard deviation, range.. Descriptive analysis uses key

indicators to demonstrate what has already happened in the past and give a <snapshot= of the

past. Fitz-enz and Mattox explain that descriptive analysis in HR analytics <reveal and describe

relationships and current and historical data patterns=. Besides the above statistical method for

scorecard, reporting, and dashboard, there are many mining techniques to leverage and find

patterns using clustering, segmentation..

# Figure 6: Descriptive Analytics Model

# (Caughlin, 2022)

# Predictive analysis:

Predictive analysis, as stated by Fitz-En (2010), is the insight to the future, and <the greatest

asset anyone can have=. It is a process of utilizing historical data to make predictions based on

statistical algorithms and machine learning techniques to identify the likelihood of future

outcomes based on patterns and trends in the data with the underlying assumption that the past

event and trend tend to happen again in the future. Predictive analysis can be as simple as

moving averages, aiming to recognize patterns from the past in the outcome variable(s) and

extend those patterns into the future. Predictive analysis can be processed using statistics,

modeling, and data mining techniques such as regression, which aim to grasp the relationships

between outcome variable(s) and explanatory variables, utilizing these connections to

# formulate predictions: decision tree, neural network, support vector machine (SVM) nearest

neighbor (Duan & Xiong, 2014). Predictive analysis also includes other stages In HR,

predictive models are used, for example, to predict in employee recruitment. This can be done

12

using data from previous years to estimate the logistic regression model to find predictors. The

model can be applied for new data to predict recruitment plans for the coming year.

According to Bersin's (2012) study, in the same year, only four percent of companies are using

the highest level of HR analytics, which is the predictive level.

## Figure 7: Predictive Analytics Model (Caughlin, 2022)

# Prescriptive analytics

Prescriptive analysis uses <mathematical programming, heuristic search and simulation

modeling to identify the optimal actions= (Duan & Xiong, 2014). It is a process of <prescribing

action and making targeted recommendations based on predictive-analytics finding=

(Caughlin, 2022) The result of prescriptive analysis are options and outcomes for each option.

It offers decision-makers better understandings of the situation when choosing different

alternatives and therefore can generate the best possible outcome.

In business, prescriptive solutions aid business analysts in decision-making by identifying

actions and evaluating their consequences concerning business goals, needs, and limitations.It

is possible to think about prescriptive analytics as a <if..else= statement and take into

consideration its objective and other constraints using algorithms.

According to Fitz-en and Matox (2014), it is rare to be able to see the impact of alternative

investment on the bottom line. Sivarajah et al. (2017) also conclude that the number of effective

prescriptive analytics instances in practical settings is quite scarce.

13

## Figure 8: Prescriptive Analytics Model (Caughlin, 2022)

2.2.5 Framework to get knowledge from Data Analysis

Bain and Company research in 2013 (quoted from Pease 2015, page 22) reveals , the more

advanced analytics a business performs, <the greater the margin by which it outperformed its

# competitors=.

Regarding the advanced analytics users, it is stated by Bain and company that they have double

their chance to be in the top quartile in financial performance among other players in their

industries. Moreover, advanced analytics users make faster decisions at about five times and

have three times more chance to execute decisions as pe planned. They also use data analytics

for making decision twice as frequently as other

14

# Figure 9: Process View of Data Analytics

Source Mularzl and Ulku (2014) Diagram based on the original model of Liberatore and Luo

(2010)

According to the model of Liberatore and Luo, 2010, the analytics process initiates with data

collection, a phase wherein information is gathered. Often, data necessitates certain

adjustments prior to its application in the analysis stage. Typically, data is sourced from

multiple origins, and it necessitates manipulation and arrangement to compile all pertinent and

valuable information necessary for further examination. Although data collection can be time-

intensive, its meticulous execution is vital, as inaccurate, or erroneous data could result in

## incorrect conclusions or complications during the analysis phase

Subsequently, data can be explored and evaluated using interactive tables, charts, and

dashboards. These tools for summarizing and visualizing data allow for the integration of

# multidimensional data and statistical outcomes within a unified graphical interface, which

facilitates the exploration of data from various viewpoints and in diverse formats. The

capabilities and features of these tools are continually advancing in most Business Intelligence

(BI) software. Predictive modeling techniques are utilized to anticipate trends, validate

relationships, and establish classifications based on a set of input data. These methods

encompass numerous statistical techniques (such as logistic and linear regressions, forecasting,

and cluster analysis), operational research (OR) models (including stochastic and simulation

# models), and artificial intelligence (AI) approaches (such as neural networks). Optimization

15

models can also be applied to discover the most optimal solution within a set of predefined

assumptions and constraints. Such models include various mathematical programming models

and AI heuristics, such as genetic algorithms. These approaches collectively enable a

comprehensive analysis of the data, providing valuable insights and facilitating informed

# decision-making.

Also according to the authors, Insights, on their own, possess restricted value unless they are

transformed into actionable steps by management. These actions can encompass enhancements

in operational decisions, reconfiguration of existing processes, and formulation or modification

of strategies. At the operational level, insights have the potential to enhance the quality and

promptness of decisions made by frontline managers.

# 2.3 People Analytics

While the name PA may not imply the business aspect, various authors and researchers have

come to agree that <PA is about the business=. Ferrar and Greenaway (2021) suggest that the

focus of PA is to deliver commercial value to employees and the broader workforce. Such value

should equip managers and executives with evidence-based insights for decision-making

regarding employees and the workforce. In its most effective form, PA extends its impact even

to the highest levels of governance, influencing the board of directors, investors, and society

# as a whole.

# 2.3.1 Definition of People Analytics

<People Analytics= is also referred to as <Human Resource Analytics=, <Workforce Analytics=

# or <Human Capital Analytics=.

According to Khan and Millner (2020) and other authors, there are distinct definitions for each

# of the above-mentioned term:

HR analytics primarily focuses on evaluating the performance of the HR department itself,

including the analysis of key performance indicators (KPIs) such as employee turnover and

time to hire. These analytics are mainly relevant to the HR team.

16

Workforce analytics, on the other hand, has a broader scope and covers the entire workforce,

including the potential inclusion of data related to automation, AI, and robots. Workforce

analytics provides a more comprehensive view for creating a holistic workforce strategy.

PA goes even further by encompassing HR, the entire workforce, and customer insights. It

involves measuring and analyzing all this information and integrating it to enhance decision-

making and overall business performance.

In this master’s thesis, the term <People Analytics= is employed, as it seems to be an emerging

term, and PA does not belong within only HR but rather, these analytics deal with business

# performance such as <sales productivity, retention, accidents, frauds and other people-issue

# that drive customer retention and customer satisfaction= (Bersin, 2015). Among many

definitions for PA, Vihari and Rao (2013) describe PA as <the application of sophisticated data

## mining and business analytics techniques to the field of HR=.

Isson et al. (2016) argue that the field of PA initiates the process by formulating specific talent

management inquiries or objectives. Subsequently, it combines diverse data sources for

generating predictive insights concerning future scenarios. These insights, in turn, serve as a

basis for formulating actionable strategies within organizations, leading to quantifiable

# outcomes.

Dooren (2012) refers to PA as a methodology that is achieved through the application of

statistical methods and experimental approaches, using metrics such as efficiency,

effectiveness, and impact…to comprehend and assess the cause-and-effect connection between

HR practices and organizational performance results. Results can be customer satisfaction,

sales, or profit. It establishes credible foundations for human capital decisions, influencing

# business strategy and performance.

Kapoor and Sherif (2012) define HRA as the process that involves collecting, transforming,

and managing key HR-related data and documents. This information is then analyzed utilizing

business analytics models, and the outcomes of the analysis are communicated to decision-

makers, enabling them to make informed and intelligent decisions.

HRA is believed to be a methodology for developing innovative insights (Smeyers & Delmotte,

2013). Johnson-Murray, Rachael, et al. (2018) refer to PA as a <powerful tool for elevating

the credibility of the HR function=. Heuvel and Bondarouk (2017) argue that HRA is the

17

# systematic identification and quantification of the people drivers of business outcomes, with

the purpose of making better decisions.

# 2.3.2 History of People Analytics

The human capital metrics were put into use in the early twentieth century by mechanical

## engineers and later psychology researchers.

The earliest adoption of data in human resources, as scripted by Isson (2016), was in 1911,

when a mechanical engineer made an experiment to measure workers' productivity and the

industry’s efficiency. In his work, he suggests best practices and guidelines for efficiency.

In 1923 Hugo MÜnsterberg, and in 1945 Elton Mayo employed metrics and measured the

impact of each component on work performance and morale by adjusting and monitoring each

variable. His metrics included working hours, rest breaks, lighting, humidity, and temperature.

Heuvel and Bondarouk (2017) have summarized the evolution of PA analytics from the first

hit of digitalization development to the HR department since 1980 for HR automation and

adoption of HR information systems. In this phase, there were many studies on the maturity

model of HR, the development of the HR framework for automation, and the prerequisite for

adoption. However, the system is predominantly used for payroll and other administrative

purposes. In the 1990s, Organizations began to realize the prospects of utilizing computer

systems in Human resource management. HR department cautiously increased their use of

information systems even though there was research done by academics and practitioners on

other potential applications of IS that could be done in everyday HR practice.

During the 2000s, the Human Resources (HR) field witnessed an expansion in technology

utilization. This era saw the emergence of the term "e-HRM," which refers to electronic Human

Resource Management. During this time, HR departments began harnessing technology for

strategic planning and implementation. This adoption encompassed a range of functions,

including administrative tasks in 62% of companies, employee recruitment in 52%,

# performance management for employees in 52%, and compensation management in 49% of

# companies.

# (Cedar Crestone 2006)

18

As of today, advancements in technology and the implementation of big data analytics have

significantly bolstered Human Resource Management (HRM) by enabling the creation of more

streamlined and data-driven solutions for businesses (van den Heuvel, Bondarouk, 2017). The

process of digitalizing HRM has opened up various opportunities for its enhancement (van den

## Heuvel & Bondarouk, 2016; Dahlbom et al., 2019).

## 2.3.3 Five Stages of People Analytics Development

Human Resources (HR) is not limited to HR operations; it is centered around the business and

plays an important role as a business center, not just a cost center. Similarly, people analytics

transcends not only the measurement of HR activities as visualized in scorecards or dashboards

but also the presentation of intriguing insights or interesting pieces of information. Instead, its

primary purpose is to contribute to achieving tangible outcomes and delivering concrete results

# for the organization.

Ferrar and Green (2021) describe the development of PA by <five ages=: Discovery,

Realization, Innovation, Value and a prediction for the future, which is the age of Excellence

19

## Figure 10: Five Ages of People Analytics (Source: Ferrar & Green 2021)

As mentioned briefly in the previous section about the history of PA, the earliest adoption of

PA was in the year 1911. According to the authors, the Discovery phase lasted for almost a

century, from its earliest adoption until the 2010s (1910s -2000). This phase of development

witnessed two World Wars, and nine global recessions, according to WorldBank., which were

in recession in 1914, 1917-21, 1930-32, 1938, 1945-46, 1975, 1982, 1991, and 2009.

Moreover, other significant events in this phase are the technological development and the

dawn of <mass industrialization= in 1940 (Ferrar & Green 2021), when the HR department

expanded its scope beyond the administration's focus.

In the 1980s and 1990s, there was a transformation in the human resources department. It

shifted from a narrow focus on administration to encompassing recruitment, development,

reward, and performance management. This evolution created a demand for measuring

<processes and the efficiency= with a large amount of data collected via online and offline

# channels.

In addition to reporting, PA functions also create business diagnoses. However, it's important

to note that these diagnoses may not be conducted on a regular basis. (Ferrar and Greenaway,

2021)

20

The phase of Realization (2010-2015) was a post-global financial crisis period (2009), when

the desire to measure and ensure the effectiveness and efficiency of business operations became

a prominent goal ithin various industries. During this period, the value of data also became

increasingly apparent and was often referred to as the "new oil."The growth of PA was aligned

with the emergence of Big Data and the rapid adoption of analytical methods when giant tech

companies pioneered in creating maturity models and new methods to realize and to translate

people's data to understanding for strategic planning and enhancement of competitive

# advantage.

The analytics at this phase varied from reporting and dashboard to very advanced analytics and

could even possibly be integrated with financial indicators to have more <specific, scientific

## and value-oriented insight= from PA. (Ferrar and Greenaway, 2021)

# The phase of Innovation (2015-2020)

The business value PA at this phase was realized and recognized; therefore, advanced analysis

was employed more intensively to improve business performance. This Age of Innovation was

also marked by several key features, including the introduction of novel models, technology

applications, specialization, and a growing pool of professionals entering the field of people

analytics. Ferrar and Greenaway also quote the work from Guenole et al. (2017) regarding the

link between workforce analytics and business performance, which indicates that businesses

start PA from a business problem, not from data. PA is a <core component of people strategy

of business overall.= The authors also emphasize the 2017 report by Corporate Research

# Forum, Strategic Workforce Analytics, which indicates that 69 percent of North American

organizations employing 10,000 or more individuals had established a team dedicated to people

# analytics.

The Age of Value (2020-2025) witnessed a sudden increase in PA technology market volume.

An unprecedented global pandemic began in 2020, which also required PA reports to be set up

and strategies to be figured out while the new working conditions were introduced. Novel

issues arrived in the workplace regarding mental well-being in the context of social distancing,

remote working policy, and the health and wellness of the employees. The authors conclude

that the global situation has elevated the role of people analytics to greater levels of importance,

demanding increased speed and precision in day-to-day operational choices and the

## formulation of long-term strategic scenarios.

21

In the Age of Excellence (2025-2030) the authors expect PA to become an embedded function

## across organizations of all sizes and shapes.

## 2.3.4 The adoption model of People Analytics

As reviewed in the evolution of PA over the recent years, the growing adoption of HR

information systems has facilitated data storage in a centralized location, simplifying the

# information-gathering process.

Nevertheless, data consolidation into one location does not automatically allow it to be ready

for integration into organizational statistical analysis software. There are different dimensions

# in the adoption model of effective PA.

According to Ferrar and Greenaway, an excellent PA model has nine dimensions.

## Figure 11: Nine Dimensions for Excellence in People Analytics Models

# (Source: Ferrar and Green 2021)

# Foundation:

Success in people analytics is determined by a supporting foundation that is built upon the

# pillars of sound governance, well-defined methodologies, and efficient stakeholder

# management.

22

According to the authors, Governance of PA refers to the <mechanisms, processes, and

procedures= that govern the operation of people analytics. It serves as the foundation for all

analytics activities regarding an effective structure and stewardship for data management and

## projects, risk management, and human resource management in the PA team.

The methodology focuses on the processes and frameworks required to ensure the

consistency and adaptability of people analytics. The methodology gives guidance to choose

priorities with clear and transparent criteria. Methodology also agrees on how to develop

strategies for directing the team.

# Stakeholders possibly belong to the various categories of stakeholders with whom people

analytics teams collaborate to make a <meaningful impact and provide value=. Stakeholder

management emphasizes the importance of strategies for engaging with stakeholders in terms

of stakeholder meetings and approaches for building relationships.

# Resources.

Skills delves into the role skills, and responsibilities of the people analytics leader and team

members. The operating model for the analytics team is also highlighted.

Technology. Refer to the choice of technology and how to leverage technology to expand the

reach of analytics solutions and harness emerging technologies in data collection, analysis,

## generation of insights, and access to data.

Data discusses data stewardship, data management, and strategies for extracting value from

data. This pillar includes a particular emphasis on leveraging various data sources, including

emerging data, to enhance people analytics beyond the realm of human resources processes,

addressing more multifaceted business challenges.

# Value

The core value of people analytics is to be delivered to the organization regarding business

performance and organizational data analytics culture and to its employees regarding their

working lives.

Workforce Experience refers to employees as a pillar for a successful PA. The role of PA as

a value-creator for workforce experience is as essential as it is to the organization.

Business Outcome This typically refers to the organization’s financial performance and

other tangible outcomes, which were realized as a result of PA implementation

23

Culture. This pillar focuses on fostering a culture within the HR function that encourages and

empowers professionals to embrace analytics.

# 2.3.5 Adoption Framework of PA

PA should start with a business problem (Isson et al., Fit-Enz et al., Ferrar and Greenaway,

Edwards &Edwards). Isson et al. (2016) explain the <migration= from Business Analytics to

People Analytics as a <switch= from the research subject for the same analysis from <customer=

to <talent= while making efforts to answer three questions and find solutions:

- 1. What happened?

- 2. What is happening and why?

- 3. What will happen?

The authors also recommend focusing on the IMPACT framework for adopting People

## analytics at any stage of talent management.

# Identify questions

At this first step, it is pivotal to have a clear focus on the business problems to raise the

efficiency of the workforce. However, the question should be raised in a <nonintrusive way=

as the human resource information may negatively affect the workers.

# Master the data.

This involves a process data management phase, which includes data acquisition, determination

of the type of data needed to achieve analysis objectives, extraction, cleaning, and

aggregation... Consider the sources of data, its quality, and the relevant variables or attributes

that need to be collected. Identify the sources of data that can fulfill data analytics requirements.

Provide the meaning.

This process involves visualizing and interpreting data to address business inquiries. It includes

analyzing the results and connecting them to the initial objectives. It entails recognizing

patterns, detecting trends, and identifying relationships within the data, which can yield

## valuable insights and guide decision-making.

24

# Act on the findings and recommendations.

After finding evidence, recommendations and suggestions should be made. Identify the most

critical and actionable insights from data analysis and focus on those that align with business

objectives and have the potential to drive significant impact or improvements.

Communication insights: A multifaceted communication strategy that disseminates insights

throughout the organization should be employed.

Track the outcomes: follow up and track the outcome of actions, which have been done

according to analysis’s insights

25

## Figure 12: IMPACT model (Source: Isson et al. (2016))

Pease et al. (2014) propose a People Analytics blueprint to develop a measurement plan, step

# by step:

- Purpose: identify the purpose of the analytics project

- Questions to be answered.

- Data sources

- Data collection method

- Timing

- Stakeholders

- Reporting requirements

# Implementation and considerations

The Isson’s IMPACT model and Pease’s Blueprint suggest similar steps to achieve success in

People analytics, create a strong data foundation and encourage a culture of data-driven

decision-making within the business. These two models also create frameworks to promote the

use of data and analytics across HR teams and businesses as a whole to inform decision-

making, drive innovation, and continuously improve performance. However, while the

IMPACT model focuses on communicating and measuring the impacts of the analysis, the

blueprints give a guideline on the development plan of the analysis itself.

26

# 2.3.5 The value of Data Analytics

## 2.3.5.1 Business value of People analytics from ROI based-view

Ben-Gal (2018)in her Return On Investment-based review of PA, describes an increasing

amount of research papers on the topics, in addition, the topic also acquires more attention in

practice and emerges in business and management journals. The author describes four PA

research approaches, which include empirical research, conceptual, case-based, and technical

research. According to Ben-Gal, this indicates PA has enhanced its presence in business

research. The research reveals four significant trends of PA research categorized by its impacts

# on ROI:

- PA as a strategic management tool

- Evidence-based approach in PA

- PA as a decision-making support tool

- Future of PA as management fad

As a management tool, PA is proven to have a positive impact on organizational development

and yields a high ROI for the organization. More specifically, when instilled in the management

process, analytics accommodates the strategy-making with measurement, metrics, and

prediction. The author highlights the prediction of turnover rates as a notable example of PAl

## outcomes with substantial implications for long-term business effects.

The evidence-based approach also proves that PA has a high ROI for the organization. PA,

with its methods and techniques, is a powerful tool for management to understand their

employees at the individual level, as well as the whole organizational performance. The

evidence-based approach also seeks advice on tools and analytical methods for each specific

# HR problem.

Regarding the supporting function of PA, research shows the impact of PA on the efficiency

and effectiveness of the organizational decision-making process. The ROI from this aspect of

PA is high.

The last trend is that PA as a management fad in the future will yield low ROI. According to

the author, this is due to the fact of its <speculative in nature=. There are debates about

integrating HR analytics into the HR function and determining the roles of HR professionals,

as discussed by Rasmussen and Ulrich (2015).

27

# 2.3.5.2 The value of PA

Analytics is often said to be a process that unveils hidden and strategic value for business.

According to Marler and Boudreau as cited by Peeters et al. (2020), PA or <Talent analytics,=

<Human resource Analytics= is an HR practice empowered by technology development,

employing statistical and visualization techniques to analyze <HR process, human capital,

organizational performance, and external economic benchmarks=. Isson et al. describe PA as

the <integration of disparate data sources= such as employee data, organization data, and data

from the labor market. While data analytics is conducted for making evidence-based day-to-

day decision-making and strategic decisions, the PA focuses on answering essential questions

# about <acquisition, retention, placement, promotion, compensation and workforce and

succession planning < (Walford-Wright & Scott-Jackson, 2018) in a proven, more accurate and

insightful manner and help the HR depart avoid making decisions using experience and gut-

feeling and guesswork (King, 2016). Dooren 2012 defines PA as: <a methodology for

understanding and evaluating the causal relationship between HR practices and organizational

performance outcomes (such as customer satisfaction, sales or profit), and for providing

legitimate and reliable foundations for human capital decisions for the purpose of influencing

the business strategy and performance, by applying statistical techniques and experimental

approaches based on metrics of efficiency, effectiveness and impact=.

Pease (2015), in his book, quoted a research result by Deloitte, which indicates organizations

which employ Human resource analytics are <doubling their improvements in recruiting,

tripling their leadership development capabilities, and enjoying 30 percent higher stock prices.=

Pease (2015) also concludes the primary PA by surveying 114 organizations that employ PA

at the mid-maturity level… Most organizations (88%) agree that PA gives them the power of

data-driven decision-making. More than three-fourths of organizations believe PA gives them

the ability to improve their business performance. Lastly, over 70% conclude that PA enables

## improvement in their current programs and processes.

28

# Figure 13: Analytics Achievement

# Source: Sierra-Cedar (2019)

In their white paper, Sierra-Cedar (2019) summarized the perspectives of 1892 respondent

organizations regarding their attitudes toward the use of PA. More than half of respondents

agreed that the cost management factor was achieved by employing PA.

Specifically, recruiting costs, workforce alternates, and the cost of hiring may expand, and

the company's strategy may be reshaped. According to Walford-Wright and Scott-Jackson

(2018), talent acquisition is challenging. These challenges include a lack of strategy or a clear

vision; absence of technology, for example, an application tracking system or lack of other

automation processes, which leads to lengthy time to hire; reliance on external agencies: no

# referral program, high cost per hire; other recruiting process and talent management

challenges lead to low quality of hire, low engagement of human resource; weak relationships

with hiring managers and internal applicants, and a lack of key performance indicators (KPI)

or individual development plans (IDP) for the talent acquisition team. Notably, the absence

of PA is, according to the author, one of the organization's core strategies. These factors can

impact the company's financial resources and necessitate reevaluating its recruitment

# approach and organizational strategies.

Besides a clear vision and outsourcing cost, there needs to be other technology used in the

selection process to ensure talent acquisition optimization. The PA can be used <as a

29

predictive tool.= At the same time, it builds a <template= for future hires and <see the

candidate three-dimensionally,= a <democratic, impartial= and decision support to achieve the

# best candidate.

2.4 Skill sets of HR specialist in order to perform PA

Discussing skills for PA, Johnson-Murray et al. (2018) postulate that there are three

fundamental knowledge domains that a Human Resources (HR) expert should possess to

implement People Analytics (PA) effectively, which are People skill, Business knowledge and

# Data Skill.

By People skill, the authors refer to the organization’s workforce, their psychology, and their

motivation to work. The people knowledge domain also requires knowledge about how to use

power and influence to <secure buy-in and communicate=

Business knowledge: as concluded by different authors, the ultimate goal of PA is to enhance

an organization’s performance outcome, the PA should have a a comprehensive view of the

business process and understanding of organizational competitive advantages’s origin. Since

the analysis begins with the business problem, business domain knowledge is undoubtedly a

# must-have.

Knowledge about data includes two different expertises: data expertise and analytics expertise.

Data expertise is not just about working with data itself from the very first raw form to ready-

to-use format, it is also required to gather, extract, clean data, and manage a database system.

On the other hand, analytics expertise enables analysts to mine the data for an actionable and

# comprehensive data story.

Ferrar and Green (2021) quoted six skills for an excellent data analytics team in their work,

## which originates from Guenole, N, Ferrar, J and Feinzig, S (2017):

30

## Figure 14:Six elements of an excellent People Analytics Expert

(Source: Excellence in People Analytics: How to Use Workforce Data to Create Business

# Value (Ferrar. And. Green 2021))

In the scope of this thesis, Data Science element form Six Skills for Success is discussed.

According to the table, to successfully leverage workforce data, various skills are required: the

data science element indicates expertise in data engineering while the communication skill

refers to data analytics. Data science includes a wide range of advanced mathematics: statistics

and modeling, data management expertise to work with databases, programming knowledge,

data modeling, and machine learning. Communication skills are also broad, which include

analyzing and visualizing data to figure out actionable insight. Communicating of findings in

a narrative that influences business strategy decisions is also a part of this element.

## 2.5 Analytics skills of HR Department in current landscape

Ferrar and Greenaway (2021) argue that the significance of PA as a field is rapidly increasing

not only within the HR department x§ across the broader business functions. There are

increasing numbers of individuals equipped with existing analytical skills and deepening their

analytical skills in working in HR. Senior leaders are becoming increasingly aware of the

31

imperative for a data-driven approach within their HR operations. Human resources executives

who dedicate resources to people analytics are on their ways to discover innovative avenues to

enhance their companies' competitive edge in the marketplace.

However, Edwards and Edwards (2016) point out that <the majority of HR functions do not

have the core capabilities to carry out predictive analytics activities=, which is an advanced

analytics. In addition, the authors specify that there is a lack of training and education for HR

specialists in terms of statistical and numerical knowledge. These skills are considered non-

compulsory, and the HR function is a <safe haven= from numbers. The author argues that,

within the context of the United Kingdom’s Chartered Institute of Personnel and Development

syllabus, exist a deficiency in designated areas to develop HR student qualifications in

# numerics and statistics.

In the same year, a Harvard Business Review study also revealed that 47% of surveyed

companies suggest that lack of expertise in analytics acumen is one of the biggest hindrances

to PA. HR professionals should acquire the ability to identify the employee metrics that exert

the most influence on business outcomes. Additionally, they should possess the skill to

construct stories that explain the implications of these numbers for the business. The report

also highlights a requirement for an effective solution offered by PA analytics, which is the

self-financing ability of this solution.A self-financing ability means that the savings generated

from the implementation of the PA solution should exceed the cost of implementing the

# solution.

Caughlin (2022) states that there is a lack of emphasis on HR students’ data literacy skills,

## which results in a <shortage of HR analytics talents=.

Harris et al. (2011) postulate that <success with human capital analytics will depend, in large

part, on HR’s ability to find and nurture analytical talent – the people who produce the data,

the quantitative analysis, and statistical models you need to make better decisions and achieve

# better results=.

32

## Figure 15: People Data Analyst skills (Source: Pease (2015))

An interview by Pease (2015, page 90) also reveals the top three barriers to PA success which

reflect the importance of Data infrastructure and skills of the HR. 65% of interviewees agree

Data Collection is a hindrance to their PA. This is also the biggest hindrance reported.

Secondly, 59% of respondents’ organizations stated Data Integration as their hindrance. The

third primary challenge of PA to organizations reported is a lack of data skills, which was

reported by 53%

## 2.6 Business Analytics to People Analytics

Isson et al. (2016) highlight the reliance on creativity, instinct, and the experience of marketing

professionals rather than data-driven decision-making. However, as competition grew, the

marketing industry underwent a significant transformation by integrating analytics into its

operations. This shift aimed to make marketing a more strategic and accountable business

# function.

The adoption of analytics in marketing was driven by the desire to strategically attract, segment,

acquire, grow, retain, and reward customers. Marketing recognized the importance of

understanding its customer base, target demographics, and the entire customer life cycle. This

led to the birth of marketing analytics. Organizations combine marketing with marketing

analytics, striking similararities between Business Analytics and People Analytics when

examining the transition from one to the other. Likewise, the authors propose a shift from (1)

33

Analytics in Marketing to Analytics in Talent Management. (2) Customer Life Cycle

Management to Talent Life Cycle Management. (3)Customer Relationship Management to

Talent Relationship Management. (4)Customer 360-Degree Analysis to Talent 360-Degree

# Analysis and Understanding.

This transition signifies a broader application of analytical approaches from customer-centric

areas to areas focused on managing and optimizing organizational talent.

The authors also brief the history of marketing analytics, which is in a similar narrative: prior

to the 1990s, marketing relied heavily on the balance between art (experience, judgment, and

## instinct) and science (data intelligence)=.

This transformation in marketing can be showcased as an adoption model to the HR department

in incorporating People Analytics programs to proactively embrace the analytics and make

## more informed decisions in human resources and talent management.

# 2.7 People Analytics Maturity model

In the field of Human resource analytics, Bersin (Bersin, 2012,page 44) suggests a maturity

# model.

Moreover, he postulates four levels of talent analytics. According to his suggestions, they are

operational reporting, advanced reporting, strategic analytics, and predictive analytics.

Predictive analytics is considered to be the most advanced level of People Analytics.

34

Figure 16: People Analytics Maturity Model (Source Bersin, Deloitte Consulting 2018 (Murray et al., 2018, page 40))

Murray et al. quoted the maturity model of People Analytics in practice. The authors explain

# each level

Level 1 - Operational Reporting: As a groundwork level for data analysis,

organizations with this maturity level use data and metrics primarily to understand past

events and possibly the reasons behind them. The focus is on comprehending the

available data and gaining consensus on its interpretation.

Level 2 - Advanced Reporting: advanced reporting means to be more <proactive or

routine= by employing automated reporting systems and data visualization dashboards.

Relationships among variables are also explored and analyzed.

Level 3 - Strategic Analytics: Organizations at this level move beyond understanding

past events and relationships to developing causal models, root cause identification, and

determining the impact on business outcomes. An example of this analysis is

identifying the drivers of turnover or employee engagement.

Level 4 - Predictive Analytics: The highest level involves forecasting future events,

trends, or outcomes and using those predictions for business planning. An instance from

Murray et al. (2018) is to utilize data on turnover, promotions, and market trends to

create scenarios that inform workforce planning.

35

## 2.8 Predictive analysis for organization performance

Several research studies have discovered that companies possessing advanced capabilities in

people analytics generally exhibit superior performance in various financial indicators. These

improvements encompass a 30% increase in stock prices over a three-year span (Bersin by

Deloitte, 2013), a 79% rise in return on equity (Sierra-Cedar, 2014), a 96% surge in revenues

over a three-year period (Chakrabarti, 2017), and a 56% augmentation in profit margins

(Martin, 2018) when compared to their counterparts.

According to the U.S . Department of Labor, a replacement costs 41% of an employee's annual

salary. The result of research by Kostman and Schiemann reveals that a manufacturing

company with 11,526 employees can save $18.8 million just by cutting the turnover rate from

17.8% to 6.8%.

2.9 What data have been used

PA employs three types of data (Isson et al., 2016, page 59):

Talent data: which refers to data of the HR department and organization as a whole, and the

employee themselves. The organization’s and HR department’s talent data are cost for

# recruiting, employee turnover, compensation and reward policy, etc., and organizational

structure and strategy. Talent data of an individual are their productivity, other employee’s

compensation and benefit, their work efficiency, engagement and work alignment, networking,

# job satisfaction, and so on.

# Company data: refers to financial revenue, business performance, and target acquisition, etc.

Labor market data: public data about the labor pool, such as unemployment rate and other

# macroeconomic indexes e.g, Gross Domestic Product, inflation rate, and average salary...

Labor market data can also be acquired from job advertisements and job openings in the

# industry

36

## Figure 17: From Business Question to People Analytics

# Source: Isson et al., 2016

Edwards and Edwards (2016) summarized PA data sources, including: HR database, Employee

# attitude survey data, Customer satisfaction survey data, Sales performance data, and

# Operational performance data

HR database (such as SAP or Oracle) which are software platforms that store and manage

employee data. These platforms are repositories containing various information, ranging from

# personal details

# to employment history, personal

information, employment history,

performance metrics, and more. In their example, Edwards and Edwards (2016) provided a list

of data points that an HR database typically furnishes for the purpose of People Analytics (PA).

These data points include Age, gender, education level, role, salary, performance ratings,

disabilities, tenure, sickness absence, and leaver information…

Employee attitude survey data: In practice, employee attitude survey data is usually stored

in survey programs and exported to Excel after being collected from employee feedback

through surveys and feedback mechanisms. These surveys and questionnaires could be

designated as five-point scale questions, True/False questions. Employee attitude data provides

valuable insights into employee engagement and other metrics such as of job satisfaction and

37

understanding of how employees fit into organizational culture.

Caughlin (2021) argues that the quality of data acquired from an employee survey is influenced

by several crucial factors, including its content, its relevance and appropriateness, respondent’s

understanding and their motivation and engagement

Survey Design and Content, which refers to the formulation of survey questions. Questions

should be clear, concise, and unbiased to ensure accurate responses. Ambiguity or leading

questions can distort the data.

The relevance and Appropriateness of questions to the organization and the specific aspects it

aims to measure. It should also be appropriate for the target population. Questions that do not

apply to certain employees or aspects of their job might lead to confusion and inaccurate

# responses.

Respondents' Understanding: Even well-written questions might not be effective if employees

do not understand them as intended. Piloting the survey with a small sample group can help

identify potential problems with wording or question structure.

Motivation and Engagement: The motivation of employees to participate in the survey can

significantly impact the quality of responses. If employees do not see the value in the survey

or feel it won't lead to any meaningful changes, they might not put in their best effort while

responding. Clear communication about the purpose of the survey and its potential impact can

# boost motivation.

Customer satisfaction survey data: Likewise, customer satisfaction survey data is often

stored in survey programs and exported to Excel. Customer satisfaction survey data is feedback

and evaluations from customer ratings regarding the performance of customer-facing

employees. Not surprisingly, customer feedback is also part of PA, as it offers valuable insights

into customer preferences, but when linked with employee profiles and operational data,

companies can recognize the influence of employee skills and behaviors on the overall

# customer experience.

The customer satisfaction survey data design should also follow crucial factors mentioned

# above, as the influence of design, content, relevance, appropriateness, and respondents'

understanding and motivation have significant impacts on the quality of data.

Sales performance data. As the ultimate purpose of PA is to drive commercial value, sales

performance is one of the key indicators of employees, who are members of the sales force.

38

Sales performance data reveals factors that foster sales performance and hinder the revenue

stream. This data may include periodic sale value generated from existing or new customers to

evaluate team or personal performance.

Operational performance data: information or metrics that gauge the effective and efficient

functioning. This typically pertains to the organization's efficiency in various operational

aspects. An example of this data is processing time for customer orders or, the duration of a

## customer call or other surveillance and monitoring.

## 2.10 Data Acquisition and HR IT Infrastructure

# 2.10.1 Current State

According to HR Business Review by Harward (2016) concerning different aspects of current

PA practice, 54% of HR expert respondents consider data quality to be the biggest hindrance

of PA, which is also ranked as the most significant barrier. 44% of respondents shared the view

that investment in analytical systems among companies needs to be more adequately invested.

McCartney and Fu (2021) raise questions about data quality after conducting a systematic

literature review on recent PA peer-reviewed articles. They also conclude that data quality is

one of the significant barriers to organizations conducting PA as low-quality or accurate data

results in unreliable insight and suggestions, which causes financial loss and consequences to

business performance. In other words, the accuracy and reliability of analytical results depend

on the quality of the input data. Ensuring accurate and high-quality data inputs is essential to

obtain meaningful and trustworthy insights from analytical processes. Nevertheless, numerous

organizations continue to face challenges when it comes to having trust and confidence in their

Human Resources (HR) and people-related data. McCartney and Fu also quoted a report by

Deloitte (2017), which studies over 10,000 business and HR leaders; merely 8% of surveyed

HR leaders indicated confidence in their ability to utilize the data available to them effectively.

As discussed in the previous chapter, People Analytics (PA) necessitates data of varying types

and formats. This data must be collected from diverse sources and systems spanning multiple

business functions, making HR data <vast, messy, and constantly changing= (McCartney & Fu,

39

2021). Therefore, the very first stage of PA: Data collection, faces challenges while requiring

skills to collect and manipulate data.

Not only data quality, data management, and governance are issues for PA. McCartney and Fu

quoted the work of Minbaeva (2018), <Most firms do not know what types of data are already

available to them or in what form. In fact, most firms do not have the answers to some basic

questions: What data do we have? Where do we store it? How was the data collected?=.

Consequently, this leads to an inadequate volume of data required for the successful

implementation of PA, as Fernandez and Gallardo-Gallardo (2020) claim that <there may be

insufficient data to be able to <ask the right questions.=

# 2.10.2 Infrastructure as enabler

With the expansion of the people analytics domain, the people analytics technology market has

been rising as a new sector. A study by Garr and Mehrotra (2020) reveals a double-digit growth

# of the people analytics technology market during the unfavorable economic circumstances

brought about by the pandemic in 2019 and 2020, at 35%. The HR technology has fostered the

development and implementation of PA. It responds to market needs and makes more solutions

available while organizations invest in PA technology (McCartney & Fu, 2021).

HRIS enables the HR department to to gather, extract, and analyze substantial volumes of data.

Beyond data handling, HRIS equips HR professionals with enhanced workforce

comprehension by facilitating the creation of interactive dashboards and scorecards. These

visual tools spotlight vital workforce metrics across various domains, including compensation,

## employee engagement, performance, diversity and inclusion, and talent management

# (McCartney & Fu, 2021).

Ferrar and Greenaway (2021) conclude that <Technology is an important dimension of PA=

and introduced three waves of PA technology.

40

## Figure 18: Waves of People Analytics Technology

## (Source: Ferrar and Greenaway, generated from Ferrar, Styr and Ktena (2020)

The first wave, <Core HR.= Technology in the first wave is Cloud-based core HR systems,

which are <SaaS (or Software as a Service). An approach to software licensing and delivery in

which software is hosted remotely in the cloud and accessed via an internet browser=. The shift

for this first wave, estimated by Ferrar and Greenaway (2021), took place during the twenty-

first century's first decade and continued until 2015 and provided a basic data needs for people

regarding data and analytics. However, these technologies are considered to be <insufficient=

because professionals working with these core HR platforms face various challenges

concerning the platform's functioning. The main obstacles are the lack of data models, the

ability to incorporate external data, and the lack of predictive analytics capability. These

obstacles restrict insights and hamper the capacity to provide actionable recommendations.

They also caused a struggle to integrate specialized data from emerging platforms, limiting the

ability to address complex business topics solely through core HR systems.

The adoption rate of this cloud-based HR technology at the end of 2020 was 83% out of 60%

# of global organizations.

The second wave is called the "Analytics Dashboard", which occurred from the beginning of

the 2010s to the beginning of 2020. During this period, People Analytics dashboards were

integrated into HR systems, enabling the creation of visualizations and dashboards based on

data generated within those specific systems. The advancement of technology has accelerated

the decision-making process of business. Data from different departments are integrated from

various sources, which enhances the quality of data analytics and provides better insight. This

approach not only improves data quality but also leads to significant time and cost savings by

eliminating manual data integration processes. It facilitates a more streamlined and efficient

data analysis process, ultimately benefiting the organization's decision-making and operational

41

efficiency. However, a crucial limitation persisted - the inability to aggregate data from diverse

# sources beyond their own system.

In terms of budget allocation, expenditures on HR technology were considered as "additive"

and typically recorded under the HR department's budget. Consequently, the value of HR

analytics remained primarily associated with HR functions, and the broader business benefits

of People Analytics still needed to be fully acknowledged and recognized. There was still a

skill gap in the HR department regarding the ability of HR professionals to employ and utilize

the PA technology effectively. According to Ferrar and Greenaway (2021), the lack of analytics

culture failed to drive PA technology across organizations.

65% of global organizations adopted this second wave and reported their positive change in

PA.

The authors refer to the Third Wave as <specialist people analytics technology.= This wave

started at the beginning of the 2020s and is the current trend.

By 2020, 37% of businesses will employ more advanced and specialist PA technology to

conduct analyses such as <talent market intelligence, behavioral skills, relationships,

productivity and organizational network analysis, employee engagement and listening,

# employee text analytics= and so on.

The forthcoming third wave of analytics is anticipated to fulfill all expectations, empowering

businesses to harness advanced and predictive analytics capabilities. As McCartney and Fu

(2021, page 5) quoted from Angrave et al. (2016) suggest: <Rather than providing strategic

and predictive analytics that allow organizations to ask and answer big questions about how

value can be created, captured and leveraged, HRIS typically provide answers to a more limited

set of questions focused on operational reporting [...] the costly analytics capabilities provided

by the latest forms of HRIS are failing to deliver strategic HR analytics capabilities=.

King (2016, page 491) suggests that <the ability for analytics to be applied in a meaningful way

has been hindered, not helped, by the growing HR analytics industry, which is often built upon

products and services that fail to meet the needs of HR professionals and organizations=.

42

# 2.11 People analytics Scope of analysis:

Pease (2015, page 44) suggests a People Analytics analytics continuum from the most basic to

# the most advanced one:

- Anecdotes

- Scorecards and Dashboards

- Benchmarks

- Correlation

# Isolation and causation

- Predictive analysis

- Optimization

## Figure 19: People Analytics Continuum (Source: Pease (2015))

# Among those anecdotes, scorecards and dashboards, benchmarks, correlation, isolation, and

causation are parts of descriptive analysis. Pease states that anecdote is the ground level of the

PA analytics continuum. At this level, organizations collect their employee’s stories and

43

opinions concerning various organizational matters. One method of collecting anecdotal

evidence is employee interviews after a company’s training program.

Scorecards are a tracking tool of employee performance and alignment to an organization’s

strategies by displaying chosen HR metrics and indicators measuring business processes.

Scorecards are made using more advanced techniques and technology or even can be

automated. Dashboards which in the same category share similarities but differ in terms of

technology use and duration of use. Dashboards are for shorter term projects, even ad-hoc and

employ basic analytics tools. In earlier work, Pease et al. (2013) defined Dashboards as a way

to offer a quick overview of essential performance metrics (such as those related to sales,

marketing, human resources, or production) pertaining to a specific goal or business process.

A dashboard serves as an indicator of whether everything is operating smoothly or if there are

any issues that need attention

Benchmark, which became popular in the 1980s, takes leading companies in the field as the

standards and studies the gaps. Salary, and turnover rate are among the indicators in benchmark

reports. Benchmarks had been used as a <standard tool= however, the author Pease (2015)

# considers it an overestimated method.

Correlation reveals the relationship between elements displayed in more advanced dashboards.

The author emphasizes the difference between correlation and causation, which is a higher

# analysis stage.

Predictive analysis is defined by Pease (2015) as a prediction for the future in case a change is

made. Optimization is <assessing and measuring the different factors that control and mediate

impact is that you can use them to control future impact and improve outcomes.= Pease et al.

(2014) claim that optimization can be done through predictive analysis.

# 2.12 People Analytics framework:

# Predictive People Analytics

Edwards and Edwards (2016) define Predictive People analytics as the employment of

advanced statistical and quantitative analysis methods to the Human resource related data

within organizations to predict, for example, factors contributing to high performance or factors

44

leading to employee attrition or to make concrete forecasts about specific results or

# consequences (e.g., employee or organizational behavior) under specific circumstances.

Isson et al. (2016, page 79) postulated seven most important stages of PA, which is termed

<seven pillars= which business leaders should employ to boost their performance and optimize

# their workforce

- 1. Workforce planning

The workforce planning analytics is an approach to addressing key questions to set up the plan

for the human resource, regarding strategic plan (industry trends, re-organization, scaling of

the human resource, restructuring the human resource of the company, turnover rates,

# retirement rate) and financial planning and talent management, in term of identify

## characteristic, skills and other qualification. In

This predictive people analytics may provide valuable insights into workforce planning since

the organization achieves the effectiveness of analytics, which demands on the quality and

accuracy of the data being analyzed. Ethical considerations and data privacy should also be

prioritized when implementing predictive people analytics to ensure fair and responsible use

# of employee data.

There are six major categories of data for workforce planning:

- Talent data

- Market data

- Business data

- Economic and industry data

- Labor statistics data

- University and graduation data.

The turnover analysis, according to Isson et al. (2016, page 110) should address the causal

# relationship between different factors to both voluntary turnover and involuntary turnover.

Involuntary turnover should also be understood by the breakdown of demographic attributes

and performance metrics; in addition, this analysis should also be performed by other

## macroeconomic factors and market competition.

45

At the more advanced level, the workforce planning analysis investigates thorough labor

market supply/demand trends, makes comparisons with the existing labour profile of the

organization for gap analyses and forecast future needs and trends. The predictive analysis,

therefore, provides organization with a labour deficit and surplus anticipation.

- 2. Talent sourcing analytics

Talent sourcing is defined by Isson et al. (2016) as the <first stage of the talent acquisition

process=. It involves the process of recognizing and locating potential candidates via various

recruiting channels. Among a diverse range of sourcing channels online (social media, big data

sourcing, niche sites, corporate sites, job board) and offline channels (recruiting at targeting

# education institutions, employee referral programs and internal candidate, print and billboard

or recruiting agencies). The authors highlight the need to capture the digitalization movement

of talent recruitment and the introduction of new generations and new skill sets to the labour

market. Talent sourcing analytics seeks to provide a comprehensive job seeker decision

journey, which reminds of the Customer decision-making journey and the urge to have insight

## into the workforce to the same degree as insights of their customers.

Job seeker decision journey consists of four phases:

Stages 1: Initial. The report at this phase reveals the motivation and triggers behind candidates'

# job-seeking activity.

Stage 2: Active Consideration, Evaluation, or Knowledge. The analysis identifies the active

or frequent points of contact for the job seekers while approaching the organization.

Stage 3: Action. The analysis of this stage describes various phases of the application process

from the considering applying moment to the acceptance of a job offer.

Stage 4. Post hired. At this stage, the employee’s engagement and commitment are addressed

and analyzed. This is also a measurement of how emotionally invested and dedicated

employees are to the jobs and the organization.

46

# Figure 20: Job seeker’s journey

- 3. Acquisition/hiring

The talent acquisition analytics emphasize the four stages of recruiting

- Application.

- Preselection.

- Interviews.

- Selection.

The talent acquisition analytics quantify the selection process’s metrics in terms of quantity of

applicant numbers and interview rounds. In addition, the analytics also address other qualitative

indicators such as interview question type, relevancy of candidate resumes and relevancy of

education and work background. The predictive analysis of talent acquisition is reported to be

employed by 67% of interviewed companies (Isson et al. ,2016), which has impacts on their

recruiting process.

- 4. Onboarding, culture fit, and engagement

Onboarding, culture fit, and engagement analytics are designed for standardized and well-

structured experience onboarding programs. Insights from data are a guideline for each stage

47

of onboarding and identifying the critical elements for each specific program to enhance its

overall effectiveness. Furthermore, the application of analytics can provide insights into the

progress of each new employee within the onboarding process and predict which aspects of the

program are indicative of future employee success.

This analysis does not just only measure the perceptions and activities of new hires during the

onboarding process, it is essential also to establish analytical connections between onboarding

programs and specific outcomes, identify predictive indicators of whether a new employee will

achieve long-term success within organization, which depends as well on the organization

## objective and the roles of each new hires

- 5. Talent Engagement Analytics

Analytics play a crucial role in comprehending the various factors that impacts on employee

engagement, leading to a workforce that is more satisfied and more productive while

concurrently reducing unplanned turnover. Furthermore, analytics provide human capital

management teams with the tools to analyze and interpret talent-related data and information.

Data collected for employee engagement analytics are typically from Employee surveys, which

focus on drivers of employee engagement. Employee engagement survey data, when combined

with onboarding and exit survey data, recruitment data, various HR datasets, learning and

# management information, customer survey data, and even macroeconomic or industry-specific

data, can collectively form a comprehensive analytical dataset.

With this rich dataset in hand, organizations can leverage analytics to make predictions related

to various critical outcomes, such as employee performance, turnover rates, the quality of new

hires, and other relevant metrics. This data-driven approach enables organizations to anticipate

trends, identify areas for improvement, and implement targeted strategies to optimize their

## workforce management and business performance.

Regarding employee retention analysis, the authors suggest this can be done by employing

# performance and engagement metrics

## 6.Performance assessment and development and employee lifetime value

As the biggest asset for organizations, Human Resources is also considered as the <source of

innovation=. The dedication and enthusiasm of the people grant organizations a competitive

edge. To fully unlock this potential value, organizations must take proactive steps to harmonize

48

# their workforce's personal goals, strengths, and passions with the organization's immediate and

# long-term goals.

Performance management emerges to facilitate the harmony of individual and team objectives

with those of the organization. Through effective performance management, organizations can

harness the full value of each individual and team by ongoing monitoring and adjustments as

organizational goals evolve and individual circumstances change.

# 7.Employee wellness, health, and safety

Isson et al. (2016) postulate , in practice, companies that integrate workplace wellness and

health programs into their talent management life cycle have recognized the value. Big Data

analytics are used to showcase the effectiveness regarding financial terms, which is return on

investment (ROI) , and to optimize companies’ talent management programs. The authors also

state companies under study have proven the causal relationship through the use of data

analytics to evaluate the impact of their wellness programs. Their data-driven insights provide

compelling evidence of the positive relationship between workplace wellness, employee

## productivity, and the overall financial performance of their company.

The employee’s health profile of the company may be built. Employee health and safety , for

instance, in the mining industry, can be predicted by optimizing predictive models for issues

concerning which employee is more prone to accidents. Where accidents possibly happen, and

which equipment is more likely to cause incidents?

# Different HR analysis:

David E. Caughlin (2022), in his work, suggests seven applications for HR analytics

- 1. Employee Demographic

- 2. Employee Surveys

- 3. Employee Training

49

- 4. Employee selection

- 5. Employee separation and retention

- 6. Employee performance management

- 7. Employee compensation and rewards

# Employee Demographic:

Employee Demographic deals with employee’s demographic information, e.g, gender, age,

year of experience, department, education background. Although demographic variable when

being put into analysis with a variety of other variables can be leveraged for more advanced

analysis, for example, employee segmentation; Employee Demographic analysis is more about

describing the workforce population, employing descriptive aggregation methods for ordinal

and nominal, interval and ratio variables, such as sum, average, min, max, and center tendency

## (mean, media, mode) and dispersion, frequency (count).

With reference to Isson et al (2016), this employee demographic is a vital step to understand

the human resource of the organization and build a competency profile. The authors suggest

demographic information should include:

# Job title

# Job category

# Job level

# Job status

- Quantity required

- Quality of hire

- Diversity

- Financial implication, cost per hire, compensation and benefit

# Employee Surveys

Employee Surveys are a typical data source to understand employee’s feeling, attitude,

engagement… The response can be in Likert-type data, which is on a one to five scale or in

# text form with open-ended questions.

To analyze employee surveys, Caughlin (2022) employs aggregating and segmenting, meaning

aggregation results (mean, median, mode, frequency, min, max…) to describe a specific

50

cluster. A cluster can be a team, a department, or a working unit. This process can also be

referred to as segmentation.

The author also utilizes Cronbach’s alpha to estimate Internal Consistency Reliability, which

<tells us how consistent scores on different items (e.g., questions) are to one another=. Also

based on Cronbach’s alpha, the analysis goes further by calculating to eliminate and introduce

a new variable, which is a composite from several other variables to <measure the different

## sub-facets of the conceptual performance domain=.

# Employee Training:

Employee training aims to enhance employee performance to reach business goals by helping.

Reviewing and evaluating training programs gives organizations ideas about the impact and

effectiveness of training on employees. The author introduces three tests for pre and post-

training performance: with the control group, without the control group, and between two

# comparison groups.

# Employee Selection:

Employee selection refers to the recruitment process for the best fit of the position and

organization. Selection is done by interviews, personality tests, cognitive ability tests, work

samples or simulations, application blanks, or recommendations. The author introduces various

linear regression method, which is predictive method to conduct employee selection.

# Employee separation and retention:

Retention of talents is one of the critical strategic plans of the organization HR’s division. The

author introduces analysis to estimate the correlation and causation between elements and

logistic regression to estimate the turnover rate. Turn over rate is generally classified into two

groups: voluntary and involuntary. An effective employee separation and retention analysis

reveals insights into reasons for leaving regarding recruitment from other organizations,

following employee's career after leaving the organization, employee’s performance, and other

demographic indicators. The predictive analysis also identifies employees with a high chance

of leaving their current position to pursue a career change.

51

# Employee Performance Management

The performance management includes various stages, from developing, managing, and

evaluating employee performance. It is an <on going process of assessment and feedback=. The

analysis includes various linear and non-linear regression models.

# Employee compensation and reward

The compensation to an employee can be in monetary or in monetary form. The analysis can

be in market survey form to benchmark with other competitors in the market, and the regression

model can be used to estimate the market pay line and other predictors of pay level. The

company-ratio is introduced to compare employee’s pay rate in comparison with others

# employee in the same level.

# Table 1: Authors and People Analytics

# Authors

# Analytics

# Author

# Analytics

# Edwards

# and

# Diversity Analytics David E. Caughlin

# Employee Demographic

# Edward

(

# Employee Attitute

# Employee Surveys

# survey-

# Engagement

# and

# Workforce

# Perception

52

# Predicting

# Employee separation and

# Turnover

# retention

# Recruitment

# Employee selection

# Analysis

# Mornitoring

# the

- Employee

# impact

# of

# Training

# Inteverntion

- Employee

# compensation

# and

# rewards

- Employee

# performance

# management

# 2.13 Predictive analytics with Python

As Predictive analytics is considered as the highest level of PA, and Data Science is one of

building block for an analyst in PA ,we discuss the use of algorithm and demonstrate one of

the most popular PA analytics matter: to predict the turnover for Workforce planning

Kumar (2016) define predictive modelling as a collection of statistical algorithms implemented

within a statistical tool. When applied to historical data, these algorithms generate a

mathematical function or equation. Subsequently, this function can be employed to anticipate

future outcomes based on specific inputs, with the aim of achieving business goals or

facilitating improved decision-making in a broader context.. The array of available algorithms

for predictive modelling encompasses Linear Regression, Logistic Regression, Clustering,

53

Decision Trees, Time-Series Modeling, Naïve Bayes Classifiers, Natural Language Processing,

# among others.

These models fall into two distinct categories: supervised and unsupervised algorithms.

Supervised Algorithms: In this category, historical data includes both input variables and an

output variable. The model utilizes both input and output variables from past data. Examples

of supervised algorithms comprise Linear Regression, Logistic Regression, Decision Trees,

# and similar methods.

Unsupervised Algorithms: These algorithms operate without an output variable in historical

data. Clustering is an example of an unsupervised algorithm, wherein the model identifies

patterns and relationships within the input variables without the guidance of an output

# variable.

## Chapter 3: Predictive Analysis for Employee Attrition

3.1 Dataset exploration and cleaning using Python

The dataset is fictitious and was generated by IBM data experts. Examining the dataset can

reveal the elements contributing to employee turnover and delve into significant inquiries. In

the scope of this thesis, dataset is used to implementing predictive analysis.

The data set is accessed from https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-

# analytics-attrition-dataset

# in October 2023

According to data source classification of Isson et al. ( 2016, page 59), which put data into

three sources: Talent data, Company data and Labour market data. These data come from talent

data group, which refers to data of the HR department and organization as a whole, and the

# employee themselves.

According to Edwards and Edwards (2016), who summarized PA data sources into : HR

database, Employee attitude survey data, Customer satisfaction survey data, Sales performance

54

# data, and Operational performance data

HR database 'Age', 'Attrition', 'BusinessTravel', 'DailyRate', 'Department',

'DistanceFromHome', 'Education', 'EducationField', 'EmployeeCount',

'EmployeeNumber', 'Gender', 'HourlyRate',

'JobInvolvement', 'JobLevel', 'JobRole', 'YearsAtCompany', 'YearsInCurrentRole',

'YearsSinceLastPromotion',

# 'YearsWithCurrManager'

# Employee Attitude Survey data

'JobSatisfaction',

,

'EnvironmentSatisfaction',

## 'WorkLifeBalance', 'RelationshipSatisfaction'

# Import libraries

# import pandas as pd

# import numpy as np

# import matplotlib.pyplot as plt

import seaborn as sns

# %matplotlib inline

# import plotly.express as px

# Import library for feature engineering

from sklearn.preprocessing import LabelEncoder

# Libraries for performance evaluation

# # Classification performance evaluation

## from sklearn.model_selection import train_test_split

# from sklearn.metrics import classification_report,confusion_matrix, accuracy_score

# # Logistic regression

## from sklearn.linear_model import LogisticRegression

# # Decision trees

## from sklearn.tree import DecisionTreeClassifier

55

# from sklearn import tree

# import graphviz

## from sklearn.ensemble import BaggingClassifier

# # Random forest classifier

## from sklearn.ensemble import RandomForestClassifier

# # Regression

## from sklearn.metrics import mean_squared_error as MSE

## from sklearn.linear_model import LinearRegression

## from sklearn.tree import DecisionTreeRegressor

## from sklearn.ensemble import RandomForestRegressor

# # Grid search

## from sklearn.model_selection import GridSearchCV

Import dataset and check

# Read the file

## attrition_data = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')

# Check the data

# attrition_data.head()

This returns first five rows, at the same time we can check the width dimension of the dataset,

which is 35 columns.

We can check dataset columns by

# attrition_data.columns

This returns name of 35 columns

Index(['Age', 'Attrition', 'BusinessTravel', 'DailyRate', 'Department',

56

'DistanceFromHome', 'Education', 'EducationField', 'EmployeeCount',

'EmployeeNumber', 'EnvironmentSatisfaction', 'Gender', 'HourlyRate',

'JobInvolvement', 'JobLevel', 'JobRole', 'JobSatisfaction',

'MaritalStatus', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked',

'Over18', 'OverTime', 'PercentSalaryHike', 'PerformanceRating',

'RelationshipSatisfaction', 'StandardHours', 'StockOptionLevel',

'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance',

'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion',

'YearsWithCurrManager'],

# dtype='object')

Data cleaning with Python

# Check for duplication

# attrition_data.duplicated().sum()

Check the uniqueness of value across columns

# Notice from the quick check that there may are columns with only one value

# We conduct to check and drop features with just one value

# for col in attrition_data.columns:

uniques = len(attrition_data[col].unique())

if uniques == 1:

print("Dropping col: ", col)

## attrition_data.drop(col, axis=1, inplace=True)

This code detects and drops three columns, which has only one value.

Dropping col: EmployeeCount

Dropping col: Over18

Dropping col: StandardHours

57

# Over18: Y for all instances

# EmployeeCount: 1.0 for all instances

# StandardHours: 80.0 for all instances

EmployeeNumber is also dropped since Id doesn't have impact on the analysis

# Exploratory analysis of the dataset

## attrition_counts = attrition_data['Attrition'].value_counts()

# print(attrition_counts)

# Yes 237

# Name: Attrition, dtype: int64

# attrition_data.describe().T.style.background_gradient(axis = 0 ,cmap = "Oranges" )

# Explore numerical data

First we identify numerical data columns

numerical= attrition_data.select_dtypes(include = 'int64').columns

# print(numerical)

Index(['Age', 'DailyRate', 'DistanceFromHome', 'Education',

'EnvironmentSatisfaction', 'HourlyRate', 'JobInvolvement', 'JobLevel',

58

'JobSatisfaction', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked',

'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction',

'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear',

'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole',

'YearsSinceLastPromotion', 'YearsWithCurrManager'],

# dtype='object')

Store them in a list

# num_data=attrition_data[numerical]

# Plot numerical data

## # distribution of approximatly continuous numerical variables

plt.figure(figsize = (14,12))

# loop over the columns to create a histogram for each one

## for i, column in enumerate(num_data.columns, 1):

# plt.subplot(6, 4, i)

sns.histplot(num_data[column],kde = True)

## plt.title('Distribution of {}'.format(column))

# plt.tight_layout()

# plt.show()

59

Similarly, we explore categorical data, which Python define datatype as Object

category= attrition_data.select_dtypes(include = 'object').columns

# print(category)

Index(['Attrition', 'BusinessTravel', 'Department', 'EducationField', 'Gender',

'JobRole', 'MaritalStatus', 'OverTime'],

# dtype='object')

# Store columns names into a list

# category_data=attrition_data[category]

Then plot the categorical data

plt.figure(figsize = (20, 40))

60

# loop through the columns in category_data and plot a bar plot for each

## for i, column in enumerate(category_data.columns):

# plt.subplot(10, 3, i+1)

## sns.countplot(data = category_data, x = column)

## plt.title('Count of Different Types in {}'.format(column))

# plt.xticks(rotation = 90)

# plt.tight_layout()

# plt.show()

## Data feature engineering for Predictive Analysis

# One-hot encode categorical data

# encoder = LabelEncoder()

# for field in attrition_data.columns:

## if attrition_data[field].dtypes == 'object':

## attrition_data[field] = encoder.fit_transform(attrition_data[field])

# attrition_data.head()

## Relationship between each category to attrition

61

## attrition_data[numerical].apply(lambda x: x.corr(attrition_data['Attrition']))

# The result show correlation between some attribute like Age, Employee Satisfaction, Job

Involvement, Job level, monthly income, Stock Option level, Total Working Year, Years at

## company, Years in Current Roles, Year with Current Manager with Attrition

Age -0.159205

# DailyRate -0.056652

# DistanceFromHome 0.077924

# Education -0.031373

# EnvironmentSatisfaction -0.103369

# HourlyRate -0.006846

# JobInvolvement -0.130016

JobLevel -0.169105

# JobSatisfaction -0.103481

# MonthlyIncome -0.159840

# MonthlyRate 0.015170

NumCompaniesWorked 0.043494

# PercentSalaryHike -0.013478

PerformanceRating 0.002889

# RelationshipSatisfaction -0.045872

# StockOptionLevel -0.137145

TotalWorkingYears -0.171063

# TrainingTimesLastYear -0.059478

# WorkLifeBalance -0.063939

# YearsAtCompany -0.134392

# YearsInCurrentRole -0.160545

# YearsSinceLastPromotion -0.033019

# YearsWithCurrManager -0.156199

# dtype: float64

62

## Logistic Regression for Predictive Analysis

# 3.2 Logistic regression

Logistic Regression can be employed for Binary or Categorical Variables (for example, yes/no,

pass/fail), traditional linear regression is not appropriate. Logistic regression is introduced as

an alternative specifically tailored for these scenarios.

# There is an underlying Linear Relationship Assumption for Logistic Regression. The

assumption is : there a linear relationship between the predictor (independent) variables and

the output (dependent) variable. This means that the change in the predictor variables is

assumed to result in a linear change in the log-odds of the output variable in logistic regression.

In logistic regression, the output variable undergoes a transformation. Instead of predicting the

actual values, logistic regression predicts the probability that the given input belongs to a

particular category. The transformation involves converting the linear combination of

predictors into a probability using a logistic function, also known as the sigmoid

function.Logistic regression is particularly useful when dealing with binary outcomes or

situations where there are only two possible categories. The logistic function maps the linear

combination of predictors to a value between 0 and 1, representing the probability of belonging

# to one of the categories. (Kumar, 2016)

Question logistic regression helps to solve for our dataset is to predict whether a random

employee will voluntarily quite the position given his details such as salary, distance from

home, his age, education level and time working in current position and so on. These conditions

are in this case predictor variables while output variables are the Quit/ Not Quite categorial

# value.

## 3.3 Predictive Analysis with Logistic Regression

# prediction_data = attrition_data

Assigned predictors and outcome

## X = prediction_data.drop(['Attrition'], axis=1)

# y= prediction_data['Attrition']

# X.columns

63

# Create training data and test set

# #create training and test set

## This will create four things:

## # X_train and X_test: predictors for training and test set

## # y_train and y_test: outcome for training and test set

## X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2

Import function to build the model

## from sklearn.linear_model import LogisticRegression

## model = LogisticRegression(max_iter=10000,solver = 'lbfgs')

Train the model using fit

# model.fit(X_train, y_train)

# Model fit

# import statsmodels.api as sm

# logit_model = sm.Logit(y_train, X_train)

# result = logit_model.fit()

# print(result.summary())

Apply to test set

# y_predict = model.predict(X_test)

# y_predict[:10]

Check to model with confusion matrix

## from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

## matrix = confusion_matrix(y_test, y_predict)

# print(matrix)

64

Which returns:

[[236 9]

[ 35 14]]

# Classification report

## from sklearn.metrics import classification_report

report = classification_report(y_test, y_predict)

# print(report)

(cid:32)(cid:32)(cid:32)(cid:112)(cid:114)(cid:101)(cid:99)(cid:105)(cid:115)(cid:105)(cid:111)(cid:110)(cid:32)(cid:32)(cid:32)(cid:32)(cid:114)(cid:101)(cid:99)(cid:97)(cid:108)(cid:108)(cid:32)(cid:32)(cid:102)(cid:49)(cid:45)(cid:115)(cid:99)(cid:111)(cid:114)(cid:101)(cid:32)(cid:32)(cid:32)(cid:115)(cid:117)(cid:112)(cid:112)(cid:111)(cid:114)(cid:116)(cid:32) (cid:32) (cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:48)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:48)(cid:46)(cid:56)(cid:56)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:48)(cid:46)(cid:57)(cid:54)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:48)(cid:46)(cid:57)(cid:50)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:50)(cid:53)(cid:48)(cid:32) (cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:49)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:48)(cid:46)(cid:53)(cid:50)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:48)(cid:46)(cid:50)(cid:55)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:48)(cid:46)(cid:51)(cid:54)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:52)(cid:52)(cid:32) (cid:32) (cid:32)(cid:32)(cid:32)(cid:32)(cid:97)(cid:99)(cid:99)(cid:117)(cid:114)(cid:97)(cid:99)(cid:121)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:48)(cid:46)(cid:56)(cid:53)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:50)(cid:57)(cid:52)(cid:32) (cid:32)(cid:32)(cid:32)(cid:109)(cid:97)(cid:99)(cid:114)(cid:111)(cid:32)(cid:97)(cid:118)(cid:103)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:48)(cid:46)(cid:55)(cid:48)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:48)(cid:46)(cid:54)(cid:49)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:48)(cid:46)(cid:54)(cid:52)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:50)(cid:57)(cid:52)(cid:32) (cid:119)(cid:101)(cid:105)(cid:103)(cid:104)(cid:116)(cid:101)(cid:100)(cid:32)(cid:97)(cid:118)(cid:103)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:48)(cid:46)(cid:56)(cid:51)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:48)(cid:46)(cid:56)(cid:53)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:48)(cid:46)(cid:56)(cid:51)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:50)(cid:57)(cid:52)(cid:32)

# Plot the confusion matrix

## disp= ConfusionMatrixDisplay(confusion_matrix= matrix)

# disp.plot()

## plt.title('Confusion Matrix of Regression model')

# plt.show()

65

(cid:102)(cid:114)(cid:111)(cid:109)(cid:32)(cid:115)(cid:107)(cid:108)(cid:101)(cid:97)(cid:114)(cid:110)(cid:46)(cid:109)(cid:111)(cid:100)(cid:101)(cid:108)(cid:95)(cid:115)(cid:101)(cid:108)(cid:101)(cid:99)(cid:116)(cid:105)(cid:111)(cid:110)(cid:32)(cid:105)(cid:109)(cid:112)(cid:111)(cid:114)(cid:116)(cid:32)(cid:99)(cid:114)(cid:111)(cid:115)(cid:115)(cid:95)(cid:118)(cid:97)(cid:108)(cid:95)(cid:115)(cid:99)(cid:111)(cid:114)(cid:101)(cid:32) (cid:109)(cid:111)(cid:100)(cid:101)(cid:108)(cid:32)(cid:61)(cid:32)(cid:76)(cid:111)(cid:103)(cid:105)(cid:115)(cid:116)(cid:105)(cid:99)(cid:82)(cid:101)(cid:103)(cid:114)(cid:101)(cid:115)(cid:115)(cid:105)(cid:111)(cid:110)(cid:40)(cid:109)(cid:97)(cid:120)(cid:95)(cid:105)(cid:116)(cid:101)(cid:114)(cid:61)(cid:49)(cid:48)(cid:48)(cid:48)(cid:48)(cid:44)(cid:115)(cid:111)(cid:108)(cid:118)(cid:101)(cid:114)(cid:32)(cid:61)(cid:32)(cid:39)(cid:108)(cid:98)(cid:102)(cid:103)(cid:115)(cid:39)(cid:41)(cid:32) (cid:115)(cid:99)(cid:111)(cid:114)(cid:101)(cid:115)(cid:32)(cid:61)(cid:32)(cid:99)(cid:114)(cid:111)(cid:115)(cid:115)(cid:95)(cid:118)(cid:97)(cid:108)(cid:95)(cid:115)(cid:99)(cid:111)(cid:114)(cid:101)(cid:40)(cid:109)(cid:111)(cid:100)(cid:101)(cid:108)(cid:44)(cid:32)(cid:88)(cid:95)(cid:116)(cid:114)(cid:97)(cid:105)(cid:110)(cid:44)(cid:32)(cid:121)(cid:95)(cid:116)(cid:114)(cid:97)(cid:105)(cid:110)(cid:44)(cid:32)(cid:99)(cid:118)(cid:61)(cid:53)(cid:44)(cid:32)(cid:115)(cid:99)(cid:111)(cid:114)(cid:105)(cid:110)(cid:103)(cid:32)(cid:61)(cid:32) (cid:39)(cid:97)(cid:99)(cid:99)(cid:117)(cid:114)(cid:97)(cid:99)(cid:121)(cid:39)(cid:41)(cid:32) (cid:115)(cid:99)(cid:111)(cid:114)(cid:101)(cid:115)(cid:32)

(cid:97)(cid:114)(cid:114)(cid:97)(cid:121)(cid:40)(cid:91)(cid:48)(cid:46)(cid:56)(cid:52)(cid:55)(cid:52)(cid:53)(cid:55)(cid:54)(cid:51)(cid:44)(cid:32)(cid:48)(cid:46)(cid:56)(cid:54)(cid:51)(cid:56)(cid:50)(cid:57)(cid:55)(cid:57)(cid:44)(cid:32)(cid:48)(cid:46)(cid:56)(cid:53)(cid:49)(cid:48)(cid:54)(cid:51)(cid:56)(cid:51)(cid:44)(cid:32)(cid:48)(cid:46)(cid:56)(cid:53)(cid:49)(cid:48)(cid:54)(cid:51)(cid:56)(cid:51)(cid:44)(cid:32)(cid:48)(cid:46)(cid:56)(cid:56)(cid:48)(cid:56)(cid:53)(cid:49)(cid:48)(cid:54)(cid:93)(cid:41)(cid:32) (cid:109)(cid:115)(cid:101)(cid:32)(cid:61)(cid:32)(cid:77)(cid:83)(cid:69)(cid:40)(cid:121)(cid:95)(cid:116)(cid:101)(cid:115)(cid:116)(cid:44)(cid:32)(cid:121)(cid:95)(cid:112)(cid:114)(cid:101)(cid:100)(cid:105)(cid:99)(cid:116)(cid:41)(cid:32) (cid:112)(cid:114)(cid:105)(cid:110)(cid:116)(cid:32)(cid:40)(cid:109)(cid:115)(cid:101)(cid:41)(cid:32)

(cid:48)(cid:46)(cid:49)(cid:52)(cid:54)(cid:50)(cid:53)(cid:56)(cid:53)(cid:48)(cid:51)(cid:52)(cid:48)(cid:49)(cid:51)(cid:54)(cid:48)(cid:53)(cid:52)

# 3.4 Tree and Random Forest with Python

A decision tree is a supervised machine learning algorithm primarily used for classification

tasks, particularly when the target variable is discrete or categorical (i.e., it has distinct classes).

This algorithm is also applicable for regression tasks, where the target variable is continuous,

but here we'll focus on its classification aspect.

Decision trees fall under the category of supervised learning algorithms. In supervised learning,

the algorithm is trained on a labeled dataset where both input features (predictors) and

corresponding target labels (categories) are known. Decision trees are well-suited for scenarios

66

where the outcomet to predict is categorical and has two or more classes. For our instance, it is

classification problem like determining whether an employee will leave or not.

Predictor variables, for classification tree, can be either categorical or numerical. This

flexibility allows decision trees to handle a variety of data types.The decision-making process

in a decision tree is represented as a tree-like structure of if-then rules. Each node in the tree

represents a decision based on a specific feature, and the branches emanating from the node

represent the possible outcomes of that decision. The leaves of the tree correspond to the final

# predicted class.

# Multiple-Staged Criteria and Variables:

Decision trees are particularly useful when decisions are based on multiple stages, involving

different criteria and variables at each stage. The algorithm iteratively chooses the best features

to split the data, resulting in a tree structure that captures the decision-making process.

Decision trees serve as effective decision-making tools due to their clear and interpretable

structure. They are used in various fields, including finance, healthcare, and marketing, where

decisions based on multiple criteria need to be made

# Figure 20: Decision tree illustration

# representation of a decision tree

67

## 3.5 Implementing Tree Regression and Random Forest with Python

From the above imported dataset and exploration, further analysis can be done for tree

# regression and decision tree

# Create other training and test set

## X2 = data.loc[:, data.columns != 'Attrition']

# y2 = data['Attrition']

## X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, random_state=42)

# # Decision tree

attrition_tree = DecisionTreeClassifier(random_state = 42)

## tree_model = attrition_tree.fit(X_train2,y_train2)

# pred_tree = tree_model.predict(X_test2)

## print(confusion_matrix(y_test2,pred_tree))

# 2 out 3 in the more important class is missed

## print(classification_report(y_test2,pred_tree))

# Which returns

[[276 44]

[ 33 15]]

precision recall f1-score support

0 0.89 0.86 0.88 320

1 0.25 0.31 0.28 48

# accuracy 0.79 368

macro avg 0.57 0.59 0.58 368

68

weighted avg 0.81 0.79 0.80 368

# To see how we perform we create prediction and calculate MSE

# mse_1 = MSE(y_test2, pred_tree)

print('MSE of unpruned tree is', mse_1)

MSE of unpruned tree is 0.20923913043478262

Because the previous simple linear regression performs better, tree should be pruned

params = {"criterion":("gini", "entropy"),

"splitter":("best", "random"),

"max_depth":(list(range(1, 20))),

"min_samples_split":[2, 3, 4],

"min_samples_leaf":list(range(1, 20)),

}

## tree_clf = DecisionTreeClassifier(random_state=42)

# tree_cv = GridSearchCV(

tree_clf,

params,

scoring="f1",

n_jobs=-1,

verbose=1,

# cv=5

)

# tree_cv.fit(X_train2, y_train2)

# best_params = tree_cv.best_params_

print(f"Best paramters: {best_params})")

69

## tree_clf = DecisionTreeClassifier(**best_params)

# tree_clf.fit(X_train2, y_train2)

# attrition_tree_tune

## = DecisionTreeClassifier(criterion='entropy', max_depth=

# min_samples_leaf= 17)

## tree_model_tune = attrition_tree_tune.fit(X_train2,y_train2)

## pred_tree_tune = tree_model_tune.predict(X_test2)

## print(confusion_matrix(y_test2,pred_tree_tune))

# 2 out 3 in the more important class is missed

## print(classification_report(y_test2,pred_tree_tune))

# Which returns

[[300 20]

[ 33 15]]

precision recall f1-score support

0 0.90 0.94 0.92 320

1 0.43 0.31 0.36 48

# accuracy 0.86 368

macro avg 0.66 0.62 0.64 368

weighted avg 0.84 0.86 0.85 368

# Calculate MSE

70

8,

# mse_2 = MSE(y_test2, pred_tree_tune)

print('MSE of pruned tree is', mse_2)

(cid:32) (cid:77)(cid:83)(cid:69)(cid:32)(cid:111)(cid:102)(cid:32)(cid:112)(cid:114)(cid:117)(cid:110)(cid:101)(cid:100)(cid:32)(cid:116)(cid:114)(cid:101)(cid:101)(cid:32)(cid:105)(cid:115)(cid:32)(cid:48)(cid:46)(cid:49)(cid:52)(cid:52)(cid:48)(cid:50)(cid:49)(cid:55)(cid:51)(cid:57)(cid:49)(cid:51)(cid:48)(cid:52)(cid:51)(cid:52)(cid:55)(cid:56)

# Calculate and plot confusion matrix

## matrix2 = confusion_matrix(y_test2, pred_tree_tune)

# print(matrix2)

[[300 20]

[ 33 15]]

## disp= ConfusionMatrixDisplay(confusion_matrix= matrix2)

# disp.plot()

## plt.title('Confusion Matrix of Pruned tree model')

# plt.show()

See what features are the most important

# # First try with decision trees

71

# We can simply obtain feature importance using feature_importances_

# We check our best model for regression trees

# We can see that only three varibales play a role in the prediction

# pd.Series(data

=

# tree_clf

.feature_importances_,

## X_train2.columns).sort_values(ascending= False)

# Top 5 most important features:

# MonthlyIncome 0.212755

# OverTime 0.180789

# TotalWorkingYears 0.084827

# MaritalStatus 0.064750

# YearsAtCompany 0.055265

# Random Forest

## X3= attrition_data.drop(['Attrition'], axis=1)

# # Outcome

# y3= attrition_data['Attrition']

# Then we create training and test set, with 25% of the data in the test set

# X_train3, X_test3, y_train3, y_test3 =

train_test_split(X3, y3,

# random_state=42)

attrition_rf = RandomForestClassifier(n_estimators = 200, random_state = 0)

72

# index=

test_size=0.25,

# We fit the training set

# attrition_rf.fit(X_train3, y_train3)

# # Create predictions

## y_pred_rf = attrition_rf.predict(X_test3)

# mse_rf = MSE(y_test3, y_pred_rf)

# As we can see, without any parameter selection, we already got better results than linear

# regression

print('MSE of random forests is', mse_rf)

MSE of random forests is 0.13043478260869565

Optimize the random forest

## grid = dict(max_depth = [4, 6, 8], min_samples_leaf = [10, 15, 20])

forest_att = RandomForestClassifier(n_estimators = 200, random_state = 0)

# grid_search

=

GridSearchCV(estimator=forest_att,

param_grid=grid,

# scoring='neg_mean_squared_error')

# grid_result = grid_search.fit(X, y)

# # Print out the best result

print("Best result is obtained using", grid_result.best_params_)

Best result is obtained using {'max_depth': 6, 'min_samples_leaf': 10}

73

attrition_rf = RandomForestClassifier(n_estimators = 200, max_depth = 6,

# min_samples_leaf = 10, random_state = 0)

# We fit the training set

## attrition_rf_fit = attrition_rf.fit(X_train3, y_train3)

# # Create predictions

## y_pred_rf =attrition_rf_fit.predict(X_test3)

# mse_rf = MSE(y_test3, y_pred_rf)

# As we can see, without any parameter selection, we already got better results than linear

# regression

print('MSE of random forests is', mse_rf)

# #feature importance

# pd.Series(data

=

# attrition_rf_fit

.feature_importances_,

## X_train3.columns).sort_values(ascending= False)

# OverTime 0.129725

# MonthlyIncome 0.111417

# TotalWorkingYears 0.077554

Age 0.074027

# StockOptionLevel 0.057388

(cid:77)(cid:83)(cid:69)(cid:32)(cid:111)(cid:102)(cid:32)(cid:111)(cid:112)(cid:116)(cid:105)(cid:109)(cid:105)(cid:122)(cid:101)(cid:100)(cid:32)(cid:114)(cid:97)(cid:110)(cid:100)(cid:111)(cid:109)(cid:32)(cid:102)(cid:111)(cid:114)(cid:101)(cid:115)(cid:116)(cid:115)(cid:32)(cid:105)(cid:115)(cid:32)(cid:48)(cid:46)(cid:49)(cid:50)(cid:55)(cid:55)(cid:49)(cid:55)(cid:51)(cid:57)(cid:49)(cid:51)(cid:48)(cid:52)(cid:51)(cid:52)(cid:55)(cid:56)(cid:52)

## matrix3 = confusion_matrix(y_test3, y_pred_rf)

# print(matrix3)

74

# index=

[[317 3]

[ 44 4]]

## disp= ConfusionMatrixDisplay(confusion_matrix= matrix3)

# disp.plot()

## plt.title('Confusion Matrix of Random Forest model')

# plt.show()

## print(classification_report(y_test3,y_pred_rf))

precision recall f1-score support

0 0.88 0.99 0.93 320

1 0.57 0.08 0.15 48

# accuracy 0.87 368

macro avg 0.72 0.54 0.54 368

weighted avg 0.84 0.87 0.83 368

75

# 3.6 Conclusion from analysis

Based on the conducted analysis utilizing logistic regression, decision tree, and random forest

algorithms to predict employee attrition, several key conclusions can be drawn:

Random forest, particularly after tuning hyperparameters, emerged as the most effective

method for predicting employee attrition. This indicates that the ensemble approach of

combining multiple decision trees and utilizing bootstrapping and feature randomness leads to

# superior predictive performance.

Despite random forest's superiority after tuning, it's noteworthy that even without

hyperparameter tuning, the random forest still outperformed the other methods, showcasing its

robustness and versatility in handling data with minimal parameter optimization.

The performance of logistic regression, while a commonly used method, fell short compared

to both random forest and decision tree models. This suggests that the linear relationship

assumptions of logistic regression might not capture the complexity and non-linearity present

## in the employee attrition data as effectively as decision tree-based methods.

Decision tree, particularly when pruned to avoid overfitting, showed competitive performance

but ultimately ranked lower compared to random forest. Pruning helps simplify the tree

structure and prevents it from capturing noise in the data, yet it may also lead to some loss of

predictive accuracy compared to random forest's ensemble approach.

In conclusion, the findings suggest that for predicting employee attrition, employing a random

forest model with proper hyperparameter tuning yields the most accurate results. However, it's

essential to recognize the comparative advantages and limitations of each method in different

scenarios. Logistic regression remains a straightforward baseline model, while decision trees,

especially pruned ones, offer interpretability alongside reasonable predictive performance.

Future research could explore ensemble methods further or investigate additional features to

# enhance predictive accuracy.

76

# Chapter 4

# 4.1 Ethics and Other Considerations

Challenges in the use of Predictive PA are argue to benefit companies and yield advantages for

employees through various functionalities. In its most effective implementation, analytics aids

in the identification of talent that might otherwise go unnoticed. This, in turn, fosters a more

equitable reward system and empowers employees by facilitating enhanced workplace

retention. Overall, it ensures employee satisfaction, engagement, and optimal performance as

it becomes more recognizable with evidence.

On the other hand, many authors criticize the nature of PA and point out its unethical side and

risk of being misused. For instance, Schiemann et al. (2017) raise concern about People

analytics as a <backward looking=, when collecting historical data on employee background

and their performance. To have a good grasp of the future scene, it requires organizations to

poccess a very wide variety of skills to leverage historical data. Furthermore, in an

organizational context the provision the actionable insight extracted from data does not

guarantee the buy-in of decision makers, whether insights are taken into consideration or

implemented in actual action.

There are more risks beyond the question of PA in general and Predictive Analysis. According

to Giermindl et al. (2021), there are four prime challenges that organizations should take into

consideration while employing PA.

First challenge to be mentioned by the authors (Giermindl et al, 2021) is the utilization of PA

to monitor workplace behavior raises ethical and moral questions that demand careful

consideration. There are concerns over data privacy related to collected data's content, usage,

and access. The second concern is transparency. Transparency and informed consent are crucial

in maintaining ethical standards. The third concern is data quality, as the trained dataset has a

significant impact on the algorithm. Ensuring data accuracy and fairness in algorithms is a

significant ethical challenge. Second challenge is the application of algorithms to control

human actions has substantial implications for organizational dynamics, feasibility, societal

77

effects, and workplace ethical standards. These consequences are not thoroughly explored and

need proper examination and resolution. The third challenge raised by the authors is the

behavior of humans is generally highly complex, often shaped by complex factors such as

emotions, culture, and personal experiences. Handing the interpretation of human behavior to

an algorithm may result in overlooking the intricate nature of human factors. These

misinterpretations may lead to financial costs to the business. Last but not least, PA can be

intrusive and may violate employees' data protection and privacy rights due to excessive data

collection and lack of transparency in data usage. Continuous monitoring may create an

atmosphere of constant surveillance, impacting employee’s sense of autonomy and freedom

# within the workplace.

Misinterpretation of HR data may cause significantly high costs both financial and non-

financial to employers and employees. The companies may suffer from not just financial loss

to companies and organizations but also life-changing impact on employees. Misinterpreting

HR data can lead to ineffective recruitment, training, and performance management decision-

making. It can also result in wasted resources, inefficient budget allocation, and missed growth

opportunities. In the long term, these financial losses can be substantial and hinder the

organization's ability to compete in the market. Consequently, a wrong decision may negatively

impact organizational reputation or lead to legal liabilities. Unfair treatment due to

misinterpretation has an adverse effect on employee well-being and hinders their professional

# growth.

Moreover, according to Tursunbanyera et al. (2018), companies tend to prioritize the

technological aspects of Predictive Analytics, emphasizing the adoption and upgrading of IT

infrastructure in their quest for more efficient data mining methods. Conversely, the ethical

dimensions of PA are receiving inadequate attention compared to their significance. The

authors also highlight the lack of literature regarding the ethical side of PA, or <near absence

of ethical considerations in the corpus of academic, grey and online literature, despite the

significant risks to privacy and autonomy these innovations present for employees=

# 4.2 Predictive analytics criticism

Predictive analytics can contribute to enhancing the additional business value for the company.

Conversely, Oehler and Falletta (2015) argue that these advancements are game changers when

78

creating new business tasks for the HR department. The authors argue instead of a human-to-

human relationship, HR when fueled with analytics emphasizes more on business value and

financial value, as well as profit creation. The authors also postulate discrimination against

certain candidates or employees which is caused by the analytics and algorithm.

## 4.3 Other suggestions to utilize People Analytics or Predictive Analytics

Leonardi and Contractor (2018) criticize the current People Analytics approach as <narrow=

while employing only attribute data, which describes only facts and state of the employee. They

propose Relational Analytics, utilizing social network analytics, rather than data about Traits,

which are static characteristics, attributes, or qualities of an individual or an object, and State,

which are typically transient and subject to variability over time.

The authors propose six signatures of Relational Analytics, which mines personal

communication in various forms for analyzing and interpreting patterns, relationships, and

structures within social networks. This Relational Analytics examines interaction(cid:32)Patterns by

analyzing the frequency and nature of interactions between individuals or entities within and

beyond the border of an organization. In addition, the analysis can investigate how a particular

individual influences others and study the spread of opinions or behaviors within the network.

This analytics may involve identifying key influencers or understanding the mechanisms

# behind information diffusion.

# Including the predict are Ideation signature, Influence, Efficiency, Innovation, Silo, and

# Vulnerability

Ideation signature: This analysis is used to predict the employee who may generate novel ideas

by exchanging information with a variety of people and entities, especially external groups or

organizations. Influence analysis is used to predict the ability to influence and figure out the

most influential employees. Efficiency analysis identifies the teams that will successfully

conclude projects within the specified timeframe by looking at the internal density among the

79

team members. Innovation analysis is used to identify the teams that will demonstrate practical

innovation by examining the external density to the internal density of communication. This

analysis can also prove whether the team may possess diverse ideas and information. Silo

analysis determines if there are silos within an organization. This signature also introduces

modularity, which is the internal-to-external communication proportion. An organization tends

to be silo and has a high modularity. Vulnerability analysis determines a key and irreplaceable

employee of the organization, without whom the network may become disconnected and

# siloed.

## 4.4 Elements to Evolution of People Analytics

There are four elements that Fitz-Enz and II Mattox (2014) believe will shape the emerging

trend of PA. The first element authors mention, however, is not Information Technology but

the Finance field, which include Business standards and the assessment of an organization's

value.These standards and valuation act as framework and provides a structured approach for

organizations to gather and report data related to talent development within the realm of Human

Resources. It outlines principles and guidelines for reporting metrics that are essential for

understanding and managing the development of an organization's workforce. This

standardized approach ensures consistency and uniformity in how organizations measure and

report HR metrics. It also allows for benchmarking, enabling organizations to compare their

performance against industry standards or best practices. This, in turn, facilitates a more

comprehensive understanding of where an organization stands in terms of talent development.

The second element authors emphasize is Mathematics or more accurately the significance of

modeling, particularly in the context of understanding seemingly chaotic situations, such as

those found in organizational processes like the recruiting cycle. The author draws inspiration

from James Gleick's perspective on mathematics, asserting that modeling is essential for

accurately defining a situation. According to Gleick, the primary objective of mathematics is

to unveil the intricate structures concealed within seemingly disorderly streams of data.

The author argues that the scientific exploration of chaotic processes aims to uncover and

define the underlying patterns. Once these patterns or structures are identified, they can be

80

explained. This explanatory step is deemed crucial for any system, including the recruitment

# cycle within an organization.

The narrative suggests that understanding the contributing factors to chaotic or unpredictable

processes allows for control. By comprehending and controlling the inputs, organizations can

influence the outputs. In the context of the recruiting cycle, this implies that by understanding

and managing the factors contributing to unpredictable hiring and firing patterns, organizations

can mitigate the extremes of overstaffing and understaffing.

The ultimate goal is to bring stability to the workforce by controlling these extreme swings,

leading to more predictable and manageable outcomes. This control, in turn, has positive

## implications for organizational efficiency, effectiveness, and profitability.

The third element is Big Data, an emerging trend in IT. This Big Data growth among HR

professionals is fuelled by the desire for Predictive Analytics among Leaders. Predictive

analytics involves using data, statistical algorithms, and machine learning techniques to

identify the likelihood of future outcomes based on historical data. The emphasis is on tracking

and improving future performance rather than just understanding the current situation.

Secondly, the availability and accessibility of advanced statistical tools allow analysts to delve

deeper into understanding the "why" behind data patterns, moving beyond basic descriptive

statistics. Lastly, roles such as business analysts, statisticians will see increased demand. In

response to the business need for sophisticated data analysis more professionals are educated

and become available.

Last but not least, more automated processes will be introduced and provide feedback in real

# time or with minimal time gap.

81

# Chapter 5: Discussion

The aim of this thesis was to enhance comprehension of HR analytics and its practical

application. Furthermore, it investigated the potential value of various levels of People

# analytics to the decision-making processes of business and its decision-makinng process.

The perception of the HR function transcends its traditional role as a mere business support

entity to current role as a pivotal driver of strategic drivers. This shift is propelled by various

factors, including the evolving demographics of the workforce, increased labor mobility, and

notably, the influence of digitalization. Consequently, HR is tasked with novel responsibilities

at a higher level of importance within organizations. To effectively leverage HR capabilities,

businesses must adopt an effective analytics approach to understanding their workforce just as

the way they understand their customers, utilizing data-driven insights. This approach,

advocating for evidence-based decision-making over reliance on intuition and anecdotal

evidence, not only demonstrates tangible impacts on business outcomes but also exerts a

# profound influence on both operational and strategic decision-making processes (van den

# Heuvel & Bondarouk, 2017).

While metrics and reporting play an important role, many now recognize that analytics goes

far deeper. Its core strength lies in identifying trends and patterns within the data. By

uncovering these hidden insights, organizations can develop strategic roadmaps that inform

data-driven decision-making. This shift empowers organizations to move beyond simply

measuring performance and instead leverage analytics to proactively shape their future success

Research reinforces the established notion that data analytics can significantly enhance an

organization's performance, both financially and non-financially, ultimately leading to a

competitive advantage (van de Wetering et al., 2019; Wamba et al., 2017, Pease (2015)).

Regarding financial benefit, data analytics doubles the likelihood of achieving top-quartile

financial performance within their respective industries. While non-financially wise data

analytics speeds the decision-making capabilities up by five times faster, triples the success

rate in executing decisions as planned, and doubles the frequency of utilizing data-driven

decision-making compared to non-advanced analytics users.

82

Within the HR domain, PA emerges as a critical data analysis practice. PA involves the

measurement, analysis, and integration of various HR and non - HR data points.. HR analytics

and big data have emerged as potential solutions to overcome this challenge. By enabling the

integration of data from diverse sources, both internal (within HR) and external, these

approaches can bridge the gap between HR and the broader business context. This integrated

view allows HR to make data-driven decisions that are strategically aligned with overall

## business goals and not just talent management strategies.

As People Analytics (PA) reaches a higher level of maturity, its applications within HR extend

far beyond influencing hiring decisions. It has the potential to transform a wide range of HR

## practices (Edwards & Edwards 2016, Caughlin 2023), including:

Employee Selection: PA can go beyond resumes by analyzing skills, cultural fit, and past

performance data to identify top talent.

Leadership Development: By analyzing leadership behavior and its impact on employee

engagement and performance, PA can inform targeted leadership development programs.

Employee Engagement: Employee surveys become more insightful when combined with

other HR data points, allowing for a deeper understanding of employee sentiment and the

## development of targeted engagement strategies.

Diversity & Inclusion: PA can support diversity analysis by identifying potential biases in

recruitment and promotion practices and measuring the impact of diversity initiatives.

Retention Management: Analyzing separation data alongside other factors can help identify

## the root causes of turnover and inform retention strategies.

Performance & Productivity: Leveraging performance management data helps identify areas

for improvement and allows for a more data-driven approach to talent development.

Compensation & Reward Fairness: PA can help ensure fairness in compensation practices

by analyzing pay equity across various demographics. Additionally, employee survey data

enriched with performance indicators can inform more effective reward structures.

The evolution of technology has enabled corporations to retain and leverage their ever-growing

data reserves. This vast amount of data, however, remains largely untapped without the

complementary expertise to analyze and extract meaningful insights. It is the convergence of

powerful technology and the skilled application of analytical methods that unlocks the true

potential of data. By harnessing these combined forces, corporations can transform raw data

83

into actionable intelligence that informs strategic decision-making, drives innovation, and

# ultimately fuels competitive advantage.

People Analytics (PA) establishes itself as the critical foundation for iterative strategic

decision-making processes within HR. It provides a framework for leveraging the various

utilization of data-driven Human Resource Management (HRM), encompassing data, metrics,

and analytics, across all stages of the decision-making cycle. This integrated approach ensures

that the value of these elements lies not in their standalone existence, but rather in their

application (Fitz-enz, 2010). Consequently, the selection of appropriate metrics and analytical

tools becomes crucial. Tailoring these elements to the specific context of the decision at hand

is essential for maximizing their effectiveness.

In the pursuit of maturity within PA, there are suggestions that consistency throughout the

analytical process is paramount. Maintaining standardized procedures for data collection,

analysis, and evaluation across various projects and time frames is essential. Evaluation post-

analysis emerges as a crucial component of maturity levels. By systematically assessing the

effectiveness and impact of each analysis, organizations can gauge whether the insights gleaned

are aligned with initial objectives and if they translate into actionable outcomes. This iterative

evaluation process serves as a foundation for continuous improvement within analytical

endeavors. Another pivotal aspect contributing to maturity lies in the selection of appropriate

data collection method and tailor data collection approaches to the specific research questions.

Whether drawing from structured quantitative data sources or tapping into unstructured

qualitative data, the focus should always be on data relevance, accuracy, and reliability and

legal, ethical aspects. Equally significant is the consideration of methodology. The choice of

analytical approach should align closely with the objectives of the analysis and the nature of

# the data available.

In essence, the journey toward maturity in PA hinges on a multifaceted approach encompassing

# consistency in processes, rigorous evaluation of outcomes, thoughtful selection of data

# collection methods, and the application of appropriate analytical methodologies. By

prioritizing these considerations, organizations can foster a culture of data-driven decision-

making that propels them toward greater organizational effectiveness and performance.

84

## Appendix List of Literature by abo.finna.fi search:

# Excellence in people

analytics : how to use

## https://abo.finna.fi/Record/abo_electronic_

workforce data to create

aa.9913646199405972?sid=2937807369

# business value

# Introduction to People

# Analytics: A Practical

## https://abo.finna.fi/Record/abo_electronic_

# Guide to Data-Driven

aa.9913646083805972?sid=2937947946

# HR Data-Driven HR

# The Practical Guide to

# HR Analytics : Using

# Data

## https://ebookcentral.proquest.com/lib/abo-

to Inform, Transform,

# ebooks/reader.action?docID=5415355

# and Empower HR

# Decisions

# Developing Human

# Capital : Using

# Analytics to Plan and

## https://ebookcentral.proquest.com/lib/abo-

# Optimize Your Learning

# ebooks/reader.action?docID=1718752

# and Development

# Investments

85

# Jonathan Ferrar; David

# Green

# Nadeem Khan, Dave

# Millner

# Rachael Johnson-

# Murray, , Lindsay

# McFarlane, , Valerie

Streets, ,

# and Shonna Waters

# Gene Pease, , Barbara

# Beresford, , and Lew

# Walker

# Optimize Your Greatest

# Asset -- Your People :

# How to Apply

# Analytics to Big Data to

# Improve Your Human

# Capital Investments

# People Analytics

# in the Era of Big Data :

# Changing the Way You

Attract, Acquire,

# Develop, and

# Retain Talent

# Predictive HR analytics :

mastering the HR

# metric

# Learning

# Predictive Analytics

# with Python : Gain

# Practical Insights into

# Predictive

# Modelling by

# Implementing Predictive

# Analytics Algorithms on

# Public Datasets

# with Python

## https://ebookcentral.proquest.com/lib/abo-

# ebooks/detail.action?docID=4040706

## https://ebookcentral.proquest.com/lib/abo-

# ebooks/detail.action?docID=4513107

## https://abo.finna.fi/Record/abo_electronic_

aa.9913645333205972?sid=2927301361&i

# mgid=1

## https://abo.finna.fi/Record/abo_electronic_

aa.9913617389705972?sid=2927301361

86

# Gene Pease

# Jean-Paul Isson, Jesse

# S. Harriott, and Jac

# Fitz-enz

# Edwards, Martin R. ;

Edwards,

# Kirsten

Kumar, Ashish,

author ; Gulipalli,

# Pradeep, writer of

# foreword

# The New HR Analytics :

Predicting the

# EconomicValue of

## https://ebookcentral.proquest.com/lib/abo-

# ebooks/reader.action?docID=533015

# Jac Fitz-Enz

# Your Company's Human

# Capital Investments

# Human Capital

# Analytics: How to

## https://abo.finna.fi/Record/abo_electronic_

# Gene Pease, Boyce

# Harness the Potential of

# Your Organization's

aa.9913646932905972?sid=3139389180

# Byerly,Jac Fitz-enz

# Greatest Asset

# HR analytics and

## https://abo.finna.fi/Record/abo_electronic_

# innovations in

aa.9913514103105972?sid=3508218757

# Tony Miller

# workforce planning

# Reference list:

(cid:111) Aitkenhead, M. (2008). A co-evolving decision tree classification method. Expert Systems With Applications, 34(1), 18325.

https://doi.org/10.1016/j.eswa.2006.08.008

87

# (cid:111) Ben

Gal, H. C. (2019). An ROI-based review of HR analytics: practical

# implementation

‐

## tools. Personnel Review, 48(6), 142931448.

https://doi.org/10.1108/pr-11-2017-0362

(cid:111) Bersin, J. (2015, February 1). The geeks arrive in HR: People Analytics from

is

# her.

# Forbes.

# Retrieved October

6,

2023,

## https://www.forbes.com/sites/joshbersin/2015/02/01/geeks-arrive-in-hr-

## people-analytics-is-here/?sh=4ae63a5673b4

(cid:111) Caughlin, D. E. (2023). R for HR: An introduction to human resource [Ebook].

# analytics

using R

# (Version

0.1.3:

2023-09-13)

# https://rforhr.com/

(cid:111) Characteristics of Big Data: Types & Examples. (n.d.). Bay Atlantic from

# University.

# Retrieved

# May

7,

2023,

## https://bau.edu/blog/characteristics-of-big-data/

(cid:111) Chornous, G., & ура, . (2020). Integration of information systems for predictive workforce analytics: models, synergy, security of

Entrepreneurship. European Journal of Sustainable Development, 9(1),

- 83. https://doi.org/10.14207/ejsd.2020.v9n1p83

(cid:111) Cijan, A., Jenič, L., Lamovšek, A., & Stemberger, J. (2019). HOW THE WORKPLACE. Dynamic

# DIGITALIZATION CHANGES

# Relationships

# Management

Journal,

8(1),

3321.

https://doi.org/10.17708/drmj.2019.v08n01a01

(cid:111) Cios, K., Roman, S., Pedrycz, W., & Kurgan, L. (2007). Data mining: A knowledge discovery approach. In Springer eBooks. Springer New York,

NY. https://doi.org/10.1007/978-0-387-36795-8

(cid:111) Cote, C. (2021, November 2). WHAT IS PRESCRIPTIVE ANALYTICS? 6 EXAMPLES. Harvard Business School Online. Retrieved November 1,

## 2023, from https://online.hbs.edu/blog/post/prescriptive-analytics

(cid:111) Duan, L., & Xiong, Y. (2015). Big data analytics and business analytics. 1321.

# Journal

# of

# Management

Analytics,

2(1),

https://doi.org/10.1080/23270012.2015.1020891

(cid:111) Edwards, M. R., & Edwards, K. (2016). Predictive HR Analytics: Publishers.

# Mastering

# the

# HR Metric.

# Kogan

# Page

88

## https://abo.finna.fi/Record/abo_electronic_aa.9913645333205972?sid=

4080122552

(cid:111) Erdoğmuş, N., & Esen, M. (2011). An investigation of the effects of technology readiness on technology acceptance in e-HRM. Procedia -

# Social

# and

# Behavioral

Sciences,

24,

4873495.

https://doi.org/10.1016/j.sbspro.2011.09.131

(cid:111) Evans, J. (2017). Business Analytics. Pearson. (cid:111) Fabio. (n.d.). Sierra-Cedar 2018-2019 HRSystemsSurvey WhitePaper. from March

# Scribd.

# Retrieved

1,

2023,

## https://www.scribd.com/document/525117632/Sierra-Cedar-2018-

# 2019-HRSystemsSurvey-WhitePaper

(cid:111) Falletta, S. (2015). Point/counterpoint: Should companies have free rein to use predictive analytics. HRMagazine: On Human Resource

Management,

26327.

## https://www.researchgate.net/publication/340037599_Should_Compani

## es_Have_Free_Rein_to_Use_Predictive_Analytics

(cid:111) Ferrar, J., & Green, D. (2018). Excellence in People Analytics: How to Use Workforce Data to Create Business Value. Kogan Page Publishers.

## https://abo.finna.fi/Record/abo_electronic_aa.9913646199405972?sid=

2937807369 (cid:111) Fitz-enz, J.

## (2013). The new HR Analytics : Predicting

# the

EconomicValue of your company’s human capital

# investments.

AMACOM,

2010.

## https://ebookcentral.proquest.com/lib/abo-

# ebooks/reader.action?docID=533015

(cid:111) Gandomi, A. H., & Haider, M. (2015). Beyond the hype: Big data concepts, methods, and analytics. International Journal of Information

Management,

35(2),

1373144.

https://doi.org/10.1016/j.ijinfomgt.2014.10.007

## (cid:111) Giermindl, L., Strich, F., Christ, O., Leicht

# Deobald, U., & Redzepi, A.

(2021). The dark sides of people analytics: reviewing the perils for

‐

organisations and employees. European Journal of

# Information

Systems,

31(3),

4103435.

https://doi.org/10.1080/0960085x.2021.1927213

89

(cid:111) Guenole, N., Ferrar, J., & Feinzig, S. (2017). The Power of People: How Improve

## Successful Organizations Use Workforce Analytics To

# Business Performance. FT Press.

(cid:111) Harris, J. G., Craig, E., & Light, D. A. (2011). Talent and analytics: new approaches, higher ROI. Journal of Business Strategy, 32(6), 4313.

https://doi.org/10.1108/02756661111180087

(cid:111) HBR Analytic Services. (2014). HR Joins the Analytics Revolution. Harward Business Review. Retrieved December 13, 2023, from

## https://hbr.org/resources/pdfs/comm/visier/18765_HBR_Visier_Report_

# July2014.pdf

(cid:111) Hinawi, A. (2023). A Systematic Literature Review: Big Data Analytics Impact on Firm Performance [Master’s Thesis, Åbo Akademi University].

https://urn.fi/URN:NBN:fi-fe2023051544510

(cid:111)

Isson, J. P., & Harriott, J. S. (2016). People Analytics in the Era of Big

## Data: Changing the Way You Attract, Acquire, Develop, and Retain

# Talent.

# John

# Wiley

&

## https://abo.finna.fi/Record/abo_electronic_aa.9913446491805972?sid=

4080121451

(cid:111) Kapoor, B., & Sherif, J. S. (2012). Human resources in an enriched environment of business intelligence. Kybernetes, 41(10), 162531637.

https://doi.org/10.1108/03684921211276792

(cid:111) Khan, N., & Millner, D. (2020). Introduction to People Analytics: A to Data-driven HR. Kogan Page Publishers.

# Practical Guide

## https://abo.finna.fi/Record/abo_electronic_aa.9913646083805972?sid=

2937947946

(cid:111) Kose, M. A., & Sugawara, N. (2020, June 16). Understanding the depth of the 2020 global recession in 5 charts. World Bank. Retrieved October

## 15, 2023, from https://blogs.worldbank.org/opendata/understanding-

# depth-2020-global-recession-5-charts

(cid:111) Kumar, A. (2016). Learning Predictive Analytics with Python. Packt Ltd.

# Publishing

## https://abo.finna.fi/Record/abo_electronic_aa.9913617389705972?sid=

4080123848

90

# Sons.

(cid:111) Leonardi, P., & Contractor, N. (2018). Better People Analytics: Measure who they know, not just who they are. Harvard Business Review.

## https://hbr.org/2018/11/better-people-analytics

(cid:111) McCartney, S., & Fu, N. (2022). Promise versus reality: a systematic review of the ongoing debates in people analytics. Journal of

# Organizational

Effectiveness,

9(2),

2813311.

https://doi.org/10.1108/joepp-01-2021-0013

(cid:111) Miller, T. (2014). HR Analytics and Innovations in Workforce Planning Press. Business

# (1st

ed.).

# Expert

## https://abo.finna.fi/Record/abo_electronic_aa.9913514103105972?sid=

4080133394

(cid:111) Mularz, C. M., & Ülkü, M. A. (2014a). Analytics for nonprofits. In IGI Global eBooks (pp. 1153123). https://doi.org/10.4018/978-1-4666-5202-

6.ch012

(cid:111) Mularz, C. M., & Ülkü, M. A. (2014b). Analytics for nonprofits. In IGI Global eBooks (pp. 1153123). https://doi.org/10.4018/978-1-4666-5202-

6.ch012

## (cid:111) PAVANSUBHASH. (2014). IBM HR Analytics Employee Attrition & [Dataset].

# Performance

## https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-

# attrition-dataset

(cid:111) Pease, G. (2015). Optimize Your Greatest Asset -- Your People: How to Apply Analytics to Big Data to Improve Your Human Capital Investments.

# John

# Wiley

&

# Sons.

## https://abo.finna.fi/Record/abo_electronic_aa.9913463999705972?sid=

4080120293

(cid:111) Pease, G., Beresford, B., & Walker, L. (2014a). Developing Human Capital: Using Analytics to Plan and Optimize Your Learning and

# Development

# Investments.

# John

# Wiley

&

# Sons.

## https://abo.finna.fi/Record/abo_electronic_aa.9913465374605972?sid=

4080117353

(cid:111) Pease, G., Beresford, B., & Walker, L. (2014b). Developing human capital: Using Analytics to Plan and Optimize Your Learning and

## Development Investments. John Wiley & Sons.

91

(cid:111) Pease, G., Byerly, B., & Fitz-Enz, J. (2013). Human Capital Analytics: How to Harness the Potential of Your Organization’s Greatest Asset.

# John

# Wiley

&

# Sons.

## https://abo.finna.fi/Record/abo_electronic_aa.9913646932905972?sid=

4080131669

(cid:111) Peeters, T., Paauwe, J., & Van De Voorde, K. (2020). People analytics effectiveness: developing a framework. Journal of Organizational

Effectiveness, 7(2), 2033219. https://doi.org/10.1108/joepp-04-2020-

0071

(cid:111) Red Thread Research, Garr, S., & Mehrotra, P. (2020). People Analytics Tech 2020. Red Thread Research. Retrieved August 8, 2023, from

# https://redthreadresearch.com/wp-

## content/uploads/2020/12/RedThread_PAT2020_Final-1.pdf

(cid:111) Schiemann, W. A., Seibert, J. H., & Blankenship, M. H. (2017). Putting human capital analytics to work: Predicting and driving business

success. Human Resource Management,

57(3),

7953807.

https://doi.org/10.1002/hrm.21843

(cid:111) Sierra-Cedar. (2019, October 2). Sierra-Cedar 201932020 HR Systems Survey Findings: The Future of HR Technology. Sierra-Cedar. Retrieved

# November

6,

2023,

# from

## https://cdn.ymaws.com/www.clevelandshrm.com/resource/collection/09

E0F41E-BD60-41C0-A2FD-

## AAD4D5A44B59/The_Future_of_HR_Technology_Virtual_Learning-

# _February_2020_.pdf

(cid:111) Sivarajah, U., Kamal, M. M., Irani, Z., & Weerakkody, V. (2017). Critical analysis of Big Data challenges and analytical methods. Journal of

# Business

Research,

70,

2633286.

https://doi.org/10.1016/j.jbusres.2016.08.001

(cid:111) Someh, I. A., & Shanks, G. (2015). How business analytics systems provide benefits and Contribute to firm performance. European

## Conference on Information Systems. https://doi.org/10.18151/7217270

(cid:111) Soraya, S. (2018). Data Analytics and Big Data. John Wiley & Sons https://ebookcentral-proquest-

# Incorporated.

## com.ezproxy.vasa.abo.fi/lib/abo-ebooks/detail.action?docID=5401178.

92

(cid:111) Stubbs, E. (2011). The value of business analytics: Identifying the Path

# to Profitability. John Wiley & Sons.

(cid:111) Tursunbayeva, A., Di Lauro, S., & Pagliari, C. (2018). People analytics4 A scoping review of conceptual boundaries and value propositions.

# International Journal of

# Information Management, 43, 2243247.

https://doi.org/10.1016/j.ijinfomgt.2018.08.002

(cid:111) Van De Wetering, R., Mikalef, P., & Krogstie, J. (2018). BIG DATA IS POWER: BUSINESS VALUE FROM a PROCESS ORIENTED

## ANALYTICS CAPABILITY. Conference: 21st International Conference

# on

# Business

# Information

# Systems.

## https://www.researchgate.net/publication/327019980_BIG_DATA_IS_P

## OWER_BUSINESS_VALUE_FROM_A_PROCESS_ORIENTED_ANAL

# YTICS_CAPABILITY

(cid:111) Van Den Heuvel, S., & Bondarouk, T. (2017). The rise (and fall?) of HR analytics. Journal of Organizational Effectiveness, 4(2), 1573178.

https://doi.org/10.1108/joepp-03-2017-0022

(cid:111) Van Dooren, J. (2012). HR Analytics in practice. An overview of the influence of contingency factors on the applicability of HR analytics in

# Dutch

# organizations

# [Master’s

thesis,

# Tilburg University].

# https://arno.uvt.nl/show.cgi?fid=127276

(cid:111) Vihari, N., & Rao, M. K. (n.d.). Analytics as a Predictor for Strategic and Sustainable Human Resource Function: An Integrative Literature review.

# IIM

Calcutta,

Calcutta,

# India.

## https://www.researchgate.net/publication/272167423_Analytics_as_a_

## Predictor_for_Strategic_and_Sustainable_Human_Resource_Function

# _An_Integrative_Literature_Review

# (cid:111) Walford-Wright, G., & Scott

Jackson, W. (2018). Talent Rising; people

analytics and technology driving talent acquisition strategy. Strategic Hr

‐

Review, 17(5), 2263233. https://doi.org/10.1108/shr-08-2018-0071 (cid:111) Wamba, S. F., Gunasekaran, A., Akter, S., Ren, S. J. F., Dubey, R., & Childe, S. J. (2017). Big data analytics and firm performance: Effects of

## dynamic capabilities. Journal of Business Research, 70, 3563365.

https://doi.org/10.1016/j.jbusres.2016.08.009

93

(cid:111) Waters, S. D., Johnson-Murray, R., Streets, V. N., & McFarlane, L. (2015). The Practical Guide to HR Analytics: Using Data to Inform,

Transform,

# and

# Empower

# HR

# Decisions.

## https://abo.finna.fi/Record/abo_electronic_aa.9913557271305972?sid=

4080115895

94
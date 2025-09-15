# Digital Article / Strategy

How 3 Companies Are Using AI to Mimic Expert Judgement Advanced AI can learn how seasoned experts make decisions and perform tasks that used to require specialized knowledge. by Graham Kenny and Roger Moser

## Published on HBR.org / November 15, 2024 / Reprint H08GUL

# Jorg Greuel/Getty Images

You might not have heard of expert systems, but they’re already in

use in many ﬁelds including fault diagnosis, ﬁnance, and medicine.

In artiﬁcial intelligence (AI), an expert system is a computer program

that mimics the decision-making capabilities of a human expert. These

systems are built to address complex problems by reasoning through

Copyright © 2024 Harvard Business School Publishing. All rights reserved.

1

This document is authorized for use only by Matt O'Donnell (matthew.od11@gmail.com). Copying or posting is an infringement of copyright. Please contact customerservice@harvardbusiness.org or 800-988-0886 for additional copies.

## HBR / Digital Article / How 3 Companies Are Using AI to Mimic Expert Judgement

extensive knowledge bases, primarily using if-then rules instead of

# traditional procedural programming.

However, they haven’t up until recently made the widespread

impact expected on management decision-making. One reason is that

managerial contexts are much more in ﬂux than other applications.

Now, because of changes in technology and AI, expert systems are

becoming increasingly powerful. They can capture actual human

expertise with the level of ﬂexibility and adaptability required.

Here we explain how advanced AI is facilitating the transfer of expertise

## from humans to machines and back to humans like never before. We

examine three cases of where this has occurred and suggest how these

advances in technology could boost the eﬀectiveness of your strategic

decision making to improve competitiveness.

Evaluating high-return investment opportunities

A German venture capital organization that we’ll call Bavaria Ventures

is always on the lookout for ﬁnancially attractive startups. However, as

Josef, one of the business partners explains, “We’ve seen double-digit

growth in the number of applications we receive per analyst.” This has

put pressure on the company as the decision-making process involves

vetting each application. “It’s both time consuming and complex,”

Josef continues, “numerous contextual factors must be considered, and

personal judgement based on experience plays a huge role. But the

sheer volume of applications means that we must delegate the ﬁrst stage

# assessment to junior analysts.”

The problem is that the junior analysts simply don’t have the experience

to spot a potential winner and often overlook good proposals. This

happens even when they follow the decision-making template deﬁned

by Bavaria Ventures’ managing partners.

Copyright © 2024 Harvard Business School Publishing. All rights reserved.

2

This document is authorized for use only by Matt O'Donnell (matthew.od11@gmail.com). Copying or posting is an infringement of copyright. Please contact customerservice@harvardbusiness.org or 800-988-0886 for additional copies.

## HBR / Digital Article / How 3 Companies Are Using AI to Mimic Expert Judgement

What the company did: Bavaria Ventures wanted speedier and more

accurate assessments of startups based on what its managing partners

believed were the most promising ones. Rather than continue to train

junior analysts in the hope that they’d transfer the company’s decision-

making template into accurate assessments, Bavarian Ventures turned

to producing a hybrid expert system which it labelled AI-4-VC. “The

ﬁrst step,” says Josef, “was to turn to a university for help in developing

a solution that facilitated a faster and more accurate ranking of

startup applications.” This was designed to mimic how an experienced

managing partner of Bavaria Ventures went about assessing a startup’s

# attractiveness in the ﬁrst round.

According to Josef, the tool was developed through a combination of

machine learning (speciﬁcally, a “random forest” algorithm that uses

decision trees to make predictions) and deep learning in the form of

natural language processing.He explained how it works. “The solution

ranks applications according to their ﬁt with what we’re looking for. A

senior analyst periodically reviews the results to see if he or she wishes

to overrule the algorithm. If the senior analyst does, then this is taken

in by the algorithm and the weighting of criteria is adjusted. The expert

system implements any change in preferences among the managing

# partners in almost real-time.”

Results: After a period, the AI-4-VC replaced some of the junior

analysts and minimized the time spent on low-ﬁt applications. This

assisted Bavaria Ventures to respond faster to the applications from

startups with the most promising potential. They also discovered that

their AI-4-VC solution was accurate even with relatively small-size

# datasets of applications.

How to do it yourself: A professional with a basic knowledge of

machine learning will be able to put a system like this together. Major

Copyright © 2024 Harvard Business School Publishing. All rights reserved.

3

This document is authorized for use only by Matt O'Donnell (matthew.od11@gmail.com). Copying or posting is an infringement of copyright. Please contact customerservice@harvardbusiness.org or 800-988-0886 for additional copies.

## HBR / Digital Article / How 3 Companies Are Using AI to Mimic Expert Judgement

tech companies now oﬀer platforms that make it easy to combine

machine learning with natural language processing (NLP) to build

your own expert system. If you’re looking for ﬂexibility and scalability,

## platforms like Google Cloud AI Platform, Amazon SageMaker, or Azure

Machine Learning are great options. For faster prototyping or if you’re

focused on NLP, tools like Hugging Face or Colab are most likely a better

# ﬁt.

Coping with excessive customer demands

An Indian satellite data analytics company that we’ll call Sat Vista

Analytics oﬀers “decision intelligence from space.” As Rohan, the company’s Chief Technology Oﬃcer describes, “We provide results for

banks to assess possible loans to small-hold farmers by understanding

how much each farmer is likely to earn. We also assist agribusinesses

to establish contracts and set prices of their own products [cocoa, rice,

wheat] based on likely crop yields.”

However, Sat Vista Analytics has struggled with overload from the

number of analyses demanded by its clients. These analyses required

the company’s remote sensing specialists to perform multiple tasks

ranging from data preprocessing and spectral signature analysis to the

# interpretation of vegetation indices.

What the company did: The company’s executives analyzed the

situation and decided that classic process automation based on ﬁxed

rules wouldn’t work. So, as Rohan explains, “We decided to create

‘analysis avatars,’” which are AI-based clones of their best specialists.

This involved monitoring the data analysis practices of the company’s

best remote sensing specialists and turning these behavioral patterns

# into a set of rules (algorithms).

Copyright © 2024 Harvard Business School Publishing. All rights reserved.

4

This document is authorized for use only by Matt O'Donnell (matthew.od11@gmail.com). Copying or posting is an infringement of copyright. Please contact customerservice@harvardbusiness.org or 800-988-0886 for additional copies.

## HBR / Digital Article / How 3 Companies Are Using AI to Mimic Expert Judgement

But crucially, the algorithms were based on observing the specialist’s

data processing decisions, not on rules provided by the specialist

themselves. That’s because people often aren’t all that great at

explaining how they make decisions. Rohan spelled out how this

works. “Instead of asking each specialist about their preferred ways

of treating, analyzing and interpreting satellite data to create a set

of recommendations, we monitored what each specialist actually did

with the diﬀerent data sets.” The analysis avatar started out with a

simple machine-learning based approach and continued to become

more complex as more data points about the specialists’ behavior were

collected.

Results: Today, the analysis avatars can mimic the data treatment

behavior of the company’s best remote sensing specialists to a level

of precision, recall, and accuracy that meets most simple application

demands. This has left the human specialists to focus on new or more

complicated tasks. Moreover, inexperienced remote sensing specialists

joining the company fresh from university can learn the company’s best

practices without distracting its human experts.

How to do it yourself: Look for existing AI platforms that enable AI

models to capture and replicate expert decision-making patterns

automatically through observation. Your ideal platform should support

continuous learning and real-time data processing. This will enable

your AI system to evolve as new data is gathered, thus making

intelligent decisions based on expert behavior without relying on

predeﬁned rules.

Upskilling R&D for competitive advantage

An Australian company that we’ll call Be Smarter wanted to improve the

problem-solving skills of its R&D employees to boost competitiveness.

Copyright © 2024 Harvard Business School Publishing. All rights reserved.

5

This document is authorized for use only by Matt O'Donnell (matthew.od11@gmail.com). Copying or posting is an infringement of copyright. Please contact customerservice@harvardbusiness.org or 800-988-0886 for additional copies.

## HBR / Digital Article / How 3 Companies Are Using AI to Mimic Expert Judgement

They considered developing online training courses to upgrade their

employees’ R&D skills and problem-solving methods.

However, as Leo, Head of R&D, pointed out, “We soon realized that the

administrative eﬀort required, the cost involved and the need to achieve

alignment with diﬀerent training needs presented serious obstacles.”

What the company did: Be Smarter adopted a more ﬂexible approach.

This involved AI agents, each representing a speciﬁc type of expertise.

As Leo explains, “The agents can interpret and generate human-like text

to carry out a wide range of functions, such as explaining concepts,

answering questions or providing speciﬁc recommendations.” The

agent is ﬂexible and can deliver modules when the employee needs

them or skip over content when it’s not required.

R&D employees can use diﬀerent agents as assistants to help them

look at a given problem from an unusual perspective. Leo provided

a case where “an R&D employee facing a technological challenge can

choose multiple AI agents to help them with a technical explanation,

a fresh perspective, or instructions about how to tackle the problem

from a diﬀerent angle.” For example, an R&D employee facing a mining

technology problem can choose a software testing agent, a geology

agent, or a machinery agent to help them.

When selecting agents, R&D employees regularly asked themselves

which agents are most suitable in helping them with their type of

problem. So, Be Smarter decided to install a rating system for employees

to provide feedback on the usefulness of an AI agent for diﬀerent types

# of problems.

Results: The AI agents assisted R&D employees to access the most

suitable technological or problem-solving expertise when needed. This

Copyright © 2024 Harvard Business School Publishing. All rights reserved.

6

This document is authorized for use only by Matt O'Donnell (matthew.od11@gmail.com). Copying or posting is an infringement of copyright. Please contact customerservice@harvardbusiness.org or 800-988-0886 for additional copies.

## HBR / Digital Article / How 3 Companies Are Using AI to Mimic Expert Judgement

is based on their peers’ recommendations of which agents were most

## helpful for which type of problem – a recommender system. This

lowered the personal training costs and boosted the eﬀectiveness of the

support oﬀered.

How to do it yourself: If you’re seeking to enhance your problem-

solving capabilities, consider implementing AI agents that represent

speciﬁc areas of expertise. Review the growing number of AI-based

platforms for creating agentic systems that can capture diverse expert

## knowledge. These process complex queries and interact with users as

if guided by human experts. Focus on creating a ﬂexible system where

your employees can choose agents tailored to their immediate needs

allowing for personalized learning and assistance

. . .

Today, you can integrate advanced AI technologies to transform how

expertise is transferred and utilized within your organization. AI agents

can now support dynamic decision-making systems that adapt in near

real-time, oﬀering you more ﬂexibility and responsiveness in strategic

# decision-making.

Instead of relying on static expert systems, ensure your decision-making

support algorithms are designed to be continuously updated through

feedback. This enables you to stay agile and make more informed

decisions as conditions evolve. The beauty of advanced AI is its

ﬂexibility to incorporate changes on the ﬂy.

As AI continues to evolve, you should proactively explore how

these advances can be integrated into your strategic decision-making

processes. This will help you drive innovation, ensuring that your

business remains competitive in a rapidly-changing environment.

This article was originally published online on November 15, 2024.

Copyright © 2024 Harvard Business School Publishing. All rights reserved.

7

This document is authorized for use only by Matt O'Donnell (matthew.od11@gmail.com). Copying or posting is an infringement of copyright. Please contact customerservice@harvardbusiness.org or 800-988-0886 for additional copies.

## HBR / Digital Article / How 3 Companies Are Using AI to Mimic Expert Judgement

Graham Kenny is the CEO of Strategic Factors and author of Strategy Discovery. He is a recognized expert in strategy and performance measurement who helps managers, executives, and boards create successful organizations in the private, public, and not-for-proﬁt sectors. He has been a professor of management in universities in the U.S. and Canada.

# RM

Roger Moser serves on the faculty at Macquarie University, IIM Udaipur, and the University of St. Gallen, specializing in Decision Intelligence and Digital Business Model Innovation. With a focus on the intersection of advanced digital technologies and business strategy, he frequently advises industry leaders and policymakers on leveraging these technologies to enhance organizational decision-making. He authors a monthly newsletter, Decision Model Innovation, where he explores cutting-edge trends in this evolving ﬁeld.

Copyright © 2024 Harvard Business School Publishing. All rights reserved.

8

This document is authorized for use only by Matt O'Donnell (matthew.od11@gmail.com). Copying or posting is an infringement of copyright. Please contact customerservice@harvardbusiness.org or 800-988-0886 for additional copies.
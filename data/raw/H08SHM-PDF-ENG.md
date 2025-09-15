## Digital Article / AI and Machine Learning

What Gets Measured, AI Will Automate Smart leaders must bet on the unmeasurable: taste, trust, experiences, and the yet-unknown. by Christian Catalini, Jane Wu, and Kevin Zhang

## Published on HBR.org / June 19, 2025 / Reprint H08SHM

# Eugene Mymrin/Getty Images

AI doesn’t need a sci-ﬁ upgrade to upend the economy—current

models, and the cheaper, more capable versions already in the pipeline,

are set to disrupt nearly every corner of the labor market. Their

## surprising performance across text, image, and video threatens to

upend how work is done across the creative ranks of writers, designers,

## photographers, architects, animators, and brand advertisers, as well as

the spreadsheet crowd of ﬁnancial analysts, consultants, accountants,

Copyright © 2025 Harvard Business School Publishing. All rights reserved.

1

This document is authorized for use only by Matt O'Donnell (matthew.od11@gmail.com). Copying or posting is an infringement of copyright. Please contact customerservice@harvardbusiness.org or 800-988-0886 for additional copies.

## HBR / Digital Article / What Gets Measured, AI Will Automate

and tax preparers. Not even the credentialed bastions of law, medicine,

or academia are safe: AI can sift through oceans of content and serve

## up bespoke advice or coursework at a fraction of today’s cost—and with

quality that’s closing in fast.

There are major questions about how much more powerful AI tools

might become—and how soon. Anthropic’s Dario Amodei and OpenAI’s

Sam Altman claim artiﬁcial general intelligence (AGI) could be only

a year or two away. Meta’s Yann LeCun is more skeptical, arguing

that current models lack grounded physical understanding, durable

## memory, coherent reasoning, and strategic foresight, and Apple just

published new research claiming that today’s models perform only

within the limits of their training data. Yet even if progress stopped

tomorrow, the disruption is already underway.

To navigate this new landscape, leaders need to understand—and

plan for—how automation will aﬀect their businesses. That requires

understanding which tasks and responsibilities are most likely to come

under pressure and charting a course to move the enterprise up the

intelligence value chain before time runs out.

# What Is Not at Risk of Automation?

Academic researchers and practitioners have extensively debated which

jobs and tasks are most vulnerable to automation. Some threats are

obvious: self-driving vehicles may soon be in a position to displace

## millions of ride-sharing, bus, and truck drivers. Meanwhile, language

## translation, swaths of creative writing, design, and even everyday

coding are being handed oﬀ to AI.

In February, Anthropic shared revealing user stats: although the chat

format naturally steers people toward human augmentation, about 43%

of interactions already represented some form of automation, in which

Copyright © 2025 Harvard Business School Publishing. All rights reserved.

2

This document is authorized for use only by Matt O'Donnell (matthew.od11@gmail.com). Copying or posting is an infringement of copyright. Please contact customerservice@harvardbusiness.org or 800-988-0886 for additional copies.

## HBR / Digital Article / What Gets Measured, AI Will Automate

users ask the AI to perform a task directly as opposed to helping

them iterate and think it through. That share will keep climbing as

modular AI agents enter the workforce, trading data and coordinating

tasks through protocols like MCP. Environments that are extensively

measured or codiﬁed—whether through laws, tax codes, compliance

## protocols, or streams of sensor data—face the greatest near-term risk of

being handed over to machines.

## AI research pioneers Ajay Agrawal, Joshua Gans, and Avi Goldfarb

argued in 2018 that as AI advances, the last bastion of human advantage

will be judgment—the ability to weigh options and make decisions

## under uncertainty. Yet that insight hands us an impossible homework

assignment: pinning down exactly what qualiﬁes as judgment at any

given moment.

Tasks that demand human judgment today—choosing a medical

treatment, reviewing a legal contract, scripting a ﬁlm that nails the

## zeitgeist—could soon pass to AI as models tap richer data and greater

compute. Nor can we assume people will always prefer a human

therapist, counselor, or mediator, according to recent research. An AI

counterpart can operate around the clock, at a fraction of the cost, and

## —aside from a handful of human superstars—may oﬀer more consistent

# quality.

So, how can we separate the tasks AI will automate next from those that

will require new breakthroughs in AI technology to do so? To answer

that, we must go back to ﬁrst principles and revisit where it all began.

## From Lab Contest to Industrial Revolution

Back in the mid-2000s, computer scientist Fei-Fei Li saw that the ﬁeld of

computer vision, which is focused on enabling computers to “see” and

interpret images, was dealing with a bottleneck: algorithms were pixel-

Copyright © 2025 Harvard Business School Publishing. All rights reserved.

3

This document is authorized for use only by Matt O'Donnell (matthew.od11@gmail.com). Copying or posting is an infringement of copyright. Please contact customerservice@harvardbusiness.org or 800-988-0886 for additional copies.

## HBR / Digital Article / What Gets Measured, AI Will Automate

starved, ingesting too little visual data to reach human performance.

Her solution was refreshingly brute-force: she built ImageNet—a vast,

meticulously labeled image trove assembled with help from Amazon

Mechanical Turk. But her true stroke of genius came in 2010, when

she bolted a global leaderboard onto the dataset—transforming image

## recognition into a gladiatorial contest for researchers.

For two years, the annual leaderboard inched forward.

## Then, in 2012, Alex Krizhevsky, Ilya Sutskever, and Geoﬀrey Hinton

blew the competition away. Using two oﬀ-the-shelf NVIDIA GTX 580

graphics cards, the trio from Toronto was able to train a breakthrough

convolutional neural network in just a few days—a groundbreaking

approach that proved you could bend computer-vision history on a grad

# student budget.

That moment ended the decades-long AI winter, put neural nets at the

center of progress, and revealed the playbook the ﬁeld still runs on.

First, gather relevant data—roughly 14 million labeled images in the

ImageNet case. Next, rely on metrics to quantify and drive progress.

Last, ﬂood a model with data and GPU muscle until it teaches itself, a

formula that has carried AI from categorizing objects to writing ﬂuent

prose and, most recently, to reasoning, planning, and wielding external

tools in today’s emerging “thinking” systems.

# Data, Reward, Compute

The framework that propelled the image recognition breakthrough is far

more general than most realize. It can be invoked whenever we can a)

deﬁne the task environment and assemble its data—be it a corpus of

text, a repository of images and video, logged driving miles, or streams

from a robot’s sensors; b) specify a target reward, explicit (“did the

model predict the next word?”) or implicit (inferred from observing

Copyright © 2025 Harvard Business School Publishing. All rights reserved.

4

This document is authorized for use only by Matt O'Donnell (matthew.od11@gmail.com). Copying or posting is an infringement of copyright. Please contact customerservice@harvardbusiness.org or 800-988-0886 for additional copies.

## HBR / Digital Article / What Gets Measured, AI Will Automate

human behavior); and c) provide the computational power to let the

# system iterate.

Stack those three ingredients and you get a general-purpose automation

engine. Two data trends now accelerate the ﬂywheel. First, models

can mint limitless synthetic examples—for instance, generating virtual

“driving miles” that cover every oddball scenario, rather that relying

on data from real world drivers. And second, AI is increasingly

ﬁelded across a variety of devices and sensors—on phones, in cars,

and elsewhere—as a low-cost surveyor, capturing and quantifying real-

world signals that were once too expensive or impractical to measure.

If you can shoehorn a phenomenon into numbers, AI will learn it and

reproduce it back at scale—and the tech keeps slashing the cost of that

conversion, so measurement gets cheaper, faster, and quietly woven

into everything we touch. More things become countable, the circle

resets, and the model comes back for seconds. That means that any job

that can be measured can, in theory, be automated.

# Measurement Too Cheap to Meter

Economist Zvi Griliches’s landmark 1957 study of hybrid corn adoption

gives us a sharp lens on what comes next. Farmers ﬁrst planted the

## pricey seed only on their best acres—where the yield jump easily

covered the extra cost and learning curve of using a new product.

As hybrids improved and word spread, even thin-margin ﬁelds soon

cleared the beneﬁt-cost bar. With AI, the investment into measuring

things follows the same payoﬀ curve. When turning reality into data is

expensive, companies tend to only invest in the headline cases—credit-

## card fraud, algorithmic market-making, jet-engine prognostics.

But AI now slashes the cost of precise measurement, making

continuous, ﬁne-grained sensing the default. Lightweight models run

Copyright © 2025 Harvard Business School Publishing. All rights reserved.

5

This document is authorized for use only by Matt O'Donnell (matthew.od11@gmail.com). Copying or posting is an infringement of copyright. Please contact customerservice@harvardbusiness.org or 800-988-0886 for additional copies.

## HBR / Digital Article / What Gets Measured, AI Will Automate

beside the sensors, trimming bandwidth and latency, while synthetic

data ﬁlls gaps when the real world is slow or awkward to capture.

Each extra decimal place quickly pays for itself: tiny error cuts

multiplied across millions of AI-driven decisions add up fast. As precise

measurement gets cheaper, ever-slimmer beneﬁt streams pencil out,

and tasks once too minor to monitor slide into the automation net.

Not only may we soon have intelligence too cheap to meter, we’ll also

be measuring ever more of the world to expand—and continuously

upgrade—what that intelligence can reach. We already live in the era

of “artiﬁcial-metrics intelligence,” where anything we can quantify is

swiftly queued for automation.

# Thriving Despite Unknown Unknowns

Humans are evolutionary generalists, selected to navigate half-drawn

maps. We don’t merely survive unknown unknowns—we thrive on

them, and that resilience is our deﬁning edge. Over countless

generations we ﬁne-tuned our vocal cords and social brains until

language emerged—opening the door to cumulative knowledge,

abstract reasoning, and symbolic thought. From there we pushed

beyond our biological limits, forging tools that stretched our senses,

expanded our memory, and multiplied our abilities.

But the cornerstone of our advantage is our highly plastic, densely

wired prefrontal cortex. This neural command center lets us spin

## endless “what-ifs,” rehearse counterfactual futures, and pivot strategy

the instant conditions shift. Short of a true singularity, even quantum

machines will struggle to match our talent for open-ended, cross-

# domain counterfactual planning.

As AI accelerates progress, it creates fresh unknown unknowns, so our

maps keep being redrawn. Meanwhile, it routinizes the predictable—

Copyright © 2025 Harvard Business School Publishing. All rights reserved.

6

This document is authorized for use only by Matt O'Donnell (matthew.od11@gmail.com). Copying or posting is an infringement of copyright. Please contact customerservice@harvardbusiness.org or 800-988-0886 for additional copies.

## HBR / Digital Article / What Gets Measured, AI Will Automate

much as mechanized farming lifted us from subsistence—freeing more

## of our counterfactual brainpower for higher-level problems.

AI will also struggle in domains where measurement verges on the

impossible—witness the decade-long, globe-spanning eﬀort the Event

Horizon Telescope needed to capture a single black-hole image, and

the still-unsolved challenges of probing extreme-scale physics, Earth’s

## deep mantle and abyssal oceans, or live cellular interactions inside the

human brain. It will also lag where measurement is throttled by privacy,

ethics, or regulation; where society requires transparent reasoning—

at least until model interpretability catches up; and where people

simply prefer a human touch. Yet, as with hybrid corn adoption, future

generations will keep revisiting the cost-beneﬁt calculus for each of

these—and may reach conclusions very diﬀerent from ours.

But one crucial carve-out in what can be measured may prove

## decisive: tasks that defy quantiﬁcation because their outcome odds

are fundamentally unknowable—the realm of Knightian uncertainty,

where you can’t assign any probabilities because the risks themselves

are undeﬁned. Scaling a startup, allocating capital or talent into highly

uncertain ventures, containing a novel pathogen, setting central bank

policy during a ﬁnancial regime shift, drafting AI ethics, inventing

a new artistic medium, igniting a fashion trend, or creating a new

genre-bending blockbuster—all sit in zones where probabilities vanish.

Some creative acts and discoveries amount to little more than clever

## recombinations of the familiar, but the truly ambitious hinge on our

singular ability to envision genuinely new and complex counterfactual

# worlds.

The list is ﬂuid—tasks drop oﬀ the moment they become measurable,

and new ones surface just as quickly. Each shift forces painful economic

and social adjustments, squeezing more work into a superstar economy

Copyright © 2025 Harvard Business School Publishing. All rights reserved.

7

This document is authorized for use only by Matt O'Donnell (matthew.od11@gmail.com). Copying or posting is an infringement of copyright. Please contact customerservice@harvardbusiness.org or 800-988-0886 for additional copies.

## HBR / Digital Article / What Gets Measured, AI Will Automate

that concentrates outsized rewards at the peaks of creativity, talent, and

capital. Yet AI oﬀers a paradoxical gift: by democratizing education and

serving as everyone’s personal copilot, it hands more people than ever

the tools to reach those peaks. Jobs themselves will keep evolving, and

any breakthrough that turns the unknown into the countable will scale

and be imitated at meme speed.

For leaders steering their organizations through this turbulent

transition, what lies beyond the spreadsheet? It’s everything that won’t

ﬁt in a cell: the skills that refuse to be tallied, the open-ended problems

## with no reliable precedent, the intangibles—trust, taste, and the subtle

dimensions of quality and experience—and the conviction to press

ahead even when every metric says “wait.” Manage only what you can

measure, and you surrender the most valuable ground to rivals who

cultivate what can’t be counted. Amar Bose, the sound and electrical

engineer who founded the Bose Corporation, proved the point: while

others worshipped spec-sheet numbers, he zeroed in on how music

sounded to people in real rooms—a quality no existing metric could

catch—and in doing so, he rewrote the rules of the audio industry.

Directionally, the prescription is simple. Back wildcard bets with

fuzzy ROI, reward teams that reframe problems and lean into the

unknown, and rotate talent through roles that confront uncertainty

## across R&D, new markets, and complex customer, partner, and policy

interactions. Carve out slack time and engineer cross-team collisions

to spark serendipity and idea recombination. Treat those pockets of

planned ambiguity not as liabilities, but as strategic assets.

Only leaders who pay attention to what is measurable—and, more

crucially, to what stubbornly isn’t—will be ready when the next shift

# arrives.

This article was originally published online on June 19, 2025.

Copyright © 2025 Harvard Business School Publishing. All rights reserved.

8

This document is authorized for use only by Matt O'Donnell (matthew.od11@gmail.com). Copying or posting is an infringement of copyright. Please contact customerservice@harvardbusiness.org or 800-988-0886 for additional copies.

## HBR / Digital Article / What Gets Measured, AI Will Automate

# CC

Christian Catalini is the founder of the MIT Cryptoeconomics Lab and a research scientist at MIT. He is also co-founder and Chief Strategy Oﬃcer of Lightspark. Previously, he was co-creators of Libra and Chief Economist of the Libra Association. Christian Catalini advises a number of crypto companies, including Coinbase. He is also a member of the U.S. Commodity Futures Trading Commission’s Technology Advisory Committee.

# JW

Jane Wu is an Assistant Professor of Strategy at UCLA where she conducts research at the intersection of innovation, entrepreneurship, and strategy. Her current work focuses on the role of metrics in shaping ﬁrm innovation. She also studies the entrepreneurial strategy choices that high-growth startup founders encounter.

# KZ

Kevin Zhang is a Staﬀ Machine Learning Engineer at Lightspark, focusing on strategic AI projects. He is also the creator of Inference Grid, a decentralized network for AI inference. Previously, Kevin served as a Senior Software Engineer for Ads Core ML at Meta.

Copyright © 2025 Harvard Business School Publishing. All rights reserved.

9

This document is authorized for use only by Matt O'Donnell (matthew.od11@gmail.com). Copying or posting is an infringement of copyright. Please contact customerservice@harvardbusiness.org or 800-988-0886 for additional copies.
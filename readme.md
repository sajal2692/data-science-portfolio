# Data Science Portfolio

> These are data-science projects I built early in my career (around 2016). If you're starting out — learning the fundamentals or putting together your own portfolio — I hope you find them a useful reference. As of 2026 I've refreshed the whole repository so every notebook still runs top-to-bottom on a current **Python 3.14** stack. For my current work in AI engineering (LLM agents, RAG, and applied ML), see **[sajalsharma.com](https://sajalsharma.com)**.

A collection of data-science projects — completed for academic, self-learning, and hobby purposes — presented as Jupyter notebooks, plus a few R analyses published on RPubs.

_Data used in these projects (under `data/`) is for demonstration purposes only._

## Running the notebooks

The project uses [uv](https://github.com/astral-sh/uv) for environment management (Python 3.14):

```bash
uv sync
uv run jupyter lab
```

Or with pip:

```bash
pip install -r requirements.txt
```

Most notebooks read the small datasets under `data/`. Two fetch their data on first run and cache it: the digit-recognition notebook downloads MNIST via `torchvision`, and the stock-market notebook pulls tech-stock prices via `yfinance` (with a vendored snapshot as a fallback).

## Contents

- ### Machine Learning

	- [Predicting Boston Housing Prices](https://github.com/sajal2692/data-science-portfolio/blob/main/boston_housing/boston_housing.ipynb): Building and tuning a decision-tree regressor to predict home values, and evaluating how reliable those predictions are. (Includes a note on the Boston dataset's history and why it was retired from scikit-learn.)
	- [Supervised Learning: Finding Donors for CharityML](https://github.com/sajal2692/data-science-portfolio/blob/main/finding_donors/finding_donors.ipynb): Comparing several supervised learning algorithms to predict whether an individual earns more than $50,000 a year, to help a fictional charity identify likely donors.
	- [Unsupervised Learning: Creating Customer Segments](https://github.com/sajal2692/data-science-portfolio/blob/main/customer_segments/customer_segments.ipynb): Using PCA and Gaussian-mixture clustering to uncover structure in the annual spending of wholesale customers.
	- [Reinforcement Learning: Training a Smartcab to Drive](https://github.com/sajal2692/Training-a-Smartcab-to-Drive): Creating an optimized Q-Learning driving agent that navigates a Smartcab through its environment towards a goal.
	- [Deep Learning: Digit Sequence Recognition with a CNN](https://github.com/sajal2692/data-science-portfolio/blob/main/digit_recognition-mnist-sequence.ipynb): A PyTorch convolutional network that reads sequences of 1-5 digits from a single image, using five classification heads on a shared convolutional trunk and synthetic data built from MNIST.

	_Tools: PyTorch, scikit-learn, Pandas, Seaborn, Matplotlib, Pygame_

- ### Natural Language Processing

	- [Disaster Message Classifier](https://github.com/sajal2692/disaster-message-classifier): A multilabel classification model to predict the categories of a disaster message. Includes an ETL pipeline, an ML pipeline, and a web app to classify messages. _Tools: NLTK, Scikit-learn, XGBoost, Flask, Plotly_
	- [3-way Sentiment Analysis for Tweets](https://github.com/sajal2692/data-science-portfolio/blob/main/3-Way%20Sentiment%20Analysis%20for%20Tweets.ipynb): 3-way polarity (positive, negative, neutral) classification of tweets from hand-built features and a logistic-regression classifier — with a modern zero-shot transformer baseline (twitter-roberta) alongside for comparison.
	- [Cross Language Information Retrieval](https://github.com/sajal2692/data-science-portfolio/blob/main/Cross%20Language%20Information%20Retrieval.ipynb): A CLIR system which, given a query in German, searches text documents written in English — with IBM Model 1 alignment and a BM25 / language-model scorer built from scratch.
	- [Yelp Review Classification](https://github.com/sajal2692/data-science-portfolio/blob/main/Yelp%20Review%20Classification.ipynb): Classifying 1-star vs 5-star Yelp reviews from their text with a bag-of-words Naive Bayes model.
	- [SMS Spam Classification](https://github.com/sajal2692/data-science-portfolio/blob/main/SMS%20Spam%20Classification.ipynb): Classifying SMS messages as spam or ham with a TF-IDF + Naive Bayes pipeline.

	_Tools: NLTK, scikit-learn, transformers_

- ### Data Analysis and Visualisation
	- __Python__
		- [Scalable Walkability Analysis of Melbourne](https://github.com/sajal2692/Scalable-Walkability-Analysis-of-Melbourne): Analysis of walkability of suburbs in Melbourne, Victoria and its implications.
		- [Titanic Dataset - Exploratory Analysis](https://github.com/sajal2692/data-science-portfolio/blob/main/Titanic%20Dataset%20-%20Exploratory%20Analysis.ipynb): Exploratory analysis of the passengers onboard RMS Titanic using Pandas and Seaborn visualisations.
		- [Stock Market Analysis for Tech Stocks](https://github.com/sajal2692/data-science-portfolio/blob/main/Stock%20Market%20Analysis%20for%20Tech%20Stocks.ipynb): Analysis of technology stocks including price over time, daily returns, correlation, and a Monte Carlo value-at-risk simulation.
		- [2016 US General Election Poll Data Analysis](https://github.com/sajal2692/data-science-portfolio/blob/main/2016%20General%20Election%20Poll%20Analysis.ipynb): A simple analysis of 2016 US General Election poll data (recovered from the Internet Archive).
		- [911 Calls - Exploratory Analysis](https://github.com/sajal2692/data-science-portfolio/blob/main/911%20Calls%20-%20Exploratory%20Analysis.ipynb): Exploratory data analysis of the 911-calls dataset from Kaggle, demonstrating feature extraction from raw variables.

	_Tools: Pandas, Seaborn, Matplotlib, yfinance_

	- __R__ (published on RPubs)
		- [Behavioral Risk Factor Surveillance System (BRFSS) 2013: Exploratory Data Analysis](https://rpubs.com/sajal_sharma/brfss2013): Exploratory analysis of the BRFSS-2013 data set, investigating the relationships between education and eating habits, sleep and mental health, and smoking, drinking and general health.
		- [Inferential Statistics: Do men or women oppose sex education?](https://rpubs.com/sajal_sharma/inferential_statistics): Using the GSS (General Social Survey) dataset to infer whether, in 2012, men in the United States were more likely than women to oppose sex education in public schools.
		- [Data Visualization: Corruption and Human Development](https://rpubs.com/sajal_sharma/corruption_viz): A scatter plot of the relationship between the Human Development Index and the Corruption Perceptions Index of countries.
		- [Moneyball: Analysing and replacing lost players](https://rpubs.com/sajal_sharma/moneyball_lost_players): Exploration of 2001 baseball data to find replacements for key players lost by the Oakland A's. Inspired by the book/movie Moneyball.

- ### Micro Projects

	- __Python__ — short, focused scikit-learn exercises:
		- [Linear Regression](https://github.com/sajal2692/data-science-portfolio/blob/main/ML%20Micro%20Projects/Machine%20Learning%20with%20Linear%20Regression.ipynb): Predicting an e-commerce customer's yearly spend, and interpreting the coefficients.
		- [Logistic Regression](https://github.com/sajal2692/data-science-portfolio/blob/main/ML%20Micro%20Projects/Machine%20Learning%20with%20Logistic%20Regression.ipynb): Predicting whether an internet user clicked an ad.
		- [K-Nearest Neighbours](https://github.com/sajal2692/data-science-portfolio/blob/main/ML%20Micro%20Projects/ML%20with%20K%20Nearest%20Neighbors.ipynb): Classifying instances into two target classes, choosing K by cross-validation.
		- [Support Vector Machines](https://github.com/sajal2692/data-science-portfolio/blob/main/ML%20Micro%20Projects/ML%20with%20Support%20Vector%20Machines.ipynb): Classifying the iris dataset with a grid-searched SVM.
		- [Decision Trees and Random Forests](https://github.com/sajal2692/data-science-portfolio/blob/main/ML%20Micro%20Projects/Machine%20Learning%20with%20Decision%20Trees%20and%20Random%20Forests.ipynb): Predicting whether a borrower repays their loan, using publicly available LendingClub data.
		- [Movie Recommendations with Recommender Systems](https://github.com/sajal2692/data-science-portfolio/blob/main/ML%20Micro%20Projects/Recommender%20Systems%20with%20Python.ipynb): Item-item movie recommendations from user-rating similarities.

	- __R__ (RPubs)
		- [ML Logistic Regression](https://rpubs.com/sajal_sharma/micro_logistic): Predicting salary class using logistic regression.
		- [ML Decision Trees and Random Forests](https://rpubs.com/sajal_sharma/micro_dt_rf): Classifying schools as private or public.

---

The full R portfolio index is [here](https://rpubs.com/sajal_sharma/).

Questions or collaboration? Reach me at contact@sajalsharma.com, or see what I am working on now at [sajalsharma.com](https://sajalsharma.com).

### Support

If this repo helped you or gave you ideas for your own portfolio, you can [buy me a coffee](https://buymeacoffee.com/sajals). ❤️

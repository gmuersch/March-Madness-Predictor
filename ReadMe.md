# March Madness Predictor 

The aim of this project is to use machine learning models to predict sports games

With sports betting moving through legislation to be legalized in more and more states, the market for it will grow and
having an edge like this would give a massive advantage over the average better.

In this version I will be predicting and filling out NCAA March Madness Tournament brackets using a logistic regression model

I have collected data on 353 teams and over 11,000 basketball games. I used this data to train a logistic regression model using python's sklearn package. Once the model was trained I used it to predict the 2019 March Madness tournament. 

The model achieved an accuracy score of 77.25% and correctly predicted the winning team of the 2019 tournament.

All data was scraped from https://www.sports-reference.com/


**relevant packages**
Beautifulsoup, pandas, matplotlib, pickle, csv, requests, numpy and sklearn


This project contains 6 files, I will briefly discuss the purpose of each below:

**functions.py**

This file holds all the functions I created to complete this project. Since some of the functions were needed in multiple scripts, I found it easiest to put them all here and import them when necessary.


**Data_Scraper.py:**

In this file I used the ncaa_scrape_teams and ncaa_reg_season_scraper functions to gather the stats of all available basketball teams and all regular season game results. They were saved to csv files to be used later


**Exploratory_Analysis.ipynb:**

This jupyter notebook explores and cleans up the collected data sets and conducts some analysis to aid in feature selection


**Regression_Model.ipynb**

In this notebook I used the cleaned up data set to train a logistic regression model and test the accuracy score


**NCAA_predict.py:**

This script calls the predict_tournament function to predict the 2019 tournament with the model I trained


**Bracket_Games19.csv:**

This file holds the predicted results of the tournament. To run the model for your self, delete all the games after the first round and enter the path into the predict_tournament functions


## Tournament Results and Statistics:

### Round of 64: 

**The Model** predicted the winner **71.875%** of the time (23/32 correct predictions) which is lower than the models accuracy score of ~76%

**Vegas Odds** predicted the winner **65.625%** of the time (21/32 correct predictions)

The model was 2/2 on upset picks (both times was a 9 seed over an 8 seed)

### Round of 32:

Judging the accuracy of the model is not as straight forward after the first round since not all the matchups being predicted were actually played

Of the 16 teams that advanced, the model predicted 14 of them correctly. 

### Sweet Sixteen:

Of the 8 teams that advanced out of this round, the model predicted 5 of them correctly

### Elite Eight:

The model was less accurate in this round, correctly picking 1/4 winners.

### Final Four:

The model was 1/2 on picking the winner of this round

### Championship:

The model predicted the championship game to be between #1 Duke and #1 Virginia and predicted Virginia to win it all

It was correct in Virginia winning the tournament, but they would defeat #3 Texas Tech instead of Duke

### Thoughts:

Overall, the model was surprisingly accurate with its predictions and outperformed the majority of brackets. There is undoubtedly a lot of luck involved, but it is pretty cool that out of 64 teams my model corectly picked the national champion

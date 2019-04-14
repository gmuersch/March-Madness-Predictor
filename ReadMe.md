# March Madness Predictor 

The aim of this project is to use machine learning models to predict sports games

In this version we will be predicting and filling out NCAA March Madness Tournament brackets

For each season we have data on 351 teams and nearly 6,000 basketball games.
After collecting and cleaning this data, I used it as a training set to train a logistical regression model using python's sklearn module. 
Once the model is trained we can ask it to predict the holdout data, in this case any March Madness tournament.


The end goal for this project is to consider who my model thinks will win and how confident it is, then compare that to vegas betting odds in order to find games where my model thinks the bet has high value.
With sports betting moving through legislation to be legalized in more and more states, the market for it will grow and
having an edge like this would give a massive advantage over the average better.

In this first rendition I will be using 4 features to train the model (strength of schedule, field goal %, three point % and free throw %). For right now this feature set will be pretty basic as I focus on creating the code that will gather, clean and display the data. In the future I will mess around with advanced statistics and other factors in hopes of increasing the predictive power. Even still, it will be interesting to see what kind of predictions we will get with a somewhat basic feature set.

**Project Files**

Currently this project uses 3 seperate scripts: data_scraper.py, model.py and predictor.py 

I will briefly mention what each script accomplishes below


**Data_Scraper.py:**

In this file I defined two functions that scrapes team stats and regular season game results respectively. 
Since they are written as functions we can reuse the code to gather the data for any year we want saving it to a csv file. 


**model.py:

This script reads our scraped data and turns them into pandas dataframes. The functions match_stats_reg_season() looks at each matchup and calculates the difference in stats between the two teams(Team A stats - Team B stats) This makes it so our model only has to look at a single stat line and determine whether Team A wins or loses


After calculating the match stats of each regular season game, we use this data to train our logistic regression model and can now predict the tournament.


**predictor.py:**

This script uses the pickle module to call our trained regression model from the model.py. I defined the predict_tournament() function that reads and appends each round of the tournament, predicting the winners and advancing them in the tournament. This function loops over each newly predicted round until the entire tournament is predicted and written to a csv file 

## Tournament Results and Statistics:

**Bracket_Games19.csv:**

This file holds our models predicted tournament results.

### Round of 64: 

**The Model** predicted the winner **71.875%** of the time (23/32 correct predictions) which is lower than the models accuracy score of ~76%

**Vegas Odds** predicted the winner **65.625%** of the time (21/32 correct predictions)

The model was 2/2 on upset picks (both times was a 9 seed over an 8 seed)

### Round of 32:

Judging the accuracy of the model is not as straight forward after the first round since not all the matchups being predicted were actually played

Of the 16 teams that advanced, the model predicted 15 of them correctly (the only wrong pick was Wisconsin who lost in round one)

The model was 1/1 on upsets predicted (#5 Auburn over #4 Kansas) but vegas also favored Auburn so its not much of an upset

Due to the lack of underdog victories in this round our model was extremely accurate (The team favored by vegas won every game, but did not necessarily cover the point spread)

### Sweet Sixteen:

Of the 8 teams that advanced out of this round, the model predicted 6 of them correctly

The #1 UNC was upset by #5 Auburn and #3 Purdue squeaked out an overtime win agains #2 Tennessee

Again, the model was 1/1 on upset picks predicting #3 Texas Tech over #2 Michigan 

### Elite Eight:

The models strong preference to higher seeds ended up failing significantly in this round

It was predicted that all four of the #1 seeds would advance but only one of them (Virginia) did so making the model 1/4 on predicting the winner.

It is harder to maintain a high score in the later rounds since teams you might have picked to go far could have already lost in previous rounds (Looking at you UNC)

### Final Four:

The model was 1/2 on picking the winner of this round

### Championship:

The model predicted the championship game to be between #1 Gonzaga and #1 Virginia with Gonzaga winning the tournament

In Actuality the Championship game was played between #3 Texas Tech and #1 Virginia with Virginia being victorius

### Thoughts:

Overall, the model was surprisingly accurate with its predictions and outperformed the majority of brackets

It did come apart near the end but predicting 1 of the final two teams is fairly impressive. 

Without any knowledge of the teams seedings, it picked the higher ranked team to win 57/61 games. It would be interesting to see if the extreme of this trend is isolated to this season or not. The top teams this year were percieved to be much more talented than the rest of the field compared to previous years and the model agreed with that notion.

When the model did pick an upset it was 4/4 which is pretty cool in its own right.

Now that all the code is written and the first predictions are out of the way we can try using different feature sets with more advanced sabermetrics to see if we can improve the accuracy of the model. We can also look at the predictions of March Madness Tournaments in years past to see if this years accuracy was a fluke or not


**Will be Adding:**

-Use pathlib module to fix pathing for general use

-improve the predicitive power by testing accuracy scores of different feature sets and training sets

-Graph which features have a larger correlation to winning

-Rewrite the tournament results in a bracket format to aid in readability


Thank you for taking the time to look at my project, I spent a lot of time building this and any comments or criticisms would be appreciated!

import pandas as pd 
import csv
import pickle
import numpy as np
import requests
from bs4 import BeautifulSoup

# This file holds all the neccesary functions used in this project

# Calculates the match stats of each regular season game, skipping the games we dont have team data for 
def match_stats_reg_season(lst,df_games,df_features):
	for index,row in df_games.iterrows():
		if index%2==0: # Each game has 2 rows (one for each team) this will get rid of the redundant data
			try:	
				lst.append(np.append(df_features.loc[df_features['SCHOOL']==row[1]].values[0][1:].astype(float) - df_features.loc[df_features['SCHOOL']==row[4]].values[0][1:].astype(float),[row[6]]))
			except IndexError:
				pass
	return lst


#Calculates the match stats of each tournament game, similar to match_stats_reg_season()
def match_stats_tournament(lst,df_games,df_features):
	for index,row in df_games.iterrows():
		lst.append(df_features.loc[df_features['SCHOOL']==row[0]].values[0][1:].astype(float) - df_features.loc[df_features['SCHOOL']==row[1]].values[0][1:].astype(float))
		
	return lst


def predict_tournament(path_tournament,bracket_file,df_features,features): 
	
	# rounds list holds the indices for the first game of each tournament round in our csv file
	rounds = [0,33,50,59,64,67]

	# Load the trained regression model using pickle
	filename = 'finalized_model.sav'
	model = pickle.load(open(filename,'rb'))


	# Iterate through each round of the tournament so I can predict the winners of one round and update the bracket for the matches of the next round
	for r in rounds:

		# Two holder lists to keep track of our match stats and which teams advance respectively
		tournament_match_stats = [] 
		next_round = []	

		# Fills the df_tournament data frame with the matches to be predicted for the given rounds
		df_tournament = pd.read_csv(path_tournament)

		# Call the match_stats function to calculate the current rounds match stats
		match_stats_tournament(tournament_match_stats,df_tournament[r:],df_features)	
		
		# Save the current rounds match stats to a df
		df_tournament_match_stats = pd.DataFrame(columns=features, data=tournament_match_stats)

		# Predicts who will advance to the next round
		holdout_predicitons = model.predict(df_tournament_match_stats[features])	


		# Iterates through each matchup and picks out the predicted winner saving them to the next_round holder list
		count=0 
		for index,row in df_tournament[r:].iterrows():	

			if holdout_predicitons[count] == 0:
				next_round.append(row[0])
				count+=1

			else:
				next_round.append(row[1])
				count+=1
			
		
		# Appends the winners of each round to our bracket csv file
		# First I will check if there is a champion to properly crown them 
		if len(next_round)==1:
			with open(bracket_file,'a',newline='') as writefile:
				writer = csv.writer(writefile)
				writer.writerow(['CHAMPION:',next_round[0]])

		# Otherwise mark the start of next round and append the next matchups	
		else:
			with open(bracket_file,'a',newline='') as writefile:
				writer = csv.writer(writefile)
				writer.writerow(['NEXT ROUND'])

				for i in range(len(next_round)-1):
					if i%2==0:
						writer.writerow([next_round[i],next_round[i+1]])
					else:
						pass


# Since there is data on games that include some very small schools 
# I created a function that counts how many games we do not have team data for (a large amount would indicate an issue) and delete them from our df
def game_error_counter(df_games,df_stats):
	errors = 0
	for index,row in df_games.iterrows():
		try:
			df_stats.loc[df_stats['SCHOOL']==row[1]].values[0][2:]
		except IndexError:
			df_games = df_games.drop([index])
			errors +=1
	print("Number of errors: ", errors)


# This function scrapes the given webpage and saves the information to a csv file
# Setting it up in this way allows us to grab either basic or advanced stats of every team in any year we choose
def NCAA_scrape_teams(url,csv_name,stats_cols):
	
	# Creates an empty csv file with a header of each category we will be scraping 
	with open(csv_name,'w',newline='') as writefile:
		writer = csv.writer(writefile)
		writer.writerow(stats_cols)

	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'html.parser')
	data = soup.find(class_='table_outer_container').find('tbody').find_all('tr')

	
	for i in data:# This for loop grabs each row of stats and picks out the school name
		stats = []
		try: # Try statement because the table is broken up by headers
			stats.append(i.find('a').contents[0])
			
			for j in i.find_all(class_='right'): # This loop iterates through each col of each row of stats, saving them to a list
				
				try:	# Try statement because their is a random gap in the table	
					stats.append(float(j.contents[0]))

				except IndexError:
					continue
			
			# Our stats list will hold one team and all of its respective stats
			# We need to append it to the csv file we created above before it gets rewritten at the start of the first for loop
			with open(csv_name,'a',newline='') as appendfile:
				append = csv.writer(appendfile)
				
				append.writerow(stats)

		except AttributeError:
			continue


# Scrapes all regular season games from a given year
def NCAA_reg_season_scraper(base_url, page_num, csv_name):

	# To cycle through the many pages of basketball games, we need to create list of all the webpages using our base url 
	scroll = []
	for i in range(0,page_num,100):
		scroll.append(base_url + str(i))

	# Create a new csv file with our header
	with open(csv_name,'w',newline='') as writefile:
			writer = csv.writer(writefile)
			writer.writerow(['Date','Team','Rank','Away?','Opponent','Opp Rank','W/L','Points','Opp Points','Point Diff.','OT'])

	# This part of our function will be similar in style to our above function
	for url in scroll:

		page = requests.get(url)
		soup = BeautifulSoup(page.text,'html.parser')
		data = soup.find(class_='table_outer_container').find('tbody').find_all('tr')

		for i in data:
			holder = []
			for j in i.find_all('td'):
				try:
					holder.append(int(j.get_text()))

				except ValueError:
					holder.append(j.get_text())

				except IndexError:
					continue

			try:	# Deletes some blank spaces from scraped data
				del holder[1]
				del holder[7]
				del holder[10]

			except IndexError:
				pass

			with open(csv_name,'a',newline='') as appendfile:
				append = csv.writer(appendfile)
				if len(holder) == 0: # Deletes the blank rows in the original table 
					pass
				else:
					append.writerow(holder)

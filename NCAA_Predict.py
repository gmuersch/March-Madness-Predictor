import pandas as pd

# Path to the csv file I created holding the tournaments first round matchups
path_tournament19 = r"C:\Python\March Madness\Bracket_Games19.csv"

# path to advanced team stats
path_team_stats_advanced19 = r"C:\Python\March Madness\NCAA_Team_Data_Advanced19.csv"

# path to basic team stats
path_team_stats_basic19 = r"C:\Python\March Madness\NCAA_Team_Data_Basic19.csv"


# fill the dataframes
df_team_stats_advanced19 = pd.read_csv(path_team_stats_advanced19)
df_team_stats_basic19 = pd.read_csv(path_team_stats_basic19)

# Append the basic and advancd team stats dataframes (removed some redundant columns)
df_team_stats19 = pd.merge(df_team_stats_basic19, df_team_stats_advanced19[['SCHOOL','PACE','ORTg','FTr','3PAr','TS%','TRB%','AST%','STL%','BLK%','eFG%','TOV%','ORB%','FT/FGA']],
																			on='SCHOOL', how='outer')

# df picking out the stats used as features, this is needed for the match_stats function
df_features19 = df_team_stats19[['SCHOOL','W/L%','SRS','SOS','ORTg']]


# import the necessary functions to predict our results
from functions import match_stats_tournament, predict_tournament

features = ['W/L%','SRS','SOS','ORTg']
predict_tournament(path_tournament19,'Bracket_Games19.csv',df_features19,features)
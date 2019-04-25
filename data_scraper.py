# First I need to scrape the stats of all available NCAA Men's Basketball teams
# I will be using the past two seasons (~11,000 games & 704 teams) to train this model

# URL's for basic and advanced team stats respectively
basic_stats_url19 = 'https://www.sports-reference.com/cbb/seasons/2019-school-stats.html'
basic_stats_url18 = 'https://www.sports-reference.com/cbb/seasons/2018-school-stats.html'

advanced_stats_url19 = 'https://www.sports-reference.com/cbb/seasons/2019-advanced-school-stats.html'
advanced_stats_url18 = 'https://www.sports-reference.com/cbb/seasons/2018-advanced-school-stats.html'

basic_stats = ['SCHOOL','RANK','GAMES','WINS','LOSS','W/L%','SRS','SOS','CONF. W','CONF. L','HOME W','HOME L','AWAY W','AWAY L','POINTS SCORED','POINTS ALLOWED','MINUTES PLAYED','FG','FGA','FG%','3P','3PA','3P%','FT','FTA','FT%','OFFENSIVE REBOUNDS','TOTAL REBOUNDS','ASISTS','STEALS','BLOCKS','TURN OVERS','PF']
advanced_stats = ['SCHOOL','RANK','GAMES','WINS','LOSS','W/L%','SRS','SOS','CONF. W','CONF. L','HOME W','HOME L','AWAY W','AWAY L','POINTS SCORED','POINTS ALLOWED','PACE','ORTg','FTr','3PAr','TS%','TRB%','AST%','STL%','BLK%','eFG%','TOV%','ORB%','FT/FGA']


# Import the team scraper function from our functions script
from functions import NCAA_scrape_teams

# Call the functions to scrape the team data and save it to a csv file
NCAA_scrape_teams(basic_stats_url19,'NCAA_Team_Data_Basic19t.csv',basic_stats)
NCAA_scrape_teams(basic_stats_url18,'NCAA_Team_Data_Basic18t.csv',basic_stats)

NCAA_scrape_teams(advanced_stats_url19,'NCAA_Team_Data_Advanced19t.csv',advanced_stats)
NCAA_scrape_teams(advanced_stats_url18,'NCAA_Team_Data_Advanced18t.csv',advanced_stats)


# Now I need to gather the results of each regular season game from the past two seasons
# For each year I need the base url and the (number of pages+1)*100 in order to satisfy the url's requirments so I can flip through the webpages

#2019 Season
base_games19 ='https://www.sports-reference.com/cbb/play-index/matchup_finder.cgi?request=1&year_min=2019&year_max=2019&school_id=&opp_id=&game_type=A&game_month=&game_location=&game_result=&is_overtime=&comp_school=le&comp_opp=le&rank_school=ANY&rank_opp=ANY&order_by=date_game&order_by_asc=&offset='
pages19 = 11700

#2018 Season
base_games18 = 'https://www.sports-reference.com/cbb/play-index/matchup_finder.cgi?request=1&year_min=2018&year_max=2018&school_id=&opp_id=&game_type=A&game_month=&game_location=&game_result=&is_overtime=&comp_school=le&comp_opp=le&rank_school=ANY&rank_opp=ANY&order_by=date_game&order_by_asc=&offset='
pages18 = 11600

from functions import NCAA_reg_season_scraper

# By calling this function we once again scrape the needed data and save it to a csv file
NCAA_reg_season_scraper(base_games19,pages19,'NCAA_Reg_Season19t.csv')
NCAA_reg_season_scraper(base_games18,pages18,'NCAA_Reg_Season18t.csv')
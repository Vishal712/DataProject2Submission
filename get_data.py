## Project 2 
# Data Creation/ Data Cleaning
#Getting the datasets for both NBA and NCAA and cleaning them


#pip install sportsreference is needed to run this code, as it contains data from the popular Sportsreference website. The documentation is listed here: https://sportsreference.readthedocs.io/en/stable/sportsreference.html
#The pypi site for this package is listed here: https://pypi.org/project/sportsreference/
#  pip install sportsreference
#Dependencies
import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sportsreference.ncaab.roster import Player
from sportsreference.nba.roster import Roster

def scrape_info():
    print("Getting Data and storing in Mongo(This will take some time)")
    # Creating the list of player objects.
    # This is done by going through each team, then getting the list of player objects on each roster, and storing them in a list. This project collects data only from players on an active roster, to preserve accuracy, and because we realize that trends in the modern NBA can change rapidly that attributes like the mid-range shot is not as needed today as it was years ago.



    teams = ['ATL','BRK','BOS','CHO','CHI','CLE','DAL','DEN','DET','GSW',
            'HOU','IND','LAC','LAL','MEM','MIA','MIL','MIN','NOP','NYK',
            'OKC','ORL','PHI','PHO','POR','SAC','SAS','TOR','UTA','WAS']
    player_list = []

    for team in teams:
        teamname = Roster(team)
        for players in teamname.players:
            player_list.append(players)
    print("Got all player names")




    #Storing all stats into two dictonaries now, each dictionary containing the player name as the key, and the value being the pandas dataframe that the function Player.dataframe gives us. This dataframe is a compilation of a ton of different stats, including some advanced stats. 



    nba_player_info = {}
    ncaa_player_info = {}
    for nbaplayer in player_list:
        try:
            name = nbaplayer.name
            name = name.replace("'", "")
            name = name.replace(".", "")
            split_name = name.split()
            firstname = str(split_name[0]).lower()
            lastname = str(split_name[1]).lower()
            nameid = firstname + "-" + lastname + "-1"
            ncaa_player = Player(nameid)
            nba_player_info[nbaplayer.name] = nbaplayer.dataframe
            ncaa_player_info[nbaplayer.name] = ncaa_player.dataframe 
        except(TypeError):
            pass
    print("Stored Everything in two dictionaries")



    #This is an example of the columns from each player's dataframe, seen below. The documentation contains information about what each column represents. 
    #nba_player_info['Kevin Durant'].columns



    #Here is an example of how to get a stat from the information dictionary made earlier, this gives a career average of Kevin Durant's true shooting percentage.

    #float(nba_player_info['Kevin Durant']['true_shooting_percentage']['Career'])


    #This code below stores 2 Pandas Dataframes, one for NBA statistics and one for NCAA statistics. These statistics are from the dataframe object stored from earlier, and the purpose of this is to make is much easier to access stats than the cell above. Each stat is calculated as a career total, then averaged out later.
    #First we stored information to an NBA dataframe, and printed out names that are one's we have to omit, because there is not enough data on them to store. Often, these players have empty stats lists because they are technically on the roster, but haven't played much yet. 



    nba_required_stats_list = []
    nba_names_to_drop = []
    for key, value in nba_player_info.items():
        try:
            raw_height = nba_player_info[key]['height']['Career'][-1].split('-')
            career_height = (float(raw_height[0]) * 12 ) + float(raw_height[1])
            career_weight = float(nba_player_info[key]['weight']['Career'])
            career_points = float(nba_player_info[key]['points']['Career'])
            career_games = float(nba_player_info[key]['games_played']['Career'])
            career_assists = float(nba_player_info[key]['assists']['Career'])
            defensive_rebounds = float(nba_player_info[key]['defensive_rebounds']['Career'])
            offensive_rebounds = float(nba_player_info[key]['offensive_rebounds']['Career'])
            career_turnovers = float(nba_player_info[key]['turnovers']['Career'])
            career_blocks = float(nba_player_info[key]['blocks']['Career'])
            career_steals = float(nba_player_info[key]['steals']['Career'])
            career_free_throw_percentage = float(nba_player_info[key]['free_throw_percentage']['Career'])
            career_three_point_percentage = float(nba_player_info[key]['three_point_percentage']['Career'])
            career_PER = float(nba_player_info[key]['player_efficiency_rating']['Career'])
            career_win_shares = float(nba_player_info[key]['win_shares']['Career'])
            off_win_shares = float(nba_player_info[key]['offensive_win_shares']['Career'])
            def_win_shares = float(nba_player_info[key]['defensive_win_shares']['Career'])
            career_field_goal_percentage = float(nba_player_info[key]['field_goal_percentage']['Career'])
            career_usage_percentage = float(nba_player_info[key]['usage_percentage']['Career'])
            vorp = float(nba_player_info[key]['value_over_replacement_player']['Career'][-1])
            boxplusminus = float(nba_player_info[key]['box_plus_minus']['Career'])
            true_shooting_percentage = float(nba_player_info[key]['true_shooting_percentage']['Career'])
            player_dict =  {'Name': key,
                            'Height': career_height,
                            'Weight': career_weight,
                            'Career Points': career_points,
                            'Career Games': career_games,
                            'Career Assists': career_assists,
                            'Career Def Rebounds':defensive_rebounds,
                            'Career Off Rebounds':offensive_rebounds,
                            'Career Turnovers': career_turnovers,
                            'Career Blocks': career_blocks,
                            'Career Steals': career_steals,
                            'Career Free Throw Percentage': career_free_throw_percentage,
                            'Career Three Point Percentage': career_three_point_percentage,
                            'Career Field Goal Percentage': career_field_goal_percentage,
                            'Career PER': career_PER,
                            'Career Win Shares': career_win_shares,
                            'Offensive Win Shares': off_win_shares,
                            'Defensive Win Shares': def_win_shares,
                            'Career Usage Percentage': career_usage_percentage,
                            'VORP': vorp,
                            'Box Plus Minus': boxplusminus,
                            'True Shooting Per': true_shooting_percentage
                            }
            nba_required_stats_list.append(player_dict)
        except (KeyError, TypeError):
            nba_names_to_drop.append(key)
            #print(key)
    nba_stats_df = pd.DataFrame(nba_required_stats_list)




    #nba_stats_df




    #Now to do the same for NCAA, we have to jump through a couple more hoop because of the fact that not all players have data that is available. For example, Tyler Johnson, who is in the NBA, has no NCAA data on height. To fix this, we need to create a function, that return -999 if no information is available, or return the corresponding stat as a float. This is so the code is not cluttered with a ton of if statements.   



    def stat_checker(stat):
        if(stat is None):
            return -999
        else:
            return float(stat)



    #NO VORP OR PER
    ncaa_required_stats_list = []
    ncaa_names_to_drop = []
    for key, value in ncaa_player_info.items():
        try:
            raw_height = ncaa_player_info[key]['height']['Career'][-1]
            if(raw_height == None):
                career_height = 0
            else:
                raw_height = raw_height.split('-')
                career_height = (float(raw_height[0]) * 12 ) + float(raw_height[1])        
            career_weight = stat_checker(ncaa_player_info[key]['weight']['Career'][-1])
            career_points = stat_checker(ncaa_player_info[key]['points']['Career'][-1])
            career_games = stat_checker(ncaa_player_info[key]['games_played']['Career'][-1])
            career_assists = stat_checker(ncaa_player_info[key]['assists']['Career'][-1])
            defensive_rebounds = stat_checker(ncaa_player_info[key]['defensive_rebounds']['Career'][-1])
            offensive_rebounds = stat_checker(ncaa_player_info[key]['offensive_rebounds']['Career'][-1])
            career_turnovers = stat_checker(ncaa_player_info[key]['turnovers']['Career'][-1])
            career_blocks = stat_checker(ncaa_player_info[key]['blocks']['Career'][-1])
            career_steals = stat_checker(ncaa_player_info[key]['steals']['Career'][-1])
            career_free_throw_percentage = stat_checker(ncaa_player_info[key]['free_throw_percentage']['Career'][-1])
            career_three_point_percentage = stat_checker(ncaa_player_info[key]['three_point_percentage']['Career'][-1])
            career_win_shares = stat_checker(ncaa_player_info[key]['win_shares']['Career'][-1])
            off_win_shares = stat_checker(ncaa_player_info[key]['offensive_win_shares']['Career'][-1])
            def_win_shares = stat_checker(ncaa_player_info[key]['defensive_win_shares']['Career'][-1])
            career_field_goal_percentage = stat_checker(ncaa_player_info[key]['field_goal_percentage']['Career'][-1])
            career_usage_percentage = stat_checker(ncaa_player_info[key]['usage_percentage']['Career'][-1])
            boxplusminus = stat_checker(ncaa_player_info[key]['box_plus_minus']['Career'][-1])
            true_shooting_percentage = stat_checker(ncaa_player_info[key]['true_shooting_percentage']['Career'][-1])
            player_dict =  {'Name': key,
                            'Height': career_height,
                            'Weight': career_weight,
                            'Career Points': career_points,
                            'Career Games': career_games,
                            'Career Assists': career_assists,
                            'Career Def Rebounds':defensive_rebounds,
                            'Career Off Rebounds':offensive_rebounds,
                            'Career Turnovers': career_turnovers,
                            'Career Blocks': career_blocks,
                            'Career Steals': career_steals,
                            'Career Free Throw Percentage': career_free_throw_percentage,
                            'Career Three Point Percentage': career_three_point_percentage,
                            'Career Field Goal Percentage': career_field_goal_percentage,
                            'Career Win Shares': career_win_shares,
                            'Offensive Win Shares': off_win_shares,
                            'Defensive Win Shares': def_win_shares,
                            'Career Usage Percentage': career_usage_percentage,
                            'Box Plus Minus': boxplusminus,
                            'True Shooting Per': true_shooting_percentage
                            }
            ncaa_required_stats_list.append(player_dict)
        except KeyError as err:
            print(key, "Key Error: ", err)
        except TypeError as err:
            print(key, "Type Error: ", err)
        except AttributeError as err:
            print(key, "Attribute Error: ", err)
    ncaa_stats_df = pd.DataFrame(ncaa_required_stats_list)





    #Now we have to condense the NCAA dataframe in order to include players only from the NBA. Recall the NBA dataframe where some players didn't play enough minutes in the NBA in order to record data, so we were not able to include them. So we need to make sure the names in the NCAA line up in the NBA. This also ensures a plot of x and y are represented as actual players, making it more accurate to see a transition of stats from college to the league. 





    nbanames = list(nba_stats_df["Name"])
    ncaa_stats_df = ncaa_stats_df[ncaa_stats_df['Name'].isin(nbanames)]
    ncaa_stats_df = ncaa_stats_df.reset_index(drop = True)
    #ncaa_stats_df



    #Finally, we included averages for each stat in the dataframe in order to make data analysis in the next notebook a lot easier to do and making plotting more intuitive. Having averages for stats is more accurate than total stats, considering not all player have played the same amount of games. 



    nba_stats_df["PPG"] = ''
    nba_stats_df["APG"] = ''
    nba_stats_df["TPG"] = ''
    nba_stats_df["BPG"] = ''
    nba_stats_df["SPG"] = ''
    nba_stats_df["RPG"] = ''
    ncaa_stats_df["PPG"] = ''
    ncaa_stats_df["APG"] = ''
    ncaa_stats_df["TPG"] = ''
    ncaa_stats_df["BPG"] = ''
    ncaa_stats_df["SPG"] = ''
    ncaa_stats_df["RPG"] = ''

    for index, row in nba_stats_df.iterrows():
        player = nba_stats_df.iloc[[index]]
        nba_stats_df.loc[index, "PPG"] = float(player["Career Points"] / player["Career Games"])
        nba_stats_df.loc[index, "APG"] = float(player["Career Assists"] / player["Career Games"])
        nba_stats_df.loc[index, "TPG"] = float(player["Career Turnovers"] / player["Career Games"])
        nba_stats_df.loc[index, "BPG"] = float(player["Career Blocks"] / player["Career Games"])
        nba_stats_df.loc[index, "SPG"] = float(player["Career Steals"] / player["Career Games"])
        nba_stats_df.loc[index, "RPG"] = float(player["Career Off Rebounds"] / player["Career Games"]) + float(player["Career Def Rebounds"] / player["Career Games"])
    for index, row in ncaa_stats_df.iterrows():
        player = ncaa_stats_df.iloc[[index]]
        ncaa_stats_df.loc[index, "PPG"] = float(player["Career Points"] / player["Career Games"])
        ncaa_stats_df.loc[index, "APG"] = float(player["Career Assists"] / player["Career Games"])
        ncaa_stats_df.loc[index, "TPG"] = float(player["Career Turnovers"] / player["Career Games"])
        ncaa_stats_df.loc[index, "BPG"] = float(player["Career Blocks"] / player["Career Games"])
        ncaa_stats_df.loc[index, "SPG"] = float(player["Career Steals"] / player["Career Games"])
        ncaa_stats_df.loc[index, "RPG"] = float(player["Career Off Rebounds"] / player["Career Games"]) + float(player["Career Def Rebounds"] / player["Career Games"])



    #Finally, this saves both dataframes to csv file in order to prevent the need for running these cells again. This may take some time to run considering the request of ~800 player dataframes and objects, so loading these csv files are recommended.



    players_with_college = pd.read_csv("all_seasons.csv")

    college_players = players_with_college["player_name"].tolist()
    college_names = players_with_college["college"].tolist()

    colleges = dict(zip(college_players, college_names))



    player_list = []
    not_here = []
    for player in nba_stats_df["Name"].tolist():
        try:
            if(player == "Wesley Iwundu"):
                player = "Wes Iwundu"
            elif(player == "Frank Mason III"):
                player = "Frank Mason"
            elif(player == "Sviatoslav Mykhailiuk"):
                player = "Svi Mykhailiuk"
            player_list.append((player, colleges[player]))
        except:
            try:
                player = player.replace(".", "")
                player_list.append((player, colleges[player]))
            except:
                try:
                    jr_player = player + " Jr."
                    player_list.append((player,  colleges[jr_player]))
                except:
                    try:
                        II_player = player + " II"
                        player_list.append((player,  colleges[II_player]))
                    except:
                        try:
                            III_player = player + " III"
                            player_list.append((player,  colleges[III_player]))
                        except:
                            not_here.append(player)




    player_list.append(("Bol Bol", "Oregon"))



    player_college_dict = {}
    for item in player_list:
        player_college_dict[item[0]] = item[1]

    #converting dictionary into a dataframe
    player_college_df = pd.DataFrame.from_dict(player_college_dict,orient ='index')

    #reseting the index 
    player_college_df.reset_index(inplace=True)
    #changing the name of the column
    player_college_df.rename({'index': 'Name', 0: 'school'},axis =1, inplace = True)


    #remove any school thhat is label as None
    player_college_df = player_college_df[player_college_df.school != "None"]

    #we added the Universitty at the end of each school name 
    #so we can make it clear to google that we are searching for a university
    player_college_df["school"] = player_college_df["school"] + " University"


    #adding lat and lon column
    player_college_df["lat"] = ""
    player_college_df["lng"] = ""

    #player_college_df.head()



    gkey = "AIzaSyAQzjQQxNwPTSCT4Yv2IolnWjYbXZWrsNs"
    for index, row in player_college_df.iterrows():
        
        # name of the school
        college = row["school"]
        #adding the school and key to the target url
        target_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={college}&key={gkey}'

        # make request
        response = requests.get(target_url)
        
        # convert to json
        college_lat_lng = response.json()

        player_college_df.loc[index, "lat"] = college_lat_lng["results"][0]["geometry"]["location"]["lat"]
        player_college_df.loc[index, "lng"] = college_lat_lng["results"][0]["geometry"]["location"]["lng"]




    # Visualize to confirm lat lng appear
    #player_college_df





    #removing the the word "University" from the school column
    player_college_df["school"] = player_college_df["school"].str.split(" University", n = 1, expand = True)


    #combine the location informain with the condensed stat table 
    #retreving the necessary file 
    ncaa_clean = pd.DataFrame(ncaa_stats_df[["Name","Height","Weight", "PPG","APG","RPG", "SPG", "BPG","TPG", "Career Field Goal Percentage","Career Three Point Percentage"]])
    nba_clean = pd.DataFrame(nba_stats_df[["Name","Height","Weight", "PPG","APG","RPG", "SPG", "BPG","TPG", "Career Field Goal Percentage","Career Three Point Percentage"]])
    #renaming FGP and 3PG column
    ncaa_clean.rename({"Career Field Goal Percentage": "FGP", "Career Three Point Percentage": "3PG"}, axis=1,inplace = True)
    nba_clean.rename({"Career Field Goal Percentage": "FGP", "Career Three Point Percentage": "3PG"}, axis=1,inplace = True)

    #merging the nba_clean and player_college to add location information
    nba_location = pd.merge(player_college_df, nba_clean, on = "Name", how = "inner")



    #some NCAA entries are negative so we will be fixing it here


    ncaa_clean.set_index("Name",inplace = True)

    #fixing Chris clemons
    ncaa_clean.loc["Chris Clemons","Height"] = 69
    ncaa_clean.loc["Chris Clemons","Weight"] = 180
    ncaa_clean.loc["Chris Clemons","PPG"] = 24.8
    ncaa_clean.loc["Chris Clemons","APG"] = 2.6
    ncaa_clean.loc["Chris Clemons","RPG"] = 4.5
    ncaa_clean.loc["Chris Clemons","SPG"] = 1.6
    ncaa_clean.loc["Chris Clemons","BPG"] = 0.4
    ncaa_clean.loc["Chris Clemons","TPG"] = 2.5
    ncaa_clean.loc["Chris Clemons","FGP"] = 0.444
    ncaa_clean.loc["Chris Clemons","3PG"] = 0.363
    #fixing Dennis Smith Jr.
    ncaa_clean.loc["Dennis Smith Jr.","Height"] = 75
    ncaa_clean.loc["Dennis Smith Jr.","Weight"] = 195
    ncaa_clean.loc["Dennis Smith Jr.","PPG"] = 18.1
    ncaa_clean.loc["Dennis Smith Jr.","APG"] = 6.2
    ncaa_clean.loc["Dennis Smith Jr.","RPG"] = 4.6
    ncaa_clean.loc["Dennis Smith Jr.","SPG"] = 1.9
    ncaa_clean.loc["Dennis Smith Jr.","BPG"] = 0.4
    ncaa_clean.loc["Dennis Smith Jr.","TPG"] = 3.4
    ncaa_clean.loc["Dennis Smith Jr.","FGP"] = 0.455
    ncaa_clean.loc["Dennis Smith Jr.","3PG"] = 0.359
    #fixing Frank Jackson
    ncaa_clean.loc["Frank Jackson","Height"] = 75
    ncaa_clean.loc["Frank Jackson","Weight"] = 205
    ncaa_clean.loc["Frank Jackson","PPG"] = 10.9
    ncaa_clean.loc["Frank Jackson","APG"] = 1.7
    ncaa_clean.loc["Frank Jackson","RPG"] = 2.5
    ncaa_clean.loc["Frank Jackson","SPG"] = 0.6
    ncaa_clean.loc["Frank Jackson","BPG"] = 0.1
    ncaa_clean.loc["Frank Jackson","TPG"] = 1.4
    ncaa_clean.loc["Frank Jackson","FGP"] = 0.473
    ncaa_clean.loc["Frank Jackson","3PG"] = 0.395
    #fixing Gary Payton II
    ncaa_clean.loc["Gary Payton II","Height"] = 75
    ncaa_clean.loc["Gary Payton II","Weight"] = 175
    ncaa_clean.loc["Gary Payton II","PPG"] = 14.7
    ncaa_clean.loc["Gary Payton II","APG"] = 4.1
    ncaa_clean.loc["Gary Payton II","RPG"] = 7.7
    ncaa_clean.loc["Gary Payton II","SPG"] = 2.8
    ncaa_clean.loc["Gary Payton II","BPG"] = 0.8
    ncaa_clean.loc["Gary Payton II","TPG"] = 2.1
    ncaa_clean.loc["Gary Payton II","FGP"] = 0.485
    ncaa_clean.loc["Gary Payton II","3PG"] = 0.302
    #fixing Gary Trent Jr.
    ncaa_clean.loc["Gary Trent Jr.","Height"] = 78
    ncaa_clean.loc["Gary Trent Jr.","Weight"] = 209
    ncaa_clean.loc["Gary Trent Jr.","PPG"] = 14.5
    ncaa_clean.loc["Gary Trent Jr.","APG"] = 1.4
    ncaa_clean.loc["Gary Trent Jr.","RPG"] = 4.2
    ncaa_clean.loc["Gary Trent Jr.","SPG"] = 1.2
    ncaa_clean.loc["Gary Trent Jr.","BPG"] = 0.1
    ncaa_clean.loc["Gary Trent Jr.","TPG"] = 1.0
    ncaa_clean.loc["Gary Trent Jr.","FGP"] = 0.415
    ncaa_clean.loc["Gary Trent Jr.","3PG"] = 0.402
    #fixingGlenn Robinson III
    ncaa_clean.loc["Glenn Robinson III","Height"] = 78
    ncaa_clean.loc["Glenn Robinson III","Weight"] = 220
    ncaa_clean.loc["Glenn Robinson III","PPG"] = 12.0
    ncaa_clean.loc["Glenn Robinson III","APG"] = 1.0
    ncaa_clean.loc["Glenn Robinson III","RPG"] = 4.9
    ncaa_clean.loc["Glenn Robinson III","SPG"] = 1.0
    ncaa_clean.loc["Glenn Robinson III","BPG"] = 0.3
    ncaa_clean.loc["Glenn Robinson III","TPG"] = 1.0
    ncaa_clean.loc["Glenn Robinson III","FGP"] = 0.525
    ncaa_clean.loc["Glenn Robinson III","3PG"] = 0.313
    #fixing Jamal Crawford
    ncaa_clean.loc["Jamal Crawford","RPG"] = 2.8
    #fixing Jaren Jackson Jr.
    ncaa_clean.loc["Jaren Jackson Jr.","Height"] = 83
    ncaa_clean.loc["Jaren Jackson Jr.","Weight"] = 242
    ncaa_clean.loc["Jaren Jackson Jr.","PPG"] = 10.9
    ncaa_clean.loc["Jaren Jackson Jr.","RPG"] = 5.8
    ncaa_clean.loc["Jaren Jackson Jr.","APG"] = 1.1
    ncaa_clean.loc["Jaren Jackson Jr.","SPG"] = 0.6
    ncaa_clean.loc["Jaren Jackson Jr.","BPG"] = 3.0
    ncaa_clean.loc["Jaren Jackson Jr.","TPG"] = 1.8
    ncaa_clean.loc["Jaren Jackson Jr.","FGP"] = 0.513
    ncaa_clean.loc["Jaren Jackson Jr.","3PG"] = 0.396
    #fixing Kevin Porter Jr.
    ncaa_clean.loc["Kevin Porter Jr.","Height"] = 78
    ncaa_clean.loc["Kevin Porter Jr.","Weight"] = 218
    ncaa_clean.loc["Kevin Porter Jr.","PPG"] = 9.5
    ncaa_clean.loc["Kevin Porter Jr.","RPG"] = 4.0
    ncaa_clean.loc["Kevin Porter Jr.","APG"] = 1.4
    ncaa_clean.loc["Kevin Porter Jr.","SPG"] = 0.8
    ncaa_clean.loc["Kevin Porter Jr.","BPG"] = 0.5
    ncaa_clean.loc["Kevin Porter Jr.","TPG"] = 1.9
    ncaa_clean.loc["Kevin Porter Jr.","FGP"] = 0.471
    ncaa_clean.loc["Kevin Porter Jr.","3PG"] = 0.412
    #fixing Larry Nance Jr.
    ncaa_clean.loc["Larry Nance Jr.","Height"] = 80
    ncaa_clean.loc["Larry Nance Jr.","Weight"] = 235
    ncaa_clean.loc["Larry Nance Jr.","PPG"] = 11.3
    ncaa_clean.loc["Larry Nance Jr.","RPG"] = 6.6
    ncaa_clean.loc["Larry Nance Jr.","APG"] = 1.4
    ncaa_clean.loc["Larry Nance Jr.","SPG"] = 1.1
    ncaa_clean.loc["Larry Nance Jr.","BPG"] = 1.1
    ncaa_clean.loc["Larry Nance Jr.","TPG"] = 1.6
    ncaa_clean.loc["Larry Nance Jr.","FGP"] = 0.521
    ncaa_clean.loc["Larry Nance Jr.","3PG"] = 0.308
    #fixing Reggie Bullock
    ncaa_clean.loc["Reggie Bullock","Height"] = 79
    ncaa_clean.loc["Reggie Bullock","Weight"] = 205
    ncaa_clean.loc["Reggie Bullock","PPG"] = 9.9
    ncaa_clean.loc["Reggie Bullock","RPG"] = 5.0
    ncaa_clean.loc["Reggie Bullock","APG"] = 1.7
    ncaa_clean.loc["Reggie Bullock","SPG"] = 1.3
    ncaa_clean.loc["Reggie Bullock","BPG"] = 0.3
    ncaa_clean.loc["Reggie Bullock","TPG"] = 0.9
    ncaa_clean.loc["Reggie Bullock","FGP"] = 0.439
    ncaa_clean.loc["Reggie Bullock","3PG"] = 0.387
    #fixing Tim Hardaway Jr.
    ncaa_clean.loc["Tim Hardaway Jr.","Height"] = 78
    ncaa_clean.loc["Tim Hardaway Jr.","Weight"] = 205
    ncaa_clean.loc["Tim Hardaway Jr.","PPG"] = 14.3
    ncaa_clean.loc["Tim Hardaway Jr.","RPG"] = 4.1
    ncaa_clean.loc["Tim Hardaway Jr.","APG"] = 2.1
    ncaa_clean.loc["Tim Hardaway Jr.","SPG"] = 0.7
    ncaa_clean.loc["Tim Hardaway Jr.","BPG"] = 0.3
    ncaa_clean.loc["Tim Hardaway Jr.","TPG"] = 1.7
    ncaa_clean.loc["Tim Hardaway Jr.","FGP"] = 0.425
    ncaa_clean.loc["Tim Hardaway Jr.","3PG"] = 0.343
    #fixing Troy Brown Jr.
    ncaa_clean.loc["Troy Brown Jr.","Height"] = 78
    ncaa_clean.loc["Troy Brown Jr.","Weight"] = 205
    ncaa_clean.loc["Troy Brown Jr.","PPG"] = 14.3
    ncaa_clean.loc["Troy Brown Jr.","RPG"] = 4.1
    ncaa_clean.loc["Troy Brown Jr.","APG"] = 2.1
    ncaa_clean.loc["Troy Brown Jr.","SPG"] = 0.7
    ncaa_clean.loc["Troy Brown Jr.","BPG"] = 0.3
    ncaa_clean.loc["Troy Brown Jr.","TPG"] = 1.7
    ncaa_clean.loc["Troy Brown Jr.","FGP"] = 0.425
    ncaa_clean.loc["Troy Brown Jr.","3PG"] = 0.343
    #fixing Tyler Johnson
    ncaa_clean.loc["Tyler Johnson","Height"] = 76
    ncaa_clean.loc["Tyler Johnson","Weight"] = 186
    ncaa_clean.loc["Tyler Johnson","PPG"] = 10.5
    ncaa_clean.loc["Tyler Johnson","RPG"] = 4.8
    ncaa_clean.loc["Tyler Johnson","APG"] = 2.4
    ncaa_clean.loc["Tyler Johnson","SPG"] = 1.1
    ncaa_clean.loc["Tyler Johnson","BPG"] = 0.3
    ncaa_clean.loc["Tyler Johnson","TPG"] = 1.4
    ncaa_clean.loc["Tyler Johnson","FGP"] = 0.456
    ncaa_clean.loc["Tyler Johnson","3PG"] = 0.372
    #fixing Tyler Johnson
    ncaa_clean.loc["Tyler Johnson","Height"] = 76
    ncaa_clean.loc["Tyler Johnson","Weight"] = 186
    ncaa_clean.loc["Tyler Johnson","PPG"] = 10.5
    ncaa_clean.loc["Tyler Johnson","RPG"] = 4.8
    ncaa_clean.loc["Tyler Johnson","APG"] = 2.4
    ncaa_clean.loc["Tyler Johnson","SPG"] = 1.1
    ncaa_clean.loc["Tyler Johnson","BPG"] = 0.3
    ncaa_clean.loc["Tyler Johnson","TPG"] = 1.4
    ncaa_clean.loc["Tyler Johnson","FGP"] = 0.456
    ncaa_clean.loc["Tyler Johnson","3PG"] = 0.372
    #fixing Vince Carter
    ncaa_clean.loc["Vince Carter","RPG"] = 4.5
    ncaa_clean.loc["Vince Carter","TPG"] = 1.3
    #fixing Wendell Carter Jr.
    ncaa_clean.loc["Wendell Carter Jr.","Height"] = 82
    ncaa_clean.loc["Wendell Carter Jr.","Weight"] = 259
    ncaa_clean.loc["Wendell Carter Jr.","PPG"] = 13.5
    ncaa_clean.loc["Wendell Carter Jr.","RPG"] = 9.1
    ncaa_clean.loc["Wendell Carter Jr.","APG"] = 2.0
    ncaa_clean.loc["Wendell Carter Jr.","SPG"] = 0.8
    ncaa_clean.loc["Wendell Carter Jr.","BPG"] = 2.1
    ncaa_clean.loc["Wendell Carter Jr.","TPG"] = 2.0
    ncaa_clean.loc["Wendell Carter Jr.","FGP"] = 0.561
    ncaa_clean.loc["Wendell Carter Jr.","3PG"] = 0.413

    #dropping Lou Willima since he came straight out of HS
    ncaa_clean.drop(index='Lou Williams',inplace = True)

    #replace all of the -999 to nan
    ncaa_clean = ncaa_clean.replace(-999.0, np.nan)
    # ncaa_clean



    ncaa_clean.reset_index(inplace = True)



    #exporting the csv files in case of mongo failure
    #nba_clean.to_csv('static/assets/data/NBA_Data.csv', index = False)
    #ncaa_clean.to_csv('static/assets/data/NCAA_Data.csv', index = False)
    #nba_location.to_csv('static/assets/data/NBA_Location.csv', index = False)




    #Now putting these dataframes into local mongo database. So that app.py flask app can pull the data from Mongo and store them as csv's



    import pymongo

    conn = 'mongodb+srv://sabu:cp3@cluster0.suglk.mongodb.net/test'
    client = pymongo.MongoClient(conn)

    ncaa_clean = ncaa_clean.replace(np.nan, 0)

    # Declare the database
    db = client.NBA_NCAA
    db.NBA.drop()
    db.NCAA.drop()
    db.NBA_Location.drop()

    # Declare the collection
    NBA = db.NBA
    NCAA = db.NCAA
    NBA_Location = db.NBA_Location

    #Convert the NBA dataframe into a dictionary and insert into Mongo
    NBA_dict = nba_clean.to_dict('records')
    NBA.insert_many(NBA_dict)

    #Convert the NCAAl dataframe into a dictionary and insert into Mongo.

    NCAA_dict = ncaa_clean.to_dict('records')
    NCAA.insert_many(NCAA_dict)

    #Convert the NCAAl dataframe into a dictionary and insert into Mongo.
    NBA_Location_dict = nba_location.to_dict('records')
    NBA_Location.insert_many(NBA_Location_dict)

    print("Done. Data stored in Mongo")

if __name__ == "__main__":
    scrape_info()
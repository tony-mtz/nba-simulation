
import requests
import pandas as pd
from teamList import teamList
#load:
    #TeamData.py
    #PlayerData.py
    #sim

#used to get ids from team csv and then get each shot chart
#for each player in each team


class PlayerData:
    def __init__(self):
        
        self.userAgent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36"
        self.shot_chart_url0 = ("http://stats.nba.com/stats/shotchartdetail?AheadBehind=&CFID=33&"
                                 "CFPARAMS=2017-18&ClutchTime=&Conference=&ContextFilter=&Context"
                                 "Measure=FGA&DateFrom=&DateTo=&Division=&EndPeriod=10&EndRange=28800&"
                                 "GROUP_ID=&GameEventID=&GameID=&GameSegment=&GroupID=&GroupMode=&Group"
                                 "Quantity=5&LastNGames=0&LeagueID=00&Location=&Month=0&OnOff=&Opponent"
                                 "TeamID=0&Outcome=&PORound=0&Period=0&PlayerID=")
        
        self.shot_chart_url1 = ("&PlayerID1=&PlayerID2"
                                 "=&PlayerID3=&PlayerID4=&PlayerID5=&PlayerPosition=&PointDiff=&Position=&"
                                 "RangeType=0&RookieYear=&Season=2017-18&SeasonSegment=&SeasonType=Regular+"
                                 "Season&ShotClockRange=&StartPeriod=1&StartRange=0&StarterBench=&TeamID=0&Vs"
                                 "Conference=&VsDivision=&VsPlayerID1=&VsPlayerID2=&VsPlayerID3=&VsPlayerID4=&"
                                 "VsPlayerID5=&VsTeamID=")               
        self.teams = teamList
    
    def getPlayerData(self):      
        for j in self.teams:
            df = pd.read_csv('../2018/'+j[0]+'.csv')
            for i in df.PLAYER_ID:
                player = str(i)
                response = requests.get(self.shot_chart_url0 + player + 
                                        self.shot_chart_url1,headers={"USER-AGENT":self.userAgent})
                headers = response.json()['resultSets'][0]['headers']
                shots = response.json()['resultSets'][0]['rowSet']
            
                shot_df = pd.DataFrame(shots, columns=headers)
                shot_df.to_csv('../2018/'+player+'.csv')
                
import requests
import pandas as pd
#get team roster

class TeamData:
    def __init__(self):
        #add team ID at the end of this line
        self.url = "https://stats.nba.com/stats/commonteamroster?LeagueID=00&Season=2017-18&TeamID=" #example 1610612744
        self.userAgent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36"
        #team ids
        self.teams = [ ('lakers','1610612747'),
                     ('warriors', '1610612744'), 
                     ('celtics','1610612738'),
                     ('rockets', '1610612745'), 
                     ('kings','1610612758'), 
                     ('mavericks','1610612742'),
                     ('knicks', '1610612752'), 
                     ('bulls', '1610612741'), 
                     ('clippers', '1610612746'),
                     ('nets','1610612751'),
                     ('76ers', '1610612755'),
                     ('raptors', '1610612761'),
                     ('cavaliers', '1610612739'),
                     ('pistons', '1610612765'),
                     ('pacers', '1610612754'),
                     ('bucks', '1610612749'),
                     ('hawks', '1610612737'),
                     ('hornets', '1610612766'),
                     ('heat', '1610612748'),
                     ('magic', '1610612753'),
                     ('wizards', '1610612764'),
                     ('nuggets', '1610612743'),
                     ('timberwolves', '1610612750'),
                     ('thunder', '1610612760'),
                     ('trail blazers', '1610612757'),
                     ('jazz', '1610612762'),
                     ('suns', '1610612756'),
                     ('grizzlies', '1610612763'),
                     ('pelicans', '1610612740'),
                     ('spurs', '1610612759')
                     ]
    
    '''
    Gets roster information for each team and saves it
    in a csv file under a folder named '2018'
    '''
    def getData(self):
        for i in self.teams:
            response = requests.get(self.url+i[1],headers={"USER-AGENT":self.userAgent})
            headers = response.json()['resultSets'][0]['headers']
            team = response.json()['resultSets'][0]['rowSet']
        
            team_df = pd.DataFrame(team, columns=headers)
            team_df.to_csv('../2018/' + i[0]+'.csv')    
    
     #box score
    def getGamesPlayedBox(self):
        url = ("https://stats.nba.com/stats/teamgamelog?DateFrom=&DateTo=&"
               "LeagueID=00&Season=2017-18&SeasonType=Regular+Season&TeamID=") #1610612744
        
        for i in self.teams:
            response = requests.get(url+i[1],headers={"USER-AGENT":self.userAgent})
            headers = response.json()['resultSets'][0]['headers']
            team = response.json()['resultSets'][0]['rowSet']
        
            team_df = pd.DataFrame(team, columns=headers)
            team_df.to_csv('../teamGames/' + i[0]+'.csv')
            
    def loadTeamBox(self,teamName):
        stats_df = pd.read_csv('../teamGames/'+teamName+'.csv')
    #    teamStats = stats_df.loc[stats_df['TEAM_ID']==teamID]
        return stats_df 
    
    #per game
    def getTeamStats(self):
        team_stats = ("https://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division="
                      "&GameScope=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&"
                      "OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience="
                      "&PlayerPosition=&PlusMinus=N&Rank=N&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season"
                      "&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=")                         
        
        response = requests.get(team_stats,headers={"USER-AGENT":self.userAgent})
        headers = response.json()['resultSets'][0]['headers']
        stats = response.json()['resultSets'][0]['rowSet']            
        stats_df = pd.DataFrame(stats, columns=headers)
        stats_df.to_csv('../2018/'+'teamstats'+'.csv')
    
    #per game
    def loadTeamStats(self, teamID):
        stats_df = pd.read_csv('2018/'+'teamstats'+'.csv')
        teamStats = stats_df.loc[stats_df['TEAM_ID']==teamID]
        return teamStats
  
    #per 100 pos
    def getTeamStats100(self):
        team_stats = ("https://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division=&"
                      "GameScope=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&"
                      "OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Per100Possessions&Period=0&"
                      "PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2017-18&SeasonSegment=&"
                      "SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=")        
        
        response = requests.get(team_stats,headers={"USER-AGENT":self.userAgent})
        headers = response.json()['resultSets'][0]['headers']
        stats = response.json()['resultSets'][0]['rowSet']
            
        stats_df = pd.DataFrame(stats, columns=headers)
        stats_df.to_csv('../2018/'+'teamstats100'+'.csv')
    
    def loadTeamStats100(self,teamID):
        stats_df = pd.read_csv('2018/'+'teamstats100'+'.csv')
        teamStats = stats_df.loc[stats_df['TEAM_ID']==teamID]
        return teamStats

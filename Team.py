

import pandas as pd
from Player import Player
import numpy as np
import matplotlib.pyplot as plt
#from teamstats import loadTeamStats
#from teamstats100 import loadTeamStats100
from utility.TeamData import TeamData

year = '2018/' #can change to folder csv is in
#example lakers:1610612747
class Team:
    def __init__(self, teamName):
        self.teamName = teamName
        self.df = pd.read_csv(year+teamName+'.csv')
        self.playerIDS = self.df.PLAYER_ID
        self.roster = {} #player objects
        self.teamTotalShots = 0 #total number of shots taken by the team
        self.shotDistPerPlayer = [] #player shot distribution
        self.clock = []
        self.shotQ = []
        self.fga = 0
        self.data = TeamData()
        self.teamStats = None
        self.loadTeamStats()
        self.teamStats100 = None
        self.loadTeamStats100()
        
        
#        self.shotdist = np.random.choice(self.playerIDS, p= self.shotDistPerPlayer)
        self.loadRoster()
        self.teamTotalShotAttempts()
        self.shotDist()
        
    def loadRoster(self):
        for i in self.playerIDS:
            player = {i: Player(i)}
            self.roster.update(player)
        
    def teamTotalShotAttempts(self):
        count =0
        for i in self.roster:
            count += self.roster[i].totalShots
        
        self.teamTotalShots = count
        
    def shotDist(self):
        li = []
        for i in self.roster:
            li.append(self.roster[i].totalShots/self.teamTotalShots)
        self.shotDistPerPlayer = li
        
    #take a shot 
    #the player ID will be returned
    #you need to then reach into the player shooting chart
    def pickShooter(self):
        return np.random.choice(self.playerIDS, p= self.shotDistPerPlayer)
    
    def loadTeamStats(self):
        self.teamStats = self.data.loadTeamStats(self.df['TeamID'][0])      
        #usage:
        #teamName.teamStats['FGA']
        
    def loadTeamStats100(self):
        self.teamStats100 = self.data.loadTeamStats100(self.df['TeamID'][0])      
        
    def scat(self):
        tot = []
        for i in range(25):
            tot.append(0)
            
        for i in range(10000):
            t = self.getShotClock()
            print(t)
            tot[t] +=1
            
        x = list(range(25))
        plt.scatter(x,tot)
        plt.show()
        
        
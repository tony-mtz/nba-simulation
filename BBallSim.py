
from Team import Team
import numpy as np

class BBallSim:
    def __init__(self, teamA, teamB):
        self.teamA = Team(teamA)
        self.teamB = Team(teamB)
        self.score = [0,0]
        self.statsA = []
        self.statsB = []
        
    #resets scores after a simulation
    def resetScore(self):
        self.score[0] =0
        self.score[1] = 0            
            

        
    def gameLoop(self):
        self.score[0] = self.singleLoop(100, self.teamA)
        self.score[1] = self.singleLoop(107, self.teamB)

    def singleLoop(self, possAmount, team): 
        score = 0             
        while possAmount >0:
            tov = team.teamStats100['TOV'].values[0]
            result_TOV = np.random.choice([0,1], p=[1-(tov/100) , tov/100] )
            if result_TOV == 1:
                possAmount -=1
                continue
            shooter = team.pickShooter()
            shot, loc = team.roster[shooter].takeShot()
            blka = team.teamStats100['BLKA'].values[0]
            result_BLKA =  np.random.choice([0,1], p=[1-(blka/100) , blka/100] )
            if result_BLKA == 1:
                chance = np.random.choice([0,1])
                if chance == 1: #1 is turnover
                    possAmount -= 1
                    continue
            if shot ==1:
                if loc >8:
                    score += 3
                else:
                    score += 2
            else:
                oreb = team.teamStats100['OREB'].values[0]
                result_OREB = np.random.choice([0,1], p=[1-(oreb/100) , oreb/100] )
                if result_OREB == 1:
                    possAmount +=1
                    continue
            possAmount -=1
        #add free throws         
        ft = team.teamStats100['FTM'].values[0]
        score += round(ft)
        return score
        















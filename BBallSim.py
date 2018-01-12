from Team import Team
import numpy as np

class BBallSim:
    def __init__(self, teamA, teamB):
        self.teamA = Team(teamA)
        self.teamB = Team(teamB)
        self.score = [0,0]
        
    #resets scores after a simulation
    def resetScore(self):
        self.score[0] =0
        self.score[1] = 0
        
    def gameLoop(self):
        #team A is away and team B is home
        #home team gets possession advantage 
        self.score[0] = self.singleLoop(100, self.teamA)
        self.score[1] = self.singleLoop(107, self.teamB)
        
    #simulates team's possessions
    #teamStats100 are based on per 100 possessions statistics
    def singleLoop(self, possAmount, team): 
        score = 0             
        while possAmount >0:
            #check the turn over rate of the team
            #if the ball is turned over then end the possession
            tov = team.teamStats100['TOV'].values[0]
            result_TOV = np.random.choice([0,1], p=[1-(tov/100) , tov/100] )
            if result_TOV == 1:
                possAmount -=1
                continue
            #pick a shooter based on the team's shot distribution            
            shooter = team.pickShooter()
            #pick a shot location bashed on the shooters distribution
            shot, loc = team.roster[shooter].takeShot()
            #check if the shot is blocked, if it is then end the possession
            blka = team.teamStats100['BLKA'].values[0]
            result_BLKA =  np.random.choice([0,1], p=[1-(blka/100) , blka/100] )
            if result_BLKA == 1:
                chance = np.random.choice([0,1])
                if chance == 1: #1 is turnover
                    possAmount -= 1
                    continue
            #if the shot is not blocked then check if the shot was made
            if shot ==1:
                #if the shot was made check the location of the shot to 
                #see if it was a 3 pointer or 2 pointer
                if loc >8:
                    score += 3
                else:
                    score += 2
            else:
                #if the shot was made then restart the possession
                oreb = team.teamStats100['OREB'].values[0]
                result_OREB = np.random.choice([0,1], p=[1-(oreb/100) , oreb/100] )
                if result_OREB == 1:
                    continue
            possAmount -=1
        #add free throws         
        ft = team.teamStats100['FTM'].values[0]
        score += round(ft)
        return score
        















#load teams
from Team import Team
import numpy as np

#give home team the tip ball
class BBallSim:
    def __init__(self, teamA, teamB):
        self.teamA = Team(teamA)
        self.teamB = Team(teamB)
        self.score = [0,0]
        self.statsA = []
        self.statsB = []
        
    def resetScore(self):
        self.score[0] =0
        self.score[1] = 0
    
        
    def simLoop(self):        
        
        for i in range(7700):
                 
            shooter = self.teamA.pickShooter()
            shot, loc = self.teamA.roster[shooter].takeShot()
#            print(f"team a shooter: {self.teamA.roster[shooter].playerID}")
            if shot ==1:
                if loc >8:
                    self.score[0]+=3
                else:
                    self.score[0]+=2
                    
        print(self.score[0]/100)
        
            
    def possession(self, env, offense, defense):
        yield env.timeout(offense.getShotClock())
        
    
    def genPoss(self):
        
#        df_A = loadTeamBox(self.teamA.teamName)
        posA = 100
        
        while posA >0:
            tov = self.teamA.teamStats100['TOV'].values[0]
            result_TOV = np.random.choice([0,1], p=[1-(tov/100) , tov/100] )
            if result_TOV == 1:
                posA -=1
                continue
            shooter = self.teamA.pickShooter()
            shot, loc = self.teamA.roster[shooter].takeShot()
            blka = self.teamA.teamStats100['BLKA'].values[0]
            result_BLKA =  np.random.choice([0,1], p=[1-(blka/100) , blka/100] )
            if result_BLKA ==1:
                chance = np.random.choice([0,1])
                if chance == 1: #1 is turnover
                    posA -=1
                    continue
            if shot ==1:
                if loc >8:
                    self.score[0]+=3
                else:
                    self.score[0]+=2
            else:
                oreb = self.teamA.teamStats100['OREB'].values[0]
                result_OREB = np.random.choice([0,1], p=[1-(oreb/100) , oreb/100] )
                if result_OREB == 1:
                    posA +=1
                    continue
            posA -=1
        #add free throws         
        ft = self.teamA.teamStats100['FTM'].values[0]
        self.score[0] += round(ft)
                    
        posB = 107       
        while posB >0:
            tov = self.teamB.teamStats100['TOV'].values[0]
            result_TOV = np.random.choice([0,1], p=[1-(tov/100) , tov/100] )
            if result_TOV == 1:
                posB -=1
                continue
            shooter = self.teamB.pickShooter()
            shot, loc = self.teamB.roster[shooter].takeShot()
            blka = self.teamB.teamStats100['BLKA'].values[0]
            result_BLKA =  np.random.choice([0,1], p=[1-(blka/100) , blka/100] )
            if result_BLKA ==1:
                chance = np.random.choice([0,1])
                if chance == 1: #1 is turnover
                    posB -=1
                    continue
            if shot ==1:
                if loc >8:
                    self.score[1]+=3
                else:
                    self.score[1]+=2
            else:
                oreb = self.teamB.teamStats100['OREB'].values[0]
                result_OREB = np.random.choice([0,1], p=[1-(oreb/100) , oreb/100] )
                if result_OREB == 1:
                    posB +=1
                    continue
            posB -=1
            
        ftb = self.teamB.teamStats100['FTM'].values[0]
        self.score[1] += round(ftb)
        #print(self.score)
        self.statsA.append(self.score[0])
        self.statsB.append(self.score[1])
            
    def sim(self, env):
        r = self.simLoop(env)
        env.process(r)
        




















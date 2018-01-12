# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 21:15:09 2017

@author: tonyd
"""

import numpy as np
#from loadplayer import loadPlayer

import pandas as pd

year = '2018/'
class Player:
    def __init__(self, playerID ):
        self.playerID = playerID
        self.playerName = None
        self.stats = self.loadPlayer(playerID)
        self.totalShots = self.totShots()
        self.zones_list = [(u'Less Than 8 ft.', u'Center(C)'),
                           (u'8-16 ft.', u'Center(C)'),
                           (u'8-16 ft.', u'Left Side(L)'),
                           (u'8-16 ft.', u'Right Side(R)'),
                           (u'16-24 ft.', u'Center(C)'),
                           (u'16-24 ft.', u'Left Side Center(LC)'),
                           (u'16-24 ft.', u'Left Side(L)'),
                           (u'16-24 ft.', u'Right Side Center(RC)'),
                           (u'16-24 ft.', u'Right Side(R)'),
                           (u'24+ ft.', u'Center(C)'),
                           (u'24+ ft.', u'Left Side Center(LC)'),
                           (u'24+ ft.', u'Left Side(L)'),
                           (u'24+ ft.', u'Right Side Center(RC)'),
                           (u'24+ ft.', u'Right Side(R)'),
                           (u'Back Court Shot', u'Back Court(BC)')]
        self.shotChart = []
        self.shotAccuracy = []
        self.shotChartDist()
        self.shotAccur()
#        self.getPlayerName()
        
    
    
    #total shots taking by the player from all locations
    def totShots(self):
        count =0
        shotList = [count+a[1] for a in self.stats]
        return sum(shotList)
    
    def getPlayerName(self):
        df = pd.read_csv(year+str(self.playerID) + '.csv')
        self.playerName = df.PLAYER_NAME[0]
        #print(self.playerName)
    
    def shotChartDist(self):
        for i in self.stats:
            if self.totalShots >0:
                self.shotChart.append(i[1]/self.totalShots)
            else:
                self.shotChart.append(0)

    def shotAccur(self):
        for i in self.stats:
            if i[1]>0:
                self.shotAccuracy.append(i[0]/i[1])
            else:
                self.shotAccuracy.append(0)
    
    def takeShot(self):
        pickLocation = np.random.choice(list(range(15)), p = self.shotChart)
        makemiss = self.shotAccuracy[pickLocation]
        shot = np.random.choice([0,1],p=[1-makemiss, makemiss])
#        print(f"shot made?:{shot} from {self.zones_list[pickLocation]}")
        #print(makemiss)
        return shot, pickLocation
        
    
    
    def loadPlayer(self, playerID):
        year = '2018/'
        playerID = str(playerID)
        df = pd.read_csv(year +playerID + '.csv')
        #3 feet is restricted area
        
        stats = []
        for i in range(15):
            stats.append([0,0])
            
        for i,j,k in zip(df.SHOT_ZONE_RANGE,df.SHOT_ZONE_AREA, df.SHOT_MADE_FLAG):
            if i == self.zones_list[0][0] and j == self.zones_list[0][1]:
                stats[0][1] +=1
                if k:
                    stats[0][0] +=1  
            
            if i == self.zones_list[1][0] and j == self.zones_list[1][1]:
                stats[1][1] +=1
                if k:
                    stats[1][0] +=1 
                    
            if i == self.zones_list[2][0] and j == self.zones_list[2][1]:
                stats[2][1] +=1
                if k:
                    stats[2][0] +=1 
            
            if i == self.zones_list[3][0] and j == self.zones_list[3][1]:
                stats[3][1] +=1
                if k:
                    stats[3][0] +=1 
                    
            if i == self.zones_list[4][0] and j == self.zones_list[4][1]:
                stats[4][1] +=1
                if k:
                    stats[4][0] +=1 
                    
            if i == self.zones_list[5][0] and j == self.zones_list[5][1]:
                stats[5][1] +=1
                if k:
                    stats[5][0] +=1 
                    
            if i == self.zones_list[6][0] and j == self.zones_list[6][1]:
                stats[6][1] +=1
                if k:
                    stats[6][0] +=1 
                    
            if i == self.zones_list[7][0] and j == self.zones_list[7][1]:
                stats[7][1] +=1
                if k:
                    stats[7][0] +=1 
                    
            if i == self.zones_list[8][0] and j == self.zones_list[8][1]:
                stats[8][1] +=1
                if k:
                    stats[8][0] +=1 
                    
            if i == self.zones_list[9][0] and j == self.zones_list[9][1]:
                stats[9][1] +=1
                if k:
                    stats[9][0] +=1 
            
            if i == self.zones_list[10][0] and j == self.zones_list[10][1]:
                stats[10][1] +=1
                if k:
                    stats[10][0] +=1  
            
            if i == self.zones_list[11][0] and j == self.zones_list[11][1]:
                stats[11][1] +=1
                if k:
                    stats[11][0] +=1 
                    
            if i == self.zones_list[12][0] and j == self.zones_list[12][1]:
                stats[12][1] +=1
                if k:
                    stats[12][0] +=1 
            
            if i == self.zones_list[13][0] and j == self.zones_list[13][1]:
                stats[13][1] +=1
                if k:
                    stats[13][0] +=1 
                    
            if i == self.zones_list[14][0] and j == self.zones_list[14][1]:
                stats[14][1] +=1
                if k:
                    stats[14][0] +=1 
        #            
        for i in range(9):
            stats[i].append(2)
        for i in range(9,15):
            stats[i].append(3)
            
    #    print(stats)
    #    for i in stats:
    #        if i[1]>0:
    #             print(i[0]/i[1])
    #        else:
    #            print(0)     
        return stats
    
    
    
#keep this for now
#to verify player simulation
    
#dur = Player(202326)
#
#shotS =[]
#locationS = []
#for i in range(1000):
#    shotS, locationS = dur.takeShot()
#    
#
#
#stats = []
#for i in range(15):
#    stats.append([0,0])
#    
#for z in range(1000):
#    k, i = dur.takeShot()
#    if i == 0:
#        stats[0][1] +=1
#        if k ==1 :
#            stats[0][0] +=1  
#    
#    if i == 1:
#        stats[1][1] +=1
#        if k:
#            stats[1][0] +=1 
#            
#    if i == 2:
#        stats[2][1] +=1
#        if k:
#            stats[2][0] +=1 
#    
#    if i == 3:
#        stats[3][1] +=1
#        if k:
#            stats[3][0] +=1 
#            
#    if i == 4:
#        stats[4][1] +=1
#        if k:
#            stats[4][0] +=1 
#            
#    if i == 5:
#        stats[5][1] +=1
#        if k:
#            stats[5][0] +=1 
#            
#    if i == 6:
#        stats[6][1] +=1
#        if k:
#            stats[6][0] +=1 
#            
#    if i == 7:
#        stats[7][1] +=1
#        if k:
#            stats[7][0] +=1 
#            
#    if i == 8:
#        stats[8][1] +=1
#        if k:
#            stats[8][0] +=1 
#            
#    if i == 9:
#        stats[9][1] +=1
#        if k:
#            stats[9][0] +=1 
#    
#    if i == 10:
#        stats[10][1] +=1
#        if k:
#            stats[10][0] +=1  
#    
#    if i == 11:
#        stats[11][1] +=1
#        if k:
#            stats[11][0] +=1 
#            
#    if i == 12:
#        stats[12][1] +=1
#        if k:
#            stats[12][0] +=1 
#    
#    if i == 13:
#        stats[13][1] +=1
#        if k:
#            stats[13][0] +=1 
#            
#    if i == 14:
#        stats[14][1] +=1
#        if k:
#            stats[14][0] +=1 
##            
#for i in range(9):
#    stats[i].append(2)
#for i in range(9,15):
#    stats[i].append(3)
#    
#    print(stats)
#    for i in stats:
#        if i[1]>0:
#             print(i[0]/i[1])
#        else:
#            print(0)





#for i in 
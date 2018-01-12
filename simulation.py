# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 22:54:02 2018

@author: tonyd
"""

#run simulation
import numpy as np
from scipy.stats import norm
from BBallSim import BBallSim

matches = [('warriors', 'clippers'),
           ('celtics', 'nets'),
           ('rockets', 'pistons'),
           ('bulls', 'pacers'),           
           ('cavaliers', 'magic'),
           ('bucks', 'wizards'),
           ('pelicans', 'timberwolves'),
           ('nuggets', 'kings')
           ]
#ends at 3 jan

f = open('jan61.txt', 'w')
for i in matches:
    win = 0
    team1 = i[0]
    team2 = i[1]

    amount = 500
    score1 =0
    score2 =0
    
    percT1 =0
    percT2=0
    sim = BBallSim(team1, team2)
    for i in range(amount):
    #    sim = BBallSim(team1, team2)
        
        sim.gameLoop()
        if sim.score[0] >sim.score[1]:
            percT1 += 1
        if sim.score[1] >sim.score[0]:
            percT2 +=1
        
        score1 += sim.score[0]
        score2 += sim.score[1]        
        sim.resetScore() 
    
    f.write(f"{team1}         {score1/amount}   {100*(percT1/amount)}% \n")
    f.write(f"{team2}         {score2/amount}   {100*(percT2/amount)}% \n")
    #print(f"{score1/amount +score2/amount }")
    f.write(f"({round(score1/amount -score2/amount) })\n")
    p = (percT1/amount) * (1-(percT1/amount))/np.sqrt(amount)
    inter = norm.ppf(.95)*p
    Lconf = (percT1/amount) - inter
    Rconf = (percT1/amount) + inter
    f.write(f"90% confidence interval : {Lconf*100} and {Rconf*100} \n")
    
    p2 = (percT2/amount) * (1-(percT2/amount))/np.sqrt(amount)
    inter2 = norm.ppf(.95)*p2
    Lconf2 = (percT2/amount) - inter2
    Rconf2 = (percT2/amount) + inter2
    f.write(f"90% confidence interval : {Lconf2*100} and {Rconf2*100} \n")
    f.write('..\n')
    f.write('..\n')
    print('....working')
print('...done')
f.close()
    



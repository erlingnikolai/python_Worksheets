# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 12:21:45 2016

@author: enu
"""

import numpy as np


#variables
forest_means = []
amazon = 2.5
simulation = 1000
five_percent = (int(simulation/20))
trees = 100



def ws1one():
    s = np.random.uniform(0.5,5,trees)
    print(np.mean(s))



def ws1two():    
    for x in range(0, simulation):
        s = np.random.uniform(0.5,5,trees)
        forest_means.append(np.mean(s))
    print ("the lowest value of the mean is " + str(min(forest_means)))
forest_means = sorted(forest_means)

def ws1three():
    if amazon <= forest_means[50]:
        
        print(str(amazon) + " is lower than the 5% " + str(forest_means[five_percent]))
    else:
        print(str(amazon) + " is higher than the 5% " + str(forest_means[five_percent]))
    

    

ws1one()
ws1two()
ws1three()
    
def printstuff():
    print(min(forest_means))
    print(max(forest_means))
    print(np.mean(forest_means))    
#printstuff()

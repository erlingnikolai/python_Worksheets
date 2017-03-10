# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:21:31 2017

@author: enu
"""
import random as r
import pandas as pd

    
#print (test)

myset = []

def luckyTip():
    for i in range(5):
        myset.append(r.randint(1,59))

    print(myset)
    
    
    
def compare():
    url = "https://www.national-lottery.co.uk/results/lotto/draw-history/csv"
    data_brain = pd.read_csv(url, na_values=".")
    test = data_brain.loc[:, "Ball 1":"Ball 6"]
    for x, row in test.iterrows():
        print(row)
        
    
 
        
    
    
    
    
luckyTip()
compare()

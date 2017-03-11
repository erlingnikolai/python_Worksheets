# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:21:31 2017

@author: enu
"""
import random as r
import pandas as pd

    

mySet = []


def luckyTip():
    for i in range(6):
        mySet.append(r.randint(1,59))


def compare():
    url = "https://www.national-lottery.co.uk/results/lotto/draw-history/csv"
    data_brain = pd.read_csv(url, na_values=".")
    test = data_brain.loc[:, "Ball 1":"Ball 6"]
    for x, row in test.iterrows():
        lottoSet = []
        lottoSet.extend((row["Ball 1"], row["Ball 2"], row["Ball 3"], row["Ball 4"], row["Ball 5"], row["Ball 6"]))
        if len(set(lottoSet)& set(mySet)) == 4:
            print ("4/6")

        if len(set(lottoSet)& set(mySet)) == 5:
            print ("5/6")
        if set(lottoSet).issubset(set(mySet)):
            print ("YOU WON !!!")


luckyTip()

for x in range(1000000000000):
    mySet = []
    luckyTip()
    compare()
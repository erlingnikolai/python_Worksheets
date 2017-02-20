import pandas as pd
import random as r

#1
def WS10one():
    url = "http://chart.finance.yahoo.com/table.csv?s=GOOG"
    data_brain = pd.read_csv(url, na_values=".")
    print (data_brain)
    data_brain.loc [:, "Open":"Close"].plot()


def WS10two():
    for i in range(5):
        print(r.randint(1,10))

def WS10three():
    listofzeroes = [0] * 6
    for i in range(10000):
        temp = r.randint(1,6)
        listofzeroes[temp-1] = listofzeroes[temp-1]+1
    print (listofzeroes)
    for i in range(6):
        print(str(i+1) + " = " +str(listofzeroes[i]/100) + "%")
        
        
def WS10four():
    deck = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
    for i in range(5):
        r.shuffle(deck)
        print(deck)
 
def WS10five():
    deck1 = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
    for i in range(5):
        deck2 =r.sample(deck1, k=4)
        print (deck2)
        
def WS10six():
   deck1 = 'CA C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK DA D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK HA H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK SA S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK'.split()
   player1 =r.sample(deck1, k=5)
   player2 =r.sample(deck1, k=5)
   player3 =r.sample(deck1, k=5)
   player4 =r.sample(deck1, k=5)
   print(player1)
   print(player2)
   print(player3)
   print(player4)
#WS10one()
#WS10two()   
#WS10three()
#WS10four()
#WS10five()
WS10six()
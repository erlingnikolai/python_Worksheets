stock = {
    "apple": 10,
    "strawberry": 35,
    "orange": 9,
    "beetroot": 20,
    "carrot": 13
}

prices = {
    "apple": 1.4,
    "strawberry": 2.0,
    "orange": 1.0,
    "beetroot": 2.5,
    "carrot": 1.2
}

cymraeg = {
    "apple": "afal",
    "strawberry": "mefys",
    "orange": "oren",
    "beetroot": "betys",
    "carrot": "moron"
}

customer1 = ["apple", "orange", "apple", "beetroot", "beetroot"]

        
def replaceSymbols(test):
    symbols = " {}',w"
    for x in symbols:
        if x == ",":
            test = test.replace(x, " | ")
        else:   
            test = test.replace(x, "")w
    return test





def ws1():
    num1 =  input('What is your first number: ')
    num2 =  input('What is your second number: ')
    print(float(num1)*float(num2))
    
def ws2a():
    all = 0
    print("name        stock    buy 1    buy all")
    for x in sorted(stock.keys()):
        print (str(x).ljust(12) + str(stock[x]).ljust(10) + str(prices[x]).ljust(9) +
           str(stock[x] * prices[x]))
        all += stock[x] * prices[x]
    print ("the value of every smoothie in the stock is " + str(all))

def ws2b():      
    cus1 = 0
    for x in stock:
        for y in customer1:
            if x == y:
                stock[x] -= 1
                cus1 += prices[x]          
    print("customer1 would need to pay " + str(cus1))

         
def ws2c():  
    englishName = input('what is the name of the new smoothie in english: ')    
    welshName = input('what is the name of the new smoothie in welsh: ')
    value = input("how much is the value of 1 " + str(englishName) + ":")
    howMany = input("how many " + str(englishName) + " would you like to put in the stock:")
    stock[englishName] = howMany
    prices[englishName] = value
    cymraeg[englishName] =  welshName
    print("  stock \n| "   + replaceSymbols(str(stock)) + " |")
    print("  prices \n| "  +  replaceSymbols(str(prices)) + " |")
    print("  cymraeg \n| " +  replaceSymbols(str(cymraeg)) + " |")
    
def ws2d():
    print("    SMOOTHIES")
    for x in stock:
        print(cymraeg[x].ljust(15) + " £" + str(prices[x]))
    print("    SMWDDIS")
    for x in stock:
        print(x.ljust(15) + " £" + str(prices[x]))
    
while True:    
    
    ws = input('ws1 ws2a ws2b ws2c ws2d: ')
    if ws == "ws1":
        ws1()
    elif ws == "ws2a":
        ws2a()
    elif ws == "ws2b":
        ws2b()
    elif ws == "ws2c":
        ws2c()
    elif ws == "ws2d":
        ws2d()
    elif ws == "quit":
        break  
    else:
        print("there is no command named " + ws)

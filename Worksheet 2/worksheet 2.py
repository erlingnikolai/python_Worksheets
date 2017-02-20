#imports
import math



# 1.
town = "ABERYSTWYTH"
count = 0;

if town.lower().endswith("yth"):
    print("hooray")
print("there are " + str(town.lower().count("y")) + " Y in aberystwyth");
print("there are " + str(len(town)) + " letters in aberystwyth")


# 2.
depth = 20
radius = 14
volume = math.pi * radius ** 2 * depth 

if volume < 12000:
    print ("the volume is " + str(volume) + " and is lower than 12000")
if volume > 15000:
    print ("the volume is " + str(volume) + " and is greater than 15000")
else:
    print ("the volume is " + str(volume) + " it is between 12000 and 15000")
    

# 3.
switch1 = False
switch2 = True
if switch1 != switch2:
    print("on")
else:
    print("off")

# 4.a
setFor = 0
print("for loop")
for x in range(0, 75):
    setFor +=  1.0/( 2 ** x)
    print(str("%.20f" % setFor) + " set " + str(x))
    if setFor == 2.0:
        break
 
# 4.b
setWhile = 0
x = 0
print("while loop")
while (setWhile < 2.0):
    setWhile += 1.0/(2 ** x)
    print(str("%.20f" % setWhile) + " set " + str(x))
    x = x + 1

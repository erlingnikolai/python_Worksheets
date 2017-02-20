#2d list.....
aberystwyth_farms = [
    ["oats", "oats", "wheat", "wheat", "wheat"],
    ["hay", "wheat", "wheat", "wheat"],
    ["potatoes", "potatoes", "potatoes"],
    ["barley", "wheat", "hay", "barley", "wheat", "hay"],
    ["potatoes", "turnips", "potatoes", "turnips", "potatoes", "turnips"],
    ["barley"],
    ["wheat", "wheat", "turnips", "turnips", "turnips"]
]

hereford_farms = [
    ["barley", "barley", "oats", "oilseedrape", "barley"],
    ["oilseedrape", "barley", "oats"],
    ["barley", "barley", "barley", "oats", "barley", "barley"],
    ["barley", "cabbage", "oilseedrape", "barley", "barley", "cabbage"],
    ["oilseedrape", "oats", "oats", "oilseedrape", "oats"],
    ["oats", "cabbage"]
]

aber = set(x for y in aberystwyth_farms for x in y)
hereford = set(x for y in hereford_farms for x in y)
print ("Aberystwyth \n " + str(sorted(aber))) #3a
print (" \nHereford \n " +  str(sorted(hereford))) #3a
print (" \nboth towns \n" + str(aber.intersection(hereford))) #3b
print (" \only in Hereford \n" + str(aber - hereford)) #3c
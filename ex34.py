# ex34: Accessing elements of lists

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
print animals

#print "The animal at 1: %s" % animals[1] # python
#print "The 3rd animal:  %s" % animals[2] # peacock
#print "The 1st animal:  %s" % animals[0] # bear
#print "The animal at 3: %s" % animals[3] # kangaroo
#print "The 5th animal:  %s" % animals[4] # whale
#print "The animal at 2: %s" % animals[2] # peacock
#print "The 6th animal:  %s" % animals[5] # platypus
#print "The animal at 4: %s" % animals[4] # whale

# or, to find the positions and order of all entries:
def printAnimal(place):
    if place == 1:
        num2en = "1st"
    elif place == 2:
        num2en = "2nd"
    elif place == 3:
        num2en = "3rd"
    else:
        num2en = str(place)+"th"
    print "The %s animal is at %d and is a %s." % (
        num2en, place-1, animals[place-1])
    print "The animal at %d is the %s animal and is a %s." % (
        place-1, num2en, animals[place-1])


for i in range(1, len(animals)+1):
    printAnimal(i)

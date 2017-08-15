# ex 31: Making Decisions

print """You enter a dark rom with three doors.
 Do you go through door #1, door #2, or door #3?"""

door = raw_input("> ")

if door == "1":
    print "\nThere's a giant bear here eating a cheesecake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "\nThe bear eats your face off. Good job!"
    elif bear == "2":
        print "\nThe bear eats your legs off. Good job!"
    else:
        print "\nWell, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "\nYou stare into the endless abyss at Cthulu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "\nYour body survives powered by a mind of jello. Good job!"
    else:
        print "\nThe insanity rots your eyes into a pool of muck. Good job!"

elif door =="3":
    print "\nYou are asked to select one pill from two and take it."
    print "One is red, and the other is blue."
    print "1. Take the red pill."
    print "2. Take the blue pill."

    pill = raw_input("> ")

    if pill == "1":
        print "\nYou wake up to find this is just a dream. Good job!"
    elif pill == "2":
        print "\nIt's poisonous and you die. Good job!"
    else:
        "The person gets mad and kills you. Good job!"

else:
    print "\nYou wake up and find this is just a ridiculous dream."
    print """However you feel a great pity that you did enter a room
    to find out what would happen!"""

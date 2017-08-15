# ex30: Else and if

# assign 30 to variable 'people'
people = 30
# assign 40 to variable 'cars'
cars = 40
# assign 15 to variable 'buses'
buses = 15

# if the number of cars is greater than the number of people
if cars > people:
    print "We should take the cars."
# if the number of cars is less than the number of people
elif cars < people:
    print "We should not take the cars."
# if neither of these is true i.e. if number of cars & people are equal
else:
    print "We can't decide."

# if there are more buses than cars
if buses > cars:
    print "That's too many buses."
# if there are fewer buses than cars
elif buses < cars:
    print "Maybe we could take the buses"
# if neither of the above, i.e. buses == cars
else:
    print "We still can't decide."

# if there are more people than buses
if people > buses:
    print "All right, let's just take the buses."
# if fewer or equal people to buses
else:
    print "Fine, let's stay home then."

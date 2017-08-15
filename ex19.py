# ex19: Functions and varables

# define a function to print how many cheeses and crackers there are
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# out of function, back in main script
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
# define amount_of_cheese and amount_of_crackers as variables
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do maths inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and maths:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def typesofcake(cake1,cake2,cake3):
    print "We have %s, %s, and %s." % (cake1, cake2, cake3)
    mycake = raw_input("Which would you like? ")
    if mycake in (cake1, cake2, cake3):
        print "Good choice - %s it is!" % mycake
    else:
        print "Sorry, we don't have %s. Better luck next time." % mycake

wantcake = raw_input("Would you like some cake? [y/n] ")
if wantcake == 'y':
    typesofcake('Victoria sponge','Red velvet','Vanilla slice')
else:
    print "I have nothing to say to you."


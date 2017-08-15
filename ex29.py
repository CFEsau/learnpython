# ex29: What if

people = 20
cats = 30
dogs = 15

# An if statement creates a "branch" in the code.
# If the boolean expression is true then run the code, otherwise skip.
# The colon indicates a new block of code, and anything
# that is indented underneath is part of that block.
if people < cats:
    print "Many cats! The world is saved!"

if people > cats:
    print "Not many cats! The world is doomed!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."


if (dogs < cats) and (people < cats):
    print "Cats are more than people and dogs. People are scared by cats!"

if (dogs < cats) and not (people < cats):
    print "Cats are more than dogs. Mice are living a hard life!"

if (dogs == cats) or (cats < 10):
    print "Cats are fighting against dogs! Mice are happy!"

if cats != 0:
    print "There are cats. Mice cannot be too complacent."

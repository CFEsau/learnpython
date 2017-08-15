# ex12: Prompting people
# raw_input() takes prompts to show a user what they need to type
# y = raw_input("Name? ")
# The code from ex11 is rewritten below using only raw_input

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and weigh %r." % (age, height, weight)

# 'pydoc raw_input' in terminal shows the python documentation help files
# other manuals available - open, file, os, and sys...

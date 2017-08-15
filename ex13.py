#ex13: Parameters, unpacking, variables

from sys import argv
# 'import' tells the program to use 'argv' from the 'sys' module
# (sometimes also called 'libraries')

# 'argv' is the 'argument variable'. This variable holds the
# arguments you pass into your python script when you run it.

script, first, second, third = argv
# This line 'unpacks' argv so that rather than holding
# all the arguments, it gets assigned to four variables
# that you can work with: script, first, second, and third.
# 'Take whatever is in argv, unpack it, and assign
# it to all of these variables on the left in order'

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

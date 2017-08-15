# ex18: Names, variables, code, functions

# Make four different functions that work like previous scripts

# This one is like previous scripts with argv
# *args is equivalent to argv but for functions
def print_two(*args):
    arg1, arg2 = args                        # unpack arguments
    print "arg1: %r, arg2: %r" % (arg1, arg2) # print arguments

# That *args is actually pointless. Can just do this:
def print_two_again(arg1,arg2): #use the names we want inside ()
    print "arg1: %r, arg2: %r" % (arg1, arg2) # print arguments

# This takes just one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# This one takes no arguments
def print_none():
    print "I got nothin'."

print_two("Claire","Esau")
print_two_again("Claire", "Esau")
print_one("First!")
print_none()

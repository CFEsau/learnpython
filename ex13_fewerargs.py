from sys import argv

script, first, last = argv

print "Your name is %s %s." % (first, last)
middle_bool = raw_input("Do you have a middle name? [y/n] " )
if middle_bool=='y':
    middle = raw_input("What is your middle name? ")
    print "Your full name is %s %s %s" % (first, middle, last)
else:
    print "Your full name is %s %s" % (first, last)

# ex16: Reading and writing files

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# Open this file in 'write' mode
target = open(filename, 'w')
# (just using 'open()' will open it in the default 'r' (read) mode)

#print "Truncating the file. Goodbye!"
# Not neccessary if opening the file with 'w' mode
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "And finally, we close it."
target.close()
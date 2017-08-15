#ex15: Reading files

from sys import argv

script, filename = argv

# open file and save contents as string in variable 'txt'
txt = open(filename)

# print 'filename' defined in argv
print "Here's your file %r:" % filename
# call the 'read()' function on txt and print file contents
print txt.read()
# close the file
txt.close()

# ask user to enter the filename again
print "\nType the filename again:"
# prompt for filename using '>' and save string in file_again
file_again = raw_input("> ")

# save the file contents in a string called txt_again
txt_again=open(file_again)

#print the first 10 characters of the first line:
print "First 10 characters of first line:\n\t", txt_again.readline(10)
# call the 'read()' function on txt_again & print contents
# (this reads the rest of the file, after what has already been read)
print "Rest of file contents:"
print "\t",txt_again.read()
# close the file
txt_again.close()

txt = open(filename)
i=0
for line in txt:
    i=i+1 # could use 'enumerate' but this is getting ahead...
    # https://stackoverflow.com/questions/3961265/
    # get-line-number-of-certain-phrase-in-file-python
    print "Line %d: %s" % (i,line.rstrip())
    # rstrip() removes the trailing blank line
txt.close()

# ex17: More files

from sys import argv
from os.path import exists
# returns True if file exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()
# Equivalent to
#indata = open(from_file).read()
# Can't explicitly close file this way but should close automatically

print "The input file is %d bytes long" % len(indata)

print "Does the output fie exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)
# Equivalent to
#open(to_file,'w').write(indata)

print "All right, all done."

in_file.close()
out_file.close()

# Alternatively, can do all of this with
#open(to_file, 'w').write(open(from_file).read())

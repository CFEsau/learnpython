from sys import argv

script, filename = argv

ifile = open(filename)
print ifile.read()
ifile.close

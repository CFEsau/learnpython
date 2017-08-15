#ex10: What was that?

#using the escape character '\'
print "I am 5'6\" tall." # escape double-quote inside string
print 'I am 5\'6" tall.\n'

#using triple quotes """ to spread text across lines without \n
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
fat_cat_single = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print fat_cat_single

# Assign string value for each variable
intro = "I'll print a week"
mon = "Mon"
tue = "Tue"
wed = "Wed"
thu = "Thu"
fri = "Fri"
sat = "Sat"
sun = "Sun"

print "%s\n%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (intro, mon, tue, wed, thu, fri, sat, sun)

print "Using \"%r\":"
print "%r" % intro
print "%r" % "She said \"I'll print a week\""
print "%r" % "She said \'I'll print a week\'"
# the single and double quote escapes math up with
# the bounding quotes and the ' in I'll differently

print "Using \"%s\":"
print "%s" % intro
print "%s" % "She said \"I'll print a week\""
print "%s" % "She said \'I'll print a week\'"

# Try out some escape sequences
print "------------------"

print "\nEscape sequences:\n"

#https://linuxconfig.org/list-of-python-escape-sequence-characters-with-examples
#\\:
print "Double backslash (\"\\\\\") prints the backslash character: \\\n"
#\', \":
print "Single \' and double \" quotes given by \\\' and \\\"\n"
#\a: sound terminal bell
print "\'print \"\\a\"\' sounds terminal bell\n"
#\b: ASCII backspace
print "\\b: ASCII backspace. e.g. \'print \"ab\" + \"\\b\" + \"c\"\' gives 'ac'"
print "ab" + "\b" + "c"
#\f: ASCII formfeed.
print "\n\\f: ASCII formfeed. \'print \"hello\\fworld\"\' gives"
print "hello\fworld"
#\N{}: character from unicode database
print "\n\\N{name} prints a character from the UNICODE database"
print u"\N{DAGGER} \N{SOLIDUS} \N{BLACK SPADE SUIT}" #not all working in xterm
#\r: ASCII carriage return. Overwrites preceding characters
print """\\r: ASCII carriage return. Moves all characters after
\tthe CR to the beginning of the new line while
\toverridingthe same number of characters moved
\te.g. \'print \"123456\\rXX_XX\"\' gives"""
print "123456\rXX_XX"
#\t: ASCII horizontal tab
print "\n\\t: ASCII horizontal tab. \tUsed a fair bit already."
#\u: Unicode character (16-bit)
print """\n\\uxxxx: print 16-bit hex value Unicode character
\te.g. \'print u\"\\u041b\"\' should give pi symbol"""
#\U: Unicode character (32-bit)
print """\n\\Uxxxxxxxx: print 32-bit hex value Unicode character
\te.g. \'print u\"\\U000001a9\"\' should give capital Sigma"""
#\v: vertical tab
print "\n\\v: ASCII vertical tab."
print "This is an example\v of what \\v does."
#octal value:
print """\n\\ooo: print character based on its octal value
\te.g. \'print \"\\043\"\' gives \043"""
#\x..: hex value
print """\n\\xhh: print character based on its hex value
\te.g. \'print \"\\x23\"\' gives \x23"""

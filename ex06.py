# Assign a string to variable x with 10 replacing the formatting character
x = "There are %d types of people." % 10
# Assign the string "binary" to variable 'binary'
binary = "binary"
# Assign the string "don't" to variable 'do_not'
do_not = "don't"
# Assign string to variable y with 'binary' and
# 'do_not' strings replacing the formatting characters
y = "Those who know %s and those who %s." % (binary, do_not)

# Print "There are 10 types of people."
print x
# Print "Those who know binary and those who don't."
print y

# Print "I said: 'There are 10 types of people.'", quoting the string x
print "I said: %r." % x
# As above for string y
print "I also said: '%s'." %y
# (%r stands for 'raw' and is best used in debugging)

# Assign boolean False to  variable 'hilarious'
hilarious = False
# Assign string to joke_evaluation with formatting character %r.
joke_evaluation = "Isn't that joke so funny?! %r"

#Print "Isn't that joke so funny?! False"
print joke_evaluation % hilarious

# Assign strings to 'w' and 'e'
w = "This is the left side of..."
e = "a string with a right side."
# Print the strings assigned to variables w and e in one statement
print w + e # concaternate strings with + operator

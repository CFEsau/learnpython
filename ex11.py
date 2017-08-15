#ex11: Asking questions

# input(): Read a value from standard input.
# Equivalent to eval(raw_input(prompt)).
# raw_input(): Read a string from standard input.
# The trailing newline is stripped.

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
# There is a comma at the end of each print line so
# the print doesn't end the line with a new line.

print "So, you're %r old, %r tall and weigh %r." % (age, height, weight)
# In the output, the single quote needs to be escaped
# otherwise it would end the string.

print "Enter an integer: ",
num = int(raw_input())
print "The number you have input is %d" % num

print "Enter a name: ",
name = raw_input()
print "How old is %s?" % name,
age = input()
print "What is %s's height?" % name,
height = input()
print "What's %s's weight?" % name,
weight = input()
print "What is the colour of %s's eyes?" % name,
eyes = raw_input()
print "What is the colour of %s's hair?" % name,
hair = raw_input()
# 'input' tries to convert inputs as if they were python code,
# but it has security problems so try to avoid it.
# to input an integer, use x = int(raw_input())

type(name) # the data type of name will be <type 'str'>
type(age)  # the data type of age will be <type 'int'>

print "Let's talk about %s" % name
print "He's %d years old." % age
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair." % (eyes, hair)

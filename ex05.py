#ex05: More variables and printing

name = 'Claire F. Esau'
age = 28 # not a lie
height = (5*12) + 6 # inches
weight = (9*14) + 10 # lbs
eyes = 'Hazel'
teeth = 'White'
hair = 'Brown'

print "\nLet's talk about %s." % name
print "She's %d inches tall." % height
print "She weighs %d pounds." % weight
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

# Try more formatting characters
greeting = "Hello,\t"
firstname = "Claire"
surname = "Esau"

# compare %s and %r formats
print "\nFormatting with %r: %s my name is %s %s\n and I'm %d years old." % (
    '%s', greeting, firstname, surname, age)
print "Formatting with %r: %r my name is %s %s\n and I'm %d years old." % (
    '%r', greeting, firstname, surname, age)

# convert inches and pounds to centimetres and kilos
inch2cm = 2.54
lb2kg = 0.453592
# print height in cm to 2 d.p.
print "\nShe's %.2f centimetres tall." % (height * inch2cm)
# print weight in kg to 3 d.p.
print "She weighs %.3f kg." % (weight * lb2kg)

# ex21: Functions can return something

def add(a, b):
    print "ADDING %.2f + %.2f" % (a,b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %.2f - %.2f" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %.2f * %.2f" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %.2f / %.2f" % (a, b)
    return a / b

# my own function to test return
def isequal(a,b):
    print "Is %r equal to %r?" % (a, b)
    return (a==b)

print "Let's do some maths with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is a puzzle."
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes: ", what, "Can you do it by hand?"

# Test the isequal function
num1 = 40
num2 = 50
num3 = 50

print isequal(num1, num2)
print isequal(num2, num3)

# A new puzzle
print "The volume of a sphere:"
# 4/3 * pi * r^3
r=float(raw_input("\nEnter radius: "))
volume = multiply(4,divide(multiply(3.14159,multiply(r**2,r)),3.0))
print "\nThe volume of a sphere of radius %.2f is %.2f" % (r, volume)

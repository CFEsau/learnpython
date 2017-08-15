# Demonstrate what the % character does in calculations
print "The % character:"
print "4 % 2 =", 4 % 2
print "100 % 16 =", 100 % 16
# % is the 'modulus' operator, not per cent.
print "X % Y = J means X divided by Y with J remaining,"
print "or 'The remainder of X divided by Y is'."

print ""

print "Floating point numbers:"
print "8/5 =", 8/5
print "8/5. =", 8/5.
print "8./5 =", 8./5
print "8./5. =", 8./5.
print "Using integers drops the fractional part -"
print "make the calculation floating point!"

print ""

# The following expressions are more complicated claculations.

# decimal: more accurate than float.
import decimal
print "Using 'decimal':"
print (decimal.Decimal(9876) + decimal.Decimal("54321.012345678987654321"))
print "Using floating point:"
print 9876 + 54321.12345678987654321
print ""

# fraction
import fractions
print "Using 'fraction':"
print fractions.Fraction(1, 3)
print fractions.Fraction(4, 6)
print 3 * fractions.Fraction(1, 3)
print ""

# complex numbers
print "Complex numbers:"
print (1j * 1J)
#print (3 + 1j * 3)j #This is in the github solutions but doesn't work...
print ""

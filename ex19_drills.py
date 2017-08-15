# Solutions to ex19 study drills, from
# github.com/wzpan/Learn-Python-The-Hard-Way/blob/master/Python2/ex19.py

#ex19: Functions and variables

# Define a function named "cheese_and_crackers"
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


# Print "We can just give the function numbers directly:"
print "We can just give the function numbers directly:"
# Call the function, with 2 numbers as the actual parameters
cheese_and_crackers(20, 30)

# Print "OR, we can use variables from our script:"
print "OR, we can use variables from our script:"
# assign 10 to a variable named amount_of_cheese
amount_of_cheese = 10
# assign 50 to a variable named amount_of_crackers
amount_of_crackers = 50

# Call the function, with 2 variables as the actual parameters
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Print "We can even do maths inside too:"
print "We can even do maths inside too:"
# Call the function, with two maths expressions as the actual
# parameters. Python will first calculate the expressions and then
# use the results as the actual parameters.
cheese_and_crackers(10 + 20, 5 + 6)

# Print "And we can combine the two, variables and maths:"
print "And we can combine the two, variables and maths:"
# Call the function, with two expressions that consists of variables
# and maths as the actual parameters
cheese_and_crackers(amount_of_cheese + 100, amount_of_cheese + 1000)

# The * in *argv tells python to take all the arguments to the function
# and put them in argv as a list.
def print_args(*argv):
    size = len(argv)
    print "Size: ", size
    print "Hello! Welcome to %r!" % argv[0]
    if size > 1:
        for i in range(1, size):
            print "Param %d is %r" % (i, argv[i])
        return 0
    return -1

# 1. use numbers as actual parameters.
print "\nMethod 1"
print_args(10,20,30)

# 2. use string and numbers as actual parameters
print "\nMethod 2"
print_args("print_args", 10, 20)

# 3. use strings as actual parameters
print "\nMethod 3"
print_args("print_args", "Joseph", "Pan")

# 4. use variables as actual parameters
print "\nMethod 4"
first_name = "Joseph"
last_name = "Pan"
print_args("print_args", first_name, last_name)

# 5. contain mathematical expressions
print "\nMethod 5"
print_args("print_args", 5*4, 2.0/5)

# 6. more complicated calculations
print "\nMethod 6"
print_args("print_args", '.'*10, '>'*3)

# 7. more parameters
print "\nMethod 7"
print_args("print_args", 10, 20, 30, 40, 50)

# 8. tuples as parameters
print "\nMethod 8"
nums1 = (10, 20, 30)
nums2 = (40, 50, 60)
print_args("print_args", nums1, nums2)

# 9. more complicated types
print "\nMethod 9"
nums3 = [70, 80, 90]
set1 = {"apple", "banana", "orange"}
dict1 = {'id': '0001', 'name': first_name+" "+last_name}
str1 = "Wow, so complicated!"
print_args("print args", nums1, nums2, nums3, set1, dict1, str1)

# 10. function as parameter and return values
if print_args(cheese_and_crackers, print_args) != -1:
    print "You just sent more than one parameter. Great!"

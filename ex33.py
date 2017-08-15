# ex33: While loops


def findnumbers_while(imax,step):
    i = 0
    numbers = []
    while i < imax:
        print "At the top i is %d" % i
        numbers.append(i)
        
        i = i + step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
        
    return numbers


def findnumbers_for(imax,step):
    numbers = []
    for i in range(0,imax,step):
        print "At the top i is %d" % i
        numbers.append(i)
        
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
        
    return numbers


imax = 6
increment = 2
loop = raw_input("Use 'while' or 'for' loop to find numbers? [while/for]: ")

if loop == "while":
    numbers = findnumbers_while(imax, increment) # (imax, increment)
else:
    if not loop == "for":
        print "\nInput not recognised. Defaulting to 'for'."
    numbers = findnumbers_for(imax, increment)
    
print "\nThe numbers: "
for num in numbers:
    print num



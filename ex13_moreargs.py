from sys import argv

script, name, age, rabbit1, rabbit2, hamster = argv

print "Your name is %s and you are %d years old." % (name,int(age))
print ("Your rabbits' names are %s and %s, and your "
       "hamster's name is %s." % (rabbit1, rabbit2, hamster))

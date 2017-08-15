# ex14: Prompting and passing

from sys import argv

script, user_name, location = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "You're running me from %s." % location
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. I'm not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

print "How's the weather in %s?" % location
weather = raw_input(prompt)
print "%s is %s? I can't feel it as I'm a robot." % (location, weather)
print "\t\v\\|0.0|/"

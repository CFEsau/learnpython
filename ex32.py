# ex32: Loops and lists

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
#for i in range(0, 6):
#    print "Adding %d to the list." % i
#    # append is a function that lists understand
#    elements.append(i)
elements = range(0, 6)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i

print "\nMore on lists:\n"

# find the lengths of lists:
print "'fruits' has %d entries" % len(fruits)
print "Use '+' to append two lists: "
exotic = ['guava', 'canteloupe', 'kiwi']
all_fruits = exotic + fruits
print "A bigger list of fruits is", all_fruits
# list.extend(list2) is similar to using +
if 'tomato' in all_fruits:
    print "\nYes, tomato is a fruit!"
else:
    print "\n No tomato. It is a fruit, but functions as a vegetable"
#https://developers.google.com/edu/python/lists

moreinfo = raw_input("Do you want to know more about lists? [y/n]: ")
if moreinfo == 'y' or moreinfo == "Y":
    print "\nUse list.insert(index, elem) to insert an element at a given index"
    print "e.g. for list 'elements' from earlier:"
    print elements
    print "Insert 2.5 using elements.insert(3, 2.5):"
    elements.insert(3, 2.5)
    print elements

    print """\nFind index containing certain entry is in a list
    using list.index(elem)."""
    print "elements.index(0), elements.index(3):"
    print elements.index(0), elements.index(3)
    print """If a value/string isn't in the list you'll get a ValueError.
    To avoid this, use 'in' to check list contents."""

    print "\n To remove an element use list.remove(elem)"
    print "Again, this gives a ValueError if not present."
    print "e.g. elements.remove(3):"
    elements.remove(3)
    print elements

    print "\nlist.reverse() reverses the list:"
    elements.reverse()
    print elements
    elements.reverse()

    print """\nlist(reversed(listname)) reverses the list in place
    (doesn't return it)"""
    print "list(reversed(elements) = %r" % list(reversed(elements))
    print "Elements is still %r." % elements

    print """\nlist.pop(index) removes and returns the element at the given
index. If no element is given the rightmost element is removed."""
    elements.pop()
    print elements

    print "\nSlices work on lists just as with strings."
    list_slice = ['a', 'b', 'c', 'd']
    print "list_slice = %r" % list_slice
    print "list_slice[1:-1] gives: %r" % list_slice[1:-1]
    print "(-1 is last element, -1] is up to & excluding last element)"
    print "replace ['a', 'b'] with ['z'] using list_slice[0:2] = 'z':"
    list_slice[0:2] = 'z'
    print list_slice
    
else:
    print "\nOK. Bye bye!"

"""
Write two Python functions to find the minimum number in a list.
The first function should compare each number to every other
number on the list. O(n^2). The second function should be linear O(n).

This is Cory DeMar code
"""
import random
import time

# This is O(n^2)
def findMin(aList):
        theMin = aList[0]
        for x in aList:
                smallest = True
                for y in aList:
                        if x > y:
                                smallest = False
                if smallest:
                        theMin = x
        return theMin

this = findMin([random.random() for x in range(1000)])

start = time.clock()
print(this)
end = time.clock()
print("time:", end - start)

# This is O(n)
def find_min(aList):
        the_min = aList[0]
        for x in aList:
                if x < the_min:
                        the_min = x
        return the_min


that = find_min([random.random() for x in range(1000)])

starting = time.clock()
print(that)
ending = time.clock()
print("time:", ending - starting)

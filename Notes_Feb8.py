# Teaching things
class bob:
        def __init__(self, nm, age):
                self.name = nm
                self.age = age
                
        # Differ from start
        def hiThere(self, n):
                for rose in range(n):
                        print(self.name)

sue = bob("sue", 19)

print(sue)
print(sue.name, sue.age)

mary = sue
print(mary.name, mary.age)
print()

# Differ thing
a = [1, 2, 3]
b = [x for x in a] # Copied list 'a'
print(a, b)
b[1] = 99
print(a, b)
print()

# Differ thing
jack = [a, a, a]
print(jack)
a[2] = 5
print (jack)
print()

# Differ thing
a = bob("guy", 22)
b = bob("girl", 23)
print(a.name, b.name)
b.name = "sue"
print(a.name, b.name)
print()

# Differ thing
def add5(n):
        return n + 5
def sub5(n):
        return n - 5
print(add5(10), sub5(10))

aeon = add5
print(aeon(5))
print()

# Differ thing
print(type("abc".strip()))
print(type("abc".strip))
print("abc   ".strip)
print("abc   ".strip())
print()

# Differ thing
def silly(op, n):
        print(op(n)) # Don't actually need it
        return op(n)
silly(add5, 5)
silly(sub5, 5)

import math as m
import numpy as np

silly(m.sin, 5)
print()

a.fred = add5
print(a.fred(15))

b.fred = sub5
print(b.fred(15))
print()

# Differ thing
class cory:
        def __init__(self, v):
                self.value = v
                self.fpt = None

head = None
for x in range (10):
        bob = cory(x)
        bob.fpt = head
        head = bob

while head != None:
        print(head.value)
        head = head.fpt

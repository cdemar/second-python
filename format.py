v0 = "leri"
v1 = 23

bob = "{0} bob is cool {1}"
print(bob.format(v0, v1))

bob = "{0} bob is cool {1:5d}"
print(bob.format(v0, v1))

bob = "{0} bob is cool {1:05d}"
print(bob.format(v0, v1))

bob = "{0:23s} bob is cool {1}"
print(bob.format(v0, v1))

bob = "{0:>23s} bob is cool {1}"
print(bob.format(v0, v1))

bob = "{0:^23s} bob is cool {1}"
print(bob.format(v0, v1))

for i in range(90,100):
        print("{0:^5d}".format(i))

for i in range(7,15):
        print("{0:>5x}".format(i))

for i in range(7,15):
        print("{0:>5b}".format(i))

for i in range(7,15):
        print("{0:>5.2f}".format(i))

for i in range(7,15):
        print("{0:>5.4e}".format(i))

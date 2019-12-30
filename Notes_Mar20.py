import random
import time
import matplotlib.pyplot as py

# set of letters
letters = 'abcdefghijklmnopqrstuvwxyz'

def randstring():
        """returns a random string for 1-20 characters long """
        # rl is the length of the strong 1-21
        rl = int(round(random.random()*20, 0) + 1)
        # resurt is what is returned
        result = ''
        # loop adds randome letters to the result
        for ix in range(rl):
                # random char index points to the random letter...
                # 32717 is the big number that might be prime-ish ???
                # The % takes the remainder dividing by the length of the letters
                random_char_index = int(round(random.random() * 32717917,
                                              0) % len(letters))
                # adds the letter to the result
                resuslt = result + letters[random_char_index]
        return result

#for ix in range(10):
#        print(randstring())

strs = [randstring() for x in range(1000)]
#print(len(strs))

start_time = time.clock()
for list_string in strs:
        bob = strs.index(list_string)
stop_time = time.clock()
print("Time to use a simple list {}".format(stop_time - start_time))

# This will  hold the list of lists
class stringHash:
    def __init__(self, primary_length):
        self.primary_length = primary_length
        self.primary_list = [ None for x in range(primary_length)]

# I will turn a string into just some numbers
    def myHash(self, string):
        rv = 1010101
        for c in string:
            rv += ord(c)
            rv *= 1928374611
            rv = rv % 321717
        return rv % self.primary_length

    def addString(self, string):
        hash_index = self.myHash(string)
        if self.primary_list[hash_index] == None:
            self.primary_list[hash_index] = [string]
        else:
            self.primary_list[hash_index].append(string)

    def myIndex(self,string):
        hash_index = self.myHash(string)
        if self.primary_list[hash_index] == None:
            print("oops Morris")
            return -1
        else:
            return self.primary_list[hash_index].index(string)

# this created the object for the 100
sh = stringHash(100)

#cnts = [0 for x in range(100)]

# add everyone in
for list_string in strs:
        sh.addString(list_string)

start_time = time.clock()

for list_string in strs:
    bob = sh.myIndex(list_string)
    
stop_time = time.clock()

# was added 3/22/18
def fun():
        start_time = time.clock()
        for s in strs:
                bob = strs.index(s)
        end_time = time.clock()
        print(end_time - start_time)

fun()

print("Hashed time {}".format(stop_time - start_time))

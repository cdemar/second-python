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

class linkhash:
        
        class myString:
                def __init__(self, string):
                        self.string = string
                        self.link = None
                        
        def __init__(self, nentries):
                self.head = [None for x in range(nentries)]
                self.tail = [None for x in range(nentries)]

        def myHash(self, string):
                rv = 2323
                for c in string:
                        rv += ord(c)
                return rv % len(self.head)

        def addString(self, string):
                hashed = self.myHash(string)
                myobj = self.myString(string)
                if self.tail[hashed] == None:
                        self.tail[hashed] = myobj
                        self.head[hashed] = myobj
                else:
                        self.tail[hashed].link = myobj
                        self.head[hashed] = myobj

        def myIndex(self, string):
                hashed = self.myHash(string)
                lnk = self.head[hashed]
                while lnk != None:
                        if lnk.string == string:
                                return lnk
                        lnk = lnk.link
                return None


bash = linkhash(100)

for s in strs:
        bash.addString(s)

def testLink():
        start_time = time.clock()
        for s in strs:
               bob = bash.myIndex(s)
        end_time = time.clock()
        print("Link list", end_time - start_time)

def regular():
        


testLink()


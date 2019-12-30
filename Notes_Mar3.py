"""
working with and play with links...
A linked list
First, the list needs something that references the beginning and end of the list...
Pick a set of names... head tail
"""

import matplotlib.pyplot as plt

head = None
tail = None
# None is special object value that can't be referenced

"""
diffine a class to hold some data... Use the deaths data from the midterm
"""
class mental_death:
        def __init__(self, state, code, death, population):
                self.link = None
                self.state = state
                self.code = code
                self.death = death
                self.population = population
                self.norm = self.death/self.population
                
        def __str__(self):
                return "Mental heath death -- state {} death {}".format(self.state, self.death)

# Function to append to the list
def addtolist(thing):
        global head,tail
        if tail == None:
                head = thing
                tail = thing
                thing.link = None
        else:
                tail.link = thing
                thing.link = None # To be safe
                tail = thing

def readit(fn):
        with open(fn,"r") as f:
                f.readline()
                for l in f:
                        pieces = l.strip().split("\t")
                        if len(pieces) > 1:
                                # The 1 = take out the first " and -1 = take out the last "
                                md = mental_death(pieces[0][1:-1], int (pieces[1][1:-1]),
                                                        float(pieces[2]), float(pieces[3]))
                                addtolist(md)
readit("C:\\Users\\coryd\\Desktop\\mid_data.txt")

liz = head
srate = []
sname = []
while liz != None:
        #print(liz)
        srate.append(liz.norm)
        sname.append(liz.state)
        liz = liz.link

plt.plot(srate)
plt.show()
print(sname[srate.index(min(srate))],min(srate))
print(sname[srate.index(max(srate))],max(srate))
print("dangerous",max(srate)/min(srate))



                

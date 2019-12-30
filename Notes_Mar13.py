"""
A simple easy analysis of food
Dinner vs Dessert
This analyzes the recipes
"""
# holds the words read in from a recipe
# this defines the word
class rword:
    def __init__(self,wd):
        self.word=wd
        self.categories=[]
rwords=[]

#function to read in a recipe(file)
# toss periods, commas, semicolons, colons
repchars=[',','.',';',':','/','(',')','-']
def readrec(fn):
    global rwords
    rwords=[] #helps look at each file seperated. clean up the stuff
    with open(fn,"r") as f:
        for l in f:
            wds=l.strip().split()
            for w in wds:
                for rp in repchars:
                    w=w.replace(rp,'') #takes away the punctuation
                if len(w)>0:
                    wc = rword(w)
                    rwords.append(wc)

#print(readrec("r1.txt")

worddict = {}

def readdict(fn):
    global worddict
    worddict={}
    with open(fn,"r") as f:
        f.readline() #reads the title to skip it
        for l in f:
            tks=l.strip().split(",") #look at the code and the Dict
            if tks[0] in worddict:
                worddict[tks[0]].append(tks[1])
            else:
                worddict[tks[0]]=[tks[1]]

#readdict("mealwords.csv")
#for x in worddict:
#        print(x, worddict[x])

def analwords():
    for w in rwords:
        if w.word in worddict:
            for c in worddict[w.word]:
                w.categories.append(c)

def sumcategory(cn):
    cnt=0
    for w in rwords:
        if cn in w.categories:
            cnt += 1
    return cnt

def decision():
    des = sumcategory("Dessert")
    din = sumcategory("Dinner")
    if des > din:
        return "Dessert"
    return "Dinner"

def main(rn):
    rwords=[]
    readrec("C:\\Users\\coryd\\Desktop\\python_class_idle\\food_sent\\r{}.txt".format(rn))
    readdict("C:\\Users\\coryd\\Desktop\\python_class_idle\\food_sent\\mealwords.csv")
    analwords()
    print("r{} {}".format(rn, decision()))

for x in range(1,17):
    main(x)

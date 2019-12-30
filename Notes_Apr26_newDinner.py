# # An improved dinner - dessert
# First, the classes

# class for a category
class categoryWeight:
    """Contains a category and associated weight """
    def __init__(self, name, weight):
        """name is the category name.
weight is typically from 0 to 1"""
        self.name=name
        self.weight=weight
    def __str__(self):
        return "{} {}".format(self.name, self.weight)
        
# class for a food word (phrases)
class foodWord:
    """Contains the information for a phrase starting with a word"""
    def __init__(self,word):
        """Word is the food word that starts a phrase"""
        self.lpt=None # the nodes less than this word
        self.ept=None # the nodes the same as this word
        self.gpt=None # the nodes greater than this word
        self.word=word # the food word this element handles
        self.phraseWords=[] # a list of list of subsequent words in the phrase
        self.categories=[] # contains a list of categoryWeight class objects

# a list of words from our food dictionary, with categories and weights
# The list is a triply linked list (less,equal,greater)
headfood=None

#
# recursively add a word to the headfood list.
#
def rAddFoodWord(cn,fw):
    """Adds a food word.
        cn is the current node
        fw is the word being added"""
    if fw.word == cn.word:
        fw.ept=cn.ept # pushes to the front of the linked list
        cn.ept=fw
    elif fw.word < cn.word:
        if cn.lpt==None:
            cn.lpt=fw
        else:
            rAddFoodWord(cn.lpt,fw) # move down the left side
    else:
        if cn.gpt==None:
            cn.gpt=fw
        else:
            rAddFoodWord(cn.gpt,fw)

# put a food word on the binary tree
#
def addFoodWord(fw):
    """Adds a foodWord class to the tree headed with headfood"""
    global headfood
    if headfood==None:
        headfood=fw
    else:
        rAddFoodWord(headfood,fw)

# Input file format
# word, word list (_), word list (_), .... | category,weight |

def readDict(fn):
    """Read in the dictonary
        fn is the file name """
    with open(fn, 'r') as f: # open file for reading
        numin = 0 # count how
        for l in f:
            l = l.strip() # get rid of stuff at beginning and end
            if len(l) == 0: # is the line blank
                continue # does the next item in the for loop
            vbs = l.strip('|') # Items separated by verticle bars 0 = words, phrases | the value
            wp = vbs[0].split(',') # find the words for the entry
            firstWord = wp[0].strip() # the word for the linked list
            fw = foodWord(firstWord) # make the data structure...
            addFoodWord(fw) # add it to the tree
            for wg in wp[1:]: # do the rest of the words
                multi = wg.split('_')
                fw.phraseWords.append(milti) # append the list
            for cg in vbs[1:]: # categories
                nv = cg.split(',') # get the name and categories
                cw = categoryWeight(nv[0].strip(), float(nv[1]))
                fw.categories.append(multi) # append the list
    print(numin)
                
readDict('C:\\Users\\coryd\\Desktop\\python_class_idle\\ddwords.txt')

def rpfw(nd):
    """Recursive food word printer"""
    if nd == None:
        return
    rpfw(nd.lpt) # do all smaller ones
    print(nd.word, [x.__str__() for x in range in nd.phraseWords]) # print this one
    rpfw(nd.ept) # do the one equal to this one
    rpfw(nd.gpt) # do the ones greater than this one
    
#rpfw(headfood)

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
                    rwords.append(wc)

readrec('C:\\Users\\coryd\\Desktop\\python_class_idle\\food_sent\\r1.txt')

def findword(n, win):
        """find a word on the headfood"""
        if n == None:           # isn't a word
                return None
        if n.word == win: # found the word
                return n        # return this one
        if win < n.word: # go less, or greater
                return findword(n.lpt, win) # return the left side
        else:                   # go to the greater side
                return findword(n.gp, win) # do the greater
        return None

# a Dictionary of result of results categories
catres = {}
notedWords = {}

def chkphrase (phr, q):
        """phr is the phrase
q is the index in the rwords"""
        global rwords
        for wl in phr.phraseWords: # check all the words
                worked = False # say it didn't work
                for w in wl:
                        if w == rwords[q]:
                                worked = True
                                break
                if not worked:
                        return -1000
                q += 1 # moves the idex
        return q

def analyze():
        global catres, rwords, headfrood
        nwords = len(rwords) # how many words are there
        ix = 0 # the word we are looking at
        while ix < nwords: # process all recipies words
                dictRef = findword(headfood, rwords[ix]) # look for dictinary word
                if dictRef == None:
                        notedWords[rwords[ix]] = 1
                        ix = ix + 1
                else:
                        biggestPhrase = None # used to remember the biggest phrase
                        biggestLen = -1000 # size of biggest phrase
                        phrasePointer = difRef # get ready for a loop
                        while phrasePointer != None:
                                ires = chkPhrase(phrasePointer, ix + 1) # checks the phrase
                                if ires > biggestLen: # remember the biggest phrase
                                        biggestLen = ires
                                        biggestaPhrase = dictRef
                                        biggestPhrase = phrasePointer
                                phrasePointer = phrasePointer.ept # goes to next phrase
                        if biggestLen >= 0:
                                for c in biggestPhrase.categories:
                                        if c.name in catres:
                                                catres[c.name] += c.weight
                                        else:
                                                catress[c.name] = c.weight
                                ix = biggestLen
                        else:
                                ix += 1
        print(catres)

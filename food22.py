
# coding: utf-8

# # An improved dinner - dessert
# First, the classes

# In[1]:


# class for a category
class categoryWeight:
    """Contains a category and associated weight """
    def __init__(self,name,weight):
        """name is the category name.
weight is typically from 0 to 1"""
        self.name=name
        self.weight=weight
    def __str__(self):
        return str("{} {}".format(self.name,self.weight))


# In[2]:


# class for a food word (phrases)
class foodWord:
    """Contains the information for a phrase starting with a word"""
    def __init__(self,word):
        """word is the food word that starts a phrase"""
        self.lpt=None # the nodes less than this word
        self.ept=None # the nodes the same as this word
        self.gpt=None # the nodes greater than this word
        self.word=word # the food word this element handles
        self.phraseWords=[] # a list of list of subsequent words in the phrase
        self.categories=[] # contains a list of categoryWeight class objects


# In[3]:


# a list of words from our food dictionary, with categories and weights
# The list is a triply linked list (less,equal,greater)
headfood=None


# In[4]:


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

# In[5]:


def readDict(fn):
    """Read in the dictionary
    fn is the file name"""
    with open(fn,"r") as f:  # open file for reading
        numin=0 # count how many lines we read in
        for l in f:
            numin+= 1 # add 1 to the read in
            l=l.strip() # get rid of stuff at beginning and end
            if len(l)==0: # is the line blank
                continue # does the next item in the for loop
            vbs=l.split("|") # Items separated by verticle bars 0=words,phrases 1: categories
            wp=vbs[0].split(",") # find the words for the entry
            firstWord = wp[0].strip() # the word for the linked list
            fw=foodWord(firstWord) # make the data structure...
            addFoodWord(fw) # add it to the tree
            for wg in wp[1:]: # do the rest of the words
                multi=wg.split("_") # get words from group
                fw.phraseWords.append(multi) # append the list
            for cg in vbs[1:]: # categories
                nv=cg.split(",") # get the names and categories
                cw=categoryWeight(nv[0].strip(),float(nv[1]))
                fw.categories.append(cw)
        print(numin)   
            


# In[6]:


readDict("/Users/corydemar/Desktop/Programing/python_class_2/ddwords.txt")


# In[7]:


def rpfw(nd):
    """recursive food word printer"""
    if nd == None: # if empty, return
        return
    rpfw(nd.lpt) # do all smaller ones
    print(nd.word,nd.phraseWords,[x.__str__() for x in nd.categories]) #print this one
    rpfw(nd.ept) # do the ones equal to this one
    rpfw(nd.gpt) # do the ones greater than this one


# In[15]:


#rpfw(headfood)


# In[11]:


# toss periods, commas, semicolons, colons
repchars=[',','.',';',':','/','(',')','-']
rwords=[]
def readrec(fn):
    global rwords
    rwords=[]
    with open(fn,"r") as f:
        for l in f:
            wds=l.strip().split()
            for w in wds:
                for rp in repchars:
                    w=w.replace(rp,'')
                if len(w)>0:
                    rwords.append(w)            



# In[19]:


readrec("/Users/corydemar/Desktop/Programing/python_class_2/food_sent/r1.txt")
def findword(n,win):
    """finds a word on the headfood"""
    if n == None:     # isn't a word
        return None
    if n.word == win: # found the word
        return n      # return this one
    if win < n.word:  # go less, or greater
        return findword(n.lpt,win)  # return the left side
    else:             # go to the greater side
        return findword(n.gpt,win)  # do the greater
    return None


# In[20]:


# a dictionary of result categories
catres={}
notedWords={}


# In[23]:


def chkPhrase(phr,q):
    """phr is the phrase
q is the index in the rwords"""
    global rwords
    for wl in phr.phraseWords: #check all the words
        worked=False  # say it didn't work
        for w in wl:
            if w == rwords[q]:
                worked=True
                break
        if not worked:
            return -1000
        q+=1 # moves the index
    return q    
        

def analyze():
    global catres, rwords, headfood
    nwords = len(rwords)  # how many words are there
    ix=0 # the word we are looking at
    while ix < nwords: # process all recipie words
        dictRef=findword(headfood,rwords[ix]) # look for dictionary word
        if dictRef == None:
            notedWords[rwords[ix]]=1
            ix = ix + 1
        else:
            biggestPhrase=None # used to remember the biggest phrase
            biggestLen=-1000  # size of biggest phrase
            phrasePointer=dictRef  # get ready for a loop
            while phrasePointer != None:
                ires=chkPhrase(phrasePointer,ix+1) #checks the phrase
                if ires>biggestLen: # remember the biggest phrase
                    biggestLen=ires
                    biggestPhrase=phrasePointer
                phrasePointer=phrasePointer.ept #goes to next phrase
            if biggestLen >=  0:
                for c in biggestPhrase.categories:
                    if c.name in catres:
                        catres[c.name]+= c.weight
                    else:
                        catres[c.name]=c.weight
                ix=biggestLen
            else:
                ix+=1
    print(catres)


# In[24]:


analyze()


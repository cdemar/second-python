
# coding: utf-8

# # A set of items to read in the word list 

# First, define a class to hold one word.
# The class will be on a binary tree to allow easy access. It will have links to other words that differ by one character.

class w4:
    """Holds a single word for the graph search"""
    def __init__(self, w):
        self.word = w     # the 4 letter word
        self.lpt = None   # Binary tree <= link
        self.gpt = None   # Binary tree > link
        self.diff1 = []   # list of words that differ by 1 letter
        self.mark = False # tells me if I'm looping
        

head_word = None  # head pointer for binary tree

def Raddword(n,new_word):
    if new_word.word <= n.word:
        if n.lpt == None:
            n.lpt=new_word
            return
        Raddword(n.lpt,new_word)
        return
    else:
        if n.gpt == None:
            n.gpt=new_word
            return
        Raddword(n.gpt,new_word)
        return

def addword(w):
    global head_word
    if head_word == None:
        head_word=w
        return
    Raddword(head_word,w)


# Read Words reads in the words, and builds a tree

def readWords(fn):
    with open(fn,"r") as f:
        for l in f:
            l=l.strip()
            if len(l)==4:
                addword(w4(l))

# read in the words
# my file is local to where I run jupyter notebook
# you may need to put a path here
readWords("c:\Users\corydemar\Desktop\Programing\python_class_2\World_4list\word4list.txt")


# Create a function to indicate words differ in one letter position


def onediff(w1,w2):
    dcnt=0
    for ix in range(len(w1.word)):
        if w1.word[ix]!=w2.word[ix]:
            dcnt += 1
    if dcnt == 1:
        return True
    return False


# compare every word to every other word O(n^2)


# compares a word (w2)
# to all words on the W1 tree
def compw2(w1,w2):
    if w1 == None:
        return
    compw2(w1.lpt,w2)
    if onediff(w1,w2):
        if not(w1 in w2.diff1):
            w2.diff1.append(w1)   # add link 
        if not (w2 in w1.diff1):
            w1.diff1.append(w2)   # add link
    compw2(w1.gpt,w2)

# look at all the words once
def compw1(w):
    global head_word
    if w == None:
        return
    compw1(w.lpt)
    compw2(head_word,w)  # Now, do all 2nd words
    compw1(w.gpt)

compw1(head_word) # this is what takes the longes

# find a word on the handword tree
def find_word(n, wv):
    if n == None:
        return None
    if wv == n.word:
        return n
    if wv < n.word:
        rv = find_word(n.lpt, wv)
        if rv != None:
            return rv
    return find_word(n.gpt, wv)

fool = find_word(head_word, "fool")

for l in fool.diff1:
    print(l.word)

poop = find_word(head_word, "poop")

# things that go into the fifo elements
class fifo_element:
    def __init__(self, me, depth, path):
        self.me = me
        self.depth = depth
        self.path = []
        for p in path:
            self.path.append(p)
        self.path.append(me)

fifo = []

def onestep(element, lastone):
    global fifo
    print(len(fifo))
    if element.me.mark:    # already been here
        print("i'm marked", element.me.word)
        return False
    element.me.mark = True
    for l in element.me.diff1:
        fifo.append(fifo_element(l, element.depth + 1, element.path))
        if l == lastone:
            print("gotit", l.word, lastone.word)
            return True
    return False



def manysteps(firstone, lastone):
    global fifo
    fifo.append(fifo_element(firstone, 1, []))

    while len(fifo) > 0:
        rv = onestep(fifo[0], lastone)
        if rv:
            break
        fifo = fifo[1:]
    print(rv)
    print("Happyness")
    for l in fifo[len(fifo - 1)]:
        print(l.me.word)

manysteps(fool, poop)




 





# coding: utf-8

# # A mapper for the old food list to new foods
# This maps the old food list to a new format for phrases, weights, etc
# Input file format word, word list (\_), word list (\_), .... | category,weight |
# 

# In[1]:


class oldword:
    """Holds a word from the old format"""
    def __init__(self,word):
        self.word=word
        self.categories=[]
# the word list
wl={}

with open("mealwords.csv","r") as f:
    f.readline() # get rid of the first line (It's a header for col names)
    for l in f:
        toks=l.strip().split(",")
        if not (toks[0] in wl):
            ow=oldword(toks[0])
            wl[toks[0]]=ow
        wl[toks[0]].categories.append(toks[1])

print("I got {} words".format(len(wl)))


# In[7]:


import random
with open("ddwords.txt","w") as fo:
    kyobj=wl.keys()
    kys=[ x for x in kyobj]
    random.shuffle(kys)
    for w in kys:
        fo.write("{}".format(w))
        for c in wl[w].categories:
            fo.write("|{},1.0".format(c))
        fo.write("\n")
        


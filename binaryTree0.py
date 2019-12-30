
# coding: utf-8

# # Multiple links
# Links can be used to establish a relationship between data items. When multiple links are used, performance better than O(n) can be achieved.
# 
# One of the most common use of multiple links is to establish a relationship between this node, and subsequent nodes. A common form of two links is called a binary tree. (The tree word is used, and many books talk about leafs, etc.)
# 
# A simple two link system has two links. One relates data in the parent to data in a child. When two links are used, typically a relationship is defined for one link, and the other link is everything else.
# 
# As an example, assume one link indicates the child is less than or equal to the parent. The other link then indicates the child is greater than the parent.

# In[1]:


class treenode:
    def __init__(self,val):
        self.value=val
        self.lpt=None # less than or equal to pointer
        self.gpt=None # greater than pointer
    


# If we are lucky, 1/2 the children will be under the lpt link, and 1/2 the children will be under the gpt. When searching the tree for a piece of data, each time we visit a node, the amount of data to search is cut in half. We look at the relationship of the search data to the node data, and then follow the appropriate link. 
# 
# This results in a balanced binary tree (1/2 the data on each link) having a search time of (log2(n)). A balanced binary tree would require 20 comparisons to find an item in a set of 1 million items. This represents a significant performance improvement.  Unlike a hash, the binary tree still has order.

# In[2]:


head=None


# A binary tree still needs something to tell where the tree is located. I have used the name head.  

# In[3]:


#
# recursive routine to add a node
#
def addTreeRecursive(treeNode,addedNode):
    if addedNode.value <= treeNode.value: # the relationship for lpt
        if treeNode.lpt==None: # does it have a child
            treeNode.lpt=addedNode
            return
        addTreeRecursive(treeNode.lpt,addedNode)
        return
    else:
        if treeNode.gpt==None:
            treeNode.gpt=addedNode
            return
        addTreeRecursive(treeNode.gpt,addedNode)
        return

def addTree(n):
    global head
    n.lpt=None
    n.gpt=None
    if head == None:
        head=n
        return
    addTreeRecursive(head,n)
    return


# In[4]:


import random
for q in range(2000000):
    addTree(treenode(random.random()))


# This builds a tree with 20 random numbers. The tree can be "walked" to print out the numbers in order. This is done using recursion, and following the less than links before printing anything, and then printing, and following the greater than links.

# In[5]:


def rptree(n,limit):
    if limit > 10:
        return limit
    if n == None:
        return limit
    limit=rptree(n.lpt,limit)
    if limit > 10:
        return limit
    print("{0:10.7f}".format(n.value))
    limit=limit+1
    limit=rptree(n.gpt,limit)
    return limit

rptree(head,0)


# To print the tree in descending order, simply follow the greater links first, and then print. Then follow the less than links.

# In[6]:


def rptree_descend(n):
    if n==None:
        return
    rptree_descend(n.gpt)
    print(n.value)
    rptree_descend(n.lpt)
    return


# In[7]:


depth=[]
def recDepth(n,d):
    global depth
    if n == None:
        return d
    depth.append(d)
    ld=recDepth(n.lpt,d+1)
    gd=recDepth(n.gpt,d+1)
    if ld > gd:
        return ld
    else:
        return gd


# In[8]:


recDepth(head,0)


# In[9]:


sum(depth)/len(depth)


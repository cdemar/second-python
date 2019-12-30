"""
Read in all the baby names. Place them on a 3 link tree
(less than, greater than, and equal to)

Traverse the tree, and count the number of names equal to for each name. (done)

Traverse the tree, and link on a second set of gpt, lpt links by count.

Traverse the count tree, and print the 5 names with the most counts
and the count for each name.

cut and paste your code and program results in the wrapper file.
"""

name_count = {}

# class for a the name
class name_Word:
    """Contains the information for a phrase starting with a word"""
    def __init__(self,word, cnt):
        """word is the food word that starts a phrase"""
        self.lpt = None # the nodes less than this word
        self.ept = None # the nodes the same as this word
        self.gpt = None # the nodes greater than this word
        self.clpt=None # count less than or equal to links
        self.cgpt=None # count greater than links
        self.word = word # the food word this element handles
        self.count = cnt
        self.sum=0

head = None

# This puts the name into the binery tree
def addNameLink(cn, fw):
    """Adds a Name.
cn is the current node
fw is the word being added"""
    if fw.word == cn.word:
        fw.ept = cn.ept # pushes to the front of the linked list
        cn.ept = fw
    elif fw.word <= cn.word:
        if cn.lpt == None:
            cn.lpt = fw
        else:
            addNameLink(cn.lpt, fw) # move down the left side
    else:
        if cn.gpt == None:
            cn.gpt = fw
        else:
            addNameLink(cn.gpt, fw)

# This looks just at the name to put on the head
def addNameWord(fw):
    global head
    if head == None:
        head = fw
    else:
        addNameLink(head, fw)


headNum = None

# This looks at the name count to see what is bigger
def addNumLink(fw, cn):
    """Adds a Number.
cn is the word being added
fw is the current node"""
    if cn.num == fw.num:
        cn.ept = fw.ept # pushes to the front of the linked list
        fw.ept = cn
    elif cn.num <= fw.num:
        if fw.lpt==None:
            fw.lpt=cn
        else:
            addNumLink(cn, fw.lpt) # move down the left side
    else:
        if fw.gpt == None:
            fw.gpt = cn
        else:
            addNameLink(cn, fw.gpt)
            
# This makes the head of the amount per persion
def addNumWord(fw):
    global headNum
    if headNum == None:
        headNum = fw
    else:
        addNumLink(headNum, fw)

# This adds up the amount per name
def addemup(n):
    if n == None:
        return
    addemup(n.lpt)
    e=n.ept
    while(e != None):
        n.sum += e.count
        e=e.ept
    n.sum += n.count
    addemup(n.gpt)

# This looks at all the names from 1880 to 2015
# and would read them all
def onefile():
    firstyr = 1880
    lastyr = 2015
    global name_count
    for year in range(firstyr, lastyr):
        filename = "C:\\Users\\coryd\\Desktop\\python_class_idle\\names_baby\\yob{0}.txt".format(year)
        with open(filename,'r') as f:
            for l in f:
                x = l.strip().split(',')
                name = x[0]
                numbers = int(x[2])
                w=(name,numbers)
                addNameWord(w)
                addNumWord(w)

onefile()

addemup(head)

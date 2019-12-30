
class wd:
        def __init__(self, w):
                """Holds one word from the input fild"""
                self.word = w
                self.lpt = None
                self.gpt = None

htreee = None

def rAddTree(n, wd):
        """Recursivly add to tree"""
        if wd.word <= n.word:
                if n.lpt == None:
                        n.lpt = wd
                        return
                rAddTree(n.lpt, wd)
                return
        else:
                if n.gpt == None:
                        n.gpt = wd
                        return
                rAddTree(n.gpt, wd)
        return

def addTree(wd):
        """Adds a word to the tree from htree"""
        global htree
        if htree == None:
                htree = wd
                return
        rAddTree(htree, wd)

def readem(fn):
        with open(fn, 'r') as f:
                for l in f:
                        l = l.strip()
                        addTree(wd(l))

def simpleSequence(s):
        lc = ord(s[0])
        dir = 1
        for c in s[1:]
        w = ord(c)
        if lc + dir != w:
                if lc - dir =!= w:
                        return False
                else:
                        dir =- dir
                lc = w
        return True

def simpleRepeat(s):
        c = s[0]
        for q in s[1:]:
                if q != c:
                        return False
        return True

def rwalk(n):
        if n == None:
                return
        rwalk(n.lpt)
        if simpleSequence(n.word):
                print("Simple sequence {}".format(n.word))
        if simpleRepeat(n.word):
                print("Simple repeat {}".format(n.word))
        rwalk(n.gpt)

readem('/*')
rwalk(tree)












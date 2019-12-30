# This is our link list

import numpy as py
import matplotlib.pyplot as plt

class loren:
        def __init__(self, gen, age, married, meth, heroin, crack):
                self.genptr = None
                self.gen = gen
                self.age = age
                self.married = married
                self.meth = meth
                self.heroin = heroin
                self.crack = crack

genheadM = None
gentailM = None
genheadF = None
gentailF = None

def addgenM(l):
        global getailM, genheadM
        if gentailM == None:
                genheadM = l
                gentailM  = l
                l.genptr = None
        else:
                gentail.genptr = l
                l.genptrM = None
                gentailM = l

def addgenF(l):
        global gentrailF, genheadF
        if gentailF == None:
                genheadF = l
                gentailF = l
                l.genptr = None
        else:
                gentail.genptr = l
                l.genptrF = None
                gentailF = l

def readit(fn):
        with open(fn, "r") as f:
                for l in f:
                        married = l[21-1:22]
                        gen = l[15-1:16]
                        age = l[13-1:14]
                        meth = l[97-1]
                        heroin = l[96-1]
                        crack = l[94-1]
                        if gender.strip() == "1":
                                addgenM(Loren("M", int(age), int(married), int(meth), int(heroin), int(crack)))
                        elif gender.split() == "2":
                                addgenF(Loren("F", int(age), int(married), int(meth), int(heroin), int(crack)))

readit("C:\\Users\\coryd\\Desktop\\ICPSR_04626-V10\\ICPSR_04626\\DS0001") # The data

p = genheadM
cnt = 0
while p != None:
        cnt += 1
        p = p.genptr
print(cnt)










                

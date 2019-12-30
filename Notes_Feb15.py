"""
ICPSR
stay away from the restricted-use data

{ } = search
[ ] = order seq.
"""

import numpy as np
import random
import time

bob = [random.random() for x in range(10000)]

def testit(n):
        start_time = time.clock()
        for x in range(n):
                sue = random.random()
                if sue in bob:
                        flag = 1
                else:
                        flag = 0
        stop_time = time.clock()
        print("time {0}".format(stop_time - start_time))

testit(1000)

# differ thing

class kasia:
        def __init__(self):
                self.education = []
              #  self.age = []
                # self.drug = []
                self.crack = []
                self.heroin = []
                self.meth = []
                

liz = kasia()
# import pdb  # the de-bigger
import os  # is the weeker one

def getstuff(fn):
        global liz
        with open(fn, "r") as f:
                for l in f:
                       # age_code = int(l[13 -1:14])
 #                       print(age_code)
                        edu_code = int(l[23-1:24])
 #                       print(edu_code)
                        alcdrug_code = int(l[111-1:112])
 #                       print(alcdrug_code)
                        crack_code = int(l[94-1])
 #                       print(crack_code)
                        haroin_code = int(l[96-1])
 #                       print(heroin_code)
                        meth_code = (l[101-1])
 #                       print(meth_code)

 # new stuff 
                         katherine = crack_code + heroin_code + meth_code
                         if lkatherine >0:
                                liz.education.append(edu_code)
                                liz.crack.append(crack_code)
                                liz.haroin.append(haroin_code)
                                liz.meth.append(meth_code)
# end of new stuff


len(liz.drugs)

getstuff("C:\\Users\\coryd\\Desktop\\ICPSR_04626-V10\\ICPSR_04626\\DS0001") # The path finder

"""EVERYTHING BEFORE THIS WAS LAST LASS

# look up pdb

np.corrcoef([liz.age, liz.education, liz.drugs])

shaheer = [0 for x in range(13)]
shaheer_people = [0 for x in range(13)]
for vvv in range(len(liz.age)):
        if liz.education[vvv] > 0:
                shaheer[liz.age[vvv]] += liz.drugs[vvv]
                shaheer_people[liz.age[vvvv]] += 1
for  www in range(len(shaheer)):
        if shaheer[_people[www] > 0:
                shaheer[www] = shaheer[www] / len(liz.drugs)
plt.plot(shaheer)
plt..show()

"""

np.corrcoef([liz.age, liz.education, liz.drugs])

shaheer_meth = [0 for x in range(6)]
shaheer_crack = [0 for x in range(6)]
shaheer_heroin = [0 for x in range(6)]

for vvv in range(len(liz.age)):
        if liz.education[vvv] > 0:
                if liz.meth[vvv] > 0:
                        shaheer_meth[liz.education[vvv]] += 1
                if liz.crack[vvv] > 0:
                        shaheer_crack[liz.education[vvv]] += 1
                if liz.haroin[vvv] > 0:
                        shaheer_heroin[liz.education[vvv]] += 1

plt.plot(shaheer_meth, "*c")
plt.plot(shaheer_crack, "b")
plt.plot(shaheer_heroin, "r")
plt..show()
np.corrcoef([shaheer_meth, shaheer_crack, shaheer_heroin])
print(shaheer_crack[5]/shaheer_crack[3])



                        

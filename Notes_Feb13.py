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
                self.age = []
                self.drug = []

liz = kasia()
import pdb # better for coding
# inport os is the weeker one

def getstuff(fn):
        global liz
        with open(fn, "r") as f:
                for l in f:
                        age_code = int(l[13 -1:14])
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
                        liz.education.append(edu_code)
                        liz.age.append(age_code)
                        liz.drugs.append(crack_code + heroin_code + meth_code)
  #                      pdb.exit()


len(liz.drugs)




                        
                        

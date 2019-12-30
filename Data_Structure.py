"""
Create a structure of related experiment data
Include by subject, and by experiment step.
You may use publicly available economic data also.
"""
import matplotlib.pyplot as plt
import numpy as np

class mark:
        def __init__(self):
                self.alcdrug = [] # Substance abuse type
                self.stfips = [] # censur states at admission

info = mark()

state = [[0 for x in range(4)] for x in range(73)]

def getstuff(fn):
        global info
        with open(fn, "r") as f:
                for l in f:
                        drug_code = int(l[111-1:112])
                        #print(drug_code)
                        state_code = int(l[37-1:38])
                        #print(state_code)
                        
                        info.alcdrug.append(drug_code)
                        info.stfips.append(state_code)
                        try:
                                state[state_code][drug_code] += 1
                        except:
                                print(state_code)
                                print(drug_code)
# The path finder
getstuff("C:\\Users\\coryd\\Desktop\\python_class_idle\\SAMHDA\\04626-0001-Data.txt")

len(info.stfips)

np.corrcoef([info.alcdrug, info.stfips])

"""
drug_code[none, alcohol_only, drug_only, both]

It looks at each state where 'x' gets through each one,
'range(len(state))' states it is looking at the lenth of the
range of 'state'. The second part is looking at the
spasific part of the 'drug' in the above 'drug_code'.
"""
none = [state[x][0] for x in range(len(state))]
alcohol_only = [state[x][1] for x in range(len(state))]
drug_only = [state[x][2] for x in range(len(state))]
both = [state[x][3] for x in range(len(state))]

plt.xlabel("States")
plt.ylabel("Drug amount")
plt.plot(none, 'b')
plt.plot(alcohol_only, 'r')
plt.plot(drug_only, 'g')
plt.plot(both, 'k')
plt.show()

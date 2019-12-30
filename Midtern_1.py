# Midtern 1 code

import numpy as py
import matplotlib.pyplot as plt

first = 1
last = 56

nr = []
sn = []

def onefile(yr):
    global info
    fn = 'C:\\Users\\coryd\\Desktop\\python_class_idle\\mid_data.txt'
    with open(fn, 'r') as f:
            f.readline()
            for l in f:
                cols = l.strip().split('\t')
                if len(cols) > 1:
                    state = cols[0][1:-1]
                    stateCode = float(cols[1][1:-1])
                    death = float(cols[2])
                    people = float(cols[3])
                    rate = death / people
                    nr.append(rate)
                    sn.append(state)

onefile(5)

xv = [x for x in range (first, last)]

print("The state that has the min amount was", sn[nr.index(min(nr))], "at", min(nr))
print("The state that has the max amount was", sn[nr.index(max(nr))], "at", max(nr))

plt.plot(nr)
plt.show()

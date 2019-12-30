import matplotlib.pyplot as plt
import numpy as np

#makes the male/female dictionary
MF = {"M":{}, "F":{}}

firstyr = 1880
lastyr = 2015

#where the files are located
dirname = "C:\\Users\\coryd\\Desktop\\python_class_idle\\names_baby"

def onefile(yr):
    """processes a file for one year.
assumes the file is in diffectory
contained in global varialbe dirname"""

    global MF
    filename = "{0}/yob{1:4d}.txt".format(dirname,yr)
    f = open(filename, "r")
    for l in f:
        cols = l.strip().split(",")
        name = cols[0]
        gender = cols[1]
        cnt = float(cols[2])
        if not (name in MF[gender]):
            MF[gender][name] = [0.0 for x in range(firstyr, lastyr)]
        MF[gender][name][yr-firstyr] = cnt
    f.close()

def readall():
    for yr in range (1880,2015):
        onefile(yr)

readall()

xv = [x for x in range (1880,2015)]

# What sex are you looking for?
sex = "M"

# what name are you looking for?
name = "Cory"

print ("Now for the hunt for someone like " + name)
bestname = ""
bestvalue = -1000.0
tname = name
for n in MF[sex].keys():
        if n == name:
                continue
        corrcoef = np.corrcoef(MF[sex][tname], MF[sex][n])
        corx = corrcoef[1,0]
        if corx  > bestvalue:
                bestvalue = corx
                bestname = n
print(bestname, bestvalue)
plt.plot(xv, MF[sex][tname], "r")
plt.xlabel("year")
plt.ylabel("Numbers")
plt.title("{0}, {1}".format(name, sex))
plt.show()
plt.plot(xv, MF[sex][bestname], "b")
plt.xlabel("year")
plt.ylabel("Numbers")
plt.title("{0}, {1}".format(bestname, sex))
plt.show()

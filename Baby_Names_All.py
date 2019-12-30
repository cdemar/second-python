import matplotlib.pyplot as plt

#makes the male/female dictionary
MF = {"M":{}, "F":{}}

firstyr = 1880
lastyr = 2015

#where the files are located
dirname = "Users⁩\\corydemar\⁩\⁨Desktop⁩\\⁨Programing\⁩\⁨python_class_2\\⁨names_baby⁩"

def onefile(yr):
    """processes a file for one year.
assumes the file is in diffectory
contained in global varialbe dirname"""

    global MF
    filename = "{0}/yob{1:4d}.txt".format(dirname, yr)
    f = open(filename, "r")
    for l in f:
        cols = l.strip().split(",")
        name = cols[0]
        gender = cols[1]
        cnt = float(cols[2])
        if not (name in MF[gender]):
            #print(MF)
            #print('this is after')
            MF[gender][name] = [0.0 for x in range(firstyr, lastyr)]
            #print(MF)
            #print(len(MF[gender][name]))
        MF[gender][name][yr-firstyr] = cnt
        #print(MF)
    f.close()

def readall():
    for yr in range (firstyr,lastyr):
        onefile(yr)

readall()

xy = [x for x in range (firstyr, lastyr)]

plt.plot(xy,MF["M"]["Cory"])
plt.show()

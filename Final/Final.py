#
# Coders: Cory DeMar & Blake Francis
# Predicting the best College Basketball players (based on position)
# Took about 18 hrs for the whole thing
# Sources
# http://www.espn.com/mens-college-basketball/statistics
# https://www.basketball-reference.com/leagues/NBA_2017_per_game.html
#

import statsmodels.formula.api as smf
import pandas as pd

# Pro Stats column 6-30
proG = []
proF = []
proC = []
# Pro PER column 31
proG2 = []
proF2 = []
proC2 = []
# College Stats 2-12
clgG = []
clgF = []
clgC = []
# College player names 1
nmG = []
nmF = []
nmC = []
# Vector lists
listG = []
listF = []
listC = []

def read_pro(fn):
        with open(fn, 'r') as f:
                next(f)
                for l in f:
                        l = l.strip().split(',')
                        Pos = l[2] # Pro Position
                        if Pos == 'G':
                                proG2.append(l[30])
                        if Pos == 'F':
                                proF2.append(l[30])
                        if Pos == 'C':
                                proC2.append(l[30])
                        if Pos == 'G':
                                proG.append(l[5:30])
                        if Pos == 'F':
                                proF.append(l[5:30])
                        if Pos == 'C':
                                proC.append(l[5:30])
                        
read_pro("C:/Users/coryd/Desktop/python_class_idle/Final/Stats Pro.csv")

def read_clg(fn):
        with open(fn, 'r') as f:
                next(f)
                for l in f:
                        l = l.strip().split(',')
                        MIN = float(l[2]) # Players average time
                        Pos = l[14] # College Position
                        if Pos == 'G' and MIN >16:
                                nmG.append(l[0])
                        if Pos == 'F' and MIN >16:
                                nmF.append(l[0])
                        if Pos == 'C' and MIN >16:
                                nmC.append(l[0])
                        if Pos == 'G' and MIN >16:
                                clgG.append(l[2:12])
                        if Pos == 'F' and MIN >16:
                                clgF.append(l[2:12])
                        if Pos == 'C' and MIN >16:
                                clgC.append(l[2:12])

read_clg("C:/Users/coryd/Desktop/python_class_idle/Final/College Basketball Teams.csv")

# we have to go two 'for loops' deep
# i is looking at first loop
# j is looking at second loop

# Reads Pro
intProG = [[float(j) for j in i] for i in proG]
intProF = [[float(j) for j in i] for i in proF]
intProC = [[float(j) for j in i] for i in proC]
# Read Pro
intProG2 = [float(i) for i in proG2]
intProF2 = [float(i) for i in proF2]
intProC2 = [float(i) for i in proC2]
# Read college
intClgG = [[float(j) for j in i] for i in clgG]
intClgF = [[float(j) for j in i] for i in clgF]
intClgC = [[float(j) for j in i] for i in clgC]

# Read in Pro data into 3 different data frames (position based)
dfGP = pd.DataFrame(intProG, columns = ['G', 'GS', 'MP', 'FG', 'FGA', 'FGP', 'THREEP', 'THREEPA', 'THREEPP', 'TWOP', 'TWOPA',
                                        'TWOPP', 'EFGP', 'FT', 'FTA', 'FTP', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PPG'])
dfFP = pd.DataFrame(intProF, columns = ['G', 'GS', 'MP', 'FG', 'FGA', 'FGP', 'THREEP', 'THREEPA', 'THREEPP', 'TWOP', 'TWOPA',
                                        'TWOPP', 'EFGP', 'FT', 'FTA', 'FTP', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PPG'])
dfCP = pd.DataFrame(intProC, columns = ['G', 'GS', 'MP', 'FG', 'FGA', 'FGP', 'THREEP', 'THREEPA', 'THREEPP', 'TWOP', 'TWOPA',
                                        'TWOPP', 'EFGP', 'FT', 'FTA', 'FTP', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PPG'])

# Adding Dependent Variable to each model
dfGP['PER'] = pd.Series(intProG2)
dfGP

dfFP['PER'] = pd.Series(intProF2)
dfFP

dfCP['PER'] = pd.Series(intProC2)
dfCP

# Just the Guards
# Dropping Stats columns that we dont need
dfGP.drop(['G', 'GS', 'FG', 'FGA', 'THREEP', 'THREEPA', 'TWOP', 'TWOPA', 'TWOPP',
           'EFGP', 'FT', 'FTA', 'ORB', 'DRB', 'TRB', 'STL', 'BLK', 'TOV', 'PF'], axis = 1)

modelG = smf.ols(formula = 'PER ~ MP + FGP + THREEPP + FTP + AST + PPG', data = dfGP).fit()

print("The info for Guards")
print(modelG.params)
print()

# Just the Forward
dfFP.drop(['G', 'GS', 'FG', 'FGA', 'THREEP', 'THREEPA', 'THREEPP', 'TWOP', 'TWOPA', 'TWOPP',
           'EFGP', 'FT', 'FTA', 'FTP', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'TOV', 'PF'], axis = 1)

modelF = smf.ols(formula = 'PER ~ FGP + BLK + MP + PPG', data = dfFP).fit()

print("The info for Forwards")
print(modelF.params)
print()

# Just the Center
dfCP.drop(['G', 'GS', 'FG', 'FGA', 'THREEP', 'THREEPA', 'THREEPP', 'TWOP', 'TWOPA',
           'TWOPP', 'EFGP', 'FT', 'FTA', 'ORB', 'DRB', 'AST', 'STL', 'TOV', 'PF'], axis = 1)

modelC = smf.ols(formula = 'PER ~ BLK + FGP + TRB + FTP + MP + PPG', data = dfCP).fit()

print("The info for Centers")
print(modelC.params)

# Put college data into data frame
dfGC = pd.DataFrame(intClgG, columns = ['MP', 'PPG', 'TRB', 'AST', 'SPG', 'BLK', 'TPG', 'FGP', 'FTP', 'THREEPP'])
dfFC = pd.DataFrame(intClgF, columns = ['MP', 'PPG', 'TRB', 'AST', 'SPG', 'BLK', 'TPG', 'FGP', 'FTP', 'THREEPP'])
dfCC = pd.DataFrame(intClgC, columns = ['MP', 'PPG', 'TRB', 'AST', 'SPG', 'BLK', 'TPG', 'FGP', 'FTP', 'THREEPP'])
# The ones that are being droped
mydfGC = dfGC.drop(['TRB', 'SPG', 'BLK', 'TPG'], axis = 1)
mydfFC = dfFC.drop(['TRB', 'AST', 'SPG', 'TPG', 'FTP', 'THREEPP'], axis = 1)
mydfCC = dfCC.drop(['AST', 'SPG', 'TPG', 'THREEPP'], axis = 1)
# The ones being used
newdfGC = mydfGC[['MP', 'FGP', 'THREEPP', 'FTP', 'AST', 'PPG']]
newdfFC = mydfFC[['FGP', 'BLK', 'MP', 'PPG']]
newdfCC = mydfCC[['BLK', 'FGP', 'TRB', 'FTP', 'MP', 'PPG']]

modelG = modelG.predict(newdfGC)
modelF = modelF.predict(newdfFC)
modelC = modelC.predict(newdfCC)

# This pairs with the names with the PER
# and puts them into a list of vectors for Guard.
for i in range(len(modelG)):
        if modelG[i]:
                modelG_list = (nmG[i], modelG[i])
                listG.append(modelG_list)

sortedG = sorted(listG, key = lambda tup:tup[1], reverse = True)

# This pairs with the names with the PER
# and puts them into a list of vectors for Forward.
for i in range(len(modelF)):
        if modelF[i]:
                modelF_list = (nmF[i], modelF[i])
                listF.append(modelF_list)

sortedF = sorted(listF, key = lambda tup:tup[1], reverse = True)

# This pairs with the names with the PER
# and puts them into a list of vectors for Center.
for i in range(len(modelC)):
        if modelC[i]:
                modelC_list = (nmC[i], modelC[i])
                listC.append(modelC_list)

sortedC = sorted(listC, key = lambda tup:tup[1], reverse = True)

# Printing out top 10
print()
print("Top Guards looking at players with at least 16 minutes of average playing time")
for i in range(len(sortedG)):
        if i < 10:
                print(sortedG[i])
print()
print("Top Forwards looking at players with at least 16 minutes of average playing time")
for i in range(len(sortedF)):
        if i < 10:
                print(sortedF[i])
print()
print("Top Centers looking at players with at least 16 minutes of average playing time")
for i in range(len(sortedC)):
        if i < 10:
                print(sortedC[i])

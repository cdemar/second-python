#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests

kasia = requests.get("https://www.finance.yahoo.com")
#print(kasia.text)

soup = BeautifulSoup(kasia.text, "lxml")

links = soup.find_all('a')
#print(links)

refs = [ x.get('href') for x in links if x.get('href') != None]

baddies = ["ucdavis", "#"]

refs2 = []
for bob in refs:
        if bob != None:
                ok = True
                for test in baddies:
                        if (test in bob) or (bob[0] == '/'):
                                 ok = False
                if ok:
                        refs2.append(bob)
                                
for l in refs2:
        print(l)

print(len(refs2))

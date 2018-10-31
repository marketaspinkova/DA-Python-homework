"""
ja = {"jmeno": "Marketa", "prijmeni": "Spinkova", "happy" : True}
print(len(ja))
print(ja["jmeno"])

hani = {"jmeno": "Hana", "prijmeni": "Benesova", "happy" : True}

my = [ja, hani]
print(my[1]["jmeno"])
"""

kurz = {
  "nazev": 'Úvod do programování',
  "lektor": 'Martin Podloucký',
  "konani": [
    {
      "misto": 'T-Mobile', 
      "koucove": [
        'Dan Vrátil', 
        'Filip Kopecký', 
        'Martina Nemčoková'
      ], 
      "ucastnic": 30
    },
    {
      "misto": 'MSD IT', 
      "koucove": [
        'Dan Vrátil', 
        'Zuzana Tučková', 
        'Martina Nemčoková'
      ], 
      "ucastnic": 25
    },
    {
      "misto": 'Škoda DigiLab', 
      "koucove": [
        'Dan Vrátil', 
        'Filip Kopecký', 
        'Kateřina Kalášková'
      ], 
      "ucastnic": 41
    }
  ]
}

"""
print(kurz["konani"][-1]["koucove"])

print(kurz["konani"][-1]["ucastnic"])
print(kurz["konani"][0]["koucove"][-1])
print(len(kurz["konani"]))
print([k["misto"] for k in kurz["konani"]])
"""
"""
Vypište na výstup počet účastnic na posledním konání kurzu.
Vypište na výstup jméno posledního kouče na prvním konání kurzu.
Vypište na výstup celkový počet konání kurzu.
Vypište na výstup všechna místa, na kterých se kurz konal. Použijte chroustání seznamů.
"""
"""
import json


soubor = open("absolventi.json", encoding = "utf-8")
obsah = soubor.read()

slovnik = json.loads(obsah)

print(slovnik)

soubor.close()
print(slovnik[0]["jmeno"])
"""

"""
recept = {
  'nazev': 'Batáty se šalvějí a pancettou',
  'narocnost': 'stredni',
  'doba': 30,
  'ingredience': [
    ['batát', '1', '15 kč'],
    ['olivový olej', '2 lžíce', '2 kč'],
    ['pancetta', '4-6 plátků', '21 kč'],
    ['přepuštěné máslo', '2 lžíce', '5 kč'],
    ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
    ['sůl', '1/2 lžičky', '0.1 kč'],
    ['muškátový oříšek', 'špetka', '1 kč'],
    ['česnek', '2 stroužky', '1 kč'],
    ['šalvějové lístky', '20-25', '12 kč']
  ]
}

from math import ceil
cena = [recept["ingredience"][x][2] for x in range(len(recept["ingredience"]))]
cena = ceil(sum([float(c.replace(" kč", "")) for c in cena]))

print(cena)
"""
"""
Vypište pomocí funkce print() kolik bude celé jídlo stát korun zaokrouhleně na celé koruny nahoru.
"""


"""
import requests
import json
requests = requests.get("http://api.kodim.cz/python-data/people")
lidi = json.loads(requests.text)


print(len(lidi))
print(lidi[0])

female = 0
male = 0
for x in range(len(lidi)):
	if lidi[x]["gender"] == "Female":
		female = female + 1
	if lidi[x]["gender"] == "Male":
		male = male + 1

print(female)
print(male)
"""
"""
Zjistěte kolik lidí celkem seznam obsahuje.
Zjistěte jaké všechny informace máme o jednotlivých osobách.
Zjistěte, kolik je v souboru mužů a žen.
"""

import sys
month = sys.argv[2]
day = sys.argv[1]

address = "http://svatky.adresa.info/json?date="
address = address + day + month

import requests
import json
requests = requests.get(address)
names = json.loads(requests.text)

print(names)
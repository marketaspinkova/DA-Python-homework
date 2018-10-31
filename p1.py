"""
otázky:
1. jaký je úzus odražení? jak tady funguje to automatické odražení (vypadá jako šipka)?
2. jak poznám, kdy se jak píše atribut? např. sort(seznam) a seznam.sorted()? a jaký je mezi sort a sorted rozdíl? (6)
3. jak napsat novou fci pro práci se seznamem? ad např úkol 9 (jak se píše, že atributem je, že musíme mít seznam)
5. seznamy (6) - jak to udělat, když chci přidat víc prvků, ale není to range? plus mi u 6 nefunguje automatizace


"""


"""
#4 urok v bance______________________________________________________________________
money = 1000000
interest = 0.024
years = 10
for x in range(years):
    money = money + money * interest
print("The final sum is", round(money), "CZK.")
"""

"""
#5 délka filmu ___________________________________________________________________________
name = "Two Towers"
length_min = 223
hours = length_min // 60
minutes = length_min % 60
print("The film", name, "is", hours, "hours and", minutes, "minutes long.")
"""


#6 teploty__________________________________(jak to udělat, když chci přidat víc prvků, ale není to range?)

years = []
years.extend(range(2001, 2011))

temperature = [7.8, 8.7, 8.2, 7.8, 7.7, 8.2, 9.1, 8.9, 8.4, 7.2]

columns = [years] + [temperature]

rows = []
for x in range(0, 10):
    rows.append(years[x], temperature[x])
print(rows)

# vznikne 10 podseznamů, ale je v nich vše, nejsou po dvojicích
"""
for x in range(0, 10):
    line = [columns[0][x], columns[1][x]]
    rows = []
    rows.extend(line)
print(rows)
# přidá se jen jeden prvek
"""


rows = [[2001, 7.8], [2002, 8.7], [2003, 8.2], [2004, 7.8], [2005, 7.7], [2006, 8.2], [2007, 9.1], [2008, 8.9], [2009, 8.4], [2010, 7.2]]

task_a = print(rows[2][1])
task_b = print(rows[4][0])
task_c = print(rows[-1])

#task_d
for x in range(2, 10):
    print(rows[x])

for x in range(2, 10):
    seznam_radky = [columns[0][x], columns[1][x]]
    print(seznam_radky)

#task_e
for x in range(2):
    print(rows[x])

#task_f zkouším pro random čísla
choice = [5, 6, 7, 8]
for x in choice:
    print(rows[x-1])

#task_g proč tu nefunguje sort?
print(sorted(temperature))

rows = [[2001, 7.8], [2002, 8.7], [2003, 8.2], [2004, 7.8], [2005, 7.7], [2006, 8.2], [2007, 9.1], [2008, 8.9], [2009, 8.4], [2010, 7.2]]

teploty = []
for x in range(10):
   teplota = rows[x][1]
   teploty.append(teplota)
print(sorted(teploty))
"""

"""
#7 Průměr
s = []
mean = sum(s) / len(s)
print(mean)
"""

"""
#8 Nový koberec________________________________________________________________________________

import math

room = 30
van = 5
side = round(math.sqrt(room), 2)

print("One side is", side , "metres.")
if side <= van:
    print("And it fits in the van!")
else:
    print("And it does not fit in the van.")
"""

"""
#9 Rozpětí - jak napsat novou funkci? ______________________________________________________

#def rozpeti([]):
#    rozpeti = max() - min()
#    print(rozpeti)

s = []
rozpeti = max(s) - min(s)
print(rozpeti)
"""

"""
#10 Vlastní minimum a maximum___________________________________________________

s = []
s2 = sorted(s)
mini = s2[0]
maxi = s2[-1]
print(mini, maxi)
"""

"""
#11 Střed seznamu_________________________________________________________________________

s = [5, 7, -11, 2]
x = round(len(s) / 2 + 0.1)
print(s[x])

s = [5, 7, -11, 2]
x = int(len(s) / 2)
print(s[x])
"""

"""
#12 Střed seznamu podruhé ______________________________________________________________________________

s = [5, 7, -11, 2]
if len(s) % 2 != 0:
    x = int(len(s) / 2)
    print(s[x])
else:
    x = int(len(s) / 2 - 1)
    print(s[x])


s1 = [5, 7, -11, 2, 7, 8]
s2 = [5, 7, -11, 2, 5]

x = len(s2) / 2 - 0.6
stred = s2[round(x)]
print(stred)
"""


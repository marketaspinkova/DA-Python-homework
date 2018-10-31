"""
# 4 Čas v minutách

import sys
hours = int(sys.argv[1])
minutes = int(sys.argv[2])
print(hours * 60 + minutes)
"""
"""
# 5 Zaokrouhlování

import sys
import math
number = float(sys.argv[1])
print(math.ceil(number))
print(math.floor(number))
print(round(number))
"""

"""
# 6 Doména na URL

import sys
domain = sys.argv[1]
print("http://" + domain)
"""

"""
# 7 Průměr versus medián

import sys
import statistics
values = (sys.argv[1:])
values = [int(v) for v in values]
print("Mean is", statistics.mean(values))
print("Median is", statistics.median(values))
"""


# 8 Klasické zaokrouhlování

import sys
import math
number = "2.5"


if number[-1] == "5":
   number[-1] = "6"
   print(round(float(number)))
else:
   print(round(float(number)))

"""
number = (sys.argv[1])
if number[-1] == "5":
    print(math.ceil(float(number)))
else:
    print(round(float(number)))
"""

"""
# 9 Minuty

import sys
casy = sys.argv[1:]
casy = [int(c) for c in casy]
dohodiny = [c < 60 for c in casy]
nadhodinu = [c > 60 and (c % 60) for c in casy]
print(dohodiny)
print(nadhodinu)
"""

"""
# 10 Fahrnheit vs. Celsius

import sys

F = int(sys.argv[1])
C = 5 * (F - 32) // 9
print(F, "stupnu Fahrenheita je", C, "stupnu Celsia.")
"""

"""
# 11 Cesta k souboru

import sys
path = sys.argv[1]
print(str(path.replace("\\", "/")))
"""

"""
# 12 Házení kostkou

import sys
import random

steny = int(sys.argv[1])
hody = int(sys.argv[2])
for h in range(hody):
    print(str(random.randint(1, steny)))

steny = int(sys.argv[1])
hody = int(sys.argv[2])
hodyseznam = []
hodyseznam.extend(range(1, hody))
result = [random.randint(1, steny) for h in hodyseznam] # nebo for h in range(hody)
print(result)
"""

"""
# 13 Karty 1__________________________________________________________
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "A"]
colours = ["kříže", "srdce", "piky", "káry"]

import random
print("Karta:", cards[random.randint(0, 11)], colours[random.randint(0, 3)])
"""

"""
# 14 Jak proměnit hada na velblouda________________________________________

import sys
print(sys.argv)

name = sys.argv[1]
name = (name.replace("_"," ")).split()
name = [n.capitalize() for n in name]
name = ("").join(name)
print(name)
"""
"""
# 14 Jak proměnit velblouda na hada________________________________________
import sys
import re

name = sys.argv[1]
name = re.findall('^[a-z]+|[A-Z][^A-Z]*', name)
name = [n.lower() for n in name]
name = ("_").join(name)

print(name)
"""
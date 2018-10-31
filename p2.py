"""
#2 Čísla jako text + 4 Zápis na jeden řádek
hodnoty = ['12', '1', '7', '-11']
hodnoty[2] = str(int(hodnoty[2]) + 4)
print(hodnoty)
"""
"""
#3 Čísla v textu
hodnoty = '12.1 1.68 7.45 -11.51'
add = 0.25
s = hodnoty.split( )
number = s[-1]
number = float(number)
number = number + add
number = str(number)
s[-1] = number
s = " ".join(s)
print(s)
"""

"""
mereni = ["12.1", "1.68", "7.45", "-11.51"]
print([str(round(float(m) for m in mereni.split(" ")))])
"""
"""
cisla = [[1, 2], [3, 4], [5, 6]]
print([sum(radek) for radek in cisla])
"""
"""
cisla = [1.12, 4.51, 2.64, 13.1, 0.1]
print([c * 2 for c in cisla])
print([c * -1 for c in cisla])
print([c * c for c in cisla])
print([str(c) for c in cisla])
"""

"""
jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']
print([len(j) for j in jmena])
print([j.upper() for j in jmena])
print([j + "a" for j in jmena])
print([j.lower() + '@email.cz' for j in jmena])
"""

teploty = [
  [2.1, 5.2, 6.1, -0.1],
  [2.2, 4.8, 5.6, -1.0],
  [3.3, 6.5, 5.9, 1.2],
  [2.9, 5.6, 6.0, 0.0],
  [2.0, 4.6, 5.5, -1.2],
  [1.0, 3.2, 2.1, -2.0],
  [0.4, 2.7, 1.3, -2.8]
]
"""
print([sum(t) / len(t) for t in teploty])

print([t[0] for t in teploty])

print([t[-1] for t in teploty])

print([[t[1], t[-1]] for t in teploty])

dny = ([sum(t) / len(t) for t in teploty])
print(sum(dny) / len(dny))

print(sum([sum(t) / len(t) for t in teploty]) / len([sum(t) / len(t) for t in teploty]))
"""

"""
veky = [35, 12, 44, 11, 18, 21, 28, 18]
print([18 - v for v in veky])
print([v >= 18 for v in veky])
print([v == 18 for v in veky])
"""

"""
delky = [136, 105, 82]
trvani = [(str(d // 60) + ":" + str(d % 60)) for d in delky]
print(trvani)
"""


kraje = [
  ['Hlavní město Praha', '1 280 508'],
  ['Jihočeský kraj', '638 782'],
  ['Jihomoravský kraj', '1 178 812'],
  ['Karlovarský kraj', '296 749'],
  ['Kraj Vysočina', '508 952'],
  ['Královéhradecký kraj', '550 804'],
  ['Liberecký kraj', '440 636'],
  ['Moravskoslezský kraj', '1 209 879'],
  ['Olomoucký kraj', '633 925'],
  ['Pardubický kraj', '517 087'],
  ['Plzeňský kraj', '578 629'],
  ['Středočeský kraj', '1 338 982'],
  ['Ústecký kraj', '821 377'],
  ['Zlínský kraj', '583 698']
]

misto = ([k[0] for k in kraje])


lide = ([k[1].split( ) for k in kraje])
lide = (["".join(l) for l in lide])
lide = ([int(l) for l in lide])

"""
table = [misto, lide]
print(table)
"""

hlasy = [ 
  [78774, 43179, 225111, 144799, 242854],
  [91062, 22451, 17475, 53391, 46450],
  [179186, 216499, 4493, 156305, 61222],
  [9619, 53476, 926, 64737, 34566],
  [66904, 85730, 27271, 12964, 38041],
  [118755, 1929, 30426, 25178, 31952],
  [64467, 40993, 81181, 39392, 4335],
  [11221, 97970, 26179, 98539, 112578],
  [171064, 7638, 8752, 96666, 39738],
  [74235, 101680, 18920, 45904, 1922],
  [39309, 1505, 10531, 30458, 40228],
  [131584, 1812, 241122, 22267, 99326],
  [194133, 39985, 200997, 28229, 20780],
  [66188, 51607, 15977, 177272, 17664]
]

kandidati = ["Rezek", "Doležal", "Bednář", "Brotz", "Kašpar"]

"""
print([print(k, "má", sum([h[0] for h in hlasy]), "hlasů." ) for k in kandidati])


rezek = sum([h[0] for h in hlasy])
dolezal = sum([h[1] for h in hlasy])
bednar = sum([h[2] for h in hlasy])
brotz = sum([h[3] for h in hlasy])
kaspar = sum([h[4] for h in hlasy])

vysledky1 = [rezek, dolezal, bednar, brotz, kaspar]
vysledky2 = list(enumerate(vysledky1, 1))
vysledky3 = sorted(vysledky2, key=lambda v: v[1])
print(vysledky3)
"""



# ucast_kraje

kraje = [
  ['Hlavní město Praha', '1 280 508'],
  ['Jihočeský kraj', '638 782'],
  ['Jihomoravský kraj', '1 178 812'],
  ['Karlovarský kraj', '296 749'],
  ['Kraj Vysočina', '508 952'],
  ['Královéhradecký kraj', '550 804'],
  ['Liberecký kraj', '440 636'],
  ['Moravskoslezský kraj', '1 209 879'],
  ['Olomoucký kraj', '633 925'],
  ['Pardubický kraj', '517 087'],
  ['Plzeňský kraj', '578 629'],
  ['Středočeský kraj', '1 338 982'],
  ['Ústecký kraj', '821 377'],
  ['Zlínský kraj', '583 698']
]

"""
ucast1 = [sum(h) for h in hlasy]

ucast2 = []
for x in range(14):
    u = round(ucast1[x] / lide[x] * 100)
    ucast2.append(u)

ucast3 = list(enumerate(ucast2, 1))
ucast4 = sorted(ucast3, key=lambda v: v[1])

print(ucast4)
"""

"""
vitez_kraj = [list(enumerate(h, 1)) for h in hlasy]
print([sorted(v, key=lambda v: v[1]) for v in vitez_kraj])
"""

x = []
x.extend(range(15))

kandidat_kraj = [h / lide[x] * 100 for h in hlasy ]

kandidat_kraj = []
for x in range(14):
    k = round(hlasy[x] / lide[x] * 100)
    kandidat_kraj.append(k)
print(kandidat_kraj)



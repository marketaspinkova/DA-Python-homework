"""
# 1 Výplata přesněji__________________________________________________________________________________

import sys
mzda = int(sys.argv[1])
vykaz = open("vykaz.txt")
za_rok = sum([int(v) * mzda for v in vykaz])
za_mesic = round(za_rok / 12)
print(za_rok, za_mesic)
program.close()
"""
"""
Zatím jsme výplatu počítali za předpokladu, že každý měsíc odpracujeme stejný počet hodin, což není příliš realistické. Vytvořte proto textový soubor vykaz.txt, který bude obsahovat 12 řádků a na každém řádku počet odpracovaných hodin za každý měsíc za poslední rok.

Otevřete tento soubor ve svém programu a načtěte hodnoty na řádcích do seznamu vykaz. Vytiskněte tento seznam na konzoli funkcí print() abyste si ověřili, že jste soubor načetli správně.
Nechte uživatele zadat na příkazovém řádku hodinovou mzdu. Spočítejte a na výstup vytiskněte celkovou výplatu za celý rok a průměrnou výplatu na jeden měsíc.
"""

"""
# 2 Počet slov _________________________________________________________________________________________

program = open("praha.txt", encoding='utf-8')
seznam = [radek.split(" ") for radek in program]
delka = [len(s) for s in seznam]
print("Řádky mají", delka, "slov.")
print("Delka je", sum(delka), "slov.")
program.close()
"""
"""
Stáhněte si odezdanou slohovou práci. Zadání bylo sepsat text o nejméně 150ti slovech pojednávající o našem hlavním městě. Napište program, který spočítá počet slov v tomto textu, abychom věděli, zda bylo zadání formálně splněno. Nechte se vést následujícím návodem.

Nechte váš program otevřít soubor a načíst jednotlivé řádky do seznamu.
Každý řádek převeďte na seznam slov. Slovem se rozumí vše, co je odděleneo mezerou nebo novým řádkem.
Vypište na výstup seznam hodnot udávající počty slov na každém řádku.
Vypište na výstup celkový počet všech slov v souboru.
"""

"""
# 3 Pujcovna___________________________________________________________________________________________

import sys
soubor = sys.argv[1]

program = open(soubor, encoding='utf-8')
seznam = [radek.strip() for radek in program]
seznam = [radek.replace("," , ".") for radek in seznam]
seznam = [radek.split(" ") for radek in seznam]
del(seznam[-1])
km = sum([float(x[1]) for x in seznam])
print("Auta dohromady najela", km, "km.")

program.close()
"""
"""
Půjčovna aut má v každém kraji ČR jedno auto s danou SPZ. Ke konci roku chce zjistit, kolik všechna auta najezdila dohromady kilometrů. V souboru auta.txt je pro každou SPZ zaznamenáno kolik dané auto ujelo kilometrů za daný rok. Hodnoty jsou v tísících kilometrů. Bohužel se v jednotlivých krajích blbě zkoordinovali a někdo používal desetinnou čárku, někdo zase tečku.

Napište program, který na výstup vypíše součet všech ujetých kilometrů. Jistě se vám bude hosti metoda řetězců jménem replace().
Upravte váš program tak, aby jméno souboru k otevření dostal na příkazové řádce, abychom mohli takto zpracovávat výkazy s různých souborů aniž bychom museli upravovat samotný kód programu.
"""

"""
# 4 Dny v měsíci_______________________________________________________________________________________


pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mesice = ["leden", "unor", "brezen", "duben", "kveten", "cerven", "cervenec", "srpen", "zari", "rijen", "listopad", "prosinec"]
soubor = open('kalendar.txt', 'w')

# a. [soubor.write(str(den) + "\n") for den in pocty_dni]
# b. [soubor.write(mesice[x] + "\t" + str(pocty_dni[x]) + "\n") for x in range(len(pocty_dni))]

soubor.write("měsíc" + "\t" + "počet dní" + "\n") and [soubor.write(mesice[x] + "\t" + str(pocty_dni[x]) + "\n") for x in range(len(pocty_dni))]

soubor.close()
"""
"""
Napište program, který bude mít přímo v kódu zapsaný počet dní v jednotlivých měsích takto:
pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
Nechte váš program vypsat tento seznam do souboru s názvem kalendar.txt, každé číslo na jeden řádek.
Upravte váš program tak, aby zároveň s počtem dnů vypisoval i název měsíce. Odělte v souboru název měsíce a počet dnů pomocí tabulátoru.
Upravte váš program tak, aby jako první řádek výsledného souboru obsahoval nadpisy pro jednotlivé sloupce, tedy měsíc a počet dní.
"""

"""
# 5. Rozepsaná výplata______________________________________________________________________________

import sys
mzda = int(sys.argv[1])

pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mesice = ["leden", "unor", "brezen", "duben", "kveten", "cerven", "cervenec", "srpen", "zari", "rijen", "listopad", "prosinec"]

vykaz = open("vykaz.txt", "w")
pocty_hodin = open("pocty_hodin.txt")
hodiny = [int(p.strip()) for p in pocty_hodin]

vykaz.write("měsíc" + "\t" + "počet dní" + "\n") and [vykaz.write(mesice[x] + "\t" + str(pocty_dni[x]) + "\t" + str(hodiny[x] * mzda) + "\n") for x in range(len(pocty_dni))]

vykaz.close()
pocty_hodin.close()
"""
"""
Modifikujte program pro počítání výplaty z předchozí sekce tak, aby nevypisoval průměrnou výplatu za rok, nýbrž aby vypsal konrétní vyplacenou částku pro každý měsíc zvlášť.

Nejprve tyto informace vypište na výstup pomocí funkce print().
Poté program upravte tak, aby vypsal tyto výsledky do souboru.
"""

"""
# 6. hody kostkou______________________________________________________________________________________

import random
import sys

hody = open("hody.txt", "w")
pocet_hodu = int(sys.argv[1])

[hody.write(str(random.randint(1, 12)) + ", ") for x in range(pocet_hodu - 1)] and hody.write(str(random.randint(1, 12)))

hody.close()
"""
"""
Napište program, který vytvoří seznam deseti náhodných hodů dvanáctistěnnou kostkou.
Nejdříve tento seznam vytiskněte na konzoli pomocí funkce print().
Upravte váš program tak, aby náhodné hody kostkou vypsal do souboru s názvem hody.txt na jeden řádek oddělené čárkou a mezerou.
Upravte váš program tak, aby počet hodů dostal jako parametr na příkazové řádce. Zkuste použitím vašeho program vyrobit 100, 1000 a 10 000 hodů.
"""
"""
# 7 Pasažéři______________________________________________________________________________________

pasazeri = open("pasazeri.txt")

passengers = [p.strip() for p in pasazeri]

passengers = [p.split(" ") for p in passengers]
dny = [[p.split(",") for p in passengers[x]] for x in range(len(passengers))]
print(dny)

# Napište program, který vypíše pro první den kolik pasažérů jelo celkem směrem tam a kolik směrem zpět.

den1_tam = sum([int(dny[0][x][0]) for x in range(len(dny[0]))])
den1_zpet = sum([int(dny[0][x][1]) for x in range(len(dny[0]))])
print(den1_tam)
print(den1_zpet)

# Nechť váš program vypisuje součty pasažárů ze celý týden, tedy kolik lidí za celý týden jelo směrem tam a kolik směrem zpět

tyden_tam = sum([sum([int(dny[y][x][0]) for x in range(len(dny[0]))]) for y in range(len(dny))])
tyden_zpet = sum([sum([int(dny[y][x][1]) for x in range(len(dny[0]))]) for y in range(len(dny))])
print(tyden_tam)
print(tyden_zpet)

pasazeri.close()
"""
"""
Autobus mezi Zdebudevsí a Kozoprdy jezdí čtyřikrát denně každý všední den v týdnu. Za poslední týden jsme naměřili počty pasažérů pro každou jízdu tam i zpět. Data jsou uložená v souboru pasazeri.txt. Jízda vždy obsahuje dvě čísla oddělená čárkou, která udávají počet pasažérů směrem tam a směrem zpět.
Nechť váš program vypisuje součty pasažárů ze celý týden, tedy kolik lidí za celý týden jelo směrem tam a kolik směrem zpět.
"""
"""
# 8 Přeznámkování_______________________________________________________________________________________

znamky = open("znamky.txt", encoding='utf-8')
znamky_nove = open("znamky_nove.txt", "w")

grades = [g.strip() for g in znamky]
grades2 = grades[1:]
grades2 = [g.replace("1", "A") for g in grades2] 
grades2 = [g.replace("2", "B") for g in grades2]
grades2 = [g.replace("3", "C") for g in grades2]
grades2 = [g.replace("4", "D") for g in grades2]
grades2 = [g.replace("5", "F") for g in grades2]

# alternativa
# letters = [_, "A", "B", "C", "D", "F"]
# grades2 = [letters[1] for grade in grades2]
#

print(grades2)

znamky_nove.write(grades[0] + "\n")
[znamky_nove.write(g + "\n") for g in grades2]

znamky_nove.close()
znamky.close()
"""
"""
Univerzita pro celoživotní vzdělávání se rozhodla změnit svůj známkovací systém z číselných známek 1 až 5 na hodnocení písmeny A až F. Bohužel změna se odehrála jaksi uprostřed semestru, takže je potřeba změnit aktuální výkazy o známkách z čísel na písmena. Nechte se vést následujícím postupem.

Otevřete si dokument s jedním výkazem známek.
Zkopírujte si tuto tabulku do textového souboru.
Napište program, který tuto tabulku načte ze souboru a změní všechny známky tak, že 1 bude A, 2 bude B, 3 bude C, 4 bude D a 5 bude F.
Vypište váš výsledek do nějakého souboru tak, aby se z něj dal zase zkopírovat do tabulky Google.
Vytvořte novou Google tabulku, která vypadá stejně jako ta výše avšak s převedenými známkami.
"""
"""
import sys
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])


if num2 == 0:
  print("nulou delit nelze")
else:
  podil = round((num1 / num2), 3)
  print(podil)
"""
"""
Napište program deleni.py, který na příkazové řádce obdrží dvě celá čísla a vypíše jejich podíl zaokrouhlený na tři desetinná čísla. Pokud je druhé číslo 0, program vypíše hlášku, že nulou dělit nelze.
"""

"""
import sys
name = sys.argv[1]
age = int(sys.argv[2])

if age >= 18:
    print(name "muze vstoupit.")
else:
    print(name "ma vstup zakazan.")
"""
"""
Napište program prihlaseni.py, který na příkazové řádce obdrží jméno uživatele a jako věk. Pokud má uživatel alespoň 18 let, program vypíše zprávu že uživatel může vstoupit, v opačném případě, že vstup je zakázán.
"""

"""
import sys
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])

if num1 >= num2 and num1 >= num3:
    print(num1, "je nejvetsi.")
    exit()

if num2 >= num1 and num2 >= num3:
    print(num2, "je nejvetsi.")
    exit()

if num3 >= num2 and num3 >= num1:
    print(num3, "je nejvetsi.")
    exit()
"""
"""
5. Napište program max2.py, který dostane na vstupu tři celá čísla a vrátí větší z nich.
"""

"""
import sys
num = sys.argv[1:]
num = [int(n) for n in num]

for n in num:
    print(n)

for n in num:
    print(n, n - 2 * n)

for n in num:
    if n > 0:
        print(n)

for n in num:
    if n >= 0:
        print(n)
    if n < 0:
        print(n - 2 * n)
"""
"""
6. Napište program, který dostane na příkazové řádce seznam celých čísel a
vypíše všechna tato čísla pod sebe, každé na nový řádek,
vypíše každé číslo spolu s jeho opačnou hodnotu (obrácené znaménko),
vypíše pouze čísla větší než 0,
čísla větší než 0 vypíše tak jak jsou, čísla menší než nula vypíše s obráceným znaménkem.
"""

"""
import sys
name = sys.argv[1]
password = sys.argv[2]
password_true = "lama"

if password == password_true:
	print("přístup povolen")
else:
	print("přístup odepřen")
"""
"""
7. Napište program login.py, který na příkazovém řádku obdrží uživatelské jméno a heslo. Program bude mít v sobě uloženo správné heslo a pokud jej uživatel zadá, program vypíše něco ve smyslu "přístup povolen". Zadá-li uživatel špatné heslo, program odpoví "přístup odepřen".
"""

"""
import sys
currency = sys.argv[1]
amount = int(sys.argv[2])

if currency == "EUR":
	print(amount * 27, "CZK")
elif currency == "CZK":
	print(round(amount / 27, 1), "EUR")
else:
	print("Please write in EUR or CZK.")
"""
"""
8. Napište program usd.py, který bude umět převádět měnu na americké dolary. 
"""




"""
9. Napište program, který s z textového souboru přečte seznam zůstatků na spořících účtech a vypíše tyto zůstatky navýšené o 2.5% úrok.
Vypište každý navýšený zůstatek na samostatný řádek.
Vypište jen ty zůstatky, které najsou záporné.
Zkuste jednotlivé řádky očíslovat. Každý řádek tedy bude obsahovat číslo řádku a výsledný zůstatek.
"""

"""
zustatky = open("zustatky.txt")
zust = [round(int(z) * 0.025 + int(z)) for z in zustatky]
zustatky.close()

print(zust)

x = 0
for z in zust:
	if z >= 0:
		print(x + 1, z)
		x = x + 1
"""
"""
9. Napište program, který s z textového souboru přečte seznam zůstatků na spořících účtech a vypíše tyto zůstatky navýšené o 2.5% úrok.
Vypište každý navýšený zůstatek na samostatný řádek.
Vypište jen ty zůstatky, které najsou záporné.
Zkuste jednotlivé řádky očíslovat. Každý řádek tedy bude obsahovat číslo řádku a výsledný zůstatek.
"""

num = [3, 5, 8, 0, 4, 2, 0, 7, 6, 2, 0, 5]
num2 = [3, 5, 8, 9, 10]


x = 1
found = 0
for n in num[1:]:
	if num[x] < num[x - 1]:
		print("no")
		found = 1
		exit()
	x = x + 1
if found == 0:
		print("yes")
		
	

"""
else:
		print("yes")
		break
Napište program, který o zadaném seznamu celých čísel rozhodne, zda jsou čísla v tomto seznamu vzestupně seřazena.
"""
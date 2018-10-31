mesta = ["Praha", "Brno", "Tabor", "Krumlov"]
soubor = open("mesta.txt", "w")
[soubor.write(mesto + "\n") for mesto in mesta]
soubor.close()
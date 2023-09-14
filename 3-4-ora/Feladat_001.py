# feladat_001
"""
Kérjük be a billenytűzetröl a nevünket, és irassuk ki a képernyőre!
A billentyűzet mindig szöveget (string-et) olvssuk be!
type(változó)
"""
vnev = input("Kérek egy vezetéknevet: ")
knev= input("kérek egy keresztnevet: ")
print(f"A megadott név a következő: {vnev} {knev}")

print(f"A vnev változó típusa: {type(vnev)}")
print(f"A knev változó típusa: {type(knev)}")
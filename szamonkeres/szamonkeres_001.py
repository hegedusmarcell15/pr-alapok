# Hegedűs Marcell 10/D 1.csoport
#Szamonkeres_001.py
"""
Bekérek egy osztályzatot 1-5 irassuk ki a megadott jegyet értékkel és
 szövegesen ha nem megfelelő jegset adtam akkor irja ki a jegy értékét és mellé hogy nem megfelelő jegy

"""
ertek = input("Kerek egy osztalyzatot:")
ertek = int(ertek)

if ertek == 5 :
    print(f"5, jeles")
elif ertek == 4 :
    print(f"4, jo")
elif ertek == 3 :
    print(f"3, kozepes")
elif ertek == 2 :
    print(f"2, elegseges")
elif ertek == 1 :
    print(f"1, elegtelen")
else :
    print(f"{ertek} nem megfelől jegy")

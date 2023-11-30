#Hegedűs Marcell 10/D 2023.10.30
#Sorszám: 6
#2 Feladat
import random
fej = "fej"
iras = "iras"
lista = (fej, iras)
(random.choice(lista))
fejiras = random.choice(lista)
gen = input(f'fej vagy írás:')

if gen == fejiras:
    print (f'eltaláltad')
else:
    print(f'nem talált')
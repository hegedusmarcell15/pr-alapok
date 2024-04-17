"""
A korok nevű listában tárol 5 darab kor obejktumot, melyek surgara
[0; 10] tartományba eső, véletlenszerűen előállított számérték. 
"""


import random

class Kor:
    osztaly_valtozo = 111
    evszam = 2024

    def __init__(self, sugar, kozeppont):
        self.sugar = sugar
        self.kozeppont = kozeppont
    
    def terulet(self):
        return self.sugar * pow(3.14, 2)

    def kerulet(self):
        return self.sugar * 3.14 * 2 


kor01 = Kor(5, (3, 7))
print(f"{kor01.terulet():.2f}")
print(f"{kor01.kerulet():.2f}")

kor02 = Kor(10, (1, 1))
print(f"{kor02.kerulet():.2f}")
print(f"{kor02.terulet():.2f}")


print(f"{kor01.kerulet() + kor02.kerulet():.2f}")
print(f"{kor01.terulet() + kor02.terulet():.2f}")


print(Kor.evszam)
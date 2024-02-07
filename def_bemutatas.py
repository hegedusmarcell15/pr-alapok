'''
#eljárás
def koszont_nevvel(nev) :
    print('Szia'+ nev +', üdv a fedélzeten!')

koszont_nevvel('Ádám')
'''
'''
def koszont_nevvel2(vezeteknev, keresztnev):
    print(f"Szia {vezeteknev} {keresztnev}, üdv a fedélzeten!")

koszont_nevvel2('Hegedűs', 'Marcell')
'''

#függvény
def koszont_nevvel1(nev1):
    uzenet = 'Szia' + nev1 +', üdv a fedélzeten'
    return uzenet

print(koszont_nevvel1('Ádám1'))
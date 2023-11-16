#feladat_017
#adatbekérés while-ciklussal 

#while szam < 5 or 10 < szam:

szam = int(input('Adj meg egy számot 5 és 10 között! '))
while not 5 <= szam <= 10:
    szam =int(input('Helytelen érték'))

print('Rendben')
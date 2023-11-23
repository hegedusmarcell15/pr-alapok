#Létre hozok egy  jelszót. Irassuk ki a képernyőre, hogy a belépéshez kérek egy jelszót.
#Kérjen a jelszót belépéshez. ha 5-ször rossz jelszót adtak meg akkor kiirja a program, rossz jelszót adtál meg több lehetőség nincsen.
#Ha jó a jelszó, írja ki , hogy a jó jelszó  sikeres belépés.

jelszo = "Kando"
proba = 0
keres = None
while jelszo!=keres or proba <5:
    keres = input("Add meg a jelszót: ")
    proba+=1
    if proba == 5:
        print("Nem jó a jelszó")
        break
    if keres == jelszo:
        print('Sikeres belépés')
        break
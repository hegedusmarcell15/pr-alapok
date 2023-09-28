sebesség = input ('Kérek egy sebességet:')
sebesség = int(sebesség)
if sebesség == 0:
    print(f'Megálltál')
elif sebesség <= 50:
    print(f'Megengedett sebesség')
elif sebesség <= 65:
    print(f'Büntetés 15000Ft')
elif sebesség <= 80:
    print(f'Büntetés 30000Ft')
elif sebesség <= 100:
    print(f'Bünetés 60000Ft')
else: 
    print(f'Elveszik a jogosítványod')
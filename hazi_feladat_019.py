szam = int(input('Adj meg egy páros számot! '))

for i in range(1, szam // 2 + 1):
    print('O' * i)

for i in range(szam // 2, 0, -1):
    print('O' * i)
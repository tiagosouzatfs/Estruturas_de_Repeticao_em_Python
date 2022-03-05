# Utilizei os naturais de 0 a 500 para ter onde parar pq senão demora demais.

a = 0
b = 0
c = 0

for a in range(0, 500):
    for b in range(0, 500):
        for c in range(0, 500):
            if (a**2 + b**2) == pow(c, 2) and (a+b+c) == 1000:
                print(a)
                print(b)
                print(c)
                print('-----------')

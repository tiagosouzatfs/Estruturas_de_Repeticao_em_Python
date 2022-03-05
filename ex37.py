
aux1 = 0
aux2 = 0
soma = 0
quadrado = 0
for i in range(1000, 10000):
    aux1 = int(i/100)
    aux2 = int(i%100)
    soma = aux1 + aux2
    quadrado = pow(soma, 2)
    if quadrado == i:
        print(i)
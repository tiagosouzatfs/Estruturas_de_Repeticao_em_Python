
print('Série S com 5 elementos')
n = 5
valor = 0
for elemento in range(0, n):
    if elemento == 0:
        valor = 0
        fatorial = 1
    else:
        cont = 1
        fatorial = 1
        while cont <= 2*elemento:
            fatorial = fatorial * cont
            cont = cont + 1

    valor = valor + (elemento/fatorial)

print('E = ', end='')
for num in range(0, n):
    if num == n-1:
        print(f'{num}/{2*num}! : = {valor}', end='')
    elif num == 0:
        print('0 + ', end='')
    else:
        print(f'{num}/{2*num}! + ', end='')
        
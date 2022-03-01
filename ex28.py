'''
0! = 1
1! = 1
2! = 2 x 1 = 2
3! = 3 x 2 x 1 = 6
4! = 4 x 3 x 2 x 1 = 24
.
.
.
n! = n x ... x 3 x 2 x 1 = m'''


n = 0
while n <= 0:
    n = int(input('Digite um número inteiro positivo para limitar a série E (Fatorial): '))

#n = 5
valor = 0
for elemento in range(0, n+1):
    if elemento == 0:
        valor = 0
        fatorial = 1
    if elemento == 1:
        valor = 1
        fatorial = 1

    else:
        cont = 1
        fatorial = 1
        while cont <= elemento:
            fatorial = fatorial * cont
            cont = cont + 1

    valor = valor + (1/fatorial)
#print(valor)

print('E = ', end='')
for num in range(0, n+1):
    if num == n:
        print(f'1/{num} : = {valor}', end='')
    elif num == 1:
        print('1/1 + ', end='')
    elif num == 0:
        print('1 + ', end='')
    else:
        print(f'1/{num} + ', end='')
        
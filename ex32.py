
n = 0
while n <= 0:
    n = int(input('Digite um número inteiro postivo: '))

d1 = 0
d2 = 0
for i in range(1, n+1):
    d1 = int(input('Digite um número: '))
    d2 = int(input('Digite um número: '))
    if (d1 > d2):
        print(f'O número {d1} é maior que o número {d2}')
    elif (d1 < d2):
        print(f'O número {d2} é maior que o número {d1}')
    else:
        print(f'O número {d1} é igual ao número {d2}')

n = 0
while n <= 0:
    n = int(input('Digite um número para o limite das sequências: '))

# sequência 1: 1+2+3+4+5+6+...+n
somador = 0
print('Sequência 1: ', end=' ')
for num in range(1, n+1):
    somador = somador + num
    if num == n:
        print(f'{num} = {somador}', end=' ')
    else:
        print(f'{num} + ', end=' ')

print('\n')

# sequência 2: 1-2+3-4+5-6+...+somatório n(-1)^(n-1)
# acho que o autor da lista copiou e colou o valor fim da sequência 3 (2n-1), a forma correta para esta sequência é somatório n(-1)^(n-1).
somador = 0
print('Sequência 2: ', end=' ')
for num in range(1, n+1):
    aux = num*((-1)**(num-1))
    somador = somador + aux
    if aux < 0:
        print(f'{aux} + ', end=' ')
    if aux > 0:
        print(f'{aux} ', end=' ')
    if num == n:
        print(f' = {somador}', end=' ')

print('\n')

# sequência 3: 1+3+5+7+...+(2n-1)
somador = 0
print('Sequência 3: ', end=' ')
for num in range(1, n+1):
    aux = (2*num) - 1
    somador = somador + aux
    if num == n:
        print(f'{aux} = {somador}', end=' ')
    else:
        print(f'{aux} + ', end=' ')
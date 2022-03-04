
n = 0
i = 0
j = 0
while n <= 0:
    n = int(input('Digite um número inteiro postivo para limitar a sequência de múltiplos: '))
    i = int(input('Digite um número inteiro postivo: '))
    j = int(input('Digite um número inteiro postivo: '))

contador = 0

print(f'A série de múltiplos de {i} e {j} em ordem crescente para {n} elementos é: ', end=' ')
for num in range(0, 1001):
    if contador == n:
        break
    elif num % i == 0 and num % j == 0:
        print(num, end=' ')
        contador = contador + 1
    elif num % i == 0 and num % j != 0:
        print(num, end=' ')
        contador = contador + 1
    elif num % i != 0 and num % j == 0:
        print(num, end=' ')
        contador = contador + 1
    
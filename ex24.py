
n = 0
while n <= 0:
    n = int(input('Digite um número inteiro positivo: '))

soma = 0
for divisores in range(1, n):
    if (n % divisores) == 0:
        print(divisores)
        soma = soma + divisores
print(f'O somatório de todos os divisores é: {soma}')
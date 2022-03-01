
n = 0
while n <= 0:
    n = int(input('Digite um número inteiro positivo: '))

for divisores in range(1, n+1):
    if (n % divisores) == 0:
        print(divisores)
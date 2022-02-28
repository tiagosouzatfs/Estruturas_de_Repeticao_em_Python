
n = 0
while n <= 0 or (n % 2) == 0:
    n = int(input('Digite um número inteiro positivo ímpar: '))

for num in range(n, 0, -1):
    if (num % 2) != 0:
        print(num)
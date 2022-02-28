
n = 0
while n <= 0 or (n % 2) == 0:
    n = int(input('Digite um número inteiro positivo ímpar: '))

for num in range(1, n+1):
    if (num % 2) != 0:
        print(num)
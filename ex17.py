
n = 0
soma = 0
while n <= 0:
    n = int(input('Digite um número inteiro positivo: '))

for num in range(1, n+1):
    print(num)
    soma = soma + num
print(f'A soma de todos os números naturais é: {soma}')
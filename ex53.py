
print("Triângulo de Floyd")
n = 0
while n <= 0:
    n = int(input('Digite um número inteiro positivo: '))
print('\n')
elemento = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(elemento, end=' ')
        elemento = elemento + 1
    print('\n')

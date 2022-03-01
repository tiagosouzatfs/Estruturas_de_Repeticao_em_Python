
soma = 0
for num in range(0, 1001):
    if (num % 3) == 0 or (num % 5) == 0:
        soma = soma + num
        #print(soma)
print(f'O somatório de todos os múltiplos de 3 ou 5 de 0 a 1000, são: {soma}')
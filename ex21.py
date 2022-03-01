
somaPares = 0
multImpares = 1
n1 = int(input('Digite um número para o início do intervalo: '))
n2 = int(input('Digite um número para o fim do intervalo: '))

for n in range(n1, n2+1):
    if (n % 2) == 0:
        somaPares = somaPares + n
        print(n)
    else:
        multImpares = multImpares * n
        print(n)
print(f'A soma dos pares é: {somaPares} e a multiplicação dos ímpares é: {multImpares}')

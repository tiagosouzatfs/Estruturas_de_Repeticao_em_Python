
print('Se quiser sair digite o número 1000 ou menores que 0!')
n = 0
contadorGeral = 0
contadorPar = 0
contadorImpar = 0
while n >= 0:
    n = int(input('Digite um número inteiro: '))
    contadorGeral = contadorGeral + 1
    if n == 1000 or n < 0:
        print('Sair')
        break
    elif (n % 2) == 0:
        print("Número par")
        contadorPar = contadorPar + 1
    else:
        print("Número ímpar")
        contadorImpar = contadorImpar + 1
    
print(f'A quantidade de Números digitados é: {contadorGeral-1}')
print(f'A quantidade de Números pares é: {contadorPar}')
print(f'A quantidade de Números impares é: {contadorImpar}')
print(contadorPar + contadorImpar)
    
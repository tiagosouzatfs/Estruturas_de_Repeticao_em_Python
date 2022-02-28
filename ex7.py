
cont = 0
soma = 0
while cont != 10:
    n = int(input('Digite um inteiro positivo: '))
    if n > 0:
        soma = soma + n
        cont = cont + 1
    else:
        print('Tente novamente, o número digitador não é um inteiro positivo!')
print(soma/cont)
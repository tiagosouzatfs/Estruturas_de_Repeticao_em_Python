# considerando que o 1 não é primo, para os efeitos deste exemplo, porém, vi que alguns altores de livros e pesquisas consideram o 1 primo
a = 0
b = 0
qtdDivisores = 0
contador = 0

while a <= 2 and b <= 3:
    a = int(input('Digite um número inteiro positivo maior ou igual a 2: '))
    b = int(input('Digite um número inteiro positivo maior ou igual a 3: '))

elemento = a
while elemento <= b:
    for i in range(1, elemento+1):
        if (elemento % i) == 0:
            qtdDivisores = qtdDivisores + 1
            
    if qtdDivisores <= 2:
        print(f'{elemento} é primo.')
        contador = contador + 1
        qtdDivisores = 0
    else:
        print(f'{elemento} não é primo.')
        qtdDivisores = 0

    elemento = elemento + 1

print(f'Existem {contador} números primos no intervalo de {a} e {b}')
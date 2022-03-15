# considerando que o 1 não é primo, para os efeitos deste exemplo, porém, vi que alguns altores de livros e pesquisas consideram o 1 primo
n = 0
qtdDivisores = 0
somador = 0
contador = 0
elemento = 2
n = 2000000

while contador < n:
    for i in range(1, elemento+1):
        if (elemento % i) == 0:
            qtdDivisores = qtdDivisores + 1
            
    if qtdDivisores <= 2:
        print(f'{elemento} é primo.')
        somador = somador + elemento
        contador = contador + 1
        qtdDivisores = 0
    else:
        print(f'{elemento} não é primo.')
        qtdDivisores = 0

    elemento = elemento + 1

print(f'A soma dos {n} primeiros números primos é {somador}')    
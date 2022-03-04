
vi = 0
vf = 0
while (vi and vf) <= 0:
    vi = int(input('Digite o valor inicial do intervalo, deverá ser maior ou igual a zero: ')) 
    vf = int(input('Digite o valor final do intervalo, deverá ser maior ou igual a zero: '))

    if vi >= vf:
        print('Intervalo de valores inválido! O valor final deverá ser maior do que o valor inicial.')
        break

somador = 0
for i in range(vi, vf+1):
    if i % 2 != 0:
        somador = somador + i
print(f'A soma dos ímpares nesse intervalor é: {somador}')
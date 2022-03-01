
soma = 0
contador = 0
while True:
    nota = int(input('Digite as notas: '))
    if nota >= 10 and nota <= 20:
        soma = soma + nota
        contador = contador + 1
    else:
        break
print(f'A média das notas é : {soma/contador}')

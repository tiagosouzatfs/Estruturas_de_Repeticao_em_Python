
# Algoritmo do Trono, vamos colocar no trono primeiro o maior número e depois o menor número

tronoMaior = 0
tronoMenor = 0
contador = 0
aux = 0
while contador < 10:
    n = int(input('Digite um número: '))
    if n > tronoMaior:
        tronoMaior = n
    if n < tronoMenor:
        tronoMenor = n
    contador = contador + 1
print(f'O maior número é {tronoMaior}')
print(f'O menor número é {tronoMenor}')
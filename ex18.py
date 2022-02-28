
n = 0
tronoMaior = 0
contador = 0
lista = []
while n <= 0:
    n =int(input('Digite um número inteiro positivo: '))

for num in range(0, n):
    num = int(input('Digite um número qualquer: '))
    lista += [num]
    if num > tronoMaior:
        tronoMaior = num
print(lista)

for maior in range(len(lista)):
    if tronoMaior == lista[maior]:
        contador = contador + 1
print(f'O maior número número é {tronoMaior} e ele foi lido {contador} vezes')

# Utilizei o conceito de lista para resolver este problema

# Forma 01
soma = 0
contador = 0
n = 0
while (contador != 50):
    if (n % 2) == 0:
        print(n)
        soma = soma + n
        contador = contador + 1
    n = n + 1
print(f'A soma dos 50 primeiros números pares é {soma}')
# print(contador) - coloquei esse print para verificar se realmente estava dando certo a contagem das divisões

print('\n')
# Forma 02
soma1 = 0
for n in range(0, 99, 2):
        print(n)
        soma1 = soma1 + n
print(f'A soma dos 50 primeiros números pares é {soma}')

"""Lembrar que para as duas formas estamos começando em 0. Vi outras formas na internet que essa soma dá 2550,
 pois como só vamos até 98 então por isso dá 2450, se fossemos até 100, começando em 2, aí daria 2550."""
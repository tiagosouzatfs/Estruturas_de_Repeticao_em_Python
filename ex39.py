
b = 0
h = 0
while b <= 0:
    b = float(input('Digite o tamanho da base do triângulo: '))

while h <= 0:
    h = float(input('Digite o tamanho da altura do triângulo: '))

a = (b*h)/2
print(f'A área do triângulo é: {a}')
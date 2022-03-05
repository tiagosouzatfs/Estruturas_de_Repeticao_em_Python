
n = 0
while True:
    n = int(input('Digite um valor inteiro positivo: '))
    if n <= 0:
        print('Valor inválido. Saindo do programa!')
        break
    else:
        print(f'Quadrado: {n**2}')
        print(f'Cubo: {n**3}')
        print(f'Raíz quadrada: {n**(1/2)}')
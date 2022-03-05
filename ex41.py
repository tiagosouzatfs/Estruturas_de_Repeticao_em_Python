
r1 = 0
r2 = 0
rtotal = 0
while True:
    r1 = float(input('Digite um valor de resistência r1: '))
    r2 = float(input('Digite um valor de resistência r2: '))
    if (r1 or r2) == 0:
        print('Resistência total igual a zero. Saindo do programa!')
        break
    else:
        rtotal = (r1*r2)/(r1+r2)
        print(f'Resistência Total igual a {rtotal}')

s = 0
numerador = 1
print('S = ', end=' ')
for denominador in range(1, 51):
    s = s + (numerador/denominador)
    if denominador == 50:
        print(f'{numerador}/{denominador} = {s}', end=' ')
    else:
        print(f'{numerador}/{denominador} + ', end=' ')
    numerador = numerador + 2
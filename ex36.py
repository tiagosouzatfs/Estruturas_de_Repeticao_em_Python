
somador_Q = 0
print(f'Soma dos quadrados dos primeiros 100 números natuarais: ' , end=' ')
for i in range(1, 101):
    somador_Q = somador_Q + (i**2)
print(somador_Q)

q_Somador = 0
print(f'Quadrado da soma dos primeiros 100 números natuarais: ' , end=' ')
for i in range(1, 101):
    q_Somador = q_Somador + i
print(q_Somador**2)

print(f'A diferença entre a soma dos quadrados dos 100 primeiros números naturais e o quadrado da soma é: {somador_Q} - {q_Somador} = {(q_Somador**2)-somador_Q}.')
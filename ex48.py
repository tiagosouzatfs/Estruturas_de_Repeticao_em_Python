
# Fn = Fn-1 + Fn-2, com F0 = 0 e F1 = 1
print('Sequência Fibonacci')
fib = 0
fibantes = 0
fibdepois = 1
somador = 0
n = 4000000
print('A sequência Fibonacci de soma de números pares menores de 4 milhões é: 0', end=' ') #coloquei o 0 para deixar o código organizado com relação ao sinal para ficar bonitinho ;)
while True:
    fib = fibantes + fibdepois
    fibantes = fibdepois
    fibdepois = fib
    if somador >= n:
        print(f'= {somador}', end=' ')
        break
    elif (fib % 2) == 0:
        print(f'+ {fib}', end=' ')
        somador = somador + fib
     
    
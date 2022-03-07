
# Fn = Fn-1 + Fn-2, com F0 = 0 e F1 = 1
print('Sequência Fibonacci')
n = 0
while n <= 0:
    n = int(input('Digite um valor inteiro positivo: '))

fib = 0
fibantes = 0
fibdepois = 1
print('A sequência Fibonacci é: 0 1', end=' ')
while True:
    fib = fibantes + fibdepois
    print(f'{fib}', end=' ')
    if fib > n:
        break
    else:
        fibantes = fibdepois
        fibdepois = fib 
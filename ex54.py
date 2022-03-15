# considerando que o 1 não é primo, para os efeitos deste exemplo, porém, vi que alguns altores de livros e pesquisas consideram o 1 primo
n = 0
qtdDivisores = 0
while n <= 1:
    n = int(input('Digite um número inteiro maior do que 1 para continuar ou 0 para sair: '))
    if n == 0:
        break

for i in range(1, n+1):
    if (n % i) == 0:
        qtdDivisores = qtdDivisores + 1

if qtdDivisores <= 2:
    print('O número digitado é primo!')
else:
    print('O número digitado não é primo!')
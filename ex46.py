
from random import randint
from time import sleep

print('Acerte o número no chute, de 1 a 1000.')
print('Gerando número aleatório...')
sleep(2)
n = randint(1, 1001)
print('Pronto, vamos tentar.')
chute = 0
tentativas = 0
while True:
    chute = int(input('Chute um número inteiro positivo: '))
    tentativas = tentativas + 1
    if chute == n and tentativas == 1:
        print('Eita cagada, foi de primeira em!!! kkkkk')
    elif chute > n:
        print('Baixe mais um pouco o valor na próxima tentativa, seu chute está alto.')
    elif chute < n:
        print('Aumente mais um pouco o valor na próxima tentativa, seu chute está baixo.')
    else:
        print('Parabéns, você acertou o número gerado aleatoriamente.')
        print(f'Você tentou {tentativas} vezes, até acertar o número.')
        break

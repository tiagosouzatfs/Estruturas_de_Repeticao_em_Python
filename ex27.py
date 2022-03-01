
# Número harmônico H(n) representa a série harmônica

n = 0
while n <= 0:
    n = int(input('Digite um número inteiro positivo para limitar a série harmônica: '))
print('H(n) = ', end='')
valor = 0
for harmonico in range(1, n+1):
    valor = valor + (1/harmonico)
    if harmonico == n:
        print(f'1/{harmonico} : = {valor}', end='')
    elif harmonico == 1:
        print('1 + ', end='')
    else:
        print(f'1/{harmonico} + ', end='')
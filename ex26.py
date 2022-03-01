# Forma 1
n = int(input('Digite umm número inteiro: '))
while True:
    print(n)
    if (n % 11) == 0 or (n % 13) == 0 or (n % 17) == 0:
        print(f'O primeiro múltiplo é: {n}')
        break
    n = n + 1

# Forma 2
n = int(input('Digite umm número inteiro: '))
while True:
    print(n)
    if (n % 11) == 0:
        print(f'O primeiro múltiplo é: {n}, múltiplo de 11!')
        break
    elif (n % 13) == 0:
        print(f'O primeiro múltiplo é: {n}, múltiplo de 13!')
        break
    elif (n % 17) == 0:
        print(f'O primeiro múltiplo é: {n}, múltiplo de 17!')
        break
    n = n + 1
# Forma 1

for cont in range(1, 4):
    for n in range(1, 101):
        print(f"{n} ", end='')
    print('\n')

# Forma 2

cont = 0
while cont < 3:
    n = 0
    while n < 100:
        n = n + 1
        print(f'{n} ', end='')
    print("\n")
    cont = cont + 1
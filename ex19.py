
n = 0
while n < 100 or n > 999:
    n = int(input("Digite um número entre 100 e 999: "))

n1 = int(n / 100)
n2 = int((n-(n1 * 100))/10)
n3 = (n-(n1 * 100))-(n2 * 10)

print(f'{n1},{n2},{n3}')

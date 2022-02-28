# Forma 1
for num in range(3, 16, 3):
    print(num)
    

# Formas 2
contador_multiplos = 0
n = 0

while contador_multiplos != 5:
    n = n + 1 
    if (n % 3) == 0:
        print(n)
        contador_multiplos = contador_multiplos + 1

# Formas 3 - Uso do Break
contador_multiplos = 0
n = 0
while True:
    n = n + 1 
    if (n % 3) == 0:
        print(n)
        contador_multiplos = contador_multiplos + 1
        if contador_multiplos == 5:
            break
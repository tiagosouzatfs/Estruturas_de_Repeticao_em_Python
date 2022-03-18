
# São palíndromos de dois números
palindromoMaior = 0
for i in range(10, 100):
    for j in range(10, 100):
        num = i * j
        #dividindo o número em quatro partes
        p1 = int(num/1000)
        #print(p1, end=' ')
        p2 = int((num%1000)/100)
        #print(p2, end=' ')
        p3 = int(int((num%1000)%100)/10)
        #print(p3, end=' ')
        p4 = int(int((num%1000)%100)%10)
        #print(p4, end=' ')
        #print('\n')
    #print('\n')
        #testar o palíndromo
        if (p1 == p4) and (p2 == p3):
            palindromo = (p1*1000)+(p2*100)+(p3*10)+p4
            print(f'Palíndromo {p1} {p2} {p3} {p4} formado por {i} * {j}')

            if palindromo > palindromoMaior:
                palindromoMaior = palindromo
        #print()
    #print()

print(f'O maior palíndromo encontrado a partir do produto de dois números de dois digitos foi o {palindromoMaior}')
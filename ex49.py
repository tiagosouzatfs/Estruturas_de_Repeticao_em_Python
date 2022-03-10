
#salarioCarlos = 0
taxaCarlos = 0.02 #2%
taxajoao = 0.05 #5%
contadorMeses = 0
salarioCarlos = float(input('Digite o salário do funcionário Carlos: R$ '))
salarioJoao = ((1/3)*salarioCarlos)
print(f'Então o salário de João é R$ {salarioJoao}')

#Vou usar a função round para arredondar e definir a quantidade de casas decimais em 2
while True:
    contadorMeses = contadorMeses + 1
    salarioCarlos = (taxaCarlos * salarioCarlos) + salarioCarlos 
    salarioJoao = (taxajoao * salarioJoao) + salarioJoao
    print(f'Mês {contadorMeses} o salário de Carlos é R$ {round(salarioCarlos, 2)} e o de João é R$ {round(salarioJoao, 2)}')
    if salarioJoao >=  salarioCarlos:
        print(f'A quantidade de meses para o salário de João iguale ou ultrapasse o de Carlos é {contadorMeses}.')
        break
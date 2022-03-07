
print('Calculadora com opções de menu.')
n1 = 0
n2 = 0
op = 0
menu = 0
while True:
    print('Menu de opções:')
    print('opção: 1 - > somar')
    print('opção: 2 - > subtrair')
    print('opção: 3 - > multiplicação')
    print('opção: 4 - > divisão')
    print('opção: 5 - > sair')
    menu = int(input('Digite uma opção do menu acima: '))
    if menu < 1 or menu > 5:
        print('Opção inválida, voltando para o menu...')
    else:
        if menu == 5:
            print('Saindo da calculadora... até mais.')
            break
        
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        if menu == 1:
            op = n1 + n2
            print(f'A soma de {n1} + {n2} = {op}')
            print('Voltando para o menu...')
        elif menu == 2:
            op = n1 - n2
            print(f'A subtração de {n1} - {n2} = {op}')
            print('Voltando para o menu...')
        elif menu == 3:
            op = n1 * n2
            print(f'A multiplicação de {n1} * {n2} = {op}')
            print('Voltando para o menu...')
        elif menu == 4:
            if n2 != 0:
                op = n1 / n2
                print(f'A divisão de {n1} / {n2} = {op}')
                print('Voltando para o menu...')
            else:
                print('Divisão por zero dá indeterminação, voltando para o menu...')
        
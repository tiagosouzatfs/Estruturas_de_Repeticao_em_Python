
# km/h para m/s -> divide por 3,6
# m/s para km/h -> multiplica por 3,6
# fator de transformação: 3,6

print('Transformação de unidades de velocidade.')
velocidade = 0
menu = 0
print('Escolha um opção para conversão ou sair: 1 - km/h para m/s, 2 - m/s para km/h ou 3 - para sair.')
while True:
    menu = int(input('Opção: '))
    if 1 <= menu <= 3:
        if menu == 1:
            velocidade = float(input('Digite a velocidade a ser convertida de km/h para m/s: '))
            transf = (velocidade / 3.6)
            print(f'A velocidade de {velocidade} km/h equivale a {transf} em m/s.')
        elif menu == 2:
            velocidade = float(input('Digite a velocidade a ser convertida de km/h para m/s: '))
            transf = (velocidade * 3.6)
            print(f'A velocidade de {velocidade} em m/s equivale a {transf} em km/h.')
        else:
            break
    else:
        print('Tente novamente, opção inválida: ')
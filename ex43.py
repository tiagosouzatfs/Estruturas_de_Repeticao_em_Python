
from bdb import Breakpoint


print('Digite 0 para sair.')
idade = 0
contador = 0
somaIdades = 0
while True:
    idade = int(input(f'Digite uma idade qualquer: '))
    if idade < 0:
        print('Digite uma idade válida! Tente novamente.')
    elif idade == 0:
        print('Saindo do programa!')
        break
    else:
        somaIdades = somaIdades + idade
        contador = contador + 1
print(f'A média das idades digitadas é de {somaIdades/contador} anos.') 
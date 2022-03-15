
"""Em 1995 -> 2.000,00
   Em 1996 -> 2.000,00 * 1.5% = 2030"""
anoAtual = int(input('Digite o ano corrente: '))
contadorDeAno = 1996
aumentoAtual = 0.015
salarioReajuste = 2030
while contadorDeAno < anoAtual :
    contadorDeAno = contadorDeAno + 1
    aumentoAtual = aumentoAtual * 2
    print(f'Aumento de {aumentoAtual*100}%')
    salarioReajuste = (salarioReajuste * aumentoAtual) + salarioReajuste
    print(f'No ano corrente de {contadorDeAno} o salário do funcionário reajustado é R$ {round(salarioReajuste, 2)}')
print(f'Passaram-se {anoAtual - 1996} anos desde o primeiro reajuste em 1996.')

#Teste com a lib python datetime com a classe datetime e o objeto now() que recolhe a data atual do pc
from datetime import datetime
"""Em 1995 -> 2.000,00
   Em 1996 -> 2.000,00 * 1.5% = 2030"""
anoAtual = datetime.now()
contadorDeAno = 1996
aumentoAtual = 0.015
salarioReajuste = 2030
while contadorDeAno < anoAtual.year :
    contadorDeAno = contadorDeAno + 1
    aumentoAtual = aumentoAtual * 2
    print(f'Aumento de {aumentoAtual*100}%')
    salarioReajuste = (salarioReajuste * aumentoAtual) + salarioReajuste
    print(f'No ano corrente de {contadorDeAno} o salário do funcionário reajustado é R$ {round(salarioReajuste, 2)}')
print(f'Passaram-se {(anoAtual.year) - 1996} anos desde o primeiro reajuste em 1996.')



qtdNota100 = 0
qtdNota50 = 0
qtdNota20 = 0
qtdNota10 = 0
qtdNota5 = 0
qtdNota2 = 0
qtdNota1 = 0
valorSaque = 0
resto = 0
while True:
    valorSaque = int(input('Digite um valor de saque, inteiro: '))
    if valorSaque <= 0:
        print('Valor incorreto, Digite novamente!!!')
    elif valorSaque >= 100:
        qtdNota100 = int(valorSaque / 100)
        resto = (valorSaque % 100)
        if resto >= 50 and resto < 100:
            qtdNota50 = 1
            resto = resto - 50 # atualiza o resto
        if resto >= 40 and resto <= 49:
            qtdNota20 = 2
            resto = resto - 40
        if resto >= 30 and resto <= 39:
            qtdNota20 = 1
            qtdNota10 = 1
            resto = resto - 30
        if resto >= 20 and resto <= 29:
            qtdNota20 = 1
            resto = resto - 20
        if resto >= 10 and resto <= 19:
            qtdNota10 = 1
            resto = resto - 10
        if resto == 9:
            qtdNota5 = 1
            qtdNota2 = 2
        if resto == 8:
            qtdNota5 = 1
            qtdNota2 = 1
            qtdNota1 = 1
        if resto == 7:
            qtdNota5 = 1
            qtdNota2 = 1
        if resto == 6:
            qtdNota5 = 1
            qtdNota1 = 1
        if resto == 5:
            qtdNota5 = 1
        if resto == 4:
            qtdNota2 = 2
        if resto == 3:
            qtdNota2 = 1
            qtdNota1 = 1
        if resto == 2:
            qtdNota2 = 1
        if resto == 1:
            qtdNota1 = 1

        print(f'{qtdNota100} notas de R$ 100,00 - {qtdNota50} nota de R$ 50,00 - {qtdNota20} notas de R$ 20,00 - {qtdNota10} notas de R$ 10,00 - {qtdNota5} notas de R$ 5,00 - {qtdNota2} notas de R$ 2,00 - e {qtdNota1} notas de R$ 1,00', end=" ")
        break
    else:
        if valorSaque >= 50 and valorSaque < 100:
            qtdNota50 = 1
            valorSaque = valorSaque - 50 # atualiza o valor do saque
        if valorSaque >= 40 and valorSaque <= 49:
            qtdNota20 = 2
            valorSaque = valorSaque - 40
        if valorSaque >= 30 and valorSaque <= 39:
            qtdNota20 = 1
            qtdNota10 = 1
            valorSaque = valorSaque - 30
        if valorSaque >= 20 and valorSaque <= 29:
            qtdNota20 = 1
            valorSaque = valorSaque - 20
        if valorSaque >= 10 and valorSaque <= 19:
            qtdNota10 = 1
            valorSaque = valorSaque - 10
        if valorSaque == 9:
            qtdNota5 = 1
            qtdNota2 = 2
        if valorSaque == 8:
            qtdNota5 = 1
            qtdNota2 = 1
            qtdNota1 = 1
        if valorSaque == 7:
            qtdNota5 = 1
            qtdNota2 = 1
        if valorSaque == 6:
            qtdNota5 = 1
            qtdNota1 = 1
        if valorSaque == 5:
            qtdNota5 = 1
        if valorSaque == 4:
            qtdNota2 = 2
        if valorSaque == 3:
            qtdNota2 = 1
            qtdNota1 = 1
        if valorSaque == 2:
            qtdNota2 = 1
        if valorSaque == 1:
            qtdNota1 = 1

        print(f'{qtdNota50} nota de R$ 50,00 - {qtdNota20} nota(s) de R$ 20,00 - {qtdNota10} nota de R$ 10,00 - {qtdNota5} nota de R$ 5,00 - {qtdNota2} nota(s) de R$ 2,00 - e {qtdNota1} nota de R$ 1,00', end=" ")
        break

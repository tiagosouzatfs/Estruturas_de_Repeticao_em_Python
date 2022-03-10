
contadorAnos = 0
alturaChico = 1.50 #metros
alturaZe = 1.10 #metros
taxaCrescimentoZe = 0.03 #centímetros
taxaCrescimentoChico = 0.02 #centímetros

while True:
    contadorAnos = contadorAnos + 1
    alturaChico = (alturaChico*taxaCrescimentoChico) + alturaChico
    alturaZe = (alturaZe*taxaCrescimentoZe) + alturaZe
    if alturaZe > alturaChico:
        print(f'Zé vai precisar de {contadorAnos} anos para passar da altura de Chico.')
        break
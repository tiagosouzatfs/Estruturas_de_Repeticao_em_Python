
maior = 0
menor = 100000000000000000000 
''' se inicializar com zero da ruim por causa da condição do menor e toda vez que 
executar o programa, o menor será igual a 0'''
n = 0
while True:
    n = int(input('Digite um valor inteiro: '))
    if n < 0:
        print('Valor digitado inválido. Saindo do programa!')
        break
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
print(f'Maior número digitado: {maior}')
print(f'Menor número digitado: {menor}')

somador = 0
contador = 0
maior = 0
menor = 100000000000000000000000000000000000000 # coloquei esse número enorme apenas para referência com a troca do menor consumo, pq se for zero sempre vai ser zero
somadorPares = 0
contadorPares = 0
somadorImpares = 0
contadorImpares = 0
while True:
    n = float(input('Digite um valor maior que zero: '))
    if n < 0:
        print('Número incorreto, digite novamente.')
    elif n == 0:
        print('Saindo.')
        break
    else:
        somador += n
        contador += 1

        if n > maior:
            maior = n
        elif n < menor:
            menor = n

        if (n % 2) == 0:
            somadorPares += n
            contadorPares += 1
        else:
            somadorImpares += n
            contadorImpares += 1

print(f'Soma dos números digitados: {somador}')
print(f'Quantidade de números digitados: {contador}')
print(f"Média dos números digitados: {somador/contador}")
print(f'Maior número digitado: {maior}')
print(f'Menor número digitado: {menor}')
print(f'Média dos números pares digitados: {somadorPares/contadorPares}')
print(f'Média dos números pares digitados: {somadorImpares/contadorImpares}')

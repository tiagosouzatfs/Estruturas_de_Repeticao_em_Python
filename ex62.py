
#Fiz até 100, pq escrever até mil é ralado kkkkkk

contador = 0
numeros = ("um, dois, três, quatro, cinco, seis, sete, oito, nove, dez, onze, doze, treze, quatorze, quinze, dezesseis, dezessete, dezoito, dezenove, vinte, vinte e um, vinte e dois, vinte e três, vinte e quatro, vinte e cinco, vinte e seis, vinte e sete, vinte e oito, vinte e nove, trinta, trinta e um, trinta e dois, trinta e três, trinta e quatro, trinta e cinco, trinta e seis, trinta e sete, trinta e oito, trinta e nove, quarenta, quarenta e um, quarenta e dois, quarenta e três, quarenta e quatro, quarenta e cinco, quarenta e seis, quarenta e sete, quarenta e oito, quarenta e nove, cinquenta, cinquenta e um, cinquenta e dois, cinquenta e três, cinquenta e quatro, cinquenta e cinco,cinquenta e seis, cinquenta e sete, cinquenta e oito, cinquenta e nove, sessenta, sessenta e um, sessenta e dois, sessenta e três, sessenta e quatro, sessenta e cinco, sessenta e seis, sessenta e sete, sessenta e oito, sessenta e nove, setenta, setenta e um, setenta e dois, setenta e três, setenta e quatro, setenta e cinco, setenta e seis, setenta e sete, setenta e oito, setenta e nove, oitenta, oitenta e um, oitenta e dois, oitenta e três, oitenta e quatro, oitenta e cinco, oitenta e seis, oitenta e sete, oitenta e oito, oitenta e nove, noventa, noventa e um, noventa e dois, noventa e três, noventa e quatro, noventa e cinco, noventa e seis, noventa e sete, noventa e oito, noventa e nove, cem")
letra = list(numeros) # a função list() vai transformar a string dos números em um vetor em que cada caracter vira uma posição no vetor
print(letra)
for i in range(len(letra)):
    if letra[i] != " " and letra[i] != ",":
        contador += 1

print(f"Foram utilizadas {contador} letras para contar as palavras dos números por extenso de 1 a 100")
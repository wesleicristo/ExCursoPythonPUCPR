# Elabore um algoritmo que leia um conjunto de 10 números inteiros.
# Mostre então qual o valor da soma e da média aritmética do conjunto.

contador = 1
valor = 0
soma = 0

while contador <= 10 :
    valor = (int(input(f"{contador}° valor: ")))
    soma += valor
    contador += 1
print(f"A soma dos valores: {soma}")
print(f"A média dos valores: {soma/10}")
# Uma empresa de câmbio permite a compra de dólares, libras e euros. Elabore um algoritmo
# que leia o código da moeda que o cliente quer comprar e qual o montante que ele quer
# adquirir nessa moeda. Mostre então quanto ele deverá pagar em reais para concretizar
# a operação. Além da cotação, a empresa cobra uma comissão de 5% (quando o valor for menor
# que R$ 1.000), ou de 3% (quando maior ou igual a R$1.000). Considere o câmbio do dia.

print(f"Digite o valor desejado comprar (Dolar: USD | Libra: GBP | Euro: EUR)")
print(f"Ex: USD99.999")

valorCompra = input("Digite o valor desejado:")

taxaMaior = 3       # taxa de comissão quando o valor for maior que o alvo
taxaMenor = 5       # taxa de comissão quando o valor for menor que o alvo
alvoTaxa = 1000     # valor alvo para mudança da taxa de comissão
cambioDolar = 4.93
cambioLibra = 6.04
cambioEuro = 5.25
valorCobrado = 0.0

if valorCompra[:3].upper() == "USD":
    valorCalculo = float(valorCompra[3:])

    if valorCalculo >= alvoTaxa :
        valorCalculo += valorCalculo * (taxaMaior / 100)
    else:
        valorCalculo += valorCalculo * (taxaMenor / 100)

    valorCobrado = valorCalculo * cambioDolar
    print(f"Valor cobrado por USD{float(valorCompra[3:]):.2f} é BRL{valorCobrado:.2f}")
elif valorCompra[:3].upper() == "GBP":
    valorCalculo = float(valorCompra[3:])

    if valorCalculo >= alvoTaxa :
        valorCalculo += valorCalculo * (taxaMaior / 100)
    else:
        valorCalculo += valorCalculo * (taxaMenor / 100)

    valorCobrado = float(valorCompra[3:]) * cambioLibra
    print(f"Valor cobrado por GBP{float(valorCompra[3:]):.2f} é BRL{valorCobrado:.2f}")
elif valorCompra[:3].upper() == "EUR":
    valorCalculo = float(valorCompra[3:])

    if valorCalculo >= alvoTaxa :
        valorCalculo += valorCalculo * (taxaMaior / 100)
    else:
        valorCalculo += valorCalculo * (taxaMenor / 100)

    valorCobrado = float(valorCompra[3:]) * cambioEuro
    print(f"Valor cobrado por EUR{float(valorCompra[3:]):.2f} é BRL{valorCobrado:.2f}")
else:
    print(f"Digite o codigo correto da moeda!")
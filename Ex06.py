# Imprima uma tabela de conversão de polegadas para centímetros,
# cuja escala vai de 1 a 20 polegadas. A conversão entre estas duas unidades é dada por:
# centímetro = polegada × 2,54

contador = 1

while contador <= 20 :
    print(f"{contador} = {contador * 2.54}")
    contador += 1
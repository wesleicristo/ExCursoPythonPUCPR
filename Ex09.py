# Imprima os números múltiplos de 3 entre li (limite inicial) e lf (limite final).
# Os valores inteiros de li e lf devem ser informados pelo usuário e não
# pertencem ao intervalo, ou seja, intervalo aberto.

limiteInicial = int(input("Digite o valor Inicial: "))
limiteFinal = int(input("Digite o valor Final: "))
contador = limiteInicial + 1

while contador < limiteFinal :
    if contador % 3 == 0 :
        print(f"{contador}")
    contador += 1
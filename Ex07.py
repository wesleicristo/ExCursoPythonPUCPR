# Considerando que 1 milha vale exatamente 1.609,344 metros,
# imprima uma tabela de conversão de metros (m) para milhas (mi.),
# de 20 km até 160 km, de 10 em 10 quilômetros.

km = 20

while km <= 160 :
    print(f"{km*1000} mt = {km/1.609344:.4f} mi")
    km += 10
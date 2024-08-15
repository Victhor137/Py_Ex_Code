x = []
contador = 0
while contador < 10:
    valor = int(input("Digite um valor: "))
    if 9 < valor < 21:
        x.append(valor)
        contador = contador+1
    else:
        contador = contador+1
print(x)
calc = x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7] + x[8] + x[9]
print(calc)

# Input_1
valor1 = float(input("Digite o primeiro valor (não pode ser zero): "))

# Bitree_1
while valor1 == 0:
    print("O primeiro valor não pode ser zero. Tente novamente.")
    valor1 = float(input("Digite o primeiro valor (não pode ser zero): "))

# Input_2
valor2 = float(input("Digite o segundo valor (não pode ser zero): "))

# Bitree_2
while valor2 == 0:
    print("O segundo valor não pode ser zero. Tente novamente.")
    valor2 = float(input("Digite o segundo valor (não pode ser zero): "))

# Calc+print
resultado = valor1 / valor2
print(f"A média de {valor1} e {valor2} é: {resultado:.2f}")

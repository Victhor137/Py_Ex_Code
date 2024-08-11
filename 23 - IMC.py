# Ler dados de entrada
nome = input("Digite o nome: ")
altura = float(input("Digite a altura (em metros): "))
sexo = input("Digite o sexo (M para masculino, F para feminino): ").upper()

# Calcular o peso ideal
if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = None

# Exibir o resultado
if peso_ideal is not None:
    print(f"{nome}, o seu peso ideal é: {peso_ideal:.2f} kg")
else:
    print("Sexo inválido. Use 'M' para masculino ou 'F' para feminino.")

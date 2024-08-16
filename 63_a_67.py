# 65 a 67 - escreva dois numeros e calcule todos os valores entre eles incluindo os numeros.
def prog_arit(a,b):
    return (b - a + 1) * (a + b) // 2
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
resultado = prog_arit(a,b)
print(resultado)

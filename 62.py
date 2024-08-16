# Inicializando listas para armazenar os dados dos alunos
alunos = []
num_alunos = int(input("Digite o número de alunos: "))

# Loop para coletar informações dos alunos
for _ in range(num_alunos):
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a nota da 1ª Av: "))
    nota2 = float(input("Digite a nota da 2ª Av: "))
    nota3 = float(input("Digite a nota da 3ª Av: "))
    
    media = (nota1 + nota2 + nota3) / 3
    
    # Adicionando as informações do aluno em um dicionário
    aluno = {
        'nome': nome,
        'nota1': nota1,
        'nota2': nota2,
        'nota3': nota3,
        'media': media
    }
    
    # Adicionando o dicionário à lista de alunos
    alunos.append(aluno)

# Exibindo os resultados
print(f"\nNúmero de alunos cadastrados: {len(alunos)}")
print("\nDados dos alunos:")
for aluno in alunos:
    print(f"Nome: {aluno['nome']}")
    print(f"Notas: {aluno['nota1']}, {aluno['nota2']}, {aluno['nota3']}")
    print(f"Média: {aluno['media']:.2f}\n")

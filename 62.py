aluno_nome = []
aluno_nota1 = []
aluno_nota2 = []
aluno_nota3 = []
aluno_media = []
quantidade_alunos = len(aluno_nome)
alunos = int(input("Digite o número de alunos: "))
contador = quantidade_alunos
while alunos > contador:
    nome = str(input("Digite o nome do aluno: "))
    nota1 = float(input("Digite a nota da 1ºAv: "))
    nota2 = float(input("Digite a nota da 2ºAv: "))
    nota3 = float(input("Digite a nota da 3ºAv: "))
    media = (nota1 + nota2 + nota3)/3
    aluno_nome.append(nome)
    aluno_nota1.append(nota1)
    aluno_nota2.append(nota2)
    aluno_nota3.append(nota3)
    aluno_media.append(media)
    contador = contador+1
quantidade_alunos = len(aluno_nome)
print(quantidade_alunos)
print(aluno_nome)
print(aluno_media)

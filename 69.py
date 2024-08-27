estoque = []
valor = []
def adicionar_produto():
  produto = input("Digite o nome do produto: ")
  estoque.append(produto)
  valor = int(input("Digite o valor do produto: "))
  valor.append(valor)
  print("Produto adicionado com sucesso!")
  mais_produtos = input("Deseja adicionar mais produtos? (s/n)")
  if mais_produtos == "s":
    adicionar_produto()
  else:
    print("Estoque atualizado com sucesso!")

print(" --- Estoque de Produtos ---")
print("1 - Cadastrar produto")
print("2 - Listar produtos")
print("3 - Remover produto")
produto = int(input("Digite a opção desejada: "))
if produto == 1:
  adicionar_produto()

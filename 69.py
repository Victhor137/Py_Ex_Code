estoque = []
valor = []

#def para adicionar produto no estoque
def adicionar_produto():
  produto = input("Digite o nome do produto: ")
  estoque.append(produto)
  preco = float(input("Digite o valor do produto: "))
  valor.append(preco)
  print("Produto adicionado com sucesso!")
  mais_produtos = input("Deseja adicionar mais produtos? (s/n)")
  if mais_produtos == "s":
    adicionar_produto()
  else:
    print("Estoque atualizado com sucesso!")
#def para listar produto no estoque
def listar_produto():
  if not estoque:
    print("Nenhum produto cadastro.")
  else:
    for i in range(len(estoque)):
      print(f"{estoque[i]} - R${valor[i]:.2f}")

#def remover produto
def remover_produto():
  produto = str(input("Digite o nome do produto: "))
  if produto in estoque:
    index = estoque.index(produto)
    estoque.pop(index)
    valor.pop(index)
    print(f"O produto '{produto}' foi removido com sucesso!")

#inicio da interface
while True:
  print(" --- Estoque de Produtos ---")
  print("1 - Cadastrar produto")
  print("2 - Listar produtos")
  print("3 - Remover produto")
  produto = int(input("Digite a opção desejada: "))
  if produto == 1:
    adicionar_produto()
  elif produto == 2:
    listar_produto()
  elif produto == 3:
    remover_produto()

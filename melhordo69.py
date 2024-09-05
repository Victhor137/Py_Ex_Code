import tkinter as tk
from tkinter import messagebox
estoque = []
valor = []

#def para adicionar produto no estoque
def adicionar_produto():
  produto = entry_produto.get()
  try:
    preco = float(entry_valor.get())
  except ValueError:
    messagebox.showerror("Erro, o valor deve ser um número.")
    return

  estoque.append(produto)
  valor.append(preco)
  messagebox.showinfo("Sucesso, produto adicionado com sucesso!")

  entry_produto.delete(0, tk.END)
  entry_produto.delete(0, tk.END)

#def para listar produto no estoque
def listar_produto():
  text_area.delete(1.0, tk.END)
  if not estoque:
    text_area.insert(tk.END, "Nenhum produto cadastrado.\n")
  else:
    for i in range(len(estoque)):
      text_area.insert(tk.END, f"{estoque[i]} - R${valor[i]:.2f}\n")

#def remover produto
def remover_produto():
  produto = entry_produto.get()
  if produto in estoque:
    index = estoque.index(produto)
    estoque.pop(index)
    valor.pop(index)
    messagebox.showinfo("Sucesso!",f"O produto '{produto}' foi removido com sucesso!")
  else:
    messagebox.showerror("Erro", "Produto não encontrado.")
  entry_produto.delete(0, tk.END)

#def para criar a interface gráfica
def criar_widgets():

  #Cria campo de entrada para ler o nome do produto
  global entry_produto, entry_valor, text_area
  tk.Label(root, text="Nome do Produto: ").pack()
  entry_produto = tk.Entry(root)
  entry_produto.pack()

  #Cria um campo de entrara para ler o valor do produto
  tk.Label(root, text="Valor do Produto: ").pack()
  entry_valor = tk.Entry(root)
  entry_valor.pack()

  #Botões da interface
  tk.Button(root, text="Adicionar Produto", command=adicionar_produto).pack()
  tk.Button(root, text="Listar Produtos", command=listar_produto).pack()
  tk.Button(root, text="Remover Produto", command=remover_produto).pack()

  #area do texto para mostrar a lista de produtos
  text_area = tk.Text(root, height=10, width=50)
  text_area.pack()

#inicio da interface
"""while True:
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
"""
# a partir de agora estou montando a interface gráfica
root = tk.Tk()
root.title("Estoque de Produto")
criar_widgets()
root.mainloop()

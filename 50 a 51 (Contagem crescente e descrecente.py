escolha = str.upper(input("Escolha se a contagem vai ser crescente ou descrecente digitando (C para crescente e D para descrecente: "))
if escolha == "C":
    x = 1
    while x<=10:
        print(x)
        x = x+1
elif escolha == "D":
    x = 10
    while x>0:
        print(x)
        x = x-1

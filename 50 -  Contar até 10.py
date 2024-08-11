#Código com erro, precisa depurar
# input
run = int(input("Digite um valor de 0 a 10: "))
#bitree
while True:
    if run == 0:
        run = int(input("Zero é sacanagem, digita outro aí: "))
    elif run > 10:
         run = int(input("O valor é alto demais, digite um valor menor: "))
    elif run <10:
        run = int(input("Algo tá errado: "))
while run > 0:
    print(run)
    run = run - 1

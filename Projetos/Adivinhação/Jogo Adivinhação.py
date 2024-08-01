import random
escolha = 1
while escolha == 1:
    print("         ADIVINHAÇÃO!")
    print("")
    while True:
        try:
            enter = input("     Pressione Enter para começar!")
            if not enter == "":
                print("     Tecla inválida!")
            else:
                break
        except ValueError:
            print("Erro!")

    print("")
    print("     Tente Acertar o número!")
    numero_aleatorio = random.randint(1, 100)
    while True:
        try:
            chute = int(input(""))
            if chute > numero_aleatorio:
                print("O número é menor!")
            elif chute < numero_aleatorio:
                print("O número é maior!")
            elif chute == numero_aleatorio:
                print("Parabéns! O número é: ", numero_aleatorio)
                print("Gostaria de continuar? [s para continuar/n para sair]")
                continuar = input("")
                if continuar == "n":
                    print("Obrigado por jogar!")
                    break
        except ValueError:


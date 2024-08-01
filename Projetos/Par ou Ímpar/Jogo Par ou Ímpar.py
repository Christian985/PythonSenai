import random
print("             PAR OU ÍMPAR!")
print("")
while True:
    try:
        enter = input("     Pressione Enter para começar!")
        if enter != "":
            print("     Tecla inválida!")
        else:
            break
    except ValueError:
        print("Erro!")

numero_aleatorio = random.randint(0, 100)
print("Escolha Par(p) ou Impar(i)!")
escolha = input("")

while True:
    try:
        if escolha == "p":
            print(numero_aleatorio)
        elif numero_aleatorio == 0:
            print("Você venceu!", numero_aleatorio)
            print("Gostaria de continuar? [S/N]")
            continuar = input("")
            if continuar == "n":
                print("Obrigado por jogar!")
                break
        elif numero_aleatorio == 2:
            print("Você venceu!", numero_aleatorio)
            print("Gostaria de continuar? [S/N]")
            continuar = input("")
            if continuar == "n":
                print("Obrigado por jogar!")
                break
        elif numero_aleatorio == 4:
            print("Você venceu!", numero_aleatorio)
            print("Gostaria de continuar? [S/N]")
            continuar = input("")
            if continuar == "n":
                print("Obrigado por jogar!")
                break
        elif numero_aleatorio == 6:
            print("Você venceu!", numero_aleatorio)
            print("Gostaria de continuar? [S/N]")
            continuar = input("")
            if continuar == "n":
                print("Obrigado por jogar!")
                break
        elif numero_aleatorio == 8:
            print("Você venceu!", numero_aleatorio)
            print("Gostaria de continuar? [S/N]")
            continuar = input("")
            if continuar == "n":
                print("Obrigado por jogar!")
                break
        elif numero_aleatorio == 10:
            print("Você venceu!", numero_aleatorio)
            print("Gostaria de continuar? [S/N]")
            continuar = input("")
            if continuar == "n":
                print("Obrigado por jogar!")
                break
        if escolha == "i":
            break
    except ValueError:
        print("Erro!")
while True:
    try:
        if escolha == "i":
            print(numero_aleatorio)
        if not escolha == "i":
            print(" Tecla inválidada!")
        elif numero_aleatorio == 1:
            print("Você venceu!", numero_aleatorio)
            print("Gostaria de continuar? [S/N]")
            continuar = input("")
        elif numero_aleatorio == 3:
            print("Você venceu!", numero_aleatorio)
            print("Gostaria de continuar? [S/N]")
            continuar = input("")
        elif numero_aleatorio == 5:
            print("Você venceu!", numero_aleatorio)
            print("Gostaria de continuar? [S/N]")
            continuar = input("")
        elif numero_aleatorio == 7:
            print("Você venceu!", numero_aleatorio)
            print("Gostaria de continuar? [S/N]")
            continuar = input("")
        elif numero_aleatorio == 9:
            print("Você venceu!", numero_aleatorio)
            print("Gostaria de continuar? [S/N]")
            continuar = input("")
        else:
            break
    except ValueError:
        print("Erro!")

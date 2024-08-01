import random
numero_aleatorio = random.randint(1, 100)
# Menu
print("        Adivinhação!")
print("")
print(" Pressione Enter para começar!")
enter = input("")
if enter != "":
    print("       Tecla inválida!")

print("Tente acertar o número!")
print("")
while True:
    try:
        # Sistema
        chute = int(input(""))
        if chute > numero_aleatorio:
            print("O número é menor!")
        elif chute < numero_aleatorio:
            print("O número é maior!")
        elif chute == numero_aleatorio:
            print("Parabéns! O número é: ", numero_aleatorio)
            print("")
            # Finalização e jogar novamente
            print("Gostaria de jogar novamente? [S/N]")
            continuar = input("")
            if continuar == "n":
                print("Obrigado por jogar!")
                break
            elif continuar == "s":
                print("Boa sorte!")
    except ValueError:
        print("Erro!")

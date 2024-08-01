import random
# menu.
print("             Par ou ímpar!")
print("")

numero_aleatorio = random.randint(0, 10)

# Sistema.
while True:
    try:
        # Escolha.
        print("     Escolha Par[p] ou Impar[i]!")
        escolha = input("")
        if escolha == "p" or escolha == "i":
            print("Escolha um número de 0 a 10!")
            numero = int(input(""))
            # Aleatoriedade
            resul = numero + numero_aleatorio
            # Par
            if resul % 2 == 0:
                if escolha == "p":
                    print("O resultado é: ", resul, "Você venceu!")
                else:
                    print("O resultado é: ", resul, "Você perdeu!")
            # Ímpar
            else:
                if escolha == "i":
                    print("O resultado é: ", resul, "Você venceu!")
                else:
                    print("O resultado é: ", resul, "Você perdeu!")
                print("")
            print("Gostaria de jogar novamente? [S/N]")
            continuar = input("")
            if continuar == "n":
                print("Obrigado por jogar!")
                break
            elif continuar == "s":
                print("Boa sorte!")
    except ValueError:
        print("Erro!")

# Enquanto a condição for verdadeira.
while True:
    # O try vai tentar executar esse bloco de código
    try:
        idade = int(input("Digite sua idade: "))

        # O if verifica se a idade é válida
        if idade < 0 or idade > 100:
            print("idade inválida")
            # O break sai do while
            break
        else:
            print("Idade: ", idade)
    except ValueError:
        # Caso der erro, executa aqui
        print("Digite sua idade em número. Ex: 26")

    # Print("Idade: ", idade)

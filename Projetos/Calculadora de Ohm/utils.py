# tensão = v = r * i
# corrente = r = v / i
# resistência = i = v / r
# resistor = resistência = (tensão da fonte (ts) - tensão do LED (tl) / corrente do LED (cl)
def calculadora():
    print("                        Guia de Siglas")
    print("tensão = v = r * i")
    print("corrente = r = v / i")
    print("resistência = i = v / r")
    print("resistor = i = tensão da fonte (ts) - tensão do LED (tl) ) / corrente do LED (cl)")
    alter = input("insira o calculo com suas siglas (exemplo: v = r * i): ")
    tensao = int(input("(Caso essa não tenha sido sua escolha digite 0) Digite o valor da tensão: "))
    corrente = int(input("(Caso essa não tenha sido sua escolha digite 0) Digite o valor da corrente: "))
    resistencia = int(input("(Caso essa não tenha sido sua escolha digite 0) Digite o valor da resistência: "))
    resistor = int(input("(Caso essa não tenha sido sua escolha digite 0) Digite o valor do resistor: "))

    if alter == "v = r * i":
        print(tensao)

    elif alter == "r = v / i":
        print(corrente)

    elif alter == "i = v / r":
        print(resistencia)

    elif alter == "i = (ts - tl) / cl":
        print(resistor)

# Código antigo acima
# Código novo abaixo


def calculadora_2():
    while True:
        try:
            print("Tensão = 1")
            print("Corrente = 2")
            print("Resistência = 3")
            print("Resistor = 4")
            print("Sair = 0")
            escolha = int(input("--> "))
            if escolha == 0:
                print("Saindo do programa")
                break
            else:
                return escolha
        except ValueError:
            print("Erro")

def tensao():
    print("Tensão")
    ten_1 = float(input("Corrente: "))
    ten_2 = float(input("Resistência: "))
    ten_resul = ten_1 * ten_2
    print("A tensão é: ", ten_resul)


def corrente():
    print("Corrente")
    corr_1 = float(input("Tensão: "))
    corr_2 = float(input("Resistência: "))
    corr_resul = corr_1 / corr_2
    print("A tensão é: ", corr_resul)


def resistencia():
    print("Resistência")
    res_1 = float(input("Tensão: "))
    res_2 = float(input("Corrente: "))
    res_resul = res_1 / res_2
    print("A tensão é: ", res_resul)


def resistor():
    print("Resistor")
    resi_1 = float(input("Tensão da fonte: "))
    resi_2 = float(input("Tensão do LED: "))
    resi_3 = float(input("Corrente do LED: "))
    resi_cal = resi_1 - resi_2
    resi_resul = resi_cal / resi_3
    print("A tensão é: ", resi_resul)


opcao = calculadora_2()

if opcao == 0:
    print("Saindo do programa")
elif opcao == 1:
    tensao()
elif opcao == 2:
    corrente()
elif opcao == 3:
    resistencia()
elif opcao == 4:
    resistor()

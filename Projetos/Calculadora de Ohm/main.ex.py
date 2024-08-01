print("Calculadora de Ohm")
print("")
print("1 - Resistência")
print("2 - Tensão")
print("3 - Corrente")
print("4 - Resistência necessária para um resistor")
print("")

opcao = int(input("Digite o número da escolha desejada: "))


if opcao == 1:
    print("Resistência")
    print("")
    tensao = float(input("Digite a tensão em volts: "))
    corrente = float(input("Digite a corrente em amperes: "))

    resistencia = tensao / corrente

    print(f"A resistência é de {resistencia} ")


elif opcao == 2:
    print("Tensão")
    print("")
    resistencia = float(input("Digite a resistência em ohms: "))
    corrente = float(input("Digite a corrente em amperes: "))

    tensao = resistencia * corrente

    print(f"A tensão é de {tensao} volts")

elif opcao == 3:
    print("Corrente")
    print("")

    tensao = float(input("Digite a tensão em volts: "))
    resistencia = float(input("Digite a resistência em ohms: "))

    corrente = tensao / resistencia

elif opcao == 4:
    print("Resistencia resistor\n")
    print("")
    tensao_fonte = float(input("Digite a tensão em volts: "))
    tensao_dispositivo = float(input("Digite a tensão do dispositivo em volts: "))
    corrente = float(input("Digite a corrente em amperes: "))

    resistencia_resistor = (tensao_fonte - tensao_dispositivo) / corrente

    print(f"A resistência necessária desse resistor é de {resistencia_resistor} ")
else:
    print("opção inválida")

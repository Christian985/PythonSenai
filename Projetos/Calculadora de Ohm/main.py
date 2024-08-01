# tensao = v = r * i
# corrente = r = v / i
# resistencia = i = v / r
# resistor = resistencia = (tensão da fonte (ts) - tensão do LED (tl) / corrente do LED (cl)

print("                        Guia de Siglas")
print("tensao = v = r * i")
print("corrente = r = v / i")
print("resistencia = i = v / r")
print("resistor = i = tensão da fonte (ts) - tensão do LED (tl) ) / corrente do LED (cl)")
alter = input("insira o calculo com suas siglas (exemplo: v = r * i): ")
tensao = int(input("(Caso essa não tenha sido sua escolha digite 0) Digite o valor da tensao: "))
corrente = int(input("(Caso essa não tenha sido sua escolha digite 0) Digite o valor da corrente: "))
resistencia = int(input("(Caso essa não tenha sido sua escolha digite 0) Digite o valor da resistencia: "))
resistor = int(input("(Caso essa não tenha sido sua escolha digite 0) Digite o valor do resistor: "))

if alter == "v = r * i":
    print(tensao)

elif alter == "r = v / i":
    print(corrente)

elif alter == "i = v / r":
    print(resistencia)

elif alter == "i = (ts - tl) / cl":
    print(resistor)

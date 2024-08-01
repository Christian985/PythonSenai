# Adição
# Subtração
# Divisão
# Multiplicação

def menu():
    print("----------------------------------------------")
    print("             Menu")
    print("Use 1 para calcular com adição ")
    print("Use 2 para calcular com subtração ")
    print("Use 3 para calcular com divisão ")
    print("Use 4 para calcular com multiplicação ")
    print("----------------------------------------------")

def calculadora():
    escolha = int(input("-->"))
    calculo = int(input(""))
    calculo2 = int(input(""))
    if escolha == 1:
        resul_mais = calculo + calculo2
        print("O resultado é: ", resul_mais)
    elif escolha == 2:
        resul_mais = calculo - calculo2
        print("O resultado é: ", resul_mais)
    elif escolha == 3:
        resul_mais = calculo / calculo2
        print("O resultado é: ", resul_mais)
    elif escolha == 4:
        resul_mais = calculo * calculo2
        print("O resultado é: ", resul_mais)
    else:
        print("Escolha invalida")


menu()

calculadora()

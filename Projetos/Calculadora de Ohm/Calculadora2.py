def calculadora():
    print("Calculadora")
    while True:
        try:
            print("1 - Soma")
            print("2 - Subtração")
            print("3 - Multiplicação")
            print("4 - Divisão")
            print("0 - Sair")
            escolha = int(input(""))
            if escolha == 0:
                print("Saindo do programa")
                break
            elif escolha == 1:
                soma_1 = float(input("Primeiro calculo: "))
                soma_2 = float(input("Segundo calculo: "))
                resul_soma = soma_1 + soma_2
                print("Resultado: ", resul_soma)
            elif escolha == 2:
                sub_1 = float(input("Primeiro calculo: "))
                sub_2 = float(input("Segundo calculo: "))
                resul_sub = sub_1 - sub_2
                print("Resultado: ", resul_sub)
            elif escolha == 3:
                multi_1 = float(input("Primeiro calculo: "))
                multi_2 = float(input("Segundo calculo: "))
                resul_multi = multi_1 * multi_2
                print("Resultado: ", resul_multi)
            elif escolha == 4:
                divi_1 = float(input("Primeiro calculo: "))
                divi_2 = float(input("Segundo calculo: "))
                resul_divi = divi_1 / divi_2
                print("Resultado: ", resul_divi)
        except ValueError:
            print("Escolha os números apresentados acima!")


calculadora()

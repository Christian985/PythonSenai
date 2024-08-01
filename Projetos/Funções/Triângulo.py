def triangulo():
    lado1 = int(input("Digite o lado 1: "))
    lado2 = int(input("Digite o lado 2: "))
    lado3 = int(input("Digite o lado 3: "))
    if lado1 == lado2 and lado1 == lado3 or lado2 == lado1 and lado2 == lado3 or lado3 == lado1 and lado3 == lado2:
        print("O triângulo é equilatero")
    elif lado1 != lado2 and lado1 == lado3 or lado2 != lado1 and lado2 == lado3 or lado3 != lado1 and lado3 == lado2:
        print("O triângulo é isóceles")
    elif lado1 != lado2 and lado3 != lado2:
        print("O triângulo é escaleno")
    else:
        print("Erro")

triangulo()

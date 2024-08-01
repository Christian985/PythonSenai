numero1 = int(input("Insira um número: "))
numero2 = int(input("Insira outro número adicional: "))
if numero1 > numero2:
    print(f"o número {numero1} é maior que o {numero2}")
elif numero2 > numero1:
    print(f"O número {numero2} é maior que o {numero1}")
elif numero1 == numero2:
    print(f"Ambos os números {numero1} e {numero2} são iguais")
else:
    print("Erro!")

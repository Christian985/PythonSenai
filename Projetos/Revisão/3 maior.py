numero1 = int(input("Insira um número: "))
numero2 = int(input("Insira outro número adicional: "))
numero3 = int(input("Insira outro número adicional: "))
if numero1 > numero2 and numero1 > numero3:
    print(f"O número {numero1} é maior!")
elif numero2 > numero1 and numero2 > numero3:
    print(f"O número {numero2} é maior!")
elif numero3 > numero2 and numero3 > numero1:
    print(f"O número {numero3} é maior!")
else:
    print("Erro")

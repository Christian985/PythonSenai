# Faixa de Renda Anual Bruta            Alíquota
# Até R$ 56.072,00                      0%
# De R$ 56.072,00 a R$ 238.532,00       7,50%
# De R$ 238.532,00 a R$ 522.400,00      15%
# De R$ 522.400,00 a R$ 987.600,00      22,50%
# Acima de R$ 987.600,00                27,50%
print("Insira sua renda anual bruta (Use '.' para indicar centavos caso necessário)")
while True:
    try:
        renda_bruta = int(input("R$ "))
        if renda_bruta <= 0:
            print("Erro!")
            break
        elif renda_bruta <= 56072.00:
            print(f"Nenhum desconto atribuído a seu imposto de renda. R$ {renda_bruta}")
            break
        elif renda_bruta >= 56072.00 and renda_bruta <= 238532.00:
            renda_7 = renda_bruta * 0.075
            print("Você recebeu um desconto de 7,50%!", f"Sua renda foi {renda_7}!")
            break
        elif renda_bruta >= 238532.00 and renda_bruta <= 522400.00:
            renda_8 = renda_bruta * 0.15
            print("Você recebeu um desconto do imposto de renda em 15%!", f"Sua renda foi {renda_8}!")
            break
        elif renda_bruta >= 522400.00 and renda_bruta <= 987600.00:
            renda_9 = renda_bruta * 0.225
            print("Você recebeu um desconto do imposto de renda em 22,50%!", f"Sua renda foi {renda_9}!")
            break
        elif renda_bruta >= 987600.00:
            renda_10 = renda_bruta * 0.275
            print("Você recebeu um desconto do imposto de renda em 27,50%!", f"Sua renda foi {renda_10}!")
            break
    except ValueError:
        print("Erro! Use números!")

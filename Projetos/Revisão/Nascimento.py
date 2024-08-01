ano = int(input("Digite o ano de nascimento: "))
idade = 2024 - ano
if idade > 100 or idade < 0:
    print("Erro!")
elif idade < 18 or idade == 1:
    print(f"Você é de menor. Sua idade é {idade} anos.")
elif idade >= 18 or idade == 100:
    print(f"Você é de maior. Sua idade é {idade} anos")
else:
    print("Erro!")

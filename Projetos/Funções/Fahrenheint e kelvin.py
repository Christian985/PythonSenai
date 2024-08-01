# Convensor de temperatura: Crie uma função que receba um valor de temperatura em graus
# Celsius como parâmetro e retorne o valor convertido para Fahrenheint e Kelvin.
#                       Conversão de Escala Termométricas
#           De -> para                  |            Fórmula
#       Celsius -> Kelvin               |            K = C + 273
#     Celsius -> Fahrenheint            |          F = C x 1,8 + 32

print("     Escreva o valor em graus celsius")
escolha = float(input(""))
def kelvin_():
    kelvin = escolha + 273.15
    print(f"{kelvin}K")

def fahrenheit_():
    fahrenheit = escolha * 1.8 + 32
    print(f"{fahrenheit}F")

kelvin_()
fahrenheit_()
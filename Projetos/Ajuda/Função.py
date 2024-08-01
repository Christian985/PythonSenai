from datetime import datetime


def menu_calculadora():
    print("Calculadora")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")


def ola_nome(nome):
    print(f"Ola {nome}")


def return_ola_nome(nome):
    return f"Ola {nome}"


def exibir_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    print("Sua idade é ", idade, "anos")


def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade


def solicita_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite seu ano de nascimento: "))
            if ano_nascimento > datetime.now().year:
                print("Digite um ano válido")
            else:
                return ano_nascimento
        except ValueError:
            print("Digite um valor inteiro. Ex: 1997")

# Exibe o menu da calculadora
menu_calculadora()

# Exibe o print com "Ola Lucas"
ola_nome("Lucas")

# Retorna o texto com o "Ola Lucas"
print("Boa tarde return", return_ola_nome("Lucas"))

# O código funciona mesmo quando vazio
ola_nome("")

exibir_idade(1997)
# Ou
print(calcular_idade(ano_nascimento=1997))

ano_nascimento = solicita_ano_nascimento()

exibir_idade(ano_nascimento=ano_nascimento)

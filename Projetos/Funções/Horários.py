from datetime import datetime
# 1 - Mensagem automática: Crie uma função que receba um nome como
# parâmetro e escreva uma saudação baseada na hora atual

def solicita_nome():
    nome = input("Qual o seu nome? ")
    return nome

def solicita_saudacao(tempo):
    if tempo >= 0 and tempo <= 5:
        saudacao = "Boa madrugada!"
    elif tempo > 5 and tempo <= 11:
        saudacao = "Bom dia!"
    elif tempo > 11 and tempo <= 18:
        saudacao = "Boa tarde!"
    elif tempo > 18 and tempo <= 23:
        saudacao = "Boa noite!"

    return saudacao

tempo = datetime.now().hour
usuario = solicita_nome()
print(solicita_saudacao(tempo), usuario)



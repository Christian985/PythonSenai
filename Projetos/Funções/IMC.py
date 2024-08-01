def imc():
    peso = float(input("Insira seu peso: "))
    altura = float(input("Insira sua altura: "))
    imc_altura = altura * altura
    imc = peso / imc_altura
    if imc < 18.5:
        print("Abaixo do peso!", imc)
    elif 18.5 == imc or imc <= 25:
        print("Peso ideal!", imc)
    elif 25 > imc or imc <= 30:
        print("Sobrepeso!", imc)
    elif 30 > imc or imc <= 40:
        print("Obesidade!", imc)
    elif imc > 40:
        print("Obesidade morbida!", imc)
    else:
        print("Erro")


imc()

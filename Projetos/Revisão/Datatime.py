import datetime
tempo = datetime.datetime.now()
print("Seja bem vindo!")
print("Ano:", tempo.year)
print("Mês:", tempo.month, tempo.strftime("- %B"))
print("Dia:", tempo.day, tempo.strftime("- %A"))
print(f"Hora: {tempo.hour}:{tempo.minute}")
print(tempo.strftime("%d/%m/%Y"))

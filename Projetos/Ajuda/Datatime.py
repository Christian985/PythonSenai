import datetime

# alimentar variável com tempo "agora"
tempo = datetime.datetime.now()

# exemplos aplicação
print(f'"datetime.now()": {tempo}')


# tratar datas
print(f'"Ano "tempo.year": {tempo.year}-Mes:{tempo.month}-Dia:{tempo.day}')

# tempo.strftime para configurar modo de exibição
print(tempo.strftime('%A  %d,%B %Y %I:%M %p'))

# tratar horas
print(f'Hora "tempo.hour":{tempo.hour} |Minuto:{tempo.minute}segundo:{tempo.second}"')

# %A = semana
# %d = dia
# %B = mês
# %Y = ano
# %I = horas
# %M = minutos
# %p = segundos

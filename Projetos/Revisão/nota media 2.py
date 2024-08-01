print("Coloque suas notas abaixo")
nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))
nota_soma = nota1 + nota2
nota_media = nota_soma / 2
if nota_media == 70 and 100:
    print(f"Aprovado! Sua nota foi {nota_media}")
elif nota_media <= 70:
    print(f"Reprovado! Sua nota foi {nota_media}")
else:
    print("Erro!")

# -*- coding: utf-8 -*-

def media():
    args = input().split(' ')
    args = [float(x) for x in args]

    mediaPonderada = (args[0]*2 + args[1]*3 + args[2]*4 + args[3]) / 10
    if mediaPonderada >= 7:
        mediaPonderada = round(mediaPonderada, 1)
        aprovado = "Aluno aprovado."
        return f"Media: {mediaPonderada}\n{aprovado}"
    elif mediaPonderada < 5:
        aprovado = "Aluno reprovado."
        mediaPonderada = round(mediaPonderada, 1)
        return f"Media: {mediaPonderada}\n{aprovado}"
    else:
        aprovado = "Aluno em exame."
        exame = float(input())
        novaMedia = round(((mediaPonderada+exame) / 2), 1)
        if novaMedia >= 5:
            result = "Aluno aprovado."
        else:
            result = "Aluno reprovado."
        return f"Media: {mediaPonderada}\n{aprovado}\nNota do exame: {exame}\n{result}\nMedia final: {novaMedia}"


print(media())

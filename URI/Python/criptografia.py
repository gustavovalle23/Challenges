# -*- coding: utf-8 -*-


def criptografiaPython(frase):
    texto = list(frase)
    texto1 = []

    for letra in texto:
        if letra.isalpha():
            texto1.append(chr(ord(letra)+3))
        else:
            texto1.append(letra)

    texto1 = texto1[::-1]

    texto = []

    texto1 = ''.join(texto1)

    for letra in texto1[:len(texto1)//2:]:
        texto.append(letra)

    for letra in texto1[len(texto1)//2::]:
        texto.append(chr(ord(letra)-1))

    print(''.join(texto))


if __name__ == "__main__":
    number = int(input())
    frases = []
    for _ in range(number):
        frases.append(input())

    for item in frases:
        criptografiaPython(item)

# -*- coding: utf-8 -*-
from math import sqrt


def pares_impares_positivos_negativos(numbers):
    pares = 0
    impares = 0

    positivos = 0
    negativos = 0

    for item in numbers:
        if item % 2 == 0:
            pares += 1
        else:
            impares += 1
        if item > 0:
            positivos += 1
        elif item < 0:
            negativos += 1
    
    print(f'{pares} valor(es) par(es)\n{impares} valor(es) impar(es)')
    print(f'{positivos} valor(es) positivo(s)\n{negativos} valor(es) negativo(s)')


    

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    numbers = [a, b, c, d, e]

    pares_impares_positivos_negativos(numbers)

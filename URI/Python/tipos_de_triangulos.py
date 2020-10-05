# -*- coding: utf-8 -*-
from math import sqrt


def tipos_de_triangulos(a: float, b: float, c: float):

    if a >= (b+c):
        print('NAO FORMA TRIANGULO')
        return
    if (b**2 + c**2) == a**2:
        print('TRIANGULO RETANGULO')
    if (a**2) > (b**2 + c**2):
        print('TRIANGULO OBTUSANGULO')
    if a**2 < (b**2 + c**2):
        print('TRIANGULO ACUTANGULO')
    if a == b and b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or b == c or a == c:
        print('TRIANGULO ISOSCELES')

if __name__ == "__main__":
    a, b, c = input().split()
    a = float(a)
    b = float(b)
    c = float(c)
    numbers = [a, b, c]
    numbers.sort(reverse=True)

    tipos_de_triangulos(numbers[0], numbers[1], numbers[2])

# -*- coding: utf-8 -*-
def triangulo(a: str, b: str, c: str) -> str:
    a = float(a)
    b = float(b)
    c = float(c)

    if (a < b + c) and (b < a + c) and (c < a + b):
        return "Perimetro = {:.1f}" .format(a+b+c)
    return "Area = {:.1f}" .format(c * (a+b) / 2)


if __name__ == "__main__":
    a, b, c = input().split()
    print(triangulo(a, b, c))

# -*- coding: utf-8 -*-


def coordenadas(x: float, y: float) -> str:
    if x == 0:
        if y == 0:
            return 'Origem'
        if y != 0:
            return 'Eixo Y'
    if y == 0:
        if x != 0:
            return 'Eixo X'
    if x > 0:
        if y > 0:
            return 'Q1'
        if y < 0:
            return 'Q4'
    if x < 0:
        if y > 0:
            return 'Q2'
        if y < 0:
            return 'Q3'


if __name__ == "__main__":
    x, y = input().split(' ')
    print(coordenadas(float(x), float(y)))

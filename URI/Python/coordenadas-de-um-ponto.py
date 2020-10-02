# -*- coding: utf-8 -*-


def coordenadas(x: float, y: float) -> str:
    if x > 0:
        if y > 0:
            return 'Q1'
        return 'Q4'
    elif x < 0:
        if y < 0:
            return 'Q3'
        return 'Q2'
    return 'Origem'


if __name__ == "__main__":
    x, y = input('Coordenadas: ').split(' ')
    print(coordenadas(float(x), float(y)))

# -*- coding: utf-8 -*-
import copy


def sort_simples(listaOriginal):
    listaOriginal[0] = int(listaOriginal[0])
    listaOriginal[1] = int(listaOriginal[1])
    listaOriginal[2] = int(listaOriginal[2])

    listaOrdenada = copy.deepcopy(listaOriginal)
    listaOrdenada.sort()

    [print(num) for num in listaOrdenada]
    print()
    [print(num) for num in listaOriginal]


if __name__ == "__main__":
    listaOriginal = input().split()
    sort_simples(listaOriginal)

# -*- coding: utf-8 -*-

from datetime import timedelta


def tempo_de_jogo():
    inicio, fim = input().split()
    inicio = int(inicio)
    fim = int(fim)

    diferenca = timedelta(hours=fim) - timedelta(hours=inicio)

    if inicio == fim:
        print(f'O JOGO DUROU 24 HORA(S)')
        return

    print(f'O JOGO DUROU {int(diferenca.seconds/60/60)} HORA(S)')


if __name__ == "__main__":
    tempo_de_jogo()

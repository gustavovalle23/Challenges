# -*- coding: utf-8 -*-


def tempo_de_jogo_com_minutos():
    x = input().split()
    hora_inicial, minuto, hora_final, minuto_final = x

    hora_inicial = int(x[0])
    minuto = int(x[1])
    hora_final = int(x[2])
    minuto_final = int(x[3])

    if hora_inicial < hora_final:
        h = hora_final - hora_inicial
        if minuto < minuto_final:
            m = minuto_final - minuto
        if minuto > minuto_final:
            h = h - 1
            m = (60 - minuto) + minuto_final
        if minuto == minuto_final:
            m = 0
    if hora_inicial > hora_final:
        h = (24 - hora_inicial) + hora_final
        if minuto < minuto_final:
            m = minuto_final - minuto
        if minuto > minuto_final:
            h = h - 1
            m = (60 - minuto) + minuto_final
        if minuto == minuto_final:
            m = 0
    if hora_inicial == hora_final:
        if minuto < minuto_final:
            m = minuto_final - minuto
            h = 0
        if minuto > minuto_final:
            m = (60 - minuto) + minuto_final
            h = 23
        if minuto == minuto_final:
            h = 24
            m = 0
    
    print(f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)')


if __name__ == "__main__":
    tempo_de_jogo_com_minutos()

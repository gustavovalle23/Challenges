# -*- coding: utf-8 -*-


animal1 = input()
animal2 = input()
animal3 = input()

saida = ''

if animal1 == 'vertebrado':
    if animal2 == 'ave':
        if animal3 == 'carnivoro':
            saida = 'aguia'
        elif animal3 == 'onivoro':
            saida = 'pomba'
    elif animal2 == 'mamifero':
        if animal3 == 'onivoro':
            saida = 'homem'
        elif animal3 == 'herbivoro':
            saida = 'vaca'
elif animal1 == 'invertebrado':
    if animal2 == 'inseto':
        if animal3 == 'hematofago':
            saida = 'pulga'
        elif animal3 == 'herbivoro':
            saida = 'lagarta'
    elif animal2 == 'anelideo':
        if animal3 == 'hematofago':
            saida = 'sanguessuga'
        elif animal3 == 'onivoro':
            saida = 'minhoca'

print(saida)
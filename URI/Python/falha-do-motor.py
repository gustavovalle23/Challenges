# -*- coding: utf-8 -*-

numero = int(input())
numeros = input()
n = numeros.split()
n2 = []
aux = 0
for item in n:
    n2.append(int(item))
for item in range(numero-1):
    if (n2[item] > n2[item+1]):
        print(item+2)
        aux = aux+1
        break
if(aux == 0):
    print(0)

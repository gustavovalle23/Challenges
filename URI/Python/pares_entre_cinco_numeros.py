# -*- coding: utf-8 -*-

array = []
for i in range(5):
    n = int(input())
    array.append(int(n))

pares = 0
for i in range(5):
    if array[i] % 2 == 0:
        pares += 1
print(pares, "valores pares") 

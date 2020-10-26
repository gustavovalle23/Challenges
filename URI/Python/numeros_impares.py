# -*- coding: utf-8 -*-

impares = []
num = int(input())

for i in range(1, 1000, 2):
    if num >= i:
        print(i)
    else:
        break

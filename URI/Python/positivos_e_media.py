# -*- coding: utf-8 -*-

positivos = 0
soma = 0

for i in range(6):
    num = float(input())
    if num > 0:
        positivos += 1
        soma += num

print(f'{positivos} valores positivos')
print('%.1f' % (soma/positivos))
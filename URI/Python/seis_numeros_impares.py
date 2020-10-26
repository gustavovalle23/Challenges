# -*- coding: utf-8 -*-

number = int(input())
flag = 0

for num in range(number, number+13):
    if num % 2 == 1:
        print(num)
        flag += 1
    if flag == 6:
        break
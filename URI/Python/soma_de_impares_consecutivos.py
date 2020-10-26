# -*- coding: utf-8 -*-


x = float(input())
y = float(input())

a = 0
flag = max(x, y)
flag1 = min(x, y) + 1

while flag1 < flag:
    if flag1 % 2 == 1:
        a += flag1
    flag1 += 1

print(int(a))

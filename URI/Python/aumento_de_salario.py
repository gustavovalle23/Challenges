# -*- coding: utf-8 -*-

salario = float(input())
novo = 0
reajuste = 0

if salario >= 0 and salario <= 400:
    novo = (salario*0.15) + salario
    reajuste = 15
elif salario >= 400.01 and salario <= 800:
    novo = (salario*0.12) + salario
    reajuste = 12
elif salario >= 800.01 and salario <= 1200:
    novo = (salario*0.10) + salario
    reajuste = 10
elif salario >= 1200.01 and salario <= 2000:
    novo = (salario*0.07) + salario
    reajuste = 7
elif salario > 2000:
    novo = (salario*0.04) + salario
    reajuste = 4


print('Novo salario: %.2f' %(novo))
print('Reajuste ganho: %.2f' %(novo - salario))
print(f'Em percentual: {reajuste} %')
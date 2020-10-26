# -*- coding: utf-8 -*-

salario = float(input())


if salario < 2000:
    print('Isento')
elif salario >= 2000.01 and salario <= 3000:
    imposto = (salario - 2000) * 0.08
    print('R$ %.2f' % (imposto))


elif salario >= 3000.01 and salario <= 4500:
    salario = salario - 2000
    salarioNew = salario - 1000
    imposto = (salario - salarioNew) * 0.08
    imposto += salarioNew * 0.18

    print('R$ %.2f' % (imposto))

elif salario > 4500:
    imposto1 = 350
    imposto = (salario - 4500) * 0.28
    imposto += imposto1

    print('R$ %.2f' % (imposto))

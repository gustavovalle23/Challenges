# -*- coding: utf-8 -*-


""" 
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.
"""

num = float(input(''))
print('NOTAS:')


n100 = num // 100
print(f'{int(n100)} nota(s) de R$ 100.00')
num = num - (n100*100) # rest
n50 = num // 50
print(f'{int(n50)} nota(s) de R$ 50.00')
num = num - (n50*50) # rest
n20 = num // 20
print(f'{int(n20)} nota(s) de R$ 20.00')
num = num - (n20*20) # rest
n10 = num // 10
print(f'{int(n20)} nota(s) de R$ 10.00')
num = num - (n10*10) # rest
n5 = num // 5
print(f'{int(n5)} nota(s) de R$ 5.00')
num = num - (n5 * 5) # rest
n2 = num // 2
print(f'{int(n2)} nota(s) de R$ 2.00')
num = num - (n2 * 2) # rest


print('MOEDAS:')

num = num*100

real = num // 100
print(f'{int(real)} moeda(s) de R$ 1.00')
num = num - (real*100) # rest
n50 = num // 50
print(f'{int(n50)} moeda(s) de R$ 0.50')
num = num - (n50*50) # rest
n25 = num // 25
print(f'{int(n25)} moeda(s) de R$ 0.25')
num = num - (n25 * 25) # rest
n10 = num // 10
print(f'{int(n10)} moeda(s) de R$ 0.10')
num = num - (n10 * 10) # rest
n05 = num // 5
print(f'{int(n05)} moeda(s) de R$ 0.05')
num = num - (n05 * 5) # rest
print(f'{int(num)} moeda(s) de R$ 0.01')

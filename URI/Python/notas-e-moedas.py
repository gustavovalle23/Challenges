# -*- coding: utf-8 -*-

if __name__ == '__main__':

    def minMoedas(num):
        print('NOTAS:')

        flag = num // 100
        print(f'{int(flag)} nota(s) de R$ 100.00')
        num = num - (flag*100)  # rest
        flag = num // 50
        print(f'{int(flag)} nota(s) de R$ 50.00')
        num = num - (flag*50)  # rest
        flag = num // 20
        print(f'{int(flag)} nota(s) de R$ 20.00')
        num = num - (flag*20)  # rest
        flag = num // 10
        print(f'{int(flag)} nota(s) de R$ 10.00')
        num = num - (flag*10)  # rest
        flag = num // 5
        print(f'{int(flag)} nota(s) de R$ 5.00')
        num = num - (flag * 5)  # rest
        flag = num // 2
        print(f'{int(flag)} nota(s) de R$ 2.00')
        num = num - (flag * 2)  # rest

        print('MOEDAS:')

        num = num*100

        flag = num // 100
        print(f'{int(flag)} moeda(s) de R$ 1.00')
        num = num - (flag*100)  # rest
        flag = num // 50
        print(f'{int(flag)} moeda(s) de R$ 0.50')
        num = num - (flag*50)  # rest
        flag = num // 25
        print(f'{int(flag)} moeda(s) de R$ 0.25')
        num = num - (flag * 25)  # rest
        flag = num // 10
        print(f'{int(flag)} moeda(s) de R$ 0.10')
        num = num - (flag * 10)  # rest
        flag = num // 5
        print(f'{int(flag)} moeda(s) de R$ 0.05')
        num = num - (flag * 5)  # rest
        print(f'{int(num)} moeda(s) de R$ 0.01')


    num = float(input(''))

    minMoedas(num)